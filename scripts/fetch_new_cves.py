#!/usr/bin/env python3
"""Fetch CVEs published between the previous list and now.

New vulnerabilities are read from the NVD API 2.0, which supports filtering by
publication date. The end of the last list is stored in the manifest so the
next run resumes where the previous one stopped. The unauthenticated API is
rate limited to 5 requests per 30 seconds, so pagination is throttled.
"""

import argparse
import csv
import datetime as dt
import http.client
import json
import os
import subprocess
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

NVD_URL = "https://services.nvd.nist.gov/rest/json/cves/2.0"
DEFAULT_USER_AGENT = "new-cves/1.0 (https://github.com/GHLists/new-cves)"

RESULTS_PER_PAGE = 2000
MAX_PAGES = 10
RATE_LIMIT_SECONDS = 6.0
DESCRIPTION_LIMIT = 300
METRIC_PREFERENCE = ("cvssMetricV40", "cvssMetricV31", "cvssMetricV30", "cvssMetricV2")
CSV_HEADER = (
    "published_at",
    "cve",
    "severity",
    "score",
    "status",
    "cwe",
    "references",
    "description",
)

TRANSIENT_ERRORS = (
    urllib.error.URLError,
    TimeoutError,
    json.JSONDecodeError,
    http.client.HTTPException,
    OSError,
)


def iso(moment):
    moment = moment.astimezone(dt.timezone.utc)
    if moment.microsecond:
        fraction = f"{moment.microsecond:06d}".rstrip("0")
        return moment.strftime("%Y-%m-%dT%H:%M:%S") + f".{fraction}Z"
    return moment.strftime("%Y-%m-%dT%H:%M:%SZ")


def parse_timestamp(value):
    text = str(value).strip()
    if text.endswith("Z"):
        text = text[:-1] + "+00:00"
    moment = dt.datetime.fromisoformat(text)
    if moment.tzinfo is None:
        moment = moment.replace(tzinfo=dt.timezone.utc)
    return moment.astimezone(dt.timezone.utc)


def timestamp_filename(moment):
    moment = moment.astimezone(dt.timezone.utc)
    stamp = moment.strftime("%Y-%m-%dT%H-%M-%S")
    if moment.microsecond:
        stamp += "-" + f"{moment.microsecond:06d}".rstrip("0")
    return stamp + "Z"


def nvd_timestamp(moment):
    moment = moment.astimezone(dt.timezone.utc)
    millis = moment.microsecond // 1000
    return moment.strftime("%Y-%m-%dT%H:%M:%S.") + f"{millis:03d}Z"


def fetch_json(url, user_agent, retries=3, backoff=10.0):
    last_error = None
    for attempt in range(1, retries + 1):
        request = urllib.request.Request(
            url,
            headers={"User-Agent": user_agent, "Accept": "application/json"},
        )
        try:
            with urllib.request.urlopen(request, timeout=60) as response:
                return json.load(response)
        except TRANSIENT_ERRORS as error:
            last_error = error
        if attempt < retries:
            print(f"attempt {attempt} failed ({last_error}), retrying", file=sys.stderr)
            time.sleep(backoff * attempt)
    raise RuntimeError(f"failed to fetch {url}: {last_error}")


def fetch_window(since, until, user_agent, retries, max_pages):
    """Return every CVE published between ``since`` and ``until``."""
    entries = []
    seen = set()
    start = 0
    for _ in range(max_pages):
        params = urllib.parse.urlencode(
            {
                "pubStartDate": nvd_timestamp(since),
                "pubEndDate": nvd_timestamp(until),
                "resultsPerPage": RESULTS_PER_PAGE,
                "startIndex": start,
            }
        )
        payload = fetch_json(f"{NVD_URL}?{params}", user_agent, retries=retries)
        if not isinstance(payload, dict) or not isinstance(
            payload.get("vulnerabilities"), list
        ):
            raise RuntimeError("NVD response has an invalid vulnerabilities field")
        batch = payload["vulnerabilities"]
        for item in batch:
            cve = item.get("cve") if isinstance(item, dict) else None
            if not isinstance(cve, dict):
                continue
            cve_id = cve.get("id")
            if not isinstance(cve_id, str) or not cve_id or cve_id in seen:
                continue
            seen.add(cve_id)
            entries.append(cve)
        total = payload.get("totalResults")
        start += len(batch)
        if not batch or not isinstance(total, int) or start >= total:
            return entries, True
        time.sleep(RATE_LIMIT_SECONDS)
    return entries, False


def english_description(cve):
    for description in cve.get("descriptions") or []:
        if isinstance(description, dict) and description.get("lang") == "en":
            return str(description.get("value") or "")
    return ""


def severity_and_score(metrics):
    for key in METRIC_PREFERENCE:
        for metric in metrics.get(key) or []:
            if not isinstance(metric, dict):
                continue
            data = metric.get("cvssData") or {}
            score = data.get("baseScore")
            if score is None:
                continue
            label = data.get("baseSeverity") or metric.get("baseSeverity") or ""
            return str(label), score
    return "", ""


def cwe_ids(cve):
    ids = []
    for weakness in cve.get("weaknesses") or []:
        for description in (weakness or {}).get("description") or []:
            value = (description or {}).get("value")
            if isinstance(value, str) and value and value not in ids:
                ids.append(value)
    return "; ".join(ids)


