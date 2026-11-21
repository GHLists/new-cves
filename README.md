# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-11-21 15:18 UTC

New CVEs published between 2026-11-21 14:19 UTC and 2026-11-21 15:18 UTC.

[Full CSV](data/new-cves-2026-11-21T15-18-40-818796Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-11-21 15:17:06 | [CVE-2025-61963](https://nvd.nist.gov/vuln/detail/CVE-2025-61963) | High | 8.4 | Improper input validation within the AmdPlatformRasSmm driver could allow an attacker with privileged access to overwri… |
| 2026-11-21 15:17:08 | [CVE-2026-0462](https://nvd.nist.gov/vuln/detail/CVE-2026-0462) | Medium | 5.9 | Insufficient Granularity of Access Control in AMD Secure Encrypted Virtualization (SEV) firmware could allow a maliciou… |
| 2026-11-21 15:17:08 | [CVE-2026-133983](https://nvd.nist.gov/vuln/detail/CVE-2026-133983) | Medium | 6.9 | A vulnerability was detected in eigent-ai eigent up to 1.0.2. Affected by this vulnerability is an unknown functionalit… |
| 2026-11-21 15:17:09 | [CVE-2026-28235](https://nvd.nist.gov/vuln/detail/CVE-2026-28235) | Medium | 6.7 | Improper address validation in the AMD RAID Configuration Driver could allow an attacker with administrative access to… |
| 2026-11-21 15:17:10 | [CVE-2026-40671](https://nvd.nist.gov/vuln/detail/CVE-2026-40671) | Medium | 4.6 | Incomplete cleanup during VMRUN error handling could allow access to a Secure Encrypted Virtualization-Secure Nested Pa… |
| 2026-11-21 15:17:10 | [CVE-2026-74127](https://nvd.nist.gov/vuln/detail/CVE-2026-74127) | Critical | 9.4 | Improper verification of a cryptographic signature in the PSP Boot ROM of AMD Zeppelin (Zen1/Zen+) processors could all… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
