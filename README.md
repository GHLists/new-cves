# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-11-20 02:18 UTC

New CVEs published between 2026-11-20 01:18 UTC and 2026-11-20 02:18 UTC.

[Full CSV](data/new-cves-2026-11-20T02-18-46-815437Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-11-20 02:17:16 | [CVE-2026-102430](https://nvd.nist.gov/vuln/detail/CVE-2026-102430) | Medium | 6.9 | An uncontrolled recursion vulnerability exists in the LINE iOS app prior to version 26.19.0. The Flex Message processin… |
| 2026-11-20 02:17:16 | [CVE-2026-133224](https://nvd.nist.gov/vuln/detail/CVE-2026-133224) | Medium | 5.4 | A flaw was found in Keycloak. When an administrator revokes tokens by setting a not-before revocation cutoff, Keycloak… |
| 2026-11-20 02:17:16 | [CVE-2026-133225](https://nvd.nist.gov/vuln/detail/CVE-2026-133225) | Medium | 5.4 | A flaw was found in Keycloak. When processing token requests using the User-Managed Access (UMA) grant, Keycloak fails… |
| 2026-11-20 02:17:16 | [CVE-2026-133226](https://nvd.nist.gov/vuln/detail/CVE-2026-133226) | Medium | 4.3 | A flaw was found in Keycloak. The Account API endpoint for sharing resources fails to verify whether owner-managed acce… |
| 2026-11-20 02:17:17 | [CVE-2026-133228](https://nvd.nist.gov/vuln/detail/CVE-2026-133228) | Medium | 6.8 | A flaw was found in Keycloak. When a client application enforces step-up authentication or multi-factor authentication… |
| 2026-11-20 02:17:17 | [CVE-2026-133413](https://nvd.nist.gov/vuln/detail/CVE-2026-133413) | Medium | 4.6 | A vulnerability was detected in smartalock wireguard-lwip up to cfba91666590e86bd67842c71cedf9a423be823a. This affects… |
| 2026-11-20 02:17:17 | [CVE-2026-133414](https://nvd.nist.gov/vuln/detail/CVE-2026-133414) | Medium | 6.9 | A security flaw has been discovered in sofastack sofa-bolt up to 1.6.12. Affected by this issue is the function Hessian… |
| 2026-11-20 02:17:17 | [CVE-2026-133415](https://nvd.nist.gov/vuln/detail/CVE-2026-133415) | Medium | 5.5 | A vulnerability has been found in sumiie24 School-Management-System up to d946d649c7c95e101fc5679ecd91999533bb10d7. The… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
