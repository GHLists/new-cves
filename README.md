# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-22 19:19 UTC

New CVEs published between 2026-10-22 18:18 UTC and 2026-10-22 19:19 UTC.

[Full CSV](data/new-cves-2026-10-22T19-19-48-974405Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-10-22 19:17:30 | [CVE-2022-51026](https://nvd.nist.gov/vuln/detail/CVE-2022-51026) | Critical | 9.3 | Bytebase 0.12.0 before 1.0.1 contains an authentication bypass vulnerability that allows unauthenticated attackers to l… |
| 2026-10-22 19:17:32 | [CVE-2025-65200](https://nvd.nist.gov/vuln/detail/CVE-2025-65200) |  |  | An issue was discovered in localstack 4.9.2 allowing attackers to execute arbitrary code via crafted content hosted on… |
| 2026-10-22 19:17:33 | [CVE-2025-69723](https://nvd.nist.gov/vuln/detail/CVE-2025-69723) |  |  | A reflected cross-site scripting (XSS) vulnerability in localstack v4.9.2 allows attackers to execute arbitrary Javascr… |
| 2026-10-22 19:17:36 | [CVE-2026-113875](https://nvd.nist.gov/vuln/detail/CVE-2026-113875) | Low | 2.3 | On a SmileCDR HAPI FHIR server with REST-hook subscriptions enabled, if a user is granted subscription-creation permiss… |
| 2026-10-22 19:17:36 | [CVE-2026-113876](https://nvd.nist.gov/vuln/detail/CVE-2026-113876) | Medium | 5.3 | SmileCDR HAPI FHIR does not correctly check authorization for conditional create actions. A user with CREATE but not RE… |
| 2026-10-22 19:17:37 | [CVE-2026-114519](https://nvd.nist.gov/vuln/detail/CVE-2026-114519) | High | 8.6 | Missing Authorization (CWE-862) in the user API of Roskus Prospero Flow CRM from 2.0.0 before 5.26.0 allows a user with… |
| 2026-10-22 19:17:37 | [CVE-2026-114612](https://nvd.nist.gov/vuln/detail/CVE-2026-114612) | Critical | 9.9 | LiteLLM is a proxy server (AI Gateway) to call LLM APIs in OpenAI (or native) format. From 1.87.0 until 1.100.4, 1.101.… |
| 2026-10-22 19:17:37 | [CVE-2026-114613](https://nvd.nist.gov/vuln/detail/CVE-2026-114613) | High | 7.5 | MessagePack is the serializer implementation for Python msgpack.org. Prior to 1.2.3, the msgpack-python C extension (ms… |
| 2026-10-22 19:17:37 | [CVE-2026-114643](https://nvd.nist.gov/vuln/detail/CVE-2026-114643) | Medium | 5.3 | The MongoDB C# Driver writes GeoJSON extra members without checking whether their names collide with reserved GeoJSON m… |
| 2026-10-22 19:17:38 | [CVE-2026-114644](https://nvd.nist.gov/vuln/detail/CVE-2026-114644) | High | 8.2 | The MongoDB C# Driver's BSON library contains an uncontrolled resource consumption weakness in its deserialization hand… |
| 2026-10-22 19:17:38 | [CVE-2026-114645](https://nvd.nist.gov/vuln/detail/CVE-2026-114645) | Medium | 5.7 | A 32-bit integer wraparound in the MongoDB C Driver's Windows-only Kerberos/SSPI authentication code can cause an under… |
| 2026-10-22 19:17:38 | [CVE-2026-114646](https://nvd.nist.gov/vuln/detail/CVE-2026-114646) | Medium | 6.9 | A data-validation flaw exists in the BSON handling and binary serialization path of the MongoDB C# Driver. When an appl… |
| 2026-10-22 19:17:38 | [CVE-2026-114647](https://nvd.nist.gov/vuln/detail/CVE-2026-114647) | Medium | 5.3 | The MongoDB C# Driver does not reject replacement documents whose top-level field names begin with a dollar sign in Fin… |
| 2026-10-22 19:17:38 | [CVE-2026-114648](https://nvd.nist.gov/vuln/detail/CVE-2026-114648) | High | 7.2 | The MongoDB C# Driver does not neutralize dot and dollar characters in dictionary keys, field names and array-filter id… |
| 2026-10-22 19:17:38 | [CVE-2026-114649](https://nvd.nist.gov/vuln/detail/CVE-2026-114649) | High | 7.6 | The MongoDB C# Driver compares TLS client certificates by issuer and serial number only when deciding whether two clien… |
| 2026-10-22 19:17:38 | [CVE-2026-114650](https://nvd.nist.gov/vuln/detail/CVE-2026-114650) | Medium | 6.9 | A flaw in the client-side encryption support of the MongoDB .NET/C# driver can cause data designated for client-side fi… |
| 2026-10-22 19:17:39 | [CVE-2026-114651](https://nvd.nist.gov/vuln/detail/CVE-2026-114651) | Medium | 6.3 | A memory-handling weakness in the BSON deserialization component of the MongoDB C# Driver may cause data left over from… |
| 2026-10-22 19:17:39 | [CVE-2026-114652](https://nvd.nist.gov/vuln/detail/CVE-2026-114652) | High | 7.1 | A data-query-logic neutralization weakness in the update-statement construction component of the MongoDB C# Driver can… |
| 2026-10-22 19:17:39 | [CVE-2026-114653](https://nvd.nist.gov/vuln/detail/CVE-2026-114653) | High | 7.1 | A client-side encryption schema construction component in the MongoDB C# Driver places caller-supplied field identifier… |
| 2026-10-22 19:17:39 | [CVE-2026-114654](https://nvd.nist.gov/vuln/detail/CVE-2026-114654) | Medium | 6.9 | A numeric-type conversion flaw in the BSON handling library of the MongoDB C# Driver allows an out-of-range binary subt… |
| 2026-10-22 19:17:40 | [CVE-2026-114655](https://nvd.nist.gov/vuln/detail/CVE-2026-114655) | Medium | 6.0 | libmongocrypt builds requests to external key management services (AWS, Azure and GCP) by inserting values from key vau… |
| 2026-10-22 19:17:40 | [CVE-2026-115347](https://nvd.nist.gov/vuln/detail/CVE-2026-115347) | High | 8.7 | Mistune before 3.3.0 contains an inefficient algorithmic complexity vulnerability in parse_link_text that allows remote… |
| 2026-10-22 19:17:40 | [CVE-2026-115348](https://nvd.nist.gov/vuln/detail/CVE-2026-115348) | High | 8.7 | Mistune from 3.0.0 before 3.3.0 contains an algorithmic complexity vulnerability in the inline link parser's parse_link… |
| 2026-10-22 19:17:40 | [CVE-2026-115349](https://nvd.nist.gov/vuln/detail/CVE-2026-115349) | High | 8.7 | Mistune from 3.0.0 before 3.3.0 contains an algorithmic complexity denial of service vulnerability in the parse_link_te… |
| 2026-10-22 19:17:40 | [CVE-2026-115350](https://nvd.nist.gov/vuln/detail/CVE-2026-115350) | Medium | 5.3 | Mistune before 3.3.0 contains a cross-site scripting vulnerability in the Include directive that emits included .html,… |
| 2026-10-22 19:17:40 | [CVE-2026-115351](https://nvd.nist.gov/vuln/detail/CVE-2026-115351) | Medium | 5.3 | Mistune from 3.2.1 before 3.3.0 contains a CSS injection vulnerability that allows attackers controlling markdown input… |
| 2026-10-22 19:17:41 | [CVE-2026-115352](https://nvd.nist.gov/vuln/detail/CVE-2026-115352) | High | 8.7 | Mistune before 3.3.0 contains an algorithmic complexity vulnerability in the inline link parser that allows unauthentic… |
| 2026-10-22 19:17:41 | [CVE-2026-115353](https://nvd.nist.gov/vuln/detail/CVE-2026-115353) | Critical | 9.2 | Mistune before 3.3.0 contains a path traversal vulnerability in the RST include directive that allows attackers to read… |
| 2026-10-22 19:17:41 | [CVE-2026-115354](https://nvd.nist.gov/vuln/detail/CVE-2026-115354) | High | 7.1 | Mistune before 3.3.0 contains a path traversal vulnerability in the opt-in Include directive that allows attackers to r… |
| 2026-10-22 19:17:41 | [CVE-2026-115355](https://nvd.nist.gov/vuln/detail/CVE-2026-115355) | High | 8.7 | Mistune before 3.3.0 contains a path traversal vulnerability in the Include directive that allows attackers to read arb… |
| 2026-10-22 19:17:41 | [CVE-2026-115356](https://nvd.nist.gov/vuln/detail/CVE-2026-115356) | Medium | 5.3 | OpenBao before 2.6.4 and 2.7.x before 2.7.1 does not verify, when renewing a token issued by the Kubernetes Auth method… |
| 2026-10-22 19:17:41 | [CVE-2026-115357](https://nvd.nist.gov/vuln/detail/CVE-2026-115357) | Low | 2.1 | OpenBao before 2.6.4 and 2.7.x before 2.7.1 fails to write response audit entries for the unauthenticated sys/generate-… |
| 2026-10-22 19:17:41 | [CVE-2026-115358](https://nvd.nist.gov/vuln/detail/CVE-2026-115358) | Low | 2.0 | OpenBao before 2.6.3 contains an information disclosure vulnerability that allows attackers to leak sensitive data into… |
| 2026-10-22 19:17:42 | [CVE-2026-115359](https://nvd.nist.gov/vuln/detail/CVE-2026-115359) | Medium | 6.3 | OpenBao before 2.6.4 and 2.7.x before 2.7.1 contains a flaw in its rate limit quota subsystem where role resolution fai… |
| 2026-10-22 19:17:42 | [CVE-2026-115360](https://nvd.nist.gov/vuln/detail/CVE-2026-115360) | Medium | 5.3 | OpenBao before 2.6.3 contains an open redirect vulnerability in the UI's OIDC identity provider that affects users not… |
| 2026-10-22 19:17:42 | [CVE-2026-115361](https://nvd.nist.gov/vuln/detail/CVE-2026-115361) | Low | 2.1 | OpenBao before 2.6.3 contains an ACL bypass vulnerability that silently drops explicit deny rules based on forbidden id… |
| 2026-10-22 19:17:42 | [CVE-2026-115362](https://nvd.nist.gov/vuln/detail/CVE-2026-115362) | Low | 2.1 | OpenBao before 2.6.4 and 2.7.x before 2.7.1 does not check Secret ID expiration at use in the AppRole auth method, leav… |
| 2026-10-22 19:17:42 | [CVE-2026-115363](https://nvd.nist.gov/vuln/detail/CVE-2026-115363) | Low | 2.1 | OpenBao 2.2.0 before 2.6.4 and 2.7.0 before 2.7.1 contains an information disclosure vulnerability that exposes the tls… |
| 2026-10-22 19:17:42 | [CVE-2026-115364](https://nvd.nist.gov/vuln/detail/CVE-2026-115364) | Low | 2.1 | OpenBao before 2.6.3 contains a missing authorization check that allows attackers to stop Agent and Proxy services by o… |
| 2026-10-22 19:17:42 | [CVE-2026-115365](https://nvd.nist.gov/vuln/detail/CVE-2026-115365) | High | 7.5 | OpenBao from 2.3.0 before 2.6.3 contains an incorrect authorization vulnerability in its ACL policy cache that allows t… |
| 2026-10-22 19:17:43 | [CVE-2026-115366](https://nvd.nist.gov/vuln/detail/CVE-2026-115366) | Low | 2.0 | OpenBao from 2.3.0 before 2.6.3 contains an improper authorization vulnerability that allows privileged child-namespace… |
| 2026-10-22 19:17:43 | [CVE-2026-115369](https://nvd.nist.gov/vuln/detail/CVE-2026-115369) | Low | 2.1 | OpenBao from 2.5.0 before 2.6.2 fails to enforce the PKI role allowed_ip_sans_cidr restriction on IP SANs taken from a… |
| 2026-10-22 19:17:43 | [CVE-2026-115370](https://nvd.nist.gov/vuln/detail/CVE-2026-115370) | Medium | 5.3 | Incus 6.0.5 before 6.0.7, 6.12.0 before 7.0.2, and 7.1.0 before 7.5.0 contains a restriction bypass vulnerability that… |
| 2026-10-22 19:17:43 | [CVE-2026-115371](https://nvd.nist.gov/vuln/detail/CVE-2026-115371) | High | 7.1 | Incus 6.0.3 before 6.0.7, 6.6.0 before 7.0.2, and 7.1.0 before 7.5.0 contains an improper authorization vulnerability t… |
| 2026-10-22 19:17:43 | [CVE-2026-115372](https://nvd.nist.gov/vuln/detail/CVE-2026-115372) | Critical | 9.0 | Incus from 7.3.0 before 7.5.0 contains a project restriction bypass that allows restricted project users to set block.c… |
| 2026-10-22 19:17:43 | [CVE-2026-115373](https://nvd.nist.gov/vuln/detail/CVE-2026-115373) | High | 7.0 | Incus before 6.0.7, 6.1.0 before 7.0.2, and 7.1.0 before 7.5.0 contains a missing authorization vulnerability in GET /1… |
| 2026-10-22 19:17:43 | [CVE-2026-115374](https://nvd.nist.gov/vuln/detail/CVE-2026-115374) | High | 7.1 | Incus 7.0.0 before 7.0.2 and 7.1.0 before 7.5.0 contains a signature verification flaw in its built-in S3 server that a… |
| 2026-10-22 19:17:44 | [CVE-2026-115375](https://nvd.nist.gov/vuln/detail/CVE-2026-115375) | Critical | 9.4 | Incus 7.0.0 before 7.0.2 and 7.1.0 before 7.5.0 contains a path traversal vulnerability that allows clients able to cre… |
| 2026-10-22 19:17:44 | [CVE-2026-115376](https://nvd.nist.gov/vuln/detail/CVE-2026-115376) | High | 8.3 | Incus 7.0.1 before 7.0.2 and 7.2.0 before 7.5.0 contains an authorization bypass vulnerability that allows project-rest… |
| 2026-10-22 19:17:44 | [CVE-2026-115377](https://nvd.nist.gov/vuln/detail/CVE-2026-115377) | Critical | 9.4 | Incus before 6.0.7, 6.1.0 before 7.0.2, and 7.1.0 before 7.5.0 contains an arbitrary file write vulnerability that allo… |
| 2026-10-22 19:17:44 | [CVE-2026-115378](https://nvd.nist.gov/vuln/detail/CVE-2026-115378) | Medium | 6.9 | Incus before 6.0.7, 6.1.0 before 7.0.2, and 7.1.0 before 7.5.0 contains an arbitrary file write vulnerability in sftpRe… |
| 2026-10-22 19:17:44 | [CVE-2026-115379](https://nvd.nist.gov/vuln/detail/CVE-2026-115379) | Medium | 6.9 | Wasmtime 47.0.0 before 48.0.4 and 49.0.0 before 49.0.2 contains a missing GC rooting vulnerability that leaves referenc… |
| 2026-10-22 19:17:44 | [CVE-2026-115380](https://nvd.nist.gov/vuln/detail/CVE-2026-115380) | Medium | 5.1 | Wasmtime before 36.0.17, 37.0.0 before 48.0.4, and 49.0.0 before 49.0.2 contains a denial of service vulnerability in t… |
| 2026-10-22 19:17:45 | [CVE-2026-115381](https://nvd.nist.gov/vuln/detail/CVE-2026-115381) | Medium | 5.9 | Wasmtime before 36.0.17, 37.0.0 before 48.0.4, and 49.0.0 before 49.0.2 contains an unbounded memory allocation in the… |
| 2026-10-22 19:17:45 | [CVE-2026-115382](https://nvd.nist.gov/vuln/detail/CVE-2026-115382) | Medium | 5.9 | Wasmtime 46.0.0 before 48.0.4 and 49.0.0 before 49.0.2 contains a denial-of-service vulnerability in its wasi:http impl… |
| 2026-10-22 19:17:45 | [CVE-2026-115383](https://nvd.nist.gov/vuln/detail/CVE-2026-115383) | Medium | 5.9 | Wasmtime 47.0.0 before 48.0.4 and 49.0.0 before 49.0.2 contains an improper validation vulnerability that accepts compo… |
| 2026-10-22 19:17:45 | [CVE-2026-115384](https://nvd.nist.gov/vuln/detail/CVE-2026-115384) | Critical | 9.4 | Wasmtime 39.0.0 before 48.0.4 and 49.0.0 before 49.0.2 contains a stack buffer overflow vulnerability that allows malic… |
| 2026-10-22 19:17:45 | [CVE-2026-115385](https://nvd.nist.gov/vuln/detail/CVE-2026-115385) | Medium | 6.9 | Wasmtime 46.0.0 before 48.0.4 and 49.0.0 before 49.0.2 contains a denial of service vulnerability in the wasmtime-wasi… |
| 2026-10-22 19:17:45 | [CVE-2026-115386](https://nvd.nist.gov/vuln/detail/CVE-2026-115386) | Low | 2.1 | Wasmtime before 36.0.17, 37.0.0 before 48.0.4, and 49.0.0 before 49.0.2 contains an information disclosure vulnerabilit… |
| 2026-10-22 19:17:46 | [CVE-2026-115387](https://nvd.nist.gov/vuln/detail/CVE-2026-115387) | Medium | 6.9 | Wasmtime before 36.0.16, 37.0.0 before 48.0.3, and 49.0.0 before 49.0.1 contains a denial of service vulnerability in w… |
| 2026-10-22 19:17:46 | [CVE-2026-115388](https://nvd.nist.gov/vuln/detail/CVE-2026-115388) | Medium | 6.9 | wasmtime-wasi-http in Wasmtime before 36.0.16, 37.0.0 before 48.0.3, and 49.0.0 before 49.0.1 does not enforce the wasi… |
| 2026-10-22 19:17:46 | [CVE-2026-115389](https://nvd.nist.gov/vuln/detail/CVE-2026-115389) | Low | 1.0 | Wasmtime before 36.0.16, 37.0.0 before 48.0.3, and 49.0.0 before 49.0.1 does not adequately account for host allocation… |
| 2026-10-22 19:17:46 | [CVE-2026-115390](https://nvd.nist.gov/vuln/detail/CVE-2026-115390) | Medium | 6.9 | Wasmtime 47.0.0 before 48.0.3 and 49.0.0 before 49.0.1 contains a fuel accounting flaw in Cranelift-compiled call_ref a… |
| 2026-10-22 19:17:46 | [CVE-2026-115391](https://nvd.nist.gov/vuln/detail/CVE-2026-115391) | Medium | 6.9 | Wasmtime 46.0.0 before 46.0.3 and 47.0.0 before 47.0.4 contains an uncontrolled resource allocation vulnerability in it… |
| 2026-10-22 19:17:46 | [CVE-2026-115392](https://nvd.nist.gov/vuln/detail/CVE-2026-115392) | High | 8.8 | Wasmtime before 24.0.13, 25.0.0 before 36.0.14, 37.0.0 before 46.0.3, and 47.0.0 before 47.0.4 allows a filesystem sand… |
| 2026-10-22 19:17:47 | [CVE-2026-115393](https://nvd.nist.gov/vuln/detail/CVE-2026-115393) | Low | 1.0 | Wasmtime before 24.0.12, 25.0.0 before 36.0.13, 37.0.0 before 46.0.2, and 47.0.0 before 47.0.3 contains a type confusio… |
| 2026-10-22 19:17:47 | [CVE-2026-115394](https://nvd.nist.gov/vuln/detail/CVE-2026-115394) | Medium | 6.8 | Ghidra through 12.2 contains an uncontrolled memory allocation vulnerability in BinaryField.read() that allows attacker… |
| 2026-10-22 19:17:47 | [CVE-2026-115395](https://nvd.nist.gov/vuln/detail/CVE-2026-115395) | Medium | 6.8 | Ghidra 10.3 before 12.2 contains a resource allocation without limits vulnerability in ThemeReader.readZipTheme() that… |
| 2026-10-22 19:17:47 | [CVE-2026-115396](https://nvd.nist.gov/vuln/detail/CVE-2026-115396) | Medium | 6.8 | Ghidra 10.3 before 12.2 contains an improper handling of highly compressed data vulnerability in ThemeReader.processIco… |
| 2026-10-22 19:17:47 | [CVE-2026-115397](https://nvd.nist.gov/vuln/detail/CVE-2026-115397) | Medium | 6.8 | Ghidra before 12.2 contains a resource allocation without limits vulnerability in ExtensionUtils.unzipToInstallationFol… |
| 2026-10-22 19:17:47 | [CVE-2026-115414](https://nvd.nist.gov/vuln/detail/CVE-2026-115414) | High | 8.4 | OS command injection in the Terraform hook in AWS SAM CLI before 1.166.2 might allow an actor who can influence the Ter… |
| 2026-10-22 19:17:48 | [CVE-2026-115517](https://nvd.nist.gov/vuln/detail/CVE-2026-115517) | Medium | 6.4 | Unrestricted network access between execution contexts in KNIME Business Hub before version 1.19.0 allows an authentica… |
| 2026-10-22 19:17:48 | [CVE-2026-115519](https://nvd.nist.gov/vuln/detail/CVE-2026-115519) | Low | 2.1 | Missing security attributes on sensitive cookies in KNIME Business Hub before version 1.19.0 allow an unauthenticated r… |
| 2026-10-22 19:17:56 | [CVE-2026-79844](https://nvd.nist.gov/vuln/detail/CVE-2026-79844) | Critical | 10.0 | No description provided |
| 2026-10-22 19:17:56 | [CVE-2026-79846](https://nvd.nist.gov/vuln/detail/CVE-2026-79846) | Critical | 10.0 | No description provided |
| 2026-10-22 19:17:56 | [CVE-2026-79847](https://nvd.nist.gov/vuln/detail/CVE-2026-79847) | Critical | 10.0 | No description provided |
| 2026-10-22 19:17:56 | [CVE-2026-79848](https://nvd.nist.gov/vuln/detail/CVE-2026-79848) | Critical | 10.0 | No description provided |
| 2026-10-22 19:17:57 | [CVE-2026-79849](https://nvd.nist.gov/vuln/detail/CVE-2026-79849) | Critical | 10.0 | No description provided |
| 2026-10-22 19:17:57 | [CVE-2026-79850](https://nvd.nist.gov/vuln/detail/CVE-2026-79850) | Critical | 10.0 | No description provided |
| 2026-10-22 19:17:57 | [CVE-2026-79851](https://nvd.nist.gov/vuln/detail/CVE-2026-79851) | Critical | 10.0 | No description provided |
| 2026-10-22 19:17:57 | [CVE-2026-79852](https://nvd.nist.gov/vuln/detail/CVE-2026-79852) | Critical | 9.8 | No description provided |
| 2026-10-22 19:17:57 | [CVE-2026-79853](https://nvd.nist.gov/vuln/detail/CVE-2026-79853) | Critical | 9.8 | No description provided |
| 2026-10-22 19:17:57 | [CVE-2026-79854](https://nvd.nist.gov/vuln/detail/CVE-2026-79854) | Critical | 9.8 | No description provided |
| 2026-10-22 19:17:57 | [CVE-2026-79855](https://nvd.nist.gov/vuln/detail/CVE-2026-79855) | Critical | 9.8 | No description provided |
| 2026-10-22 19:17:57 | [CVE-2026-79856](https://nvd.nist.gov/vuln/detail/CVE-2026-79856) | Critical | 9.8 | No description provided |
| 2026-10-22 19:17:57 | [CVE-2026-79857](https://nvd.nist.gov/vuln/detail/CVE-2026-79857) | Critical | 9.8 | No description provided |
| 2026-10-22 19:17:58 | [CVE-2026-79858](https://nvd.nist.gov/vuln/detail/CVE-2026-79858) | Critical | 9.8 | No description provided |
| 2026-10-22 19:17:58 | [CVE-2026-79859](https://nvd.nist.gov/vuln/detail/CVE-2026-79859) | Critical | 9.8 | No description provided |
| 2026-10-22 19:17:58 | [CVE-2026-79860](https://nvd.nist.gov/vuln/detail/CVE-2026-79860) | Critical | 9.8 | No description provided |
| 2026-10-22 19:17:58 | [CVE-2026-79861](https://nvd.nist.gov/vuln/detail/CVE-2026-79861) | Critical | 9.8 | No description provided |
| 2026-10-22 19:17:58 | [CVE-2026-79862](https://nvd.nist.gov/vuln/detail/CVE-2026-79862) | Critical | 9.6 | No description provided |
| 2026-10-22 19:17:58 | [CVE-2026-79863](https://nvd.nist.gov/vuln/detail/CVE-2026-79863) | Critical | 9.6 | No description provided |
| 2026-10-22 19:17:58 | [CVE-2026-79864](https://nvd.nist.gov/vuln/detail/CVE-2026-79864) | Critical | 9.6 | No description provided |
| 2026-10-22 19:17:58 | [CVE-2026-79865](https://nvd.nist.gov/vuln/detail/CVE-2026-79865) | Critical | 9.6 | No description provided |
| 2026-10-22 19:17:58 | [CVE-2026-79866](https://nvd.nist.gov/vuln/detail/CVE-2026-79866) | Critical | 9.6 | No description provided |
| 2026-10-22 19:17:59 | [CVE-2026-79867](https://nvd.nist.gov/vuln/detail/CVE-2026-79867) | Critical | 9.6 | No description provided |
| 2026-10-22 19:17:59 | [CVE-2026-79868](https://nvd.nist.gov/vuln/detail/CVE-2026-79868) | Critical | 9.6 | No description provided |
| 2026-10-22 19:17:59 | [CVE-2026-79869](https://nvd.nist.gov/vuln/detail/CVE-2026-79869) | Critical | 9.6 | No description provided |
| 2026-10-22 19:17:59 | [CVE-2026-79870](https://nvd.nist.gov/vuln/detail/CVE-2026-79870) | Critical | 9.6 | No description provided |
| 2026-10-22 19:17:59 | [CVE-2026-79871](https://nvd.nist.gov/vuln/detail/CVE-2026-79871) | Critical | 9.6 | No description provided |
| 2026-10-22 19:17:59 | [CVE-2026-79872](https://nvd.nist.gov/vuln/detail/CVE-2026-79872) | Critical | 9.4 | No description provided |
| 2026-10-22 19:17:59 | [CVE-2026-79873](https://nvd.nist.gov/vuln/detail/CVE-2026-79873) | Critical | 9.3 | No description provided |
| 2026-10-22 19:17:59 | [CVE-2026-79874](https://nvd.nist.gov/vuln/detail/CVE-2026-79874) | Critical | 9.3 | No description provided |
| 2026-10-22 19:17:59 | [CVE-2026-79875](https://nvd.nist.gov/vuln/detail/CVE-2026-79875) | Critical | 9.3 | No description provided |
| 2026-10-22 19:18:00 | [CVE-2026-79876](https://nvd.nist.gov/vuln/detail/CVE-2026-79876) | Critical | 9.3 | No description provided |
| 2026-10-22 19:18:00 | [CVE-2026-79877](https://nvd.nist.gov/vuln/detail/CVE-2026-79877) | High | 8.8 | No description provided |
| 2026-10-22 19:18:00 | [CVE-2026-79878](https://nvd.nist.gov/vuln/detail/CVE-2026-79878) | High | 8.8 | No description provided |
| 2026-10-22 19:18:00 | [CVE-2026-79879](https://nvd.nist.gov/vuln/detail/CVE-2026-79879) | High | 8.8 | No description provided |
| 2026-10-22 19:18:00 | [CVE-2026-79880](https://nvd.nist.gov/vuln/detail/CVE-2026-79880) | High | 8.7 | No description provided |
| 2026-10-22 19:18:00 | [CVE-2026-79881](https://nvd.nist.gov/vuln/detail/CVE-2026-79881) | High | 8.3 | No description provided |
| 2026-10-22 19:18:00 | [CVE-2026-79882](https://nvd.nist.gov/vuln/detail/CVE-2026-79882) | High | 8.3 | No description provided |
| 2026-10-22 19:18:00 | [CVE-2026-79883](https://nvd.nist.gov/vuln/detail/CVE-2026-79883) | High | 8.3 | No description provided |
| 2026-10-22 19:18:00 | [CVE-2026-79884](https://nvd.nist.gov/vuln/detail/CVE-2026-79884) | High | 8.2 | No description provided |
| 2026-10-22 19:18:01 | [CVE-2026-79885](https://nvd.nist.gov/vuln/detail/CVE-2026-79885) | High | 8.2 | No description provided |
| 2026-10-22 19:18:01 | [CVE-2026-79886](https://nvd.nist.gov/vuln/detail/CVE-2026-79886) | High | 8.2 | No description provided |
| 2026-10-22 19:18:01 | [CVE-2026-79887](https://nvd.nist.gov/vuln/detail/CVE-2026-79887) | High | 8.1 | No description provided |
| 2026-10-22 19:18:01 | [CVE-2026-79888](https://nvd.nist.gov/vuln/detail/CVE-2026-79888) | High | 8.1 | No description provided |
| 2026-10-22 19:18:01 | [CVE-2026-79889](https://nvd.nist.gov/vuln/detail/CVE-2026-79889) | High | 8.1 | No description provided |
| 2026-10-22 19:18:01 | [CVE-2026-79890](https://nvd.nist.gov/vuln/detail/CVE-2026-79890) | High | 8.1 | No description provided |
| 2026-10-22 19:18:01 | [CVE-2026-79891](https://nvd.nist.gov/vuln/detail/CVE-2026-79891) | High | 8.1 | No description provided |
| 2026-10-22 19:18:01 | [CVE-2026-79892](https://nvd.nist.gov/vuln/detail/CVE-2026-79892) | High | 7.8 | No description provided |
| 2026-10-22 19:18:01 | [CVE-2026-79893](https://nvd.nist.gov/vuln/detail/CVE-2026-79893) | High | 7.5 | No description provided |
| 2026-10-22 19:18:01 | [CVE-2026-79894](https://nvd.nist.gov/vuln/detail/CVE-2026-79894) | High | 7.5 | No description provided |
| 2026-10-22 19:18:02 | [CVE-2026-79895](https://nvd.nist.gov/vuln/detail/CVE-2026-79895) | High | 7.5 | No description provided |
| 2026-10-22 19:18:02 | [CVE-2026-79955](https://nvd.nist.gov/vuln/detail/CVE-2026-79955) | High | 7.5 | No description provided |
| 2026-10-22 19:18:02 | [CVE-2026-79956](https://nvd.nist.gov/vuln/detail/CVE-2026-79956) | High | 7.2 | No description provided |
| 2026-10-22 19:18:06 | [CVE-2026-95704](https://nvd.nist.gov/vuln/detail/CVE-2026-95704) | High | 7.2 | No description provided |
| 2026-10-22 19:18:06 | [CVE-2026-95705](https://nvd.nist.gov/vuln/detail/CVE-2026-95705) | High | 7.2 | No description provided |
| 2026-10-22 19:18:06 | [CVE-2026-95706](https://nvd.nist.gov/vuln/detail/CVE-2026-95706) | High | 7.2 | No description provided |
| 2026-10-22 19:18:06 | [CVE-2026-95707](https://nvd.nist.gov/vuln/detail/CVE-2026-95707) | High | 7.2 | No description provided |
| 2026-10-22 19:18:06 | [CVE-2026-95708](https://nvd.nist.gov/vuln/detail/CVE-2026-95708) | High | 7.2 | No description provided |
| 2026-10-22 19:18:06 | [CVE-2026-95709](https://nvd.nist.gov/vuln/detail/CVE-2026-95709) | High | 7.2 | No description provided |
| 2026-10-22 19:18:06 | [CVE-2026-95710](https://nvd.nist.gov/vuln/detail/CVE-2026-95710) | High | 7.1 | No description provided |
| 2026-10-22 19:18:06 | [CVE-2026-95711](https://nvd.nist.gov/vuln/detail/CVE-2026-95711) | High | 7.1 | No description provided |
| 2026-10-22 19:18:07 | [CVE-2026-95712](https://nvd.nist.gov/vuln/detail/CVE-2026-95712) | High | 7.1 | No description provided |
| 2026-10-22 19:18:07 | [CVE-2026-95713](https://nvd.nist.gov/vuln/detail/CVE-2026-95713) | High | 7.0 | No description provided |
| 2026-10-22 19:18:07 | [CVE-2026-95714](https://nvd.nist.gov/vuln/detail/CVE-2026-95714) | Medium | 6.8 | No description provided |
| 2026-10-22 19:18:07 | [CVE-2026-95715](https://nvd.nist.gov/vuln/detail/CVE-2026-95715) | Medium | 6.8 | No description provided |
| 2026-10-22 19:18:07 | [CVE-2026-95716](https://nvd.nist.gov/vuln/detail/CVE-2026-95716) | Medium | 6.5 | No description provided |
| 2026-10-22 19:18:07 | [CVE-2026-95717](https://nvd.nist.gov/vuln/detail/CVE-2026-95717) | Medium | 5.5 | No description provided |
| 2026-10-22 19:18:08 | [CVE-2026-95718](https://nvd.nist.gov/vuln/detail/CVE-2026-95718) | Medium | 5.3 | No description provided |
| 2026-10-22 19:18:08 | [CVE-2026-95719](https://nvd.nist.gov/vuln/detail/CVE-2026-95719) | Medium | 4.9 | No description provided |
| 2026-10-22 19:18:08 | [CVE-2026-95720](https://nvd.nist.gov/vuln/detail/CVE-2026-95720) | Medium | 4.4 | No description provided |
| 2026-10-22 19:18:08 | [CVE-2026-95721](https://nvd.nist.gov/vuln/detail/CVE-2026-95721) | Low | 3.3 | No description provided |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
