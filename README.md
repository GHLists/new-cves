# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-30 12:20 UTC

New CVEs published between 2026-10-30 11:18 UTC and 2026-10-30 12:20 UTC.

[Full CSV](data/new-cves-2026-10-30T12-20-03-00046Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-10-30 12:16:32 | [CVE-2025-68391](https://nvd.nist.gov/vuln/detail/CVE-2025-68391) | Medium | 5.3 | ARKETEAM Protectel modules PROTECTELMAJ and BDF are vulnerable to arbitrary file upload. Any user is able to upload arb… |
| 2026-10-30 12:16:33 | [CVE-2025-68392](https://nvd.nist.gov/vuln/detail/CVE-2025-68392) | Medium | 5.1 | ARKETEAM Protectel modules PROTECTELMAJ and BDF allow low privileged users to use some of the functionalities reserved… |
| 2026-10-30 12:16:33 | [CVE-2025-68393](https://nvd.nist.gov/vuln/detail/CVE-2025-68393) | High | 8.4 | ARKETEAM Protectel modules PROTECTELMAJ and BDF are vulnerable to SQL injection vulnerability. Improper neutralization… |
| 2026-10-30 12:16:33 | [CVE-2025-68394](https://nvd.nist.gov/vuln/detail/CVE-2025-68394) | High | 8.4 | ARKETEAM Protectel modules PROTECTELMAJ and BDF are vulnerable to SQL injection vulnerability. Improper neutralization… |
| 2026-10-30 12:16:33 | [CVE-2025-68395](https://nvd.nist.gov/vuln/detail/CVE-2025-68395) | Medium | 5.1 | ARKETEAM Protectel modules PROTECTELMAJ and BDF contain a note editor module vulnerable to Stored XSS. A low privileged… |
| 2026-10-30 12:16:33 | [CVE-2026-101209](https://nvd.nist.gov/vuln/detail/CVE-2026-101209) | Low | 2.7 | Dell OpenManage Enterprise, versions prior to 4.8.0, contains a Server-Side Request Forgery (SSRF) vulnerability. A hig… |
| 2026-10-30 12:16:34 | [CVE-2026-101213](https://nvd.nist.gov/vuln/detail/CVE-2026-101213) | High | 7.8 | Dell OpenManage Enterprise, versions prior to 4.8.0, contains an Improper Privilege Management vulnerability. A low pri… |
| 2026-10-30 12:16:34 | [CVE-2026-101214](https://nvd.nist.gov/vuln/detail/CVE-2026-101214) | High | 7.2 | Dell OpenManage Enterprise, versions prior to 4.8.0, contains an Improper Neutralization of Special Elements used in an… |
| 2026-10-30 12:16:34 | [CVE-2026-105924](https://nvd.nist.gov/vuln/detail/CVE-2026-105924) | Medium | 4.3 | A NULL pointer dereference vulnerability in the Qt QCborValue to JSON conversion of the Qt Core module. |
| 2026-10-30 12:16:34 | [CVE-2026-110970](https://nvd.nist.gov/vuln/detail/CVE-2026-110970) | Low | 2.3 | Płatnik uses HTTP protocol to download updates, libraries and support files. It allows an attacker to conduct a Man-In-… |
| 2026-10-30 12:16:34 | [CVE-2026-110971](https://nvd.nist.gov/vuln/detail/CVE-2026-110971) | High | 7.7 | Use of a weak password encoding algorithm in Płatnik software allows a user who obtains encoded password to easily deco… |
| 2026-10-30 12:16:34 | [CVE-2026-110972](https://nvd.nist.gov/vuln/detail/CVE-2026-110972) | High | 8.6 | Płatnik performs client-side authentication. An attacker with access to any application instance connected to the backe… |
| 2026-10-30 12:16:34 | [CVE-2026-111504](https://nvd.nist.gov/vuln/detail/CVE-2026-111504) | High | 7.2 | Dell OpenManage Enterprise, versions prior to 4.8.0, contains an Improper Neutralization of Argument Delimiters in a Co… |
| 2026-10-30 12:16:34 | [CVE-2026-101210](https://nvd.nist.gov/vuln/detail/CVE-2026-101210) | High | 7.2 | Dell OpenManage Enterprise, versions prior to 4.8.0, contains an Improper Neutralization of Special Elements used in an… |
| 2026-10-30 12:16:35 | [CVE-2026-111505](https://nvd.nist.gov/vuln/detail/CVE-2026-111505) | High | 8.8 | Dell OpenManage Enterprise, versions prior to 4.8.0, contains an Improper Neutralization of Special Elements used in an… |
| 2026-10-30 12:16:35 | [CVE-2026-119146](https://nvd.nist.gov/vuln/detail/CVE-2026-119146) | Medium | 6.3 | ProFTPD before 1.3.9e and 1.3.10rc5 contains a buffer overflow vulnerability in the mod_rewrite int:utf8trans RewriteMa… |
| 2026-10-30 12:16:35 | [CVE-2026-119147](https://nvd.nist.gov/vuln/detail/CVE-2026-119147) | Medium | 5.3 | ProFTPD before 1.3.9e and 1.3.10rc5 contains an authorization bypass in the mod_sftp copy-file extension handler that s… |
| 2026-10-30 12:16:35 | [CVE-2026-119364](https://nvd.nist.gov/vuln/detail/CVE-2026-119364) | Medium | 6.0 | ProFTPD through 1.3.9e and 1.3.10rc1 through 1.3.10rc4 contains a link-following vulnerability in mod_copy that allows… |
| 2026-10-30 12:16:35 | [CVE-2026-119371](https://nvd.nist.gov/vuln/detail/CVE-2026-119371) | Medium | 6.8 | SQLite before 3.54.0 contains a stack exhaustion vulnerability that allows attackers to bypass the SQLITE_LIMIT_EXPR_DE… |
| 2026-10-30 12:16:35 | [CVE-2026-119372](https://nvd.nist.gov/vuln/detail/CVE-2026-119372) | Medium | 6.8 | SQLite before 3.54.0 built with FTS3/FTS4 and SQLITE_ENABLE_FTS3_PARENTHESIS contains a use-after-free vulnerability in… |
| 2026-10-30 12:16:36 | [CVE-2026-119373](https://nvd.nist.gov/vuln/detail/CVE-2026-119373) | High | 8.5 | SQLite before 3.54.0 built with FTS5 contains a heap buffer overflow in fts5MergeRowidLists() that undersizes the outpu… |
| 2026-10-30 12:16:36 | [CVE-2026-119374](https://nvd.nist.gov/vuln/detail/CVE-2026-119374) | High | 8.5 | SQLite before 3.54.0 built with FTS5 contains a heap buffer overflow in fts5DoSecureDelete() that allows attackers to w… |
| 2026-10-30 12:16:36 | [CVE-2026-119375](https://nvd.nist.gov/vuln/detail/CVE-2026-119375) | Medium | 6.8 | SQLite before 3.54.0 contains an information disclosure vulnerability that allows attackers to read uninitialized page-… |
| 2026-10-30 12:16:36 | [CVE-2026-119376](https://nvd.nist.gov/vuln/detail/CVE-2026-119376) | Medium | 6.8 | SQLite before 3.54.0 contains a stack exhaustion vulnerability that allows attackers to bypass the SQLITE_LIMIT_EXPR_DE… |
| 2026-10-30 12:16:36 | [CVE-2026-119377](https://nvd.nist.gov/vuln/detail/CVE-2026-119377) | Low | 2.0 | SQLite before 3.54.0 contains an authorization bypass vulnerability in lookupName() that invokes the authorizer only fo… |
| 2026-10-30 12:16:36 | [CVE-2026-119378](https://nvd.nist.gov/vuln/detail/CVE-2026-119378) | Medium | 6.8 | SQLite before 3.54.0 contains a use-after-free vulnerability in the R-Tree extension that allows attackers to make appl… |
| 2026-10-30 12:16:36 | [CVE-2026-119379](https://nvd.nist.gov/vuln/detail/CVE-2026-119379) | High | 8.5 | SQLite before 3.54.0 built with the session extension contains a heap buffer overflow vulnerability in sqlite3changeset… |
| 2026-10-30 12:16:37 | [CVE-2026-119407](https://nvd.nist.gov/vuln/detail/CVE-2026-119407) | High | 7.1 | Element Web and Element Desktop before 1.12.32 accept guest credentials from URL fragment parameters in loadSession, al… |
| 2026-10-30 12:16:37 | [CVE-2026-119408](https://nvd.nist.gov/vuln/detail/CVE-2026-119408) | High | 8.7 | n8n before 2.42.6, 2.43.x before 2.43.3, and 3.x before 3.0.1 contains a remote code execution vulnerability via deprec… |
| 2026-10-30 12:16:37 | [CVE-2026-119409](https://nvd.nist.gov/vuln/detail/CVE-2026-119409) | High | 8.6 | OPNsense before 26.7.8 contains a command injection vulnerability that allows authenticated users with the System: Firm… |
| 2026-10-30 12:16:37 | [CVE-2026-119414](https://nvd.nist.gov/vuln/detail/CVE-2026-119414) | Medium | 5.3 | Bitwarden Server before 2026.10.1 on Entity Framework backends contains an authorization bypass vulnerability that allo… |
| 2026-10-30 12:16:37 | [CVE-2026-119415](https://nvd.nist.gov/vuln/detail/CVE-2026-119415) | Medium | 6.3 | CakePHP through 5.4.3 contains a header injection vulnerability in FormDataPart that allows attackers to inject MIME pa… |
| 2026-10-30 12:16:38 | [CVE-2026-119416](https://nvd.nist.gov/vuln/detail/CVE-2026-119416) | Medium | 6.3 | CakePHP through 5.4.3 contains an improper cookie domain validation vulnerability in the Http Client CookieCollection t… |
| 2026-10-30 12:16:38 | [CVE-2026-119417](https://nvd.nist.gov/vuln/detail/CVE-2026-119417) | Medium | 6.3 | CakePHP 4.5.12, 4.6.5, 5.1.8 through 5.1.10, 5.2.14 through 5.2.15, 5.3.7, and 5.4.0 through 5.4.3 contain an email hea… |
| 2026-10-30 12:16:38 | [CVE-2026-119418](https://nvd.nist.gov/vuln/detail/CVE-2026-119418) | Critical | 9.2 | CakePHP through 5.4.3 contains an sql injection vulnerability that allows attackers to inject SQL by supplying unvalida… |
| 2026-10-30 12:16:38 | [CVE-2026-119419](https://nvd.nist.gov/vuln/detail/CVE-2026-119419) | Critical | 9.2 | CakePHP through 5.4.3 contains an sql injection vulnerability that allows attackers to inject SQL by supplying unvalida… |
| 2026-10-30 12:16:38 | [CVE-2026-119420](https://nvd.nist.gov/vuln/detail/CVE-2026-119420) | High | 8.7 | Lago through 1.55.0 contains an authentication bypass vulnerability that allows organization administrators to obtain s… |
| 2026-10-30 12:16:38 | [CVE-2026-119421](https://nvd.nist.gov/vuln/detail/CVE-2026-119421) | High | 8.2 | Juspay Hyperswitch through 1.128.0 (and builds before 2026.10.19.0) contains a missing authorization vulnerability that… |
| 2026-10-30 12:16:39 | [CVE-2026-119422](https://nvd.nist.gov/vuln/detail/CVE-2026-119422) | High | 8.2 | Juspay Hyperswitch before 1.128.0 contains an authentication bypass vulnerability that allows unauthenticated attackers… |
| 2026-10-30 12:16:39 | [CVE-2026-119423](https://nvd.nist.gov/vuln/detail/CVE-2026-119423) | Medium | 6.9 | OPNsense core before 26.7.8 contains a log injection vulnerability that allows unauthenticated attackers to plant victi… |
| 2026-10-30 12:16:39 | [CVE-2026-119424](https://nvd.nist.gov/vuln/detail/CVE-2026-119424) | Medium | 6.1 | OPNsense core before 26.7.8 contains a configuration line injection vulnerability that allows authenticated users with… |
| 2026-10-30 12:16:39 | [CVE-2026-119425](https://nvd.nist.gov/vuln/detail/CVE-2026-119425) | Medium | 5.3 | OPNsense core 26.1.6 through 26.7.7 contains an authentication bypass vulnerability in the captive portal roaming featu… |
| 2026-10-30 12:16:39 | [CVE-2026-119426](https://nvd.nist.gov/vuln/detail/CVE-2026-119426) | High | 7.7 | phpMyAdmin through 5.2.3 contains a cross-site request forgery vulnerability that allows remote attackers to execute ar… |
| 2026-10-30 12:16:39 | [CVE-2026-119427](https://nvd.nist.gov/vuln/detail/CVE-2026-119427) | Low | 2.3 | phpMyAdmin through 5.2.3 contains an sql injection vulnerability in Designer saveSetting() that allows authenticated us… |
| 2026-10-30 12:16:40 | [CVE-2026-119428](https://nvd.nist.gov/vuln/detail/CVE-2026-119428) | Medium | 6.3 | phpMyAdmin through 5.2.3 contains a server-side request forgery vulnerability that allows unauthenticated attackers to… |
| 2026-10-30 12:16:40 | [CVE-2026-119429](https://nvd.nist.gov/vuln/detail/CVE-2026-119429) | Medium | 5.3 | phpMyAdmin through 5.2.3 contains a missing re-authentication vulnerability that allows authenticated attackers to remo… |
| 2026-10-30 12:16:40 | [CVE-2026-119545](https://nvd.nist.gov/vuln/detail/CVE-2026-119545) | Medium | 6.9 | Forgejo through 15.0.11, 16.0.0 through 16.0.7, and 17.0.0 through 17.0.1 contains a server-side request forgery vulner… |
| 2026-10-30 12:16:40 | [CVE-2026-119546](https://nvd.nist.gov/vuln/detail/CVE-2026-119546) | Medium | 6.8 | Forgejo through 15.0.11, 16.0.0 through 16.0.7, and 17.0.0 through 17.0.1 contains a path traversal vulnerability in re… |
| 2026-10-30 12:16:40 | [CVE-2026-119547](https://nvd.nist.gov/vuln/detail/CVE-2026-119547) | Medium | 5.3 | Forgejo through 15.0.11, 16.0.0 through 16.0.7, and 17.0.0 through 17.0.1 contains an information disclosure vulnerabil… |
| 2026-10-30 12:16:41 | [CVE-2026-119548](https://nvd.nist.gov/vuln/detail/CVE-2026-119548) | Low | 2.3 | Lago through 1.55.0 contains an authorization bypass vulnerability in Invoices::Payments::StripeService that allows use… |
| 2026-10-30 12:16:41 | [CVE-2026-119549](https://nvd.nist.gov/vuln/detail/CVE-2026-119549) | High | 7.1 | Jellyfin through 12.4 contains a server-side request forgery vulnerability that lets authenticated users bypass SvgSecu… |
| 2026-10-30 12:16:41 | [CVE-2026-119550](https://nvd.nist.gov/vuln/detail/CVE-2026-119550) | Medium | 5.1 | Jellyfin through 12.4 contains an information disclosure vulnerability in PlaylistsController.GetPlaylist that allows a… |
| 2026-10-30 12:16:41 | [CVE-2026-119551](https://nvd.nist.gov/vuln/detail/CVE-2026-119551) | High | 7.1 | Jellyfin through 12.4 contains an authorization bypass vulnerability in SuggestionsController.GetSuggestions that allow… |
| 2026-10-30 12:16:42 | [CVE-2026-119552](https://nvd.nist.gov/vuln/detail/CVE-2026-119552) | Medium | 6.3 | Uptime Kuma through 2.5.8 contains a race condition in the Socket.IO first-run setup handler that allows unauthenticate… |
| 2026-10-30 12:16:42 | [CVE-2026-119553](https://nvd.nist.gov/vuln/detail/CVE-2026-119553) | High | 7.1 | Moodle 5.3.0, 5.2.0 through 5.2.4, 5.1.0 through 5.1.8, 5.0.0 through 5.0.11, and through 4.5.15 contains a path traver… |
| 2026-10-30 12:16:42 | [CVE-2026-119554](https://nvd.nist.gov/vuln/detail/CVE-2026-119554) | Medium | 6.0 | Moodle 5.3.0, 5.2.0 through 5.2.4, 5.1.0 through 5.1.8, 5.0.0 through 5.0.11, and through 4.5.15 contain an sql injecti… |
| 2026-10-30 12:16:42 | [CVE-2026-119555](https://nvd.nist.gov/vuln/detail/CVE-2026-119555) | Medium | 5.3 | Moodle 4.2.0 through 4.5.15, 5.0.0 through 5.0.11, 5.1.0 through 5.1.8, 5.2.0 through 5.2.4, and 5.3.0 contain an infor… |
| 2026-10-30 12:16:42 | [CVE-2026-119556](https://nvd.nist.gov/vuln/detail/CVE-2026-119556) | Medium | 5.3 | Moodle 4.2.0 through 4.5.15, 5.0.0 through 5.0.11, 5.1.0 through 5.1.8, 5.2.0 through 5.2.4, and 5.3.0 contain a missin… |
| 2026-10-30 12:16:42 | [CVE-2026-119557](https://nvd.nist.gov/vuln/detail/CVE-2026-119557) | High | 8.2 | n8n from 2.14.0 through 2.46.3 contains a path traversal vulnerability in the Databricks node that allows unauthenticat… |
| 2026-10-30 12:16:43 | [CVE-2026-119558](https://nvd.nist.gov/vuln/detail/CVE-2026-119558) | Low | 2.3 | OpenCart through 4.1.0.4 contains a business logic vulnerability that allows logged-in customers to place unpaid full-p… |
| 2026-10-30 12:16:43 | [CVE-2026-119559](https://nvd.nist.gov/vuln/detail/CVE-2026-119559) | High | 8.2 | OpenLiteSpeed through 1.9.4 contains an authentication bypass vulnerability that allows unauthenticated remote attacker… |
| 2026-10-30 12:16:43 | [CVE-2026-119560](https://nvd.nist.gov/vuln/detail/CVE-2026-119560) | Medium | 6.0 | OPNsense core through 26.7.8 contains a configuration injection vulnerability that allows authenticated users to append… |
| 2026-10-30 12:16:43 | [CVE-2026-119561](https://nvd.nist.gov/vuln/detail/CVE-2026-119561) | High | 7.6 | phpMyAdmin through 5.2.3 contains an authentication bypass vulnerability in CustomServer::parseAndValidateAssertionResp… |
| 2026-10-30 12:16:43 | [CVE-2026-119562](https://nvd.nist.gov/vuln/detail/CVE-2026-119562) | Low | 2.3 | phpMyAdmin through 5.2.3 contains an sql injection vulnerability that allows authenticated users to inject SQL by suppl… |
| 2026-10-30 12:16:43 | [CVE-2026-119563](https://nvd.nist.gov/vuln/detail/CVE-2026-119563) | Medium | 5.1 | phpMyAdmin through 5.2.3 contains a stored cross-site scripting vulnerability that allows database users with CREATE pr… |
| 2026-10-30 12:16:43 | [CVE-2026-119564](https://nvd.nist.gov/vuln/detail/CVE-2026-119564) | Medium | 6.0 | Plausible Analytics Community Edition through 3.2.1 contains an information exposure vulnerability that allows site edi… |
| 2026-10-30 12:16:44 | [CVE-2026-119565](https://nvd.nist.gov/vuln/detail/CVE-2026-119565) | Medium | 5.3 | Plausible Analytics through 3.2.1 contains a mass assignment vulnerability in update_traffic_change_notification that a… |
| 2026-10-30 12:16:44 | [CVE-2026-119566](https://nvd.nist.gov/vuln/detail/CVE-2026-119566) | Medium | 6.3 | Prometheus through 3.15.1 contains a credential leak vulnerability that allows attackers to capture Azure AD or Google… |
| 2026-10-30 12:16:44 | [CVE-2026-119567](https://nvd.nist.gov/vuln/detail/CVE-2026-119567) | Low | 2.3 | vsftpd through 3.0.5 contains an access control bypass vulnerability that allows authenticated FTP users to execute den… |
| 2026-10-30 12:16:44 | [CVE-2026-119568](https://nvd.nist.gov/vuln/detail/CVE-2026-119568) | Critical | 9.1 | vsftpd through 3.0.5 contains an authentication bypass vulnerability in ssl_data_accept() that allows unauthenticated a… |
| 2026-10-30 12:16:44 | [CVE-2026-119586](https://nvd.nist.gov/vuln/detail/CVE-2026-119586) | High | 8.5 | SQLite command-line shell through 3.54.1 contains a command injection vulnerability in the .recover command that emits… |
| 2026-10-30 12:16:44 | [CVE-2026-119591](https://nvd.nist.gov/vuln/detail/CVE-2026-119591) | Medium | 6.8 | SQLite before 3.54.0 contains a stack exhaustion vulnerability in countOfViewOptimization() that allows attackers to cr… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
