# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-14 18:20 UTC

New CVEs published between 2026-10-14 17:19 UTC and 2026-10-14 18:20 UTC.

[Full CSV](data/new-cves-2026-10-14T18-20-09-123994Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-10-14 17:19:10 | [CVE-2026-75083](https://nvd.nist.gov/vuln/detail/CVE-2026-75083) | Medium | 5.9 | The receive path of the NXP KW41Z IEEE 802.15.4 driver, kw41z_rx() in drivers/ieee802154/ieee802154_kw41z.c, computed t… |
| 2026-10-14 17:19:10 | [CVE-2026-75084](https://nvd.nist.gov/vuln/detail/CVE-2026-75084) | Medium | 6.8 | The CC1200 sub-GHz IEEE 802.15.4 driver takes the PHY packet length from the first byte of the radio's RX FIFO in get_p… |
| 2026-10-14 17:19:10 | [CVE-2026-75085](https://nvd.nist.gov/vuln/detail/CVE-2026-75085) | Medium | 4.2 | The STM32WBA IEEE 802.15.4 driver in drivers/ieee802154/ieee802154_stm32wba.c computed the packet length of a received… |
| 2026-10-14 17:19:10 | [CVE-2026-76519](https://nvd.nist.gov/vuln/detail/CVE-2026-76519) | Critical | 9.8 | A vulnerability in the Advanced Malware Protection (AMP) feature of Cisco Secure Email Gateway could allow an unauthent… |
| 2026-10-14 17:19:11 | [CVE-2026-77524](https://nvd.nist.gov/vuln/detail/CVE-2026-77524) | Critical | 9.9 | KEDA is a Kubernetes-based Event Driven Autoscaling component. In version 2.20.2 and earlier, a namespace administrator… |
| 2026-10-14 17:19:11 | [CVE-2026-77564](https://nvd.nist.gov/vuln/detail/CVE-2026-77564) | Low | 3.3 | Talos Linux is a Linux distribution built for Kubernetes deployments. Prior to 1.12.9 and 1.13.3, talosctl support incl… |
| 2026-10-14 17:20:05 | [CVE-2026-86562](https://nvd.nist.gov/vuln/detail/CVE-2026-86562) | High | 7.8 | A flaw was found in DPDK lib/vhost. A TOCTOU double-fetch of control-queue descriptors allows a heap buffer overflow wi… |
| 2026-10-14 17:20:05 | [CVE-2026-86563](https://nvd.nist.gov/vuln/detail/CVE-2026-86563) | High | 7.8 | A flaw was found in DPDK lib/vhost. A double-offset bug in vhost log mapping calculation can lead to incorrect memory a… |
| 2026-10-14 17:20:05 | [CVE-2026-86565](https://nvd.nist.gov/vuln/detail/CVE-2026-86565) | High | 8.2 | A flaw was found in DPDK lib/vhost. A guest can desynchronize virtqueue size from inflight descriptor table size, causi… |
| 2026-10-14 17:20:20 | [CVE-2026-92151](https://nvd.nist.gov/vuln/detail/CVE-2026-92151) | High | 7.5 | F´ (F Prime) is a framework that enables development and deployment of spaceflight and other embedded software applicat… |
| 2026-10-14 17:20:21 | [CVE-2026-92153](https://nvd.nist.gov/vuln/detail/CVE-2026-92153) | High | 7.1 | F´ (F Prime) is a framework that enables development and deployment of spaceflight and other embedded software applicat… |
| 2026-10-14 17:20:21 | [CVE-2026-93635](https://nvd.nist.gov/vuln/detail/CVE-2026-93635) | Medium | 5.3 | LDAP filter injection in Zimbra Collaboration Suite 10.1.0 through 10.1.21 allows unauthenticated attackers to alter ex… |
| 2026-10-14 17:20:21 | [CVE-2026-93637](https://nvd.nist.gov/vuln/detail/CVE-2026-93637) | Low | 3.7 | An authentication rate-limit bypass in Zimbra Collaboration Suite 10.1.0 through 10.1.21 allows unauthenticated attacke… |
| 2026-10-14 17:20:21 | [CVE-2026-94200](https://nvd.nist.gov/vuln/detail/CVE-2026-94200) | High | 8.2 | Improper Validation of Consistency within Input vulnerability in Erlang OTP ssl (tls_handshake_1_3, ssl_handshake and t… |
| 2026-10-14 17:20:28 | [CVE-2026-96596](https://nvd.nist.gov/vuln/detail/CVE-2026-96596) | Medium | 5.9 | Loop with Unreachable Exit Condition ('Infinite Loop') vulnerability in Erlang OTP stdlib (erl_tar module), hexpm hex_c… |
| 2026-10-14 18:17:07 | [CVE-2026-0322](https://nvd.nist.gov/vuln/detail/CVE-2026-0322) | High | 8.6 | A remote code execution (RCE) vulnerability in the management interface of Palo Alto Networks PAN-OS® software enables… |
| 2026-10-14 18:17:10 | [CVE-2026-100413](https://nvd.nist.gov/vuln/detail/CVE-2026-100413) | High | 7.0 | SeaweedFS is a distributed storage system for files and blobs. From 4.0.388 until 4.41, the SFTP Helm chart embedded on… |
| 2026-10-14 18:17:10 | [CVE-2026-101949](https://nvd.nist.gov/vuln/detail/CVE-2026-101949) | High | 8.7 | A NULL Pointer Dereference vulnerability in the routing protocol daemon (rpd) of Juniper Networks Junos OS and Junos OS… |
| 2026-10-14 18:17:11 | [CVE-2026-101952](https://nvd.nist.gov/vuln/detail/CVE-2026-101952) | High | 8.7 | An Improper Validation of Consistency within Input vulnerability in the routing protocol daemon (rpd) of Juniper Networ… |
| 2026-10-14 18:17:11 | [CVE-2026-101954](https://nvd.nist.gov/vuln/detail/CVE-2026-101954) | Critical | 9.3 | An Improper Authentication vulnerability in the J-Web management interface and its NETCONF session handling of Juniper… |
| 2026-10-14 18:17:11 | [CVE-2026-101959](https://nvd.nist.gov/vuln/detail/CVE-2026-101959) | High | 7.1 | A Function Call With Incorrect Variable or Reference as Argument vulnerability in the routing protocol daemon (rpd) of… |
| 2026-10-14 18:17:11 | [CVE-2026-101961](https://nvd.nist.gov/vuln/detail/CVE-2026-101961) | High | 8.7 | A NULL Pointer Dereference vulnerability in the routing-policy nexthop-ECMP matcher of Juniper Networks Junos OS and Ju… |
| 2026-10-14 18:17:11 | [CVE-2026-101962](https://nvd.nist.gov/vuln/detail/CVE-2026-101962) | High | 8.7 | An Improper Handling of Length Parameter Inconsistency vulnerability in the routing protocol daemon (rpd) of Juniper Ne… |
| 2026-10-14 18:17:11 | [CVE-2026-101963](https://nvd.nist.gov/vuln/detail/CVE-2026-101963) | High | 8.7 | An Incorrect Calculation vulnerability in the routing protocol daemon (rpd) of Juniper Networks Junos OS and Junos EVO… |
| 2026-10-14 18:17:12 | [CVE-2026-101964](https://nvd.nist.gov/vuln/detail/CVE-2026-101964) | High | 7.1 | A Reachable Assertion vulnerability in the routing protocol daemon (rpd) of Juniper Networks Junos OS and Junos OS Evol… |
| 2026-10-14 18:17:12 | [CVE-2026-101972](https://nvd.nist.gov/vuln/detail/CVE-2026-101972) | High | 7.1 | An Integer Overflow or Wraparound vulnerability in the routing protocol daemon (rpd) of Juniper Networks Junos OS and J… |
| 2026-10-14 18:17:12 | [CVE-2026-101975](https://nvd.nist.gov/vuln/detail/CVE-2026-101975) | High | 7.1 | A Reachable Assertion vulnerability in the routing protocol daemon (rpd) of Juniper Networks Junos OS and Junos OS Evol… |
| 2026-10-14 18:17:12 | [CVE-2026-101976](https://nvd.nist.gov/vuln/detail/CVE-2026-101976) | High | 8.7 | An Out-of-bounds Write vulnerability in the routing protocol daemon (rpd) of Juniper Networks Junos OS and Junos OS Evo… |
| 2026-10-14 18:17:12 | [CVE-2026-101979](https://nvd.nist.gov/vuln/detail/CVE-2026-101979) | High | 8.7 | A Stack-based Buffer Overflow vulnerability in the authd Juniper Networks Junos OS and Junos OS Evolved allows a networ… |
| 2026-10-14 18:17:12 | [CVE-2026-101981](https://nvd.nist.gov/vuln/detail/CVE-2026-101981) | High | 8.7 | A Stack-based Buffer Overflow vulnerability in the routing protocol daemon (rpd) of Juniper Networks Junos OS and Junos… |
| 2026-10-14 18:17:13 | [CVE-2026-101982](https://nvd.nist.gov/vuln/detail/CVE-2026-101982) | Critical | 9.3 | A Stack-based Buffer Overflow vulnerability in the routing protocol daemon (rpd) of Juniper Networks Junos OS and Junos… |
| 2026-10-14 18:17:13 | [CVE-2026-101983](https://nvd.nist.gov/vuln/detail/CVE-2026-101983) | Critical | 9.3 | A Stack-based Buffer Overflow vulnerability in the httpd process of Juniper Networks Junos OS and Junos OS Evolved allo… |
| 2026-10-14 18:17:13 | [CVE-2026-102077](https://nvd.nist.gov/vuln/detail/CVE-2026-102077) | High | 8.7 | An Improper Check for Unusual or Exceptional Conditions vulnerability in the Packet Forwarding Engine (PFE) of Juniper… |
| 2026-10-14 18:17:17 | [CVE-2026-102476](https://nvd.nist.gov/vuln/detail/CVE-2026-102476) | Critical | 9.1 | In Eclipse Vert.x versions [5.0.0,5.0.12] or [5.1.0,5.1.9] or [5.2.0, 5.2.0], the Vert.x HTTP client relies on an SSL c… |
| 2026-10-14 18:17:19 | [CVE-2026-103081](https://nvd.nist.gov/vuln/detail/CVE-2026-103081) | High | 7.5 | Improper Control of Generation of Code ('Code Injection') vulnerability in VillaTheme Salevo woo-boost-sales allows Cod… |
| 2026-10-14 18:17:19 | [CVE-2026-103414](https://nvd.nist.gov/vuln/detail/CVE-2026-103414) | High | 8.4 | The GUIX binary resource (theme) loader sizes its arena and populates it in two separate passes that traverse the resou… |
| 2026-10-14 18:17:19 | [CVE-2026-103415](https://nvd.nist.gov/vuln/detail/CVE-2026-103415) | Critical | 9.3 | When a TLS 1.3 client processes a HelloRetryRequest, it copies the server's cookie into its second ClientHello without… |
| 2026-10-14 18:17:21 | [CVE-2026-103975](https://nvd.nist.gov/vuln/detail/CVE-2026-103975) | Medium | 6.5 | Appium is a cross-platform automation framework for all kinds of apps, built on top of the W3C WebDriver protocol. Prio… |
| 2026-10-14 18:17:21 | [CVE-2026-104103](https://nvd.nist.gov/vuln/detail/CVE-2026-104103) | High | 8.1 | Ludwig is a low-code framework for building custom LLMs, neural networks, and other AI models. Prior to 0.17.8, ludwig.… |
| 2026-10-14 18:17:22 | [CVE-2026-105066](https://nvd.nist.gov/vuln/detail/CVE-2026-105066) | High | 7.1 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in SimplyRETS Simply… |
| 2026-10-14 18:17:24 | [CVE-2026-106464](https://nvd.nist.gov/vuln/detail/CVE-2026-106464) | High | 8.7 | `_nx_secure_x509_parse_signature_data` computes the certificate signature's length as `tlv_length - 1` without first ch… |
| 2026-10-14 18:17:25 | [CVE-2026-106465](https://nvd.nist.gov/vuln/detail/CVE-2026-106465) | High | 8.7 | The NetX Secure DTLS server sends a HelloVerifyRequest carrying a freshly generated cookie, but never checks the cookie… |
| 2026-10-14 18:17:25 | [CVE-2026-107348](https://nvd.nist.gov/vuln/detail/CVE-2026-107348) | Medium | 5.9 | Integer overflow in the message buffer growth logic (mbuf_make_room) in PgBouncer 1.21.0 through 1.26.0 allows a remote… |
| 2026-10-14 18:17:25 | [CVE-2026-107349](https://nvd.nist.gov/vuln/detail/CVE-2026-107349) | High | 7.5 | An infinite loop in PgBouncer 1.20.0 through 1.26.0 allows an unauthenticated remote attacker to cause a denial of serv… |
| 2026-10-14 18:17:25 | [CVE-2026-107350](https://nvd.nist.gov/vuln/detail/CVE-2026-107350) | High | 8.8 | Improper authentication in PgBouncer 1.17.0 through 1.26.0 allows a remote attacker who knows the password of a user li… |
| 2026-10-14 18:17:27 | [CVE-2026-108151](https://nvd.nist.gov/vuln/detail/CVE-2026-108151) | Medium | 5.3 | Improper Control of Generation of Code ('Code Injection') vulnerability in PluginUs.Net MDTF wp-meta-data-filter-and-ta… |
| 2026-10-14 18:17:27 | [CVE-2026-108390](https://nvd.nist.gov/vuln/detail/CVE-2026-108390) | Critical | 9.9 | Hestia Control Panel is a lightweight and powerful control panel for the modern web. From version 1.9.7 through 1.10.4,… |
| 2026-10-14 18:17:27 | [CVE-2026-108395](https://nvd.nist.gov/vuln/detail/CVE-2026-108395) | High | 7.5 | The Model Context Protocol Java SDK is the official Java SDK for Model Context Protocol servers and clients. From versi… |
| 2026-10-14 18:17:29 | [CVE-2026-108480](https://nvd.nist.gov/vuln/detail/CVE-2026-108480) | High | 8.2 | Missing Authorization vulnerability in Skydropx Skydropx skydropx allows Exploiting Incorrectly Configured Access Contr… |
| 2026-10-14 18:17:29 | [CVE-2026-108483](https://nvd.nist.gov/vuln/detail/CVE-2026-108483) | High | 7.1 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in hippooo Hippoo Mo… |
| 2026-10-14 18:17:29 | [CVE-2026-108484](https://nvd.nist.gov/vuln/detail/CVE-2026-108484) | High | 7.1 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in WPManageNinja Bes… |
| 2026-10-14 18:17:33 | [CVE-2026-109527](https://nvd.nist.gov/vuln/detail/CVE-2026-109527) | High | 7.5 | The Model Context Protocol Python SDK is the official Python SDK for Model Context Protocol servers and clients. In mcp… |
| 2026-10-14 18:17:36 | [CVE-2026-110777](https://nvd.nist.gov/vuln/detail/CVE-2026-110777) | Medium | 5.7 | A flaw was found in evolution-data-server. Calendar events containing a file:// URI in their ATTACH property automatica… |
| 2026-10-14 18:17:36 | [CVE-2026-42093](https://nvd.nist.gov/vuln/detail/CVE-2026-42093) | High | 8.7 | Redash is a package for data visualization and sharing. From versions after 8.0.0 until 26.9.0, the Query Results query… |
| 2026-10-14 18:17:37 | [CVE-2026-54554](https://nvd.nist.gov/vuln/detail/CVE-2026-54554) | High | 7.5 | FOG is a free open-source cloning/imaging/rescue suite/inventory management system. Prior to 1.5.10.1870, the managemen… |
| 2026-10-14 18:17:37 | [CVE-2026-55572](https://nvd.nist.gov/vuln/detail/CVE-2026-55572) | Critical | 10.0 | e107 is a content management system (CMS). Prior to 2.3.7, the bundled alt_auth plugin's otherdb and e107db authenticat… |
| 2026-10-14 18:17:38 | [CVE-2026-55573](https://nvd.nist.gov/vuln/detail/CVE-2026-55573) | Critical | 9.8 | e107 is a content management system (CMS). Prior to 2.3.7, install.php decodes the attacker-controlled previous_steps P… |
| 2026-10-14 18:18:18 | [CVE-2026-76083](https://nvd.nist.gov/vuln/detail/CVE-2026-76083) | Medium | 4.9 | Redash is a package for data visualization and sharing. From 10.0.0 until 26.9.0, the JSON data source query runner in… |
| 2026-10-14 18:18:18 | [CVE-2026-77371](https://nvd.nist.gov/vuln/detail/CVE-2026-77371) | Critical | 9.3 | Redash is a package for data visualization and sharing. From 26.0.0 until 26.9.0, the DuckDB query runner's _connect()… |
| 2026-10-14 18:18:19 | [CVE-2026-79957](https://nvd.nist.gov/vuln/detail/CVE-2026-79957) | High | 8.1 | ServiceNext contains an insecure direct object reference (IDOR) in the /api/Usuario/GetUsuarios endpoint, which accepts… |
| 2026-10-14 18:19:17 | [CVE-2026-86461](https://nvd.nist.gov/vuln/detail/CVE-2026-86461) | High | 8.8 | The FV Flowplayer Video Player plugin for WordPress is vulnerable to Limited Arbitrary File Upload in all versions up t… |
| 2026-10-14 18:19:18 | [CVE-2026-86566](https://nvd.nist.gov/vuln/detail/CVE-2026-86566) | Medium | 6.5 | A flaw was found in DPDK lib/vhost. A guest with runt RX descriptors can underflow the copy length in vhost enqueue, ca… |
| 2026-10-14 18:19:18 | [CVE-2026-86567](https://nvd.nist.gov/vuln/detail/CVE-2026-86567) | High | 8.8 | A flaw was found in DPDK lib/vhost. The VDUSE handler fails to invalidate vring pointers when the IOTLB is invalidated,… |
| 2026-10-14 18:19:18 | [CVE-2026-86845](https://nvd.nist.gov/vuln/detail/CVE-2026-86845) | Medium | 6.5 | A flaw was found in DPDK lib/vhost vhost-crypto. Session cleanup can leave a stale cached session pointer, and the data… |
| 2026-10-14 18:19:18 | [CVE-2026-86846](https://nvd.nist.gov/vuln/detail/CVE-2026-86846) | Medium | 6.5 | A flaw was found in DPDK lib/vhost vhost-crypto. A guest can supply an avail-ring descriptor index that is used without… |
| 2026-10-14 18:19:19 | [CVE-2026-86847](https://nvd.nist.gov/vuln/detail/CVE-2026-86847) | Medium | 6.5 | A flaw was found in DPDK lib/vhost vhost-crypto. Write-back chain cleanup can follow an uninitialized next pointer when… |
| 2026-10-14 18:19:19 | [CVE-2026-86848](https://nvd.nist.gov/vuln/detail/CVE-2026-86848) | High | 8.8 | A flaw was found in DPDK lib/vhost vhost-crypto. The indirect-descriptor snapshot double-fetches a guest descriptor nex… |
| 2026-10-14 18:19:19 | [CVE-2026-86849](https://nvd.nist.gov/vuln/detail/CVE-2026-86849) | Medium | 6.5 | A flaw was found in DPDK lib/vhost vhost-crypto. Integer overflow in chain length checks, and missing length checks on… |
| 2026-10-14 18:19:19 | [CVE-2026-86856](https://nvd.nist.gov/vuln/detail/CVE-2026-86856) | Medium | 6.5 | A flaw was found in the DPDK nfp vDPA driver. Stack and heap buffers sized for a single queue pair can be overflowed wh… |
| 2026-10-14 18:19:30 | [CVE-2026-88164](https://nvd.nist.gov/vuln/detail/CVE-2026-88164) | High | 8.8 | Missing authorization in Microsoft Office SharePoint allows an authorized attacker to elevate privileges over a network. |
| 2026-10-14 18:19:34 | [CVE-2026-92150](https://nvd.nist.gov/vuln/detail/CVE-2026-92150) | High | 7.5 | F´ (F Prime) is a framework that enables development and deployment of spaceflight and other embedded software applicat… |
| 2026-10-14 18:19:34 | [CVE-2026-92152](https://nvd.nist.gov/vuln/detail/CVE-2026-92152) | Critical | 9.3 | F´ (F Prime) is a framework that enables development and deployment of spaceflight and other embedded software applicat… |
| 2026-10-14 18:19:34 | [CVE-2026-92154](https://nvd.nist.gov/vuln/detail/CVE-2026-92154) | High | 8.1 | F´ (F Prime) is a framework that enables development and deployment of spaceflight and other embedded software applicat… |
| 2026-10-14 18:19:34 | [CVE-2026-92155](https://nvd.nist.gov/vuln/detail/CVE-2026-92155) | High | 7.5 | F´ (F Prime) is a framework that enables development and deployment of spaceflight and other embedded software applicat… |
| 2026-10-14 18:19:34 | [CVE-2026-92156](https://nvd.nist.gov/vuln/detail/CVE-2026-92156) | Medium | 6.5 | F´ (F Prime) is a framework that enables development and deployment of spaceflight and other embedded software applicat… |
| 2026-10-14 18:19:35 | [CVE-2026-92157](https://nvd.nist.gov/vuln/detail/CVE-2026-92157) | Medium | 6.5 | F´ (F Prime) is a framework that enables development and deployment of spaceflight and other embedded software applicat… |
| 2026-10-14 18:19:35 | [CVE-2026-92158](https://nvd.nist.gov/vuln/detail/CVE-2026-92158) | High | 7.2 | F´ (F Prime) is a framework that enables development and deployment of spaceflight and other embedded software applicat… |
| 2026-10-14 18:19:35 | [CVE-2026-92159](https://nvd.nist.gov/vuln/detail/CVE-2026-92159) | Medium | 6.5 | F´ (F Prime) is a framework that enables development and deployment of spaceflight and other embedded software applicat… |
| 2026-10-14 18:19:35 | [CVE-2026-92160](https://nvd.nist.gov/vuln/detail/CVE-2026-92160) | Medium | 6.5 | F´ (F Prime) is a framework that enables development and deployment of spaceflight and other embedded software applicat… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
