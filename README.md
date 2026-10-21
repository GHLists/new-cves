# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-21 01:20 UTC

New CVEs published between 2026-10-21 00:18 UTC and 2026-10-21 01:20 UTC.

[Full CSV](data/new-cves-2026-10-21T01-20-06-123106Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-10-21 01:17:18 | [CVE-2020-37286](https://nvd.nist.gov/vuln/detail/CVE-2020-37286) | High | 8.3 | Vyper from 0.1.0b4 before 0.3.0 contains a memory corruption vulnerability caused by an incorrect stack tip pointer whe… |
| 2026-10-21 01:17:18 | [CVE-2020-37287](https://nvd.nist.gov/vuln/detail/CVE-2020-37287) | High | 8.2 | Vyper before 0.2.6 contains a call stack corruption vulnerability that causes incorrect function outputs when complex t… |
| 2026-10-21 01:17:18 | [CVE-2020-37288](https://nvd.nist.gov/vuln/detail/CVE-2020-37288) | Medium | 6.3 | Vyper from 0.1.0b10 before 0.2.3 generates incorrect code for a return statement inside a for loop in an internal funct… |
| 2026-10-21 01:17:18 | [CVE-2020-37289](https://nvd.nist.gov/vuln/detail/CVE-2020-37289) | Medium | 6.3 | Vyper before 0.3.1 lacks a uint8 type, allowing interface return values declared as uint8, such as ERC20.decimals(), to… |
| 2026-10-21 01:17:18 | [CVE-2021-48018](https://nvd.nist.gov/vuln/detail/CVE-2021-48018) | High | 8.3 | Vyper from 0.2.13 before 0.2.15 allocates storage slots for @nonreentrant reentrancy locks at the same locations as con… |
| 2026-10-21 01:17:19 | [CVE-2021-48019](https://nvd.nist.gov/vuln/detail/CVE-2021-48019) | Medium | 6.3 | Vyper before 0.2.9 deploys forwarder proxies through the built-in create_forwarder_to function that report a fixed 4096… |
| 2026-10-21 01:17:19 | [CVE-2021-48020](https://nvd.nist.gov/vuln/detail/CVE-2021-48020) | High | 8.3 | Vyper from 0.1.0b4 before 0.3.0 contains a memory corruption vulnerability caused by an incorrect stack tip pointer whe… |
| 2026-10-21 01:17:19 | [CVE-2025-71437](https://nvd.nist.gov/vuln/detail/CVE-2025-71437) | High | 8.7 | Astral uv before 0.8.22 contains a path traversal vulnerability in source distribution (sdist) tar extraction that allo… |
| 2026-10-21 01:17:19 | [CVE-2026-105044](https://nvd.nist.gov/vuln/detail/CVE-2026-105044) | High | 8.5 | Improper Neutralization of Special Elements used in an OS Command in Security Toolbox versions before 20260929 in Qingt… |
| 2026-10-21 01:17:20 | [CVE-2026-111943](https://nvd.nist.gov/vuln/detail/CVE-2026-111943) |  |  | On most platforms, Go uses the given system root certificates. However, in some narrower cases, the system trust stores… |
| 2026-10-21 01:17:25 | [CVE-2026-113736](https://nvd.nist.gov/vuln/detail/CVE-2026-113736) | High | 8.9 | A vulnerability has been found in D-Link DHP-W610AV 1.02EUb03. The impacted element is the function login_prepare_hnap… |
| 2026-10-21 01:17:25 | [CVE-2026-113737](https://nvd.nist.gov/vuln/detail/CVE-2026-113737) | Low | 2.0 | A flaw has been found in R6410418 Jackrong-llm-finetuning-guide up to ef2b17f2798cd18cd85375080c35a58397ad0d09. This af… |
| 2026-10-21 01:17:25 | [CVE-2026-113738](https://nvd.nist.gov/vuln/detail/CVE-2026-113738) | Low | 2.1 | A vulnerability has been found in R6410418 Jackrong-llm-finetuning-guide up to ef2b17f2798cd18cd85375080c35a58397ad0d09… |
| 2026-10-21 01:17:25 | [CVE-2026-113740](https://nvd.nist.gov/vuln/detail/CVE-2026-113740) | Low | 2.1 | A flaw has been found in itsourcecode Online Cake Ordering System 1.0. Affected by this vulnerability is an unknown fun… |
| 2026-10-21 01:17:25 | [CVE-2026-113741](https://nvd.nist.gov/vuln/detail/CVE-2026-113741) | Low | 2.1 | A vulnerability has been found in itsourcecode Online Cake Ordering System 1.0. Affected by this issue is some unknown… |
| 2026-10-21 01:17:26 | [CVE-2026-114038](https://nvd.nist.gov/vuln/detail/CVE-2026-114038) | Medium | 5.1 | A flaw was found in device-mapper-multipath. A local user can trigger an out-of-bounds read by sending a command with a… |
| 2026-10-21 01:17:26 | [CVE-2026-114041](https://nvd.nist.gov/vuln/detail/CVE-2026-114041) | Medium | 6.9 | FreeRDP before 3.32.1 on Windows contains a heap out-of-bounds read in client_cli_present_gateway_message that passes a… |
| 2026-10-21 01:17:26 | [CVE-2026-114042](https://nvd.nist.gov/vuln/detail/CVE-2026-114042) | High | 7.1 | FreeRDP 3.32.0 contains a use-after-free vulnerability in the drdynvc channel that frees a pool-owned stream with the o… |
| 2026-10-21 01:17:26 | [CVE-2026-114043](https://nvd.nist.gov/vuln/detail/CVE-2026-114043) | High | 7.1 | FreeRDP before 3.32.1 contains a heap-based out-of-bounds read in WinPR's clipboard PNG-to-CF_DIB synthesis because win… |
| 2026-10-21 01:17:26 | [CVE-2026-114044](https://nvd.nist.gov/vuln/detail/CVE-2026-114044) | Medium | 6.9 | FreeRDP before 3.32.1 contains a heap out-of-bounds read vulnerability in the Android client that allows malicious RDP… |
| 2026-10-21 01:17:26 | [CVE-2026-114045](https://nvd.nist.gov/vuln/detail/CVE-2026-114045) | High | 8.7 | FreeRDP before 3.32.1 contains a heap-based buffer overflow in the server-side rdpsnd channel because an integer wrapar… |
| 2026-10-21 01:17:27 | [CVE-2026-114046](https://nvd.nist.gov/vuln/detail/CVE-2026-114046) | High | 7.1 | FreeRDP 3.0.0 before 3.32.0 contains a null-pointer dereference in the smartcard emulation backend that accepts a null… |
| 2026-10-21 01:17:27 | [CVE-2026-114047](https://nvd.nist.gov/vuln/detail/CVE-2026-114047) | High | 7.6 | FreeRDP from 2.0.0 before 3.32.0 contains an improper certificate validation vulnerability in its proxy that accepts un… |
| 2026-10-21 01:17:27 | [CVE-2026-114048](https://nvd.nist.gov/vuln/detail/CVE-2026-114048) | Medium | 5.1 | WWBN AVideo before 24.0 contains a cross-site request forgery vulnerability in legacy endpoints like playlistStatus.php… |
| 2026-10-21 01:17:27 | [CVE-2026-114049](https://nvd.nist.gov/vuln/detail/CVE-2026-114049) | Medium | 6.3 | vLLM before 0.31.0 contains a cross-request mask leak in InputBatch.condense() that allows remote attackers to constrai… |
| 2026-10-21 01:17:27 | [CVE-2026-114050](https://nvd.nist.gov/vuln/detail/CVE-2026-114050) | High | 7.1 | vLLM before 0.31.0 uses a client-supplied multimodal uuid verbatim as cache identity with no consistency check on cache… |
| 2026-10-21 01:17:27 | [CVE-2026-114051](https://nvd.nist.gov/vuln/detail/CVE-2026-114051) | High | 7.1 | vLLM before 0.31.0 skips the min_tokens <= max_tokens check for /inference/v1/generate requests with a null max_tokens,… |
| 2026-10-21 01:17:27 | [CVE-2026-114052](https://nvd.nist.gov/vuln/detail/CVE-2026-114052) | High | 8.7 | vLLM after 0.24.0 and before 0.31.0 contains a memory exhaustion vulnerability in MOSS-Audio model serving that caches… |
| 2026-10-21 01:17:28 | [CVE-2026-114053](https://nvd.nist.gov/vuln/detail/CVE-2026-114053) | Critical | 9.2 | vLLM from 0.7.3 before 0.31.0 forwards the request-supplied mm_processor_kwargs.code_revision to Transformers AutoProce… |
| 2026-10-21 01:17:28 | [CVE-2026-114054](https://nvd.nist.gov/vuln/detail/CVE-2026-114054) | High | 7.1 | vLLM before 0.31.0 contains a cache aliasing vulnerability that allows authenticated attackers to collide shared cache… |
| 2026-10-21 01:17:28 | [CVE-2026-114055](https://nvd.nist.gov/vuln/detail/CVE-2026-114055) | High | 8.7 | vLLM from 0.7.3 before 0.31.0 contains an uncontrolled resource consumption vulnerability that allows remote clients to… |
| 2026-10-21 01:17:28 | [CVE-2026-114056](https://nvd.nist.gov/vuln/detail/CVE-2026-114056) | Medium | 5.3 | ArcadeDB from 26.8.1 before 26.10.1 contains an authorization bypass vulnerability that allows read-only users to modif… |
| 2026-10-21 01:17:28 | [CVE-2026-114057](https://nvd.nist.gov/vuln/detail/CVE-2026-114057) | Medium | 5.3 | ArcadeDB from 26.2.1 before 26.10.1 contains a missing authorization vulnerability in the Bolt protocol handler that al… |
| 2026-10-21 01:17:28 | [CVE-2026-114058](https://nvd.nist.gov/vuln/detail/CVE-2026-114058) | Medium | 5.3 | ArcadeDB from 26.2.1 before 26.10.1 contains a missing authorization vulnerability in the Bolt protocol handler that le… |
| 2026-10-21 01:17:28 | [CVE-2026-114059](https://nvd.nist.gov/vuln/detail/CVE-2026-114059) | High | 7.7 | ArcadeDB before 26.10.1 contains a remote code execution vulnerability that allows authenticated users, including read-… |
| 2026-10-21 01:17:29 | [CVE-2026-114060](https://nvd.nist.gov/vuln/detail/CVE-2026-114060) | Low | 2.1 | SvelteKit (@sveltejs/kit) before 3.0.0 contains an open redirect vulnerability in enhanced form actions (use:enhance) o… |
| 2026-10-21 01:17:29 | [CVE-2026-114061](https://nvd.nist.gov/vuln/detail/CVE-2026-114061) | Low | 2.3 | SvelteKit (@sveltejs/kit) before 3.0.0 contains a cross-site scripting vulnerability in prerendered pages because a cac… |
| 2026-10-21 01:17:29 | [CVE-2026-114062](https://nvd.nist.gov/vuln/detail/CVE-2026-114062) | Medium | 6.9 | SvelteKit before 3.0.0 contains a server-side request forgery vulnerability that allows remote attackers to reach inter… |
| 2026-10-21 01:17:29 | [CVE-2026-114063](https://nvd.nist.gov/vuln/detail/CVE-2026-114063) | High | 8.7 | SvelteKit (@sveltejs/kit) from 2.10.0 before 3.0.0 contains a path traversal vulnerability in the vite preview server o… |
| 2026-10-21 01:17:29 | [CVE-2026-114064](https://nvd.nist.gov/vuln/detail/CVE-2026-114064) | Medium | 5.1 | Snipe-IT before 8.7.0 contains a server-side request forgery vulnerability in the webhook testing feature that allows s… |
| 2026-10-21 01:17:29 | [CVE-2026-114065](https://nvd.nist.gov/vuln/detail/CVE-2026-114065) | High | 7.1 | Trigger.dev before 4.7.3 contains a tenant filtering bypass vulnerability that allows authenticated users to read other… |
| 2026-10-21 01:17:30 | [CVE-2026-114066](https://nvd.nist.gov/vuln/detail/CVE-2026-114066) | High | 7.2 | Trigger.dev before 4.7.0 contains a missing authorization vulnerability that allows holders of unrestricted environment… |
| 2026-10-21 01:17:30 | [CVE-2026-114067](https://nvd.nist.gov/vuln/detail/CVE-2026-114067) | High | 7.1 | Trigger.dev 4.5.0 before 4.6.2 contains an improper authorization vulnerability in the PUT snapshot-url session endpoin… |
| 2026-10-21 01:17:30 | [CVE-2026-114068](https://nvd.nist.gov/vuln/detail/CVE-2026-114068) | High | 7.2 | Trigger.dev before 4.6.0 contains a missing authorization vulnerability in the waitpoint token wait endpoint that allow… |
| 2026-10-21 01:17:30 | [CVE-2026-114069](https://nvd.nist.gov/vuln/detail/CVE-2026-114069) | High | 8.6 | Trigger.dev before 4.6.0 contains an improper authorization vulnerability in the GET /api/v1/projects/:projectRef/envva… |
| 2026-10-21 01:17:30 | [CVE-2026-114070](https://nvd.nist.gov/vuln/detail/CVE-2026-114070) | Medium | 5.1 | Trigger.dev 4.5.0 before 4.6.0 contains an information disclosure vulnerability in the Dashboard Agent input proxy that… |
| 2026-10-21 01:17:30 | [CVE-2026-114071](https://nvd.nist.gov/vuln/detail/CVE-2026-114071) | Low | 2.3 | Trigger.dev before 4.5.12 contains an authorization bypass vulnerability that allows authenticated project members to c… |
| 2026-10-21 01:17:31 | [CVE-2026-114072](https://nvd.nist.gov/vuln/detail/CVE-2026-114072) | Medium | 5.3 | The Trigger.dev webapp before 4.5.12 contains a cross-site request forgery vulnerability in its organization-level Slac… |
| 2026-10-21 01:17:31 | [CVE-2026-114073](https://nvd.nist.gov/vuln/detail/CVE-2026-114073) | Medium | 6.8 | Trigger.dev CLI before 4.5.9 contains an information disclosure vulnerability that exposes resolved environment secret… |
| 2026-10-21 01:17:31 | [CVE-2026-114074](https://nvd.nist.gov/vuln/detail/CVE-2026-114074) | Medium | 5.3 | Trigger.dev before 4.5.10 contains a server-side request forgery vulnerability that allows authenticated project member… |
| 2026-10-21 01:17:31 | [CVE-2026-114075](https://nvd.nist.gov/vuln/detail/CVE-2026-114075) | Medium | 5.3 | Trigger.dev before 4.5.12 contains an authorization bypass vulnerability that allows holders of capability-restricted u… |
| 2026-10-21 01:17:31 | [CVE-2026-114076](https://nvd.nist.gov/vuln/detail/CVE-2026-114076) | Medium | 5.3 | Trigger.dev before 4.5.2 contains a blind server-side request forgery vulnerability that allows authenticated tenants t… |
| 2026-10-21 01:17:31 | [CVE-2026-114077](https://nvd.nist.gov/vuln/detail/CVE-2026-114077) | Medium | 6.1 | Trigger.dev before 4.5.6 contains an authorization bypass vulnerability in createDeploymentBackgroundWorkerV4 that reso… |
| 2026-10-21 01:17:32 | [CVE-2026-114078](https://nvd.nist.gov/vuln/detail/CVE-2026-114078) | High | 7.2 | Trigger.dev before 4.5.6 contains an authorization bypass vulnerability in DeleteTaskScheduleService and SetActiveOnTas… |
| 2026-10-21 01:17:32 | [CVE-2026-114079](https://nvd.nist.gov/vuln/detail/CVE-2026-114079) | Medium | 5.3 | Trigger.dev before 4.5.6 contains an improper authorization vulnerability that allows holders of lower-trust environmen… |
| 2026-10-21 01:17:32 | [CVE-2026-114080](https://nvd.nist.gov/vuln/detail/CVE-2026-114080) | Medium | 5.3 | Trigger.dev before 4.5.2 contains a blind server-side request forgery vulnerability that allows authenticated project m… |
| 2026-10-21 01:17:32 | [CVE-2026-114081](https://nvd.nist.gov/vuln/detail/CVE-2026-114081) | High | 8.3 | Trigger.dev before 4.5.6 contains an SQL injection vulnerability in the TSQL query compiler, which concatenates window-… |
| 2026-10-21 01:17:32 | [CVE-2026-114082](https://nvd.nist.gov/vuln/detail/CVE-2026-114082) | High | 7.2 | Trigger.dev before 4.6.2 contains an authorization vulnerability that allows public-token holders with session write ac… |
| 2026-10-21 01:17:32 | [CVE-2026-114083](https://nvd.nist.gov/vuln/detail/CVE-2026-114083) | High | 8.6 | Trigger.dev before 4.5.0-rc.3 contains a path traversal vulnerability in the api/v1/packets and api/v2/packets endpoint… |
| 2026-10-21 01:17:32 | [CVE-2026-114084](https://nvd.nist.gov/vuln/detail/CVE-2026-114084) | High | 8.3 | Trigger.dev before 4.5.6 contains an SQL injection vulnerability in the /realtime/v1/runs endpoint, which concatenates… |
| 2026-10-21 01:17:33 | [CVE-2026-114085](https://nvd.nist.gov/vuln/detail/CVE-2026-114085) | High | 8.8 | Trigger.dev through 4.7.6 contains a missing authentication vulnerability in the supervisor workload server that allows… |
| 2026-10-21 01:17:33 | [CVE-2026-114086](https://nvd.nist.gov/vuln/detail/CVE-2026-114086) | Medium | 6.9 | Trigger.dev before 4.5.5 contains a missing authentication vulnerability in the realtime streams POST handler that allo… |
| 2026-10-21 01:17:33 | [CVE-2026-114087](https://nvd.nist.gov/vuln/detail/CVE-2026-114087) | Critical | 9.2 | Trigger.dev before 4.5.6 self-hosted Docker Compose deployments using the default secrets from hosting/docker/.env.exam… |
| 2026-10-21 01:17:33 | [CVE-2026-114088](https://nvd.nist.gov/vuln/detail/CVE-2026-114088) | High | 8.3 | Trigger.dev before 4.5.4 contains a hardcoded default secret vulnerability in the /coordinator Socket.IO namespace that… |
| 2026-10-21 01:17:33 | [CVE-2026-114089](https://nvd.nist.gov/vuln/detail/CVE-2026-114089) | High | 8.7 | Trigger.dev before 4.5.2 contains a cross-site request forgery vulnerability in the CLI authorization-code flow because… |
| 2026-10-21 01:17:33 | [CVE-2026-114090](https://nvd.nist.gov/vuln/detail/CVE-2026-114090) | High | 7.6 | Trigger.dev cli-v3 from 3.0.0 before 4.5.4 contains a missing authentication vulnerability in the trigger dev --mcp ser… |
| 2026-10-21 01:17:34 | [CVE-2026-114091](https://nvd.nist.gov/vuln/detail/CVE-2026-114091) | Medium | 6.0 | Trigger.dev before 4.5.0 looks up runs by friendlyId alone in the api.v1.runs.$runParam.replay route without scoping th… |
| 2026-10-21 01:17:34 | [CVE-2026-114092](https://nvd.nist.gov/vuln/detail/CVE-2026-114092) | High | 8.3 | Trigger.dev before 4.5.0 performs no authentication or organization check in the action handler of the dashboard run re… |
| 2026-10-21 01:17:34 | [CVE-2026-114093](https://nvd.nist.gov/vuln/detail/CVE-2026-114093) | Medium | 5.3 | Trigger.dev before 4.5.6 contains a cross-site request forgery vulnerability that allows remote attackers to log out au… |
| 2026-10-21 01:17:34 | [CVE-2026-114094](https://nvd.nist.gov/vuln/detail/CVE-2026-114094) | High | 8.7 | Dulwich before 1.2.9 fails to validate DOS drive letter prefixes in Git tree path elements on Windows, allowing arbitra… |
| 2026-10-21 01:17:34 | [CVE-2026-114095](https://nvd.nist.gov/vuln/detail/CVE-2026-114095) | High | 7.1 | Dulwich before 1.2.9 contains a denial of service vulnerability in Pack.resolve_object that allows attackers to cause i… |
| 2026-10-21 01:17:34 | [CVE-2026-114096](https://nvd.nist.gov/vuln/detail/CVE-2026-114096) | High | 7.3 | Dulwich from 0.24.0 before 1.2.8 contains a symlink following vulnerability in porcelain.checkout(paths=[...]) that all… |
| 2026-10-21 01:17:35 | [CVE-2026-114097](https://nvd.nist.gov/vuln/detail/CVE-2026-114097) | High | 7.3 | Dulwich from 0.23.1 before 1.2.8 contains a path traversal vulnerability in CommitFilter._apply_index_filter() that all… |
| 2026-10-21 01:17:35 | [CVE-2026-114098](https://nvd.nist.gov/vuln/detail/CVE-2026-114098) | High | 7.3 | Dulwich from 0.22.5 before 1.2.8 contains a path traversal vulnerability in stash.py pop() that allows attackers to wri… |
| 2026-10-21 01:17:35 | [CVE-2026-114099](https://nvd.nist.gov/vuln/detail/CVE-2026-114099) | Medium | 6.9 | Coraza from 3.0.0 before 3.8.1 has a JSON body processor that flattens nested properties into dot-separated ARGS_POST n… |
| 2026-10-21 01:17:35 | [CVE-2026-114100](https://nvd.nist.gov/vuln/detail/CVE-2026-114100) | Medium | 6.9 | Coraza from 3.0.4 before 3.8.1 contains a request body inspection bypass because request-body processor selection compa… |
| 2026-10-21 01:17:35 | [CVE-2026-114101](https://nvd.nist.gov/vuln/detail/CVE-2026-114101) | Medium | 6.3 | Coraza before 3.8.1 extracts multipart upload filenames with Go's mime.ParseMediaType, which silently ignores RFC 5987… |
| 2026-10-21 01:17:35 | [CVE-2026-114102](https://nvd.nist.gov/vuln/detail/CVE-2026-114102) | High | 8.7 | adm-zip before 0.6.1 contains a denial of service vulnerability that allows unauthenticated attackers to crash the Node… |
| 2026-10-21 01:17:36 | [CVE-2026-114103](https://nvd.nist.gov/vuln/detail/CVE-2026-114103) | Medium | 6.9 | adm-zip 0.6.0 contains a decompression bomb protection bypass that allows attackers to evade the maxOutputLength guard… |
| 2026-10-21 01:17:36 | [CVE-2026-114104](https://nvd.nist.gov/vuln/detail/CVE-2026-114104) | High | 8.2 | adm-zip before 0.6.1 contains an inconsistent entry resolution vulnerability that allows attackers to bypass content va… |
| 2026-10-21 01:17:36 | [CVE-2026-114105](https://nvd.nist.gov/vuln/detail/CVE-2026-114105) | Medium | 6.9 | Adm-zip before 0.6.1 contains an incorrect permission assignment vulnerability that allows attackers to set setuid, set… |
| 2026-10-21 01:17:36 | [CVE-2026-114106](https://nvd.nist.gov/vuln/detail/CVE-2026-114106) | High | 8.7 | HKUDS Vibe-Trading from 0.1.0 before 0.1.7 contains a path traversal vulnerability that allows remote attackers to read… |
| 2026-10-21 01:17:36 | [CVE-2026-114107](https://nvd.nist.gov/vuln/detail/CVE-2026-114107) | High | 8.7 | HKUDS Vibe-Trading from 0.1.0 before 0.1.7 contains an indirect prompt injection vulnerability that allows remote attac… |
| 2026-10-21 01:17:36 | [CVE-2026-114108](https://nvd.nist.gov/vuln/detail/CVE-2026-114108) | Critical | 9.3 | HKUDS Vibe-Trading from 0.1.0 before 0.1.7 contains a missing authentication vulnerability that allows unauthenticated… |
| 2026-10-21 01:17:36 | [CVE-2026-114109](https://nvd.nist.gov/vuln/detail/CVE-2026-114109) | High | 8.7 | uv before 0.11.15 contains a path traversal vulnerability that allows malicious wheels to write files outside the scrip… |
| 2026-10-21 01:17:37 | [CVE-2026-114110](https://nvd.nist.gov/vuln/detail/CVE-2026-114110) | High | 8.7 | Astral uv before 0.11.6 contains a path traversal vulnerability that allows attackers to delete arbitrary files by supp… |
| 2026-10-21 01:17:37 | [CVE-2026-114111](https://nvd.nist.gov/vuln/detail/CVE-2026-114111) | High | 8.9 | sharp before 0.35.5 bundles a librsvg dependency affected by a memory-related vulnerability (CVE-2026-96889) that, unde… |
| 2026-10-21 01:17:37 | [CVE-2026-114112](https://nvd.nist.gov/vuln/detail/CVE-2026-114112) | High | 8.9 | Sharp before 0.35.4 bundles a vulnerable libheif dependency that allows attackers to achieve possible remote code execu… |
| 2026-10-21 01:17:37 | [CVE-2026-114113](https://nvd.nist.gov/vuln/detail/CVE-2026-114113) | High | 8.4 | Sharp before 0.35.0 bundles a version of libvips affected by multiple vulnerabilities (CVE-2026-33327, CVE-2026-33328,… |
| 2026-10-21 01:17:37 | [CVE-2026-114114](https://nvd.nist.gov/vuln/detail/CVE-2026-114114) | Medium | 6.0 | Vyper 0.1.0b1 before 0.1.0b12, 0.1.0b14, and 0.4.1 through 0.5.0b1 mix character-based line offsets with Python's UTF-8… |
| 2026-10-21 01:17:37 | [CVE-2026-114115](https://nvd.nist.gov/vuln/detail/CVE-2026-114115) | Medium | 6.3 | Vyper 0.3.8 through 0.5.0b1 contains a compiler miscompilation vulnerability in parse_IfExp that reads nested arrays wi… |
| 2026-10-21 01:17:37 | [CVE-2026-114116](https://nvd.nist.gov/vuln/detail/CVE-2026-114116) | Medium | 6.0 | Vyper 0.1.0b1 before 0.1.0b17 and 0.4.1 through 0.5.0b1 builds its source-line table with str.splitlines(), which treat… |
| 2026-10-21 01:17:38 | [CVE-2026-114117](https://nvd.nist.gov/vuln/detail/CVE-2026-114117) | High | 8.2 | Vyper 0.3.8 through 0.5.0b1 contains an optimizer miscompilation in which (msg.value \| K) or (len(msg.data) \| K), where… |
| 2026-10-21 01:17:38 | [CVE-2026-114118](https://nvd.nist.gov/vuln/detail/CVE-2026-114118) | Medium | 6.3 | Vyper 0.3.4 through 0.5.0b1 computes the remaining blueprint size in create_from_blueprint by uint256 subtraction witho… |
| 2026-10-21 01:17:38 | [CVE-2026-114119](https://nvd.nist.gov/vuln/detail/CVE-2026-114119) | Critical | 9.3 | Best Practice Software Bp Premier before 1.14.1.1128 uses a hardcoded Microsoft SQL Server administrative password that… |
| 2026-10-21 01:17:38 | [CVE-2026-114197](https://nvd.nist.gov/vuln/detail/CVE-2026-114197) | High | 8.7 | Deserialization of untrusted data in Mandiant FLARE capa releases before 10.0.0 allows arbitrary code execution when a… |
| 2026-10-21 01:17:38 | [CVE-2026-114198](https://nvd.nist.gov/vuln/detail/CVE-2026-114198) | High | 8.7 | Deserialization of untrusted data in Mandiant FLARE floss releases before 3.2.0 allows arbitrary code execution when a… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
