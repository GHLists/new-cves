# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-08 00:18 UTC

New CVEs published between 2026-10-07 23:19 UTC and 2026-10-08 00:18 UTC.

[Full CSV](data/new-cves-2026-10-08T00-18-36-04734Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-10-08 00:16:33 | [CVE-2026-107315](https://nvd.nist.gov/vuln/detail/CVE-2026-107315) | Medium | 5.3 | pgjdbc, the PostgreSQL JDBC Driver, versions 42.7.4 through 42.7.13 pads a value that is shorter than its declared leng… |
| 2026-10-08 00:16:35 | [CVE-2026-17538](https://nvd.nist.gov/vuln/detail/CVE-2026-17538) | Medium | 5.4 | The LatePoint - Appointment Booking & Reservation plugin for WordPress is vulnerable to Insecure Direct Object Referenc… |
| 2026-10-08 00:16:35 | [CVE-2026-94154](https://nvd.nist.gov/vuln/detail/CVE-2026-94154) | Medium | 6.1 | The Aurora Heatmap plugin for WordPress is vulnerable to Stored Cross-Site Scripting via the ‘url’ parameter in all ver… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
