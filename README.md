# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-09-29 18:18 UTC

New CVEs published between 2026-09-29 17:20 UTC and 2026-09-29 18:18 UTC.

[Full CSV](data/new-cves-2026-09-29T18-18-59-448456Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-09-29 18:17:06 | [CVE-2026-102242](https://nvd.nist.gov/vuln/detail/CVE-2026-102242) | High | 8.6 | Improper link resolution (CWE-59 / CWE-22) in the allowedLocalRoots path validation in Google MCP Toolbox for Databases… |
| 2026-09-29 18:17:07 | [CVE-2026-102555](https://nvd.nist.gov/vuln/detail/CVE-2026-102555) | High | 8.2 | A flaw was found in libsoup. The soup_uri_decode_data_uri() function incorrectly treated base64 data-URI payloads as NU… |
| 2026-09-29 18:17:08 | [CVE-2026-102558](https://nvd.nist.gov/vuln/detail/CVE-2026-102558) | High | 8.6 | A flaw was found in libsoup. When max-incoming-payload-size is unlimited (0), SoupWebsocketConnection could grow its in… |
| 2026-09-29 18:17:08 | [CVE-2026-102559](https://nvd.nist.gov/vuln/detail/CVE-2026-102559) | High | 8.6 | A flaw was found in libsoup. When constructing a masked WebSocket client frame for a very large outgoing payload, size… |
| 2026-09-29 18:17:08 | [CVE-2026-102560](https://nvd.nist.gov/vuln/detail/CVE-2026-102560) | High | 8.6 | A flaw was found in libsoup. When the permessage-deflate WebSocket extension compresses a very large outgoing message,… |
| 2026-09-29 18:17:09 | [CVE-2026-102639](https://nvd.nist.gov/vuln/detail/CVE-2026-102639) | High | 7.1 | MobilityDB version 1.3.0 and earlier contains an out-of-bounds read vulnerability in the MEOS binary and library WKB de… |
| 2026-09-29 18:17:09 | [CVE-2026-102677](https://nvd.nist.gov/vuln/detail/CVE-2026-102677) | High | 7.8 | Electron is a framework for writing cross-platform desktop applications using JavaScript, HTML and CSS. From 42.3.3 unt… |
| 2026-09-29 18:17:09 | [CVE-2026-102709](https://nvd.nist.gov/vuln/detail/CVE-2026-102709) | High | 8.4 | Improper validation of non-secure (NS) pointers in multiple TrustZone-M non-secure callable (NSC) entry functions allow… |
| 2026-09-29 18:17:10 | [CVE-2026-102710](https://nvd.nist.gov/vuln/detail/CVE-2026-102710) | Critical | 9.3 | Attacker model / Preconditions: a loaded `TXM_MODULE_USER_MODE \| TXM_MODULE_MEMORY_PROTECTION` module issuing kernel di… |
| 2026-09-29 18:17:10 | [CVE-2026-102711](https://nvd.nist.gov/vuln/detail/CVE-2026-102711) | Medium | 5.7 | Two issues in the ThreadX loadable-module loader, reached when a device loads an attacker-controlled module object via… |
| 2026-09-29 18:17:10 | [CVE-2026-102712](https://nvd.nist.gov/vuln/detail/CVE-2026-102712) | High | 8.8 | On the first DTLS ClientHello, the parser copies a device-claimed session_id length and validates the ciphersuite-list… |
| 2026-09-29 18:17:10 | [CVE-2026-102713](https://nvd.nist.gov/vuln/detail/CVE-2026-102713) | High | 8.8 | The TFTP server accepts a DATA datagram of any size. The dispatcher rejects datagrams shorter than four bytes (nxd_tftp… |
| 2026-09-29 18:17:10 | [CVE-2026-102714](https://nvd.nist.gov/vuln/detail/CVE-2026-102714) | High | 7.1 | `_nx_icmpv6_validate_options()` scans the option area with `while (length > 2)` (`common/src/nx_icmpv6_validate_options… |
| 2026-09-29 18:17:10 | [CVE-2026-102715](https://nvd.nist.gov/vuln/detail/CVE-2026-102715) | High | 7.1 | Any host on the LAN can send two mDNS records and make the responder write past the end of its transmit packet. The str… |
| 2026-09-29 18:17:10 | [CVE-2026-102716](https://nvd.nist.gov/vuln/detail/CVE-2026-102716) | High | 8.7 | An unauthenticated client can drain the RTSP server's packet pool with a couple of dozen requests that carry a Session… |
| 2026-09-29 18:17:11 | [CVE-2026-102718](https://nvd.nist.gov/vuln/detail/CVE-2026-102718) | High | 8.7 | hey, `_nx_snmp_utility_object_id_get` in the NetX Duo SNMP addon does not validate the claimed OID data length against… |
| 2026-09-29 18:17:11 | [CVE-2026-102719](https://nvd.nist.gov/vuln/detail/CVE-2026-102719) | Medium | 6.3 | Predictable DTLS HelloVerifyRequest Cookie in NetX Secure |
| 2026-09-29 18:17:11 | [CVE-2026-102720](https://nvd.nist.gov/vuln/detail/CVE-2026-102720) | Medium | 5.3 | A DHCP server, or anyone on the LAN who answers a DISCOVER first, can make the client read about a kilobyte past the en… |
| 2026-09-29 18:17:11 | [CVE-2026-102721](https://nvd.nist.gov/vuln/detail/CVE-2026-102721) | Medium | 6.9 | A TFTP server that answers with a short ERROR packet makes the client read up to 64 bytes past the received datagram. E… |
| 2026-09-29 18:17:11 | [CVE-2026-102722](https://nvd.nist.gov/vuln/detail/CVE-2026-102722) | Medium | 6.9 | In the IPv4 PASV path, the FTP Client accepts whatever address was sent in the server's `227` reply. Validation only co… |
| 2026-09-29 18:17:11 | [CVE-2026-102723](https://nvd.nist.gov/vuln/detail/CVE-2026-102723) | Medium | 6.0 | NULL Pointer Dereference on MSRP Attribute Table Exhaustion |
| 2026-09-29 18:17:11 | [CVE-2026-102724](https://nvd.nist.gov/vuln/detail/CVE-2026-102724) | Medium | 6.0 | NULL Pointer Dereference When Evicting the Sole MSRP Attribute |
| 2026-09-29 18:17:12 | [CVE-2026-102725](https://nvd.nist.gov/vuln/detail/CVE-2026-102725) | Medium | 6.0 | Out-of-bounds Read from Unvalidated MSRP Attribute List Length |
| 2026-09-29 18:17:12 | [CVE-2026-102726](https://nvd.nist.gov/vuln/detail/CVE-2026-102726) | Medium | 6.0 | Unbounded PPP IPCP Option Parsing Causes a Worker Stall and Out-of-bounds Read |
| 2026-09-29 18:17:12 | [CVE-2026-102727](https://nvd.nist.gov/vuln/detail/CVE-2026-102727) | Medium | 6.0 | FTP Passive Data Connection Not Bound to the Authenticated Control Peer |
| 2026-09-29 18:17:12 | [CVE-2026-102728](https://nvd.nist.gov/vuln/detail/CVE-2026-102728) |  |  | Two client-side TLS/DTLS handshake parsers in NetX Secure read fields from a server-supplied message before validating… |
| 2026-09-29 18:17:12 | [CVE-2026-102729](https://nvd.nist.gov/vuln/detail/CVE-2026-102729) | Medium | 5.9 | `gx_binres_theme_load()` sizes its theme buffer for the theme it was asked for, and allocates it even when the resource… |
| 2026-09-29 18:17:12 | [CVE-2026-102730](https://nvd.nist.gov/vuln/detail/CVE-2026-102730) | High | 8.6 | Mounting an attacker-controlled NAND flash image (`lx_nand_flash_open()`) triggers an unbounded out-of-bounds heap **wr… |
| 2026-09-29 18:17:12 | [CVE-2026-102757](https://nvd.nist.gov/vuln/detail/CVE-2026-102757) | High | 8.5 | An unprivileged, memory-protected ThreadX module can have the kernel read and write memory at addresses of its choosing… |
| 2026-09-29 18:17:13 | [CVE-2026-102758](https://nvd.nist.gov/vuln/detail/CVE-2026-102758) |  |  | The `_nx_secure_x509_asn1_tlv_block_parse()` function parses ASN.1 TLV (tag-length-value) blocks out of DER-encoded dat… |
| 2026-09-29 18:17:13 | [CVE-2026-102759](https://nvd.nist.gov/vuln/detail/CVE-2026-102759) | Medium | 6.3 | NetX Secure TLS accepts an empty application-data record without verifying its message authentication code. In `_nx_sec… |
| 2026-09-29 18:17:13 | [CVE-2026-102760](https://nvd.nist.gov/vuln/detail/CVE-2026-102760) | High | 8.3 | When NetX Secure is built with `NX_SECURE_KEY_CLEAR`, every TLS record sent on an active session is wiped after it has… |
| 2026-09-29 18:17:13 | [CVE-2026-102761](https://nvd.nist.gov/vuln/detail/CVE-2026-102761) | Critical | 9.3 | NetX Duo's WebSocket client resets the unmasking cursor to the first `NX_PACKET` each time it advances through a chaine… |
| 2026-09-29 18:17:13 | [CVE-2026-102762](https://nvd.nist.gov/vuln/detail/CVE-2026-102762) | High | 8.2 | The NetX Duo MQTT client leaks the packet carrying a malformed PUBLISH message. Each malformed PUBLISH costs one packet… |
| 2026-09-29 18:17:13 | [CVE-2026-102806](https://nvd.nist.gov/vuln/detail/CVE-2026-102806) | Medium | 6.0 | OpenClaw before 2026.9.5 contains an incorrect authorization vulnerability in the Gateway's local media root allowlist… |
| 2026-09-29 18:17:13 | [CVE-2026-102807](https://nvd.nist.gov/vuln/detail/CVE-2026-102807) | Medium | 6.0 | OpenClaw before 2026.9.4 contains an incorrect authorization vulnerability in the mcp.app.view method that allows read-… |
| 2026-09-29 18:17:14 | [CVE-2026-102808](https://nvd.nist.gov/vuln/detail/CVE-2026-102808) | High | 7.1 | PX4 Autopilot through 1.17.0 contains a NULL pointer dereference vulnerability in the sd_stress command where the -b by… |
| 2026-09-29 18:17:14 | [CVE-2026-102809](https://nvd.nist.gov/vuln/detail/CVE-2026-102809) | High | 7.1 | PX4 Autopilot through 1.17.0 contains an uncontrolled stack allocation vulnerability in the file2 test command that fai… |
| 2026-09-29 18:17:14 | [CVE-2026-102810](https://nvd.nist.gov/vuln/detail/CVE-2026-102810) | High | 8.7 | Marmite through 0.4.2 contains a path traversal vulnerability in the development server started by --serve that allows… |
| 2026-09-29 18:17:14 | [CVE-2026-102811](https://nvd.nist.gov/vuln/detail/CVE-2026-102811) | High | 8.7 | Marmite through 0.4.2 contains missing authentication in the development server endpoints /__marmite__/content, /__marm… |
| 2026-09-29 18:17:14 | [CVE-2026-12345](https://nvd.nist.gov/vuln/detail/CVE-2026-12345) | Medium | 5.9 | The cleanup of tempfile.TemporaryDirectory is vulnerable to a race condition. An attacker who can modify the tree durin… |
| 2026-09-29 18:17:17 | [CVE-2026-84414](https://nvd.nist.gov/vuln/detail/CVE-2026-84414) | High | 7.8 | IBM i 7.6, 7.5, 7.4, and 7.3 could allow a local authenticated attacker to change the ownership of arbitrary files due… |
| 2026-09-29 18:17:17 | [CVE-2026-84421](https://nvd.nist.gov/vuln/detail/CVE-2026-84421) | High | 8.8 | IBM DataStage on Cloud Pak for Data 5.4.0.0 could allow a remote authenticated attacker to execute arbitrary code due t… |
| 2026-09-29 18:17:17 | [CVE-2026-84422](https://nvd.nist.gov/vuln/detail/CVE-2026-84422) | High | 7.2 | IBM Guardium Data Protection 12.2 is vulnerable to command injection in the CLI certificate SMIME recipient deletion fu… |
| 2026-09-29 18:17:17 | [CVE-2026-84436](https://nvd.nist.gov/vuln/detail/CVE-2026-84436) | Critical | 9.1 | IBM Guardium Data Protection 12.2 is vulnerable to command injection in the certificate export CLI functionality, allow… |
| 2026-09-29 18:17:17 | [CVE-2026-84440](https://nvd.nist.gov/vuln/detail/CVE-2026-84440) | High | 7.5 | IBM Guardium Data Protection 12.2 is vulnerable to command injection in the SNMP alert notification functionality. An a… |
| 2026-09-29 18:17:18 | [CVE-2026-84842](https://nvd.nist.gov/vuln/detail/CVE-2026-84842) | High | 8.1 | IBM Guardium Data Protection 12.2 is vulnerable to path traversal and arbitrary file deletion in the Datasource REST co… |
| 2026-09-29 18:17:18 | [CVE-2026-94954](https://nvd.nist.gov/vuln/detail/CVE-2026-94954) |  |  | A stack-based buffer overflow vulnerability exists in the web management interface of TOTOLINK N150RT (NTR150) firmware… |
| 2026-09-29 18:17:18 | [CVE-2026-95274](https://nvd.nist.gov/vuln/detail/CVE-2026-95274) |  |  | Improper output encoding in DevTools in Google Chrome prior to 154.0.8037.57 allowed a remote attacker who had compromi… |
| 2026-09-29 18:17:18 | [CVE-2026-95275](https://nvd.nist.gov/vuln/detail/CVE-2026-95275) |  |  | Incorrect reference resolution in MediaStream in Google Chrome prior to 154.0.8037.57 allowed a remote attacker to bypa… |
| 2026-09-29 18:17:18 | [CVE-2026-95276](https://nvd.nist.gov/vuln/detail/CVE-2026-95276) |  |  | Improper input validation in Themes in Google Chrome prior to 154.0.8037.57 allowed a remote attacker who had compromis… |
| 2026-09-29 18:17:19 | [CVE-2026-95277](https://nvd.nist.gov/vuln/detail/CVE-2026-95277) |  |  | Use after free in Views in Google Chrome prior to 154.0.8037.57 allowed a remote attacker to potentially execute arbitr… |
| 2026-09-29 18:17:19 | [CVE-2026-95278](https://nvd.nist.gov/vuln/detail/CVE-2026-95278) |  |  | Missing authorization in WakeLock in Google Chrome prior to 154.0.8037.57 allowed a remote attacker who had compromised… |
| 2026-09-29 18:17:19 | [CVE-2026-95279](https://nvd.nist.gov/vuln/detail/CVE-2026-95279) |  |  | UI misrepresentation in Omnibox in Google Chrome on on Android prior to 154.0.8037.57 allowed a remote attacker to spoo… |
| 2026-09-29 18:17:19 | [CVE-2026-95280](https://nvd.nist.gov/vuln/detail/CVE-2026-95280) |  |  | Race condition in V8 in Google Chrome prior to 154.0.8037.57 allowed a remote attacker to execute arbitrary code inside… |
| 2026-09-29 18:17:19 | [CVE-2026-95281](https://nvd.nist.gov/vuln/detail/CVE-2026-95281) |  |  | Buffer overflow in ANGLE in Google Chrome on on Android prior to 154.0.8037.57 allowed a remote attacker to execute arb… |
| 2026-09-29 18:17:19 | [CVE-2026-95282](https://nvd.nist.gov/vuln/detail/CVE-2026-95282) |  |  | Use after free in Platform in Google Chrome prior to 154.0.8037.57 allowed a remote attacker to execute arbitrary code… |
| 2026-09-29 18:17:19 | [CVE-2026-95283](https://nvd.nist.gov/vuln/detail/CVE-2026-95283) |  |  | Buffer overflow in Tint in Google Chrome on on Android prior to 154.0.8037.57 allowed a remote attacker to potentially… |
| 2026-09-29 18:17:20 | [CVE-2026-95284](https://nvd.nist.gov/vuln/detail/CVE-2026-95284) |  |  | Buffer overflow in ANGLE in Google Chrome on on Android prior to 154.0.8037.57 allowed a remote attacker to execute arb… |
| 2026-09-29 18:17:20 | [CVE-2026-95285](https://nvd.nist.gov/vuln/detail/CVE-2026-95285) |  |  | Missing authorization in WebView in Google Chrome on on Android prior to 154.0.8037.57 allowed a remote attacker who ha… |
| 2026-09-29 18:17:20 | [CVE-2026-95286](https://nvd.nist.gov/vuln/detail/CVE-2026-95286) |  |  | Type confusion in Bindings in Google Chrome prior to 154.0.8037.57 allowed a remote attacker to execute arbitrary code… |
| 2026-09-29 18:17:20 | [CVE-2026-95287](https://nvd.nist.gov/vuln/detail/CVE-2026-95287) |  |  | Missing authorization in Navigation in Google Chrome prior to 154.0.8037.57 allowed a remote attacker who had compromis… |
| 2026-09-29 18:17:20 | [CVE-2026-95288](https://nvd.nist.gov/vuln/detail/CVE-2026-95288) |  |  | UI misrepresentation in Mobile in Google Chrome on on iOS prior to 154.0.8037.57 allowed a remote attacker to spoof UI… |
| 2026-09-29 18:17:20 | [CVE-2026-95289](https://nvd.nist.gov/vuln/detail/CVE-2026-95289) |  |  | Incorrect authorization in Scroll in Google Chrome prior to 154.0.8037.57 allowed a remote attacker leveraging social e… |
| 2026-09-29 18:17:20 | [CVE-2026-95290](https://nvd.nist.gov/vuln/detail/CVE-2026-95290) |  |  | Missing authorization in NFC in Google Chrome prior to 154.0.8037.57 allowed a remote attacker who had compromised the… |
| 2026-09-29 18:17:20 | [CVE-2026-95291](https://nvd.nist.gov/vuln/detail/CVE-2026-95291) |  |  | UI misrepresentation in SecurityIndicators in Google Chrome on on iOS prior to 154.0.8037.57 allowed a remote attacker… |
| 2026-09-29 18:17:20 | [CVE-2026-95292](https://nvd.nist.gov/vuln/detail/CVE-2026-95292) |  |  | Incorrect authorization in Safebrowsing in Google Chrome prior to 154.0.8037.57 allowed a remote attacker to bypass sys… |
| 2026-09-29 18:17:21 | [CVE-2026-95293](https://nvd.nist.gov/vuln/detail/CVE-2026-95293) |  |  | Uninitialized resource in GPU in Google Chrome prior to 154.0.8037.57 allowed a remote attacker to read memory outside… |
| 2026-09-29 18:17:21 | [CVE-2026-95294](https://nvd.nist.gov/vuln/detail/CVE-2026-95294) |  |  | UI misrepresentation in Browser in Google Chrome prior to 154.0.8037.57 allowed a remote attacker leveraging social eng… |
| 2026-09-29 18:17:21 | [CVE-2026-95295](https://nvd.nist.gov/vuln/detail/CVE-2026-95295) |  |  | Information leak in Mobile in Google Chrome on on iOS prior to 154.0.8037.57 allowed a local attacker to leak sensitive… |
| 2026-09-29 18:17:21 | [CVE-2026-95296](https://nvd.nist.gov/vuln/detail/CVE-2026-95296) |  |  | Missing authorization in Core in Google Chrome on on Mac prior to 154.0.8037.57 allowed a remote attacker leveraging so… |
| 2026-09-29 18:17:21 | [CVE-2026-95297](https://nvd.nist.gov/vuln/detail/CVE-2026-95297) |  |  | Missing authorization in Contextual Tasks in Google Chrome prior to 154.0.8037.57 allowed a remote attacker to bypass w… |
| 2026-09-29 18:17:21 | [CVE-2026-95298](https://nvd.nist.gov/vuln/detail/CVE-2026-95298) |  |  | Use after free in Browser in Google Chrome prior to 154.0.8037.57 allowed a local attacker to potentially execute arbit… |
| 2026-09-29 18:17:21 | [CVE-2026-95299](https://nvd.nist.gov/vuln/detail/CVE-2026-95299) |  |  | Use after free in GPU in Google Chrome prior to 154.0.8037.57 allowed a remote attacker to execute arbitrary code outsi… |
| 2026-09-29 18:17:21 | [CVE-2026-95300](https://nvd.nist.gov/vuln/detail/CVE-2026-95300) |  |  | Missing authorization in DevTools in Google Chrome prior to 154.0.8037.57 allowed a remote attacker leveraging social e… |
| 2026-09-29 18:17:22 | [CVE-2026-95301](https://nvd.nist.gov/vuln/detail/CVE-2026-95301) |  |  | Missing authorization in Extensions in Google Chrome prior to 154.0.8037.57 allowed a remote attacker who had compromis… |
| 2026-09-29 18:17:22 | [CVE-2026-95302](https://nvd.nist.gov/vuln/detail/CVE-2026-95302) |  |  | Incorrect authorization in WebAPKs in Google Chrome on on Android prior to 154.0.8037.57 allowed a local attacker to ob… |
| 2026-09-29 18:17:22 | [CVE-2026-95303](https://nvd.nist.gov/vuln/detail/CVE-2026-95303) |  |  | Incomplete cleanup in SmartCard in Google Chrome prior to 154.0.8037.57 allowed a remote attacker leveraging social eng… |
| 2026-09-29 18:17:22 | [CVE-2026-95304](https://nvd.nist.gov/vuln/detail/CVE-2026-95304) |  |  | Out of bounds write in V8 in Google Chrome prior to 154.0.8037.57 allowed a remote attacker to execute arbitrary code i… |
| 2026-09-29 18:17:22 | [CVE-2026-95305](https://nvd.nist.gov/vuln/detail/CVE-2026-95305) |  |  | UI misrepresentation in Chromoting in Google Chrome prior to 154.0.8037.57 allowed a remote attacker leveraging social… |
| 2026-09-29 18:17:22 | [CVE-2026-95306](https://nvd.nist.gov/vuln/detail/CVE-2026-95306) |  |  | Type confusion in V8 in Google Chrome prior to 154.0.8037.57 allowed a remote attacker to execute arbitrary code inside… |
| 2026-09-29 18:17:22 | [CVE-2026-95307](https://nvd.nist.gov/vuln/detail/CVE-2026-95307) |  |  | UI misrepresentation in ExtensionsMenu in Google Chrome prior to 154.0.8037.57 allowed a remote attacker leveraging soc… |
| 2026-09-29 18:17:22 | [CVE-2026-95308](https://nvd.nist.gov/vuln/detail/CVE-2026-95308) |  |  | Integer overflow in Metrics in Google Chrome prior to 154.0.8037.57 allowed a remote attacker who had compromised the r… |
| 2026-09-29 18:17:23 | [CVE-2026-95310](https://nvd.nist.gov/vuln/detail/CVE-2026-95310) |  |  | Use after free in AdFilter in Google Chrome prior to 154.0.8037.57 allowed a remote attacker to execute arbitrary code… |
| 2026-09-29 18:17:23 | [CVE-2026-95311](https://nvd.nist.gov/vuln/detail/CVE-2026-95311) |  |  | Free of non-heap memory in Fonts in Google Chrome prior to 154.0.8037.57 allowed a remote attacker leveraging social en… |
| 2026-09-29 18:17:23 | [CVE-2026-95312](https://nvd.nist.gov/vuln/detail/CVE-2026-95312) |  |  | Information leak in Passwords in Google Chrome prior to 154.0.8037.57 allowed a remote attacker who had compromised the… |
| 2026-09-29 18:17:23 | [CVE-2026-95313](https://nvd.nist.gov/vuln/detail/CVE-2026-95313) |  |  | Use after free in Fullscreen in Google Chrome prior to 154.0.8037.57 allowed a remote attacker to potentially execute a… |
| 2026-09-29 18:17:23 | [CVE-2026-95314](https://nvd.nist.gov/vuln/detail/CVE-2026-95314) |  |  | Incorrect authorization in HID in Google Chrome prior to 154.0.8037.57 allowed a remote attacker who had compromised th… |
| 2026-09-29 18:17:23 | [CVE-2026-95315](https://nvd.nist.gov/vuln/detail/CVE-2026-95315) |  |  | Use after free in Aura in Google Chrome prior to 154.0.8037.57 allowed a local attacker to potentially execute arbitrar… |
| 2026-09-29 18:17:23 | [CVE-2026-95316](https://nvd.nist.gov/vuln/detail/CVE-2026-95316) |  |  | Unchecked return value in Performance in Google Chrome prior to 154.0.8037.57 allowed a local attacker to potentially r… |
| 2026-09-29 18:17:23 | [CVE-2026-95317](https://nvd.nist.gov/vuln/detail/CVE-2026-95317) |  |  | Incorrect authorization in MediaCapture in Google Chrome prior to 154.0.8037.57 allowed a remote attacker leveraging so… |
| 2026-09-29 18:17:23 | [CVE-2026-95309](https://nvd.nist.gov/vuln/detail/CVE-2026-95309) |  |  | UI misrepresentation in Mobile in Google Chrome on on iOS prior to 154.0.8037.57 allowed a remote attacker to spoof UI… |
| 2026-09-29 18:17:24 | [CVE-2026-95318](https://nvd.nist.gov/vuln/detail/CVE-2026-95318) |  |  | Buffer overflow in Video in Google Chrome prior to 154.0.8037.57 allowed a remote attacker to potentially execute arbit… |
| 2026-09-29 18:17:24 | [CVE-2026-95319](https://nvd.nist.gov/vuln/detail/CVE-2026-95319) |  |  | Use after free in Printing in Google Chrome prior to 154.0.8037.57 allowed a remote attacker who had compromised the re… |
| 2026-09-29 18:17:24 | [CVE-2026-95320](https://nvd.nist.gov/vuln/detail/CVE-2026-95320) |  |  | Missing authorization in Navigation in Google Chrome prior to 154.0.8037.57 allowed a remote attacker who had compromis… |
| 2026-09-29 18:17:24 | [CVE-2026-95321](https://nvd.nist.gov/vuln/detail/CVE-2026-95321) |  |  | UI misrepresentation in Payments in Google Chrome on on Android prior to 154.0.8037.57 allowed a remote attacker to spo… |
| 2026-09-29 18:17:24 | [CVE-2026-95322](https://nvd.nist.gov/vuln/detail/CVE-2026-95322) |  |  | Out of bounds write in GPU in Google Chrome on on Android prior to 154.0.8037.57 allowed a remote attacker who had comp… |
| 2026-09-29 18:17:24 | [CVE-2026-95323](https://nvd.nist.gov/vuln/detail/CVE-2026-95323) |  |  | UI misrepresentation in Chromium in Google Chrome on on iOS prior to 154.0.8037.57 allowed a remote attacker leveraging… |
| 2026-09-29 18:17:24 | [CVE-2026-95324](https://nvd.nist.gov/vuln/detail/CVE-2026-95324) |  |  | Uninitialized resource in GPU in Google Chrome prior to 154.0.8037.57 allowed a remote attacker who had compromised the… |
| 2026-09-29 18:17:24 | [CVE-2026-95325](https://nvd.nist.gov/vuln/detail/CVE-2026-95325) |  |  | Use after free in ANGLE in Google Chrome prior to 154.0.8037.57 allowed a remote attacker to potentially execute arbitr… |
| 2026-09-29 18:17:24 | [CVE-2026-95326](https://nvd.nist.gov/vuln/detail/CVE-2026-95326) |  |  | Incomplete cleanup in Bluetooth in Google Chrome prior to 154.0.8037.57 allowed a remote attacker leveraging social eng… |
| 2026-09-29 18:17:25 | [CVE-2026-95327](https://nvd.nist.gov/vuln/detail/CVE-2026-95327) |  |  | Information leak in Networking in Google Chrome prior to 154.0.8037.57 allowed a remote attacker to leak sensitive info… |
| 2026-09-29 18:17:25 | [CVE-2026-95328](https://nvd.nist.gov/vuln/detail/CVE-2026-95328) |  |  | Confused deputy in Mobile in Google Chrome on on Android prior to 154.0.8037.57 allowed a local attacker leveraging soc… |
| 2026-09-29 18:17:25 | [CVE-2026-95329](https://nvd.nist.gov/vuln/detail/CVE-2026-95329) |  |  | Out of bounds write in WebGL in Google Chrome on on Android prior to 154.0.8037.57 allowed a remote attacker to potenti… |
| 2026-09-29 18:17:25 | [CVE-2026-95330](https://nvd.nist.gov/vuln/detail/CVE-2026-95330) |  |  | Improper state validation in Downloads in Google Chrome prior to 154.0.8037.57 allowed a remote attacker to bypass syst… |
| 2026-09-29 18:17:25 | [CVE-2026-95331](https://nvd.nist.gov/vuln/detail/CVE-2026-95331) |  |  | Out of bounds write in ANGLE in Google Chrome prior to 154.0.8037.57 allowed a remote attacker to potentially execute a… |
| 2026-09-29 18:17:25 | [CVE-2026-95332](https://nvd.nist.gov/vuln/detail/CVE-2026-95332) |  |  | Use of uninitialized variable in Tint in Google Chrome on on Android prior to 154.0.8037.57 allowed a remote attacker t… |
| 2026-09-29 18:17:25 | [CVE-2026-95333](https://nvd.nist.gov/vuln/detail/CVE-2026-95333) |  |  | Use after free in Metrics in Google Chrome prior to 154.0.8037.57 allowed a remote attacker to execute arbitrary code o… |
| 2026-09-29 18:17:25 | [CVE-2026-95334](https://nvd.nist.gov/vuln/detail/CVE-2026-95334) |  |  | Incorrect reference resolution in WebProtect in Google Chrome prior to 154.0.8037.57 allowed a remote attacker who had… |
| 2026-09-29 18:17:26 | [CVE-2026-95335](https://nvd.nist.gov/vuln/detail/CVE-2026-95335) |  |  | Use after free in HID in Google Chrome prior to 154.0.8037.57 allowed a remote attacker who had compromised the rendere… |
| 2026-09-29 18:17:26 | [CVE-2026-95336](https://nvd.nist.gov/vuln/detail/CVE-2026-95336) |  |  | Information leak in Transactions Platform in Google Chrome prior to 154.0.8037.57 allowed a remote attacker leveraging… |
| 2026-09-29 18:17:26 | [CVE-2026-95337](https://nvd.nist.gov/vuln/detail/CVE-2026-95337) |  |  | UI misrepresentation in Messages in Google Chrome on on Android prior to 154.0.8037.57 allowed a remote attacker levera… |
| 2026-09-29 18:17:26 | [CVE-2026-95338](https://nvd.nist.gov/vuln/detail/CVE-2026-95338) |  |  | Use after free in PDFium in Google Chrome prior to 154.0.8037.57 allowed a remote attacker to execute arbitrary code in… |
| 2026-09-29 18:17:26 | [CVE-2026-95339](https://nvd.nist.gov/vuln/detail/CVE-2026-95339) | Critical | 9.6 | Use after free in ServiceWorker in Google Chrome prior to 154.0.8037.57 allowed a remote attacker to execute arbitrary… |
| 2026-09-29 18:17:26 | [CVE-2026-95340](https://nvd.nist.gov/vuln/detail/CVE-2026-95340) |  |  | Incorrect authorization in PictureInPicture in Google Chrome prior to 154.0.8037.57 allowed a remote attacker leveragin… |
| 2026-09-29 18:17:26 | [CVE-2026-95341](https://nvd.nist.gov/vuln/detail/CVE-2026-95341) |  |  | Improper input validation in Desktop in Google Chrome prior to 154.0.8037.57 allowed a remote attacker who had compromi… |
| 2026-09-29 18:17:26 | [CVE-2026-95342](https://nvd.nist.gov/vuln/detail/CVE-2026-95342) |  |  | Missing authorization in V8 in Google Chrome prior to 154.0.8037.57 allowed a remote attacker to bypass web origin poli… |
| 2026-09-29 18:17:27 | [CVE-2026-95343](https://nvd.nist.gov/vuln/detail/CVE-2026-95343) |  |  | Use after free in WebAudio in Google Chrome prior to 154.0.8037.57 allowed a remote attacker to execute arbitrary code… |
| 2026-09-29 18:17:27 | [CVE-2026-95344](https://nvd.nist.gov/vuln/detail/CVE-2026-95344) |  |  | Race condition in DevTools in Google Chrome prior to 154.0.8037.57 allowed a remote attacker leveraging social engineer… |
| 2026-09-29 18:17:27 | [CVE-2026-95345](https://nvd.nist.gov/vuln/detail/CVE-2026-95345) |  |  | Use after free in Actor in Google Chrome prior to 154.0.8037.57 allowed a remote attacker to execute arbitrary code ins… |
| 2026-09-29 18:17:27 | [CVE-2026-95346](https://nvd.nist.gov/vuln/detail/CVE-2026-95346) |  |  | UI misrepresentation in Chromoting in Google Chrome prior to 154.0.8037.57 allowed a remote attacker to spoof UI elemen… |
| 2026-09-29 18:17:27 | [CVE-2026-95347](https://nvd.nist.gov/vuln/detail/CVE-2026-95347) |  |  | Use after free in Updater in Google Chrome on on Mac prior to 154.0.8037.57 allowed a remote attacker to execute arbitr… |
| 2026-09-29 18:17:27 | [CVE-2026-95348](https://nvd.nist.gov/vuln/detail/CVE-2026-95348) |  |  | Use after free in Bluetooth in Google Chrome prior to 154.0.8037.57 allowed a remote attacker who had compromised the r… |
| 2026-09-29 18:17:27 | [CVE-2026-95349](https://nvd.nist.gov/vuln/detail/CVE-2026-95349) |  |  | Buffer overflow in WebGL in Google Chrome on on Android prior to 154.0.8037.57 allowed a remote attacker to potentially… |
| 2026-09-29 18:17:27 | [CVE-2026-95350](https://nvd.nist.gov/vuln/detail/CVE-2026-95350) | Critical | 9.6 | Buffer overflow in ANGLE in Google Chrome on on Android prior to 154.0.8037.57 allowed a remote attacker to execute arb… |
| 2026-09-29 18:17:28 | [CVE-2026-95351](https://nvd.nist.gov/vuln/detail/CVE-2026-95351) |  |  | Use after free in Views in Google Chrome prior to 154.0.8037.57 allowed a remote attacker who had compromised the rende… |
| 2026-09-29 18:17:28 | [CVE-2026-95352](https://nvd.nist.gov/vuln/detail/CVE-2026-95352) |  |  | Incorrect authorization in DevTools in Google Chrome prior to 154.0.8037.57 allowed a remote attacker leveraging social… |
| 2026-09-29 18:17:28 | [CVE-2026-95353](https://nvd.nist.gov/vuln/detail/CVE-2026-95353) |  |  | Use after free in Bindings in Google Chrome prior to 154.0.8037.57 allowed a remote attacker to execute arbitrary code… |
| 2026-09-29 18:17:28 | [CVE-2026-95354](https://nvd.nist.gov/vuln/detail/CVE-2026-95354) |  |  | Use after free in Verifier in Google Chrome prior to 154.0.8037.57 allowed a remote attacker who had compromised the re… |
| 2026-09-29 18:17:28 | [CVE-2026-95355](https://nvd.nist.gov/vuln/detail/CVE-2026-95355) |  |  | Incorrect authorization in Navigation in Google Chrome on on iOS prior to 154.0.8037.57 allowed a remote attacker who h… |
| 2026-09-29 18:17:28 | [CVE-2026-95356](https://nvd.nist.gov/vuln/detail/CVE-2026-95356) |  |  | Use after free in WindowDialog in Google Chrome prior to 154.0.8037.57 allowed a remote attacker leveraging social engi… |
| 2026-09-29 18:17:28 | [CVE-2026-95357](https://nvd.nist.gov/vuln/detail/CVE-2026-95357) | Critical | 9.6 | Out of bounds write in GPU in Google Chrome on on Android prior to 154.0.8037.57 allowed a remote attacker to potential… |
| 2026-09-29 18:17:28 | [CVE-2026-95358](https://nvd.nist.gov/vuln/detail/CVE-2026-95358) |  |  | Incorrect authorization in Mobile in Google Chrome on on Android prior to 154.0.8037.57 allowed a local attacker to byp… |
| 2026-09-29 18:17:29 | [CVE-2026-95359](https://nvd.nist.gov/vuln/detail/CVE-2026-95359) |  |  | Uninitialized resource in GPU in Google Chrome on on Android prior to 154.0.8037.57 allowed a remote attacker who had c… |
| 2026-09-29 18:17:29 | [CVE-2026-95360](https://nvd.nist.gov/vuln/detail/CVE-2026-95360) |  |  | Race condition in Editing in Google Chrome prior to 154.0.8037.57 allowed a remote attacker leveraging social engineeri… |
| 2026-09-29 18:17:29 | [CVE-2026-95361](https://nvd.nist.gov/vuln/detail/CVE-2026-95361) |  |  | Confused deputy in DevTools in Google Chrome prior to 154.0.8037.57 allowed a remote attacker leveraging social enginee… |
| 2026-09-29 18:17:29 | [CVE-2026-95362](https://nvd.nist.gov/vuln/detail/CVE-2026-95362) |  |  | Cross-site request forgery in DevTools in Google Chrome prior to 154.0.8037.57 allowed a remote attacker leveraging soc… |
| 2026-09-29 18:17:29 | [CVE-2026-95363](https://nvd.nist.gov/vuln/detail/CVE-2026-95363) |  |  | UI misrepresentation in FileSystem in Google Chrome prior to 154.0.8037.57 allowed a remote attacker leveraging social… |
| 2026-09-29 18:17:30 | [CVE-2026-95364](https://nvd.nist.gov/vuln/detail/CVE-2026-95364) |  |  | Improper input validation in Passwords in Google Chrome prior to 154.0.8037.57 allowed a remote attacker to spoof UI el… |
| 2026-09-29 18:17:30 | [CVE-2026-95365](https://nvd.nist.gov/vuln/detail/CVE-2026-95365) |  |  | Type confusion in IndexedDB in Google Chrome prior to 154.0.8037.57 allowed a remote attacker to potentially execute ar… |
| 2026-09-29 18:17:30 | [CVE-2026-95366](https://nvd.nist.gov/vuln/detail/CVE-2026-95366) |  |  | Use of released resource in Core in Google Chrome prior to 154.0.8037.57 allowed a remote attacker who had compromised… |
| 2026-09-29 18:17:30 | [CVE-2026-95367](https://nvd.nist.gov/vuln/detail/CVE-2026-95367) |  |  | Information leak in DataTransfer in Google Chrome prior to 154.0.8037.57 allowed a remote attacker who had compromised… |
| 2026-09-29 18:17:30 | [CVE-2026-95368](https://nvd.nist.gov/vuln/detail/CVE-2026-95368) |  |  | Incorrect authorization in DevTools in Google Chrome prior to 154.0.8037.57 allowed a remote attacker leveraging social… |
| 2026-09-29 18:17:30 | [CVE-2026-95369](https://nvd.nist.gov/vuln/detail/CVE-2026-95369) |  |  | Inappropriate implementation in XML in Google Chrome prior to 154.0.8037.57 allowed a remote attacker to potentially ex… |
| 2026-09-29 18:17:30 | [CVE-2026-95370](https://nvd.nist.gov/vuln/detail/CVE-2026-95370) |  |  | Inappropriate implementation in NFC in Google Chrome prior to 154.0.8037.57 allowed a remote attacker to bypass system… |
| 2026-09-29 18:17:31 | [CVE-2026-95371](https://nvd.nist.gov/vuln/detail/CVE-2026-95371) |  |  | Missing authorization in Views in Google Chrome on on Mac prior to 154.0.8037.57 allowed a remote attacker who had comp… |
| 2026-09-29 18:17:31 | [CVE-2026-95372](https://nvd.nist.gov/vuln/detail/CVE-2026-95372) |  |  | Use after free in Chromecast in Google Chrome prior to 154.0.8037.57 allowed a remote attacker who had compromised the… |
| 2026-09-29 18:17:31 | [CVE-2026-95373](https://nvd.nist.gov/vuln/detail/CVE-2026-95373) |  |  | Use after free in DevTools in Google Chrome prior to 154.0.8037.57 allowed a remote attacker leveraging social engineer… |
| 2026-09-29 18:17:31 | [CVE-2026-95374](https://nvd.nist.gov/vuln/detail/CVE-2026-95374) |  |  | Incorrect authorization in Network in Google Chrome prior to 154.0.8037.57 allowed a remote attacker to bypass web orig… |
| 2026-09-29 18:17:31 | [CVE-2026-95375](https://nvd.nist.gov/vuln/detail/CVE-2026-95375) |  |  | Incorrect authorization in BrowserTag in Google Chrome prior to 154.0.8037.57 allowed a remote attacker who had comprom… |
| 2026-09-29 18:17:31 | [CVE-2026-95376](https://nvd.nist.gov/vuln/detail/CVE-2026-95376) |  |  | Externally controlled reference in DevTools in Google Chrome prior to 154.0.8037.57 allowed an adjacent attacker levera… |
| 2026-09-29 18:17:31 | [CVE-2026-95380](https://nvd.nist.gov/vuln/detail/CVE-2026-95380) |  |  | Type confusion in V8 in Google Chrome prior to 154.0.8037.57 allowed a remote attacker leveraging social engineering to… |
| 2026-09-29 18:17:31 | [CVE-2026-95381](https://nvd.nist.gov/vuln/detail/CVE-2026-95381) |  |  | Improper input validation in Printing in Google Chrome prior to 154.0.8037.57 allowed a remote attacker who had comprom… |
| 2026-09-29 18:17:32 | [CVE-2026-95384](https://nvd.nist.gov/vuln/detail/CVE-2026-95384) |  |  | Race condition in Transactions Platform in Google Chrome prior to 154.0.8037.57 allowed a remote attacker to potentiall… |
| 2026-09-29 18:17:32 | [CVE-2026-95385](https://nvd.nist.gov/vuln/detail/CVE-2026-95385) |  |  | Inappropriate implementation in PlatformIntegration in Google Chrome on on Windows prior to 154.0.8037.57 allowed a rem… |
| 2026-09-29 18:17:32 | [CVE-2026-95382](https://nvd.nist.gov/vuln/detail/CVE-2026-95382) |  |  | Improper input validation in Auth in Google Chrome prior to 154.0.8037.57 allowed a remote attacker who had compromised… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
