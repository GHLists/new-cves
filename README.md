# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-27 17:20 UTC

New CVEs published between 2026-10-27 16:19 UTC and 2026-10-27 17:20 UTC.

[Full CSV](data/new-cves-2026-10-27T17-20-28-851714Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-10-27 17:16:53 | [CVE-2025-64394](https://nvd.nist.gov/vuln/detail/CVE-2025-64394) | Medium | 4.3 | A vulnerability allowing a low-privileged local user to write arbitrary files with SYSTEM privileges during the install… |
| 2026-10-27 17:16:54 | [CVE-2026-102636](https://nvd.nist.gov/vuln/detail/CVE-2026-102636) | High | 7.1 | A maliciously crafted HTML payload in a design name, when displayed after another user opens the manipulated design, ca… |
| 2026-10-27 17:16:55 | [CVE-2026-102637](https://nvd.nist.gov/vuln/detail/CVE-2026-102637) | High | 7.1 | A maliciously crafted HTML payload in the documentName parameter of a Fusion protocol URL, when the protocol URL is inv… |
| 2026-10-27 17:16:55 | [CVE-2026-102638](https://nvd.nist.gov/vuln/detail/CVE-2026-102638) | High | 7.1 | A maliciously crafted HTML payload in the description of an electronic library (.lbr) file, when displayed in the Libra… |
| 2026-10-27 17:16:55 | [CVE-2026-104349](https://nvd.nist.gov/vuln/detail/CVE-2026-104349) | High | 7.3 | Creative Cloud Desktop is affected by an Uncontrolled Search Path Element vulnerability that could result in arbitrary… |
| 2026-10-27 17:16:55 | [CVE-2026-104350](https://nvd.nist.gov/vuln/detail/CVE-2026-104350) | Critical | 9.3 | Adobe Campaign Classic (ACC) is affected by a reflected Cross-Site Scripting (XSS) vulnerability. An attacker could exp… |
| 2026-10-27 17:16:55 | [CVE-2026-104351](https://nvd.nist.gov/vuln/detail/CVE-2026-104351) | Critical | 9.9 | Adobe Campaign Classic (ACC) is affected by an Improper Control of Generation of Code ('Code Injection') vulnerability… |
| 2026-10-27 17:16:55 | [CVE-2026-104353](https://nvd.nist.gov/vuln/detail/CVE-2026-104353) | Critical | 9.9 | Adobe Campaign Classic (ACC) is affected by an Improper Neutralization of Special Elements used in an OS Command ('OS C… |
| 2026-10-27 17:16:55 | [CVE-2026-104354](https://nvd.nist.gov/vuln/detail/CVE-2026-104354) | Critical | 9.1 | Adobe Campaign Classic (ACC) is affected by an Improper Neutralization of Special Elements used in an SQL Command ('SQL… |
| 2026-10-27 17:16:55 | [CVE-2026-105477](https://nvd.nist.gov/vuln/detail/CVE-2026-105477) | High | 7.3 | A vulnerability in Veeam Agent for Linux allows for local privilege escalation. Only installations that are managed by… |
| 2026-10-27 17:16:56 | [CVE-2026-105489](https://nvd.nist.gov/vuln/detail/CVE-2026-105489) | Critical | 9.9 | Adobe Campaign Classic (ACC) is affected by an Improper Neutralization of Special Elements used in an SQL Command ('SQL… |
| 2026-10-27 17:16:56 | [CVE-2026-105779](https://nvd.nist.gov/vuln/detail/CVE-2026-105779) | Critical | 9.1 | Adobe Campaign Classic (ACC) is affected by an Improper Neutralization of Special Elements used in an SQL Command ('SQL… |
| 2026-10-27 17:16:56 | [CVE-2026-105780](https://nvd.nist.gov/vuln/detail/CVE-2026-105780) | Critical | 9.9 | Adobe Campaign Classic (ACC) is affected by an Incorrect Authorization vulnerability that could result in arbitrary cod… |
| 2026-10-27 17:16:56 | [CVE-2026-105781](https://nvd.nist.gov/vuln/detail/CVE-2026-105781) | Critical | 10.0 | Adobe Campaign Classic (ACC) is affected by an Improper Neutralization of Special Elements used in an SQL Command ('SQL… |
| 2026-10-27 17:16:56 | [CVE-2026-106076](https://nvd.nist.gov/vuln/detail/CVE-2026-106076) | Critical | 9.0 | A vulnerability allowing an authenticated organization-transfer peer to inject SQL into the configuration database of t… |
| 2026-10-27 17:16:56 | [CVE-2026-106077](https://nvd.nist.gov/vuln/detail/CVE-2026-106077) | High | 8.3 | A vulnerability allowing a user with the Veeam Backup for Microsoft 365 Administrator role to read arbitrary files on t… |
| 2026-10-27 17:16:56 | [CVE-2026-106078](https://nvd.nist.gov/vuln/detail/CVE-2026-106078) | Medium | 6.9 | A vulnerability allowing an unauthenticated attacker to bypass REST API authentication with a forged federation token a… |
| 2026-10-27 17:16:56 | [CVE-2026-107671](https://nvd.nist.gov/vuln/detail/CVE-2026-107671) | High | 8.5 | A vulnerability allowing an attacker with valid Administrator credentials to bypass multi-factor authentication by disa… |
| 2026-10-27 17:16:57 | [CVE-2026-108014](https://nvd.nist.gov/vuln/detail/CVE-2026-108014) | Critical | 9.1 | Private keys for eight eMudhra intermediate CA certificates have been compromised https://emudhra.we-have-a-problem.com… |
| 2026-10-27 17:16:57 | [CVE-2026-108015](https://nvd.nist.gov/vuln/detail/CVE-2026-108015) | Critical | 9.1 | Private keys for eight eMudhra intermediate CA certificates have been compromised https://emudhra.we-have-a-problem.com… |
| 2026-10-27 17:16:57 | [CVE-2026-108140](https://nvd.nist.gov/vuln/detail/CVE-2026-108140) | Medium | 5.9 | A vulnerability allowing an authenticated user with the Restore Operator role, who also controls the contents of a back… |
| 2026-10-27 17:16:57 | [CVE-2026-108141](https://nvd.nist.gov/vuln/detail/CVE-2026-108141) | Medium | 5.9 | A vulnerability allowing an authenticated user with the Restore Operator role, who also controls the contents of a back… |
| 2026-10-27 17:16:57 | [CVE-2026-108142](https://nvd.nist.gov/vuln/detail/CVE-2026-108142) | Critical | 9.1 | A vulnerability allowing an unauthenticated attacker to bypass authorization on the CDP Coordinator Service. |
| 2026-10-27 17:16:57 | [CVE-2026-109088](https://nvd.nist.gov/vuln/detail/CVE-2026-109088) | Medium | 6.5 | A malicious X server could send malformed RECORD EnableContext reolies that can cause a X client using the parse_reply_… |
| 2026-10-27 17:16:57 | [CVE-2026-109089](https://nvd.nist.gov/vuln/detail/CVE-2026-109089) | High | 7.5 | A buffer overflow when handling DEVICE_RESOLUTION in libXi before 1.8.4 could overflow a heap, triggered by a malicious… |
| 2026-10-27 17:16:57 | [CVE-2026-109090](https://nvd.nist.gov/vuln/detail/CVE-2026-109090) | High | 7.5 | A malicious X server could cause a heap overflow by injecting a large DEVICE_ENABLE reply when processed by libXi befor… |
| 2026-10-27 17:16:58 | [CVE-2026-112353](https://nvd.nist.gov/vuln/detail/CVE-2026-112353) | Medium | 6.2 | GFI KerioConnect (Kerio Connect) before 10.0.8 Patch 2 contains a stored cross-site scripting vulnerability in the Webm… |
| 2026-10-27 17:16:58 | [CVE-2026-113775](https://nvd.nist.gov/vuln/detail/CVE-2026-113775) | High | 7.8 | A maliciously crafted dynamic library, when loaded from an arbitrary path through the TextCommands.LoadDll command expo… |
| 2026-10-27 17:16:58 | [CVE-2026-114595](https://nvd.nist.gov/vuln/detail/CVE-2026-114595) | Critical | 9.3 | In EPICS Base release 7.0.10 and prior, an integer overflow in network request processing can cause memory to be alloca… |
| 2026-10-27 17:16:58 | [CVE-2026-114596](https://nvd.nist.gov/vuln/detail/CVE-2026-114596) | High | 8.8 | In EPICS Base release 7.0.10 and prior, an improper validation of message length values during protocol parsing can tri… |
| 2026-10-27 17:16:58 | [CVE-2026-114597](https://nvd.nist.gov/vuln/detail/CVE-2026-114597) | High | 8.7 | In EPICS Base release 7.0.10 and prior, an insufficient validation of element or length values in a network message can… |
| 2026-10-27 17:16:59 | [CVE-2026-114598](https://nvd.nist.gov/vuln/detail/CVE-2026-114598) | High | 8.7 | In EPICS Base release 7.0.10 and prior, an insufficient validation of element or length values in a network message can… |
| 2026-10-27 17:16:59 | [CVE-2026-116672](https://nvd.nist.gov/vuln/detail/CVE-2026-116672) | High | 8.8 | Authlib is a Python library which builds OAuth and OpenID Connect servers. From 0.15 until 1.9.1, the documented Client… |
| 2026-10-27 17:16:59 | [CVE-2026-116673](https://nvd.nist.gov/vuln/detail/CVE-2026-116673) | Low | 3.3 | systeminformation is a System and OS information library for node.js. Prior to 5.33.14, the Linux networkStats(iface) i… |
| 2026-10-27 17:16:59 | [CVE-2026-116674](https://nvd.nist.gov/vuln/detail/CVE-2026-116674) | Medium | 6.5 | systeminformation is a System and OS information library for node.js. Prior to 5.33.13, networkStats(ifaces) in lib/net… |
| 2026-10-27 17:16:59 | [CVE-2026-116675](https://nvd.nist.gov/vuln/detail/CVE-2026-116675) | High | 8.5 | TinyMCE is an open source rich text editor. From 7.9.3 until 7.9.4 and from 8.5.1 until 8.9.3, the media plugin creates… |
| 2026-10-27 17:16:59 | [CVE-2026-117512](https://nvd.nist.gov/vuln/detail/CVE-2026-117512) | Medium | 5.5 | A vulnerability was found in oretnom23 php-travel-agency-system. This affects an unknown part of the file admin/employe… |
| 2026-10-27 17:16:59 | [CVE-2026-117513](https://nvd.nist.gov/vuln/detail/CVE-2026-117513) | Medium | 5.5 | A vulnerability was determined in oretnom23 php-travel-agency-system. This vulnerability affects unknown code of the fi… |
| 2026-10-27 17:17:00 | [CVE-2026-117514](https://nvd.nist.gov/vuln/detail/CVE-2026-117514) | Medium | 5.5 | A vulnerability was identified in oretnom23 php-travel-agency-system. This issue affects some unknown processing of the… |
| 2026-10-27 17:17:00 | [CVE-2026-48360](https://nvd.nist.gov/vuln/detail/CVE-2026-48360) | Critical | 9.6 | Adobe Connect is affected by an Improper Control of Generation of Code ('Code Injection') vulnerability that could resu… |
| 2026-10-27 17:17:00 | [CVE-2026-48379](https://nvd.nist.gov/vuln/detail/CVE-2026-48379) | High | 7.8 | Substance3D - Painter is affected by a Stack-based Buffer Overflow vulnerability that could result in arbitrary code ex… |
| 2026-10-27 17:17:00 | [CVE-2026-48380](https://nvd.nist.gov/vuln/detail/CVE-2026-48380) | Medium | 5.5 | Substance3D - Painter is affected by an out-of-bounds read vulnerability that could lead to disclosure of sensitive mem… |
| 2026-10-27 17:17:01 | [CVE-2026-54462](https://nvd.nist.gov/vuln/detail/CVE-2026-54462) | Medium | 6.5 | Knative pkg provides common packages shared across Knative repositories. Prior to 0.0.0-20260531000007-52dbd5ece63f, th… |
| 2026-10-27 17:17:01 | [CVE-2026-57185](https://nvd.nist.gov/vuln/detail/CVE-2026-57185) | Medium | 6.5 | Asterisk is an open source private branch exchange and telephony toolkit. Prior to Asterisk 20.20.1, 21.12.3, 22.10.1,… |
| 2026-10-27 17:17:01 | [CVE-2026-57189](https://nvd.nist.gov/vuln/detail/CVE-2026-57189) | Low | 2.3 | Asterisk is an open source private branch exchange and telephony toolkit. In affected deployments, an authenticated att… |
| 2026-10-27 17:17:01 | [CVE-2026-57194](https://nvd.nist.gov/vuln/detail/CVE-2026-57194) | Medium | 5.9 | Asterisk is an open source private branch exchange and telephony toolkit. Prior to Asterisk 20.20.1, 21.12.3, 22.10.1,… |
| 2026-10-27 17:17:01 | [CVE-2026-57197](https://nvd.nist.gov/vuln/detail/CVE-2026-57197) | High | 7.7 | Asterisk is an open source private branch exchange and telephony toolkit. Prior to Asterisk 20.20.1, 21.12.3, 22.10.1,… |
| 2026-10-27 17:17:01 | [CVE-2026-57198](https://nvd.nist.gov/vuln/detail/CVE-2026-57198) | Low | 2.3 | Asterisk is an open source private branch exchange and telephony toolkit. In affected deployments, an authenticated att… |
| 2026-10-27 17:17:02 | [CVE-2026-57201](https://nvd.nist.gov/vuln/detail/CVE-2026-57201) | High | 7.5 | Asterisk is an open source private branch exchange and telephony toolkit. Prior to Asterisk 20.20.1, 21.12.3, 22.10.1,… |
| 2026-10-27 17:17:02 | [CVE-2026-67400](https://nvd.nist.gov/vuln/detail/CVE-2026-67400) | Low | 3.5 | A missing token type check allowed to retrieve more additional information about the WOPI configuration with a user or… |
| 2026-10-27 17:17:02 | [CVE-2026-77167](https://nvd.nist.gov/vuln/detail/CVE-2026-77167) | High | 7.5 | Abusing the federated share endpoint, an attacker can write arbitrary rows into the oc_share_external database table. T… |
| 2026-10-27 17:17:02 | [CVE-2026-77171](https://nvd.nist.gov/vuln/detail/CVE-2026-77171) | Low | 3.5 | A public shared collective always allowed recipients of the link to create pages. |
| 2026-10-27 17:17:02 | [CVE-2026-77172](https://nvd.nist.gov/vuln/detail/CVE-2026-77172) | Medium | 5.3 | App passwords were allowed to bypass password confirmation on sensitive endpoints. |
| 2026-10-27 17:17:03 | [CVE-2026-77173](https://nvd.nist.gov/vuln/detail/CVE-2026-77173) | Medium | 4.3 | A user could create a docx or odt file with a # in the filename with confidential information such as a credit card num… |
| 2026-10-27 17:17:03 | [CVE-2026-82983](https://nvd.nist.gov/vuln/detail/CVE-2026-82983) | Low | 3.3 | The Tables app's share-listing endpoint (GET /apps/tables/share/table/{tableId}) did not verify that the requesting use… |
| 2026-10-27 17:17:03 | [CVE-2026-82984](https://nvd.nist.gov/vuln/detail/CVE-2026-82984) | Medium | 4.3 | When a team was configured as "visible to everyone", the web UI correctly blocked non-members from viewing the team ("Y… |
| 2026-10-27 17:17:03 | [CVE-2026-82986](https://nvd.nist.gov/vuln/detail/CVE-2026-82986) | Medium | 4.6 | The user in a group can bypass the group restriction set by an administrator on link sharing, creating share links for… |
| 2026-10-27 17:17:03 | [CVE-2026-87897](https://nvd.nist.gov/vuln/detail/CVE-2026-87897) | Medium | 4.6 | A SSRF vulnerability found that enables access to internal Chrome Devtools Protocol APIs that can leak the JWT authenti… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
