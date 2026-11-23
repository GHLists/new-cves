# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-11-23 16:19 UTC

New CVEs published between 2026-11-23 15:19 UTC and 2026-11-23 16:19 UTC.

[Full CSV](data/new-cves-2026-11-23T16-19-54-363242Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-11-23 16:17:25 | [CVE-2026-101220](https://nvd.nist.gov/vuln/detail/CVE-2026-101220) | Medium | 5.4 | Dell Enterprise Sonic Distribution, versions prior to 4.6.1, contains an Out-of-bounds Read vulnerability. An unauthent… |
| 2026-11-23 16:17:25 | [CVE-2026-103782](https://nvd.nist.gov/vuln/detail/CVE-2026-103782) | Critical | 9.9 | Dell Enterprise Sonic Distribution, versions prior to 4.6.1, contains an Argument Injection vulnerability. A low privil… |
| 2026-11-23 16:17:25 | [CVE-2026-107784](https://nvd.nist.gov/vuln/detail/CVE-2026-107784) | Medium | 6.3 | On Windows, the tarfile "tar" and "data" extraction filters did not reject member names or link targets that have a dri… |
| 2026-11-23 16:17:26 | [CVE-2026-129975](https://nvd.nist.gov/vuln/detail/CVE-2026-129975) | High | 8.1 | A flaw was found in gpgme. When processing crafted input, an early return following memory reallocation can leave inter… |
| 2026-11-23 16:17:28 | [CVE-2026-132779](https://nvd.nist.gov/vuln/detail/CVE-2026-132779) | Medium | 6.9 | When NGINX Plus or NGINX Open Source is configured to use TLS 1.3 early data using the ssl_early_data on directive, an… |
| 2026-11-23 16:17:29 | [CVE-2026-133632](https://nvd.nist.gov/vuln/detail/CVE-2026-133632) | High | 7.8 | In astro-airflow-mcp 0.5.0 through 0.9.1, the af CLI and the MCP server send telemetry from a Python subprocess that ca… |
| 2026-11-23 16:17:31 | [CVE-2026-134465](https://nvd.nist.gov/vuln/detail/CVE-2026-134465) | Medium | 5.8 | In mcp-server-git before 2026.10.28, the --repository restriction can be bypassed through a nested directory that conta… |
| 2026-11-23 16:17:32 | [CVE-2026-134492](https://nvd.nist.gov/vuln/detail/CVE-2026-134492) | Low | 2.3 | In mcp-server-fetch from 2026.10.10 and before 2026.11.11, the check that blocks requests to non-public addresses treat… |
| 2026-11-23 16:17:36 | [CVE-2026-135078](https://nvd.nist.gov/vuln/detail/CVE-2026-135078) | Medium | 5.1 | A vulnerability has been found in KeudellCoding User Location Map up to 1.2.5. Affected by this vulnerability is an unk… |
| 2026-11-23 16:17:37 | [CVE-2026-135206](https://nvd.nist.gov/vuln/detail/CVE-2026-135206) | High | 7.1 | ToDesktop Builder before 0.36.1 contains a path traversal vulnerability in the todesktop-fs custom protocol handler tha… |
| 2026-11-23 16:17:38 | [CVE-2026-135207](https://nvd.nist.gov/vuln/detail/CVE-2026-135207) | Medium | 5.3 | Healthchecks before 4.4 contains a verification bypass vulnerability that allows project users to mark arbitrary email… |
| 2026-11-23 16:17:38 | [CVE-2026-135208](https://nvd.nist.gov/vuln/detail/CVE-2026-135208) | Critical | 9.3 | Kerberos Agent before 3.14.4 contains an authentication bypass vulnerability that allows unauthenticated attackers to f… |
| 2026-11-23 16:17:38 | [CVE-2026-135209](https://nvd.nist.gov/vuln/detail/CVE-2026-135209) | High | 7.1 | ServerOS Panel before 1.10.1 contains a decompression bomb vulnerability in DeploySourcePacker::extract() that allows a… |
| 2026-11-23 16:17:38 | [CVE-2026-135210](https://nvd.nist.gov/vuln/detail/CVE-2026-135210) | Medium | 5.3 | Plane before 1.5.0 contains a missing authorization vulnerability in WorkspaceDraftIssueViewSet that allows authenticat… |
| 2026-11-23 16:17:38 | [CVE-2026-135211](https://nvd.nist.gov/vuln/detail/CVE-2026-135211) | Critical | 9.2 | BISHENG before 3.0.0 contains a missing authentication vulnerability in the /api/v2/workflow/invoke and /api/v2/workflo… |
| 2026-11-23 16:17:38 | [CVE-2026-135212](https://nvd.nist.gov/vuln/detail/CVE-2026-135212) | Medium | 6.0 | AiSOC before 23.6.1 contains a missing authorization vulnerability in the agents service that allows authenticated user… |
| 2026-11-23 16:17:39 | [CVE-2026-135213](https://nvd.nist.gov/vuln/detail/CVE-2026-135213) | Medium | 5.3 | Worklenz before 3.4.3 contains an insecure direct object reference vulnerability in GET /api/v1/activity-logs/:id that… |
| 2026-11-23 16:17:39 | [CVE-2026-135231](https://nvd.nist.gov/vuln/detail/CVE-2026-135231) | Medium | 5.3 | MISP contains an authorization bypass in the galaxy cluster detachment functionality. Users holding the sync role permi… |
| 2026-11-23 16:17:39 | [CVE-2026-135232](https://nvd.nist.gov/vuln/detail/CVE-2026-135232) | Medium | 5.3 | MISP Collections retained a sharing group reference (sharing_group_id) even when the collection's distribution level wa… |
| 2026-11-23 16:17:39 | [CVE-2026-135233](https://nvd.nist.gov/vuln/detail/CVE-2026-135233) | Medium | 5.3 | MISP's interactive CLI shell, when used to edit or disable a user account, did not update the user record's modificatio… |
| 2026-11-23 16:17:40 | [CVE-2026-135234](https://nvd.nist.gov/vuln/detail/CVE-2026-135234) | Medium | 4.8 | MISP contains a cross-site scripting (XSS) vulnerability in the feed and server event preview pages. When a remote MISP… |
| 2026-11-23 16:17:40 | [CVE-2026-135235](https://nvd.nist.gov/vuln/detail/CVE-2026-135235) | Medium | 4.8 | MISP contains a stored cross-site script (XSS) vulnerability in the event review page used for merge, import, and enric… |
| 2026-11-23 16:17:40 | [CVE-2026-135236](https://nvd.nist.gov/vuln/detail/CVE-2026-135236) | Medium | 6.2 | MISP contains a stored cross-site scripting (XSS) vulnerability in its map attachment rendering. When a GPX or GeoJSON… |
| 2026-11-23 16:17:41 | [CVE-2026-135237](https://nvd.nist.gov/vuln/detail/CVE-2026-135237) | Medium | 6.2 | MISP contains a DOM-based Cross-Site Scripting (XSS) vulnerability in the event report element rendering pipeline. The… |
| 2026-11-23 16:17:41 | [CVE-2026-135238](https://nvd.nist.gov/vuln/detail/CVE-2026-135238) | Medium | 4.8 | MISP contains a cross-site scripting (XSS) vulnerability in the Overmind server preview's analyst data badge component.… |
| 2026-11-23 16:17:42 | [CVE-2026-135239](https://nvd.nist.gov/vuln/detail/CVE-2026-135239) | High | 8.3 | MISP contains an authorization flaw in the data capture and import paths for events, galaxies, galaxy clusters, analyst… |
| 2026-11-23 16:17:42 | [CVE-2026-135240](https://nvd.nist.gov/vuln/detail/CVE-2026-135240) | Medium | 5.3 | MISP contains an authorization bypass in its tag attachment functionality. The endpoints responsible for editing event… |
| 2026-11-23 16:17:42 | [CVE-2026-135241](https://nvd.nist.gov/vuln/detail/CVE-2026-135241) | Medium | 5.3 | MISP contains an authorization bypass vulnerability in the handling of Galaxy and Galaxy Cluster publish/unpublish oper… |
| 2026-11-23 16:17:42 | [CVE-2026-135242](https://nvd.nist.gov/vuln/detail/CVE-2026-135242) | Medium | 6.3 | MISP contains an authorization flaw in the Sharing Group Blueprint execution path. When a blueprint is executed, it rew… |
| 2026-11-23 16:17:43 | [CVE-2026-135243](https://nvd.nist.gov/vuln/detail/CVE-2026-135243) | Medium | 5.3 | MISP contains an authorization bypass vulnerability in the handling of sightings during server synchronization and bulk… |
| 2026-11-23 16:17:43 | [CVE-2026-135244](https://nvd.nist.gov/vuln/detail/CVE-2026-135244) | Medium | 6.9 | MISP trusted client-supplied forwarded IP headers (such as X-Forwarded-For) without verifying that the request originat… |
| 2026-11-23 16:17:43 | [CVE-2026-135245](https://nvd.nist.gov/vuln/detail/CVE-2026-135245) | Medium | 5.3 | MISP's LDAP authentication components (LdapAuth plugin and Apache LDAP authentication) unconditionally re-enabled user… |
| 2026-11-23 16:17:43 | [CVE-2026-135247](https://nvd.nist.gov/vuln/detail/CVE-2026-135247) | Medium | 6.3 | MISP's LinOTPAuth plugin, used for one-time-password authentication against a LinOTP server, did not enforce TLS server… |
| 2026-11-23 16:17:43 | [CVE-2026-135248](https://nvd.nist.gov/vuln/detail/CVE-2026-135248) | Medium | 5.1 | MISP contains a vulnerability in its password reset (forgot password) functionality where the base URL used to construc… |
| 2026-11-23 16:17:44 | [CVE-2026-135249](https://nvd.nist.gov/vuln/detail/CVE-2026-135249) | High | 8.7 | MISP accepted compressed HTTP request bodies (gzip, brotli, zstd) and decompressed them before authentication was perfo… |
| 2026-11-23 16:17:44 | [CVE-2026-135250](https://nvd.nist.gov/vuln/detail/CVE-2026-135250) | High | 7.1 | MISP contains a denial-of-service vulnerability in its image processing pipeline. When generating attachment thumbnails… |
| 2026-11-23 16:17:44 | [CVE-2026-135252](https://nvd.nist.gov/vuln/detail/CVE-2026-135252) | High | 7.1 | MISP contains a Server-Side Request Forgery (SSRF) vulnerability in its feed and sync HTTP request handling. When the a… |
| 2026-11-23 16:17:44 | [CVE-2026-135253](https://nvd.nist.gov/vuln/detail/CVE-2026-135253) | Medium | 5.3 | MISP's NIDS rule export functionality for Snort and Suricata formats does not properly escape user-controlled data befo… |
| 2026-11-23 16:17:44 | [CVE-2026-135254](https://nvd.nist.gov/vuln/detail/CVE-2026-135254) | Medium | 5.1 | MISP is vulnerable to Cross-Site Request Forgery (CSRF) in its correlation management functionality. The top-correlatio… |
| 2026-11-23 16:17:45 | [CVE-2026-135256](https://nvd.nist.gov/vuln/detail/CVE-2026-135256) | High | 7.1 | MISP contains a Regular Expression Denial of Service (ReDoS) vulnerability in its Warninglist feature. Warninglist entr… |
| 2026-11-23 16:17:45 | [CVE-2026-135257](https://nvd.nist.gov/vuln/detail/CVE-2026-135257) | Medium | 5.3 | MISP contains an improper output sanitization vulnerability in the Zeek (Bro) intelligence export functionality. The ex… |
| 2026-11-23 16:17:45 | [CVE-2026-135258](https://nvd.nist.gov/vuln/detail/CVE-2026-135258) | High | 7.1 | MISP contains multiple related authorization and input-validation flaws in its object editing and attachment handling w… |
| 2026-11-23 16:17:45 | [CVE-2026-135259](https://nvd.nist.gov/vuln/detail/CVE-2026-135259) | Medium | 5.3 | MISP contains a type confusion vulnerability in the authentication key creation endpoint. When a user submits a floatin… |
| 2026-11-23 16:17:46 | [CVE-2026-135260](https://nvd.nist.gov/vuln/detail/CVE-2026-135260) | Medium | 6.9 | MISP contains multiple flaws in its login and one-time-password (OTP) brute-force lockout mechanism that collectively w… |
| 2026-11-23 16:17:46 | [CVE-2026-135261](https://nvd.nist.gov/vuln/detail/CVE-2026-135261) | Medium | 6.9 | MISP's brute-force lockout mechanism for login and one-time-password (OTP) authentication is susceptible to bypass thro… |
| 2026-11-23 16:17:46 | [CVE-2026-135262](https://nvd.nist.gov/vuln/detail/CVE-2026-135262) | Medium | 6.2 | MISP contains a DOM-based cross-site scripting (XSS) vulnerability in the Pivot Explorer component. The bundled pivotic… |
| 2026-11-23 16:18:05 | [CVE-2026-96457](https://nvd.nist.gov/vuln/detail/CVE-2026-96457) | High | 7.7 | A flaw was found in the administrative interface of Keycloak, an identity and access management solution. The issue occ… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
