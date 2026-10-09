# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-09 15:18 UTC

New CVEs published between 2026-10-09 14:18 UTC and 2026-10-09 15:18 UTC.

[Full CSV](data/new-cves-2026-10-09T15-18-34-291199Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-10-09 15:17:06 | [CVE-2026-102916](https://nvd.nist.gov/vuln/detail/CVE-2026-102916) | Medium | 6.8 | A reachable assertion in the illumos bhyve instruction emulator allows a guest to panic the host. When emulating a REP-… |
| 2026-10-09 15:17:06 | [CVE-2026-104081](https://nvd.nist.gov/vuln/detail/CVE-2026-104081) | High | 7.2 | KodExplorer before 4.55 contains a path traversal vulnerability in the unzip_pre_name() function within app/function/he… |
| 2026-10-09 15:17:07 | [CVE-2026-104112](https://nvd.nist.gov/vuln/detail/CVE-2026-104112) | Medium | 6.8 | A missing release of resources in the illumos name service cache daemon (nscd) allows a local user to exhaust kernel me… |
| 2026-10-09 15:17:07 | [CVE-2026-104113](https://nvd.nist.gov/vuln/detail/CVE-2026-104113) | Medium | 5.4 | A double free in the IP management daemon (ipmgmtd) of OmniOS and SmartOS allows a local user to crash the daemon. When… |
| 2026-10-09 15:17:07 | [CVE-2026-104114](https://nvd.nist.gov/vuln/detail/CVE-2026-104114) | Medium | 5.4 | A NULL pointer dereference in the illumos Network Auto-Magic daemon (nwamd) allows a local user to crash the daemon. nw… |
| 2026-10-09 15:17:07 | [CVE-2026-104115](https://nvd.nist.gov/vuln/detail/CVE-2026-104115) | Medium | 5.4 | A stack-based buffer overflow in the illumos reparse point daemon (reparsed) allows a local user to crash the daemon. g… |
| 2026-10-09 15:17:07 | [CVE-2026-104116](https://nvd.nist.gov/vuln/detail/CVE-2026-104116) | Low | 1.9 | A missing authorization check in the illumos zones statistics daemon (zonestatd) allows a local user in any zone to dis… |
| 2026-10-09 15:17:07 | [CVE-2026-104117](https://nvd.nist.gov/vuln/detail/CVE-2026-104117) | Low | 1.9 | A missing authorization check in the illumos IP management daemon (ipmgmtd) allows a local user to change the persisten… |
| 2026-10-09 15:17:08 | [CVE-2026-105278](https://nvd.nist.gov/vuln/detail/CVE-2026-105278) | Critical | 9.3 | The published Docker image for openPDC includes a fixed administrative credential with no forced change on first use. A… |
| 2026-10-09 15:17:09 | [CVE-2026-107804](https://nvd.nist.gov/vuln/detail/CVE-2026-107804) | Medium | 5.3 | Nginx UI is a web user interface for the Nginx web server. From 2.2.0 until 2.6.0, the bundled reverse proxy does not p… |
| 2026-10-09 15:17:09 | [CVE-2026-107805](https://nvd.nist.gov/vuln/detail/CVE-2026-107805) | High | 7.5 | Nginx UI is a web user interface for the Nginx web server. From 2.5.0 until 2.6.0, the node-signature authentication pa… |
| 2026-10-09 15:17:10 | [CVE-2026-107806](https://nvd.nist.gov/vuln/detail/CVE-2026-107806) | Critical | 9.4 | Nginx UI is a web user interface for the Nginx web server. From 2.3.8 until 2.5.0, an authenticated administrator with… |
| 2026-10-09 15:17:10 | [CVE-2026-108100](https://nvd.nist.gov/vuln/detail/CVE-2026-108100) | High | 7.1 | HortusFox (hortusfox-web) before 6.2 contains an SQL injection vulnerability that allows API token holders to inject SQ… |
| 2026-10-09 15:17:10 | [CVE-2026-108101](https://nvd.nist.gov/vuln/detail/CVE-2026-108101) | High | 7.7 | HortusFox (hortusfox-web) through 6.3 contains an unrestricted file upload vulnerability in PlantAttachmentModel that a… |
| 2026-10-09 15:17:10 | [CVE-2026-108102](https://nvd.nist.gov/vuln/detail/CVE-2026-108102) | Medium | 6.9 | Open5GS through 2.8.0 contains a heap out-of-bounds read vulnerability in ogs_pfcp_parse_volume_measurement() in lib/pf… |
| 2026-10-09 15:17:11 | [CVE-2026-108103](https://nvd.nist.gov/vuln/detail/CVE-2026-108103) | Medium | 6.9 | Open5GS through 2.8.0 contains a heap out-of-bounds read vulnerability in ogs_pfcp_parse_dropped_dl_traffic_threshold()… |
| 2026-10-09 15:17:11 | [CVE-2026-108104](https://nvd.nist.gov/vuln/detail/CVE-2026-108104) | Medium | 6.3 | Xerial snappy-java from 1.1.7.4 before 1.1.10.10 contains a double release vulnerability in SnappyFramedInputStream tha… |
| 2026-10-09 15:17:11 | [CVE-2026-108105](https://nvd.nist.gov/vuln/detail/CVE-2026-108105) | High | 8.2 | Open5GS through 2.8.0 contains a reachable assertion vulnerability in mme_gn_handle_sgsn_context_request() that allows… |
| 2026-10-09 15:17:11 | [CVE-2026-108106](https://nvd.nist.gov/vuln/detail/CVE-2026-108106) | High | 8.7 | Xerial snappy-java before 1.1.10.9 contains an unbounded memory allocation vulnerability that allows attackers to exhau… |
| 2026-10-09 15:17:11 | [CVE-2026-108107](https://nvd.nist.gov/vuln/detail/CVE-2026-108107) | Critical | 9.3 | PHPNuxBill through 2025.3.20 contains an unauthenticated SQL injection vulnerability in the radius.php FreeRADIUS REST… |
| 2026-10-09 15:17:11 | [CVE-2026-108108](https://nvd.nist.gov/vuln/detail/CVE-2026-108108) | High | 7.1 | PHPNuxBill through 2025.3.20 contains an authentication bypass vulnerability in RADIUS CHAP verification because Passwo… |
| 2026-10-09 15:17:12 | [CVE-2026-108109](https://nvd.nist.gov/vuln/detail/CVE-2026-108109) | Critical | 9.3 | PHPNuxBill through 2025.3.20 contains an account takeover vulnerability in the customer password reset flow in system/c… |
| 2026-10-09 15:17:12 | [CVE-2026-108124](https://nvd.nist.gov/vuln/detail/CVE-2026-108124) | Medium | 4.9 | Improper neutralization of special elements used in an SQL command ('SQL injection') vulnerability in wp-post-author. T… |
| 2026-10-09 15:17:12 | [CVE-2026-108125](https://nvd.nist.gov/vuln/detail/CVE-2026-108125) | High | 7.1 | Improper neutralization of special elements used in an SQL command ('SQL injection') vulnerability in wp-post-author. T… |
| 2026-10-09 15:17:13 | [CVE-2026-15340](https://nvd.nist.gov/vuln/detail/CVE-2026-15340) | Critical | 9.3 | lwIP SMTP client does not check the size of inputs, potentially allowing a buffer overflow. |
| 2026-10-09 15:17:13 | [CVE-2026-28745](https://nvd.nist.gov/vuln/detail/CVE-2026-28745) | Critical | 9.3 | Usernames and passwords, including the default credentials, are stored in the configuration file using weak encryption.… |
| 2026-10-09 15:17:13 | [CVE-2026-29797](https://nvd.nist.gov/vuln/detail/CVE-2026-29797) | High | 8.4 | No authentication is required when updating firmware or bootloader, making it easy for malicious files to be pushed to… |
| 2026-10-09 15:17:14 | [CVE-2026-32645](https://nvd.nist.gov/vuln/detail/CVE-2026-32645) | Critical | 9.2 | Default factory credentials with administrative access are enabled and persist even after configuring other administrat… |
| 2026-10-09 15:17:14 | [CVE-2026-33272](https://nvd.nist.gov/vuln/detail/CVE-2026-33272) | Medium | 6.8 | A malicious user with physical access to the device can boot the switch from factory settings without authentication, u… |
| 2026-10-09 15:17:14 | [CVE-2026-33367](https://nvd.nist.gov/vuln/detail/CVE-2026-33367) | Critical | 9.3 | SNMP can be used to perform administrative actions such as retrieving configuration files, modifying user accounts or d… |
| 2026-10-09 15:17:14 | [CVE-2026-39453](https://nvd.nist.gov/vuln/detail/CVE-2026-39453) | High | 8.5 | Navigating to a certain URL on the switch’s web server causes the switch to reboot. This can be automated using a tool… |
| 2026-10-09 15:17:14 | [CVE-2026-39460](https://nvd.nist.gov/vuln/detail/CVE-2026-39460) | Critical | 9.3 | Usernames and passwords, including the default factory credentials, are stored in plaintext within the configuration fi… |
| 2026-10-09 15:17:15 | [CVE-2026-78795](https://nvd.nist.gov/vuln/detail/CVE-2026-78795) |  |  | An issue in Netcore B11 Enterprise-level full Gigabit 9-port shop wireless router v1.3.241114.024540 and before allows… |
| 2026-10-09 15:17:15 | [CVE-2026-78796](https://nvd.nist.gov/vuln/detail/CVE-2026-78796) |  |  | An issue in Netcore B11 Enterprise-level full Gigabit 9-port shop wireless router v1.3.241114.024540 and before allows… |
| 2026-10-09 15:17:20 | [CVE-2026-95702](https://nvd.nist.gov/vuln/detail/CVE-2026-95702) | High | 8.5 | Use-after-free vulnerability in VFS in Google gVisor prior to release 20260831.0 on all platforms allows a local attack… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
