# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-11-06 17:20 UTC

New CVEs published between 2026-11-06 16:18 UTC and 2026-11-06 17:20 UTC.

[Full CSV](data/new-cves-2026-11-06T17-20-02-625291Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-11-06 16:18:54 | [CVE-2026-58141](https://nvd.nist.gov/vuln/detail/CVE-2026-58141) | High | 7.2 | Dify before 1.15.0 contains a server-side request forgery vulnerability that allows any authenticated console user to b… |
| 2026-11-06 16:18:57 | [CVE-2026-66981](https://nvd.nist.gov/vuln/detail/CVE-2026-66981) | Medium | 6.5 | HCL AION is affected by a vulnerability where the application trusted the value of the HTTP Host header supplied in req… |
| 2026-11-06 16:18:57 | [CVE-2026-66982](https://nvd.nist.gov/vuln/detail/CVE-2026-66982) | Low | 3.3 | HCL AION is affected by a vulnerability where browser autocomplete was enabled on sensitive login form fields, allowing… |
| 2026-11-06 16:18:57 | [CVE-2026-66984](https://nvd.nist.gov/vuln/detail/CVE-2026-66984) | Low | 3.1 | HCL AION is affected by a vulnerability where certain application responses revealed internal server file system paths.… |
| 2026-11-06 16:18:58 | [CVE-2026-66986](https://nvd.nist.gov/vuln/detail/CVE-2026-66986) | Low | 3.3 | HCL AION is affected by a vulnerability where user sessions did not expire after a sufficient period of inactivity. An… |
| 2026-11-06 16:18:58 | [CVE-2026-66987](https://nvd.nist.gov/vuln/detail/CVE-2026-66987) | Medium | 5.3 | HCL AION is affected by a vulnerability where the account lockout mechanism did not sufficiently restrict repeated fail… |
| 2026-11-06 16:18:58 | [CVE-2026-80301](https://nvd.nist.gov/vuln/detail/CVE-2026-80301) |  |  | Improper isolation in the Avast sandbox on Windows allows a local, low-privileged attacker executing inside the sandbox… |
| 2026-11-06 16:18:59 | [CVE-2026-80302](https://nvd.nist.gov/vuln/detail/CVE-2026-80302) |  |  | Insufficient isolation in the Avast sandbox file virtualization layer on Windows allows a local, low-privileged attacke… |
| 2026-11-06 16:18:59 | [CVE-2026-80303](https://nvd.nist.gov/vuln/detail/CVE-2026-80303) |  |  | An integer underflow vulnerability in the Avast Windows Filtering Platform (WFP) stream parser on Windows allows denial… |
| 2026-11-06 16:18:59 | [CVE-2026-90436](https://nvd.nist.gov/vuln/detail/CVE-2026-90436) |  |  | ** UNSUPPORTED WHEN ASSIGNED ** Deserialization of an inbound SOAP fault in Apache Axis 1.x allows unauthenticated remo… |
| 2026-11-06 17:17:10 | [CVE-2026-103984](https://nvd.nist.gov/vuln/detail/CVE-2026-103984) | Medium | 6.5 | FreeScout is a self-hosted help desk and shared mailbox. Prior to 1.8.231, when limit_user_customer_visibility is enabl… |
| 2026-11-06 17:17:10 | [CVE-2026-103985](https://nvd.nist.gov/vuln/detail/CVE-2026-103985) | High | 7.1 | FreeScout is a self-hosted help desk and shared mailbox. Prior to 1.8.231, the profile form exposes the only_assigned_t… |
| 2026-11-06 17:17:11 | [CVE-2026-104656](https://nvd.nist.gov/vuln/detail/CVE-2026-104656) | High | 7.3 | Improper neutralization of input in the sessions grid in Progress Telerik Fiddler Everywhere 8.3.0 and earlier allows a… |
| 2026-11-06 17:17:11 | [CVE-2026-104657](https://nvd.nist.gov/vuln/detail/CVE-2026-104657) | High | 7.5 | Missing integrity verification in the Progress Software Fiddler Download and Setup Skill on Linux, macOS, and Windows w… |
| 2026-11-06 17:17:11 | [CVE-2026-106127](https://nvd.nist.gov/vuln/detail/CVE-2026-106127) | Medium | 4.1 | Prototype Pollution in the setter utility (@progress/kendo-react-common) in Progress Software KendoReact versions 3.5.0… |
| 2026-11-06 17:17:11 | [CVE-2026-106128](https://nvd.nist.gov/vuln/detail/CVE-2026-106128) | Medium | 4.1 | Prototype Pollution in @progress/kendo-vue-common in Progress Software Kendo UI for Vue versions 0.4.0 through 9.2.0 al… |
| 2026-11-06 17:17:11 | [CVE-2026-106134](https://nvd.nist.gov/vuln/detail/CVE-2026-106134) | Medium | 5.4 | Cross-Site Scripting (XSS) in the Menu component (@progress/kendo-react-layout) in Progress Software KendoReact version… |
| 2026-11-06 17:17:11 | [CVE-2026-106135](https://nvd.nist.gov/vuln/detail/CVE-2026-106135) | Medium | 5.4 | Cross-Site Scripting (XSS) in the Chat component (@progress/kendo-angular-conversational-ui) in Progress Software Kendo… |
| 2026-11-06 17:17:12 | [CVE-2026-106136](https://nvd.nist.gov/vuln/detail/CVE-2026-106136) | Medium | 5.4 | Cross-Site Scripting (XSS) in the Chat component (@progress/kendo-react-conversational-ui) in Progress Software KendoRe… |
| 2026-11-06 17:17:12 | [CVE-2026-106141](https://nvd.nist.gov/vuln/detail/CVE-2026-106141) | Medium | 5.4 | Cross-Site Scripting (XSS) in the Editor component (@progress/kendo-angular-editor) in Progress Software Kendo UI for A… |
| 2026-11-06 17:17:12 | [CVE-2026-106142](https://nvd.nist.gov/vuln/detail/CVE-2026-106142) | Medium | 5.4 | Cross-Site Scripting (XSS) in the Editor component (@progress/kendo-react-editor) in Progress Software KendoReact versi… |
| 2026-11-06 17:17:12 | [CVE-2026-106143](https://nvd.nist.gov/vuln/detail/CVE-2026-106143) | Medium | 5.4 | Cross-Site Scripting (XSS) in the Editor component (@progress/kendo-vue-editor) in Progress Software Kendo UI for Vue v… |
| 2026-11-06 17:17:12 | [CVE-2026-106144](https://nvd.nist.gov/vuln/detail/CVE-2026-106144) | Medium | 4.1 | Prototype Pollution in the Scheduler component (@progress/kendo-angular-scheduler and @progress/kendo-angular-common) i… |
| 2026-11-06 17:17:16 | [CVE-2026-118515](https://nvd.nist.gov/vuln/detail/CVE-2026-118515) | High | 8.4 | The Symfony Serializer component DataUriNormalizer handles only the exact types SplFileInfo, SplFileObject, and File, s… |
| 2026-11-06 17:17:20 | [CVE-2026-122053](https://nvd.nist.gov/vuln/detail/CVE-2026-122053) | Medium | 6.9 | The Symfony Serializer component ObjectNormalizer treats any attribute name containing . (and, from Symfony 6.4, [) as… |
| 2026-11-06 17:17:20 | [CVE-2026-122193](https://nvd.nist.gov/vuln/detail/CVE-2026-122193) | Critical | 9.3 | OS command injection in the example SSM document provisioning script in Trusted Remote Execution (REX) before 2026-07-2… |
| 2026-11-06 17:17:21 | [CVE-2026-123831](https://nvd.nist.gov/vuln/detail/CVE-2026-123831) | Critical | 9.6 | In JetBrains CLion before 2026.2, 2026.1.4 code execution was possible in Safe Mode via Meson project settings |
| 2026-11-06 17:17:21 | [CVE-2026-123832](https://nvd.nist.gov/vuln/detail/CVE-2026-123832) | Critical | 9.6 | In JetBrains CLion before 2026.2 code execution was possible in Safe Mode via JSON compilation database |
| 2026-11-06 17:17:21 | [CVE-2026-123833](https://nvd.nist.gov/vuln/detail/CVE-2026-123833) | Low | 3.6 | In JetBrains IntelliJ IDEA before 2026.3 database connections could be established in untrusted projects |
| 2026-11-06 17:17:21 | [CVE-2026-123834](https://nvd.nist.gov/vuln/detail/CVE-2026-123834) | High | 7.5 | In JetBrains Datalore before 2026.4 improper scope validation in database tasks allowed using another workspace's servi… |
| 2026-11-06 17:17:21 | [CVE-2026-123835](https://nvd.nist.gov/vuln/detail/CVE-2026-123835) | Medium | 5.9 | In JetBrains Datalore before 2026.4 code execution was possible in another user's computation via an init script upload… |
| 2026-11-06 17:17:21 | [CVE-2026-123836](https://nvd.nist.gov/vuln/detail/CVE-2026-123836) | High | 8.8 | In JetBrains Datalore before 2026.4 workspace collaborators could obtain the owner's SSH private key via Git backup |
| 2026-11-06 17:17:22 | [CVE-2026-123837](https://nvd.nist.gov/vuln/detail/CVE-2026-123837) | High | 7.8 | In JetBrains IntelliJ IDEA before 2026.3, 2026.2.1 command injection was possible in untrusted projects via Tomcat run… |
| 2026-11-06 17:17:22 | [CVE-2026-123838](https://nvd.nist.gov/vuln/detail/CVE-2026-123838) | High | 7.8 | In JetBrains IntelliJ IDEA before 2026.3 code execution was possible in Safe Mode via UI Designer form file |
| 2026-11-06 17:17:22 | [CVE-2026-123839](https://nvd.nist.gov/vuln/detail/CVE-2026-123839) | Medium | 4.7 | In JetBrains IntelliJ IDEA before 2026.3 opening arbitrary URLs without confirmation was possible via the Remote Develo… |
| 2026-11-06 17:17:22 | [CVE-2026-123840](https://nvd.nist.gov/vuln/detail/CVE-2026-123840) | Medium | 4.7 | In JetBrains IntelliJ IDEA before 2026.3 hTML injection was possible in Remote Development editor tabs |
| 2026-11-06 17:17:22 | [CVE-2026-123841](https://nvd.nist.gov/vuln/detail/CVE-2026-123841) | High | 7.8 | In JetBrains IntelliJ IDEA before 2026.3 code execution was possible via symlinks in an imported settings archive |
| 2026-11-06 17:17:22 | [CVE-2026-123842](https://nvd.nist.gov/vuln/detail/CVE-2026-123842) | High | 7.1 | In JetBrains IntelliJ IDEA before 2026.3 arbitrary file write was possible via symlinks when extracting plugin archives |
| 2026-11-06 17:17:22 | [CVE-2026-123843](https://nvd.nist.gov/vuln/detail/CVE-2026-123843) | Low | 3.3 | In JetBrains IntelliJ IDEA before 2026.3 untrusted projects could trigger changes to GPG agent configuration |
| 2026-11-06 17:17:23 | [CVE-2026-123844](https://nvd.nist.gov/vuln/detail/CVE-2026-123844) | Medium | 5.3 | In JetBrains IntelliJ IDEA before 2026.3 sSRF was possible via custom plugin repositories |
| 2026-11-06 17:17:23 | [CVE-2026-123845](https://nvd.nist.gov/vuln/detail/CVE-2026-123845) | Low | 3.3 | In JetBrains IntelliJ IDEA before 2026.3 path traversal was possible via JSON Schema references in untrusted projects |
| 2026-11-06 17:17:23 | [CVE-2026-123846](https://nvd.nist.gov/vuln/detail/CVE-2026-123846) | Medium | 4.3 | In JetBrains IntelliJ IDEA before 2026.3 blind SSRF was possible via remote references in JSON Schema validation |
| 2026-11-06 17:17:23 | [CVE-2026-123847](https://nvd.nist.gov/vuln/detail/CVE-2026-123847) | Medium | 5.3 | In JetBrains IntelliJ IDEA before 2026.3 command execution was possible via control characters in terminal command comp… |
| 2026-11-06 17:17:23 | [CVE-2026-123848](https://nvd.nist.gov/vuln/detail/CVE-2026-123848) | High | 7.4 | In JetBrains IntelliJ IDEA before 2026.3 host name verification was missing for server TLS certificates |
| 2026-11-06 17:17:23 | [CVE-2026-123849](https://nvd.nist.gov/vuln/detail/CVE-2026-123849) | High | 7.0 | In JetBrains IntelliJ IDEA before 2026.3 code execution was possible in untrusted projects via the Terraform File Watch… |
| 2026-11-06 17:17:24 | [CVE-2026-123851](https://nvd.nist.gov/vuln/detail/CVE-2026-123851) | Medium | 5.4 | In JetBrains Junie GitHub Action before 1.6.4 prompt injection protection could be bypassed via HTML-encoded characters |
| 2026-11-06 17:17:24 | [CVE-2026-123852](https://nvd.nist.gov/vuln/detail/CVE-2026-123852) | High | 7.4 | In JetBrains Junie GitHub Action before 1.8.0 code execution with workflow credentials was possible via fork updates |
| 2026-11-06 17:17:24 | [CVE-2026-123853](https://nvd.nist.gov/vuln/detail/CVE-2026-123853) | High | 7.8 | In JetBrains IntelliJ IDEA before 2026.3, 2026.2.2 code execution was possible in Safe Mode via project-controlled JVM… |
| 2026-11-06 17:17:24 | [CVE-2026-123854](https://nvd.nist.gov/vuln/detail/CVE-2026-123854) | Medium | 5.5 | In JetBrains PyCharm before 2026.3 code execution was possible in Safe Mode via a crafted Jupyter notebook widget module |
| 2026-11-06 17:17:24 | [CVE-2026-123855](https://nvd.nist.gov/vuln/detail/CVE-2026-123855) | High | 7.5 | In JetBrains Toolbox App before 3.6.1 command injection was possible via enterprise configuration URLs |
| 2026-11-06 17:17:24 | [CVE-2026-123856](https://nvd.nist.gov/vuln/detail/CVE-2026-123856) | Medium | 6.5 | In JetBrains Toolbox App before 3.6.1 nTLM hash disclosure was possible via SVG tool icons from a Remote Development se… |
| 2026-11-06 17:17:24 | [CVE-2026-123850](https://nvd.nist.gov/vuln/detail/CVE-2026-123850) | Low | 3.5 | In JetBrains YouTrack before 2026.2.19422 cSS injection was possible in Mermaid diagrams via configuration directives |
| 2026-11-06 17:17:25 | [CVE-2026-123857](https://nvd.nist.gov/vuln/detail/CVE-2026-123857) | Medium | 4.3 | In JetBrains PhpStorm before 2026.3 xXE was possible in untrusted projects via PHPMD ruleset autodetection |
| 2026-11-06 17:17:25 | [CVE-2026-123858](https://nvd.nist.gov/vuln/detail/CVE-2026-123858) | Medium | 4.4 | In JetBrains PhpStorm before 2026.3 project files could be automatically uploaded to a deployment server from untrusted… |
| 2026-11-06 17:17:25 | [CVE-2026-123859](https://nvd.nist.gov/vuln/detail/CVE-2026-123859) | High | 8.1 | When identifier escaping is disabled through a non-default configuration, the write_pandas() data-loading functionality… |
| 2026-11-06 17:17:25 | [CVE-2026-123962](https://nvd.nist.gov/vuln/detail/CVE-2026-123962) | High | 8.4 | In FreedomBox before 26.15, unprivileged user accounts can read/write files for which they lack permissions by setting… |
| 2026-11-06 17:17:55 | [CVE-2026-49951](https://nvd.nist.gov/vuln/detail/CVE-2026-49951) | Medium | 5.3 | RAGFlow before 0.27.0 contains a server-side request forgery vulnerability that allows authenticated attackers to force… |
| 2026-11-06 17:18:33 | [CVE-2026-62850](https://nvd.nist.gov/vuln/detail/CVE-2026-62850) | Medium | 5.3 | FreeScout is a self-hosted help desk and shared mailbox. Prior to 1.8.225, the administrative tools.php maintenance end… |
| 2026-11-06 17:18:33 | [CVE-2026-62851](https://nvd.nist.gov/vuln/detail/CVE-2026-62851) | Medium | 4.3 | FreeScout is a self-hosted help desk and shared mailbox. Prior to 1.8.226, the search-by-number shortcut in Conversatio… |
| 2026-11-06 17:18:33 | [CVE-2026-62852](https://nvd.nist.gov/vuln/detail/CVE-2026-62852) | Medium | 6.5 | FreeScout is a self-hosted help desk and shared mailbox. Prior to 1.8.226, RealtimeConvNewThread checks only general ma… |
| 2026-11-06 17:18:33 | [CVE-2026-62854](https://nvd.nist.gov/vuln/detail/CVE-2026-62854) | High | 7.6 | FreeScout is a self-hosted help desk and shared mailbox. Prior to 1.8.225, a user who can edit a mailbox signature can… |
| 2026-11-06 17:18:33 | [CVE-2026-62855](https://nvd.nist.gov/vuln/detail/CVE-2026-62855) | Medium | 4.4 | FreeScout is a self-hosted help desk and shared mailbox. Prior to 1.8.225, the administrator-only App Logs viewer accep… |
| 2026-11-06 17:18:34 | [CVE-2026-62856](https://nvd.nist.gov/vuln/detail/CVE-2026-62856) | High | 7.7 | FreeScout is a self-hosted help desk and shared mailbox application. Prior to version 1.8.226, the polycast/receive end… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
