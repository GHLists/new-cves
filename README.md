# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-14 12:19 UTC

New CVEs published between 2026-10-14 11:21 UTC and 2026-10-14 12:19 UTC.

[Full CSV](data/new-cves-2026-10-14T12-19-45-36548Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-10-14 12:17:17 | [CVE-2026-73797](https://nvd.nist.gov/vuln/detail/CVE-2026-73797) | Medium | 5.3 | A security vulnerability in HPE NonStop TSQLFIL may cause address space corruption when a specific API is called. |
| 2026-10-14 12:17:17 | [CVE-2026-73798](https://nvd.nist.gov/vuln/detail/CVE-2026-73798) | High | 8.2 | A security vulnerability in HPE NonStop DNS 9.2.3 Non Secure Version could cause a Denial of Service. |
| 2026-10-14 12:17:18 | [CVE-2026-76655](https://nvd.nist.gov/vuln/detail/CVE-2026-76655) | High | 7.5 | A security vulnerability in HPE NonStop SNMP Trap Multiplexer may allow remote code execution |
| 2026-10-14 12:17:18 | [CVE-2026-85298](https://nvd.nist.gov/vuln/detail/CVE-2026-85298) | High | 7.3 | An Incorrect Authorization vulnerability in the AuthConfig validation and integration execution runtime in Google Cloud… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
