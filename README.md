# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-11-16 01:19 UTC

New CVEs published between 2026-11-16 00:20 UTC and 2026-11-16 01:19 UTC.

[Full CSV](data/new-cves-2026-11-16T01-19-02-284964Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-11-16 01:17:18 | [CVE-2026-129491](https://nvd.nist.gov/vuln/detail/CVE-2026-129491) | Medium | 5.1 | Qbian61 forum-java commit 20f7e68 through commit 63152c4 contains a stored cross-site scripting vulnerability that allo… |
| 2026-11-16 01:17:19 | [CVE-2026-129492](https://nvd.nist.gov/vuln/detail/CVE-2026-129492) | Medium | 5.3 | Bolo (bolo-solo) 1.7 through 2.6.4 contains a stored cross-site scripting vulnerability that allows unauthenticated att… |
| 2026-11-16 01:17:19 | [CVE-2026-129493](https://nvd.nist.gov/vuln/detail/CVE-2026-129493) | High | 8.7 | Bolo (bolo-solo) 1.7 through 2.6.4 contains an information disclosure vulnerability that allows unauthenticated attacke… |
| 2026-11-16 01:17:20 | [CVE-2026-129494](https://nvd.nist.gov/vuln/detail/CVE-2026-129494) | High | 8.7 | CloudPaste 1.1.0 through 1.9.1 contains an information disclosure vulnerability that allows unauthenticated attackers t… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
