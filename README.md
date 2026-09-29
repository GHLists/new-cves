# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-09-29 08:24 UTC

New CVEs published between 2026-09-29 07:19 UTC and 2026-09-29 08:24 UTC.

[Full CSV](data/new-cves-2026-09-29T08-24-18-232592Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-09-29 08:17:19 | [CVE-2026-101169](https://nvd.nist.gov/vuln/detail/CVE-2026-101169) | High | 8.7 | In affected versions of Octopus Server, an authenticated user with permissions to edit an Environment or Project can se… |
| 2026-09-29 08:17:21 | [CVE-2026-84154](https://nvd.nist.gov/vuln/detail/CVE-2026-84154) | Critical | 9.9 | A Code Injection vulnerability affecting GEOVIA Geospatial Data Manager from Release 3DEXPERIENCE R2024x through Releas… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
