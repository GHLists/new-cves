# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-24 05:20 UTC

New CVEs published between 2026-10-24 04:20 UTC and 2026-10-24 05:20 UTC.

[Full CSV](data/new-cves-2026-10-24T05-20-54-098081Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-10-24 05:17:04 | [CVE-2026-115806](https://nvd.nist.gov/vuln/detail/CVE-2026-115806) | Critical | 9.8 | The Prime Mover – Backup and Migration plugin for WordPress is vulnerable to PHP Object Injection in all versions up to… |
| 2026-10-24 05:17:06 | [CVE-2026-115807](https://nvd.nist.gov/vuln/detail/CVE-2026-115807) | High | 7.1 | The User Profile Builder – Beautiful User Registration Forms, User Profiles & User Role Editor plugin for WordPress is… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
