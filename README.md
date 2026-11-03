# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-11-03 15:19 UTC

New CVEs published between 2026-11-03 14:18 UTC and 2026-11-03 15:19 UTC.

[Full CSV](data/new-cves-2026-11-03T15-19-10-332687Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-11-03 15:17:19 | [CVE-2026-100493](https://nvd.nist.gov/vuln/detail/CVE-2026-100493) | Medium | 6.9 | An integer overflow in the DDS RGB888 loader of AMD Compressonator SDK could allow an attacker to supply a crafted DDS… |
| 2026-11-03 15:17:19 | [CVE-2026-106991](https://nvd.nist.gov/vuln/detail/CVE-2026-106991) | High | 7.1 | hustoj >=24.09.10 and <=26.08.19 is vulnerable to Incorrect Access Control. Any registered user can delete, lock, or st… |
| 2026-11-03 15:17:23 | [CVE-2026-110265](https://nvd.nist.gov/vuln/detail/CVE-2026-110265) | Medium | 6.5 | A specially crafted malformed search query could return results from outside a user's organization. Log analysis of run… |
| 2026-11-03 15:17:24 | [CVE-2026-118488](https://nvd.nist.gov/vuln/detail/CVE-2026-118488) | Medium | 5.9 | In Eclipse Vert.x versions [4.0.0, 4.5.35] or [5.0.0, 5.2.2], when a malicious server keeps sending bytes on an EOL-ter… |
| 2026-11-03 15:17:24 | [CVE-2026-118489](https://nvd.nist.gov/vuln/detail/CVE-2026-118489) | High | 7.5 | In Eclipse Vert.x versions [4.0.0,4.5.35] or [5.0.0,5.2.2], when one `CachingWebClient` is shared across users — the do… |
| 2026-11-03 15:17:24 | [CVE-2026-118527](https://nvd.nist.gov/vuln/detail/CVE-2026-118527) | Medium | 4.3 | Use of predictable filenames in Ivanti Connect Secure before versions 25.1.1.3 and 22.8R2.6 allows a remote authenticat… |
| 2026-11-03 15:17:25 | [CVE-2026-121386](https://nvd.nist.gov/vuln/detail/CVE-2026-121386) | High | 8.7 | FreeRDP before 3.32.2 contains a denial of service vulnerability in WinPR's winpr_read_png_from_buffer() and winpr_conv… |
| 2026-11-03 15:17:25 | [CVE-2026-121387](https://nvd.nist.gov/vuln/detail/CVE-2026-121387) | Medium | 5.3 | FreeRDP 2.0.0 before 3.32.2 contains an out-of-bounds read vulnerability in freerdp_dsp_decode_gsm610 that allows malic… |
| 2026-11-03 15:17:25 | [CVE-2026-121388](https://nvd.nist.gov/vuln/detail/CVE-2026-121388) | High | 7.1 | FreeRDP from 3.0.0 before 3.32.2 contains an uncontrolled resource allocation vulnerability that allows malicious RDP s… |
| 2026-11-03 15:17:26 | [CVE-2026-121389](https://nvd.nist.gov/vuln/detail/CVE-2026-121389) | Low | 2.3 | FreeRDP from 3.27.0 before 3.32.2 contains a denial of service vulnerability in rdpdr_dump_packet that allows malicious… |
| 2026-11-03 15:17:26 | [CVE-2026-121390](https://nvd.nist.gov/vuln/detail/CVE-2026-121390) | Medium | 5.3 | FreeRDP 3.0.0 before 3.32.2 built with WITH_AAD=ON contains a reachable assertion because its ARM gateway response pars… |
| 2026-11-03 15:17:26 | [CVE-2026-121391](https://nvd.nist.gov/vuln/detail/CVE-2026-121391) | Medium | 5.3 | FreeRDP from 3.0.0 before 3.32.2 contains a file descriptor leak in parallel_process_irp_create that fails to close pre… |
| 2026-11-03 15:17:26 | [CVE-2026-121392](https://nvd.nist.gov/vuln/detail/CVE-2026-121392) | Critical | 9.1 | FreeRDP before 3.32.2 contains an improper certificate validation vulnerability in tls_verify_certificate() that accept… |
| 2026-11-03 15:17:26 | [CVE-2026-121393](https://nvd.nist.gov/vuln/detail/CVE-2026-121393) | High | 7.1 | FreeRDP from 3.0.0 before 3.32.2 contains a denial of service vulnerability that allows malicious RDP servers to abort… |
| 2026-11-03 15:17:27 | [CVE-2026-121394](https://nvd.nist.gov/vuln/detail/CVE-2026-121394) | High | 7.1 | FreeRDP from 3.11.0 before 3.32.2 contains an assertion failure in the RemoteFX RLGR decoder that allows malicious serv… |
| 2026-11-03 15:17:27 | [CVE-2026-121395](https://nvd.nist.gov/vuln/detail/CVE-2026-121395) | High | 7.1 | FreeRDP from 3.17.0 before 3.32.2 contains an assertion failure in the RemoteFX differential decoder when verbose WinPR… |
| 2026-11-03 15:17:27 | [CVE-2026-121396](https://nvd.nist.gov/vuln/detail/CVE-2026-121396) | Medium | 5.3 | FreeRDP clients from 3.0.0 before 3.32.2 built with verbose WinPR assertions contain a reachable assertion in rts_read_… |
| 2026-11-03 15:17:27 | [CVE-2026-121397](https://nvd.nist.gov/vuln/detail/CVE-2026-121397) | Medium | 5.3 | FreeRDP before 3.32.2 contains a heap buffer over-read vulnerability in save_png_to_buffer() that allows malicious RDP… |
| 2026-11-03 15:17:27 | [CVE-2026-121398](https://nvd.nist.gov/vuln/detail/CVE-2026-121398) | High | 8.2 | FreeRDP before 3.32.2 contains a cross-thread use-after-free vulnerability in the freerdp-proxy dyn-channel-dump module… |
| 2026-11-03 15:17:28 | [CVE-2026-121400](https://nvd.nist.gov/vuln/detail/CVE-2026-121400) | High | 7.1 | FreeRDP before 3.32.2 contains a denial-of-service vulnerability in rdg_process_control_packet that allows a malicious… |
| 2026-11-03 15:17:28 | [CVE-2026-121401](https://nvd.nist.gov/vuln/detail/CVE-2026-121401) | Medium | 5.3 | FreeRDP before 3.32.2 contains a denial of service vulnerability where rdg_process_packet dispatches a PKT_TYPE_EXTENDE… |
| 2026-11-03 15:17:28 | [CVE-2026-121402](https://nvd.nist.gov/vuln/detail/CVE-2026-121402) | High | 7.1 | FreeRDP before 3.32.2 contains a NULL pointer dereference vulnerability that allows malicious RDP servers to crash xfre… |
| 2026-11-03 15:17:28 | [CVE-2026-121403](https://nvd.nist.gov/vuln/detail/CVE-2026-121403) | Medium | 5.3 | FreeRDP before 3.32.2 contains a denial of service vulnerability where a malformed drive DEVICE_IOREQUEST with a trunca… |
| 2026-11-03 15:17:28 | [CVE-2026-121404](https://nvd.nist.gov/vuln/detail/CVE-2026-121404) | High | 7.1 | FreeRDP before 3.32.2 contains a denial of service vulnerability in the shadow server that allows authenticated RDP cli… |
| 2026-11-03 15:17:28 | [CVE-2026-121399](https://nvd.nist.gov/vuln/detail/CVE-2026-121399) | Medium | 5.3 | FreeRDP before 3.32.2 contains a memory allocation vulnerability in rdg_receive_packet that allows a malicious RD Gatew… |
| 2026-11-03 15:17:29 | [CVE-2026-121405](https://nvd.nist.gov/vuln/detail/CVE-2026-121405) | Medium | 5.3 | FreeRDP before 3.32.2 fails to cap the OutputBufferLength in serial device-control IRP requests, allowing malicious ser… |
| 2026-11-03 15:17:29 | [CVE-2026-121406](https://nvd.nist.gov/vuln/detail/CVE-2026-121406) | Medium | 5.3 | FreeRDP before 3.32.2 allows a client assertion abort because rdpgfx_on_data_received rejects only negative zgfx_decomp… |
| 2026-11-03 15:17:29 | [CVE-2026-121407](https://nvd.nist.gov/vuln/detail/CVE-2026-121407) | High | 7.1 | FreeRDP before 3.32.2 contains a denial of service vulnerability in the shadow server's remdesk_server_thread that allo… |
| 2026-11-03 15:17:29 | [CVE-2026-121408](https://nvd.nist.gov/vuln/detail/CVE-2026-121408) | Medium | 6.0 | FreeRDP before 3.32.2 contains a use-after-free in the urbdrc USB redirection channel because FindChannelById returns a… |
| 2026-11-03 15:17:29 | [CVE-2026-121409](https://nvd.nist.gov/vuln/detail/CVE-2026-121409) | High | 8.2 | FreeRDP before 3.32.2 contains a denial of service vulnerability that allows malicious servers or unauthenticated peers… |
| 2026-11-03 15:17:29 | [CVE-2026-121410](https://nvd.nist.gov/vuln/detail/CVE-2026-121410) | Medium | 5.3 | FreeRDP before 3.32.2 contains a denial of service vulnerability in the RDPGFX ALPHA WIRETOSURFACE_2 handler that fails… |
| 2026-11-03 15:17:30 | [CVE-2026-121411](https://nvd.nist.gov/vuln/detail/CVE-2026-121411) | Low | 2.3 | FreeRDP before 3.32.2 fails to bound server-supplied target dimensions and output origin in RDPGFX MAPSURFACETOSCALEDOU… |
| 2026-11-03 15:17:30 | [CVE-2026-121412](https://nvd.nist.gov/vuln/detail/CVE-2026-121412) | High | 7.1 | FreeRDP from 3.0.0 before 3.32.2 contains an uncontrolled resource consumption vulnerability in the proxy that lets con… |
| 2026-11-03 15:17:30 | [CVE-2026-121413](https://nvd.nist.gov/vuln/detail/CVE-2026-121413) | Low | 2.3 | Parse Server before 8.6.112 and 9.0.0 before 9.10.6-alpha.4 contains an authorization bypass in the session upgrade end… |
| 2026-11-03 15:17:30 | [CVE-2026-121414](https://nvd.nist.gov/vuln/detail/CVE-2026-121414) | High | 8.2 | Parse Server before 8.6.110 and 9.0.0 before 9.10.6-alpha.2 fails to contain a serialization error when an object updat… |
| 2026-11-03 15:17:31 | [CVE-2026-121415](https://nvd.nist.gov/vuln/detail/CVE-2026-121415) | Medium | 6.3 | Parse Server before 8.6.111 and 9.0.0 before 9.10.6-alpha.3 on MongoDB skips field type validation for null-valued dot… |
| 2026-11-03 15:17:31 | [CVE-2026-121416](https://nvd.nist.gov/vuln/detail/CVE-2026-121416) | High | 7.1 | SurrealDB 2.0.0 before 3.3.1 does not enforce --deny-funcs restrictions on method-style function calls in the streaming… |
| 2026-11-03 15:17:31 | [CVE-2026-121417](https://nvd.nist.gov/vuln/detail/CVE-2026-121417) | High | 8.8 | SurrealDB before 3.3.0 contains a use-after-free vulnerability in surrealdb-core KV backends that pass borrowed transac… |
| 2026-11-03 15:17:31 | [CVE-2026-121418](https://nvd.nist.gov/vuln/detail/CVE-2026-121418) | Medium | 5.3 | SurrealDB from 3.1.0 before 3.3.0 contains an incorrect authorization vulnerability that allows record users to infer r… |
| 2026-11-03 15:17:31 | [CVE-2026-121419](https://nvd.nist.gov/vuln/detail/CVE-2026-121419) | High | 8.6 | SurrealDB from 3.1.0 before 3.3.0 contains an improper authentication vulnerability where the MCP BoundSubject fingerpr… |
| 2026-11-03 15:17:32 | [CVE-2026-121420](https://nvd.nist.gov/vuln/detail/CVE-2026-121420) | Medium | 4.8 | SurrealDB from 3.2.0 before 3.3.0 contains a server-side request forgery vulnerability in the FilteringResolver is_priv… |
| 2026-11-03 15:17:32 | [CVE-2026-121421](https://nvd.nist.gov/vuln/detail/CVE-2026-121421) | Medium | 5.3 | SurrealDB 3.1.0 before 3.3.0 contains a server-side request forgery vulnerability in network-capability matching becaus… |
| 2026-11-03 15:17:32 | [CVE-2026-121422](https://nvd.nist.gov/vuln/detail/CVE-2026-121422) | Medium | 5.1 | SurrealDB from 3.1.0 before 3.3.0 contains a server-side request forgery vulnerability that allows database Owners to b… |
| 2026-11-03 15:17:32 | [CVE-2026-121423](https://nvd.nist.gov/vuln/detail/CVE-2026-121423) | High | 7.1 | SurrealDB before 3.3.0 contains an unbounded recursion vulnerability that allows authenticated users to abort the surre… |
| 2026-11-03 15:17:32 | [CVE-2026-121424](https://nvd.nist.gov/vuln/detail/CVE-2026-121424) | High | 8.3 | Nodemailer from 3.0.0 before 10.1.4 contains an address parsing vulnerability in addressparser that allows remote attac… |
| 2026-11-03 15:17:33 | [CVE-2026-121425](https://nvd.nist.gov/vuln/detail/CVE-2026-121425) | High | 8.3 | Nodemailer from 3.0.0 before 10.1.4 contains a parsing flaw in addressparser that ends an RFC 5322 group at a semicolon… |
| 2026-11-03 15:17:33 | [CVE-2026-121426](https://nvd.nist.gov/vuln/detail/CVE-2026-121426) | High | 8.3 | Nodemailer from 3.0.0 before 10.1.4 contains an address parsing vulnerability in addressparser that ends an angle-addr… |
| 2026-11-03 15:17:33 | [CVE-2026-121427](https://nvd.nist.gov/vuln/detail/CVE-2026-121427) | High | 8.7 | AzuraCast through 0.23.8 fails to remove frontend_config.custom_config in PUT /station/{id}/profile/edit for users lack… |
| 2026-11-03 15:17:33 | [CVE-2026-121428](https://nvd.nist.gov/vuln/detail/CVE-2026-121428) | High | 8.7 | AzuraCast through 0.23.8 contains a remote code execution vulnerability that allows authenticated station managers to i… |
| 2026-11-03 15:17:33 | [CVE-2026-121429](https://nvd.nist.gov/vuln/detail/CVE-2026-121429) | High | 8.7 | AzuraCast through 0.23.8 contains a command injection vulnerability that allows station users with Profile permission t… |
| 2026-11-03 15:17:33 | [CVE-2026-121430](https://nvd.nist.gov/vuln/detail/CVE-2026-121430) | Medium | 5.3 | AzuraCast before 0.24.0 contains a missing authorization vulnerability in the GET and POST /api/station/{station_id}/wa… |
| 2026-11-03 15:17:34 | [CVE-2026-121431](https://nvd.nist.gov/vuln/detail/CVE-2026-121431) | Medium | 6.9 | AzuraCast before 0.24.0 contains a server-side request forgery vulnerability that allows station users with WebHooks pe… |
| 2026-11-03 15:17:34 | [CVE-2026-121432](https://nvd.nist.gov/vuln/detail/CVE-2026-121432) | Medium | 5.1 | AzuraCast before 0.24.0 contains a CRLF injection vulnerability that allows low-privilege station users to inject playl… |
| 2026-11-03 15:17:34 | [CVE-2026-121433](https://nvd.nist.gov/vuln/detail/CVE-2026-121433) | Medium | 5.1 | AzuraCast before 0.24.0 contains a stored CSV formula injection vulnerability that allows station users with Media perm… |
| 2026-11-03 15:17:34 | [CVE-2026-121434](https://nvd.nist.gov/vuln/detail/CVE-2026-121434) | Medium | 5.3 | Froxlor 2.3.0 before 2.3.15 contains a missing authorization check in the Certificates.add and Certificates.update API… |
| 2026-11-03 15:17:34 | [CVE-2026-121435](https://nvd.nist.gov/vuln/detail/CVE-2026-121435) | Medium | 5.3 | Froxlor before 2.3.15 contains an authorization bypass vulnerability that allows authenticated customers to create MySQ… |
| 2026-11-03 15:17:34 | [CVE-2026-121436](https://nvd.nist.gov/vuln/detail/CVE-2026-121436) | High | 8.6 | Froxlor from 2.3.8 before 2.3.15 contains an information disclosure vulnerability that allows administrators with custo… |
| 2026-11-03 15:17:35 | [CVE-2026-121437](https://nvd.nist.gov/vuln/detail/CVE-2026-121437) | High | 8.7 | Mistune from 3.3.0 before 3.3.4 contains a denial of service vulnerability that allows remote attackers to exhaust CPU… |
| 2026-11-03 15:17:35 | [CVE-2026-121438](https://nvd.nist.gov/vuln/detail/CVE-2026-121438) | Medium | 6.9 | Mistune before 3.3.3 contains a denial of service vulnerability in InlineParser.parse_link that allows attackers to cau… |
| 2026-11-03 15:17:35 | [CVE-2026-121439](https://nvd.nist.gov/vuln/detail/CVE-2026-121439) | Medium | 6.9 | Wasmtime 46.0.0 before 48.0.7 and 49.0.0 before 49.0.4 contains a response splitting vulnerability in wasi-http p3 that… |
| 2026-11-03 15:17:35 | [CVE-2026-121440](https://nvd.nist.gov/vuln/detail/CVE-2026-121440) | Medium | 6.3 | Wasmtime 46.0.0 before 48.0.7 and 49.0.0 before 49.0.4 fails to check forwarded trailers against the WasiHttpHooks::is_… |
| 2026-11-03 15:17:35 | [CVE-2026-121441](https://nvd.nist.gov/vuln/detail/CVE-2026-121441) | Medium | 6.3 | Wasmtime before 36.0.19, 37.0.0 before 48.0.7, and 49.0.0 before 49.0.4 contains a request smuggling vulnerability in w… |
| 2026-11-03 15:17:36 | [CVE-2026-121442](https://nvd.nist.gov/vuln/detail/CVE-2026-121442) | Medium | 5.3 | Frappe HRMS before 15.61.0 contains a permission bypass vulnerability that allows authenticated employees to view other… |
| 2026-11-03 15:17:36 | [CVE-2026-121443](https://nvd.nist.gov/vuln/detail/CVE-2026-121443) | Medium | 6.9 | svg-sanitizer from 1.1.0 before 1.1.1 contains a denial of service vulnerability that allows remote attackers to crash… |
| 2026-11-03 15:17:36 | [CVE-2026-121444](https://nvd.nist.gov/vuln/detail/CVE-2026-121444) | High | 8.7 | svg-sanitizer from 0.11.0 before 1.1.0 contains an algorithmic complexity denial of service vulnerability in hasInfinit… |
| 2026-11-03 15:17:36 | [CVE-2026-121445](https://nvd.nist.gov/vuln/detail/CVE-2026-121445) | High | 8.2 | darylldoyle svg-sanitizer from 1.0.0 before 1.1.0 contains a regular expression denial of service vulnerability in the… |
| 2026-11-03 15:17:36 | [CVE-2026-121446](https://nvd.nist.gov/vuln/detail/CVE-2026-121446) | Medium | 5.3 | svg-sanitizer from 0.5.0 before 1.1.0 contains an incomplete filtering vulnerability that allows attackers to bypass re… |
| 2026-11-03 15:17:37 | [CVE-2026-121447](https://nvd.nist.gov/vuln/detail/CVE-2026-121447) | Medium | 5.3 | svg-sanitizer before 1.1.0 contains a cross-site scripting vulnerability that allows attackers to bypass sanitization b… |
| 2026-11-03 15:17:37 | [CVE-2026-121448](https://nvd.nist.gov/vuln/detail/CVE-2026-121448) | High | 8.7 | Dockhand before 1.0.54 contains a path traversal vulnerability that allows authenticated users to read, overwrite, and… |
| 2026-11-03 15:17:37 | [CVE-2026-121449](https://nvd.nist.gov/vuln/detail/CVE-2026-121449) | High | 7.1 | Dockhand from 1.0.47 before 1.0.54 exposes plaintext stack secrets because deployStack() attaches resolved secret value… |
| 2026-11-03 15:17:37 | [CVE-2026-121505](https://nvd.nist.gov/vuln/detail/CVE-2026-121505) | Low | 3.7 | An out-of-bounds read in the NTS-KE client response parser (nts_client_process_response_core) in NTPsec before 1.2.4 al… |
| 2026-11-03 15:17:37 | [CVE-2026-121506](https://nvd.nist.gov/vuln/detail/CVE-2026-121506) | High | 7.4 | An out-of-bounds read and write in NTS client extension field parsing (extens_client_recv) in NTPsec before 1.2.5 allow… |
| 2026-11-03 15:17:37 | [CVE-2026-121507](https://nvd.nist.gov/vuln/detail/CVE-2026-121507) | Medium | 5.9 | Double Free in µD3TN BPv6 Fragmenter Block Duplication allows Unauthenticated Remote Attacker to Cause DoS on Allocatio… |
| 2026-11-03 15:17:38 | [CVE-2026-121510](https://nvd.nist.gov/vuln/detail/CVE-2026-121510) | High | 7.5 | Remote Unauthenticated Heap Out-of-Bounds Write in µD3TN BPv6 Administrative Record Parser allows Unauthenticated Remot… |
| 2026-11-03 15:17:38 | [CVE-2026-121511](https://nvd.nist.gov/vuln/detail/CVE-2026-121511) | High | 7.1 | Heap Out-of-Bounds Read in µD3TN BPv6/BPv7 Fragmenter allows Local Attacker to Read Memory and Reliably Cause DoS |
| 2026-11-03 15:17:38 | [CVE-2026-121512](https://nvd.nist.gov/vuln/detail/CVE-2026-121512) | High | 7.5 | Memory Leak with Amplification in µD3TN BPv6 EID Reference Handling allows Unauthenticated Remote Attacker to Cause DoS |
| 2026-11-03 15:17:38 | [CVE-2026-121513](https://nvd.nist.gov/vuln/detail/CVE-2026-121513) | High | 7.5 | Off-by-one Heap Overflow in µD3TN v0.15.1 SPP Parser allows Unauthenticated Remote Attacker to Reliably Cause DoS |
| 2026-11-03 15:17:38 | [CVE-2026-121508](https://nvd.nist.gov/vuln/detail/CVE-2026-121508) | Medium | 5.9 | Use-After-Free in µD3TN BPv6 Fragmenter Cleanup allows Unauthenticated Remote Attacker to Cause DoS on Allocation Failu… |
| 2026-11-03 15:17:39 | [CVE-2026-40652](https://nvd.nist.gov/vuln/detail/CVE-2026-40652) | Medium | 5.2 | An out-of-bounds read condition in the AMD Compressonator SDK could allow an attacker with local access to supply a spe… |
| 2026-11-03 15:17:39 | [CVE-2026-40659](https://nvd.nist.gov/vuln/detail/CVE-2026-40659) | Medium | 5.1 | An integer overflow condition in the AMD Compressonator SDK could allow an attacker with local access to supply a speci… |
| 2026-11-03 15:17:39 | [CVE-2026-40660](https://nvd.nist.gov/vuln/detail/CVE-2026-40660) | Medium | 5.2 | A heap-based out-of-bounds (OOB) read vulnerability in the AMD Compressonator SDK could allow an attacker with local ac… |
| 2026-11-03 15:17:39 | [CVE-2026-40661](https://nvd.nist.gov/vuln/detail/CVE-2026-40661) | Medium | 5.2 | An out-of-bounds write (OOW) condition in the AMD Compressonator SDK could allow an attacker with local access to suppl… |
| 2026-11-03 15:17:39 | [CVE-2026-43603](https://nvd.nist.gov/vuln/detail/CVE-2026-43603) | Medium | 6.9 | A NULL pointer dereference in the Linux GPU driver could potentially lead to a kernel crash and result in denial of ser… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
