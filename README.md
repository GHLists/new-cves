# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-11-16 16:18 UTC

New CVEs published between 2026-11-16 15:19 UTC and 2026-11-16 16:18 UTC.

[Full CSV](data/new-cves-2026-11-16T16-18-25-465623Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-11-16 16:17:53 | [CVE-2026-28731](https://nvd.nist.gov/vuln/detail/CVE-2026-28731) | Medium | 6.5 | A memory corruption vulnerability exists in VideoLAN VLC 3.0.23. A specially crafted Interplay MVE file can trigger a c… |
| 2026-11-16 16:17:53 | [CVE-2026-32789](https://nvd.nist.gov/vuln/detail/CVE-2026-32789) | Medium | 4.3 | An out-of-bounds read vulnerability exists in VideoLAN VLC 3.0.23. By using a specially crafted NUV file, an attacker c… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
