# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-16 14:19 UTC

New CVEs published between 2026-10-16 13:19 UTC and 2026-10-16 14:19 UTC.

[Full CSV](data/new-cves-2026-10-16T14-19-21-442252Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-10-16 14:17:14 | [CVE-2026-105664](https://nvd.nist.gov/vuln/detail/CVE-2026-105664) | Medium | 6.9 | The endpoint exposes an observable response discrepancy when processing ID values. A request submitted with a nonexiste… |
| 2026-10-16 14:17:16 | [CVE-2026-107617](https://nvd.nist.gov/vuln/detail/CVE-2026-107617) | Critical | 9.3 | An attacker can use a hard-coded credential to log in to EseeCloud devices. |
| 2026-10-16 14:17:22 | [CVE-2026-110287](https://nvd.nist.gov/vuln/detail/CVE-2026-110287) |  |  | Improper access control in asset contact password in Devolutions Server 2026.3.8.0 and earlier allows an authenticated… |
| 2026-10-16 14:17:22 | [CVE-2026-110804](https://nvd.nist.gov/vuln/detail/CVE-2026-110804) |  |  | Improperly controlled modification of JIT elevation settings in PAM checkout in Devolutions Server 2026.3.8.0 and earli… |
| 2026-10-16 14:17:22 | [CVE-2026-110805](https://nvd.nist.gov/vuln/detail/CVE-2026-110805) |  |  | Server-side request forgery in PingOne groups endpoint in Devolutions Server 2026.3.8.0 and earlier allows an authentic… |
| 2026-10-16 14:17:22 | [CVE-2026-110806](https://nvd.nist.gov/vuln/detail/CVE-2026-110806) |  |  | Incorrect authorization in add-on properties in Devolutions Server 2026.3.8.0 and earlier allows an authenticated user… |
| 2026-10-16 14:17:23 | [CVE-2026-111413](https://nvd.nist.gov/vuln/detail/CVE-2026-111413) | High | 8.8 | Cross-Site Request Forgery (CSRF) vulnerability in aThemeArt aThemeArt Theme Helper athemeart-theme-helper allows Cross… |
| 2026-10-16 14:17:23 | [CVE-2026-111593](https://nvd.nist.gov/vuln/detail/CVE-2026-111593) |  |  | Rejected reason: This CVE ID was reserved for a reported issue in the PDF Invoices & Packing Slips for WooCommerce Word… |
| 2026-10-16 14:17:24 | [CVE-2026-18516](https://nvd.nist.gov/vuln/detail/CVE-2026-18516) | Critical | 9.6 | An output escaping vulnerability in the Audit Logs component of Crafty Controller allows a remote, unauthenticated atta… |
| 2026-10-16 14:19:10 | [CVE-2026-90821](https://nvd.nist.gov/vuln/detail/CVE-2026-90821) | Medium | 5.4 | An input neutralization vulnerability in the Webhook URL form field component of Crafty Controller allows a remote, aut… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
