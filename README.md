# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-25 07:19 UTC

New CVEs published between 2026-10-25 06:18 UTC and 2026-10-25 07:19 UTC.

[Full CSV](data/new-cves-2026-10-25T07-19-32-350485Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-10-25 07:16:46 | [CVE-2026-116045](https://nvd.nist.gov/vuln/detail/CVE-2026-116045) | Low | 2.1 | A vulnerability was detected in 1999AZZAR designer-mcp up to 2.1.0. This affects the function get_reference of the file… |
| 2026-10-25 07:16:47 | [CVE-2026-116046](https://nvd.nist.gov/vuln/detail/CVE-2026-116046) | Medium | 4.8 | A flaw has been found in eventcatalog sdk up to 2.29.0. This vulnerability affects the function getCustomDoc/writeCusto… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
