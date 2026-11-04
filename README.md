# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-11-04 21:19 UTC

New CVEs published between 2026-11-04 20:18 UTC and 2026-11-04 21:19 UTC.

[Full CSV](data/new-cves-2026-11-04T21-19-58-527557Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-11-04 20:18:55 | [CVE-2026-113368](https://nvd.nist.gov/vuln/detail/CVE-2026-113368) | Medium | 5.3 | Sonatype Nexus Repository 3 does not check that a user account is authorized to access a repository before the reposito… |
| 2026-11-04 20:18:55 | [CVE-2026-113369](https://nvd.nist.gov/vuln/detail/CVE-2026-113369) | Medium | 6.3 | Sonatype Nexus Repository 3 allows a user account that can push manifests to a hosted OCI repository (a user account th… |
| 2026-11-04 20:18:56 | [CVE-2026-113370](https://nvd.nist.gov/vuln/detail/CVE-2026-113370) | High | 7.7 | Sonatype Nexus Repository 3 contains a SQL injection vulnerability in the optional "Reindex Search Tables By Pattern" t… |
| 2026-11-04 20:18:56 | [CVE-2026-113371](https://nvd.nist.gov/vuln/detail/CVE-2026-113371) | High | 7.1 | Sonatype Nexus Repository 3 returns the signing passphrase of an APT or YUM repository, through an internal REST endpoi… |
| 2026-11-04 20:18:56 | [CVE-2026-113372](https://nvd.nist.gov/vuln/detail/CVE-2026-113372) | High | 7.1 | Sonatype Nexus Repository 3 returns the private signing key of a YUM proxy or group repository to an account that holds… |
| 2026-11-04 20:18:56 | [CVE-2026-113373](https://nvd.nist.gov/vuln/detail/CVE-2026-113373) | Critical | 9.1 | Sonatype Nexus Repository 3 Pro does not check the local account status when a user signs in through a configured SAML… |
| 2026-11-04 20:18:57 | [CVE-2026-113374](https://nvd.nist.gov/vuln/detail/CVE-2026-113374) | High | 8.6 | Sonatype Nexus Repository 3 does not require realm administration permission when a user creates a Rut Auth capability.… |
| 2026-11-04 20:19:01 | [CVE-2026-115474](https://nvd.nist.gov/vuln/detail/CVE-2026-115474) | Medium | 6.5 | Zulip is an open-source team collaboration tool. From 8.0 until 12.2, in organizations where the Who can view all other… |
| 2026-11-04 20:19:02 | [CVE-2026-115574](https://nvd.nist.gov/vuln/detail/CVE-2026-115574) | Medium | 5.3 | Zulip is an open-source team collaboration tool. From 11.0 until 12.2, organizations with web-public channels enabled e… |
| 2026-11-04 20:19:11 | [CVE-2026-121933](https://nvd.nist.gov/vuln/detail/CVE-2026-121933) | Critical | 9.3 | A flaw has been found in Linksys E5350 1.0.00.037. This impacts the function save_settings of the file /wizard/apply.cg… |
| 2026-11-04 20:19:12 | [CVE-2026-122192](https://nvd.nist.gov/vuln/detail/CVE-2026-122192) | High | 7.1 | Improper handling of a failed memory remap in Firecracker versions 0.23.0 through 1.16.1 might allow a guest user with… |
| 2026-11-04 20:19:12 | [CVE-2026-122220](https://nvd.nist.gov/vuln/detail/CVE-2026-122220) | Critical | 9.1 | WPO365 \| LOGIN (wpo365-login) plugin before version 45.2 contains an authentication bypass by capture-replay vulnerabil… |
| 2026-11-04 20:19:12 | [CVE-2026-76806](https://nvd.nist.gov/vuln/detail/CVE-2026-76806) | Medium | 6.3 | Solidtime is an open-source time-tracking app. Prior to 0.16.0, TogglDataImporter::importData() read attacker-controlle… |
| 2026-11-04 20:19:13 | [CVE-2026-97705](https://nvd.nist.gov/vuln/detail/CVE-2026-97705) | High | 7.5 | Moleculer is a progressive microservices framework for Node.js. Prior to 0.14.36 and 0.15.2, Parser._write in src/trans… |
| 2026-11-04 21:17:39 | [CVE-2025-71453](https://nvd.nist.gov/vuln/detail/CVE-2025-71453) | Medium | 5.1 | vtenext before 25.02.2 contains a reflected cross-site scripting vulnerability in modules/Home/HomeWidgetBlockList.php… |
| 2026-11-04 21:17:39 | [CVE-2025-71454](https://nvd.nist.gov/vuln/detail/CVE-2025-71454) | Medium | 6.9 | vtenext before 25.02.2 contains a cross-site request forgery protection bypass because csrf_check() in include/utils/Vt… |
| 2026-11-04 21:17:40 | [CVE-2025-71455](https://nvd.nist.gov/vuln/detail/CVE-2025-71455) | Medium | 5.9 | vtenext before 25.02.2 contains a session identifier disclosure vulnerability that allows attackers to read the PHPSESS… |
| 2026-11-04 21:17:40 | [CVE-2025-71456](https://nvd.nist.gov/vuln/detail/CVE-2025-71456) | High | 8.6 | vtenext before 25.02.2 contains an SQL injection vulnerability that allows authenticated low-privileged users to inject… |
| 2026-11-04 21:17:40 | [CVE-2025-71457](https://nvd.nist.gov/vuln/detail/CVE-2025-71457) | Critical | 9.3 | vtenext 25.02 before 25.02.1 contains an authentication bypass vulnerability that allows unauthenticated attackers to c… |
| 2026-11-04 21:17:40 | [CVE-2026-102339](https://nvd.nist.gov/vuln/detail/CVE-2026-102339) | High | 8.2 | Telepresence enables local development against a remote Kubernetes or OpenShift cluster. Prior to 2.31.0, the Traffic M… |
| 2026-11-04 21:17:40 | [CVE-2026-102340](https://nvd.nist.gov/vuln/detail/CVE-2026-102340) | High | 8.5 | Telepresence enables local development against a remote Kubernetes or OpenShift cluster. Prior to 2.31.0, the Traffic M… |
| 2026-11-04 21:17:41 | [CVE-2026-102664](https://nvd.nist.gov/vuln/detail/CVE-2026-102664) | High | 7.1 | ProxySQL is a proxy for MySQL and its forks, as well as PostgreSQL. Prior to 3.0.10, 3.1.10, and 4.0.10, decompress_mys… |
| 2026-11-04 21:17:42 | [CVE-2026-104203](https://nvd.nist.gov/vuln/detail/CVE-2026-104203) | High | 7.5 | Traccar is an open source GPS tracking system. From 5.1 until 6.15.0, WebModule.java's MediaFilter Guice mapping and We… |
| 2026-11-04 21:17:42 | [CVE-2026-105702](https://nvd.nist.gov/vuln/detail/CVE-2026-105702) | Medium | 4.3 | IBM Db2 Genius Hub 1.1.2, 1.1.3, 1.1.4, 1.1.5 could allow a remote authenticated attacker to obtain sensitive informati… |
| 2026-11-04 21:17:43 | [CVE-2026-105991](https://nvd.nist.gov/vuln/detail/CVE-2026-105991) | Low | 3.5 | IBM Db2 Genius Hub 1.1.2, 1.1.3, 1.1.4, 1.1.5 could allow a remote authenticated attacker to bypass security restrictio… |
| 2026-11-04 21:17:46 | [CVE-2026-108536](https://nvd.nist.gov/vuln/detail/CVE-2026-108536) | Medium | 4.6 | IBM Db2 Genius Hub 1.1.2, 1.1.3, 1.1.4, 1.1.5 could allow a remote authenticated attacker to bypass security restrictio… |
| 2026-11-04 21:17:46 | [CVE-2026-108588](https://nvd.nist.gov/vuln/detail/CVE-2026-108588) | Medium | 5.4 | IBM Db2 Genius Hub 1.1.2, 1.1.3, 1.1.4, 1.1.5 could allow a remote authenticated attacker to bypass security restrictio… |
| 2026-11-04 21:17:47 | [CVE-2026-108767](https://nvd.nist.gov/vuln/detail/CVE-2026-108767) | Medium | 4.3 | IBM Db2 Genius Hub 1.1.2, 1.1.3, 1.1.4, 1.1.5 could allow a remote authenticated attacker to conduct HTTP response spli… |
| 2026-11-04 21:17:47 | [CVE-2026-108838](https://nvd.nist.gov/vuln/detail/CVE-2026-108838) | Low | 3.3 | IBM Db2 Genius Hub 1.1.2, 1.1.3, 1.1.4, 1.1.5 could allow a local attacker to cause a denial of service due to uncontro… |
| 2026-11-04 21:17:47 | [CVE-2026-108910](https://nvd.nist.gov/vuln/detail/CVE-2026-108910) | Medium | 4.3 | IBM Db2 Genius Hub 1.1.2, 1.1.3, 1.1.4, 1.1.5 could allow a remote authenticated attacker to obtain sensitive informati… |
| 2026-11-04 21:17:48 | [CVE-2026-10859](https://nvd.nist.gov/vuln/detail/CVE-2026-10859) | High | 7.5 | IBM MQ 9.2.0.0 through 9.2.0.44 LTS, 9.3.0.0 through 9.3.0.42 LTS, 9.4.0.0 through 9.4.0.26 LTS, 9.4.0.0 through 9.4.5.… |
| 2026-11-04 21:17:48 | [CVE-2026-110281](https://nvd.nist.gov/vuln/detail/CVE-2026-110281) | Medium | 5.9 | IBM Db2 Genius Hub 1.1.2, 1.1.3, 1.1.4, 1.1.5 improperly validates TLS certificate validation, which could allow an att… |
| 2026-11-04 21:17:48 | [CVE-2026-110282](https://nvd.nist.gov/vuln/detail/CVE-2026-110282) | Medium | 6.5 | IBM Db2 Genius Hub 1.1.2, 1.1.3, 1.1.4, 1.1.5 could allow a remote authenticated attacker to bypass security restrictio… |
| 2026-11-04 21:17:48 | [CVE-2026-110283](https://nvd.nist.gov/vuln/detail/CVE-2026-110283) | Medium | 4.3 | IBM Db2 Genius Hub 1.1.2, 1.1.3, 1.1.4, 1.1.5 could allow a remote authenticated attacker to cause a denial of service… |
| 2026-11-04 21:17:52 | [CVE-2026-115758](https://nvd.nist.gov/vuln/detail/CVE-2026-115758) | High | 8.2 | SumatraPDF is a multi-format reader for Windows. In version 3.6.1 and earlier, HttpGet() in src/base/Http_win.cpp uncon… |
| 2026-11-04 21:17:52 | [CVE-2026-115762](https://nvd.nist.gov/vuln/detail/CVE-2026-115762) | Medium | 6.1 | draw.io is a configurable diagramming and whiteboarding application. Prior to 31.1.5, the GraphML decoder contains a pr… |
| 2026-11-04 21:17:52 | [CVE-2026-116376](https://nvd.nist.gov/vuln/detail/CVE-2026-116376) | Low | 3.4 | IBM Db2 Genius Hub 1.1.2, 1.1.3, 1.1.4, 1.1.5 could allow a remote authenticated attacker to conduct a phishing attack… |
| 2026-11-04 21:17:56 | [CVE-2026-11376](https://nvd.nist.gov/vuln/detail/CVE-2026-11376) | High | 8.8 | IBM MQ 9.2.0.0 through 9.2.0.44 LTS, 9.3.0.0 through 9.3.0.42 LTS, 9.4.0.0 through 9.4.0.26 LTS, 9.4.0.0 through 9.4.5.… |
| 2026-11-04 21:17:56 | [CVE-2026-11724](https://nvd.nist.gov/vuln/detail/CVE-2026-11724) | High | 8.5 | IBM MQ 9.2.0.0 through 9.2.0.44 LTS, 9.3.0.0 through 9.3.0.42 LTS, 9.4.0.0 through 9.4.0.26 LTS, 9.4.0.0 through 9.4.5.… |
| 2026-11-04 21:18:06 | [CVE-2026-121968](https://nvd.nist.gov/vuln/detail/CVE-2026-121968) | High | 7.1 | Netrek-client-cow through 3.3.3 contains an out-of-bounds read vulnerability in short.c handleSMessage() that allows ma… |
| 2026-11-04 21:18:06 | [CVE-2026-121969](https://nvd.nist.gov/vuln/detail/CVE-2026-121969) | High | 7.1 | netrek-client-cow through 3.3.3 contains a stack-based buffer overflow vulnerability in handleSMessage() in short.c tha… |
| 2026-11-04 21:18:07 | [CVE-2026-122009](https://nvd.nist.gov/vuln/detail/CVE-2026-122009) | Medium | 5.5 | A flaw has been found in DataLinkDC Dinky up to 1.2.5. This vulnerability affects the function FlinkWebURITemplateProxy… |
| 2026-11-04 21:18:07 | [CVE-2026-122013](https://nvd.nist.gov/vuln/detail/CVE-2026-122013) | Critical | 9.3 | A vulnerability was detected in Comfast CF-WR632AX 2.6.0.1. Affected by this vulnerability is an unknown functionality… |
| 2026-11-04 21:18:07 | [CVE-2026-122014](https://nvd.nist.gov/vuln/detail/CVE-2026-122014) | Low | 2.1 | A vulnerability has been found in NPC-Worldwide npcpy up to 2.1.27. This affects the function load_sft_model of the fil… |
| 2026-11-04 21:18:08 | [CVE-2026-122126](https://nvd.nist.gov/vuln/detail/CVE-2026-122126) | High | 8.2 | reSIProcate reTurn client through 1.14.0 contains a heap buffer overflow in TurnTcpSocket::handleReadHeader() that allo… |
| 2026-11-04 21:18:08 | [CVE-2026-122127](https://nvd.nist.gov/vuln/detail/CVE-2026-122127) | High | 8.7 | CESNET ipfixcol2 2.7.1 before 2.9.0 contains a heap-based buffer overflow in Lz4Decoder.cpp that allows unauthenticated… |
| 2026-11-04 21:18:08 | [CVE-2026-122129](https://nvd.nist.gov/vuln/detail/CVE-2026-122129) | Medium | 6.9 | CESNET ipfixcol2 2.7.1 before 2.9.0 contains a memory allocation vulnerability in Lz4Decoder::read_start_header() that… |
| 2026-11-04 21:18:08 | [CVE-2026-122130](https://nvd.nist.gov/vuln/detail/CVE-2026-122130) | High | 8.3 | CESNET ipfixcol2 2.3.0 before 2.9.0 contains an integer overflow vulnerability in the Forwarder output plugin that allo… |
| 2026-11-04 21:18:08 | [CVE-2026-122131](https://nvd.nist.gov/vuln/detail/CVE-2026-122131) | Medium | 6.3 | Joi 17.13.6 before 17.13.9 and 18.2.5 before 18.3.1 contains a prototype pollution vulnerability in lib/messages.js com… |
| 2026-11-04 21:18:08 | [CVE-2026-122132](https://nvd.nist.gov/vuln/detail/CVE-2026-122132) | Medium | 5.1 | go-chi chi 5.2.2 through 5.5.0 contains an open redirect vulnerability in the RedirectSlashes middleware that allows at… |
| 2026-11-04 21:18:09 | [CVE-2026-122133](https://nvd.nist.gov/vuln/detail/CVE-2026-122133) | High | 8.6 | Mistral Vibe before 2.25.5 on Windows contains an untrusted search path vulnerability that allows attackers to execute… |
| 2026-11-04 21:18:09 | [CVE-2026-122134](https://nvd.nist.gov/vuln/detail/CVE-2026-122134) | High | 8.6 | Mistral Vibe before 2.25.7 contains a remote code execution vulnerability that allows attackers to run commands by conf… |
| 2026-11-04 21:18:09 | [CVE-2026-122135](https://nvd.nist.gov/vuln/detail/CVE-2026-122135) | High | 8.6 | Mistral Vibe before 3.0.3 contains a remote code execution vulnerability that allows attackers to run commands by abusi… |
| 2026-11-04 21:18:09 | [CVE-2026-122136](https://nvd.nist.gov/vuln/detail/CVE-2026-122136) | Medium | 4.1 | Powerlevel10k before 1.20.19 contains a symlink following vulnerability in _p9k_dump_instant_prompt that allows local a… |
| 2026-11-04 21:18:09 | [CVE-2026-122137](https://nvd.nist.gov/vuln/detail/CVE-2026-122137) | Medium | 5.4 | Powerlevel10k before 1.20.19 contains an insecure temporary directory vulnerability in the bundled gitstatus/install sc… |
| 2026-11-04 21:18:10 | [CVE-2026-122138](https://nvd.nist.gov/vuln/detail/CVE-2026-122138) | Medium | 6.3 | BlueprintUE Self-Hosted Edition 4.2.0 before 4.3.4 contains a login rate limit bypass vulnerability in LoginMiddleware.… |
| 2026-11-04 21:18:10 | [CVE-2026-122139](https://nvd.nist.gov/vuln/detail/CVE-2026-122139) | Medium | 6.9 | blueprintUE Self-Hosted Edition before 4.3.3 contains an account enumeration vulnerability in ForgotPasswordMiddleware.… |
| 2026-11-04 21:18:10 | [CVE-2026-122140](https://nvd.nist.gov/vuln/detail/CVE-2026-122140) | Medium | 6.3 | Trawl 1.5.0 before 1.10.0 contains a server-side request forgery vulnerability that allows unauthenticated attackers to… |
| 2026-11-04 21:18:10 | [CVE-2026-122224](https://nvd.nist.gov/vuln/detail/CVE-2026-122224) | High | 7.2 | WebVirtCloud through commit bb920b0 contains a missing authorization vulnerability that allows low-privileged authentic… |
| 2026-11-04 21:18:10 | [CVE-2026-122233](https://nvd.nist.gov/vuln/detail/CVE-2026-122233) | Medium | 6.3 | FrankenPHP before 1.13.4 contains an information disclosure vulnerability in worker mode that fails to clear last HTTP… |
| 2026-11-04 21:18:10 | [CVE-2026-122234](https://nvd.nist.gov/vuln/detail/CVE-2026-122234) | Low | 2.3 | jsondiffpatch before 0.7.7 contains a cross-site scripting vulnerability that allows attackers to inject markup by supp… |
| 2026-11-04 21:18:11 | [CVE-2026-122235](https://nvd.nist.gov/vuln/detail/CVE-2026-122235) | Medium | 5.7 | Jan from 0.8.5 before 0.8.8 contains a workspace guard bypass vulnerability in the agent-tools gate.rs that allows atta… |
| 2026-11-04 21:18:11 | [CVE-2026-12356](https://nvd.nist.gov/vuln/detail/CVE-2026-12356) | High | 7.5 | IBM MQ 9.2.0.0 through 9.2.0.44 LTS, 9.3.0.0 through 9.3.0.42 LTS, 9.4.0.0 through 9.4.0.26 LTS, 9.4.0.0 through 9.4.5.… |
| 2026-11-04 21:18:11 | [CVE-2026-12538](https://nvd.nist.gov/vuln/detail/CVE-2026-12538) | Medium | 5.4 | IBM MQ 9.4.0.0 to 9.4.0.26, 9.4.1.0 to 9.4.5.3, and 10.0.0.1 to 10.0.0.5 could allow an authenticated attacker to obtai… |
| 2026-11-04 21:18:11 | [CVE-2026-12550](https://nvd.nist.gov/vuln/detail/CVE-2026-12550) | Medium | 5.4 | IBM MQ 9.2.0.0 through 9.2.0.44 LTS, 9.3.0.0 through 9.3.0.42 LTS, 9.4.0.0 through 9.4.0.26 LTS, 9.4.0.0 through 9.4.5.… |
| 2026-11-04 21:18:11 | [CVE-2026-13271](https://nvd.nist.gov/vuln/detail/CVE-2026-13271) | High | 8.1 | IBM MQ 9.2.0.0 through 9.2.0.44 LTS, 9.3.0.0 through 9.3.0.42 LTS, 9.4.0.0 through 9.4.0.26 LTS, 9.4.0.0 through 9.4.5.… |
| 2026-11-04 21:18:11 | [CVE-2026-13284](https://nvd.nist.gov/vuln/detail/CVE-2026-13284) | High | 7.1 | IBM MQ 9.2.0.0 through 9.2.0.44 LTS, 9.3.0.0 through 9.3.0.42 LTS, 9.4.0.0 through 9.4.0.26 LTS, 9.4.0.0 through 9.4.5.… |
| 2026-11-04 21:18:12 | [CVE-2026-13289](https://nvd.nist.gov/vuln/detail/CVE-2026-13289) | High | 7.1 | IBM MQ 9.2.0.0 through 9.2.0.44 LTS, 9.3.0.0 through 9.3.0.42 LTS, 9.4.0.0 through 9.4.0.26 LTS, 9.4.0.0 through 9.4.5.… |
| 2026-11-04 21:18:12 | [CVE-2026-13292](https://nvd.nist.gov/vuln/detail/CVE-2026-13292) | High | 8.8 | IBM MQ 9.2.0.0 through 9.2.0.44 LTS, 9.3.0.0 through 9.3.0.42 LTS, 9.4.0.0 through 9.4.0.26 LTS, 9.4.0.0 through 9.4.5.… |
| 2026-11-04 21:18:12 | [CVE-2026-14252](https://nvd.nist.gov/vuln/detail/CVE-2026-14252) | Medium | 6.2 | IBM MQ 9.2.0.0 through 9.2.0.44 LTS, 9.3.0.0 through 9.3.0.42 LTS, 9.4.0.0 through 9.4.0.26 LTS, 9.4.0.0 through 9.4.5.… |
| 2026-11-04 21:18:12 | [CVE-2026-16725](https://nvd.nist.gov/vuln/detail/CVE-2026-16725) | Medium | 6.5 | IBM Watson Speech Services Cartridge 4.0.0 through 5.4.0 could allow a remote authenticated attacker to read arbitrary… |
| 2026-11-04 21:18:13 | [CVE-2026-17493](https://nvd.nist.gov/vuln/detail/CVE-2026-17493) | High | 7.5 | IBM Watson Speech Services Cartridge 4.0.0 through 5.4.0 could allow a remote attacker to cause a denial of service due… |
| 2026-11-04 21:18:13 | [CVE-2026-18142](https://nvd.nist.gov/vuln/detail/CVE-2026-18142) | High | 7.1 | IBM MQ 9.2.0.0 through 9.2.0.44 LTS, 9.3.0.0 through 9.3.0.42 LTS, 9.4.0.0 through 9.4.0.26 LTS, 9.4.0.0 through 9.4.5.… |
| 2026-11-04 21:18:13 | [CVE-2026-19319](https://nvd.nist.gov/vuln/detail/CVE-2026-19319) | Medium | 5.3 | IBM Watson Speech Services Cartridge 4.0.0 through 5.4.0 could allow a remote attacker to obtain sensitive information… |
| 2026-11-04 21:18:14 | [CVE-2026-82418](https://nvd.nist.gov/vuln/detail/CVE-2026-82418) | Critical | 9.8 | IBM Watson Speech Services Cartridge 4.0.0 through 5.4.0 could allow a remote attacker to execute arbitrary code due to… |
| 2026-11-04 21:18:17 | [CVE-2026-97373](https://nvd.nist.gov/vuln/detail/CVE-2026-97373) | Medium | 5.8 | draw.io is a configurable diagramming and whiteboarding application. Prior to 30.3.8, the optional /proxy endpoint cont… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
