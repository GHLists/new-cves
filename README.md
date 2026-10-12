# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-12 23:18 UTC

New CVEs published between 2026-10-12 22:19 UTC and 2026-10-12 23:18 UTC.

[Full CSV](data/new-cves-2026-10-12T23-18-36-514605Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-10-12 23:17:16 | [CVE-2023-54406](https://nvd.nist.gov/vuln/detail/CVE-2023-54406) | Medium | 6.9 | Frappe before 14.59.0 and 15.x before 15.5.0 contains a sandbox flaw where the frappe.flags.in_safe_exec global flag ca… |
| 2026-10-12 23:17:17 | [CVE-2023-54407](https://nvd.nist.gov/vuln/detail/CVE-2023-54407) | Medium | 6.9 | Frappe 14.x before 14.45.0 contains an information disclosure vulnerability that allows users with error log access to… |
| 2026-10-12 23:17:17 | [CVE-2023-54408](https://nvd.nist.gov/vuln/detail/CVE-2023-54408) | Medium | 5.1 | Frappe before 13.52.0 and 14.x before 14.31.0 contains an HTML injection vulnerability caused by weak escaping of user-… |
| 2026-10-12 23:17:17 | [CVE-2023-54409](https://nvd.nist.gov/vuln/detail/CVE-2023-54409) | Medium | 5.9 | Frappe before 13.46.1 and 14.x before 14.20.0 contains a cross-site scripting vulnerability because the html2text funct… |
| 2026-10-12 23:17:17 | [CVE-2023-54410](https://nvd.nist.gov/vuln/detail/CVE-2023-54410) | Medium | 5.3 | Frappe before 13.22.0 contains an improper authorization vulnerability that allows authenticated users to rename docume… |
| 2026-10-12 23:17:17 | [CVE-2023-54411](https://nvd.nist.gov/vuln/detail/CVE-2023-54411) | High | 8.2 | Frappe framework before 13.32.0 uses weak authentication for print view access, because the print view key can be deriv… |
| 2026-10-12 23:17:17 | [CVE-2023-54412](https://nvd.nist.gov/vuln/detail/CVE-2023-54412) | High | 7.1 | Frappe before 13.46.3 and 14.x before 14.21.1 contains an improper access control vulnerability in Email Template permi… |
| 2026-10-12 23:17:18 | [CVE-2024-58390](https://nvd.nist.gov/vuln/detail/CVE-2024-58390) | High | 8.7 | Frappe before 14.81.4 and 15.x before 15.41.0 contains an improper privilege management vulnerability involving a certa… |
| 2026-10-12 23:17:18 | [CVE-2024-58391](https://nvd.nist.gov/vuln/detail/CVE-2024-58391) | Medium | 5.3 | Frappe before 14.58.0 and 15.x before 15.4.0 contains a cross-site scripting vulnerability in printview because printvi… |
| 2026-10-12 23:17:18 | [CVE-2025-71430](https://nvd.nist.gov/vuln/detail/CVE-2025-71430) | Medium | 5.1 | Frappe before 14.99.10 and 15.x before 15.91.1 contains a stored cross-site scripting vulnerability in the leaderboard… |
| 2026-10-12 23:17:19 | [CVE-2025-71431](https://nvd.nist.gov/vuln/detail/CVE-2025-71431) | Medium | 6.3 | Frappe before 14.99.2 and 15.x before 15.86.0 contains an LDAP injection vulnerability because certain endpoints do not… |
| 2026-10-12 23:17:19 | [CVE-2025-71432](https://nvd.nist.gov/vuln/detail/CVE-2025-71432) | High | 8.6 | Frappe ERPNext before 14.92.1 and 15.x before 15.83.0 contains a reflected cross-site scripting vulnerability due to mi… |
| 2026-10-12 23:17:19 | [CVE-2026-102627](https://nvd.nist.gov/vuln/detail/CVE-2026-102627) | High | 8.8 | IBM TRIRIGA Application Platform 5.0.0 through 5.0.8 could allow a remote authenticated attacker to execute arbitrary c… |
| 2026-10-12 23:17:21 | [CVE-2026-108935](https://nvd.nist.gov/vuln/detail/CVE-2026-108935) | Low | 1.9 | A weakness has been identified in Edimax BR-6208AC 1.32. Affected by this issue is some unknown functionality of the fi… |
| 2026-10-12 23:17:21 | [CVE-2026-108936](https://nvd.nist.gov/vuln/detail/CVE-2026-108936) | Low | 1.9 | A security vulnerability has been detected in Edimax BR-6208AC 1.32. This affects an unknown part of the file /goform/f… |
| 2026-10-12 23:17:22 | [CVE-2026-108937](https://nvd.nist.gov/vuln/detail/CVE-2026-108937) | Medium | 5.5 | A vulnerability was detected in code-projects Online Ticket Reservation System 1.0. This vulnerability affects unknown… |
| 2026-10-12 23:17:22 | [CVE-2026-108938](https://nvd.nist.gov/vuln/detail/CVE-2026-108938) | Medium | 5.5 | A flaw has been found in code-projects Matrimonial System 1.0. This issue affects some unknown processing of the file d… |
| 2026-10-12 23:17:22 | [CVE-2026-109572](https://nvd.nist.gov/vuln/detail/CVE-2026-109572) | High | 7.2 | Open WebUI from 0.8.6 before 0.11.4 contains a privilege escalation vulnerability in the terminal proxy that allows aut… |
| 2026-10-12 23:17:22 | [CVE-2026-109573](https://nvd.nist.gov/vuln/detail/CVE-2026-109573) | Critical | 9.2 | phpMyFAQ before 4.1.9 contains an SQL injection vulnerability in PdoMysql::escape(), which escapes single quotes with b… |
| 2026-10-12 23:17:22 | [CVE-2026-109574](https://nvd.nist.gov/vuln/detail/CVE-2026-109574) | Medium | 6.7 | Hugo before v0.167.0 contains a path traversal vulnerability in css.Sass that allows malicious themes or modules to rea… |
| 2026-10-12 23:17:22 | [CVE-2026-109595](https://nvd.nist.gov/vuln/detail/CVE-2026-109595) | Medium | 6.7 | Hugo from v0.84.0 before v0.167.0 contains a path traversal vulnerability that allows malicious themes or modules to re… |
| 2026-10-12 23:17:23 | [CVE-2026-109596](https://nvd.nist.gov/vuln/detail/CVE-2026-109596) | Medium | 6.7 | Hugo from v0.162.0 before v0.167.0 contains an improper link resolution vulnerability that lets malicious themes or mod… |
| 2026-10-12 23:17:23 | [CVE-2026-109597](https://nvd.nist.gov/vuln/detail/CVE-2026-109597) | Medium | 5.1 | Hugo from v0.60.0 before v0.167.0 contains a stored cross-site scripting vulnerability that allows Markdown content aut… |
| 2026-10-12 23:17:23 | [CVE-2026-109598](https://nvd.nist.gov/vuln/detail/CVE-2026-109598) | Medium | 5.3 | Frappe Framework before 15.120.0 and 16.x before 16.33.0 contains a missing authorization vulnerability in the whitelis… |
| 2026-10-12 23:17:23 | [CVE-2026-109599](https://nvd.nist.gov/vuln/detail/CVE-2026-109599) | Medium | 5.3 | Frappe before 15.113.3 and 16.x before 16.25.0 contains a missing authorization vulnerability in which certain endpoint… |
| 2026-10-12 23:17:23 | [CVE-2026-109600](https://nvd.nist.gov/vuln/detail/CVE-2026-109600) | Medium | 6.9 | Frappe Framework before 15.118.0 and 16.x before 16.31.0 does not check whether a user account is disabled before sendi… |
| 2026-10-12 23:17:23 | [CVE-2026-109601](https://nvd.nist.gov/vuln/detail/CVE-2026-109601) | High | 7.1 | Frappe Framework before 15.117.0 and 16.x before 16.30.0 contains an arbitrary file read vulnerability in the handling… |
| 2026-10-12 23:17:23 | [CVE-2026-109602](https://nvd.nist.gov/vuln/detail/CVE-2026-109602) | Medium | 5.1 | Frappe before 15.118.0 and 16.x before 16.31.0 contains a stored cross-site scripting vulnerability in dashboard chart… |
| 2026-10-12 23:17:24 | [CVE-2026-109603](https://nvd.nist.gov/vuln/detail/CVE-2026-109603) | Medium | 4.8 | Frappe Framework 15.x before 15.107.3 and 16.x before 16.17.0 relies on a vulnerable pdfkit library (CVE-2025-26240) fo… |
| 2026-10-12 23:17:24 | [CVE-2026-109604](https://nvd.nist.gov/vuln/detail/CVE-2026-109604) | High | 8.5 | Frappe ERPNext before 15.112.0 and 16.x before 16.23.0 contains a stored cross-site scripting vulnerability because a t… |
| 2026-10-12 23:17:24 | [CVE-2026-109608](https://nvd.nist.gov/vuln/detail/CVE-2026-109608) | High | 8.7 | Frappe ERPNext before 15.121.0 and 16.x before 16.34.0 contains an SQL injection vulnerability in several endpoints tha… |
| 2026-10-12 23:17:24 | [CVE-2026-109609](https://nvd.nist.gov/vuln/detail/CVE-2026-109609) | High | 7.1 | Frappe ERPNext before 15.119.1 and 16.x before 16.32.0 contains an SQL injection vulnerability in some endpoints that l… |
| 2026-10-12 23:17:24 | [CVE-2026-109610](https://nvd.nist.gov/vuln/detail/CVE-2026-109610) | High | 7.1 | Frappe ERPNext before 15.119.1 and 16.x before 16.32.0 contains a missing authorization vulnerability because certain e… |
| 2026-10-12 23:17:24 | [CVE-2026-109611](https://nvd.nist.gov/vuln/detail/CVE-2026-109611) | Medium | 5.3 | Frappe ERPNext before 15.121.0 and 16.x before 16.34.0 contains a missing authorization vulnerability in certain endpoi… |
| 2026-10-12 23:17:25 | [CVE-2026-109612](https://nvd.nist.gov/vuln/detail/CVE-2026-109612) | High | 8.5 | Frappe ERPNext before 15.120.0 and 16.x before 16.33.0 contains a stored cross-site scripting vulnerability in a report… |
| 2026-10-12 23:17:25 | [CVE-2026-109613](https://nvd.nist.gov/vuln/detail/CVE-2026-109613) | High | 7.1 | Frappe ERPNext before 15.121.0 and 16.x before 16.34.0 contains a missing authorization vulnerability in which certain… |
| 2026-10-12 23:17:25 | [CVE-2026-109614](https://nvd.nist.gov/vuln/detail/CVE-2026-109614) | High | 7.1 | Frappe ERPNext before 16.34.0 contains a missing authorization vulnerability that allows authenticated users to read fi… |
| 2026-10-12 23:17:25 | [CVE-2026-109615](https://nvd.nist.gov/vuln/detail/CVE-2026-109615) | High | 7.1 | Frappe ERPNext before 15.121.0 and 16.x before 16.34.0 contains a missing authorization vulnerability in certain endpoi… |
| 2026-10-12 23:17:25 | [CVE-2026-109616](https://nvd.nist.gov/vuln/detail/CVE-2026-109616) | High | 7.1 | Frappe ERPNext before 15.121.3 and 16.x before 16.35.0 contains a missing authorization vulnerability in which certain… |
| 2026-10-12 23:17:26 | [CVE-2026-109617](https://nvd.nist.gov/vuln/detail/CVE-2026-109617) | High | 7.1 | Frappe ERPNext before 15.121.0 and 16.x before 16.34.0 contains a missing authorization vulnerability in certain endpoi… |
| 2026-10-12 23:17:26 | [CVE-2026-109621](https://nvd.nist.gov/vuln/detail/CVE-2026-109621) | High | 7.1 | Frappe ERPNext before 15.120.0 and 16.x before 16.23.0 contains an authorization bypass in an endpoint that honours a c… |
| 2026-10-12 23:17:26 | [CVE-2026-109622](https://nvd.nist.gov/vuln/detail/CVE-2026-109622) | Medium | 5.3 | Frappe ERPNext before 15.121.0 and 16.x before 16.34.0 contains a missing authorization vulnerability in which certain… |
| 2026-10-12 23:17:26 | [CVE-2026-109623](https://nvd.nist.gov/vuln/detail/CVE-2026-109623) | Medium | 5.3 | Frappe ERPNext before 15.121.1 and 16.x before 16.34.2 contains a missing authorization vulnerability in certain endpoi… |
| 2026-10-12 23:17:26 | [CVE-2026-109624](https://nvd.nist.gov/vuln/detail/CVE-2026-109624) | High | 7.1 | Frappe ERPNext before 15.120.0 and 16.x before 16.33.0 contains a missing authorization vulnerability in certain endpoi… |
| 2026-10-12 23:17:26 | [CVE-2026-109625](https://nvd.nist.gov/vuln/detail/CVE-2026-109625) | High | 7.1 | Frappe ERPNext before 15.121.3 and 16.x before 16.35.0 contains a missing authorization vulnerability in certain endpoi… |
| 2026-10-12 23:17:27 | [CVE-2026-109626](https://nvd.nist.gov/vuln/detail/CVE-2026-109626) | High | 7.1 | Frappe ERPNext before 16.34.2 contains an SQL injection vulnerability caused by missing input validation in multiple en… |
| 2026-10-12 23:17:27 | [CVE-2026-109627](https://nvd.nist.gov/vuln/detail/CVE-2026-109627) | High | 7.1 | Frappe ERPNext before 15.120.0 and 16.x before 16.33.0 contains a missing authorization vulnerability in which certain… |
| 2026-10-12 23:17:27 | [CVE-2026-109628](https://nvd.nist.gov/vuln/detail/CVE-2026-109628) | High | 7.1 | Frappe ERPNext before 15.121.0 and 16.x before 16.34.0 contains a missing authorization vulnerability in certain endpoi… |
| 2026-10-12 23:17:27 | [CVE-2026-109629](https://nvd.nist.gov/vuln/detail/CVE-2026-109629) | Medium | 5.3 | Frappe ERPNext before 15.121.3 and 16.x before 16.35.0 contains a missing authorization vulnerability in an endpoint th… |
| 2026-10-12 23:17:27 | [CVE-2026-109630](https://nvd.nist.gov/vuln/detail/CVE-2026-109630) | Medium | 5.3 | Frappe ERPNext before 15.121.0 and 16.x before 16.34.0 contains a missing authorization vulnerability in which certain… |
| 2026-10-12 23:17:27 | [CVE-2026-109631](https://nvd.nist.gov/vuln/detail/CVE-2026-109631) | High | 7.1 | Frappe ERPNext before 15.119.1 and 16.x before 16.32.0 contains an SQL injection vulnerability in some endpoints that l… |
| 2026-10-12 23:17:28 | [CVE-2026-109632](https://nvd.nist.gov/vuln/detail/CVE-2026-109632) | High | 7.1 | Frappe ERPNext before 15.121.0 and 16.x before 16.33.0 contains a missing authorization vulnerability in which certain… |
| 2026-10-12 23:17:28 | [CVE-2026-109633](https://nvd.nist.gov/vuln/detail/CVE-2026-109633) | High | 8.6 | Frappe ERPNext before 15.119.1 and 16.x before 16.32.0 contains a stored cross-site scripting vulnerability because con… |
| 2026-10-12 23:17:28 | [CVE-2026-109634](https://nvd.nist.gov/vuln/detail/CVE-2026-109634) | Medium | 6.9 | Frappe ERPNext before 15.121.0 and 16.x before 16.34.0 contains an SQL injection vulnerability in some endpoints due to… |
| 2026-10-12 23:17:28 | [CVE-2026-109635](https://nvd.nist.gov/vuln/detail/CVE-2026-109635) | Medium | 5.3 | Frappe ERPNext before 15.105.0 and 16.x before 16.15.0 contains a missing authorization vulnerability in certain docume… |
| 2026-10-12 23:17:28 | [CVE-2026-109636](https://nvd.nist.gov/vuln/detail/CVE-2026-109636) | High | 7.1 | Frappe ERPNext before 15.115.0 and 16.x before 16.26.0 contains a missing authorization vulnerability because certain e… |
| 2026-10-12 23:17:29 | [CVE-2026-109637](https://nvd.nist.gov/vuln/detail/CVE-2026-109637) | High | 7.1 | Frappe ERPNext before 16.14.0 contains a missing authorization vulnerability that allows authenticated users to modify… |
| 2026-10-12 23:17:29 | [CVE-2026-109638](https://nvd.nist.gov/vuln/detail/CVE-2026-109638) | High | 7.1 | Frappe ERPNext before 15.110.0 and 16.x before 16.21.0 contains a SQL injection vulnerability in some endpoints caused… |
| 2026-10-12 23:17:29 | [CVE-2026-109639](https://nvd.nist.gov/vuln/detail/CVE-2026-109639) | High | 7.1 | Frappe ERPNext before 15.102.0 and 16.x before 16.8.0 contains an SQL injection vulnerability in some endpoints due to… |
| 2026-10-12 23:17:29 | [CVE-2026-109640](https://nvd.nist.gov/vuln/detail/CVE-2026-109640) | High | 7.2 | Frappe ERPNext before 16.22.0 contains a missing authorization vulnerability that allows authenticated users to modify… |
| 2026-10-12 23:17:29 | [CVE-2026-109641](https://nvd.nist.gov/vuln/detail/CVE-2026-109641) | Medium | 6.9 | Frappe ERPNext before 15.110.0 and 16.x before 16.21.0 contains a missing authorization vulnerability in certain endpoi… |
| 2026-10-12 23:17:29 | [CVE-2026-109642](https://nvd.nist.gov/vuln/detail/CVE-2026-109642) | Medium | 5.3 | Frappe ERPNext before 15.110.0 and 16.x before 16.21.0 contains a missing authorization vulnerability in which certain… |
| 2026-10-12 23:17:30 | [CVE-2026-109643](https://nvd.nist.gov/vuln/detail/CVE-2026-109643) | High | 7.1 | Frappe ERPNext before 15.111.0 and 16.x before 16.22.0 contains a missing authorization vulnerability in certain projec… |
| 2026-10-12 23:17:30 | [CVE-2026-109644](https://nvd.nist.gov/vuln/detail/CVE-2026-109644) | High | 7.1 | Frappe ERPNext before 15.119.0 and 16.x before 16.31.0 contains a missing authorization vulnerability in certain endpoi… |
| 2026-10-12 23:17:30 | [CVE-2026-109645](https://nvd.nist.gov/vuln/detail/CVE-2026-109645) | High | 7.1 | Frappe ERPNext before 15.119.0 and 16.x before 16.31.0 contains a missing authorization vulnerability in certain endpoi… |
| 2026-10-12 23:17:30 | [CVE-2026-109646](https://nvd.nist.gov/vuln/detail/CVE-2026-109646) | High | 7.1 | Frappe ERPNext before 15.106.0 and 16.x before 16.16.0 contains an SQL injection vulnerability in some endpoints due to… |
| 2026-10-12 23:17:30 | [CVE-2026-109647](https://nvd.nist.gov/vuln/detail/CVE-2026-109647) | High | 7.1 | Frappe ERPNext before 15.106.0 and 16.x before 16.16.0 contains an SQL injection vulnerability in multiple endpoints ca… |
| 2026-10-12 23:17:31 | [CVE-2026-109648](https://nvd.nist.gov/vuln/detail/CVE-2026-109648) | High | 7.1 | Frappe ERPNext before 15.106.0 and 16.x before 16.16.0 contains an SQL injection vulnerability in some endpoints due to… |
| 2026-10-12 23:17:31 | [CVE-2026-109649](https://nvd.nist.gov/vuln/detail/CVE-2026-109649) | High | 7.1 | Frappe ERPNext before 15.102.0 and 16.x before 16.11.0 contains an SQL injection vulnerability in some endpoints due to… |
| 2026-10-12 23:17:31 | [CVE-2026-109650](https://nvd.nist.gov/vuln/detail/CVE-2026-109650) | High | 7.1 | Frappe ERPNext before 15.112.0 and 16.x before 16.23.0 contains a missing authorization vulnerability in certain endpoi… |
| 2026-10-12 23:17:31 | [CVE-2026-109651](https://nvd.nist.gov/vuln/detail/CVE-2026-109651) | Medium | 5.3 | Frappe ERPNext before 15.112.0 and 16.x before 16.23.0 contains a server-side request forgery vulnerability caused by a… |
| 2026-10-12 23:17:31 | [CVE-2026-109652](https://nvd.nist.gov/vuln/detail/CVE-2026-109652) | High | 8.7 | Frappe ERPNext before 15.119.1 and 16.x before 16.32.0 contains a server-side template injection vulnerability because… |
| 2026-10-12 23:17:31 | [CVE-2026-109653](https://nvd.nist.gov/vuln/detail/CVE-2026-109653) | High | 8.5 | Frappe ERPNext before 15.119.0 and 16.x before 16.31.0 contains a stored cross-site scripting vulnerability because rec… |
| 2026-10-12 23:17:32 | [CVE-2026-109654](https://nvd.nist.gov/vuln/detail/CVE-2026-109654) | Medium | 5.3 | Frappe ERPNext before 15.119.0 and 16.x before 16.31.0 contains a missing authorization vulnerability in which certain… |
| 2026-10-12 23:17:32 | [CVE-2026-109655](https://nvd.nist.gov/vuln/detail/CVE-2026-109655) | High | 7.1 | Frappe ERPNext before 15.115.0 and 16.x before 16.26.0 contains a missing authorization vulnerability in certain endpoi… |
| 2026-10-12 23:17:32 | [CVE-2026-109656](https://nvd.nist.gov/vuln/detail/CVE-2026-109656) | High | 7.1 | Frappe ERPNext before 15.118.2 and 16.x before 16.30.0 contains a missing authorization vulnerability in which certain… |
| 2026-10-12 23:17:32 | [CVE-2026-109657](https://nvd.nist.gov/vuln/detail/CVE-2026-109657) | Medium | 5.1 | Frappe ERPNext 16.x before 16.27.0 contains a stored cross-site scripting vulnerability that allows users with edit rig… |
| 2026-10-12 23:17:32 | [CVE-2026-109658](https://nvd.nist.gov/vuln/detail/CVE-2026-109658) | High | 7.1 | Frappe ERPNext before 15.115.0 and 16.x before 16.26.0 contains a missing authorization vulnerability in which certain… |
| 2026-10-12 23:17:32 | [CVE-2026-109659](https://nvd.nist.gov/vuln/detail/CVE-2026-109659) | High | 7.1 | Frappe ERPNext before 15.113.0 and 16.x before 16.24.0 contains a missing authorization vulnerability in which certain… |
| 2026-10-12 23:17:33 | [CVE-2026-109660](https://nvd.nist.gov/vuln/detail/CVE-2026-109660) | High | 7.1 | Frappe ERPNext before 15.112.0 and 16.x before 16.23.0 has certain endpoints that do not enforce proper authorization c… |
| 2026-10-12 23:17:33 | [CVE-2026-109661](https://nvd.nist.gov/vuln/detail/CVE-2026-109661) | High | 7.1 | Frappe ERPNext before 15.116.0 and 16.x before 16.27.0 contains a missing authorization vulnerability in certain endpoi… |
| 2026-10-12 23:17:33 | [CVE-2026-109662](https://nvd.nist.gov/vuln/detail/CVE-2026-109662) | Medium | 5.3 | Frappe ERPNext before 15.112.0 and 16.x before 16.23.0 contains a stored cross-site scripting vulnerability in a public… |
| 2026-10-12 23:17:33 | [CVE-2026-109663](https://nvd.nist.gov/vuln/detail/CVE-2026-109663) | High | 7.1 | Frappe ERPNext before 15.113.0 and 16.x before 16.22.0 contains an SQL injection vulnerability caused by missing input… |
| 2026-10-12 23:17:33 | [CVE-2026-109664](https://nvd.nist.gov/vuln/detail/CVE-2026-109664) | Medium | 5.3 | Frappe ERPNext before 15.112.0 contains a missing authorization vulnerability that allows authenticated users with a co… |
| 2026-10-12 23:17:33 | [CVE-2026-109665](https://nvd.nist.gov/vuln/detail/CVE-2026-109665) | Medium | 5.3 | Frappe ERPNext before 15.108.0 and 16.x before 16.18.0 contains a missing authorization vulnerability in certain endpoi… |
| 2026-10-12 23:17:34 | [CVE-2026-109666](https://nvd.nist.gov/vuln/detail/CVE-2026-109666) | High | 7.1 | Frappe ERPNext before 15.110.0 and 16.x before 16.21.0 contains a missing authorization vulnerability in certain endpoi… |
| 2026-10-12 23:17:34 | [CVE-2026-109667](https://nvd.nist.gov/vuln/detail/CVE-2026-109667) | High | 8.7 | Frappe ERPNext before 15.111.0 and 16.x before 16.22.0 contains a privilege escalation vulnerability in a record-creati… |
| 2026-10-12 23:17:34 | [CVE-2026-109668](https://nvd.nist.gov/vuln/detail/CVE-2026-109668) | Medium | 5.3 | Frappe ERPNext before 15.110.0 and 16.x before 16.21.0 contains a missing authorization vulnerability in certain endpoi… |
| 2026-10-12 23:17:34 | [CVE-2026-109669](https://nvd.nist.gov/vuln/detail/CVE-2026-109669) | Medium | 5.3 | Frappe ERPNext before 15.110.0 and 16.x before 16.21.0 contains a missing authorization vulnerability in which certain… |
| 2026-10-12 23:17:34 | [CVE-2026-109670](https://nvd.nist.gov/vuln/detail/CVE-2026-109670) | Medium | 5.1 | Frappe ERPNext before 15.110.0 and 16.x before 16.21.0 contains a stored cross-site scripting vulnerability caused by r… |
| 2026-10-12 23:17:34 | [CVE-2026-109671](https://nvd.nist.gov/vuln/detail/CVE-2026-109671) | High | 8.5 | Frappe ERPNext before 15.113.0 and 16.x before 16.24.0 contains a stored cross-site scripting vulnerability in a profil… |
| 2026-10-12 23:17:35 | [CVE-2026-109672](https://nvd.nist.gov/vuln/detail/CVE-2026-109672) | High | 7.1 | Frappe ERPNext before 15.118.0 and 16.x before 16.27.0 contains a missing authorization vulnerability in certain endpoi… |
| 2026-10-12 23:17:35 | [CVE-2026-109673](https://nvd.nist.gov/vuln/detail/CVE-2026-109673) | High | 8.5 | Frappe ERPNext before 15.103.0 and 16.x before 16.12.0 contains a stored cross-site scripting vulnerability because the… |
| 2026-10-12 23:17:35 | [CVE-2026-109674](https://nvd.nist.gov/vuln/detail/CVE-2026-109674) | High | 7.1 | Frappe ERPNext before 15.98.0 and 16.x before 16.6.0 contains an SQL injection vulnerability in some endpoints caused b… |
| 2026-10-12 23:17:35 | [CVE-2026-109675](https://nvd.nist.gov/vuln/detail/CVE-2026-109675) | Medium | 5.3 | Frappe Suite before commit 2697564a9c46da6acc614743eaf9915fe5238f4f contains a broken access control vulnerability in t… |
| 2026-10-12 23:17:36 | [CVE-2026-17475](https://nvd.nist.gov/vuln/detail/CVE-2026-17475) | High | 7.1 | IBM Planning Analytics 2.0, and 2.1 could allow a remote authenticated attacker to delete folders and applications belo… |
| 2026-10-12 23:17:36 | [CVE-2026-18541](https://nvd.nist.gov/vuln/detail/CVE-2026-18541) | Medium | 6.4 | IBM Planning Analytics 2.0, and 2.1 is vulnerable to stored cross-site scripting. This vulnerability allows an authenti… |
| 2026-10-12 23:17:36 | [CVE-2026-19620](https://nvd.nist.gov/vuln/detail/CVE-2026-19620) | High | 8.8 | IBM Planning Analytics 2.0, and 2.1 could allow a remote attacker to gain unauthorized administrative access due to imp… |
| 2026-10-12 23:17:37 | [CVE-2026-19622](https://nvd.nist.gov/vuln/detail/CVE-2026-19622) | High | 8.8 | IBM Planning Analytics 2.0, and 2.1 could allow a remote attacker to bypass authentication and escalate privileges due… |
| 2026-10-12 23:17:37 | [CVE-2026-19627](https://nvd.nist.gov/vuln/detail/CVE-2026-19627) | High | 8.2 | IBM Planning Analytics 2.0, and 2.1 could allow a remote attacker to read arbitrary host files and overwrite certain ap… |
| 2026-10-12 23:17:38 | [CVE-2026-75061](https://nvd.nist.gov/vuln/detail/CVE-2026-75061) | High | 7.5 | IBM Planning Analytics 2.0, and 2.1 could allow a remote attacker to traverse directories on the system. An attacker co… |
| 2026-10-12 23:17:38 | [CVE-2026-75063](https://nvd.nist.gov/vuln/detail/CVE-2026-75063) | Medium | 5.4 | IBM Planning Analytics 2.0, and 2.1 could allow a remote authenticated attacker to execute arbitrary JavaScript due to… |
| 2026-10-12 23:17:38 | [CVE-2026-75076](https://nvd.nist.gov/vuln/detail/CVE-2026-75076) | Medium | 4.3 | IBM Aspera Enterprise WebApps 1.0.0 through 1.0.6 could allow a remote attacker to obtain sensitive information due to… |
| 2026-10-12 23:17:38 | [CVE-2026-75095](https://nvd.nist.gov/vuln/detail/CVE-2026-75095) | High | 7.5 | IBM Aspera Enterprise WebApps 1.0.0 through 1.0.6 could allow a remote attacker to cause a denial of service due to unc… |
| 2026-10-12 23:17:38 | [CVE-2026-75621](https://nvd.nist.gov/vuln/detail/CVE-2026-75621) | Medium | 6.2 | IBM Aspera Enterprise WebApps 1.0.0 through 1.0.6 could allow a local attacker to obtain sensitive information due to e… |
| 2026-10-12 23:17:39 | [CVE-2026-75782](https://nvd.nist.gov/vuln/detail/CVE-2026-75782) | High | 7.8 | IBM Aspera Enterprise WebApps 1.0.0 through 1.0.6 could allow a local attacker to gain elevated privileges due to a mis… |
| 2026-10-12 23:17:41 | [CVE-2026-82096](https://nvd.nist.gov/vuln/detail/CVE-2026-82096) | High | 8.8 | IBM DataStage on Cloud Pak for Data 5.4.0.0 could allow a remote authenticated attacker to execute arbitrary commands d… |
| 2026-10-12 23:17:41 | [CVE-2026-82101](https://nvd.nist.gov/vuln/detail/CVE-2026-82101) | Critical | 9.6 | IBM DataStage on Cloud Pak for Data 5.4.0.0 could allow a remote authenticated attacker to cause a denial of service du… |
| 2026-10-12 23:17:42 | [CVE-2026-82103](https://nvd.nist.gov/vuln/detail/CVE-2026-82103) | Critical | 9.6 | IBM DataStage on Cloud Pak for Data 5.4.0.0 could allow a remote authenticated attacker to obtain sensitive information… |
| 2026-10-12 23:17:42 | [CVE-2026-82108](https://nvd.nist.gov/vuln/detail/CVE-2026-82108) | High | 8.8 | IBM DataStage on Cloud Pak for Data 5.4.0.0 could allow a remote authenticated attacker to execute arbitrary code due t… |
| 2026-10-12 23:17:42 | [CVE-2026-82110](https://nvd.nist.gov/vuln/detail/CVE-2026-82110) | Critical | 9.6 | IBM DataStage on Cloud Pak for Data 5.4.0.0 could allow a remote authenticated attacker to execute arbitrary code due t… |
| 2026-10-12 23:17:45 | [CVE-2026-84418](https://nvd.nist.gov/vuln/detail/CVE-2026-84418) | High | 7.4 | IBM DataStage on Cloud Pak for Data 5.4.0.0 can allow a man-in-the-middle attacker to present a forged TLS certificate,… |
| 2026-10-12 23:17:45 | [CVE-2026-85457](https://nvd.nist.gov/vuln/detail/CVE-2026-85457) | High | 8.1 | IBM Planning Analytics 2.0, and 2.1 could allow a remote authenticated attacker to execute arbitrary code due to a stac… |
| 2026-10-12 23:17:45 | [CVE-2026-92832](https://nvd.nist.gov/vuln/detail/CVE-2026-92832) | Medium | 5.1 | IBM Aspera Enterprise WebApps 1.0.0 through 1.0.6 could allow a local attacker to obtain sensitive information due to c… |
| 2026-10-12 23:17:45 | [CVE-2026-93891](https://nvd.nist.gov/vuln/detail/CVE-2026-93891) | High | 7.6 | IBM TRIRIGA Application Platform 5.0.0 through 5.0.8 could allow a remote authenticated attacker to obtain sensitive in… |
| 2026-10-12 23:17:45 | [CVE-2026-93892](https://nvd.nist.gov/vuln/detail/CVE-2026-93892) | High | 8.1 | IBM TRIRIGA Application Platform 5.0.0 through 5.0.8 could allow a remote authenticated attacker to obtain sensitive in… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
