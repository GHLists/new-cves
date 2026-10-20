# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-20 02:18 UTC

New CVEs published between 2026-10-20 01:19 UTC and 2026-10-20 02:18 UTC.

[Full CSV](data/new-cves-2026-10-20T02-18-58-268629Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-10-20 02:17:08 | [CVE-2026-102438](https://nvd.nist.gov/vuln/detail/CVE-2026-102438) | High | 8.5 | An uncontrolled search path element vulnerability in ASUS Armoury Crate allows local users to execute arbitrary code wi… |
| 2026-10-20 02:17:08 | [CVE-2026-105299](https://nvd.nist.gov/vuln/detail/CVE-2026-105299) | High | 8.7 | Summary Before version 0.9.0, the HTTP/1 upstream path in pingora-proxy passed the downstream request through upstream_… |
| 2026-10-20 02:17:11 | [CVE-2026-17518](https://nvd.nist.gov/vuln/detail/CVE-2026-17518) | High | 8.2 | Buffer Copy without Checking Size of Input in certain ASUS router models allows an adjacent authenticated user to corru… |
| 2026-10-20 02:17:11 | [CVE-2026-75753](https://nvd.nist.gov/vuln/detail/CVE-2026-75753) | Medium | 5.3 | Missing Authentication for a Critical Function in certain ASUS routers allows an unauthorized nearby user to send speci… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
