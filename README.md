# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-21 12:20 UTC

New CVEs published between 2026-10-21 11:18 UTC and 2026-10-21 12:20 UTC.

[Full CSV](data/new-cves-2026-10-21T12-20-43-95884Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-10-21 12:17:19 | [CVE-2026-114242](https://nvd.nist.gov/vuln/detail/CVE-2026-114242) | Medium | 5.5 | A vulnerability was identified in dhikshitha29 Insurance-Management-System 91de5edda5baa109ad8e9baf03ce6a3ceda84183/125… |
| 2026-10-21 12:17:20 | [CVE-2026-48830](https://nvd.nist.gov/vuln/detail/CVE-2026-48830) |  |  | Improper authentication in Apache bRPC through 1.17.0 allows a remote unauthenticated attacker to bypass authentication… |
| 2026-10-21 12:17:21 | [CVE-2026-54425](https://nvd.nist.gov/vuln/detail/CVE-2026-54425) |  |  | Uncontrolled recursion in the HTTP/2 HPACK decoder in Apache bRPC before 1.18.0 allows remote attackers to cause denial… |
| 2026-10-21 12:17:21 | [CVE-2026-54426](https://nvd.nist.gov/vuln/detail/CVE-2026-54426) |  |  | Uncontrolled recursion in the Redis reply parser in Apache bRPC < 1.18.0 allows a remote Redis server peer to crash a b… |
| 2026-10-21 12:17:21 | [CVE-2026-54427](https://nvd.nist.gov/vuln/detail/CVE-2026-54427) |  |  | Uncontrolled recursion in the AMF parser in Apache bRPC < 1.18.0 allows a remote RTMP peer to crash a bRPC process by s… |
| 2026-10-21 12:17:21 | [CVE-2026-56386](https://nvd.nist.gov/vuln/detail/CVE-2026-56386) |  |  | Integer underflow and out-of-bounds read in the HTTP/2 server DATA frame parser in Apache bRPC allows an unauthenticate… |
| 2026-10-21 12:17:21 | [CVE-2026-56387](https://nvd.nist.gov/vuln/detail/CVE-2026-56387) |  |  | The RTMP AMF parser in Apache bRPC accepts AMF string lengths and array counts directly from untrusted input. A remote… |
| 2026-10-21 12:17:21 | [CVE-2026-56388](https://nvd.nist.gov/vuln/detail/CVE-2026-56388) |  |  | The Redis server command parser in Apache bRPC accepts an empty RESP array as a command header. A remote unauthenticate… |
| 2026-10-21 12:17:21 | [CVE-2026-58064](https://nvd.nist.gov/vuln/detail/CVE-2026-58064) |  |  | The Redis protocol implementation in Apache bRPC allowed inline command parsing to allocate and copy the full connectio… |
| 2026-10-21 12:17:21 | [CVE-2026-59229](https://nvd.nist.gov/vuln/detail/CVE-2026-59229) |  |  | The Legacy Pipe receiver protocol (handshake / sendPipeData) uses a hardcoded SUPER_USER (root) identity when executing… |
| 2026-10-21 12:17:22 | [CVE-2026-59562](https://nvd.nist.gov/vuln/detail/CVE-2026-59562) |  |  | Missing authentication for critical function vulnerability in Apache IoTDB. This issue affects Apache IoTDB: from 2.0.0… |
| 2026-10-21 12:17:22 | [CVE-2026-61902](https://nvd.nist.gov/vuln/detail/CVE-2026-61902) |  |  | Apache bRPC versions before 1.18.0 do not consistently enforce the configured max_body_size limit in non-progressive HT… |
| 2026-10-21 12:17:22 | [CVE-2026-61916](https://nvd.nist.gov/vuln/detail/CVE-2026-61916) |  |  | Out-of-bounds reads in URL parsing and case-insensitive header lookup in Apache bRPC before version 1.18.0 on platforms… |
| 2026-10-21 12:17:22 | [CVE-2026-66392](https://nvd.nist.gov/vuln/detail/CVE-2026-66392) |  |  | Apache bRPC versions before 1.18.0 validate the server certificate chain when client TLS peer verification is enabled,… |
| 2026-10-21 12:17:22 | [CVE-2026-74755](https://nvd.nist.gov/vuln/detail/CVE-2026-74755) |  |  | An integer underflow in the mcpack2pb component of Apache bRPC (version < 1.18.0) on all platforms allows remote attack… |
| 2026-10-21 12:17:22 | [CVE-2026-74757](https://nvd.nist.gov/vuln/detail/CVE-2026-74757) |  |  | Uncontrolled resource allocation in the mcpack2pb component in Apache bRPC (version < 1.18.0) on all platforms allows r… |
| 2026-10-21 12:17:22 | [CVE-2026-74758](https://nvd.nist.gov/vuln/detail/CVE-2026-74758) |  |  | A heap use-after-free in the RTMP protocol component of Apache bRPC (versions < 1.18.0) allows a remote attacker to cra… |
| 2026-10-21 12:17:23 | [CVE-2026-78048](https://nvd.nist.gov/vuln/detail/CVE-2026-78048) |  |  | A reachable-assertion flaw in the HPACK header-compression decoder of the HTTP/2 (h2/gRPC) stack in Apache bRPC (versio… |
| 2026-10-21 12:17:23 | [CVE-2026-78058](https://nvd.nist.gov/vuln/detail/CVE-2026-78058) |  |  | Uncontrolled resource consumption in the HTTP/2 (h2) receive path of Apache bRPC (version < 1.18.0) on all platforms al… |
| 2026-10-21 12:17:23 | [CVE-2026-78066](https://nvd.nist.gov/vuln/detail/CVE-2026-78066) |  |  | Resource exhaustion in Apache bRPC (version < 1.18.0) on all platforms: multiple parsers that accept wire-controlled in… |
| 2026-10-21 12:17:23 | [CVE-2026-78334](https://nvd.nist.gov/vuln/detail/CVE-2026-78334) |  |  | Missing authentication in the streaming RPC path of Apache bRPC (version < 1.18.0) on all platforms allows a remote att… |
| 2026-10-21 12:17:23 | [CVE-2026-79704](https://nvd.nist.gov/vuln/detail/CVE-2026-79704) |  |  | An out-of-bounds read vulnerability exists in the streaming RPC client of Apache bRPC (versions 1.11.0 through 1.17.0)… |
| 2026-10-21 12:17:24 | [CVE-2026-80463](https://nvd.nist.gov/vuln/detail/CVE-2026-80463) |  |  | Unbounded memory accumulation in the stream message reassembly path of Apache bRPC (version < 1.18.0) on all platforms… |
| 2026-10-21 12:17:24 | [CVE-2026-81755](https://nvd.nist.gov/vuln/detail/CVE-2026-81755) |  |  | Uncontrolled resource consumption in the streaming RPC component of Apache bRPC (version < 1.18.0) allows a remote atta… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
