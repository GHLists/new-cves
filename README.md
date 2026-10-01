# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-01 07:20 UTC

New CVEs published between 2026-10-01 06:20 UTC and 2026-10-01 07:20 UTC.

[Full CSV](data/new-cves-2026-10-01T07-20-58-005067Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-10-01 07:16:32 | [CVE-2025-41753](https://nvd.nist.gov/vuln/detail/CVE-2025-41753) | Critical | 9.3 | The object name of a dynamically created BACnet File Object is interpreted as a file path without sufficient validation… |
| 2026-10-01 07:16:33 | [CVE-2026-103544](https://nvd.nist.gov/vuln/detail/CVE-2026-103544) | Low | 2.1 | A vulnerability was found in datadrivenconstruction OpenConstructionERP up to 14.8.1. The impacted element is an unknow… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
