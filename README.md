# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-09-28 10:19 UTC

New CVEs published between 2026-09-28 09:18 UTC and 2026-09-28 10:19 UTC.

[Full CSV](data/new-cves-2026-09-28T10-19-38-617418Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-09-28 10:16:42 | [CVE-2026-101018](https://nvd.nist.gov/vuln/detail/CVE-2026-101018) | Low | 2.0 | A vulnerability was determined in dayrui XunruiCMS up to 4.7.2. This issue affects the function group_all_edit of the f… |
| 2026-09-28 10:16:42 | [CVE-2026-101035](https://nvd.nist.gov/vuln/detail/CVE-2026-101035) | Medium | 5.5 | A flaw has been found in aligungr UERANSIM up to 3.3.0. This affects the function DecodePlainMmMessage in the library s… |
| 2026-09-28 10:16:42 | [CVE-2026-101036](https://nvd.nist.gov/vuln/detail/CVE-2026-101036) | Low | 1.9 | A vulnerability has been found in FLB-Music FLB-Music-Player 1.1.8/1.1.9/1.2.0/1.2.1. This impacts the function path.jo… |
| 2026-09-28 10:16:42 | [CVE-2026-101037](https://nvd.nist.gov/vuln/detail/CVE-2026-101037) | High | 8.6 | A vulnerability was found in FAST FAC1200R 5.0_20201119_1.0.2. Affected is the function parse_advertisement_frame of th… |
| 2026-09-28 10:16:45 | [CVE-2026-7170](https://nvd.nist.gov/vuln/detail/CVE-2026-7170) | Medium | 4.8 | Stored Cross-Site Scripting (XSS) in TPVEnlanube affecting the following endpoint and parameter: * CVE-2026-7170: param… |
| 2026-09-28 10:16:45 | [CVE-2026-7171](https://nvd.nist.gov/vuln/detail/CVE-2026-7171) | Medium | 4.8 | Stored Cross-Site Scripting (XSS) in TPVEnlanube affecting the following endpoint and parameter: * CVE-2026-7171: param… |
| 2026-09-28 10:16:45 | [CVE-2026-7172](https://nvd.nist.gov/vuln/detail/CVE-2026-7172) | Medium | 4.8 | Stored Cross-Site Scripting (XSS) in TPVEnlanube affecting the following endpoint and parameter: * CVE-2026-7172: param… |
| 2026-09-28 10:16:45 | [CVE-2026-90979](https://nvd.nist.gov/vuln/detail/CVE-2026-90979) |  |  | LDAPCache and LDAPBackingEngine build LDAP search filters for user lookup and role lookup by textually substituting the… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
