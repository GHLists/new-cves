# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-11-12 11:21 UTC

New CVEs published between 2026-11-12 10:18 UTC and 2026-11-12 11:21 UTC.

[Full CSV](data/new-cves-2026-11-12T11-21-44-166666Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-11-12 11:17:10 | [CVE-2026-124023](https://nvd.nist.gov/vuln/detail/CVE-2026-124023) |  |  | Out-of-bounds Read vulnerability in the Guththila XML parser wrapper of Apache Axis2/C. On some malformed XML input the… |
| 2026-11-12 11:17:10 | [CVE-2026-124701](https://nvd.nist.gov/vuln/detail/CVE-2026-124701) | High | 7.8 | In Telerik UI for WinForms, versions prior to 2026.4.1111, a deserialization of untrusted data vulnerability exists tha… |
| 2026-11-12 11:17:10 | [CVE-2026-124703](https://nvd.nist.gov/vuln/detail/CVE-2026-124703) | High | 7.8 | In Telerik UI for WPF, versions prior to 2026.4.1110, an improper control of code generation vulnerability exists that… |
| 2026-11-12 11:17:10 | [CVE-2026-124704](https://nvd.nist.gov/vuln/detail/CVE-2026-124704) | High | 7.8 | In Telerik UI for WPF, versions prior to 2026.4.1110, a deserialization of untrusted data vulnerability exists that all… |
| 2026-11-12 11:17:11 | [CVE-2026-126641](https://nvd.nist.gov/vuln/detail/CVE-2026-126641) | Medium | 6.5 | A host key verification flaw was found in ansible-pylibssh and in the ansible.netcommon libssh connection plugin. When… |
| 2026-11-12 11:17:11 | [CVE-2026-126643](https://nvd.nist.gov/vuln/detail/CVE-2026-126643) | Medium | 6.5 | A cleartext storage flaw was found in the AAP Gateway Operator. When reconciling an AutomationController, the operator… |
| 2026-11-12 11:17:11 | [CVE-2026-126644](https://nvd.nist.gov/vuln/detail/CVE-2026-126644) | Low | 3.9 | A link-following flaw was found in the authorized_key module of the ansible.posix collection, residual to the fix for C… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
