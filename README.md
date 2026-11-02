# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-11-02 21:18 UTC

New CVEs published between 2026-11-02 20:18 UTC and 2026-11-02 21:18 UTC.

[Full CSV](data/new-cves-2026-11-02T21-18-35-073913Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-11-02 21:17:22 | [CVE-2026-105475](https://nvd.nist.gov/vuln/detail/CVE-2026-105475) | High | 8.7 | Improper neutralization of a NUL byte in cPanel allows remote attackers to read any mail account's calendar and contact… |
| 2026-11-02 21:17:22 | [CVE-2026-105476](https://nvd.nist.gov/vuln/detail/CVE-2026-105476) |  |  | Improper link resolution before file access in cPanel allows remote authenticated users to write arbitrary root-owned f… |
| 2026-11-02 21:17:24 | [CVE-2026-116766](https://nvd.nist.gov/vuln/detail/CVE-2026-116766) | High | 8.3 | CVE-2026-116766 is an improper input handling vulnerability in the Secure Access server versions between 13.0 and prior… |
| 2026-11-02 21:17:25 | [CVE-2026-116767](https://nvd.nist.gov/vuln/detail/CVE-2026-116767) | High | 7.1 | CVE-2026-116767 is an improper input handling vulnerability in Secure Access servers prior to 14.61. Authenticated atta… |
| 2026-11-02 21:17:25 | [CVE-2026-116768](https://nvd.nist.gov/vuln/detail/CVE-2026-116768) | High | 7.1 | CVE-2026-116768 is a missing length validation vulnerability in Secure Access servers prior to 14.61. Authenticated att… |
| 2026-11-02 21:17:25 | [CVE-2026-116958](https://nvd.nist.gov/vuln/detail/CVE-2026-116958) | Medium | 6.7 | A flaw was found in konflux-ci. This vulnerability allows arbitrary code execution due to improper quoting of shell var… |
| 2026-11-02 21:17:30 | [CVE-2026-120503](https://nvd.nist.gov/vuln/detail/CVE-2026-120503) | Low | 1.9 | A vulnerability was detected in EchoHS GeekezBrowser up to 1.7.2/1.8.0. This affects an unknown part of the file /api/s… |
| 2026-11-02 21:17:30 | [CVE-2026-16305](https://nvd.nist.gov/vuln/detail/CVE-2026-16305) |  |  | Local privilege escalation in `SmartUpdate.exe` and `SmartExecute.exe` in INFINITT Healthcare Co., Ltd. INFINITT PACS a… |
| 2026-11-02 21:17:31 | [CVE-2026-29508](https://nvd.nist.gov/vuln/detail/CVE-2026-29508) | High | 8.7 | ReadyMedia (formerly MiniDLNA) versions 1.3.0 through 1.3.3 contain a stack-based buffer overflow vulnerability that al… |
| 2026-11-02 21:17:31 | [CVE-2026-49903](https://nvd.nist.gov/vuln/detail/CVE-2026-49903) |  |  | The `ClusterRenderingService.dump()` method, accessible to processes holding `android.permission.DUMP` and `android.per… |
| 2026-11-02 21:17:31 | [CVE-2026-49906](https://nvd.nist.gov/vuln/detail/CVE-2026-49906) |  |  | An unprivileged application can bypass the `android.car.permission.CAR_DISPLAY_IN_CLUSTER` permission by registering an… |
| 2026-11-02 21:17:35 | [CVE-2026-58873](https://nvd.nist.gov/vuln/detail/CVE-2026-58873) |  |  | In addDragDropListener of WindowManagerService.java, there is a possible permission bypass due to a missing permission… |
| 2026-11-02 21:17:35 | [CVE-2026-58915](https://nvd.nist.gov/vuln/detail/CVE-2026-58915) |  |  | A physical occupant on an Android Automotive OS (AAOS) Multi-User Multi-Display (MUMD) passenger display can view sensi… |
| 2026-11-02 21:17:35 | [CVE-2026-58924](https://nvd.nist.gov/vuln/detail/CVE-2026-58924) |  |  | The vulnerability is a heap out-of-bounds read in the EVS HAL's `getStreamList()` method. An attacker can craft a `Came… |
| 2026-11-02 21:17:36 | [CVE-2026-58925](https://nvd.nist.gov/vuln/detail/CVE-2026-58925) |  |  | The report details a heap Use-After-Free (UAF) vulnerability within the `android.hardware.automotive.evs-default` HAL s… |
| 2026-11-02 21:17:36 | [CVE-2026-58926](https://nvd.nist.gov/vuln/detail/CVE-2026-58926) |  |  | A Use-After-Free (UAF) vulnerability exists in the EVS HAL, allowing a privileged client to free a `buffer_handle_t` wh… |
| 2026-11-02 21:17:36 | [CVE-2026-58927](https://nvd.nist.gov/vuln/detail/CVE-2026-58927) |  |  | The vulnerability is a Use-After-Free (UAF) in the EVS AIDL HAL, arising from a data race on an unsynchronized `std::we… |
| 2026-11-02 21:17:36 | [CVE-2026-58930](https://nvd.nist.gov/vuln/detail/CVE-2026-58930) |  |  | An unprivileged application can exploit a lack of package/signature validation in SystemUI's `RemoteQCController` when… |
| 2026-11-02 21:17:37 | [CVE-2026-58977](https://nvd.nist.gov/vuln/detail/CVE-2026-58977) |  |  | In is_valid_header of timed_cache_item.c, there is a possible out-of-bounds write due to a missing bounds check. This c… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
