# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-17 19:18 UTC

New CVEs published between 2026-10-17 18:21 UTC and 2026-10-17 19:18 UTC.

[Full CSV](data/new-cves-2026-10-17T19-18-24-469281Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-10-17 19:16:27 | [CVE-2024-58398](https://nvd.nist.gov/vuln/detail/CVE-2024-58398) | Medium | 5.3 | Coder 2.3.1 before 2.14.4, 2.15.x before 2.15.3, and 2.16.0 before 2.16.1 contains an open redirect vulnerability in th… |
| 2026-10-17 19:16:28 | [CVE-2025-71435](https://nvd.nist.gov/vuln/detail/CVE-2025-71435) | Low | 2.3 | Coder before 2.23.0 contains a session expiration bypass vulnerability that allows authenticated users to retain access… |
| 2026-10-17 19:16:28 | [CVE-2026-110882](https://nvd.nist.gov/vuln/detail/CVE-2026-110882) | Medium | 4.3 | Missing Authorization vulnerability in Cozy Vision Technologies Pvt. Ltd. SMS Alert Order Notifications sms-alert allow… |
| 2026-10-17 19:16:28 | [CVE-2026-111880](https://nvd.nist.gov/vuln/detail/CVE-2026-111880) | High | 8.3 | FreeRDP versions from 2.0.0 before 3.32.0 contain a heap out-of-bounds write in the server hash-callback NTLM path that… |
| 2026-10-17 19:16:29 | [CVE-2026-111881](https://nvd.nist.gov/vuln/detail/CVE-2026-111881) | High | 7.2 | FreeRDP from 3.14.1 before 3.32.0 contains an integer underflow in the WinPR BMP writer, where a mismatched stride calc… |
| 2026-10-17 19:16:29 | [CVE-2026-111882](https://nvd.nist.gov/vuln/detail/CVE-2026-111882) | High | 8.6 | phpMyFAQ 3.2.0-alpha before 4.1.9 and 4.2.0-alpha before 4.2.0-beta contains an authentication bypass vulnerability tha… |
| 2026-10-17 19:16:29 | [CVE-2026-111884](https://nvd.nist.gov/vuln/detail/CVE-2026-111884) | High | 8.7 | phpMyFAQ before 4.1.9 and 4.2.0-alpha before 4.2.0-beta does not require the current password when changing an account… |
| 2026-10-17 19:16:29 | [CVE-2026-111885](https://nvd.nist.gov/vuln/detail/CVE-2026-111885) | High | 7.0 | phpMyFAQ from 4.2.0-alpha before 4.2.0-beta contains a missing authorization vulnerability in GroupController::deleteGr… |
| 2026-10-17 19:16:29 | [CVE-2026-111886](https://nvd.nist.gov/vuln/detail/CVE-2026-111886) | High | 7.1 | phpMyFAQ from 4.2.0-alpha.2 before 4.2.0-beta lacks brute-force lockout in the removeTwofactorConfig() 2FA removal endp… |
| 2026-10-17 19:16:29 | [CVE-2026-111887](https://nvd.nist.gov/vuln/detail/CVE-2026-111887) | Medium | 6.9 | phpMyFAQ before 4.1.9 and 4.2.0-alpha before 4.2.0-beta contains an account enumeration vulnerability that allows unaut… |
| 2026-10-17 19:16:30 | [CVE-2026-111888](https://nvd.nist.gov/vuln/detail/CVE-2026-111888) | Medium | 5.1 | phpMyFAQ from 4.0.0 before 4.1.9 contains an incorrect authorization vulnerability that allows delegated admins lacking… |
| 2026-10-17 19:16:30 | [CVE-2026-111889](https://nvd.nist.gov/vuln/detail/CVE-2026-111889) | Medium | 5.3 | phpMyFAQ from 4.1.0 before 4.1.9 and 4.2.0-alpha before 4.2.0-beta contains a missing authorization vulnerability in th… |
| 2026-10-17 19:16:30 | [CVE-2026-111890](https://nvd.nist.gov/vuln/detail/CVE-2026-111890) | High | 7.0 | phpMyFAQ from 4.2.0-alpha.2 before 4.2.0-beta contains a privilege escalation vulnerability in UserController::updateUs… |
| 2026-10-17 19:16:30 | [CVE-2026-111891](https://nvd.nist.gov/vuln/detail/CVE-2026-111891) | High | 7.0 | phpMyFAQ from 4.2.0-alpha.2 before 4.2.0-beta contains a privilege escalation vulnerability in the group permission API… |
| 2026-10-17 19:16:30 | [CVE-2026-111892](https://nvd.nist.gov/vuln/detail/CVE-2026-111892) | Medium | 6.9 | phpMyFAQ 4.2.0-alpha before 4.2.0-beta lacks effective rate limiting on the unauthenticated user/password/update and us… |
| 2026-10-17 19:16:30 | [CVE-2026-111893](https://nvd.nist.gov/vuln/detail/CVE-2026-111893) | High | 8.5 | phpMyFAQ 4.2.0-alpha before 4.2.0-beta contains a privilege escalation vulnerability in GroupController::saveCategoryRe… |
| 2026-10-17 19:16:31 | [CVE-2026-111894](https://nvd.nist.gov/vuln/detail/CVE-2026-111894) | Medium | 5.1 | phpMyFAQ 3.2.1 before 4.1.9 and 4.2.0-alpha before 4.2.0-beta contains a stored cross-site scripting vulnerability that… |
| 2026-10-17 19:16:31 | [CVE-2026-111895](https://nvd.nist.gov/vuln/detail/CVE-2026-111895) | High | 7.6 | phpMyFAQ 3.2.0 before 4.0.0 and 4.0.2 before 4.2.0-beta contains an authentication bypass in its Microsoft Entra ID log… |
| 2026-10-17 19:16:31 | [CVE-2026-111896](https://nvd.nist.gov/vuln/detail/CVE-2026-111896) | Medium | 5.1 | phpMyFAQ from 4.2.0-alpha before 4.2.0-beta contains a stored cross-site scripting vulnerability in SvgSanitizer that a… |
| 2026-10-17 19:16:31 | [CVE-2026-111897](https://nvd.nist.gov/vuln/detail/CVE-2026-111897) | High | 7.1 | phpMyFAQ 4.2.0-alpha before 4.2.0-beta contains an authorization bypass vulnerability that allows category-restricted e… |
| 2026-10-17 19:16:31 | [CVE-2026-111898](https://nvd.nist.gov/vuln/detail/CVE-2026-111898) | High | 7.7 | phpMyFAQ 4.2.0-alpha before 4.2.0-beta contains an authentication bypass vulnerability that allows Keycloak users to ta… |
| 2026-10-17 19:16:31 | [CVE-2026-111900](https://nvd.nist.gov/vuln/detail/CVE-2026-111900) | Medium | 5.3 | phpMyFAQ before 4.1.9 and 4.2.0-alpha before 4.2.0-beta contains an improper authorization vulnerability in attachment.… |
| 2026-10-17 19:16:31 | [CVE-2026-111901](https://nvd.nist.gov/vuln/detail/CVE-2026-111901) | High | 8.7 | phpMyFAQ 4.2.0-alpha before 4.2.0-beta contains an uncontrolled resource consumption vulnerability in the unauthenticat… |
| 2026-10-17 19:16:32 | [CVE-2026-111902](https://nvd.nist.gov/vuln/detail/CVE-2026-111902) | Medium | 6.9 | phpMyFAQ 4.2.0-alpha before 4.2.0-beta contains an authorization bypass vulnerability in isFaqAccessibleForUser() that… |
| 2026-10-17 19:16:32 | [CVE-2026-111903](https://nvd.nist.gov/vuln/detail/CVE-2026-111903) | Medium | 5.1 | phpMyFAQ 4.2.0-alpha before 4.2.0-beta contains a stored cross-site scripting vulnerability in SvgSanitizer that allows… |
| 2026-10-17 19:16:32 | [CVE-2026-111904](https://nvd.nist.gov/vuln/detail/CVE-2026-111904) | Medium | 6.9 | phpMyFAQ 4.2.0-alpha before 4.2.0-beta contains an information disclosure vulnerability that allows unauthenticated att… |
| 2026-10-17 19:16:32 | [CVE-2026-111905](https://nvd.nist.gov/vuln/detail/CVE-2026-111905) | High | 7.0 | phpMyFAQ 3.2.0 before 4.1.9 and 4.2.0-alpha before 4.2.0-beta contains an insecure direct object reference vulnerabilit… |
| 2026-10-17 19:16:32 | [CVE-2026-111906](https://nvd.nist.gov/vuln/detail/CVE-2026-111906) | High | 7.1 | phpMyFAQ before 4.1.9 and 4.2.0-alpha before 4.2.0-beta contains a cross-site request forgery vulnerability in the Elas… |
| 2026-10-17 19:16:32 | [CVE-2026-111907](https://nvd.nist.gov/vuln/detail/CVE-2026-111907) | High | 7.1 | phpMyFAQ 4.0.0 before 4.1.9 contains a cross-site request forgery vulnerability in the POST /admin/api/update-database… |
| 2026-10-17 19:16:33 | [CVE-2026-111908](https://nvd.nist.gov/vuln/detail/CVE-2026-111908) | High | 8.7 | phpMyFAQ 4.0.0 before 4.1.9 and 4.2.0-alpha before 4.2.0-beta contains a broken object-level authorization vulnerabilit… |
| 2026-10-17 19:16:33 | [CVE-2026-111909](https://nvd.nist.gov/vuln/detail/CVE-2026-111909) | High | 7.2 | phpMyFAQ before 4.1.9 contains a missing authorization vulnerability in the deleteUser() API that allows authenticated… |
| 2026-10-17 19:16:33 | [CVE-2026-111910](https://nvd.nist.gov/vuln/detail/CVE-2026-111910) | High | 7.1 | phpMyFAQ before 4.1.9 and 4.2.0-alpha before 4.2.0-beta contains an authorization bypass vulnerability in attachment.ph… |
| 2026-10-17 19:16:33 | [CVE-2026-111911](https://nvd.nist.gov/vuln/detail/CVE-2026-111911) | Critical | 9.3 | phpMyFAQ 4.0.0 before 4.1.9 contains an authentication bypass vulnerability where WebAuthn registration endpoints attac… |
| 2026-10-17 19:16:33 | [CVE-2026-111912](https://nvd.nist.gov/vuln/detail/CVE-2026-111912) | High | 7.1 | Admidio from 5.0.0 before 5.0.16 contains an insecure direct object reference vulnerability in ForumService::saveTopic(… |
| 2026-10-17 19:16:33 | [CVE-2026-111913](https://nvd.nist.gov/vuln/detail/CVE-2026-111913) | Medium | 5.3 | Admidio from 5.0.0 before 5.0.16 contains an authorization bypass vulnerability that allows authenticated users to expo… |
| 2026-10-17 19:16:33 | [CVE-2026-111914](https://nvd.nist.gov/vuln/detail/CVE-2026-111914) | High | 7.1 | Admidio from 5.0.11 before 5.0.16 contains a broken access control vulnerability in modules/inventory/inventory_data.ph… |
| 2026-10-17 19:16:34 | [CVE-2026-111916](https://nvd.nist.gov/vuln/detail/CVE-2026-111916) | Medium | 6.9 | Admidio before 5.0.16 contains an information disclosure vulnerability that allows unauthenticated attackers to view ro… |
| 2026-10-17 19:16:34 | [CVE-2026-111917](https://nvd.nist.gov/vuln/detail/CVE-2026-111917) | High | 7.1 | Vikunja 2.3.0 before 2.7.0 contains an improper session validation vulnerability that allows attackers to keep WebSocke… |
| 2026-10-17 19:16:34 | [CVE-2026-111918](https://nvd.nist.gov/vuln/detail/CVE-2026-111918) | Medium | 5.3 | Vikunja from 1.0.0-rc0 before 2.7.0 contains an improper authorization vulnerability in RecalculateTaskPositions that a… |
| 2026-10-17 19:16:34 | [CVE-2026-111919](https://nvd.nist.gov/vuln/detail/CVE-2026-111919) | High | 7.1 | Vikunja 0.22.0 before 2.7.0 contains an improper access revocation vulnerability that allows removed collaborators to k… |
| 2026-10-17 19:16:34 | [CVE-2026-111920](https://nvd.nist.gov/vuln/detail/CVE-2026-111920) | Medium | 5.3 | Vikunja 2.6.0 contains a broken access control flaw in getProjectAccessForUser (pkg/models/project_access.go), which re… |
| 2026-10-17 19:16:34 | [CVE-2026-111921](https://nvd.nist.gov/vuln/detail/CVE-2026-111921) | Medium | 5.3 | Vikunja 0.13.0 before 2.7.0 contains an incorrect authorization vulnerability that allows project members with Write pe… |
| 2026-10-17 19:16:34 | [CVE-2026-111922](https://nvd.nist.gov/vuln/detail/CVE-2026-111922) | High | 7.2 | Vikunja from 2.2.0 before 2.7.0 contains a permissive CORS configuration that trusts every localhost and 127.0.0.1 port… |
| 2026-10-17 19:16:35 | [CVE-2026-111923](https://nvd.nist.gov/vuln/detail/CVE-2026-111923) | High | 8.7 | Fleet before 4.89.0 contains an unbounded recursion vulnerability in Apple MDM enrollment property list parsing that al… |
| 2026-10-17 19:16:35 | [CVE-2026-111924](https://nvd.nist.gov/vuln/detail/CVE-2026-111924) | High | 8.7 | Fleet before 4.83.0 contains a denial of service vulnerability that allows unauthenticated attackers to exhaust server… |
| 2026-10-17 19:16:35 | [CVE-2026-111926](https://nvd.nist.gov/vuln/detail/CVE-2026-111926) | Medium | 4.8 | Coder from 2.10.0 before 2.34.8 has an unauthenticated agent debug HTTP server on 127.0.0.1:2113 whose /debug/manifest… |
| 2026-10-17 19:16:35 | [CVE-2026-111927](https://nvd.nist.gov/vuln/detail/CVE-2026-111927) | High | 8.7 | Coder before 2.29.20, 2.33.0 before 2.33.12, 2.34.0 before 2.34.8, and 2.35.0 before 2.35.4 contains an improper hostna… |
| 2026-10-17 19:16:35 | [CVE-2026-111928](https://nvd.nist.gov/vuln/detail/CVE-2026-111928) | Medium | 5.3 | Coder from 2.0.0 before 2.34.8 contains an incorrect authorization vulnerability in the acl_allow rule of coderd/rbac/p… |
| 2026-10-17 19:16:35 | [CVE-2026-111929](https://nvd.nist.gov/vuln/detail/CVE-2026-111929) | Medium | 6.0 | Coder from 2.30.0 before 2.34.8 contains an authorization bypass vulnerability in the provisioner daemon DownloadFile g… |
| 2026-10-17 19:16:35 | [CVE-2026-111930](https://nvd.nist.gov/vuln/detail/CVE-2026-111930) | Medium | 5.3 | Coder from 2.26.0 before 2.34.8 contains an incorrect authorization flaw in the GET /api/v2/workspaces/{id}/acl endpoin… |
| 2026-10-17 19:16:36 | [CVE-2026-111931](https://nvd.nist.gov/vuln/detail/CVE-2026-111931) | Medium | 5.3 | Coder from 2.0.0 before 2.34.8 contains an open redirect vulnerability in handleAPIKeySmuggling that allows attackers t… |
| 2026-10-17 19:16:36 | [CVE-2026-111932](https://nvd.nist.gov/vuln/detail/CVE-2026-111932) | Medium | 4.8 | Coder before 2.29.17, 2.30.0 before 2.32.7, 2.33.0 before 2.33.8, and 2.34.0 before 2.34.2 contains a stored HTML injec… |
| 2026-10-17 19:16:36 | [CVE-2026-111933](https://nvd.nist.gov/vuln/detail/CVE-2026-111933) | Medium | 6.3 | Coder before 2.29.17, 2.30.0 before 2.32.7, 2.33.0 before 2.33.8, and 2.34.0 before 2.34.2 contains a user enumeration… |
| 2026-10-17 19:16:36 | [CVE-2026-111934](https://nvd.nist.gov/vuln/detail/CVE-2026-111934) | Medium | 6.3 | Coder before 2.34.7 contains an IP spoofing vulnerability in the ExtractRealIPAddress middleware that trusts the leftmo… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
