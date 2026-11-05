# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-11-05 03:20 UTC

New CVEs published between 2026-11-05 02:20 UTC and 2026-11-05 03:20 UTC.

[Full CSV](data/new-cves-2026-11-05T03-20-03-424324Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-11-05 03:17:17 | [CVE-2025-66365](https://nvd.nist.gov/vuln/detail/CVE-2025-66365) |  |  | Incorrect handling of SIP packets leads to baseband crashes |
| 2026-11-05 03:17:17 | [CVE-2025-66366](https://nvd.nist.gov/vuln/detail/CVE-2025-66366) |  |  | Incorrect handling of unauthenticated downlink RRC Setup messages can cause the baseband to crash |
| 2026-11-05 03:17:17 | [CVE-2025-66367](https://nvd.nist.gov/vuln/detail/CVE-2025-66367) |  |  | Improper handling of NAS DLTransport messages may lead to a baseband crash. |
| 2026-11-05 03:17:18 | [CVE-2025-66368](https://nvd.nist.gov/vuln/detail/CVE-2025-66368) |  |  | Incorrect handling of SDP payload leads to a Denial of Service |
| 2026-11-05 03:17:20 | [CVE-2026-122159](https://nvd.nist.gov/vuln/detail/CVE-2026-122159) | Low | 2.1 | A weakness has been identified in Edge0-AI Audio8_TTS up to 1d64afcc2da56222b41ddcf53de7b8bc54be1fb6. This affects the… |
| 2026-11-05 03:17:21 | [CVE-2026-122160](https://nvd.nist.gov/vuln/detail/CVE-2026-122160) | Low | 2.1 | A security vulnerability has been detected in myshell-ai AIlice up to 0.4.0. This vulnerability affects the function Lo… |
| 2026-11-05 03:17:21 | [CVE-2026-122188](https://nvd.nist.gov/vuln/detail/CVE-2026-122188) | Low | 2.1 | A flaw has been found in DeepGraphLearning KnowledgeGraphEmbedding up to 2e440e0f9c687314d5ff67ead68ce985dc446e3a. Impa… |
| 2026-11-05 03:17:21 | [CVE-2026-122189](https://nvd.nist.gov/vuln/detail/CVE-2026-122189) | Low | 2.1 | A vulnerability has been found in OpenPPL ppl.nn up to bb84dc9952809b3a5a0036858a3d9f68af1c83d5. The affected element i… |
| 2026-11-05 03:17:21 | [CVE-2026-122301](https://nvd.nist.gov/vuln/detail/CVE-2026-122301) | Low | 2.3 | Parse Server before 8.6.114 and 9.0.0 before 9.10.6-alpha.6 returns field values in object create responses to callers… |
| 2026-11-05 03:17:22 | [CVE-2026-122302](https://nvd.nist.gov/vuln/detail/CVE-2026-122302) | Critical | 9.3 | Kyverno before 1.19.2 contains a privilege escalation vulnerability that allows namespace admins to create resources be… |
| 2026-11-05 03:17:22 | [CVE-2026-122303](https://nvd.nist.gov/vuln/detail/CVE-2026-122303) | Critical | 9.4 | Kyverno from 1.17.0 before 1.19.2 contains an authorization bypass vulnerability that allows namespace tenants to overw… |
| 2026-11-05 03:17:22 | [CVE-2026-122304](https://nvd.nist.gov/vuln/detail/CVE-2026-122304) | Critical | 9.4 | Kyverno from 1.17.0 before 1.19.2 contains an authorization bypass vulnerability that allows namespace admins to escape… |
| 2026-11-05 03:17:22 | [CVE-2026-122305](https://nvd.nist.gov/vuln/detail/CVE-2026-122305) | High | 8.3 | Kyverno before 1.19.2 contains a denial of service vulnerability in substituteVariablesIfAny that allows low-privileged… |
| 2026-11-05 03:17:22 | [CVE-2026-122306](https://nvd.nist.gov/vuln/detail/CVE-2026-122306) | High | 8.3 | Kyverno before 1.19.2 contains a denial of service vulnerability that allows namespaced policy authors to exhaust admis… |
| 2026-11-05 03:17:22 | [CVE-2026-122307](https://nvd.nist.gov/vuln/detail/CVE-2026-122307) | High | 8.3 | Kyverno before 1.19.2 contains a policy bypass vulnerability in the admissionpolicygenerator controller, which folds Po… |
| 2026-11-05 03:17:23 | [CVE-2026-122309](https://nvd.nist.gov/vuln/detail/CVE-2026-122309) | High | 8.2 | Kyverno before 1.19.2 contains a denial of service vulnerability that allows namespace-scoped policy authors to exhaust… |
| 2026-11-05 03:17:23 | [CVE-2026-122310](https://nvd.nist.gov/vuln/detail/CVE-2026-122310) | Critical | 9.4 | Kyverno from 1.19.1 before 1.19.2 validates a Policy's context.apiCall urlPath after cleaning it but executes the raw p… |
| 2026-11-05 03:17:23 | [CVE-2026-122311](https://nvd.nist.gov/vuln/detail/CVE-2026-122311) | Critical | 9.4 | Kyverno from 1.16.0 before 1.19.2 fails to validate path segments in the resource argument of resource.get() and resour… |
| 2026-11-05 03:17:23 | [CVE-2026-122312](https://nvd.nist.gov/vuln/detail/CVE-2026-122312) | High | 8.3 | Kyverno from 1.19.1 before 1.19.2 contains a namespace isolation bypass in APICall Fetch() in pkg/engine/apicall/apiCal… |
| 2026-11-05 03:17:23 | [CVE-2026-122313](https://nvd.nist.gov/vuln/detail/CVE-2026-122313) | Critical | 9.4 | Kyverno from 1.17.0 before 1.19.2 contains a privilege escalation vulnerability that allows namespace-scoped tenants to… |
| 2026-11-05 03:17:23 | [CVE-2026-122308](https://nvd.nist.gov/vuln/detail/CVE-2026-122308) | High | 8.4 | Kyverno before 1.19.2 contains an authorization bypass vulnerability in the Generation Handler that allows users with c… |
| 2026-11-05 03:17:24 | [CVE-2026-122314](https://nvd.nist.gov/vuln/detail/CVE-2026-122314) | High | 8.7 | Kyverno before 1.19.2 contains an unchecked type assertion in its variable-substitution engine that allows users who ca… |
| 2026-11-05 03:17:24 | [CVE-2026-122315](https://nvd.nist.gov/vuln/detail/CVE-2026-122315) | High | 8.7 | Kyverno before 1.19.2 contains an unchecked type assertion in buildStatementMap that allows unauthenticated attackers t… |
| 2026-11-05 03:17:24 | [CVE-2026-122316](https://nvd.nist.gov/vuln/detail/CVE-2026-122316) | High | 8.4 | Kyverno from 1.17.0 before 1.19.2 contains a missing authorization vulnerability in the mutate-existing background proc… |
| 2026-11-05 03:17:24 | [CVE-2026-122318](https://nvd.nist.gov/vuln/detail/CVE-2026-122318) | High | 7.2 | Kyverno before 1.19.2 contains an authentication bypass in matchCertificateData that skips verifyImages subject and sub… |
| 2026-11-05 03:17:24 | [CVE-2026-122319](https://nvd.nist.gov/vuln/detail/CVE-2026-122319) | High | 8.7 | Kyverno before 1.19.2 contains a denial-of-service vulnerability in the In and NotIn operators that allows attackers to… |
| 2026-11-05 03:17:24 | [CVE-2026-122320](https://nvd.nist.gov/vuln/detail/CVE-2026-122320) | High | 8.3 | Kyverno before 1.19.2 contains a missing authorization vulnerability that allows namespaced Policy authors to read reso… |
| 2026-11-05 03:17:25 | [CVE-2026-122321](https://nvd.nist.gov/vuln/detail/CVE-2026-122321) | High | 8.5 | Kyverno 1.18.0 before 1.19.2 contains a signature verification bypass in verifyImages because cached verification resul… |
| 2026-11-05 03:17:25 | [CVE-2026-122322](https://nvd.nist.gov/vuln/detail/CVE-2026-122322) | High | 8.7 | Kyverno from 1.11.0 before 1.19.2 contains an unbounded decompression vulnerability in extractStatement that allows rem… |
| 2026-11-05 03:17:25 | [CVE-2026-122323](https://nvd.nist.gov/vuln/detail/CVE-2026-122323) | High | 8.7 | Kyverno from 1.11.0 before 1.19.2 contains an unbounded decompression vulnerability in FetchSignatureBlob that allows a… |
| 2026-11-05 03:17:25 | [CVE-2026-122992](https://nvd.nist.gov/vuln/detail/CVE-2026-122992) | Critical | 9.2 | In G4KLX DStarGateway and F4FXL DStarGateway before 7b75de6, dstarCallsignToAPRS in APRSUtils.cpp has an integer underf… |
| 2026-11-05 03:17:26 | [CVE-2026-33958](https://nvd.nist.gov/vuln/detail/CVE-2026-33958) |  |  | Processing a malformed RRC Reconfiguration message leads to an out-of-bounds (OOB) access, resulting in a denial-of-ser… |
| 2026-11-05 03:17:26 | [CVE-2026-33965](https://nvd.nist.gov/vuln/detail/CVE-2026-33965) |  |  | An attacker may send a malicious IMS message to the target device, potentially leading to information exposure through… |
| 2026-11-05 03:17:26 | [CVE-2026-33969](https://nvd.nist.gov/vuln/detail/CVE-2026-33969) |  |  | In the NAS Authentication Request message decoding procedure, a missing lower bound check causes an infinite loop, lead… |
| 2026-11-05 03:17:26 | [CVE-2026-33971](https://nvd.nist.gov/vuln/detail/CVE-2026-33971) |  |  | In the LTE RRC component, improper handling of messages before authentication triggers a data abort, which leads to a d… |
| 2026-11-05 03:17:26 | [CVE-2026-33972](https://nvd.nist.gov/vuln/detail/CVE-2026-33972) |  |  | In the Exynos modem's IMS stack, Out of Bound access occurs due to improper validation. |
| 2026-11-05 03:17:26 | [CVE-2026-35494](https://nvd.nist.gov/vuln/detail/CVE-2026-35494) |  |  | In the baseband, memory corruption during NAS packet processing can cause a denial of service. |
| 2026-11-05 03:17:27 | [CVE-2026-35495](https://nvd.nist.gov/vuln/detail/CVE-2026-35495) |  |  | In IMS stack, improper handling of SIP packets leads to Incorrect_Access_Control vulnerability |
| 2026-11-05 03:17:27 | [CVE-2026-48173](https://nvd.nist.gov/vuln/detail/CVE-2026-48173) |  |  | In the NAS message handler, improper validation of the length field in NAS message causes memory corruption |
| 2026-11-05 03:17:27 | [CVE-2026-48174](https://nvd.nist.gov/vuln/detail/CVE-2026-48174) |  |  | In the NR RRC component, improper handling of messages before authentication triggers a data abort, which leads to a de… |
| 2026-11-05 03:17:27 | [CVE-2026-48175](https://nvd.nist.gov/vuln/detail/CVE-2026-48175) |  |  | Processing a malformed RRC message leads to an out-of-bounds read, resulting in a denial-of-service condition. |
| 2026-11-05 03:17:27 | [CVE-2026-48176](https://nvd.nist.gov/vuln/detail/CVE-2026-48176) |  |  | A memory corruption vulnerability caused by improper validation of messages |
| 2026-11-05 03:17:28 | [CVE-2026-48178](https://nvd.nist.gov/vuln/detail/CVE-2026-48178) |  |  | Out of bound access in PPC due to race condition in global variable access |
| 2026-11-05 03:17:28 | [CVE-2026-48179](https://nvd.nist.gov/vuln/detail/CVE-2026-48179) |  |  | In the Exynos modem's IMS stack, improper handling of SDP payload leads to a Denial of Service |
| 2026-11-05 03:17:28 | [CVE-2026-48183](https://nvd.nist.gov/vuln/detail/CVE-2026-48183) |  |  | Improper permission handling during buffer operations allows untrusted applications to create memory mappings with inap… |
| 2026-11-05 03:17:28 | [CVE-2026-48186](https://nvd.nist.gov/vuln/detail/CVE-2026-48186) |  |  | Improper handling of messages before AS security activation can cause unexpected behavior |
| 2026-11-05 03:17:31 | [CVE-2026-68984](https://nvd.nist.gov/vuln/detail/CVE-2026-68984) |  |  | In the Samsung Exynos NPU kernel driver, an integer overflow allows an unprivileged application to trigger memory corru… |
| 2026-11-05 03:17:31 | [CVE-2026-68985](https://nvd.nist.gov/vuln/detail/CVE-2026-68985) |  |  | In the Samsung Exynos NPU driver, improper validation of user input in the ioctl handler can lead to an out-of-bounds w… |
| 2026-11-05 03:17:31 | [CVE-2026-68990](https://nvd.nist.gov/vuln/detail/CVE-2026-68990) |  |  | In the Samsung Exynos H-Arx DRM plugin, improper input validation during buffer operations can cause memory corruption,… |
| 2026-11-05 03:17:31 | [CVE-2026-68991](https://nvd.nist.gov/vuln/detail/CVE-2026-68991) |  |  | In the Samsung Exynos ENN NeuralNetworks HAL, improper input validation during request processing can cause memory corr… |
| 2026-11-05 03:17:31 | [CVE-2026-68993](https://nvd.nist.gov/vuln/detail/CVE-2026-68993) |  |  | A double free vulnerability in NPU driver due to improper pointer management (940) |
| 2026-11-05 03:17:31 | [CVE-2026-68994](https://nvd.nist.gov/vuln/detail/CVE-2026-68994) |  |  | A double free vulnerability in NPU driver due to improper pointer management (941) |
| 2026-11-05 03:17:31 | [CVE-2026-69002](https://nvd.nist.gov/vuln/detail/CVE-2026-69002) |  |  | Incorrect authorization in Samsung framework services due to missing permission checks |
| 2026-11-05 03:17:32 | [CVE-2026-69006](https://nvd.nist.gov/vuln/detail/CVE-2026-69006) |  |  | Insufficient validation of length fields in the GNSS firmware loader can result in kernel‑memory corruption. |
| 2026-11-05 03:17:32 | [CVE-2026-69025](https://nvd.nist.gov/vuln/detail/CVE-2026-69025) |  |  | In the Exynos NPU driver, improper validation of user input in the ioctl handler can lead to an out-of-bounds write, wh… |
| 2026-11-05 03:17:32 | [CVE-2026-69043](https://nvd.nist.gov/vuln/detail/CVE-2026-69043) |  |  | In the Samsung Exynos GPU driver, improper synchronization during buffer object creation and closing can lead to memory… |
| 2026-11-05 03:17:32 | [CVE-2026-69044](https://nvd.nist.gov/vuln/detail/CVE-2026-69044) |  |  | In the Samsung GPU driver, improper reference count handling during command submission can lead to memory corruption. |
| 2026-11-05 03:17:32 | [CVE-2026-69050](https://nvd.nist.gov/vuln/detail/CVE-2026-69050) |  |  | Out-of-bounds memory access in a device driver due to improper resource state tracking. |
| 2026-11-05 03:17:32 | [CVE-2026-69066](https://nvd.nist.gov/vuln/detail/CVE-2026-69066) |  |  | Memory corruption in GPU driver due to improper validation of VMID reservation. |
| 2026-11-05 03:17:32 | [CVE-2026-69068](https://nvd.nist.gov/vuln/detail/CVE-2026-69068) |  |  | Insufficient length validation in the GNSS firmware loader may lead to corruption of kernel memory. |
| 2026-11-05 03:17:32 | [CVE-2026-69005](https://nvd.nist.gov/vuln/detail/CVE-2026-69005) |  |  | Integer overflow in NPU driver parameter processing due to insufficient bounds checking. |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
