# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-15 20:20 UTC

New CVEs published between 2026-10-15 19:19 UTC and 2026-10-15 20:20 UTC.

[Full CSV](data/new-cves-2026-10-15T20-20-04-774095Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-10-15 20:17:05 | [CVE-2026-103910](https://nvd.nist.gov/vuln/detail/CVE-2026-103910) |  |  | Rejected reason: ** REJECT ** DO NOT USE THIS CANDIDATE NUMBER. ConsultIDs: CVE-2026-101335. Reason: This candidate is… |
| 2026-10-15 20:17:06 | [CVE-2026-104198](https://nvd.nist.gov/vuln/detail/CVE-2026-104198) | Medium | 5.3 | ZoneMinder is a free, open source closed-circuit television software application. In versions 1.34.0 through 1.36.38, t… |
| 2026-10-15 20:17:06 | [CVE-2026-106700](https://nvd.nist.gov/vuln/detail/CVE-2026-106700) | High | 8.8 | ELADMIN v2.7 and earlier contains an improper access control vulnerability in the user-management endpoint PUT /api/use… |
| 2026-10-15 20:17:06 | [CVE-2026-106708](https://nvd.nist.gov/vuln/detail/CVE-2026-106708) | High | 8.8 | XXL-JOB 3.5.0-SNAPSHOT and earlier contains a Cross-Site Request Forgery (CSRF) vulnerability in the user management co… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
