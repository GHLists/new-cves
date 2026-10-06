# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-06 02:19 UTC

New CVEs published between 2026-10-06 01:19 UTC and 2026-10-06 02:19 UTC.

[Full CSV](data/new-cves-2026-10-06T02-19-57-430165Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-10-06 02:17:03 | [CVE-2026-104039](https://nvd.nist.gov/vuln/detail/CVE-2026-104039) | Medium | 4.7 | A flaw was found in SSSD. A local user can cause a denial of service (DoS) by disrupting system authentication services… |
| 2026-10-06 02:17:03 | [CVE-2026-104040](https://nvd.nist.gov/vuln/detail/CVE-2026-104040) | Medium | 4.4 | A flaw was found in SSSD. When configured with the Entra ID identity provider, input lookup names containing single quo… |
| 2026-10-06 02:17:03 | [CVE-2026-104041](https://nvd.nist.gov/vuln/detail/CVE-2026-104041) | Medium | 5.5 | A flaw was found in SSSD. An unprivileged local user can repeatedly request lookups for nonexistent entries through the… |
| 2026-10-06 02:17:03 | [CVE-2026-104042](https://nvd.nist.gov/vuln/detail/CVE-2026-104042) | Medium | 5.5 | A flaw was found in sssd. A local attacker can cause a Denial of Service (DoS) by sending a crafted Pluggable Authentic… |
| 2026-10-06 02:17:03 | [CVE-2026-104043](https://nvd.nist.gov/vuln/detail/CVE-2026-104043) | Medium | 5.5 | A flaw was found in SSSD. A local attacker with access to the Name Service Switch (NSS) responder UNIX socket can trigg… |
| 2026-10-06 02:17:03 | [CVE-2026-104044](https://nvd.nist.gov/vuln/detail/CVE-2026-104044) | Medium | 6.2 | A flaw was found in sssd. A local attacker can trigger a Denial of Service (DoS) by sending a specially crafted Pluggab… |
| 2026-10-06 02:17:03 | [CVE-2026-104380](https://nvd.nist.gov/vuln/detail/CVE-2026-104380) |  |  | Punk versions from 0.48 before 0.55 for Perl route Extended CONNECT requests to any GET route without an Origin check i… |
| 2026-10-06 02:17:04 | [CVE-2026-105484](https://nvd.nist.gov/vuln/detail/CVE-2026-105484) | Critical | 10.0 | A security vulnerability has been detected in TOTOLINK X6000R 9.4.0cu.652_B20230116. The impacted element is the functi… |
| 2026-10-06 02:17:04 | [CVE-2026-105486](https://nvd.nist.gov/vuln/detail/CVE-2026-105486) | Medium | 5.5 | A vulnerability was detected in OSSRS srs up to 7.0-a1. This affects the function systemAPI.Run of the file internal/pr… |
| 2026-10-06 02:17:04 | [CVE-2026-105487](https://nvd.nist.gov/vuln/detail/CVE-2026-105487) | Low | 2.1 | A vulnerability was found in yogeshojha reNgine up to 2.2.0. Affected by this vulnerability is the function subdomain_d… |
| 2026-10-06 02:17:04 | [CVE-2026-105571](https://nvd.nist.gov/vuln/detail/CVE-2026-105571) | Medium | 5.5 | A flaw has been found in PickMall Lilishop up to 4.2.4. The impacted element is an unknown function of the file /buyer/… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
