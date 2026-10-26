# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-26 15:19 UTC

New CVEs published between 2026-10-26 14:18 UTC and 2026-10-26 15:19 UTC.

[Full CSV](data/new-cves-2026-10-26T15-19-55-583559Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-10-26 15:16:35 | [CVE-2026-106781](https://nvd.nist.gov/vuln/detail/CVE-2026-106781) |  |  | An issue in WCH CH340/CH341 USB-to-Serial Windows Driver setup package CH341SER.EXE version 4.0 allows a local attacker… |
| 2026-10-26 15:16:36 | [CVE-2026-110733](https://nvd.nist.gov/vuln/detail/CVE-2026-110733) |  |  | Vulnerability in the SQL storage module of Apache SIS. When sorting a stream of features, the clause is copied after OR… |
| 2026-10-26 15:16:36 | [CVE-2026-110748](https://nvd.nist.gov/vuln/detail/CVE-2026-110748) |  |  | This issue affects Apache SIS from version 0.7 through 1.6 inclusive. When a data file contains links to other files, A… |
| 2026-10-26 15:16:38 | [CVE-2026-112345](https://nvd.nist.gov/vuln/detail/CVE-2026-112345) | High | 8.6 | TTLock Android application before v9.8.260718 and associated smart-lock firmware contain a hardcoded static AES key vul… |
| 2026-10-26 15:16:39 | [CVE-2026-115930](https://nvd.nist.gov/vuln/detail/CVE-2026-115930) | High | 7.6 | The MongoDB Shell (mongosh) relies on Node.js as a third-party runtime that carries its own TLS root certificate store.… |
| 2026-10-26 15:16:39 | [CVE-2026-116284](https://nvd.nist.gov/vuln/detail/CVE-2026-116284) | Medium | 5.3 | A security vulnerability has been detected in Kameleo up to 5.3.1. This vulnerability affects unknown code of the file… |
| 2026-10-26 15:16:39 | [CVE-2026-116339](https://nvd.nist.gov/vuln/detail/CVE-2026-116339) | Medium | 5.5 | A vulnerability was determined in iFlytek astron-agent up to 1.1.2. This affects an unknown function of the file core/m… |
| 2026-10-26 15:16:40 | [CVE-2026-116340](https://nvd.nist.gov/vuln/detail/CVE-2026-116340) | Low | 2.1 | A vulnerability was identified in iFlytek astron-agent up to 1.1.2. This impacts the function FileInfoV2Service.listKno… |
| 2026-10-26 15:16:40 | [CVE-2026-116497](https://nvd.nist.gov/vuln/detail/CVE-2026-116497) | Medium | 5.5 | A NULL pointer dereference vulnerability was found in gssproxy. When a GSSX_INIT_SEC_CONTEXT request is received with t… |
| 2026-10-26 15:16:40 | [CVE-2026-31158](https://nvd.nist.gov/vuln/detail/CVE-2026-31158) |  |  | SQL Injection vulnerability in CRM SOFTTRADE Infotech (aka softtradeindia) 1.0 allows a remote attacker to execute arbi… |
| 2026-10-26 15:16:40 | [CVE-2026-36698](https://nvd.nist.gov/vuln/detail/CVE-2026-36698) |  |  | Xovis AG APS-R-POE, APS-R-POE-PP, APS-R, APS-R-POE-USB, and APS-B 2.10.1.1 and earlier contains an OS command injection… |
| 2026-10-26 15:16:40 | [CVE-2026-3322](https://nvd.nist.gov/vuln/detail/CVE-2026-3322) | Medium | 5.6 | Due to improper permission checks in Lobster_pro, attackers are able to interact with endpoints that should require adm… |
| 2026-10-26 15:16:41 | [CVE-2026-65184](https://nvd.nist.gov/vuln/detail/CVE-2026-65184) | Critical | 9.8 | The root-privileged `wsserver` terminal-bridge daemon builds a shell command from client-supplied WebSocket fields and… |
| 2026-10-26 15:16:42 | [CVE-2026-77052](https://nvd.nist.gov/vuln/detail/CVE-2026-77052) | High | 8.7 | boneIO Black exposes a Node-RED instance without authentication at the /nodered/ path through a Caddy reverse proxy. Th… |
| 2026-10-26 15:16:42 | [CVE-2026-77053](https://nvd.nist.gov/vuln/detail/CVE-2026-77053) | High | 8.7 | boneIO Black firmware ships with authentication disabled by default. Its management web API listens on all network inte… |
| 2026-10-26 15:16:42 | [CVE-2026-77054](https://nvd.nist.gov/vuln/detail/CVE-2026-77054) | Medium | 6.9 | boneIO Black stores passwords, including the MQTT broker and web panel passwords, in cleartext. The GET /api/config end… |
| 2026-10-26 15:16:43 | [CVE-2026-77055](https://nvd.nist.gov/vuln/detail/CVE-2026-77055) | Critical | 9.3 | boneIO black_debian_images gives the boneio service account excessive privileges, including full passwordless sudo acce… |
| 2026-10-26 15:16:43 | [CVE-2026-77056](https://nvd.nist.gov/vuln/detail/CVE-2026-77056) | High | 7.1 | boneIO black_debian_images ships with a Mosquitto MQTT broker that uses the same default credentials on all devices. Th… |
| 2026-10-26 15:16:43 | [CVE-2026-77057](https://nvd.nist.gov/vuln/detail/CVE-2026-77057) | Low | 2.3 | boneIO Black does not limit authentication attempts on its web interface (POST /api/login) or SSH service, and does not… |
| 2026-10-26 15:16:43 | [CVE-2026-77058](https://nvd.nist.gov/vuln/detail/CVE-2026-77058) | Medium | 5.1 | boneIO Black is vulnerable to Cross-Site Request Forgery (CSRF) on all state-changing API endpoints because it lacks CS… |
| 2026-10-26 15:16:43 | [CVE-2026-77059](https://nvd.nist.gov/vuln/detail/CVE-2026-77059) | High | 8.8 | boneIO Black contains a TOCTOU race condition in the create_timedatectl_sudoers_file() function in boneio/webui/routes/… |
| 2026-10-26 15:16:43 | [CVE-2026-77060](https://nvd.nist.gov/vuln/detail/CVE-2026-77060) | Medium | 6.8 | boneIO black_debian_images stores the Mosquitto MQTT broker password file at /etc/mosquitto/passwd with world-readable… |
| 2026-10-26 15:16:44 | [CVE-2026-77061](https://nvd.nist.gov/vuln/detail/CVE-2026-77061) | Medium | 5.3 | boneIO Black directly excludes several API endpoints from the authentication. An unauthenticated remote attacker on the… |
| 2026-10-26 15:16:44 | [CVE-2026-77062](https://nvd.nist.gov/vuln/detail/CVE-2026-77062) | Medium | 6.9 | The boneIO Black web interface lacks proper clickjacking protections. A remote attacker can embed the control panel in… |
| 2026-10-26 15:16:45 | [CVE-2026-90885](https://nvd.nist.gov/vuln/detail/CVE-2026-90885) | High | 7.5 | Improper Restriction of XML External Entity Reference vulnerability in Apache Camel Saxon component. This issue affects… |
| 2026-10-26 15:16:45 | [CVE-2026-92171](https://nvd.nist.gov/vuln/detail/CVE-2026-92171) | Medium | 6.5 | A flaw was found in the Infinispan Operator for Red Hat Data Grid. When cross-site (xsite) TLS is enabled, the operator… |
| 2026-10-26 15:16:45 | [CVE-2026-93328](https://nvd.nist.gov/vuln/detail/CVE-2026-93328) | Critical | 9.3 | Path Traversal and Missing Authorization in cloud-storage source in Google Cloud MCP Toolbox for Databases (googleapis/… |
| 2026-10-26 15:16:46 | [CVE-2026-93847](https://nvd.nist.gov/vuln/detail/CVE-2026-93847) | Low | 3.5 | Mattermost versions 11.7.x <= 11.7.10 fail to validate reserved system post types on the scheduled post creation and pu… |
| 2026-10-26 15:16:46 | [CVE-2026-93848](https://nvd.nist.gov/vuln/detail/CVE-2026-93848) | Low | 2.7 | Mattermost versions 11.7.x <= 11.7.10 fail to apply outbound internal-connection filtering to the OpenID discovery endp… |
| 2026-10-26 15:16:46 | [CVE-2026-93849](https://nvd.nist.gov/vuln/detail/CVE-2026-93849) | Medium | 6.5 | Mattermost versions 11.9.x <= 11.9.1, 11.8.x <= 11.8.5, 11.7.x <= 11.7.10, 11.10.x <= 11.10.1 Mattermost fail to apply… |
| 2026-10-26 15:16:46 | [CVE-2026-93850](https://nvd.nist.gov/vuln/detail/CVE-2026-93850) | Medium | 6.5 | Mattermost versions 11.9.x <= 11.9.1, 11.8.x <= 11.8.5, 11.7.x <= 11.7.10, 11.10.x <= 11.10.1 fail to bind the volume o… |
| 2026-10-26 15:16:46 | [CVE-2026-94386](https://nvd.nist.gov/vuln/detail/CVE-2026-94386) | Medium | 4.8 | Use of Cache Containing Sensitive Information vulnerability in Apache Camel Oauth component. This issue affects Apache… |
| 2026-10-26 15:16:47 | [CVE-2026-99088](https://nvd.nist.gov/vuln/detail/CVE-2026-99088) |  |  | In the Linux kernel, the following vulnerability has been resolved: net: openvswitch: validate transport header presenc… |
| 2026-10-26 15:16:47 | [CVE-2026-99089](https://nvd.nist.gov/vuln/detail/CVE-2026-99089) |  |  | In the Linux kernel, the following vulnerability has been resolved: ASoC: samsung: i2s: enable op_clk in probe to balan… |
| 2026-10-26 15:16:47 | [CVE-2026-99090](https://nvd.nist.gov/vuln/detail/CVE-2026-99090) |  |  | In the Linux kernel, the following vulnerability has been resolved: drm/amdgpu: serialize vblank counter reads against… |
| 2026-10-26 15:16:47 | [CVE-2026-99091](https://nvd.nist.gov/vuln/detail/CVE-2026-99091) |  |  | In the Linux kernel, the following vulnerability has been resolved: Bluetooth: MGMT: Fix status of pending commands flu… |
| 2026-10-26 15:16:48 | [CVE-2026-99092](https://nvd.nist.gov/vuln/detail/CVE-2026-99092) |  |  | In the Linux kernel, the following vulnerability has been resolved: riscv: patch: fix handling of bpf-jit execmem addre… |
| 2026-10-26 15:16:48 | [CVE-2026-99093](https://nvd.nist.gov/vuln/detail/CVE-2026-99093) |  |  | In the Linux kernel, the following vulnerability has been resolved: mm: don't schedule deferred kernel page table freei… |
| 2026-10-26 15:16:48 | [CVE-2026-99094](https://nvd.nist.gov/vuln/detail/CVE-2026-99094) |  |  | In the Linux kernel, the following vulnerability has been resolved: Bluetooth: btintel_pcie: fix TX descriptor bounds c… |
| 2026-10-26 15:16:48 | [CVE-2026-99095](https://nvd.nist.gov/vuln/detail/CVE-2026-99095) |  |  | In the Linux kernel, the following vulnerability has been resolved: drm/vc4: drain the hangcheck timer and works on V3D… |
| 2026-10-26 15:16:48 | [CVE-2026-99096](https://nvd.nist.gov/vuln/detail/CVE-2026-99096) |  |  | In the Linux kernel, the following vulnerability has been resolved: io_uring/register: don't exempt disabled rings from… |
| 2026-10-26 15:16:48 | [CVE-2026-99097](https://nvd.nist.gov/vuln/detail/CVE-2026-99097) |  |  | In the Linux kernel, the following vulnerability has been resolved: tee: shm: reject zero-sized allocations in tee_dyn_… |
| 2026-10-26 15:16:48 | [CVE-2026-99098](https://nvd.nist.gov/vuln/detail/CVE-2026-99098) |  |  | In the Linux kernel, the following vulnerability has been resolved: dm-integrity: fix buffer overflow in inline mode wi… |
| 2026-10-26 15:16:48 | [CVE-2026-99099](https://nvd.nist.gov/vuln/detail/CVE-2026-99099) |  |  | In the Linux kernel, the following vulnerability has been resolved: x86/CPU/AMD: Fix AMD TLBI Erratum #1718 The process… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
