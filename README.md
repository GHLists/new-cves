# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-09-25 01:19 UTC

New CVEs published between 2026-09-25 00:20 UTC and 2026-09-25 01:19 UTC.

[Full CSV](data/new-cves-2026-09-25T01-19-17-695956Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-09-25 01:16:48 | [CVE-2026-53493](https://nvd.nist.gov/vuln/detail/CVE-2026-53493) | Medium | 6.9 | containerd is an open-source container runtime. Prior to versions 1.7.36, 2.0.13, 2.2.9, 2.3.6, and 2.4.1, a crafted OC… |
| 2026-09-25 01:16:48 | [CVE-2026-85417](https://nvd.nist.gov/vuln/detail/CVE-2026-85417) | Medium | 6.4 | Incomplete property masking in the SANnav logging subsystem permits SNMP authentication and privacy passwords to be rec… |
| 2026-09-25 01:16:48 | [CVE-2026-92288](https://nvd.nist.gov/vuln/detail/CVE-2026-92288) |  |  | Lemonldap::NG::Portal versions from 2.20.0 before 2.21.6, from 2.22.0 before 2.23.4 for Perl allow unauthenticated OAut… |
| 2026-09-25 01:16:48 | [CVE-2026-92289](https://nvd.nist.gov/vuln/detail/CVE-2026-92289) |  |  | Lemonldap::NG::Portal versions from 2.23.0 before 2.23.4 for Perl allow a PKCE bypass for public Relying Parties in "PK… |
| 2026-09-25 01:16:49 | [CVE-2026-97646](https://nvd.nist.gov/vuln/detail/CVE-2026-97646) | Medium | 5.5 | A weakness has been identified in ningzichun student-management-system up to 98760f5711cf6dc8b4adca53a9e207ca49b02ebf.… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
