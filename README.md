# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-22 23:20 UTC

New CVEs published between 2026-10-22 22:18 UTC and 2026-10-22 23:20 UTC.

[Full CSV](data/new-cves-2026-10-22T23-20-51-457765Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-10-22 22:19:18 | [CVE-2026-83938](https://nvd.nist.gov/vuln/detail/CVE-2026-83938) | Critical | 10.0 | Missing authentication for critical function in Azure Kubernetes Configuration Service allows an unauthorized attacker… |
| 2026-10-22 22:19:53 | [CVE-2026-96185](https://nvd.nist.gov/vuln/detail/CVE-2026-96185) | High | 7.5 | Stack-based buffer overflow in Microsoft Exchange Online allows an authorized attacker to execute code over a network. |
| 2026-10-22 22:20:01 | [CVE-2026-96616](https://nvd.nist.gov/vuln/detail/CVE-2026-96616) | High | 8.3 | Authentication tokens issued by the E3's web management interface on login are given an expiration time far beyond any… |
| 2026-10-22 22:20:13 | [CVE-2026-97785](https://nvd.nist.gov/vuln/detail/CVE-2026-97785) | Critical | 10.0 | Improper authentication in AAD App Proxy allows an unauthorized attacker to elevate privileges over a network. |
| 2026-10-22 23:18:17 | [CVE-2026-107861](https://nvd.nist.gov/vuln/detail/CVE-2026-107861) | Critical | 9.4 | The system control service on affected Kiloview E3 NDI encoder firmware fails to sanitize the hostname parameter accept… |
| 2026-10-22 23:18:22 | [CVE-2026-110243](https://nvd.nist.gov/vuln/detail/CVE-2026-110243) | Critical | 9.4 | The network management service on affected Kiloview E3 NDI encoder firmware fails to validate the network interface nam… |
| 2026-10-22 23:18:22 | [CVE-2026-110491](https://nvd.nist.gov/vuln/detail/CVE-2026-110491) | Medium | 6.9 | The ONVIF service on the E3 can be rendered unresponsive by sending malformed or incomplete requests to certain operati… |
| 2026-10-22 23:18:22 | [CVE-2026-110825](https://nvd.nist.gov/vuln/detail/CVE-2026-110825) | High | 8.7 | The ONVIF device service on affected Kiloview E3 NDI encoder firmware accepts hostname, DNS, and NTP configuration writ… |
| 2026-10-22 23:20:33 | [CVE-2026-92450](https://nvd.nist.gov/vuln/detail/CVE-2026-92450) | High | 8.7 | The authentication framework used by affected Kiloview E3 NDI encoder firmware signs session JSON Web Tokens using an H… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
