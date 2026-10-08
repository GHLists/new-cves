# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-08 01:20 UTC

New CVEs published between 2026-10-08 00:18 UTC and 2026-10-08 01:20 UTC.

[Full CSV](data/new-cves-2026-10-08T01-20-29-965409Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-10-08 01:16:32 | [CVE-2024-8122](https://nvd.nist.gov/vuln/detail/CVE-2024-8122) | Medium | 5.9 | The WSO2 Identity Server fails to enforce a default expiry time for SMS One-Time Passwords (OTPs) used in multi-factor… |
| 2026-10-08 01:16:32 | [CVE-2026-87679](https://nvd.nist.gov/vuln/detail/CVE-2026-87679) | High | 8.5 | When Brocade Fabric OS versions before 10.0.1 processes trunk configuration operations, the application parses user-sup… |
| 2026-10-08 01:16:32 | [CVE-2026-87680](https://nvd.nist.gov/vuln/detail/CVE-2026-87680) | High | 8.5 | A command injection vulnerability in the REST API management interface of Brocade Fabric OS versions before 10.0.1 allo… |
| 2026-10-08 01:16:32 | [CVE-2026-87681](https://nvd.nist.gov/vuln/detail/CVE-2026-87681) | High | 7.1 | An Access Control Bypass vulnerability exists in the Role-Based Access Control (RBAC) validation engine of Brocade Fabr… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
