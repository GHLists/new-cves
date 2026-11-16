# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-11-16 13:18 UTC

New CVEs published between 2026-11-16 12:18 UTC and 2026-11-16 13:18 UTC.

[Full CSV](data/new-cves-2026-11-16T13-18-19-726629Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-11-16 13:17:18 | [CVE-2026-110710](https://nvd.nist.gov/vuln/detail/CVE-2026-110710) | High | 7.5 | @fastify/multipart is the official Fastify plugin for handling multipart/form-data uploads. In versions 3.0.0 through 1… |
| 2026-11-16 13:17:18 | [CVE-2026-111559](https://nvd.nist.gov/vuln/detail/CVE-2026-111559) | Critical | 9.3 | Batflat CMS does not sanitize data passed to the /contact endpoint. A remote unauthenticated attacker can send a POST r… |
| 2026-11-16 13:17:18 | [CVE-2026-113443](https://nvd.nist.gov/vuln/detail/CVE-2026-113443) | Medium | 6.3 | visualTicket is vulnerable to Insecure Direct Object Reference in the cart service. The server modifies or deletes a ca… |
| 2026-11-16 13:17:19 | [CVE-2026-113445](https://nvd.nist.gov/vuln/detail/CVE-2026-113445) | Medium | 6.9 | visualTicket is vulnerable to information exposure through an error message in the order creation functionality. Becaus… |
| 2026-11-16 13:17:19 | [CVE-2026-113446](https://nvd.nist.gov/vuln/detail/CVE-2026-113446) | Medium | 5.1 | visualTicket is vulnerable to Reflected Cross-Site Scripting via the "culture" and "sf_culture" parameters. An attacker… |
| 2026-11-16 13:17:19 | [CVE-2026-113447](https://nvd.nist.gov/vuln/detail/CVE-2026-113447) | Medium | 5.1 | visualTicket is vulnerable to Session Fixation via the symfony session identifier passed in the URL. The application ac… |
| 2026-11-16 13:17:19 | [CVE-2026-113448](https://nvd.nist.gov/vuln/detail/CVE-2026-113448) | Medium | 5.1 | visualTicket is vulnerable to Reflected Cross-Site Scripting in logon functionality. An attacker can prepare a speciall… |
| 2026-11-16 13:17:19 | [CVE-2026-113449](https://nvd.nist.gov/vuln/detail/CVE-2026-113449) | Medium | 6.3 | visualTicket is vulnerable to information exposure through JSONP on session-bound cart service endpoints. Session-bound… |
| 2026-11-16 13:17:19 | [CVE-2026-113450](https://nvd.nist.gov/vuln/detail/CVE-2026-113450) | Medium | 5.1 | visualTicket is vulnerable to Reflected Cross-Site Scripting via the JSONP callback parameter. An attacker can prepare… |
| 2026-11-16 13:17:19 | [CVE-2026-113444](https://nvd.nist.gov/vuln/detail/CVE-2026-113444) | Medium | 5.3 | visualTicket is vulnerable to Path Traversal in the thumbnail generation mechanism. The file parameter is used directly… |
| 2026-11-16 13:17:20 | [CVE-2026-113451](https://nvd.nist.gov/vuln/detail/CVE-2026-113451) | Medium | 6.9 | visualTicket is vulnerable to Cross-Site Request Forgery (CSRF) across multiple endpoints. State-changing operations ar… |
| 2026-11-16 13:17:20 | [CVE-2026-113452](https://nvd.nist.gov/vuln/detail/CVE-2026-113452) | Medium | 5.1 | visualTicket is vulnerable to Reflected Cross-Site Scripting via the selectedDate parameter in the order summary page.… |
| 2026-11-16 13:17:20 | [CVE-2026-113453](https://nvd.nist.gov/vuln/detail/CVE-2026-113453) | Medium | 6.3 | visualTicket does not require authentication for the PDF invoice file serving functionality. Invoice PDF files reside i… |
| 2026-11-16 13:17:20 | [CVE-2026-113454](https://nvd.nist.gov/vuln/detail/CVE-2026-113454) | Medium | 5.1 | visualTicket exposes sensitive information in error messages in the administrative report generator. Because applicatio… |
| 2026-11-16 13:17:20 | [CVE-2026-113455](https://nvd.nist.gov/vuln/detail/CVE-2026-113455) | Medium | 5.1 | visualTicket displays secret token value in admin settings panel. The "KSeF - Token API" edit form renders a pre-filled… |
| 2026-11-16 13:17:20 | [CVE-2026-113456](https://nvd.nist.gov/vuln/detail/CVE-2026-113456) | Medium | 5.1 | visualTicket exposes sensitive information in error messages in the cinema report generator. An authenticated attacker… |
| 2026-11-16 13:17:20 | [CVE-2026-121192](https://nvd.nist.gov/vuln/detail/CVE-2026-121192) | Medium | 6.8 | @fastify/proxy-addr determines which network hops are trusted proxies and backs Fastify's trustProxy setting, so that f… |
| 2026-11-16 13:17:22 | [CVE-2026-19732](https://nvd.nist.gov/vuln/detail/CVE-2026-19732) | Critical | 9.9 | An OS Command Injection vulnerability affecting Station Launcher App in 3DEXPERIENCE platform from Release 3DEXPERIENCE… |
| 2026-11-16 13:17:23 | [CVE-2026-77033](https://nvd.nist.gov/vuln/detail/CVE-2026-77033) | Critical | 9.9 | An OS Command Injection vulnerability affecting Station Launcher App in 3DEXPERIENCE platform from Release 3DEXPERIENCE… |
| 2026-11-16 13:17:23 | [CVE-2026-93664](https://nvd.nist.gov/vuln/detail/CVE-2026-93664) | Critical | 10.0 | A Deserialization of Untrusted Data vulnerability affecting Station Launcher App in 3DEXPERIENCE platform from Release… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
