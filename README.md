# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-23 08:20 UTC

New CVEs published between 2026-10-23 07:19 UTC and 2026-10-23 08:20 UTC.

[Full CSV](data/new-cves-2026-10-23T08-20-18-786816Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-10-23 08:16:54 | [CVE-2026-4950](https://nvd.nist.gov/vuln/detail/CVE-2026-4950) | Medium | 4.8 | The CustomerAdministration portal (KundenManager) of VertiGIS WebOrderSystem allows privileged users to manage the empl… |
| 2026-10-23 08:16:55 | [CVE-2026-4951](https://nvd.nist.gov/vuln/detail/CVE-2026-4951) | Medium | 5.1 | The CustomerAdministration portal (KundenManager) of VertiGIS WebOrderSystem allows privileged users to search for empl… |
| 2026-10-23 08:16:55 | [CVE-2026-4952](https://nvd.nist.gov/vuln/detail/CVE-2026-4952) | Medium | 5.1 | The "ASMobile" web interface, which is part of the VertiGIS software package "GIS Portal", allows authenticated users t… |
| 2026-10-23 08:16:55 | [CVE-2026-63244](https://nvd.nist.gov/vuln/detail/CVE-2026-63244) | Critical | 9.8 | An authentication bypass vulnerability in WizLearn Technologies' Learning Management System (LMS) could allow an unauth… |
| 2026-10-23 08:16:55 | [CVE-2026-75775](https://nvd.nist.gov/vuln/detail/CVE-2026-75775) | High | 7.7 | Improper Neutralization of Special Elements used in an OS Command in certain ASUS routers allows remote user to execute… |
| 2026-10-23 08:16:55 | [CVE-2026-75779](https://nvd.nist.gov/vuln/detail/CVE-2026-75779) | High | 8.6 | Improper Neutralization of Special Elements used in an OS Command (“OS Command Injection”) and Cross-Site Request Forge… |
| 2026-10-23 08:16:55 | [CVE-2026-93489](https://nvd.nist.gov/vuln/detail/CVE-2026-93489) | High | 8.7 | Improper Authentication in ASUS router modules allows an unauthenticated nearby user to send an HTTP request and forge… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