def clean_text(value, limit=DESCRIPTION_LIMIT):
    text = " ".join(str(value or "").split())
    if len(text) > limit:
        text = text[: limit - 1].rstrip() + "\u2026"
    return text


def build_row(cve, published):
    severity, score = severity_and_score(cve.get("metrics") or {})
    references = cve.get("references")
    return {
        "published_at": iso(published),
        "cve": cve.get("id") or "",
        "severity": severity,
        "score": score,
        "status": cve.get("vulnStatus") or "",
        "cwe": cwe_ids(cve),
        "references": len(references) if isinstance(references, list) else "",
        "description": clean_text(english_description(cve)),
    }


def write_csv(path, rows):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(f".{path.name}.tmp")
    with temporary.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=CSV_HEADER)
        writer.writeheader()
        writer.writerows(rows)
    os.replace(temporary, path)


def read_manifest_text(path):
    """Read the manifest from disk, or fall back to the committed copy.

    The workflow checks out only ``scripts`` from the repository, so the
    manifest can be missing from the working tree even though it is committed.
    """
    manifest_path = Path(path)
    try:
        return manifest_path.read_text(encoding="utf-8")
    except OSError:
        pass
    try:
        result = subprocess.run(
            ["git", "show", f"HEAD:{manifest_path.as_posix()}"],
            capture_output=True,
            text=True,
            check=True,
        )
    except (OSError, subprocess.CalledProcessError):
        return None
    return result.stdout


def load_manifest(path):
    text = read_manifest_text(path)
    if text is None:
        return {}
    try:
        data = json.loads(text)
    except json.JSONDecodeError as error:
        raise RuntimeError(f"manifest {path} is not valid JSON") from error
    if not isinstance(data, dict):
        raise RuntimeError(f"manifest {path} must contain a JSON object")
    version = data.get("state_version", 1)
    if version != 1:
        raise RuntimeError(f"manifest {path} has an unsupported state version")
    return data


def save_manifest(path, manifest):
    manifest_path = Path(path)
    manifest_path.parent.mkdir(parents=True, exist_ok=True)
    temporary = manifest_path.with_name(f".{manifest_path.name}.tmp")
    text = json.dumps(manifest, indent=2, sort_keys=True, ensure_ascii=False) + "\n"
    temporary.write_text(text, encoding="utf-8")
    os.replace(temporary, manifest_path)


def parse_args(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--since",
        help="UTC start timestamp as ISO 8601 (default: end of the last list)",
    )
    parser.add_argument(
        "--until",
        help="UTC end timestamp as ISO 8601 (default: now)",
    )
    parser.add_argument(
        "--max-pages",
        type=int,
        default=MAX_PAGES,
        help=f"maximum API pages to walk (default: {MAX_PAGES})",
    )
    parser.add_argument("--output-dir", default="data")
    parser.add_argument("--manifest", default="latest.json")
    parser.add_argument("--user-agent", default=DEFAULT_USER_AGENT)
    parser.add_argument("--retries", type=int, default=3)
    parser.add_argument(
        "--lookback-hours",
        type=float,
        default=1.0,
        help="window length when no previous list exists (default: 1)",
    )
    return parser.parse_args(argv)


def main(argv=None):
    args = parse_args(argv)
    now = dt.datetime.now(dt.timezone.utc)
    until = parse_timestamp(args.until) if args.until else now
    manifest = load_manifest(args.manifest)

    if args.since:
        since = parse_timestamp(args.since)
        if "window" in manifest:
            stored_window = parse_timestamp(manifest["window"])
            if since < stored_window:
                raise RuntimeError(
                    "backfill would move the window backwards; "
                    f"the manifest window is {iso(stored_window)}"
                )
    elif "window" in manifest:
        since = parse_timestamp(manifest["window"])
    else:
        since = until - dt.timedelta(hours=args.lookback_hours)

    if since >= until:
        print(f"nothing to do ({iso(since)} >= {iso(until)})", file=sys.stderr)
        return 0

    entries, exhausted = fetch_window(
        since, until, args.user_agent, args.retries, max(1, args.max_pages)
    )

    rows = []
    skipped = 0
    for cve in entries:
        try:
            published = parse_timestamp(cve["published"])
        except (KeyError, TypeError, ValueError):
            skipped += 1
            continue
        if published <= since or published > until:
            continue
        rows.append(build_row(cve, published))
    rows.sort(key=lambda row: row["published_at"])
    if skipped:
        print(f"skipped {skipped} malformed CVEs", file=sys.stderr)

    manifest["window"] = iso(until)
    manifest["source_truncated"] = not exhausted
    if rows:
        output = Path(args.output_dir) / f"new-cves-{timestamp_filename(until)}.csv"
        write_csv(output, rows)
        manifest["list"] = {
            "path": output.as_posix(),
            "from": iso(since),
            "to": iso(until),
            "count": len(rows),
        }
        print(
            f"wrote {len(rows)} CVEs published between {iso(since)} "
            f"and {iso(until)} to {output}"
        )
    else:
        print(f"no new CVEs between {iso(since)} and {iso(until)}")
    if not exhausted:
        print(
            "NVD page limit reached; the window may be incomplete",
            file=sys.stderr,
        )
    save_manifest(args.manifest, manifest)
    return 0


if __name__ == "__main__":
    sys.exit(main())
