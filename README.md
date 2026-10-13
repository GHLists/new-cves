# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-13 07:18 UTC

New CVEs published between 2026-10-13 06:19 UTC and 2026-10-13 07:18 UTC.

[Full CSV](data/new-cves-2026-10-13T07-18-53-676624Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-10-13 07:16:30 | [CVE-2026-103316](https://nvd.nist.gov/vuln/detail/CVE-2026-103316) | High | 7.1 | The macOS version of the DigiD app is not signed with Hardened Runtime. As a result, a local process can load its own d… |
| 2026-10-13 07:16:31 | [CVE-2026-108973](https://nvd.nist.gov/vuln/detail/CVE-2026-108973) | Medium | 5.5 | A vulnerability was determined in SourceCodester Contact Tracing System 1.0. Affected by this issue is the function mov… |
| 2026-10-13 07:16:31 | [CVE-2026-108974](https://nvd.nist.gov/vuln/detail/CVE-2026-108974) | Medium | 5.5 | A vulnerability was identified in SourceCodester E-Learning System 1.0. This affects the function save_users of the fil… |
| 2026-10-13 07:16:31 | [CVE-2026-108975](https://nvd.nist.gov/vuln/detail/CVE-2026-108975) | Medium | 5.5 | A security flaw has been discovered in SourceCodester Library Management System 1.0. This vulnerability affects the fun… |
| 2026-10-13 07:16:31 | [CVE-2026-109106](https://nvd.nist.gov/vuln/detail/CVE-2026-109106) | Low | 1.9 | A security flaw has been discovered in Polaris Office App 9.9.19 on Android. Affected by this vulnerability is the func… |
| 2026-10-13 07:16:32 | [CVE-2026-75826](https://nvd.nist.gov/vuln/detail/CVE-2026-75826) | High | 8.5 | Command injection in the backup function in Teltonika Networks RUTOS 7.22 before 7.24.6 and 7.25 before 7.25.2 (RUT, RU… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
