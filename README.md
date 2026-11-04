# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-11-04 16:18 UTC

New CVEs published between 2026-11-04 15:18 UTC and 2026-11-04 16:18 UTC.

[Full CSV](data/new-cves-2026-11-04T16-18-19-1597Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-11-04 16:17:32 | [CVE-2026-106554](https://nvd.nist.gov/vuln/detail/CVE-2026-106554) |  |  | One CBOR-parsing issue in jackson-dataformats-binary's CBOR module: an unbounded run of CBOR tags drives quadratic-time… |
| 2026-11-04 16:17:33 | [CVE-2026-109518](https://nvd.nist.gov/vuln/detail/CVE-2026-109518) | High | 7.7 | On Debian, Ubuntu, and derivative Linux distributions, an on-path attacker who can manipulate the HTTP traffic (includi… |
| 2026-11-04 16:17:45 | [CVE-2026-119746](https://nvd.nist.gov/vuln/detail/CVE-2026-119746) | High | 8.2 | ProSoft Technology ICX35 devices (X35-HWC-A and ICX35-HWC-E) contain a login lockout bypass in the integrated module we… |
| 2026-11-04 16:17:47 | [CVE-2026-121950](https://nvd.nist.gov/vuln/detail/CVE-2026-121950) | High | 7.1 | FreeRDP before 3.32.2 does not check the product of surface dimensions in gdi_CreateSurface when handling an RDPGFX CRE… |
| 2026-11-04 16:17:47 | [CVE-2026-121951](https://nvd.nist.gov/vuln/detail/CVE-2026-121951) | High | 8.7 | FreeRDP 3.0.0 before 3.32.2 server-side RDP peer input parsing skips the six-byte body of a slow-path input event with… |
| 2026-11-04 16:17:47 | [CVE-2026-121952](https://nvd.nist.gov/vuln/detail/CVE-2026-121952) | Critical | 9.3 | FreeRDP before 3.32.2 has an out-of-bounds write in the proxy because rdp_read_bitmap_cache_v2_capability_set rejects o… |
| 2026-11-04 16:17:47 | [CVE-2026-121953](https://nvd.nist.gov/vuln/detail/CVE-2026-121953) | Critical | 9.3 | FreeRDP before 3.32.2 has a use-after-free in the client's rdpgfx dynamic virtual channel: a duplicate-name channel wit… |
| 2026-11-04 16:17:47 | [CVE-2026-121954](https://nvd.nist.gov/vuln/detail/CVE-2026-121954) | High | 7.1 | FreeRDP before 3.32.2 has a heap out-of-bounds write in the planar codec because freerdp_bitmap_planar_context_reset co… |
| 2026-11-04 16:17:48 | [CVE-2026-121955](https://nvd.nist.gov/vuln/detail/CVE-2026-121955) | High | 8.7 | FreeRDP before 3.32.2 contains a use-after-free vulnerability in Emulate_SCardReleaseContext that frees the emulated SC… |
| 2026-11-04 16:17:48 | [CVE-2026-121956](https://nvd.nist.gov/vuln/detail/CVE-2026-121956) | High | 8.7 | FreeRDP before 3.32.2 contains a double free in the WinPR Kerberos SSPI retrieveSomeTgt function, which installs the kr… |
| 2026-11-04 16:17:48 | [CVE-2026-121957](https://nvd.nist.gov/vuln/detail/CVE-2026-121957) | High | 8.7 | FreeRDP before 3.32.2 contains a use-after-free vulnerability that allows malicious RDP servers to corrupt client memor… |
| 2026-11-04 16:17:48 | [CVE-2026-121958](https://nvd.nist.gov/vuln/detail/CVE-2026-121958) | High | 8.7 | FreeRDP through 3.32.1 has a heap out-of-bounds write in the RDPGFX client because the delete_surface callback truncate… |
| 2026-11-04 16:17:48 | [CVE-2026-121959](https://nvd.nist.gov/vuln/detail/CVE-2026-121959) | High | 7.1 | FreeRDP before 3.32.2 contains an infinite loop vulnerability in websocket_context_read that fails to handle a zero BIO… |
| 2026-11-04 16:17:48 | [CVE-2026-121960](https://nvd.nist.gov/vuln/detail/CVE-2026-121960) | High | 8.7 | FreeRDP before 3.32.2 contains a denial of service vulnerability in the NLA-enabled shadow server when a CredSSP TSRequ… |
| 2026-11-04 16:17:49 | [CVE-2026-121961](https://nvd.nist.gov/vuln/detail/CVE-2026-121961) | High | 8.2 | FreeRDP before 3.32.2 contains a use-after-free vulnerability in the freerdp-proxy DRDYNVC tracker when intercepting th… |
| 2026-11-04 16:17:49 | [CVE-2026-121962](https://nvd.nist.gov/vuln/detail/CVE-2026-121962) | High | 7.2 | FreeRDP before 3.32.2 contains a heap buffer overflow in transport_default_read_pdu when handling partial Early User Au… |
| 2026-11-04 16:17:49 | [CVE-2026-121963](https://nvd.nist.gov/vuln/detail/CVE-2026-121963) | High | 8.2 | FreeRDP before 3.32.2 contains a use-after-free vulnerability in the asynchronous dynamic rdpsnd channel that allows ma… |
| 2026-11-04 16:17:49 | [CVE-2026-121964](https://nvd.nist.gov/vuln/detail/CVE-2026-121964) | High | 8.7 | FreeRDP before 3.32.2 contains a heap-based buffer overflow in the RD Gateway RPC client, where rpc_client_recv_fragmen… |
| 2026-11-04 16:17:49 | [CVE-2026-121965](https://nvd.nist.gov/vuln/detail/CVE-2026-121965) | Medium | 6.0 | Parse Server before 8.6.113 and 9.0.0 before 9.10.6-alpha.5 contains a prototype pollution vulnerability when building… |
| 2026-11-04 16:17:50 | [CVE-2026-121966](https://nvd.nist.gov/vuln/detail/CVE-2026-121966) | High | 7.0 | Traefik 2.x before 2.11.60 and 3.x before 3.7.16 sends ForwardAuth subrequests (and, in 3.7, Ingress NGINX auth-url req… |
| 2026-11-04 16:17:50 | [CVE-2026-121967](https://nvd.nist.gov/vuln/detail/CVE-2026-121967) | Low | 2.3 | Coder 2.28.0 before 2.29.22, 2.30.0 before 2.34.13, 2.35.0 before 2.35.10, 2.36.0 before 2.36.8, 2.37.0 before 2.37.5,… |
| 2026-11-04 16:17:50 | [CVE-2026-122032](https://nvd.nist.gov/vuln/detail/CVE-2026-122032) | High | 7.1 | SPIP before 4.4.29 contains a SQL injection vulnerability that allows authenticated attackers with back-office access t… |
| 2026-11-04 16:17:54 | [CVE-2026-91163](https://nvd.nist.gov/vuln/detail/CVE-2026-91163) | Low | 3.7 | Warpgate is an open source SSH, HTTPS, and MySQL bastion host for Linux. Prior to 0.29.0, the Kubernetes protocol liste… |
| 2026-11-04 16:17:54 | [CVE-2026-91168](https://nvd.nist.gov/vuln/detail/CVE-2026-91168) | Medium | 6.8 | Warpgate is an open source SSH, HTTPS, and MySQL bastion host for Linux. From 0.21.0 until 0.29.0, the Kubernetes reque… |
| 2026-11-04 16:17:55 | [CVE-2026-92704](https://nvd.nist.gov/vuln/detail/CVE-2026-92704) | High | 8.3 | SharpEmu is an experimental PlayStation 5 emulator for Windows and Linux. In version 0.0.3-release.3 and earlier, the r… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
