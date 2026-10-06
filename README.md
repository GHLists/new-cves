# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-06 20:19 UTC

New CVEs published between 2026-10-06 19:18 UTC and 2026-10-06 20:19 UTC.

[Full CSV](data/new-cves-2026-10-06T20-19-47-104688Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-10-06 20:17:08 | [CVE-2026-101027](https://nvd.nist.gov/vuln/detail/CVE-2026-101027) |  |  | When `[migrations] ALLOWED_DOMAINS` was configured, a hostname matching the allow list was accepted without checking it… |
| 2026-10-06 20:17:08 | [CVE-2026-101029](https://nvd.nist.gov/vuln/detail/CVE-2026-101029) |  |  | Gitea's repository migration and pull mirror egress checks could be bypassed with a hostname that returns multiple DNS… |
| 2026-10-06 20:17:08 | [CVE-2026-101149](https://nvd.nist.gov/vuln/detail/CVE-2026-101149) | Medium | 5.1 | Insufficient validation of OIDC SSO provider configuration could allow a user with specific high privileges to direct r… |
| 2026-10-06 20:17:08 | [CVE-2026-101150](https://nvd.nist.gov/vuln/detail/CVE-2026-101150) | Medium | 5.1 | Insufficient validation of OIDC bearer token configuration could allow a user with specific high privileges to direct r… |
| 2026-10-06 20:17:09 | [CVE-2026-101151](https://nvd.nist.gov/vuln/detail/CVE-2026-101151) | Medium | 5.3 | Insufficient validation of request in login flow could allow a remote, unauthenticated attacker to craft a URL that, wh… |
| 2026-10-06 20:17:09 | [CVE-2026-101152](https://nvd.nist.gov/vuln/detail/CVE-2026-101152) | High | 7.6 | Insufficient validation in the Single Sign-On (SSO) login flow could allow a remote, unauthenticated attacker to craft… |
| 2026-10-06 20:17:09 | [CVE-2026-101153](https://nvd.nist.gov/vuln/detail/CVE-2026-101153) | High | 7.2 | On affected versions of CloudVision Portal (on-premises) or CloudVision Sensor, a path traversal vulnerability exists.… |
| 2026-10-06 20:17:09 | [CVE-2026-101154](https://nvd.nist.gov/vuln/detail/CVE-2026-101154) | High | 8.6 | An authenticated remote attacker with specific permissions can read or write files on the platform filesystem beyond th… |
| 2026-10-06 20:17:09 | [CVE-2026-101155](https://nvd.nist.gov/vuln/detail/CVE-2026-101155) | High | 8.6 | An authenticated remote attacker with specific permissions can read or write files on the platform filesystem beyond th… |
| 2026-10-06 20:17:09 | [CVE-2026-101156](https://nvd.nist.gov/vuln/detail/CVE-2026-101156) | Medium | 6.2 | A stored cross-site scripting (XSS) vulnerability may allow an authenticated, high-privilege administrator to store mal… |
| 2026-10-06 20:17:09 | [CVE-2026-101157](https://nvd.nist.gov/vuln/detail/CVE-2026-101157) | Critical | 9.3 | A stored cross-site scripting (XSS) vulnerability may allow an unauthenticated attacker with adjacent-network access to… |
| 2026-10-06 20:17:10 | [CVE-2026-101158](https://nvd.nist.gov/vuln/detail/CVE-2026-101158) | Critical | 9.3 | A missing input validation vulnerability in the Fileserver upload API allows an authenticated attacker with file upload… |
| 2026-10-06 20:17:10 | [CVE-2026-102155](https://nvd.nist.gov/vuln/detail/CVE-2026-102155) | High | 7.1 | An XML External Entity (XXE) injection vulnerability in the WiFi-server Spectralight application allows any authenticat… |
| 2026-10-06 20:17:10 | [CVE-2026-102156](https://nvd.nist.gov/vuln/detail/CVE-2026-102156) | Medium | 6.9 | Improper neutralization of Lightweight Directory Access Protocol (LDAP) authentication input may allow an unauthenticat… |
| 2026-10-06 20:17:10 | [CVE-2026-102157](https://nvd.nist.gov/vuln/detail/CVE-2026-102157) | Medium | 6.0 | An insecure direct object reference (IDOR) vulnerability in a CloudVision CUE file-serving interface may allow an authe… |
| 2026-10-06 20:17:10 | [CVE-2026-102158](https://nvd.nist.gov/vuln/detail/CVE-2026-102158) | High | 7.1 | Improper validation of selected CloudVision CUE application programming interface (API) request parameters may allow an… |
| 2026-10-06 20:17:10 | [CVE-2026-102159](https://nvd.nist.gov/vuln/detail/CVE-2026-102159) | Critical | 9.3 | An access-control flaw in the CV-CUE backend may allow an unauthenticated network attacker to access functionality inte… |
| 2026-10-06 20:17:11 | [CVE-2026-102160](https://nvd.nist.gov/vuln/detail/CVE-2026-102160) | High | 8.6 | An operating system (OS) command injection vulnerability in CloudVision CUE backup management may allow an authenticate… |
| 2026-10-06 20:17:11 | [CVE-2026-102161](https://nvd.nist.gov/vuln/detail/CVE-2026-102161) | High | 8.7 | An unauthenticated attacker located on an adjacent private network (or any attacker routed through a reverse proxy/load… |
| 2026-10-06 20:17:11 | [CVE-2026-102162](https://nvd.nist.gov/vuln/detail/CVE-2026-102162) | Critical | 9.4 | On affected Arista Wi-Fi access points with captive portal, or application firewall enabled on at least one SSID, a vul… |
| 2026-10-06 20:17:11 | [CVE-2026-102163](https://nvd.nist.gov/vuln/detail/CVE-2026-102163) | High | 8.7 | On affected Arista access points with Wireless Intrusion Prevention System (WIPS) active, an unauthenticated attacker w… |
| 2026-10-06 20:17:11 | [CVE-2026-102164](https://nvd.nist.gov/vuln/detail/CVE-2026-102164) | Low | 2.3 | On affected Arista access points configured with VXLAN tunnelling and L2-proxy (a specific configuration unique to the… |
| 2026-10-06 20:17:11 | [CVE-2026-102165](https://nvd.nist.gov/vuln/detail/CVE-2026-102165) | High | 7.7 | On affected Arista Wi-Fi access points, an unauthenticated attacker with network access to the capture service can send… |
| 2026-10-06 20:17:11 | [CVE-2026-102167](https://nvd.nist.gov/vuln/detail/CVE-2026-102167) | Critical | 9.0 | On affected Arista Wi-Fi access points, a memory corruption vulnerability exists in access point's wired uplink network… |
| 2026-10-06 20:17:12 | [CVE-2026-102168](https://nvd.nist.gov/vuln/detail/CVE-2026-102168) | High | 7.1 | On affected Arista Wi-Fi access points with Captive Portal enabled, an unauthenticated wireless client connected to a C… |
| 2026-10-06 20:17:12 | [CVE-2026-102169](https://nvd.nist.gov/vuln/detail/CVE-2026-102169) | High | 7.1 | On affected Arista Wi-Fi access points with Captive Portal enabled, an unauthenticated wireless client connected to a c… |
| 2026-10-06 20:17:12 | [CVE-2026-102404](https://nvd.nist.gov/vuln/detail/CVE-2026-102404) | Medium | 6.5 | Uncontrolled Resource Consumption (CWE-400) in Elasticsearch can lead to denial of service via Excessive Allocation (CA… |
| 2026-10-06 20:17:12 | [CVE-2026-102406](https://nvd.nist.gov/vuln/detail/CVE-2026-102406) | High | 8.8 | Authorization Bypass Through User-Controlled Key (CWE-639) in Kibana could lead to cross-tenant data interception. In t… |
| 2026-10-06 20:17:12 | [CVE-2026-102407](https://nvd.nist.gov/vuln/detail/CVE-2026-102407) | Medium | 5.4 | Incorrect Authorization (CWE-863) in Elasticsearch can lead to unauthorized data stream modification via Accessing Func… |
| 2026-10-06 20:17:12 | [CVE-2026-102408](https://nvd.nist.gov/vuln/detail/CVE-2026-102408) | Medium | 4.3 | Inefficient Regular Expression Complexity (CWE-1333) in Elasticsearch can lead to denial of service via Regular Express… |
| 2026-10-06 20:17:12 | [CVE-2026-102409](https://nvd.nist.gov/vuln/detail/CVE-2026-102409) | Medium | 6.5 | Uncontrolled Recursion (CWE-674) in Elasticsearch can allow an authenticated user with low privileges to terminate an E… |
| 2026-10-06 20:17:13 | [CVE-2026-102410](https://nvd.nist.gov/vuln/detail/CVE-2026-102410) | Medium | 4.3 | Missing Authorization (CWE-862) in Kibana can lead to information disclosure via Accessing Functionality Not Properly C… |
| 2026-10-06 20:17:13 | [CVE-2026-102411](https://nvd.nist.gov/vuln/detail/CVE-2026-102411) | Medium | 6.5 | Allocation of Resources Without Limits or Throttling (CWE-770) in Elasticsearch can lead to Denial of Service via Exces… |
| 2026-10-06 20:17:13 | [CVE-2026-102412](https://nvd.nist.gov/vuln/detail/CVE-2026-102412) | Medium | 6.5 | Incorrect Authorization (CWE-863) in Kibana can lead to sensitive information disclosure via Accessing Functionality No… |
| 2026-10-06 20:17:13 | [CVE-2026-102413](https://nvd.nist.gov/vuln/detail/CVE-2026-102413) | Medium | 6.2 | Uncaught Exception (CWE-248) in Elastic Endpoint can lead to denial of service via a specially crafted file name. When… |
| 2026-10-06 20:17:13 | [CVE-2026-103005](https://nvd.nist.gov/vuln/detail/CVE-2026-103005) | Medium | 6.5 | Memory Allocation with Excessive Size Value (CWE-789) in Elasticsearch can lead to denial of service via Excessive Allo… |
| 2026-10-06 20:17:13 | [CVE-2026-103006](https://nvd.nist.gov/vuln/detail/CVE-2026-103006) | Medium | 6.5 | Uncontrolled Recursion (CWE-674) in Elasticsearch can lead to Denial of Service via a specially crafted, deeply nested… |
| 2026-10-06 20:17:13 | [CVE-2026-103007](https://nvd.nist.gov/vuln/detail/CVE-2026-103007) | High | 7.2 | Incorrect Authorization (CWE-863) in Elasticsearch can lead to Privilege Escalation via a delegated administrative priv… |
| 2026-10-06 20:17:14 | [CVE-2026-103008](https://nvd.nist.gov/vuln/detail/CVE-2026-103008) | Medium | 6.5 | Uncontrolled Recursion (CWE-674) in Elasticsearch can lead to Denial of Service via a specially crafted request that ca… |
| 2026-10-06 20:17:14 | [CVE-2026-103009](https://nvd.nist.gov/vuln/detail/CVE-2026-103009) | High | 7.1 | Authorization Bypass Through User-Controlled Key (CWE-639) in Elasticsearch can lead to Information Disclosure via a sp… |
| 2026-10-06 20:17:14 | [CVE-2026-103059](https://nvd.nist.gov/vuln/detail/CVE-2026-103059) |  |  | When Gitea's built-in SSH server is enabled (`START_SSH_SERVER = true`), the presented public key was looked up with an… |
| 2026-10-06 20:17:14 | [CVE-2026-103504](https://nvd.nist.gov/vuln/detail/CVE-2026-103504) |  |  | Changing an organization team's permission through the API with only the `permission` field did not rebuild the team's… |
| 2026-10-06 20:17:14 | [CVE-2026-103667](https://nvd.nist.gov/vuln/detail/CVE-2026-103667) |  |  | Gitea's container registry served blob downloads with a `Content-Type` taken from the media type declared in pushed ima… |
| 2026-10-06 20:17:14 | [CVE-2026-103670](https://nvd.nist.gov/vuln/detail/CVE-2026-103670) |  |  | When a Gitea Actions run was inserted, older runs in the same workflow-level concurrency group were cancelled without c… |
| 2026-10-06 20:17:14 | [CVE-2026-104047](https://nvd.nist.gov/vuln/detail/CVE-2026-104047) | Medium | 5.3 | A flaw was found in SSSD. When configured to use Microsoft Entra ID, search inputs are not properly sanitized before be… |
| 2026-10-06 20:17:14 | [CVE-2026-104048](https://nvd.nist.gov/vuln/detail/CVE-2026-104048) | Medium | 6.8 | A flaw was found in SSSD. In trust-enabled identity management environments, SSSD evaluates Host-Based Access Control (… |
| 2026-10-06 20:17:15 | [CVE-2026-104626](https://nvd.nist.gov/vuln/detail/CVE-2026-104626) |  |  | A user who can open a fork pull request can place workflow content with a shared run-level concurrency group into a Git… |
| 2026-10-06 20:17:15 | [CVE-2026-104632](https://nvd.nist.gov/vuln/detail/CVE-2026-104632) |  |  | Gitea Actions blocks the jobs of workflow runs from first-time fork pull request contributors until a maintainer approv… |
| 2026-10-06 20:17:15 | [CVE-2026-104636](https://nvd.nist.gov/vuln/detail/CVE-2026-104636) |  |  | Gitea validated the initial remote URL for push mirrors, wiki remote checks, and fetches of migrated pull request heads… |
| 2026-10-06 20:17:15 | [CVE-2026-105111](https://nvd.nist.gov/vuln/detail/CVE-2026-105111) | Low | 2.3 | Improper neutralization of input during web page generation ('cross-site scripting') vulnerability in Apache Commons BC… |
| 2026-10-06 20:17:15 | [CVE-2026-105239](https://nvd.nist.gov/vuln/detail/CVE-2026-105239) | Medium | 5.3 | Improper Neutralization of Null Byte or NUL Character vulnerability in the EventLogAppender of Apache log4net. A NUL ch… |
| 2026-10-06 20:17:15 | [CVE-2026-105240](https://nvd.nist.gov/vuln/detail/CVE-2026-105240) | Medium | 5.3 | Improper Neutralization of Null Byte or NUL Character vulnerability in the OutputDebugStringAppender of Apache log4net.… |
| 2026-10-06 20:17:15 | [CVE-2026-105241](https://nvd.nist.gov/vuln/detail/CVE-2026-105241) | Medium | 5.3 | Improper Handling of Unicode Encoding vulnerability in the SmtpPickupDirAppender of Apache log4net. Content that the ma… |
| 2026-10-06 20:17:16 | [CVE-2026-105242](https://nvd.nist.gov/vuln/detail/CVE-2026-105242) | Medium | 5.3 | Improper Handling of Exceptional Conditions vulnerability in the aspnet-request pattern converter of Apache log4net. Re… |
| 2026-10-06 20:17:16 | [CVE-2026-105243](https://nvd.nist.gov/vuln/detail/CVE-2026-105243) | Medium | 5.3 | Insufficient Logging vulnerability in the EventLogAppender of Apache log4net. Long messages were truncated to a fixed s… |
| 2026-10-06 20:17:16 | [CVE-2026-105244](https://nvd.nist.gov/vuln/detail/CVE-2026-105244) | Medium | 5.3 | Improper Encoding or Escaping of Output vulnerability in the RemoteSyslogAppender of Apache log4net. Every character ou… |
| 2026-10-06 20:17:17 | [CVE-2026-106063](https://nvd.nist.gov/vuln/detail/CVE-2026-106063) | Medium | 6.3 | A heap-based buffer overflow was found in GIMP’s DICOM export plug-in. When exporting an image with extremely large wid… |
| 2026-10-06 20:17:26 | [CVE-2026-106444](https://nvd.nist.gov/vuln/detail/CVE-2026-106444) | Medium | 4.7 | Handlebars provides the power necessary to let users build semantic templates. From 4.0.0 until 4.7.10, Handlebars.prec… |
| 2026-10-06 20:17:26 | [CVE-2026-106445](https://nvd.nist.gov/vuln/detail/CVE-2026-106445) | Critical | 9.2 | Handlebars provides the power necessary to let users build semantic templates. From 4.0.0 until 4.7.10, Handlebars look… |
| 2026-10-06 20:17:26 | [CVE-2026-106446](https://nvd.nist.gov/vuln/detail/CVE-2026-106446) | Critical | 9.8 | Handlebars provides the power necessary to let users build semantic templates. From 4.0.0 until 4.7.10, Handlebars.comp… |
| 2026-10-06 20:17:26 | [CVE-2026-106447](https://nvd.nist.gov/vuln/detail/CVE-2026-106447) | High | 8.7 | StableLib is a stable library of useful TypeScript and JavaScript code. Prior to 2.0.4, the @stablelib/cbor decoder rec… |
| 2026-10-06 20:17:26 | [CVE-2026-106448](https://nvd.nist.gov/vuln/detail/CVE-2026-106448) | High | 8.9 | StableLib is a stable library of useful TypeScript and JavaScript code. Prior to 2.0.4, the @stablelib/cbor CBOR map de… |
| 2026-10-06 20:17:26 | [CVE-2026-106449](https://nvd.nist.gov/vuln/detail/CVE-2026-106449) | Low | 3.7 | yawkat LZ4 Java provides LZ4 compression for Java. Prior to 1.11.4, net.jpountz.lz4.LZ4BlockInputStream configured with… |
| 2026-10-06 20:17:27 | [CVE-2026-106450](https://nvd.nist.gov/vuln/detail/CVE-2026-106450) | Medium | 5.3 | yawkat LZ4 Java provides LZ4 compression for Java. Prior to 1.11.4, net.jpountz.lz4.LZ4FrameInputStream readHeader() al… |
| 2026-10-06 20:17:27 | [CVE-2026-106451](https://nvd.nist.gov/vuln/detail/CVE-2026-106451) | High | 7.3 | yawkat LZ4 Java provides LZ4 compression for Java. From 1.7.0 until 1.11.4, net.jpountz.util.Native.load() uses File.cr… |
| 2026-10-06 20:17:27 | [CVE-2026-106452](https://nvd.nist.gov/vuln/detail/CVE-2026-106452) | Medium | 5.3 | yawkat LZ4 Java provides LZ4 compression for Java. Prior to 1.11.2, net.jpountz.lz4.LZ4BlockInputStream refill() valida… |
| 2026-10-06 20:17:27 | [CVE-2026-106453](https://nvd.nist.gov/vuln/detail/CVE-2026-106453) | Medium | 5.3 | yawkat LZ4 Java provides LZ4 compression for Java. Prior to 1.11.2, LZ4DecompressorWithLength uses getDecompressedLengt… |
| 2026-10-06 20:17:27 | [CVE-2026-106454](https://nvd.nist.gov/vuln/detail/CVE-2026-106454) | Medium | 4.3 | Twisted is an event-based framework for internet applications, supporting Python 3.6+. In 25.5.0 and earlier, wildcardT… |
| 2026-10-06 20:17:28 | [CVE-2026-70357](https://nvd.nist.gov/vuln/detail/CVE-2026-70357) |  |  | Gitea validates a repository migration hostname against its network allow and block lists before invoking Git, but the… |
| 2026-10-06 20:17:29 | [CVE-2026-76061](https://nvd.nist.gov/vuln/detail/CVE-2026-76061) | Medium | 5.5 | A flaw was found in CRI-O's `bind_mount_prefix` handling. When configured with a non-empty `bind_mount_prefix`, a malic… |
| 2026-10-06 20:17:29 | [CVE-2026-76741](https://nvd.nist.gov/vuln/detail/CVE-2026-76741) | Medium | 6.5 | Buffer overflow vulnerabilities exist in the affected interface of AOS-S. Successful exploitation could allow an authen… |
| 2026-10-06 20:17:29 | [CVE-2026-76742](https://nvd.nist.gov/vuln/detail/CVE-2026-76742) | Critical | 9.8 | Authentication bypass vulnerabilities exist in the web management interface of AOS-S. Successful exploitation could all… |
| 2026-10-06 20:17:29 | [CVE-2026-76743](https://nvd.nist.gov/vuln/detail/CVE-2026-76743) | Critical | 9.8 | A vulnerability have been identified in the management interface of AOS-S that could potentially allow an unauthenticat… |
| 2026-10-06 20:17:29 | [CVE-2026-76744](https://nvd.nist.gov/vuln/detail/CVE-2026-76744) | Critical | 9.8 | Buffer overflow vulnerabilities exist in the affected interface of AOS-S. Successful exploitation could allow an unauth… |
| 2026-10-06 20:17:29 | [CVE-2026-76745](https://nvd.nist.gov/vuln/detail/CVE-2026-76745) | Critical | 9.6 | Memory corruption vulnerabilities exist in AOS-S that are reachable by an unauthenticated adjacent attacker. Successful… |
| 2026-10-06 20:17:29 | [CVE-2026-76746](https://nvd.nist.gov/vuln/detail/CVE-2026-76746) | Critical | 9.3 | An unauthenticated buffer overflow vulnerability exists in AOS-S. Successful exploitation could allow an unauthenticate… |
| 2026-10-06 20:17:29 | [CVE-2026-73278](https://nvd.nist.gov/vuln/detail/CVE-2026-73278) |  |  | Gitea's OAuth2 and OpenID Connect sign-in paths do not require a WebAuthn challenge when WebAuthn is the account's only… |
| 2026-10-06 20:17:30 | [CVE-2026-76747](https://nvd.nist.gov/vuln/detail/CVE-2026-76747) | Critical | 9.1 | Buffer overflow vulnerabilities exist in the affected interface of AOS-S. Successful exploitation could allow an unauth… |
| 2026-10-06 20:17:30 | [CVE-2026-76748](https://nvd.nist.gov/vuln/detail/CVE-2026-76748) | High | 8.8 | A privilege escalation vulnerability exists in the API of AOS-S. Successful exploitation could allow an authenticated r… |
| 2026-10-06 20:17:30 | [CVE-2026-76749](https://nvd.nist.gov/vuln/detail/CVE-2026-76749) | Medium | 6.5 | A sensitive information disclosure vulnerability exists in AOS-S. Successful exploitation could allow an unauthenticate… |
| 2026-10-06 20:17:30 | [CVE-2026-76750](https://nvd.nist.gov/vuln/detail/CVE-2026-76750) | Critical | 9.8 | Deserialization of untrusted data vulnerabilities exist in the web interface of HPE Networking ClearPass Policy Manager… |
| 2026-10-06 20:17:30 | [CVE-2026-76751](https://nvd.nist.gov/vuln/detail/CVE-2026-76751) | Critical | 9.8 | A missing integrity verification vulnerability exists in the OnGuard agent of ClearPass Policy Manager. Successful expl… |
| 2026-10-06 20:17:30 | [CVE-2026-76752](https://nvd.nist.gov/vuln/detail/CVE-2026-76752) | Critical | 9.8 | Authentication bypass vulnerabilities exist in the web-based management and API interfaces of HPE Networking ClearPass… |
| 2026-10-06 20:17:30 | [CVE-2026-76753](https://nvd.nist.gov/vuln/detail/CVE-2026-76753) | Critical | 9.8 | A format string vulnerability in an affected service interface of HPE Networking ClearPass Policy Manager could allow a… |
| 2026-10-06 20:17:30 | [CVE-2026-76754](https://nvd.nist.gov/vuln/detail/CVE-2026-76754) | Critical | 9.8 | A vulnerability in an affected interface of ClearPass Policy Manager could allow an unauthenticated remote attacker to… |
| 2026-10-06 20:17:30 | [CVE-2026-79794](https://nvd.nist.gov/vuln/detail/CVE-2026-79794) | Critical | 9.1 | A SQL injection vulnerability in the web-based management interface of ClearPass Policy Manager could allow an authenti… |
| 2026-10-06 20:17:31 | [CVE-2026-79796](https://nvd.nist.gov/vuln/detail/CVE-2026-79796) | Critical | 9.8 | Vulnerabilities have been identified in the affected interface of ClearPass Policy Manager that could potentially allow… |
| 2026-10-06 20:17:31 | [CVE-2026-79797](https://nvd.nist.gov/vuln/detail/CVE-2026-79797) | High | 8.8 | An improper access control vulnerability exists in the Android client application for HPE Networking ClearPass Policy M… |
| 2026-10-06 20:17:31 | [CVE-2026-79798](https://nvd.nist.gov/vuln/detail/CVE-2026-79798) | Critical | 9.9 | SQL injection vulnerabilities in the web-based management interface of ClearPass Policy Manager could allow a low-privi… |
| 2026-10-06 20:17:31 | [CVE-2026-79799](https://nvd.nist.gov/vuln/detail/CVE-2026-79799) | High | 8.8 | A vulnerability in the web-based management interface of ClearPass Policy Manager could allow an unauthenticated remote… |
| 2026-10-06 20:17:31 | [CVE-2026-79800](https://nvd.nist.gov/vuln/detail/CVE-2026-79800) | High | 8.8 | An authenticated path traversal vulnerability exists in the command line interface of ClearPass Policy Manager. Success… |
| 2026-10-06 20:17:31 | [CVE-2026-79801](https://nvd.nist.gov/vuln/detail/CVE-2026-79801) | Critical | 9.8 | A missing integrity verification vulnerability in the client agent software of HPE Networking ClearPass Policy Manager… |
| 2026-10-06 20:17:31 | [CVE-2026-79802](https://nvd.nist.gov/vuln/detail/CVE-2026-79802) | High | 8.8 | A command injection vulnerability exists in the client software of ClearPass Policy Manager. Successful exploitation co… |
| 2026-10-06 20:17:31 | [CVE-2026-79803](https://nvd.nist.gov/vuln/detail/CVE-2026-79803) | High | 8.8 | A command injection vulnerability exists in the API of ClearPass Policy Manager. Successful exploitation could allow an… |
| 2026-10-06 20:17:32 | [CVE-2026-79805](https://nvd.nist.gov/vuln/detail/CVE-2026-79805) | Critical | 9.8 | An authenticated path traversal vulnerability exists in ClearPass Policy Manager. Successful exploitation could allow a… |
| 2026-10-06 20:17:32 | [CVE-2026-79806](https://nvd.nist.gov/vuln/detail/CVE-2026-79806) | High | 7.8 | A privilege escalation vulnerability in the ClearPass Policy Manager OnGuard Linux agent could allow malicious users on… |
| 2026-10-06 20:17:32 | [CVE-2026-79807](https://nvd.nist.gov/vuln/detail/CVE-2026-79807) | High | 7.8 | A missing integrity verification vulnerability in the Windows client software for ClearPass Policy Manager could allow… |
| 2026-10-06 20:17:32 | [CVE-2026-79808](https://nvd.nist.gov/vuln/detail/CVE-2026-79808) | High | 7.8 | A buffer overflow vulnerability exists in the OnGuard agent of ClearPass Policy Manager. Successful exploitation could… |
| 2026-10-06 20:17:32 | [CVE-2026-79809](https://nvd.nist.gov/vuln/detail/CVE-2026-79809) | High | 7.3 | An unauthenticated path traversal vulnerability exists in an API endpoint of ClearPass Policy Manager. Successful explo… |
| 2026-10-06 20:17:32 | [CVE-2026-79810](https://nvd.nist.gov/vuln/detail/CVE-2026-79810) | High | 7.2 | Remote code execution vulnerabilities exist in the affected interface of HPE Networking ClearPass Policy Manager that c… |
| 2026-10-06 20:17:32 | [CVE-2026-79811](https://nvd.nist.gov/vuln/detail/CVE-2026-79811) | High | 7.2 | A SQL injection vulnerability in the API of ClearPass Policy Manager could allow a remote authenticated attacker with a… |
| 2026-10-06 20:17:32 | [CVE-2026-79812](https://nvd.nist.gov/vuln/detail/CVE-2026-79812) | Medium | 6.1 | A denial of service vulnerability exists in the OnGuard agent of HPE Networking ClearPass Policy Manager. Successful ex… |
| 2026-10-06 20:17:32 | [CVE-2026-79813](https://nvd.nist.gov/vuln/detail/CVE-2026-79813) | Medium | 6.7 | A local privilege escalation vulnerability exists in the ClearPass client software. Successful exploitation could allow… |
| 2026-10-06 20:17:33 | [CVE-2026-79814](https://nvd.nist.gov/vuln/detail/CVE-2026-79814) | Medium | 6.7 | An arbitrary file write vulnerability in the ClearPass Policy Manager OnGuard agent could allow malicious users on a lo… |
| 2026-10-06 20:17:33 | [CVE-2026-79815](https://nvd.nist.gov/vuln/detail/CVE-2026-79815) | Medium | 6.5 | A command injection vulnerability in the OnGuard agent of ClearPass Policy Manager could allow an authenticated remote… |
| 2026-10-06 20:17:33 | [CVE-2026-79816](https://nvd.nist.gov/vuln/detail/CVE-2026-79816) | Medium | 6.3 | A vulnerability in a client interface of HPE Networking ClearPass Policy Manager could allow an unauthenticated remote… |
| 2026-10-06 20:17:33 | [CVE-2026-79817](https://nvd.nist.gov/vuln/detail/CVE-2026-79817) | Medium | 5.5 | A sensitive information disclosure vulnerability exists in the client software of HPE Networking ClearPass Policy Manag… |
| 2026-10-06 20:17:33 | [CVE-2026-79818](https://nvd.nist.gov/vuln/detail/CVE-2026-79818) | Medium | 5.3 | A vulnerability in an API interface of ClearPass Policy Manager could allow an unauthenticated remote attacker to circu… |
| 2026-10-06 20:17:33 | [CVE-2026-79960](https://nvd.nist.gov/vuln/detail/CVE-2026-79960) |  |  | When a push was authenticated with a deploy key, Gitea recorded the repository owner as the pusher, so permission check… |
| 2026-10-06 20:17:34 | [CVE-2026-89430](https://nvd.nist.gov/vuln/detail/CVE-2026-89430) |  |  | Gitea validated a push mirror's remote address against the `[migrations]` allow and block lists only when the mirror wa… |
| 2026-10-06 20:17:34 | [CVE-2026-94114](https://nvd.nist.gov/vuln/detail/CVE-2026-94114) | High | 8.2 | Symbolic name not mapping to correct object vulnerability in Apache Commons. BCEL caches attacker-controlled classes un… |
| 2026-10-06 20:17:34 | [CVE-2026-94205](https://nvd.nist.gov/vuln/detail/CVE-2026-94205) |  |  | Gitea Actions decided whether a fork pull request run needed approval based on the user who triggered the event rather… |
| 2026-10-06 20:17:34 | [CVE-2026-95106](https://nvd.nist.gov/vuln/detail/CVE-2026-95106) |  |  | Gitea accepted pushed Git trees containing two entries with the same name, which Git's own consistency checks reject. G… |
| 2026-10-06 20:17:34 | [CVE-2026-95112](https://nvd.nist.gov/vuln/detail/CVE-2026-95112) |  |  | When processing issue and comment bodies, Gitea scanned the entire preceding text for action keywords such as "closes"… |
| 2026-10-06 20:17:35 | [CVE-2026-96399](https://nvd.nist.gov/vuln/detail/CVE-2026-96399) |  |  | A repository's external issue tracker regular expression containing alternating capture groups could produce invalid sl… |
| 2026-10-06 20:17:35 | [CVE-2026-96400](https://nvd.nist.gov/vuln/detail/CVE-2026-96400) |  |  | With `[migrations] ALLOWED_DOMAINS` set to a matching entry such as `*` or a hostname wildcard, Gitea's migration URL v… |
| 2026-10-06 20:17:35 | [CVE-2026-96404](https://nvd.nist.gov/vuln/detail/CVE-2026-96404) |  |  | When Gitea's web installer is reachable against a database that already contains users, such as after `INSTALL_LOCK` ha… |
| 2026-10-06 20:17:35 | [CVE-2026-96580](https://nvd.nist.gov/vuln/detail/CVE-2026-96580) |  |  | Gitea expanded a workflow's static `strategy.matrix` into its full Cartesian product without a size limit when creating… |
| 2026-10-06 20:17:35 | [CVE-2026-96589](https://nvd.nist.gov/vuln/detail/CVE-2026-96589) |  |  | When a private repository is transferred to a user who lacks access, Gitea grants that recipient temporary read access… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
