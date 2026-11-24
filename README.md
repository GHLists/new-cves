# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-11-24 08:21 UTC

New CVEs published between 2026-11-24 07:18 UTC and 2026-11-24 08:21 UTC.

[Full CSV](data/new-cves-2026-11-24T08-21-04-309994Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-11-24 08:17:02 | [CVE-2026-105428](https://nvd.nist.gov/vuln/detail/CVE-2026-105428) | Medium | 5.3 | Binding to an unrestricted IP address in the netstack SOCKS5 proxy of the NetBird client (client/iface/netstack) in Net… |
| 2026-11-24 08:17:03 | [CVE-2026-105430](https://nvd.nist.gov/vuln/detail/CVE-2026-105430) | Medium | 6.3 | Deserialization of untrusted data in the relay server handshake of NetBird versions 0.29.0 through 0.74.7 allows an una… |
| 2026-11-24 08:17:04 | [CVE-2026-105431](https://nvd.nist.gov/vuln/detail/CVE-2026-105431) | Low | 2.1 | A protection mechanism failure in the userspace firewall of the NetBird client (client/firewall/uspfilter) in NetBird v… |
| 2026-11-24 08:17:04 | [CVE-2026-10084](https://nvd.nist.gov/vuln/detail/CVE-2026-10084) | Medium | 5.3 | An unauthenticated attacker can send an unsigned SAML single logout request to force users to log out of Grafana Enterp… |
| 2026-11-24 08:17:04 | [CVE-2026-120934](https://nvd.nist.gov/vuln/detail/CVE-2026-120934) | High | 7.0 | An External Control of File Name or Path (Argument Injection) vulnerability in the settings/notification.cgi component… |
| 2026-11-24 08:17:04 | [CVE-2026-120935](https://nvd.nist.gov/vuln/detail/CVE-2026-120935) | High | 7.0 | An argument injection vulnerability exists in the settings/vpn.cgi endpoint in the ADM. When processing a WireGuard pro… |
| 2026-11-24 08:17:04 | [CVE-2026-120936](https://nvd.nist.gov/vuln/detail/CVE-2026-120936) | High | 8.7 | An arbitrary file creation and truncation vulnerability exists in the File Explorer of ADM. An authenticated low-privil… |
| 2026-11-24 08:17:04 | [CVE-2026-120940](https://nvd.nist.gov/vuln/detail/CVE-2026-120940) | Low | 2.3 | A stack-based buffer overflow in the DHCP Server helper of ASUSTOR ADM allows an unauthenticated attacker on the local… |
| 2026-11-24 08:17:05 | [CVE-2026-120946](https://nvd.nist.gov/vuln/detail/CVE-2026-120946) | High | 8.6 | An OS command injection vulnerability in ADM allows remote authenticated administrators to execute arbitrary commands a… |
| 2026-11-24 08:17:05 | [CVE-2026-120947](https://nvd.nist.gov/vuln/detail/CVE-2026-120947) | Medium | 5.1 | A potential stack-based buffer overflow exists in ADM Defender Firewall configuration handling. Before the fix, firewal… |
| 2026-11-24 08:17:05 | [CVE-2026-120948](https://nvd.nist.gov/vuln/detail/CVE-2026-120948) | High | 8.6 | An OS command injection vulnerability in the PPPoE configuration of ADM allows an authenticated administrator to store… |
| 2026-11-24 08:17:05 | [CVE-2026-121016](https://nvd.nist.gov/vuln/detail/CVE-2026-121016) | High | 8.6 | The affected products insufficiently restrict runtime-supplied visualization data, allowing local program execution on… |
| 2026-11-24 08:17:05 | [CVE-2026-121017](https://nvd.nist.gov/vuln/detail/CVE-2026-121017) | High | 8.6 | The affected products insufficiently restrict runtime-supplied visualization data, allowing to invoke local COM/ActiveX… |
| 2026-11-24 08:17:05 | [CVE-2026-121018](https://nvd.nist.gov/vuln/detail/CVE-2026-121018) | High | 8.6 | The affected products insufficiently restrict runtime-supplied visualization commands, allowing local functionality on… |
| 2026-11-24 08:17:05 | [CVE-2026-121019](https://nvd.nist.gov/vuln/detail/CVE-2026-121019) | Medium | 4.6 | An unauthenticated attacker can trick a local user into generating an offline boot application from a malicious CODESYS… |
| 2026-11-24 08:17:05 | [CVE-2026-134896](https://nvd.nist.gov/vuln/detail/CVE-2026-134896) | High | 8.4 | An improper input validation vulnerability in the OpenVPN client configuration import feature of ADM allows authenticat… |
| 2026-11-24 08:17:06 | [CVE-2026-134897](https://nvd.nist.gov/vuln/detail/CVE-2026-134897) | High | 8.6 | An OS command injection vulnerability in ADM allows an authenticated administrator to create an iSCSI LUN with a crafte… |
| 2026-11-24 08:17:06 | [CVE-2026-135779](https://nvd.nist.gov/vuln/detail/CVE-2026-135779) | Medium | 5.3 | Reliance on an untrusted source of the client address in the WebSocket listener of the NetBird relay server (relay/serv… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
