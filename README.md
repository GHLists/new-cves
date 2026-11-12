# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-11-12 20:20 UTC

New CVEs published between 2026-11-12 19:21 UTC and 2026-11-12 20:20 UTC.

[Full CSV](data/new-cves-2026-11-12T20-20-49-263493Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-11-12 20:18:09 | [CVE-2024-21963](https://nvd.nist.gov/vuln/detail/CVE-2024-21963) | Medium | 6.0 | An out-of-bounds read vulnerability in the IOMMU could allow a malicious guest to corrupt hypervisor (HV) pages and pot… |
| 2026-11-12 20:18:12 | [CVE-2024-36344](https://nvd.nist.gov/vuln/detail/CVE-2024-36344) | Medium | 6.9 | Insufficient parameter sanitization in AMD Secure Processor (ASP) TEE DrvSys could allow an attacker with local access… |
| 2026-11-12 20:18:13 | [CVE-2025-0043](https://nvd.nist.gov/vuln/detail/CVE-2025-0043) | High | 7.0 | Incorrect directory permissions within AMD Vivado™ Lab Solutions could allow a local user-privileged attacker to escala… |
| 2026-11-12 20:18:14 | [CVE-2025-54507](https://nvd.nist.gov/vuln/detail/CVE-2025-54507) | Medium | 5.9 | Improper validation of consistency within input in AMD SEV (Secure Encrypted Virtualization) firmware could allow an at… |
| 2026-11-12 20:18:14 | [CVE-2026-0455](https://nvd.nist.gov/vuln/detail/CVE-2026-0455) | Medium | 5.9 | The Versal™ AI Edge Series Gen 2 Peripheral Protection Unit (XPPU) for the inter-processor interrupt (IPI) buffers does… |
| 2026-11-12 20:18:14 | [CVE-2026-0460](https://nvd.nist.gov/vuln/detail/CVE-2026-0460) | Low | 1.0 | Improper authentication in Bootgen could result in the use of a fixed salt value for RSA padding instead of a randomly… |
| 2026-11-12 20:18:14 | [CVE-2026-107152](https://nvd.nist.gov/vuln/detail/CVE-2026-107152) | High | 7.1 | An improper authentication vulnerability has been found in the task console in the smart_proxy_dynflow package. The con… |
| 2026-11-12 20:18:14 | [CVE-2026-107360](https://nvd.nist.gov/vuln/detail/CVE-2026-107360) | Critical | 9.6 | A flaw was found in rubygem-safemode. Compound assignment expressions in sandboxed code are evaluated without mediating… |
| 2026-11-12 20:18:15 | [CVE-2026-107443](https://nvd.nist.gov/vuln/detail/CVE-2026-107443) | High | 7.7 | A flaw was found in Foreman. An authenticated user with view_hosts privileges can retrieve rendered provisioning templa… |
| 2026-11-12 20:18:16 | [CVE-2026-111456](https://nvd.nist.gov/vuln/detail/CVE-2026-111456) | High | 7.1 | A missing authorization check has been found in ConsumerResource.setupOwner() function of consumer registration module… |
| 2026-11-12 20:18:21 | [CVE-2026-124002](https://nvd.nist.gov/vuln/detail/CVE-2026-124002) | Critical | 9.3 | XWEB EVO versions 5.2.3 through before 5.7.0 contains a pre-authentication OS command injection vulnerability that allo… |
| 2026-11-12 20:18:21 | [CVE-2026-124003](https://nvd.nist.gov/vuln/detail/CVE-2026-124003) | High | 8.5 | XWEB EVO before 5.6.2 contains a command injection vulnerability where the setuid-root Lua CGI interpreter wlua execute… |
| 2026-11-12 20:18:22 | [CVE-2026-124004](https://nvd.nist.gov/vuln/detail/CVE-2026-124004) | Critical | 9.3 | XWEB EVO before 5.6.2 contains a hardcoded backdoor password vulnerability that allows unauthenticated remote attackers… |
| 2026-11-12 20:18:22 | [CVE-2026-124005](https://nvd.nist.gov/vuln/detail/CVE-2026-124005) | Critical | 9.2 | XWEB EVO 4.3.0 through 5.8.8 contains a weak password generation vulnerability that allows remote attackers to derive t… |
| 2026-11-12 20:18:23 | [CVE-2026-124006](https://nvd.nist.gov/vuln/detail/CVE-2026-124006) | Critical | 9.2 | XWEB EVO through 5.8.8 contains a predictable credential generation vulnerability that allows attackers to derive the L… |
| 2026-11-12 20:18:23 | [CVE-2026-124007](https://nvd.nist.gov/vuln/detail/CVE-2026-124007) | Critical | 9.2 | XWEB EVO before 5.6.2 contains a pre-authentication OS command injection vulnerability that allows unauthenticated remo… |
| 2026-11-12 20:18:23 | [CVE-2026-124008](https://nvd.nist.gov/vuln/detail/CVE-2026-124008) | High | 8.6 | XWEB EVO 5.2.3 through 5.8.8 contains an authenticated OS command injection vulnerability in the devices.lua template h… |
| 2026-11-12 20:18:23 | [CVE-2026-124009](https://nvd.nist.gov/vuln/detail/CVE-2026-124009) | High | 8.6 | XWEB EVO 5.2.3 through 5.8.8 contains an authenticated OS command injection vulnerability that allows authenticated att… |
| 2026-11-12 20:18:24 | [CVE-2026-124010](https://nvd.nist.gov/vuln/detail/CVE-2026-124010) | Critical | 9.3 | XWEB EVO before 5.6.2 contains a command injection vulnerability that allows unauthenticated remote attackers to execut… |
| 2026-11-12 20:18:24 | [CVE-2026-124011](https://nvd.nist.gov/vuln/detail/CVE-2026-124011) | Medium | 6.9 | XWEB EVO 5.6.2 through 5.8.8 contains an information disclosure vulnerability that allows unauthenticated attackers to… |
| 2026-11-12 20:18:24 | [CVE-2026-124012](https://nvd.nist.gov/vuln/detail/CVE-2026-124012) | Critical | 9.2 | XWEB EVO 5.6.2 through 5.8.8 contains a hardcoded credential vulnerability where the Administrator web account is confi… |
| 2026-11-12 20:18:25 | [CVE-2026-124013](https://nvd.nist.gov/vuln/detail/CVE-2026-124013) | High | 8.7 | XWEB EVO 5.6.2 through 5.8.8 contains an authenticated OS command injection vulnerability in the api.lua import_preconf… |
| 2026-11-12 20:18:25 | [CVE-2026-124014](https://nvd.nist.gov/vuln/detail/CVE-2026-124014) | High | 8.8 | XWEB EVO 4.3.0 through 5.8.8 contains an unauthenticated arbitrary file write vulnerability that allows remote attacker… |
| 2026-11-12 20:18:26 | [CVE-2026-124015](https://nvd.nist.gov/vuln/detail/CVE-2026-124015) | High | 8.2 | XWEB EVO 5.6.2 through 5.8.8 contains an authentication bypass vulnerability that allows unauthenticated attackers to s… |
| 2026-11-12 20:18:34 | [CVE-2026-127120](https://nvd.nist.gov/vuln/detail/CVE-2026-127120) | Medium | 5.3 | A vulnerability was found in Governikus AusweisApp Mobile up to 2.5.5. This impacts an unknown function of the componen… |
| 2026-11-12 20:18:38 | [CVE-2026-45265](https://nvd.nist.gov/vuln/detail/CVE-2026-45265) | High | 8.2 | BACnet Stack is a BACnet open source protocol stack C library for embedded systems. Prior to versions 1.4.4 and 1.5.1,… |
| 2026-11-12 20:18:38 | [CVE-2026-45341](https://nvd.nist.gov/vuln/detail/CVE-2026-45341) | High | 7.5 | BACnet Stack is a BACnet open source protocol stack C library for embedded systems. From versions 1.4.0 to before 1.4.4… |
| 2026-11-12 20:18:39 | [CVE-2026-46674](https://nvd.nist.gov/vuln/detail/CVE-2026-46674) | High | 7.5 | BACnet Stack is a BACnet open source protocol stack C library for embedded systems. Prior to versions 1.4.4 and 1.5.1,… |
| 2026-11-12 20:18:39 | [CVE-2026-46676](https://nvd.nist.gov/vuln/detail/CVE-2026-46676) | Medium | 5.3 | BACnet Stack is a BACnet open source protocol stack C library for embedded systems. From versions 1.4.0 to before 1.4.4… |
| 2026-11-12 20:18:39 | [CVE-2026-46677](https://nvd.nist.gov/vuln/detail/CVE-2026-46677) | Medium | 6.5 | BACnet Stack is a BACnet open source protocol stack C library for embedded systems. Prior to versions 1.4.4 and 1.5.1,… |
| 2026-11-12 20:18:39 | [CVE-2026-47217](https://nvd.nist.gov/vuln/detail/CVE-2026-47217) | High | 7.5 | BACnet Stack is a BACnet open source protocol stack C library for embedded systems. Prior to versions 1.4.4 and 1.5.1,… |
| 2026-11-12 20:18:40 | [CVE-2026-47257](https://nvd.nist.gov/vuln/detail/CVE-2026-47257) | High | 8.1 | BACnet Stack is a BACnet open source protocol stack C library for embedded systems. In versions 1.5.0 and 1.6.0-rc1, th… |
| 2026-11-12 20:18:40 | [CVE-2026-47258](https://nvd.nist.gov/vuln/detail/CVE-2026-47258) | High | 8.2 | BACnet Stack is a BACnet open source protocol stack C library for embedded systems. Prior to versions 1.4.4, 1.5.1, and… |
| 2026-11-12 20:18:40 | [CVE-2026-47259](https://nvd.nist.gov/vuln/detail/CVE-2026-47259) | High | 8.2 | BACnet Stack is a BACnet open source protocol stack C library for embedded systems. Prior to versions 1.4.4, 1.5.1, and… |
| 2026-11-12 20:18:40 | [CVE-2026-47710](https://nvd.nist.gov/vuln/detail/CVE-2026-47710) | High | 8.2 | BACnet Stack is a BACnet open source protocol stack C library for embedded systems. Prior to versions 1.4.4, 1.5.1, and… |
| 2026-11-12 20:18:41 | [CVE-2026-47711](https://nvd.nist.gov/vuln/detail/CVE-2026-47711) | High | 8.6 | BACnet Stack is a BACnet open source protocol stack C library for embedded systems. Prior to versions 1.4.4, 1.5.1, and… |
| 2026-11-12 20:18:42 | [CVE-2026-52786](https://nvd.nist.gov/vuln/detail/CVE-2026-52786) | High | 7.1 | BACnet Stack is a BACnet open source protocol stack C library for embedded systems. Prior to versions 1.4.5, 1.5.1, and… |
| 2026-11-12 20:18:51 | [CVE-2026-68548](https://nvd.nist.gov/vuln/detail/CVE-2026-68548) | Critical | 9.4 | Algernon is a small self-contained pure-Go web server. Prior to version 1.17.10, Algernon's URL-prefix authorization ga… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
