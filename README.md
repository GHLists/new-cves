# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-20 01:19 UTC

New CVEs published between 2026-10-20 00:18 UTC and 2026-10-20 01:19 UTC.

[Full CSV](data/new-cves-2026-10-20T01-19-52-085283Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-10-20 00:19:20 | [CVE-2026-8355](https://nvd.nist.gov/vuln/detail/CVE-2026-8355) |  |  | IBM ContextForge MCP Gateway 0.1.0 through 1.0.5 is vulnerable to a server-side request Forgery (SSRF) that allows auth… |
| 2026-10-20 01:17:09 | [CVE-2026-105297](https://nvd.nist.gov/vuln/detail/CVE-2026-105297) | High | 7.5 | Summary Before version 0.8.1, Pingora's HTTP/2 server used the h2 crate's default limits unless the application set its… |
| 2026-10-20 01:17:09 | [CVE-2026-105298](https://nvd.nist.gov/vuln/detail/CVE-2026-105298) | Medium | 6.3 | Summary Before version 0.9.0, Pingora accepted HTTP/2 requests whose Host header differed from the :authority pseudo-he… |
| 2026-10-20 01:17:09 | [CVE-2026-109395](https://nvd.nist.gov/vuln/detail/CVE-2026-109395) | High | 8.8 | Ning compress-lzf before 1.2.0 contains an out-of-bounds memory access vulnerability in the sun.misc.Unsafe based Unsaf… |
| 2026-10-20 01:17:10 | [CVE-2026-109440](https://nvd.nist.gov/vuln/detail/CVE-2026-109440) | High | 8.6 | LangAlpha through 2026.09.07 contains an indirect prompt injection vulnerability that allows remote attackers to execut… |
| 2026-10-20 01:17:10 | [CVE-2026-109441](https://nvd.nist.gov/vuln/detail/CVE-2026-109441) | Medium | 6.9 | LangAlpha through 2026.09.07 contains an improper isolation vulnerability that places all tenants' sandbox containers o… |
| 2026-10-20 01:17:10 | [CVE-2026-109442](https://nvd.nist.gov/vuln/detail/CVE-2026-109442) | Critical | 9.3 | piflow 2.0.0 through 2.0.1 contains a remote code execution vulnerability in its DeepAgents chat agent, whose POST /cha… |
| 2026-10-20 01:17:10 | [CVE-2026-109443](https://nvd.nist.gov/vuln/detail/CVE-2026-109443) | High | 8.7 | JoySafeter through 1.0.0 contains a remote code execution vulnerability that allows authenticated users to run operatin… |
| 2026-10-20 01:17:10 | [CVE-2026-109444](https://nvd.nist.gov/vuln/detail/CVE-2026-109444) | High | 8.7 | OpenSRE through 0.1.2026.10.19 contains an approval gate bypass vulnerability that allows attackers to execute shell_ru… |
| 2026-10-20 01:17:11 | [CVE-2026-28850](https://nvd.nist.gov/vuln/detail/CVE-2026-28850) |  |  | An authorization issue was addressed with improved state management. This issue is fixed in visionOS 27. An app may be… |
| 2026-10-20 01:17:11 | [CVE-2026-28853](https://nvd.nist.gov/vuln/detail/CVE-2026-28853) |  |  | The issue was addressed with improved checks. This issue is fixed in macOS Sequoia 15.8, macOS Tahoe 26.7. An app may b… |
| 2026-10-20 01:17:11 | [CVE-2026-28854](https://nvd.nist.gov/vuln/detail/CVE-2026-28854) |  |  | The issue was addressed with additional app bundle integrity checks. This issue is fixed in macOS Golden Gate 27. A mal… |
| 2026-10-20 01:17:16 | [CVE-2026-65356](https://nvd.nist.gov/vuln/detail/CVE-2026-65356) |  |  | An access issue was addressed with improved access controls. This issue is fixed in macOS Golden Gate 27, macOS Sequoia… |
| 2026-10-20 01:17:17 | [CVE-2026-65372](https://nvd.nist.gov/vuln/detail/CVE-2026-65372) |  |  | A race condition was addressed with additional validation. This issue is fixed in macOS Golden Gate 27, macOS Sequoia 1… |
| 2026-10-20 01:17:17 | [CVE-2026-65379](https://nvd.nist.gov/vuln/detail/CVE-2026-65379) |  |  | The issue was addressed with improved handling of secure input state. This issue is fixed in macOS Golden Gate 27, macO… |
| 2026-10-20 01:17:18 | [CVE-2026-65396](https://nvd.nist.gov/vuln/detail/CVE-2026-65396) |  |  | A buffer overflow was addressed with improved size validation. This issue is fixed in macOS Golden Gate 27, macOS Sequo… |
| 2026-10-20 01:17:19 | [CVE-2026-75128](https://nvd.nist.gov/vuln/detail/CVE-2026-75128) | Critical | 9.3 | Langchain-Chatchat through 0.3.1.3 exposes a POST /tools/call API endpoint that invokes any registered tool by name wit… |
| 2026-10-20 01:17:19 | [CVE-2026-77926](https://nvd.nist.gov/vuln/detail/CVE-2026-77926) | High | 8.7 | Aix-DB 1.2.4 contains a remote code execution vulnerability that allows authenticated non-admin users to run operating… |
| 2026-10-20 01:17:19 | [CVE-2026-77930](https://nvd.nist.gov/vuln/detail/CVE-2026-77930) | High | 8.7 | EvoScientist 0.1.0 before 0.2.5 contains an approval bypass vulnerability that allows attackers to run host shell comma… |
| 2026-10-20 01:17:19 | [CVE-2026-77932](https://nvd.nist.gov/vuln/detail/CVE-2026-77932) | Critical | 9.3 | DB-GPT through 0.8.2 contains an unauthenticated remote code execution vulnerability because the /api/v1/chat/react-age… |
| 2026-10-20 01:17:19 | [CVE-2026-77933](https://nvd.nist.gov/vuln/detail/CVE-2026-77933) | Critical | 9.3 | DB-GPT through 0.8.2 contains a hardcoded credentials vulnerability in its default docker-compose.yml that sets a stati… |
| 2026-10-20 01:17:19 | [CVE-2026-77934](https://nvd.nist.gov/vuln/detail/CVE-2026-77934) | High | 8.7 | Coze Studio before 0.5.0 contains an insecure default configuration that allows any registered user to execute commands… |
| 2026-10-20 01:17:19 | [CVE-2026-77935](https://nvd.nist.gov/vuln/detail/CVE-2026-77935) | High | 8.7 | Coze Studio through 0.5.1 contains an insecure direct object reference vulnerability in workflow.go that allows authent… |
| 2026-10-20 01:17:20 | [CVE-2026-77936](https://nvd.nist.gov/vuln/detail/CVE-2026-77936) | Critical | 9.3 | Letta through 0.16.8 ships a compose.yaml that does not enable LETTA_SERVER_SECURE, so the password middleware is never… |
| 2026-10-20 01:17:20 | [CVE-2026-77937](https://nvd.nist.gov/vuln/detail/CVE-2026-77937) | High | 8.6 | Letta through 0.16.8 contains an authentication bypass vulnerability that allows API callers to impersonate other users… |
| 2026-10-20 01:17:20 | [CVE-2026-77938](https://nvd.nist.gov/vuln/detail/CVE-2026-77938) | High | 7.1 | Letta through 0.16.8 contains an information disclosure vulnerability that allows users running tools to read server se… |
| 2026-10-20 01:17:20 | [CVE-2026-84490](https://nvd.nist.gov/vuln/detail/CVE-2026-84490) |  |  | This issue was addressed through improved state management. This issue is fixed in iOS 27 and iPadOS 27. An attacker wi… |
| 2026-10-20 01:17:20 | [CVE-2026-84508](https://nvd.nist.gov/vuln/detail/CVE-2026-84508) |  |  | This issue was addressed with improved validation of the caller's access. This issue is fixed in iOS 27 and iPadOS 27,… |
| 2026-10-20 01:17:22 | [CVE-2026-84547](https://nvd.nist.gov/vuln/detail/CVE-2026-84547) |  |  | A memory corruption issue was addressed with improved input validation. This issue is fixed in macOS Golden Gate 27, ma… |
| 2026-10-20 01:17:23 | [CVE-2026-84579](https://nvd.nist.gov/vuln/detail/CVE-2026-84579) |  |  | A logic issue was addressed with improved checks. This issue is fixed in macOS Golden Gate 27, macOS Sequoia 15.8, macO… |
| 2026-10-20 01:17:23 | [CVE-2026-84582](https://nvd.nist.gov/vuln/detail/CVE-2026-84582) |  |  | A privacy issue was addressed with improved access restrictions. This issue is fixed in iOS 27 and iPadOS 27, macOS Gol… |
| 2026-10-20 01:17:24 | [CVE-2026-84613](https://nvd.nist.gov/vuln/detail/CVE-2026-84613) |  |  | An out-of-bounds write issue was addressed with improved bounds checking. This issue is fixed in iOS 26.7 and iPadOS 26… |
| 2026-10-20 01:17:24 | [CVE-2026-86868](https://nvd.nist.gov/vuln/detail/CVE-2026-86868) |  |  | An authentication issue was addressed with improved state management. This issue is fixed in macOS Golden Gate 27, macO… |
| 2026-10-20 01:17:25 | [CVE-2026-86871](https://nvd.nist.gov/vuln/detail/CVE-2026-86871) |  |  | An integer underflow was addressed with improved input validation. This issue is fixed in macOS Golden Gate 27, macOS S… |
| 2026-10-20 01:17:25 | [CVE-2026-86872](https://nvd.nist.gov/vuln/detail/CVE-2026-86872) |  |  | A logic issue was addressed with improved state management. This issue is fixed in Safari 27, visionOS 27, watchOS 27.… |
| 2026-10-20 01:17:25 | [CVE-2026-86874](https://nvd.nist.gov/vuln/detail/CVE-2026-86874) |  |  | An out-of-bounds read was addressed with improved input validation. This issue is fixed in Xcode 27. Parsing a maliciou… |
| 2026-10-20 01:17:25 | [CVE-2026-86875](https://nvd.nist.gov/vuln/detail/CVE-2026-86875) |  |  | An input validation issue was addressed with improved input validation. This issue is fixed in Xcode 27. Parsing a mali… |
| 2026-10-20 01:17:26 | [CVE-2026-86907](https://nvd.nist.gov/vuln/detail/CVE-2026-86907) |  |  | An authorization issue was addressed with improved entitlement checks. This issue is fixed in macOS Sequoia 15.8, macOS… |
| 2026-10-20 01:17:26 | [CVE-2026-86913](https://nvd.nist.gov/vuln/detail/CVE-2026-86913) |  |  | A use after free issue was addressed with improved memory management. This issue is fixed in iOS 26.7 and iPadOS 26.7,… |
| 2026-10-20 01:17:27 | [CVE-2026-86915](https://nvd.nist.gov/vuln/detail/CVE-2026-86915) |  |  | A race condition was addressed with improved locking. This issue is fixed in macOS Golden Gate 27. An app may be able t… |
| 2026-10-20 01:17:27 | [CVE-2026-86918](https://nvd.nist.gov/vuln/detail/CVE-2026-86918) |  |  | An out-of-bounds write issue was addressed with improved bounds checking. This issue is fixed in iOS 27 and iPadOS 27,… |
| 2026-10-20 01:17:27 | [CVE-2026-86919](https://nvd.nist.gov/vuln/detail/CVE-2026-86919) |  |  | A stack overflow was addressed with improved input validation. This issue is fixed in iOS 26.7 and iPadOS 26.7, iOS 27… |
| 2026-10-20 01:17:27 | [CVE-2026-86921](https://nvd.nist.gov/vuln/detail/CVE-2026-86921) |  |  | A permissions issue was addressed with improved validation. This issue is fixed in iOS 26.7 and iPadOS 26.7, iOS 27 and… |
| 2026-10-20 01:17:27 | [CVE-2026-86928](https://nvd.nist.gov/vuln/detail/CVE-2026-86928) |  |  | A path handling issue was addressed with improved validation. This issue is fixed in macOS Golden Gate 27. An app may b… |
| 2026-10-20 01:17:27 | [CVE-2026-86922](https://nvd.nist.gov/vuln/detail/CVE-2026-86922) |  |  | A type confusion issue was addressed with improved state management. This issue is fixed in Safari 27, iOS 27 and iPadO… |
| 2026-10-20 01:17:27 | [CVE-2026-86932](https://nvd.nist.gov/vuln/detail/CVE-2026-86932) |  |  | An authorization issue was addressed with improved state management. This issue is fixed in macOS Golden Gate 27. An ap… |
| 2026-10-20 01:17:27 | [CVE-2026-86933](https://nvd.nist.gov/vuln/detail/CVE-2026-86933) |  |  | A permissions issue was addressed with additional sandbox restrictions. This issue is fixed in macOS Golden Gate 27. An… |
| 2026-10-20 01:17:27 | [CVE-2026-86935](https://nvd.nist.gov/vuln/detail/CVE-2026-86935) |  |  | This issue was addressed by removing additional entitlements. This issue is fixed in macOS Golden Gate 27. An app may b… |
| 2026-10-20 01:17:27 | [CVE-2026-86914](https://nvd.nist.gov/vuln/detail/CVE-2026-86914) |  |  | An information disclosure issue was addressed with improved state management. This issue is fixed in macOS Golden Gate… |
| 2026-10-20 01:17:28 | [CVE-2026-86940](https://nvd.nist.gov/vuln/detail/CVE-2026-86940) |  |  | This issue was addressed by removing the vulnerable code. This issue is fixed in macOS Golden Gate 27. An app may be ab… |
| 2026-10-20 01:17:28 | [CVE-2026-86944](https://nvd.nist.gov/vuln/detail/CVE-2026-86944) |  |  | An out-of-bounds write issue was addressed with improved bounds checking. This issue is fixed in iOS 26.7 and iPadOS 26… |
| 2026-10-20 01:17:28 | [CVE-2026-86948](https://nvd.nist.gov/vuln/detail/CVE-2026-86948) |  |  | This issue was addressed by enforcing library validation on the affected binaries. This issue is fixed in Xcode 27. An… |
| 2026-10-20 01:17:28 | [CVE-2026-86949](https://nvd.nist.gov/vuln/detail/CVE-2026-86949) |  |  | This issue was addressed by enforcing library validation on the affected binaries. This issue is fixed in Xcode 27. A m… |
| 2026-10-20 01:17:28 | [CVE-2026-86953](https://nvd.nist.gov/vuln/detail/CVE-2026-86953) |  |  | An out-of-bounds write issue was addressed with improved bounds checking. This issue is fixed in iOS 27 and iPadOS 27,… |
| 2026-10-20 01:17:28 | [CVE-2026-86955](https://nvd.nist.gov/vuln/detail/CVE-2026-86955) |  |  | An authorization issue was addressed with improved state management. This issue is fixed in iOS 27 and iPadOS 27. An ap… |
| 2026-10-20 01:17:28 | [CVE-2026-86957](https://nvd.nist.gov/vuln/detail/CVE-2026-86957) |  |  | An out-of-bounds read was addressed with improved bounds checking. This issue is fixed in iOS 26.7 and iPadOS 26.7, iOS… |
| 2026-10-20 01:17:28 | [CVE-2026-86959](https://nvd.nist.gov/vuln/detail/CVE-2026-86959) |  |  | An input validation issue was addressed with improved input validation. This issue is fixed in iOS 26.7 and iPadOS 26.7… |
| 2026-10-20 01:17:28 | [CVE-2026-86961](https://nvd.nist.gov/vuln/detail/CVE-2026-86961) |  |  | A race condition was addressed with additional validation. This issue is fixed in iOS 27 and iPadOS 27, macOS Golden Ga… |
| 2026-10-20 01:17:28 | [CVE-2026-86962](https://nvd.nist.gov/vuln/detail/CVE-2026-86962) |  |  | A double free issue was addressed with improved memory management. This issue is fixed in iOS 26.7 and iPadOS 26.7, iOS… |
| 2026-10-20 01:17:29 | [CVE-2026-86963](https://nvd.nist.gov/vuln/detail/CVE-2026-86963) |  |  | A denial-of-service issue was addressed with improved input validation. This issue is fixed in iOS 26.7 and iPadOS 26.7… |
| 2026-10-20 01:17:29 | [CVE-2026-86975](https://nvd.nist.gov/vuln/detail/CVE-2026-86975) |  |  | An out-of-bounds read was addressed with improved bounds checking. This issue is fixed in iOS 27 and iPadOS 27, macOS G… |
| 2026-10-20 01:17:29 | [CVE-2026-86976](https://nvd.nist.gov/vuln/detail/CVE-2026-86976) |  |  | An authorization issue was addressed with improved state management. This issue is fixed in iOS 27 and iPadOS 27, macOS… |
| 2026-10-20 01:17:29 | [CVE-2026-86977](https://nvd.nist.gov/vuln/detail/CVE-2026-86977) |  |  | An authorization issue was addressed with improved network restrictions. This issue is fixed in iOS 27 and iPadOS 27. A… |
| 2026-10-20 01:17:29 | [CVE-2026-86979](https://nvd.nist.gov/vuln/detail/CVE-2026-86979) |  |  | A privacy issue was addressed with improved checks. This issue is fixed in macOS Golden Gate 27. An app may be able to… |
| 2026-10-20 01:17:29 | [CVE-2026-86981](https://nvd.nist.gov/vuln/detail/CVE-2026-86981) |  |  | An out-of-bounds write issue was addressed with improved bounds checking. This issue is fixed in macOS Sequoia 15.8, ma… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
