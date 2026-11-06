# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-11-06 11:21 UTC

New CVEs published between 2026-11-06 10:19 UTC and 2026-11-06 11:21 UTC.

[Full CSV](data/new-cves-2026-11-06T11-21-46-258401Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-11-06 11:17:04 | [CVE-2026-113431](https://nvd.nist.gov/vuln/detail/CVE-2026-113431) | High | 8.7 | Allocation of Resources Without Limits or Throttling vulnerability in ninenines cowlib allows an unauthenticated remote… |
| 2026-11-06 11:17:05 | [CVE-2026-115701](https://nvd.nist.gov/vuln/detail/CVE-2026-115701) | High | 8.2 | Allocation of Resources Without Limits or Throttling vulnerability in ninenines cowboy allows an unauthenticated remote… |
| 2026-11-06 11:17:05 | [CVE-2026-116630](https://nvd.nist.gov/vuln/detail/CVE-2026-116630) | Medium | 5.9 | undici is an HTTP client for Node.js. In versions 7.0.0 through 7.30.1 and 8.0.0 through 8.12.3, when an Agent composes… |
| 2026-11-06 11:17:05 | [CVE-2026-123276](https://nvd.nist.gov/vuln/detail/CVE-2026-123276) | High | 7.8 | In JetBrains CLion before 2026.3, 2026.2.4.1 code execution was possible in Safe Mode via a crafted GDB server debug pr… |
| 2026-11-06 11:17:05 | [CVE-2026-123277](https://nvd.nist.gov/vuln/detail/CVE-2026-123277) | Medium | 5.0 | In JetBrains CLion before 2026.3, 2026.2.4.1 missing authentication allowed local users to obtain the debug session env… |
| 2026-11-06 11:17:06 | [CVE-2026-123278](https://nvd.nist.gov/vuln/detail/CVE-2026-123278) | Medium | 6.7 | In JetBrains IntelliJ IDEA before 2026.3 code execution was possible via the unauthenticated JDBC worker RMI endpoint |
| 2026-11-06 11:17:06 | [CVE-2026-123279](https://nvd.nist.gov/vuln/detail/CVE-2026-123279) | Critical | 9.0 | In JetBrains Datalore before 2026.4 code execution was possible in a notebook's computation by view-only collaborators |
| 2026-11-06 11:17:06 | [CVE-2026-123280](https://nvd.nist.gov/vuln/detail/CVE-2026-123280) | High | 8.1 | In JetBrains Datalore before 2026.2.4 unauthenticated users could execute code via published interactive reports |
| 2026-11-06 11:17:06 | [CVE-2026-123281](https://nvd.nist.gov/vuln/detail/CVE-2026-123281) | High | 7.5 | In JetBrains Datalore before 2026.4 notebook code could execute commands in the sidecar container via the mount broker |
| 2026-11-06 11:17:06 | [CVE-2026-123282](https://nvd.nist.gov/vuln/detail/CVE-2026-123282) | High | 7.4 | In JetBrains Datalore before 2026.4 missing expiration validation of account tokens allowed a new authenticated session |
| 2026-11-06 11:17:06 | [CVE-2026-123283](https://nvd.nist.gov/vuln/detail/CVE-2026-123283) | Medium | 6.8 | In JetBrains Datalore before 2026.4 account takeover was possible via SSO sign-in to a pre-registered account |
| 2026-11-06 11:17:06 | [CVE-2026-123284](https://nvd.nist.gov/vuln/detail/CVE-2026-123284) | Medium | 6.5 | In JetBrains Datalore before 2026.4 improper authorisation on workspace moves allowed view-only collaborators to modify… |
| 2026-11-06 11:17:06 | [CVE-2026-123285](https://nvd.nist.gov/vuln/detail/CVE-2026-123285) | Medium | 6.3 | In JetBrains Datalore before 2026.3 command execution was possible in the database task container via JVM options injec… |
| 2026-11-06 11:17:07 | [CVE-2026-123286](https://nvd.nist.gov/vuln/detail/CVE-2026-123286) | Medium | 5.9 | In JetBrains Datalore before 2026.4 improper authorisation allowed read the notebook owner's file storage session token |
| 2026-11-06 11:17:07 | [CVE-2026-123287](https://nvd.nist.gov/vuln/detail/CVE-2026-123287) | Medium | 5.9 | In JetBrains Datalore before 2026.4 private notebook files could be downloaded without authentication via published int… |
| 2026-11-06 11:17:07 | [CVE-2026-123288](https://nvd.nist.gov/vuln/detail/CVE-2026-123288) | Medium | 5.4 | In JetBrains Datalore before 2026.4 stored XSS in notebook charts was possible via Vega editor link |
| 2026-11-06 11:17:07 | [CVE-2026-123289](https://nvd.nist.gov/vuln/detail/CVE-2026-123289) | Medium | 5.4 | In JetBrains Datalore before 2026.4 improper authorisation allowed notebook viewers to modify files |
| 2026-11-06 11:17:07 | [CVE-2026-123290](https://nvd.nist.gov/vuln/detail/CVE-2026-123290) | Medium | 5.3 | In JetBrains Datalore before 2026.4 hidden notebook code was exposed to unauthenticated users via the public interactiv… |
| 2026-11-06 11:17:07 | [CVE-2026-123291](https://nvd.nist.gov/vuln/detail/CVE-2026-123291) | Medium | 4.3 | In JetBrains Datalore before 2026.4 improper owner validation allowed reading another workspace's issues and runs noteb… |
| 2026-11-06 11:17:07 | [CVE-2026-123292](https://nvd.nist.gov/vuln/detail/CVE-2026-123292) | Low | 2.7 | In JetBrains Datalore before 2026.4 aPI tokens and sessions of removed or banned users remained valid |
| 2026-11-06 11:17:08 | [CVE-2026-123293](https://nvd.nist.gov/vuln/detail/CVE-2026-123293) | High | 7.8 | In JetBrains IntelliJ IDEA before 2026.3, 2026.2.4 code execution was possible in untrusted projects via the Terraform… |
| 2026-11-06 11:17:08 | [CVE-2026-123294](https://nvd.nist.gov/vuln/detail/CVE-2026-123294) | Critical | 9.6 | In JetBrains Hub before 2026.2.52556 privilege escalation was possible by changing email authentication details during… |
| 2026-11-06 11:17:08 | [CVE-2026-123295](https://nvd.nist.gov/vuln/detail/CVE-2026-123295) | High | 8.1 | In JetBrains Hub before 2026.2.52519 enforced two-factor authentication could be disabled via the profile update endpoi… |
| 2026-11-06 11:17:08 | [CVE-2026-123296](https://nvd.nist.gov/vuln/detail/CVE-2026-123296) | High | 7.5 | In JetBrains Hub before 2026.2.52519 privilege escalation via forged email verification was possible |
| 2026-11-06 11:17:08 | [CVE-2026-123297](https://nvd.nist.gov/vuln/detail/CVE-2026-123297) | Medium | 6.8 | In JetBrains Hub before 2026.2.52519 two-factor authentication bypass was possible via the password reset flow |
| 2026-11-06 11:17:08 | [CVE-2026-123298](https://nvd.nist.gov/vuln/detail/CVE-2026-123298) | Medium | 5.0 | In JetBrains Hub before 2026.2.52556 sMTP command injection via email verification was possible |
| 2026-11-06 11:17:08 | [CVE-2026-123299](https://nvd.nist.gov/vuln/detail/CVE-2026-123299) | Low | 3.1 | In JetBrains Hub before 2026.2.52519 information disclosure via user search queries was possible |
| 2026-11-06 11:17:08 | [CVE-2026-123300](https://nvd.nist.gov/vuln/detail/CVE-2026-123300) | Low | 2.7 | In JetBrains Hub before 2026.2.52519 missing authorisation allowed users with read-only access to modify auth module gr… |
| 2026-11-06 11:17:09 | [CVE-2026-123301](https://nvd.nist.gov/vuln/detail/CVE-2026-123301) | High | 8.2 | In JetBrains IntelliJ IDEA before 2026.3 dOM-based XSS in the OpenAPI preview error view was possible |
| 2026-11-06 11:17:09 | [CVE-2026-123302](https://nvd.nist.gov/vuln/detail/CVE-2026-123302) | High | 7.8 | In JetBrains IntelliJ IDEA before 2026.3, 2026.2.4, 2026.1.5.1, 2025.3.6.2 code execution was possible in untrusted pro… |
| 2026-11-06 11:17:09 | [CVE-2026-123304](https://nvd.nist.gov/vuln/detail/CVE-2026-123304) | High | 7.8 | In JetBrains IntelliJ IDEA before 2026.3 code execution in untrusted projects via a configured ShellCheck path |
| 2026-11-06 11:17:09 | [CVE-2026-123305](https://nvd.nist.gov/vuln/detail/CVE-2026-123305) | High | 7.5 | In JetBrains IntelliJ IDEA before 2026.3 path traversal was possible via unpacking Dev Container archives from a remote… |
| 2026-11-06 11:17:09 | [CVE-2026-123306](https://nvd.nist.gov/vuln/detail/CVE-2026-123306) | High | 7.4 | In JetBrains IntelliJ IDEA before 2026.3 improper checks allowed server certificates to be added to the trust store dur… |
| 2026-11-06 11:17:09 | [CVE-2026-123307](https://nvd.nist.gov/vuln/detail/CVE-2026-123307) | Medium | 6.8 | In JetBrains IntelliJ IDEA before 2026.3, 2026.2.4 unauthenticated connection to an arbitrary host via run configuratio… |
| 2026-11-06 11:17:09 | [CVE-2026-123308](https://nvd.nist.gov/vuln/detail/CVE-2026-123308) | Medium | 6.3 | In JetBrains IntelliJ IDEA before 2026.3 code execution via the document import was possible in untrusted projects |
| 2026-11-06 11:17:10 | [CVE-2026-123309](https://nvd.nist.gov/vuln/detail/CVE-2026-123309) | Medium | 6.1 | In JetBrains IntelliJ IDEA before 2026.3, 2026.2.4 stored XSS was possible on the built-in web server via Markdown prev… |
| 2026-11-06 11:17:10 | [CVE-2026-123310](https://nvd.nist.gov/vuln/detail/CVE-2026-123310) | Medium | 5.4 | In JetBrains IntelliJ IDEA before 2026.3 kotlin scripts could trigger dependency downloads from arbitrary repositories… |
| 2026-11-06 11:17:10 | [CVE-2026-123311](https://nvd.nist.gov/vuln/detail/CVE-2026-123311) | Medium | 5.3 | In JetBrains IntelliJ IDEA before 2026.3, 2026.2.4 command execution via a hidden run control in the Markdown preview w… |
| 2026-11-06 11:17:10 | [CVE-2026-123312](https://nvd.nist.gov/vuln/detail/CVE-2026-123312) | Low | 3.3 | In JetBrains IntelliJ IDEA before 2026.3, 2026.2.4 sSRF was possible via annotations.xml files during indexing |
| 2026-11-06 11:17:10 | [CVE-2026-123313](https://nvd.nist.gov/vuln/detail/CVE-2026-123313) | Low | 3.3 | In JetBrains IntelliJ IDEA before 2026.3 improper checks could enable disabled plugins via external dependency settings |
| 2026-11-06 11:17:10 | [CVE-2026-123314](https://nvd.nist.gov/vuln/detail/CVE-2026-123314) | Low | 3.1 | In JetBrains IntelliJ IDEA before 2026.3, 2026.2.4 xXE attack was possible via an XML response to an HTTP Client request |
| 2026-11-06 11:17:10 | [CVE-2026-123315](https://nvd.nist.gov/vuln/detail/CVE-2026-123315) | High | 7.0 | In JetBrains Junie CLI before 26.8.24 command execution was possible via the Allow Similar Commands option |
| 2026-11-06 11:17:11 | [CVE-2026-123316](https://nvd.nist.gov/vuln/detail/CVE-2026-123316) | Medium | 5.5 | In JetBrains Junie CLI before 26.6.29 sensitive environment variables were exposed in session event logs |
| 2026-11-06 11:17:11 | [CVE-2026-123317](https://nvd.nist.gov/vuln/detail/CVE-2026-123317) | High | 8.1 | In JetBrains Ktor before 3.6.1 session forgery was possible via tampered encrypted session cookies |
| 2026-11-06 11:17:11 | [CVE-2026-123318](https://nvd.nist.gov/vuln/detail/CVE-2026-123318) | Medium | 4.8 | In JetBrains Ktor before 3.6.1 hTTP request smuggling was possible in the CIO engine |
| 2026-11-06 11:17:11 | [CVE-2026-123319](https://nvd.nist.gov/vuln/detail/CVE-2026-123319) | Low | 3.7 | In JetBrains Ktor before 3.6.1 missing Domain attribute validation in client cookie storage allowed cookie injection |
| 2026-11-06 11:17:11 | [CVE-2026-123320](https://nvd.nist.gov/vuln/detail/CVE-2026-123320) | Low | 3.1 | In JetBrains Toolbox App before 3.9 insufficient warning in the login dialog allowed connecting to a malicious server |
| 2026-11-06 11:17:11 | [CVE-2026-123321](https://nvd.nist.gov/vuln/detail/CVE-2026-123321) | High | 7.8 | In JetBrains WebStorm before 2026.3, 2026.2.3 code execution via Grunt and Gulp task loading was possible in untrusted… |
| 2026-11-06 11:17:11 | [CVE-2026-123322](https://nvd.nist.gov/vuln/detail/CVE-2026-123322) | Medium | 6.3 | In JetBrains WebStorm before 2026.3, 2026.2.4 code execution was possible in untrusted projects via the Angular CLI sch… |
| 2026-11-06 11:17:11 | [CVE-2026-123323](https://nvd.nist.gov/vuln/detail/CVE-2026-123323) | High | 8.4 | In JetBrains YouTrack before 2025.3.170763, 2026.1.14150, 2026.2.19656 improper URL validation in the app widget host a… |
| 2026-11-06 11:17:12 | [CVE-2026-123324](https://nvd.nist.gov/vuln/detail/CVE-2026-123324) | High | 7.7 | In JetBrains YouTrack before 2026.2.19562 information disclosure via shared mailbox message history was possible |
| 2026-11-06 11:17:12 | [CVE-2026-123325](https://nvd.nist.gov/vuln/detail/CVE-2026-123325) | High | 7.1 | In JetBrains YouTrack before 2025.3.170763, 2026.1.14150, 2026.2.19656 inclusion of untrusted remote code was possible… |
| 2026-11-06 11:17:12 | [CVE-2026-123326](https://nvd.nist.gov/vuln/detail/CVE-2026-123326) | High | 7.1 | In JetBrains YouTrack before 2026.2.19197 incorrect authorisation in the scripts debugger allowed workflow script discl… |
| 2026-11-06 11:17:12 | [CVE-2026-123327](https://nvd.nist.gov/vuln/detail/CVE-2026-123327) | High | 7.5 | In JetBrains YouTrack before 2026.2.19562 missing authorization in the saved query endpoint allowed disclosure of issue… |
| 2026-11-06 11:17:13 | [CVE-2026-123328](https://nvd.nist.gov/vuln/detail/CVE-2026-123328) | Medium | 6.4 | In JetBrains YouTrack before 2026.2.19656 app permission bypass allowed privilege escalation via project tab |
| 2026-11-06 11:17:13 | [CVE-2026-123329](https://nvd.nist.gov/vuln/detail/CVE-2026-123329) | Medium | 5.4 | In JetBrains YouTrack before 2026.2.19562 missing authorization in TeamCity integration allowed disclosure of other pro… |
| 2026-11-06 11:17:13 | [CVE-2026-123330](https://nvd.nist.gov/vuln/detail/CVE-2026-123330) | Medium | 5.4 | In JetBrains YouTrack before 2026.2.19562 missing authorization allowed users with read-only access to change issue vis… |
| 2026-11-06 11:17:13 | [CVE-2026-123331](https://nvd.nist.gov/vuln/detail/CVE-2026-123331) | Medium | 5.4 | In JetBrains YouTrack before 2026.2.19197 article editors could change visibility of restricted child articles |
| 2026-11-06 11:17:13 | [CVE-2026-123332](https://nvd.nist.gov/vuln/detail/CVE-2026-123332) | Medium | 4.7 | In JetBrains YouTrack before 2026.2.19562 missing authorization allowed Project Admin to manage VCS hosting server conf… |
| 2026-11-06 11:17:13 | [CVE-2026-123333](https://nvd.nist.gov/vuln/detail/CVE-2026-123333) | Low | 3.8 | In JetBrains YouTrack before 2026.2.19562 sprint creation allowed moving issues from inaccessible projects between spri… |
| 2026-11-06 11:17:13 | [CVE-2026-123334](https://nvd.nist.gov/vuln/detail/CVE-2026-123334) | Low | 3.8 | In JetBrains YouTrack before 2026.2.19562 project admins of a related project could delete VCS integrations owned by an… |
| 2026-11-06 11:17:13 | [CVE-2026-123335](https://nvd.nist.gov/vuln/detail/CVE-2026-123335) | Low | 3.5 | In JetBrains YouTrack before 2026.2.19562, 2026.1.14137, 2025.3.169041 missing authorization allowed attaching tags to… |
| 2026-11-06 11:17:14 | [CVE-2026-123336](https://nvd.nist.gov/vuln/detail/CVE-2026-123336) | Low | 3.1 | In JetBrains YouTrack before 2026.2.19728 the attachment size limit could be bypassed via AI assistant thread conversion |
| 2026-11-06 11:17:14 | [CVE-2026-123337](https://nvd.nist.gov/vuln/detail/CVE-2026-123337) | Low | 3.1 | In JetBrains YouTrack before 2026.2.19656 users without update permission could change issue visibility |
| 2026-11-06 11:17:16 | [CVE-2026-66293](https://nvd.nist.gov/vuln/detail/CVE-2026-66293) | Low | 2.1 | XML injection in the encoder of Saxy. Saxy.Encoder does not neutralize the -- sequence in XML comment content: escape_c… |
| 2026-11-06 11:17:16 | [CVE-2026-66294](https://nvd.nist.gov/vuln/detail/CVE-2026-66294) | Low | 2.1 | XML injection in the Saxy XML encoder. Saxy.Encoder.cdata/1 serializes a {:cdata, characters} node by wrapping the supp… |
| 2026-11-06 11:17:16 | [CVE-2026-66295](https://nvd.nist.gov/vuln/detail/CVE-2026-66295) | Low | 2.1 | Saxy's XML encoder writes the target and the content of a processing instruction into the output document verbatim, wit… |
| 2026-11-06 11:17:17 | [CVE-2026-84155](https://nvd.nist.gov/vuln/detail/CVE-2026-84155) | Medium | 5.3 | CodeChecker's web server fails to fully invalidate a session token on logout when the server runs with more than one AP… |
| 2026-11-06 11:17:17 | [CVE-2026-84161](https://nvd.nist.gov/vuln/detail/CVE-2026-84161) | Medium | 4.9 | When an operator enables store.analysis_statistics_dir, a network client with PRODUCT_STORE permission for a product ca… |
| 2026-11-06 11:17:17 | [CVE-2026-84164](https://nvd.nist.gov/vuln/detail/CVE-2026-84164) | None | 0.0 | The HTML report that plist-to-html, CodeChecker parse --export html and CodeChecker cmd diff --output html generate put… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
