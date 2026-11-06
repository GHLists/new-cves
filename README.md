# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-11-06 01:20 UTC

New CVEs published between 2026-11-06 00:20 UTC and 2026-11-06 01:20 UTC.

[Full CSV](data/new-cves-2026-11-06T01-20-40-605022Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-11-06 01:17:47 | [CVE-2025-71458](https://nvd.nist.gov/vuln/detail/CVE-2025-71458) | High | 8.7 | FTS3 Web Monitoring (fts-monitoring) versions 3.12.0 through 3.13.2 and 3.14.0 contain an unauthenticated sql injection… |
| 2026-11-06 01:17:48 | [CVE-2026-107492](https://nvd.nist.gov/vuln/detail/CVE-2026-107492) |  |  | Rejected reason: This CVE ID has been rejected or withdrawn by its CVE Numbering Authority. |
| 2026-11-06 01:17:48 | [CVE-2026-123268](https://nvd.nist.gov/vuln/detail/CVE-2026-123268) | Low | 2.0 | A security vulnerability has been detected in libyal libvmdk up to 3fdd7839758e9f44ef95e1dfccde8552b860a4fc. Affected i… |
| 2026-11-06 01:17:48 | [CVE-2026-123269](https://nvd.nist.gov/vuln/detail/CVE-2026-123269) | Low | 1.9 | A vulnerability was detected in libyal libvmdk. Affected by this vulnerability is the function libvmdk_descriptor_file_… |
| 2026-11-06 01:17:50 | [CVE-2026-63017](https://nvd.nist.gov/vuln/detail/CVE-2026-63017) | Critical | 9.4 | Incorrect authorization in PowerSYSTEM Center allows a low-privileged, authenticated user to access resources normally… |
| 2026-11-06 01:17:50 | [CVE-2026-63774](https://nvd.nist.gov/vuln/detail/CVE-2026-63774) | Critical | 9.4 | Insufficient input validation in the PowerSYSTEM Center report designer allows an authenticated user to execute unautho… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
