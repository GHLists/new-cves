# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-01 15:20 UTC

New CVEs published between 2026-10-01 14:18 UTC and 2026-10-01 15:20 UTC.

[Full CSV](data/new-cves-2026-10-01T15-20-34-317659Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-10-01 15:17:17 | [CVE-2024-58388](https://nvd.nist.gov/vuln/detail/CVE-2024-58388) | High | 8.7 | Sharp (and Toshiba Tec rebranded) multifunction printers contain an unauthenticated local file inclusion vulnerability… |
| 2026-10-01 15:17:17 | [CVE-2026-100514](https://nvd.nist.gov/vuln/detail/CVE-2026-100514) | High | 7.5 | Unauthenticated Insecure Direct Object References (IDOR) in REST API Log <= 1.7.2 versions. |
| 2026-10-01 15:17:17 | [CVE-2026-100517](https://nvd.nist.gov/vuln/detail/CVE-2026-100517) | High | 7.5 | Unauthenticated Insecure Direct Object References (IDOR) in Photo Reviews for WooCommerce <= 1.2.30 versions. |
| 2026-10-01 15:17:25 | [CVE-2026-102378](https://nvd.nist.gov/vuln/detail/CVE-2026-102378) | High | 7.1 | Unauthenticated Cross Site Scripting (XSS) in Parallax Section block <= 2.0.4 versions. |
| 2026-10-01 15:17:25 | [CVE-2026-103004](https://nvd.nist.gov/vuln/detail/CVE-2026-103004) | Medium | 6.3 | Next.js versions from 16.3.0 to 16.3.7 warm `use cache` handlers using `next/root-params` and can leak their return val… |
| 2026-10-01 15:17:26 | [CVE-2026-103068](https://nvd.nist.gov/vuln/detail/CVE-2026-103068) | High | 8.8 | Subscriber Privilege Escalation in ByteCoreStack &#8211; MCP Connector for AI Tools <= 1.2.2 versions. |
| 2026-10-01 15:17:27 | [CVE-2026-103347](https://nvd.nist.gov/vuln/detail/CVE-2026-103347) | Medium | 5.3 | Unauthenticated Bypass Vulnerability in hCaptcha for WP <= 5.3.0 versions. |
| 2026-10-01 15:17:29 | [CVE-2026-103687](https://nvd.nist.gov/vuln/detail/CVE-2026-103687) | Medium | 5.5 | A vulnerability has been found in rhukster dom-sanitizer up to 1.0.15. The affected element is the function url of the… |
| 2026-10-01 15:17:29 | [CVE-2026-103752](https://nvd.nist.gov/vuln/detail/CVE-2026-103752) | Critical | 9.8 | Unauthenticated Privilege Escalation in Authorizer <= 3.15.3 versions. |
| 2026-10-01 15:17:30 | [CVE-2026-56589](https://nvd.nist.gov/vuln/detail/CVE-2026-56589) | High | 7.2 | HCL BigFix Service Management is affected by a Stored Cross-Site Scripting (XSS) vulnerability, which could allow an at… |
| 2026-10-01 15:17:30 | [CVE-2026-56599](https://nvd.nist.gov/vuln/detail/CVE-2026-56599) | Low | 2.2 | HCL BigFix Service Management is affected by an Insecure Cookie Attribute Configuration vulnerability, which could allo… |
| 2026-10-01 15:17:30 | [CVE-2026-62071](https://nvd.nist.gov/vuln/detail/CVE-2026-62071) | Critical | 9.3 | Unauthenticated SQL Injection in WordPress File Upload <= 5.1.10 versions. |
| 2026-10-01 15:17:30 | [CVE-2026-62073](https://nvd.nist.gov/vuln/detail/CVE-2026-62073) | High | 7.5 | Unauthenticated Broken Access Control in WP Full Stripe Free <= 8.5.6 versions. |
| 2026-10-01 15:17:31 | [CVE-2026-67104](https://nvd.nist.gov/vuln/detail/CVE-2026-67104) | Medium | 5.3 | HCL BigFix Service Management is affected by an Information Disclosure vulnerability, which could allow an unauthentica… |
| 2026-10-01 15:17:31 | [CVE-2026-67105](https://nvd.nist.gov/vuln/detail/CVE-2026-67105) | High | 7.4 | HCL BigFix Service Management is affected by an Insecure Communication vulnerability, which could allow an attacker wit… |
| 2026-10-01 15:17:31 | [CVE-2026-67106](https://nvd.nist.gov/vuln/detail/CVE-2026-67106) | Medium | 5.3 | HCL BigFix Service Management is affected by an Information Disclosure vulnerability because two exposed API endpoints… |
| 2026-10-01 15:17:31 | [CVE-2026-79898](https://nvd.nist.gov/vuln/detail/CVE-2026-79898) | Critical | 9.1 | Fortra BoKS Manager contains a command injection vulnerability in crlserver. An authenticated user authorized to add CR… |
| 2026-10-01 15:17:31 | [CVE-2026-79899](https://nvd.nist.gov/vuln/detail/CVE-2026-79899) | High | 7.9 | Fortra BoKS Manager contains an insecure temporary file vulnerability in bccgethostcert. The utility creates predictabl… |
| 2026-10-01 15:17:31 | [CVE-2026-79900](https://nvd.nist.gov/vuln/detail/CVE-2026-79900) | Medium | 6.5 | boks_ksllogsd accepts a checksum algorithm name in the MD field of an authenticated KSL start message. Affected release… |
| 2026-10-01 15:17:36 | [CVE-2026-94390](https://nvd.nist.gov/vuln/detail/CVE-2026-94390) | High | 7.2 | Editor PHP Object Injection in Hide Shipping Method For WooCommerce <= 1.5.4 versions. |
| 2026-10-01 15:17:36 | [CVE-2026-95137](https://nvd.nist.gov/vuln/detail/CVE-2026-95137) |  |  | Rejected reason: DO NOT USE THIS CANDIDATE NUMBER. ConsultIDs: none. Reason: This candidate was withdrawn by its CNA. F… |
| 2026-10-01 15:17:36 | [CVE-2026-95588](https://nvd.nist.gov/vuln/detail/CVE-2026-95588) | High | 8.6 | Unauthenticated Arbitrary File Deletion in AcyMailing SMTP Newsletter <= 11.0.5 versions. |
| 2026-10-01 15:17:37 | [CVE-2026-97251](https://nvd.nist.gov/vuln/detail/CVE-2026-97251) | Medium | 6.5 | Unauthenticated Insecure Direct Object References (IDOR) in Bus Ticket Booking with Seat Reservation <= 5.9.3 versions. |
| 2026-10-01 15:17:37 | [CVE-2026-97258](https://nvd.nist.gov/vuln/detail/CVE-2026-97258) | Medium | 6.5 | Subscriber Broken Access Control in Aruba Migration Tool <= 1.0.4 versions. |
| 2026-10-01 15:17:37 | [CVE-2026-97260](https://nvd.nist.gov/vuln/detail/CVE-2026-97260) | High | 7.1 | Unauthenticated Cross Site Scripting (XSS) in MaxGalleria <= 6.5.3 versions. |
| 2026-10-01 15:17:37 | [CVE-2026-97268](https://nvd.nist.gov/vuln/detail/CVE-2026-97268) | High | 7.1 | Unauthenticated Cross Site Scripting (XSS) in Premmerce Wishlist for WooCommerce <= 1.1.13 versions. |
| 2026-10-01 15:17:38 | [CVE-2026-97269](https://nvd.nist.gov/vuln/detail/CVE-2026-97269) | Medium | 6.5 | Unauthenticated Insecure Direct Object References (IDOR) in WPFunnels <= 3.13.1 versions. |
| 2026-10-01 15:17:38 | [CVE-2026-97273](https://nvd.nist.gov/vuln/detail/CVE-2026-97273) | High | 7.1 | Unauthenticated Cross Site Scripting (XSS) in Premmerce Wishlist for WooCommerce <= 1.1.13 versions. |
| 2026-10-01 15:17:38 | [CVE-2026-97277](https://nvd.nist.gov/vuln/detail/CVE-2026-97277) | High | 7.6 | Subscriber Broken Access Control in Social Boost <= 3.6.2 versions. |
| 2026-10-01 15:17:38 | [CVE-2026-97280](https://nvd.nist.gov/vuln/detail/CVE-2026-97280) | Medium | 6.5 | Missing Authorization vulnerability in Mamunur Rashid Review Schema review-schema allows Exploiting Incorrectly Configu… |
| 2026-10-01 15:17:38 | [CVE-2026-97281](https://nvd.nist.gov/vuln/detail/CVE-2026-97281) | Medium | 6.3 | Subscriber Broken Access Control in WP Project Manager <= 4.0.7 versions. |
| 2026-10-01 15:17:38 | [CVE-2026-97284](https://nvd.nist.gov/vuln/detail/CVE-2026-97284) | High | 8.8 | Contributor PHP Object Injection in Icegram <= 3.1.31 versions. |
| 2026-10-01 15:17:38 | [CVE-2026-97297](https://nvd.nist.gov/vuln/detail/CVE-2026-97297) | High | 7.6 | Subscriber Broken Access Control in Gratisfaction <= 4.6.3 versions. |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
