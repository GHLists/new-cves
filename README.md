# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-11-19 15:20 UTC

New CVEs published between 2026-11-19 14:21 UTC and 2026-11-19 15:20 UTC.

[Full CSV](data/new-cves-2026-11-19T15-20-24-836292Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-11-19 15:17:24 | [CVE-2026-115560](https://nvd.nist.gov/vuln/detail/CVE-2026-115560) | Critical | 9.2 | Session serializer mismatch can lead to remote code execution. Session upload progress, when enabled, can store attacke… |
| 2026-11-19 15:17:25 | [CVE-2026-120753](https://nvd.nist.gov/vuln/detail/CVE-2026-120753) | Critical | 9.1 | In Eclipse Ditto versions 1.1.0 to 3.9.8, when pre-authentication is enabled, the gateway service accepts the pre-authe… |
| 2026-11-19 15:17:25 | [CVE-2026-121584](https://nvd.nist.gov/vuln/detail/CVE-2026-121584) | Medium | 6.5 | Mattermost versions 11.7.x <= 11.7.11, 11.10.x <= 11.10.2, 11.11.x <= 11.11.1 fail to bound the number of records a sin… |
| 2026-11-19 15:17:25 | [CVE-2026-123890](https://nvd.nist.gov/vuln/detail/CVE-2026-123890) | Critical | 9.8 | VMware vCenter contains an authentication bypass vulnerability in the VMware Directory Service. Affected versions: 9.1.… |
| 2026-11-19 15:17:25 | [CVE-2026-123891](https://nvd.nist.gov/vuln/detail/CVE-2026-123891) | High | 8.1 | SDDC Manager contains an SQL-injection vulnerability due to improper sanitization of user-supplied input. Affected vers… |
| 2026-11-19 15:17:25 | [CVE-2026-123892](https://nvd.nist.gov/vuln/detail/CVE-2026-123892) | High | 7.2 | SDDC Manager contains an authenticated command-injection vulnerability due to improper sanitization of user-supplied in… |
| 2026-11-19 15:17:25 | [CVE-2026-123893](https://nvd.nist.gov/vuln/detail/CVE-2026-123893) | Medium | 6.7 | SDDC Manager contains a local privilege-escalation vulnerability. Affected versions: 9.1.x.x (fixed in 9.1.1.0200); 9.0… |
| 2026-11-19 15:17:25 | [CVE-2026-123894](https://nvd.nist.gov/vuln/detail/CVE-2026-123894) | Medium | 6.7 | VMware Tools for Windows contains a SAML token signature bypass vulnerability. Affected versions: 13.x.x.x (fixed in 13… |
| 2026-11-19 15:17:26 | [CVE-2026-126086](https://nvd.nist.gov/vuln/detail/CVE-2026-126086) | High | 8.8 | In Eclipse Dataspace Components (EDC) – Connector (`org.eclipse.edc:decentralized-claims-*`, `org.eclipse.edc:jwt-verif… |
| 2026-11-19 15:17:26 | [CVE-2026-126714](https://nvd.nist.gov/vuln/detail/CVE-2026-126714) | Critical | 9.2 | Partially overwritten session files can lead to remote code execution. The files session save handler, which is the def… |
| 2026-11-19 15:17:26 | [CVE-2026-127960](https://nvd.nist.gov/vuln/detail/CVE-2026-127960) | High | 8.7 | Denial of service through folded HTTP response headers. The HTTP stream wrapper joins each continuation line of a folde… |
| 2026-11-19 15:17:27 | [CVE-2026-128064](https://nvd.nist.gov/vuln/detail/CVE-2026-128064) | High | 8.2 | Mixed-case HTTPS and FTPS URLs can expose data in plaintext. The HTTP and FTP stream wrappers recognise URL schemes cas… |
| 2026-11-19 15:17:27 | [CVE-2026-128090](https://nvd.nist.gov/vuln/detail/CVE-2026-128090) | High | 7.7 | PHAR OpenSSL signature bypass via algorithm downgrade. The Phar extension selects the signature verification method fro… |
| 2026-11-19 15:17:27 | [CVE-2026-129182](https://nvd.nist.gov/vuln/detail/CVE-2026-129182) | Critical | 9.2 | Use-after-free via repopulation of last_fatal_error_backtrace global after shutdown. A fatal error raised while modifie… |
| 2026-11-19 15:17:27 | [CVE-2026-129289](https://nvd.nist.gov/vuln/detail/CVE-2026-129289) | Critical | 9.2 | PHP-FPM request smuggling through an unread HTTP request body. PHP does not discard the unread part of an HTTP request… |
| 2026-11-19 15:17:27 | [CVE-2026-129291](https://nvd.nist.gov/vuln/detail/CVE-2026-129291) | High | 8.8 | PHP-FPM epoll use-after-free can lead to local privilege escalation. When catch_workers_output is enabled and the epoll… |
| 2026-11-19 15:17:27 | [CVE-2026-129292](https://nvd.nist.gov/vuln/detail/CVE-2026-129292) | Medium | 5.3 | PHP-FPM status endpoint XSS via unescaped user and script fields. The PHP-FPM full status output includes the request m… |
| 2026-11-19 15:17:27 | [CVE-2026-129438](https://nvd.nist.gov/vuln/detail/CVE-2026-129438) | Medium | 6.3 | Incorrect RFC 3986 URI serialization for oversized input. The Uri\Rfc3986\Uri class does not correctly handle the outpu… |
| 2026-11-19 15:17:28 | [CVE-2026-129474](https://nvd.nist.gov/vuln/detail/CVE-2026-129474) | Critical | 9.2 | Use-after-free in magic method backtraces can lead to remote code execution. When collecting the arguments of a method… |
| 2026-11-19 15:17:28 | [CVE-2026-129481](https://nvd.nist.gov/vuln/detail/CVE-2026-129481) | Critical | 9.2 | Use-after-free after interrupted session shutdown. The session extension records the filename of the executing script w… |
| 2026-11-19 15:17:28 | [CVE-2026-129496](https://nvd.nist.gov/vuln/detail/CVE-2026-129496) | Critical | 9.2 | Timezone cache use-after-free can lead to remote code execution. In non-thread-safe builds, a diagnostic written to a f… |
| 2026-11-19 15:17:28 | [CVE-2026-129501](https://nvd.nist.gov/vuln/detail/CVE-2026-129501) | Medium | 6.3 | Double free during DOM XML serialization. The XML serializer of Dom\XMLDocument and Dom\HTMLDocument can share ownershi… |
| 2026-11-19 15:17:28 | [CVE-2026-129506](https://nvd.nist.gov/vuln/detail/CVE-2026-129506) | Medium | 6.3 | SOAP use-after-free when processing DTD entity references. The SOAP extension frees the document type definition (DTD)… |
| 2026-11-19 15:17:28 | [CVE-2026-129538](https://nvd.nist.gov/vuln/detail/CVE-2026-129538) | Medium | 6.9 | PHP-CGI out-of-bounds read and write during PATH_INFO correction. The PHP CGI binary (php-cgi), in CGI and FastCGI mode… |
| 2026-11-19 15:17:28 | [CVE-2026-129699](https://nvd.nist.gov/vuln/detail/CVE-2026-129699) | High | 7.1 | In Eclipse Ditto versions 2.0.0 to 3.8.14 and 3.9.0 to 3.9.8, the authorization check for JSON merge patch commands on… |
| 2026-11-19 15:17:29 | [CVE-2026-129700](https://nvd.nist.gov/vuln/detail/CVE-2026-129700) | High | 7.1 | In Eclipse Ditto versions 2.4.0 to 3.9.8, Thing fields a requester is not allowed to read can be disclosed through the… |
| 2026-11-19 15:17:29 | [CVE-2026-129702](https://nvd.nist.gov/vuln/detail/CVE-2026-129702) | Low | 2.3 | In Eclipse Ditto versions before 3.8.15 and 3.9.0 to 3.9.8, the policy enforcers do not let a revoke win over a grant i… |
| 2026-11-19 15:17:29 | [CVE-2026-129916](https://nvd.nist.gov/vuln/detail/CVE-2026-129916) | Low | 2.3 | In Eclipse Ditto versions 3.9.0 to 3.9.8, the resolved policy view (`GET /api/2/policies/{policyId}?policy-view=resolve… |
| 2026-11-19 15:17:32 | [CVE-2026-132039](https://nvd.nist.gov/vuln/detail/CVE-2026-132039) | High | 7.1 | In Eclipse Ditto versions before 3.9.9, Thing events delivered via WebSocket, Server-Sent Events and connections disclo… |
| 2026-11-19 15:17:35 | [CVE-2026-133161](https://nvd.nist.gov/vuln/detail/CVE-2026-133161) | High | 7.5 | ### Summary ui With `strip_ansi=True`, Pydantic AI Harness's `ToolOutputLimits` capability removes ANSI escape sequence… |
| 2026-11-19 15:17:36 | [CVE-2026-133167](https://nvd.nist.gov/vuln/detail/CVE-2026-133167) | Medium | 6.8 | OFFIS DCMTK 3.5.4 through 3.7.1 contains an integer overflow in DJCodecEncoder::encodeTrueLossless size checks that all… |
| 2026-11-19 15:17:36 | [CVE-2026-133168](https://nvd.nist.gov/vuln/detail/CVE-2026-133168) | High | 8.5 | OFFIS DCMTK 3.7.1 contains a heap buffer overflow vulnerability in togglePlanarConfiguration8 and togglePlanarConfigura… |
| 2026-11-19 15:17:36 | [CVE-2026-133169](https://nvd.nist.gov/vuln/detail/CVE-2026-133169) | Medium | 4.8 | modified eCommerce Shopsoftware through 3.3.0 contains a stored cross-site scripting vulnerability that allows authenti… |
| 2026-11-19 15:17:36 | [CVE-2026-133170](https://nvd.nist.gov/vuln/detail/CVE-2026-133170) | Low | 2.3 | Tiptap @tiptap/core 2.0.0-alpha.0 before 3.30.4 contains a cross-site scripting vulnerability that allows attackers to… |
| 2026-11-19 15:17:37 | [CVE-2026-133171](https://nvd.nist.gov/vuln/detail/CVE-2026-133171) | Medium | 6.9 | Tiptap @tiptap/core 3.7.0 before 3.30.5 contains a regular expression denial of service vulnerability in parseAttribute… |
| 2026-11-19 15:17:37 | [CVE-2026-133172](https://nvd.nist.gov/vuln/detail/CVE-2026-133172) | High | 8.7 | Cozy Cloud cozy-stack 1.6.62 before 1.6.69 contains an authorization bypass vulnerability in the shared-drive move hand… |
| 2026-11-19 15:17:37 | [CVE-2026-133173](https://nvd.nist.gov/vuln/detail/CVE-2026-133173) | High | 7.1 | WatchAlert 2.0.0 through 3.9.20 contains an insecure direct object reference vulnerability in the /api/w8t/datasource/d… |
| 2026-11-19 15:17:37 | [CVE-2026-133174](https://nvd.nist.gov/vuln/detail/CVE-2026-133174) | Medium | 5.3 | HotGo 2.18.6 through 2.19.0 contains an information disclosure vulnerability that allows authenticated backend users to… |
| 2026-11-19 15:17:37 | [CVE-2026-133175](https://nvd.nist.gov/vuln/detail/CVE-2026-133175) | Medium | 6.9 | MISP contains an authorization bypass in its server-to-server proposal synchronization mechanism. Two related flaws wer… |
| 2026-11-19 15:17:37 | [CVE-2026-133177](https://nvd.nist.gov/vuln/detail/CVE-2026-133177) | Medium | 5.3 | MISP contains an authorization flaw in the sharing group capture logic. When a sharing group is re-captured with a newe… |
| 2026-11-19 15:17:38 | [CVE-2026-133178](https://nvd.nist.gov/vuln/detail/CVE-2026-133178) | Medium | 4.8 | flowintel allows users with editor-level access to author case and task fields, including aggregated tags. When these r… |
| 2026-11-19 15:17:38 | [CVE-2026-133179](https://nvd.nist.gov/vuln/detail/CVE-2026-133179) | Low | 3.6 | In JetBrains Rider before 2026.3 code execution was possible via MSBuild configuration files in parent directories |
| 2026-11-19 15:17:38 | [CVE-2026-133180](https://nvd.nist.gov/vuln/detail/CVE-2026-133180) | Low | 3.7 | In JetBrains ReSharper before 2026.3 the What's New feature did not verify server certificates |
| 2026-11-19 15:17:38 | [CVE-2026-133181](https://nvd.nist.gov/vuln/detail/CVE-2026-133181) | Low | 3.7 | In JetBrains ReSharper before 2026.3 server host names were not verified during certificate validation |
| 2026-11-19 15:17:38 | [CVE-2026-133182](https://nvd.nist.gov/vuln/detail/CVE-2026-133182) | Medium | 5.5 | In JetBrains IntelliJ IDEA before 2026.3 the GitHub plugin exposed GitHub access tokens via its public API |
| 2026-11-19 15:17:39 | [CVE-2026-133183](https://nvd.nist.gov/vuln/detail/CVE-2026-133183) | Medium | 5.3 | MISP contains an authorization flaw in the handling of remote pull and feed operations. When a non-internal pull or a f… |
| 2026-11-19 15:17:39 | [CVE-2026-133184](https://nvd.nist.gov/vuln/detail/CVE-2026-133184) | Medium | 5.3 | MISP contains an authorization and input-validation flaw in its event push mechanism. When a user with push permissions… |
| 2026-11-19 15:17:39 | [CVE-2026-133185](https://nvd.nist.gov/vuln/detail/CVE-2026-133185) | Critical | 9.1 | Goproxy before 1.9.4 contains a weak key generation vulnerability in NewCounterEncryptorRandFromKey that derives RSA an… |
| 2026-11-19 15:17:39 | [CVE-2026-133188](https://nvd.nist.gov/vuln/detail/CVE-2026-133188) | Medium | 6.9 | MISP contains a vulnerability in the cryptographic signature verification of protected events. When a MISP instance sig… |
| 2026-11-19 15:17:39 | [CVE-2026-133190](https://nvd.nist.gov/vuln/detail/CVE-2026-133190) | Medium | 6.3 | MISP, a threat intelligence sharing platform, contains a vulnerability in its cryptographic key management for protecte… |
| 2026-11-19 15:17:40 | [CVE-2026-133192](https://nvd.nist.gov/vuln/detail/CVE-2026-133192) | Medium | 4.2 | In JetBrains Junie GitHub Action before 1.10.0 untrusted fork code could be processed in privileged workflow runs |
| 2026-11-19 15:17:40 | [CVE-2026-133193](https://nvd.nist.gov/vuln/detail/CVE-2026-133193) | Medium | 5.6 | In JetBrains Junie GitHub Action before 1.10.0 code execution was possible via path traversal in feedback session marke… |
| 2026-11-19 15:17:40 | [CVE-2026-133194](https://nvd.nist.gov/vuln/detail/CVE-2026-133194) | Medium | 5.6 | In JetBrains Junie GitHub Action before 1.10.0 command injection was possible via the action version input |
| 2026-11-19 15:17:40 | [CVE-2026-133195](https://nvd.nist.gov/vuln/detail/CVE-2026-133195) | High | 7.5 | In JetBrains Junie CLI before 26.6.29 files outside the project directory could be modified by agent file tools |
| 2026-11-19 15:17:40 | [CVE-2026-133196](https://nvd.nist.gov/vuln/detail/CVE-2026-133196) | Medium | 5.3 | In JetBrains Junie CLI before 26.11.1 files outside the project could be overwritten via shell output redirection |
| 2026-11-19 15:17:40 | [CVE-2026-133197](https://nvd.nist.gov/vuln/detail/CVE-2026-133197) | Medium | 5.0 | In JetBrains Junie CLI before 26.9.22 command injection was possible via file names in code review |
| 2026-11-19 15:17:40 | [CVE-2026-133198](https://nvd.nist.gov/vuln/detail/CVE-2026-133198) | High | 7.8 | In JetBrains Junie before 252.819.35, 253.819.35 code execution was possible via terminal environment settings in proje… |
| 2026-11-19 15:17:41 | [CVE-2026-15353](https://nvd.nist.gov/vuln/detail/CVE-2026-15353) | Medium | 6.3 | SOAP information disclosure through malformed array dimensions. The SOAP extension reads an uninitialized array positio… |
| 2026-11-19 15:17:42 | [CVE-2026-87867](https://nvd.nist.gov/vuln/detail/CVE-2026-87867) | High | 7.1 | MRemoteNG establishes encrypted but unauthenticated channel with Microsoft SQL Server backend. Client accepts any certi… |
| 2026-11-19 15:17:42 | [CVE-2026-87868](https://nvd.nist.gov/vuln/detail/CVE-2026-87868) | High | 8.2 | MRemoteNG uses single MD5 hash with no salt and no iterations for key-derivation. An attacker who obtains the encrypted… |
| 2026-11-19 15:17:42 | [CVE-2026-99321](https://nvd.nist.gov/vuln/detail/CVE-2026-99321) |  |  | In the Linux kernel, the following vulnerability has been resolved: rust_binder: wake epoll on self-work queued to poll… |
| 2026-11-19 15:17:42 | [CVE-2026-99322](https://nvd.nist.gov/vuln/detail/CVE-2026-99322) |  |  | In the Linux kernel, the following vulnerability has been resolved: ksmbd: rebind completed CREATE replays without drai… |
| 2026-11-19 15:17:43 | [CVE-2026-99323](https://nvd.nist.gov/vuln/detail/CVE-2026-99323) |  |  | In the Linux kernel, the following vulnerability has been resolved: ksmbd: fix invalid pointer dereference when get_ino… |
| 2026-11-19 15:17:43 | [CVE-2026-99324](https://nvd.nist.gov/vuln/detail/CVE-2026-99324) |  |  | In the Linux kernel, the following vulnerability has been resolved: ksmbd: fix out-of-bounds read when padding the fina… |
| 2026-11-19 15:17:43 | [CVE-2026-99325](https://nvd.nist.gov/vuln/detail/CVE-2026-99325) |  |  | In the Linux kernel, the following vulnerability has been resolved: HID: hid-lenovo-go-s: Add suspend function and gate… |
| 2026-11-19 15:17:43 | [CVE-2026-99326](https://nvd.nist.gov/vuln/detail/CVE-2026-99326) |  |  | In the Linux kernel, the following vulnerability has been resolved: HID: hid-lenovo-go-s: Prevent deadlock if device re… |
| 2026-11-19 15:17:43 | [CVE-2026-99327](https://nvd.nist.gov/vuln/detail/CVE-2026-99327) |  |  | In the Linux kernel, the following vulnerability has been resolved: HID: roccat: kovaplus: reject short button reports… |
| 2026-11-19 15:17:43 | [CVE-2026-99328](https://nvd.nist.gov/vuln/detail/CVE-2026-99328) |  |  | In the Linux kernel, the following vulnerability has been resolved: HID: picoLCD: check for fb_deferred_io_init() error… |
| 2026-11-19 15:17:43 | [CVE-2026-99329](https://nvd.nist.gov/vuln/detail/CVE-2026-99329) |  |  | In the Linux kernel, the following vulnerability has been resolved: HID: mcp2221: always initialize and cancel init_wor… |
| 2026-11-19 15:17:43 | [CVE-2026-99330](https://nvd.nist.gov/vuln/detail/CVE-2026-99330) |  |  | In the Linux kernel, the following vulnerability has been resolved: HID: mcp2200: validate READ_ALL response length The… |
| 2026-11-19 15:17:43 | [CVE-2026-99331](https://nvd.nist.gov/vuln/detail/CVE-2026-99331) |  |  | In the Linux kernel, the following vulnerability has been resolved: HID: cp2112: validate response report lengths The H… |
| 2026-11-19 15:17:44 | [CVE-2026-99332](https://nvd.nist.gov/vuln/detail/CVE-2026-99332) |  |  | In the Linux kernel, the following vulnerability has been resolved: HID: core: Fix out-of-bounds left shift by 32 in s3… |
| 2026-11-19 15:17:44 | [CVE-2026-99333](https://nvd.nist.gov/vuln/detail/CVE-2026-99333) |  |  | In the Linux kernel, the following vulnerability has been resolved: HID: amd_sfh: Use report type from request node Use… |
| 2026-11-19 15:17:44 | [CVE-2026-99334](https://nvd.nist.gov/vuln/detail/CVE-2026-99334) |  |  | In the Linux kernel, the following vulnerability has been resolved: KVM: PPC: Book3S HV: Add preempt_disable() around v… |
| 2026-11-19 15:17:44 | [CVE-2026-99335](https://nvd.nist.gov/vuln/detail/CVE-2026-99335) |  |  | In the Linux kernel, the following vulnerability has been resolved: KVM: guest_memfd: Establish memslot<=>guest_memfd b… |
| 2026-11-19 15:17:44 | [CVE-2026-99336](https://nvd.nist.gov/vuln/detail/CVE-2026-99336) |  |  | In the Linux kernel, the following vulnerability has been resolved: KVM: guest_memfd: take the invalidate lock when unb… |
| 2026-11-19 15:17:44 | [CVE-2026-99337](https://nvd.nist.gov/vuln/detail/CVE-2026-99337) |  |  | In the Linux kernel, the following vulnerability has been resolved: KVM: TDX: Enable Bus Lock VM exit Enable Bus Lock V… |
| 2026-11-19 15:17:44 | [CVE-2026-99338](https://nvd.nist.gov/vuln/detail/CVE-2026-99338) |  |  | In the Linux kernel, the following vulnerability has been resolved: KVM: TDX: Enable Notify VM exit Enable Notify VM ex… |
| 2026-11-19 15:17:44 | [CVE-2026-99339](https://nvd.nist.gov/vuln/detail/CVE-2026-99339) |  |  | In the Linux kernel, the following vulnerability has been resolved: KVM: x86: Zero reserved synic flags when delivering… |
| 2026-11-19 15:17:45 | [CVE-2026-99340](https://nvd.nist.gov/vuln/detail/CVE-2026-99340) |  |  | In the Linux kernel, the following vulnerability has been resolved: KVM: x86: Take SRCU in kvm_zap_gfn_range() kvm_zap_… |
| 2026-11-19 15:17:45 | [CVE-2026-99341](https://nvd.nist.gov/vuln/detail/CVE-2026-99341) |  |  | In the Linux kernel, the following vulnerability has been resolved: KVM: x86: Request event processing for exception VM… |
| 2026-11-19 15:17:45 | [CVE-2026-99342](https://nvd.nist.gov/vuln/detail/CVE-2026-99342) |  |  | In the Linux kernel, the following vulnerability has been resolved: KVM: x86/xen: Enforce 4-byte alignment of vcpu_info… |
| 2026-11-19 15:17:45 | [CVE-2026-99343](https://nvd.nist.gov/vuln/detail/CVE-2026-99343) |  |  | In the Linux kernel, the following vulnerability has been resolved: KVM: x86/mmu: Bug the VM if KVM attempts to walk mo… |
| 2026-11-19 15:17:45 | [CVE-2026-99344](https://nvd.nist.gov/vuln/detail/CVE-2026-99344) |  |  | In the Linux kernel, the following vulnerability has been resolved: KVM: nSVM: Ignore EFER.LMA if EFER.LME=0 when prepa… |
| 2026-11-19 15:17:45 | [CVE-2026-99345](https://nvd.nist.gov/vuln/detail/CVE-2026-99345) |  |  | In the Linux kernel, the following vulnerability has been resolved: KVM: nSVM: Reject KVM_SET_NESTED_STATE if L1 has EF… |
| 2026-11-19 15:17:45 | [CVE-2026-99346](https://nvd.nist.gov/vuln/detail/CVE-2026-99346) |  |  | In the Linux kernel, the following vulnerability has been resolved: KVM: SVM: Trigger new ASID allocation in both VMCBs… |
| 2026-11-19 15:17:45 | [CVE-2026-99347](https://nvd.nist.gov/vuln/detail/CVE-2026-99347) |  |  | In the Linux kernel, the following vulnerability has been resolved: ALSA: x86: hdmi: fix chmap array missing terminator… |
| 2026-11-19 15:17:46 | [CVE-2026-99348](https://nvd.nist.gov/vuln/detail/CVE-2026-99348) |  |  | In the Linux kernel, the following vulnerability has been resolved: afs: Fix afs to abort the rxrpc call on send error… |
| 2026-11-19 15:17:46 | [CVE-2026-99349](https://nvd.nist.gov/vuln/detail/CVE-2026-99349) |  |  | In the Linux kernel, the following vulnerability has been resolved: rxrpc: Fix lack of short-send handling in rxrpc_ker… |
| 2026-11-19 15:17:46 | [CVE-2026-99350](https://nvd.nist.gov/vuln/detail/CVE-2026-99350) |  |  | In the Linux kernel, the following vulnerability has been resolved: rxrpc: Fix update of call->tx_pending without holdi… |
| 2026-11-19 15:17:46 | [CVE-2026-99351](https://nvd.nist.gov/vuln/detail/CVE-2026-99351) |  |  | In the Linux kernel, the following vulnerability has been resolved: sunrpc: treat empty auth.unix.gid replies as negati… |
| 2026-11-19 15:17:46 | [CVE-2026-99352](https://nvd.nist.gov/vuln/detail/CVE-2026-99352) |  |  | In the Linux kernel, the following vulnerability has been resolved: SUNRPC: trace an accepted transport before publishi… |
| 2026-11-19 15:17:46 | [CVE-2026-99353](https://nvd.nist.gov/vuln/detail/CVE-2026-99353) |  |  | In the Linux kernel, the following vulnerability has been resolved: SUNRPC: Reject a socket that already has an svc_soc… |
| 2026-11-19 15:17:46 | [CVE-2026-99354](https://nvd.nist.gov/vuln/detail/CVE-2026-99354) |  |  | In the Linux kernel, the following vulnerability has been resolved: sunrpc: pin gss module across auth_domain RCU free… |
| 2026-11-19 15:17:46 | [CVE-2026-99355](https://nvd.nist.gov/vuln/detail/CVE-2026-99355) |  |  | In the Linux kernel, the following vulnerability has been resolved: SUNRPC: fix oversized GSS proxy token copy gss_read… |
| 2026-11-19 15:17:47 | [CVE-2026-99356](https://nvd.nist.gov/vuln/detail/CVE-2026-99356) |  |  | In the Linux kernel, the following vulnerability has been resolved: SUNRPC: Do not credit control-record octets to the… |
| 2026-11-19 15:17:47 | [CVE-2026-99357](https://nvd.nist.gov/vuln/detail/CVE-2026-99357) |  |  | In the Linux kernel, the following vulnerability has been resolved: SUNRPC: Copy the deferred RPC Call from the head bu… |
| 2026-11-19 15:17:47 | [CVE-2026-99358](https://nvd.nist.gov/vuln/detail/CVE-2026-99358) |  |  | In the Linux kernel, the following vulnerability has been resolved: nfsd: zero NFSv4 COMPOUND tag padding nfs4svc_encod… |
| 2026-11-19 15:17:47 | [CVE-2026-99359](https://nvd.nist.gov/vuln/detail/CVE-2026-99359) |  |  | In the Linux kernel, the following vulnerability has been resolved: NFSD: validate transport name in listener_set befor… |
| 2026-11-19 15:17:47 | [CVE-2026-99360](https://nvd.nist.gov/vuln/detail/CVE-2026-99360) |  |  | In the Linux kernel, the following vulnerability has been resolved: NFSD: Set nn->cld_net before registering the cld pi… |
| 2026-11-19 15:17:47 | [CVE-2026-99361](https://nvd.nist.gov/vuln/detail/CVE-2026-99361) |  |  | In the Linux kernel, the following vulnerability has been resolved: nfsd: propagate SETXATTR value decode errors nfsd4_… |
| 2026-11-19 15:17:47 | [CVE-2026-99362](https://nvd.nist.gov/vuln/detail/CVE-2026-99362) |  |  | In the Linux kernel, the following vulnerability has been resolved: nfsd: preflight SEQUENCE replies before accepting a… |
| 2026-11-19 15:17:47 | [CVE-2026-99363](https://nvd.nist.gov/vuln/detail/CVE-2026-99363) |  |  | In the Linux kernel, the following vulnerability has been resolved: NFSD: Map flex file layout IDs through the request'… |
| 2026-11-19 15:17:48 | [CVE-2026-99364](https://nvd.nist.gov/vuln/detail/CVE-2026-99364) |  |  | In the Linux kernel, the following vulnerability has been resolved: NFSD: Fix out-of-bounds read in the rpc_status dump… |
| 2026-11-19 15:17:48 | [CVE-2026-99365](https://nvd.nist.gov/vuln/detail/CVE-2026-99365) |  |  | In the Linux kernel, the following vulnerability has been resolved: nfsd: Fix id-to-name cache entry leak in idtoname_p… |
| 2026-11-19 15:17:48 | [CVE-2026-99366](https://nvd.nist.gov/vuln/detail/CVE-2026-99366) |  |  | In the Linux kernel, the following vulnerability has been resolved: nfsd: don't modify a session slot when replaying it… |
| 2026-11-19 15:17:48 | [CVE-2026-99367](https://nvd.nist.gov/vuln/detail/CVE-2026-99367) |  |  | In the Linux kernel, the following vulnerability has been resolved: NFSD: Don't complete a cld upcall the daemon has no… |
| 2026-11-19 15:17:48 | [CVE-2026-99368](https://nvd.nist.gov/vuln/detail/CVE-2026-99368) |  |  | In the Linux kernel, the following vulnerability has been resolved: NFSD: Do not send CB_RECALL_ANY to NFSv4.0 clients… |
| 2026-11-19 15:17:48 | [CVE-2026-99369](https://nvd.nist.gov/vuln/detail/CVE-2026-99369) |  |  | In the Linux kernel, the following vulnerability has been resolved: NFSD: Destroy a recalled delegation the client does… |
| 2026-11-19 15:17:48 | [CVE-2026-99370](https://nvd.nist.gov/vuln/detail/CVE-2026-99370) |  |  | In the Linux kernel, the following vulnerability has been resolved: NFSD: copy SETXATTR data from all XDR buffer segmen… |
| 2026-11-19 15:17:48 | [CVE-2026-99371](https://nvd.nist.gov/vuln/detail/CVE-2026-99371) |  |  | In the Linux kernel, the following vulnerability has been resolved: nfsd: clear XDR padding in GETXATTR replies nfsd4_v… |
| 2026-11-19 15:17:49 | [CVE-2026-99372](https://nvd.nist.gov/vuln/detail/CVE-2026-99372) |  |  | In the Linux kernel, the following vulnerability has been resolved: NFSD: cap the number of listeners accepted in liste… |
| 2026-11-19 15:17:49 | [CVE-2026-99373](https://nvd.nist.gov/vuln/detail/CVE-2026-99373) |  |  | In the Linux kernel, the following vulnerability has been resolved: NFS/localio: detect a short read or write before th… |
| 2026-11-19 15:17:49 | [CVE-2026-99374](https://nvd.nist.gov/vuln/detail/CVE-2026-99374) |  |  | In the Linux kernel, the following vulnerability has been resolved: NFSv4/flexfiles: Use the full 64-bit stripe_unit ff… |
| 2026-11-19 15:17:49 | [CVE-2026-99375](https://nvd.nist.gov/vuln/detail/CVE-2026-99375) |  |  | In the Linux kernel, the following vulnerability has been resolved: NFSv4/flexfiles: fail I/O to the data server once a… |
| 2026-11-19 15:17:49 | [CVE-2026-99376](https://nvd.nist.gov/vuln/detail/CVE-2026-99376) |  |  | In the Linux kernel, the following vulnerability has been resolved: NFSv4/pnfs: Free the netid when draining a data-ser… |
| 2026-11-19 15:17:49 | [CVE-2026-99377](https://nvd.nist.gov/vuln/detail/CVE-2026-99377) |  |  | In the Linux kernel, the following vulnerability has been resolved: NFSv4/pnfs: bound the CB_NOTIFY_DEVICEID array coun… |
| 2026-11-19 15:17:49 | [CVE-2026-99378](https://nvd.nist.gov/vuln/detail/CVE-2026-99378) |  |  | In the Linux kernel, the following vulnerability has been resolved: pnfs/blocklayout: Complete a device upcall when the… |
| 2026-11-19 15:17:49 | [CVE-2026-99379](https://nvd.nist.gov/vuln/detail/CVE-2026-99379) |  |  | In the Linux kernel, the following vulnerability has been resolved: smb: client: validate SMB1 EA list bounds before pa… |
| 2026-11-19 15:17:50 | [CVE-2026-99380](https://nvd.nist.gov/vuln/detail/CVE-2026-99380) |  |  | In the Linux kernel, the following vulnerability has been resolved: smb: client: validate NT transaction response layou… |
| 2026-11-19 15:17:50 | [CVE-2026-99381](https://nvd.nist.gov/vuln/detail/CVE-2026-99381) |  |  | In the Linux kernel, the following vulnerability has been resolved: smb: client: reject short or out-of-range FIND resp… |
| 2026-11-19 15:17:50 | [CVE-2026-99382](https://nvd.nist.gov/vuln/detail/CVE-2026-99382) |  |  | In the Linux kernel, the following vulnerability has been resolved: smb: client: reject FIND data areas that run past t… |
| 2026-11-19 15:17:50 | [CVE-2026-99383](https://nvd.nist.gov/vuln/detail/CVE-2026-99383) |  |  | In the Linux kernel, the following vulnerability has been resolved: smb: client: reclaim credits for decrypted reads wi… |
| 2026-11-19 15:17:50 | [CVE-2026-99384](https://nvd.nist.gov/vuln/detail/CVE-2026-99384) |  |  | In the Linux kernel, the following vulnerability has been resolved: smb: client: fix OOB read of the resume name sent i… |
| 2026-11-19 15:17:50 | [CVE-2026-99385](https://nvd.nist.gov/vuln/detail/CVE-2026-99385) |  |  | In the Linux kernel, the following vulnerability has been resolved: smb: client: fix buffer overflow in SMB2_tcon() In… |
| 2026-11-19 15:17:50 | [CVE-2026-99386](https://nvd.nist.gov/vuln/detail/CVE-2026-99386) |  |  | In the Linux kernel, the following vulnerability has been resolved: smb: client: don't resurrect an exiting tcon from c… |
| 2026-11-19 15:17:50 | [CVE-2026-99387](https://nvd.nist.gov/vuln/detail/CVE-2026-99387) |  |  | In the Linux kernel, the following vulnerability has been resolved: smb: client: bound POSIX lock data area by response… |
| 2026-11-19 15:17:51 | [CVE-2026-99388](https://nvd.nist.gov/vuln/detail/CVE-2026-99388) |  |  | In the Linux kernel, the following vulnerability has been resolved: smb: smbdirect: fix buffer length underflow in RDMA… |
| 2026-11-19 15:17:51 | [CVE-2026-99389](https://nvd.nist.gov/vuln/detail/CVE-2026-99389) |  |  | In the Linux kernel, the following vulnerability has been resolved: smb: server: size directory name conversion buffer… |
| 2026-11-19 15:17:51 | [CVE-2026-99390](https://nvd.nist.gov/vuln/detail/CVE-2026-99390) |  |  | In the Linux kernel, the following vulnerability has been resolved: xfs: fix correction of unwritten extents in quota f… |
| 2026-11-19 15:17:51 | [CVE-2026-99391](https://nvd.nist.gov/vuln/detail/CVE-2026-99391) |  |  | In the Linux kernel, the following vulnerability has been resolved: xfs: don't try to scrub self-referential dirent in… |
| 2026-11-19 15:17:51 | [CVE-2026-99392](https://nvd.nist.gov/vuln/detail/CVE-2026-99392) |  |  | In the Linux kernel, the following vulnerability has been resolved: xfs: don't subtract excess usage twice when computi… |
| 2026-11-19 15:17:51 | [CVE-2026-99393](https://nvd.nist.gov/vuln/detail/CVE-2026-99393) |  |  | In the Linux kernel, the following vulnerability has been resolved: xfs: don't overrun incore inode when cleaning attr… |
| 2026-11-19 15:17:51 | [CVE-2026-99394](https://nvd.nist.gov/vuln/detail/CVE-2026-99394) |  |  | In the Linux kernel, the following vulnerability has been resolved: xfs: complain loudly when dirtree checker finds bro… |
| 2026-11-19 15:17:51 | [CVE-2026-99395](https://nvd.nist.gov/vuln/detail/CVE-2026-99395) |  |  | In the Linux kernel, the following vulnerability has been resolved: xfs: bound inode fork length against the fork size… |
| 2026-11-19 15:17:52 | [CVE-2026-99396](https://nvd.nist.gov/vuln/detail/CVE-2026-99396) |  |  | In the Linux kernel, the following vulnerability has been resolved: xfs: bound da-node entry count against the correct… |
| 2026-11-19 15:17:52 | [CVE-2026-99397](https://nvd.nist.gov/vuln/detail/CVE-2026-99397) |  |  | In the Linux kernel, the following vulnerability has been resolved: xfs: always report inode repair setup failures LOLL… |
| 2026-11-19 15:17:52 | [CVE-2026-99398](https://nvd.nist.gov/vuln/detail/CVE-2026-99398) |  |  | In the Linux kernel, the following vulnerability has been resolved: xfs: always forget cached ACLs if the attr fork swa… |
| 2026-11-19 15:17:52 | [CVE-2026-99399](https://nvd.nist.gov/vuln/detail/CVE-2026-99399) |  |  | In the Linux kernel, the following vulnerability has been resolved: xfs: reject remote xattr entries with an out-of-ran… |
| 2026-11-19 15:17:52 | [CVE-2026-99400](https://nvd.nist.gov/vuln/detail/CVE-2026-99400) |  |  | In the Linux kernel, the following vulnerability has been resolved: xfs: reject out-of-range attribute value lengths in… |
| 2026-11-19 15:17:52 | [CVE-2026-99401](https://nvd.nist.gov/vuln/detail/CVE-2026-99401) |  |  | In the Linux kernel, the following vulnerability has been resolved: rtnetlink: wait for RCU readers in rtnl_link_unregi… |
| 2026-11-19 15:17:52 | [CVE-2026-99402](https://nvd.nist.gov/vuln/detail/CVE-2026-99402) |  |  | In the Linux kernel, the following vulnerability has been resolved: netfilter: nft_payload: restrict checksum offsets t… |
| 2026-11-19 15:17:52 | [CVE-2026-99403](https://nvd.nist.gov/vuln/detail/CVE-2026-99403) |  |  | In the Linux kernel, the following vulnerability has been resolved: xfs: mark overfull dabtree node blocks as corrupt L… |
| 2026-11-19 15:17:52 | [CVE-2026-99404](https://nvd.nist.gov/vuln/detail/CVE-2026-99404) |  |  | In the Linux kernel, the following vulnerability has been resolved: xfs: check fork type against dabtree block magic nu… |
| 2026-11-19 15:17:53 | [CVE-2026-99405](https://nvd.nist.gov/vuln/detail/CVE-2026-99405) |  |  | In the Linux kernel, the following vulnerability has been resolved: xfs: abort dirtree repair if the live update hook d… |
| 2026-11-19 15:17:53 | [CVE-2026-99406](https://nvd.nist.gov/vuln/detail/CVE-2026-99406) |  |  | In the Linux kernel, the following vulnerability has been resolved: xfs: fix lost errno returned from xfarray_foliosort… |
| 2026-11-19 15:17:53 | [CVE-2026-99407](https://nvd.nist.gov/vuln/detail/CVE-2026-99407) |  |  | In the Linux kernel, the following vulnerability has been resolved: xfs: don't repair fs summary counters with garbage… |
| 2026-11-19 15:17:53 | [CVE-2026-99408](https://nvd.nist.gov/vuln/detail/CVE-2026-99408) |  |  | In the Linux kernel, the following vulnerability has been resolved: xfs: don't proceed with xattr repair if the live up… |
| 2026-11-19 15:17:53 | [CVE-2026-99409](https://nvd.nist.gov/vuln/detail/CVE-2026-99409) |  |  | In the Linux kernel, the following vulnerability has been resolved: xfs: don't fix the directory tree if live update fa… |
| 2026-11-19 15:17:53 | [CVE-2026-99410](https://nvd.nist.gov/vuln/detail/CVE-2026-99410) |  |  | In the Linux kernel, the following vulnerability has been resolved: xfs: always reset incore attr fork buffer when rese… |
| 2026-11-19 15:17:53 | [CVE-2026-99411](https://nvd.nist.gov/vuln/detail/CVE-2026-99411) |  |  | In the Linux kernel, the following vulnerability has been resolved: xfs: actually lock the metafile reservation when ad… |
| 2026-11-19 15:17:53 | [CVE-2026-99412](https://nvd.nist.gov/vuln/detail/CVE-2026-99412) |  |  | In the Linux kernel, the following vulnerability has been resolved: xfs: avoid cross-rtgroup reaping after a repair LOL… |
| 2026-11-19 15:17:53 | [CVE-2026-99413](https://nvd.nist.gov/vuln/detail/CVE-2026-99413) |  |  | In the Linux kernel, the following vulnerability has been resolved: xfs: fix buffer overruns in xfs_ioc_attr_list When… |
| 2026-11-19 15:17:54 | [CVE-2026-99414](https://nvd.nist.gov/vuln/detail/CVE-2026-99414) |  |  | In the Linux kernel, the following vulnerability has been resolved: ovl: skip copy up of empty security.capability ovl_… |
| 2026-11-19 15:17:54 | [CVE-2026-99415](https://nvd.nist.gov/vuln/detail/CVE-2026-99415) |  |  | In the Linux kernel, the following vulnerability has been resolved: ovl: set the revalidate flags after d_instantiate()… |
| 2026-11-19 15:17:54 | [CVE-2026-99416](https://nvd.nist.gov/vuln/detail/CVE-2026-99416) |  |  | In the Linux kernel, the following vulnerability has been resolved: ovl: read the nlink xattr of every indexed non-dir… |
| 2026-11-19 15:17:54 | [CVE-2026-99417](https://nvd.nist.gov/vuln/detail/CVE-2026-99417) |  |  | In the Linux kernel, the following vulnerability has been resolved: ovl: fix a torn path in ovl_get_redirect() A hard l… |
| 2026-11-19 15:17:54 | [CVE-2026-99418](https://nvd.nist.gov/vuln/detail/CVE-2026-99418) |  |  | In the Linux kernel, the following vulnerability has been resolved: ovl: do not copy up an xattr value that was never r… |
| 2026-11-19 15:17:54 | [CVE-2026-99419](https://nvd.nist.gov/vuln/detail/CVE-2026-99419) |  |  | In the Linux kernel, the following vulnerability has been resolved: ovl: do not copy up a dentry that was removed A cha… |
| 2026-11-19 15:17:54 | [CVE-2026-99420](https://nvd.nist.gov/vuln/detail/CVE-2026-99420) |  |  | In the Linux kernel, the following vulnerability has been resolved: ovl: check that the parents of volatile/dirty are d… |
| 2026-11-19 15:17:54 | [CVE-2026-99421](https://nvd.nist.gov/vuln/detail/CVE-2026-99421) |  |  | In the Linux kernel, the following vulnerability has been resolved: ovl: always encode the origin fh when index is enab… |
| 2026-11-19 15:17:55 | [CVE-2026-99422](https://nvd.nist.gov/vuln/detail/CVE-2026-99422) |  |  | In the Linux kernel, the following vulnerability has been resolved: ovl: use the pinned upper dir in ovl_fix_origin() R… |
| 2026-11-19 15:17:55 | [CVE-2026-99423](https://nvd.nist.gov/vuln/detail/CVE-2026-99423) |  |  | In the Linux kernel, the following vulnerability has been resolved: ovl: take a snapshot of the name for copy up The co… |
| 2026-11-19 15:17:55 | [CVE-2026-99424](https://nvd.nist.gov/vuln/detail/CVE-2026-99424) |  |  | In the Linux kernel, the following vulnerability has been resolved: ovl: set OVL_WHITEOUTS before publishing the upper… |
| 2026-11-19 15:17:55 | [CVE-2026-99425](https://nvd.nist.gov/vuln/detail/CVE-2026-99425) |  |  | In the Linux kernel, the following vulnerability has been resolved: ovl: hold a reference on the parent in readdir List… |
| 2026-11-19 15:17:55 | [CVE-2026-99426](https://nvd.nist.gov/vuln/detail/CVE-2026-99426) |  |  | In the Linux kernel, the following vulnerability has been resolved: smb: client: hold server info until cifsd exits The… |
| 2026-11-19 15:17:55 | [CVE-2026-99427](https://nvd.nist.gov/vuln/detail/CVE-2026-99427) |  |  | In the Linux kernel, the following vulnerability has been resolved: smb: client: fix OOB last_entry pointer from unboun… |
| 2026-11-19 15:17:55 | [CVE-2026-99428](https://nvd.nist.gov/vuln/detail/CVE-2026-99428) |  |  | In the Linux kernel, the following vulnerability has been resolved: ocfs2: snapshot dentry names in file and setattr tr… |
| 2026-11-19 15:17:56 | [CVE-2026-99429](https://nvd.nist.gov/vuln/detail/CVE-2026-99429) |  |  | In the Linux kernel, the following vulnerability has been resolved: ocfs2: pin refcount trees before dropping the looku… |
| 2026-11-19 15:17:56 | [CVE-2026-99430](https://nvd.nist.gov/vuln/detail/CVE-2026-99430) |  |  | In the Linux kernel, the following vulnerability has been resolved: ocfs2: fix chunk number of the first chunk in a loc… |
| 2026-11-19 15:17:56 | [CVE-2026-99431](https://nvd.nist.gov/vuln/detail/CVE-2026-99431) |  |  | In the Linux kernel, the following vulnerability has been resolved: ocfs2: cancel quota sync work before freeing quota… |
| 2026-11-19 15:17:56 | [CVE-2026-99432](https://nvd.nist.gov/vuln/detail/CVE-2026-99432) |  |  | In the Linux kernel, the following vulnerability has been resolved: ocfs2/dlm: hold the lookup reference across convert… |
| 2026-11-19 15:17:56 | [CVE-2026-99433](https://nvd.nist.gov/vuln/detail/CVE-2026-99433) |  |  | In the Linux kernel, the following vulnerability has been resolved: ocfs2/dlm: hold a lock reference across grant AST e… |
| 2026-11-19 15:17:56 | [CVE-2026-99434](https://nvd.nist.gov/vuln/detail/CVE-2026-99434) |  |  | In the Linux kernel, the following vulnerability has been resolved: ocfs2/heartbeat: unlink live slots when their node… |
| 2026-11-19 15:17:56 | [CVE-2026-99435](https://nvd.nist.gov/vuln/detail/CVE-2026-99435) |  |  | In the Linux kernel, the following vulnerability has been resolved: media: rc: Fix use after free in bpf progs Since co… |
| 2026-11-19 15:17:57 | [CVE-2026-99436](https://nvd.nist.gov/vuln/detail/CVE-2026-99436) |  |  | In the Linux kernel, the following vulnerability has been resolved: media: rc: After rc_unregister_device() timers can… |
| 2026-11-19 15:17:57 | [CVE-2026-99437](https://nvd.nist.gov/vuln/detail/CVE-2026-99437) |  |  | In the Linux kernel, the following vulnerability has been resolved: media: rc: Use after free in ir_raw_event_handle()… |
| 2026-11-19 15:17:57 | [CVE-2026-99438](https://nvd.nist.gov/vuln/detail/CVE-2026-99438) |  |  | In the Linux kernel, the following vulnerability has been resolved: media: rc: mce_kbd: Fix inconsistent locking of key… |
| 2026-11-19 15:17:57 | [CVE-2026-99439](https://nvd.nist.gov/vuln/detail/CVE-2026-99439) |  |  | In the Linux kernel, the following vulnerability has been resolved: media: rc: Ensure registered is cleared in error pa… |
| 2026-11-19 15:17:57 | [CVE-2026-99440](https://nvd.nist.gov/vuln/detail/CVE-2026-99440) |  |  | In the Linux kernel, the following vulnerability has been resolved: media: rc: Ensure that rc_unregister_device() does… |
| 2026-11-19 15:17:57 | [CVE-2026-99441](https://nvd.nist.gov/vuln/detail/CVE-2026-99441) |  |  | In the Linux kernel, the following vulnerability has been resolved: nvmet-auth: serialize access to DH-HMAC-CHAP state… |
| 2026-11-19 15:17:57 | [CVE-2026-99442](https://nvd.nist.gov/vuln/detail/CVE-2026-99442) |  |  | In the Linux kernel, the following vulnerability has been resolved: nvmem: core: Fix OOB read for bit offsets of more t… |
| 2026-11-19 15:17:57 | [CVE-2026-99443](https://nvd.nist.gov/vuln/detail/CVE-2026-99443) |  |  | In the Linux kernel, the following vulnerability has been resolved: pps: generators: don't use the driver's info after… |
| 2026-11-19 15:17:58 | [CVE-2026-99444](https://nvd.nist.gov/vuln/detail/CVE-2026-99444) |  |  | In the Linux kernel, the following vulnerability has been resolved: power: supply: sbs-battery: disable polling before… |
| 2026-11-19 15:17:58 | [CVE-2026-99445](https://nvd.nist.gov/vuln/detail/CVE-2026-99445) |  |  | In the Linux kernel, the following vulnerability has been resolved: power: supply: pf1550: drain IRQ work before unregi… |
| 2026-11-19 15:17:58 | [CVE-2026-99446](https://nvd.nist.gov/vuln/detail/CVE-2026-99446) |  |  | In the Linux kernel, the following vulnerability has been resolved: phy: core: Fix race-condition between _of_phy_get()… |
| 2026-11-19 15:17:58 | [CVE-2026-99447](https://nvd.nist.gov/vuln/detail/CVE-2026-99447) |  |  | In the Linux kernel, the following vulnerability has been resolved: spi: spi-pci1xxxx: quiesce DMA engines on transfer… |
| 2026-11-19 15:17:58 | [CVE-2026-99448](https://nvd.nist.gov/vuln/detail/CVE-2026-99448) |  |  | In the Linux kernel, the following vulnerability has been resolved: ufs: use u64 for directory size in ufs_last_byte uf… |
| 2026-11-19 15:17:58 | [CVE-2026-99449](https://nvd.nist.gov/vuln/detail/CVE-2026-99449) |  |  | In the Linux kernel, the following vulnerability has been resolved: usb: gadget: fix refcount underflow in gadgetfs_bin… |
| 2026-11-19 15:17:58 | [CVE-2026-99450](https://nvd.nist.gov/vuln/detail/CVE-2026-99450) |  |  | In the Linux kernel, the following vulnerability has been resolved: vfio/nvgrace-gpu: Use a core-only open_device in fa… |
| 2026-11-19 15:17:58 | [CVE-2026-99451](https://nvd.nist.gov/vuln/detail/CVE-2026-99451) |  |  | In the Linux kernel, the following vulnerability has been resolved: wifi: mt76: mt7996: unlink TWT flow if the MCU reje… |
| 2026-11-19 15:17:59 | [CVE-2026-99452](https://nvd.nist.gov/vuln/detail/CVE-2026-99452) |  |  | In the Linux kernel, the following vulnerability has been resolved: wifi: ath9k: delete channel-context timers on deini… |
| 2026-11-19 15:17:59 | [CVE-2026-99453](https://nvd.nist.gov/vuln/detail/CVE-2026-99453) |  |  | In the Linux kernel, the following vulnerability has been resolved: xen-blkfront: unbind irq before tearing down ring a… |
| 2026-11-19 15:17:59 | [CVE-2026-99454](https://nvd.nist.gov/vuln/detail/CVE-2026-99454) |  |  | In the Linux kernel, the following vulnerability has been resolved: staging: rtl8723bs: fix protected RX frame validati… |
| 2026-11-19 15:17:59 | [CVE-2026-99455](https://nvd.nist.gov/vuln/detail/CVE-2026-99455) |  |  | In the Linux kernel, the following vulnerability has been resolved: serial: core: shut down initialized port on removal… |
| 2026-11-19 15:17:59 | [CVE-2026-99456](https://nvd.nist.gov/vuln/detail/CVE-2026-99456) |  |  | In the Linux kernel, the following vulnerability has been resolved: scsi: dc395x: sync the waiting_timer before freeing… |
| 2026-11-19 15:17:59 | [CVE-2026-99457](https://nvd.nist.gov/vuln/detail/CVE-2026-99457) |  |  | In the Linux kernel, the following vulnerability has been resolved: net: sched: prevent scheduling deactivated qdiscs T… |
| 2026-11-19 15:17:59 | [CVE-2026-99458](https://nvd.nist.gov/vuln/detail/CVE-2026-99458) |  |  | In the Linux kernel, the following vulnerability has been resolved: mtd: virt-concat: unlink discarded items before fre… |
| 2026-11-19 15:17:59 | [CVE-2026-99459](https://nvd.nist.gov/vuln/detail/CVE-2026-99459) |  |  | In the Linux kernel, the following vulnerability has been resolved: mshv_vtl: detach poll waiter on POLLFREE MSHV_SET_P… |
| 2026-11-19 15:18:00 | [CVE-2026-99460](https://nvd.nist.gov/vuln/detail/CVE-2026-99460) |  |  | In the Linux kernel, the following vulnerability has been resolved: mptcp: hold MP_JOIN msk ref when cloning reqsk TCP… |

_Showing the first 200 of 305 CVEs; see the [full CSV](data/new-cves-2026-11-19T15-20-24-836292Z.csv)._

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
