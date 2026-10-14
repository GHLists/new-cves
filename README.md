# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-14 01:20 UTC

New CVEs published between 2026-10-14 00:19 UTC and 2026-10-14 01:20 UTC.

[Full CSV](data/new-cves-2026-10-14T01-20-35-873531Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-10-14 01:17:06 | [CVE-2026-108473](https://nvd.nist.gov/vuln/detail/CVE-2026-108473) | High | 8.7 | Multiple Kasa devices contain an improper authentication vulnerability in the local device-management protocol. An unau… |
| 2026-10-14 01:17:06 | [CVE-2026-110359](https://nvd.nist.gov/vuln/detail/CVE-2026-110359) | High | 7.8 | Hyland Desktop Host for Windows before 25.1.1 is vulnerable to local privilege escalation. This is caused by a privileg… |
| 2026-10-14 01:17:06 | [CVE-2026-110385](https://nvd.nist.gov/vuln/detail/CVE-2026-110385) | High | 8.7 | A remote code execution vulnerability in ONLYOFFICE Document Server versions before10.0.0 allows an authenticated attac… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
