# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-09-29 10:18 UTC

New CVEs published between 2026-09-29 09:20 UTC and 2026-09-29 10:18 UTC.

[Full CSV](data/new-cves-2026-09-29T10-18-59-39317Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-09-29 10:17:10 | [CVE-2026-102473](https://nvd.nist.gov/vuln/detail/CVE-2026-102473) | Medium | 5.5 | A flaw was found in dash. When built without libc fnmatch, the internal pmatch() matcher implements * by unbounded recu… |
| 2026-09-29 10:17:10 | [CVE-2026-102474](https://nvd.nist.gov/vuln/detail/CVE-2026-102474) | Medium | 4.0 | A flaw was found in dash. The printf builtin reserves four bytes before converting a Unicode \u or \U escape, but the m… |
| 2026-09-29 10:17:10 | [CVE-2026-10518](https://nvd.nist.gov/vuln/detail/CVE-2026-10518) | Medium | 4.3 | GitLab has remediated an issue in GitLab EE affecting all versions from 17.9 before 19.2.7, 19.3 before 19.3.3, and 19.… |
| 2026-09-29 10:17:11 | [CVE-2026-11796](https://nvd.nist.gov/vuln/detail/CVE-2026-11796) | Medium | 5.1 | Asset Suite allows unauthenticated users to access PropertiesReloadServlet, CacheFlushServlet, MetadataCacheFlushServle… |
| 2026-09-29 10:17:11 | [CVE-2026-15390](https://nvd.nist.gov/vuln/detail/CVE-2026-15390) | Critical | 9.0 | Das U-Boot with CONFIG_IP_DEFRAG=y parameter fails to clear IP reassembly state after delivering a complete datagram. A… |
| 2026-09-29 10:17:11 | [CVE-2026-19547](https://nvd.nist.gov/vuln/detail/CVE-2026-19547) | High | 7.0 | Ghostscript for Windows is vulnerable to local privilege escalation through PostScript resource file hijacking. Due to… |
| 2026-09-29 10:17:11 | [CVE-2026-4523](https://nvd.nist.gov/vuln/detail/CVE-2026-4523) | Low | 3.7 | GitLab has remediated an issue in GitLab CE/EE affecting all versions from 15.11 before 19.2.7, 19.3 before 19.3.3, and… |
| 2026-09-29 10:17:11 | [CVE-2026-76718](https://nvd.nist.gov/vuln/detail/CVE-2026-76718) | High | 8.2 | A potential security vulnerability in HPE OneView can be exploited to allow remote session hijacking or other unauthori… |
| 2026-09-29 10:17:11 | [CVE-2026-76719](https://nvd.nist.gov/vuln/detail/CVE-2026-76719) | High | 8.2 | A security vulnerability in HPE OneView may be exploited remotely to perform session hijacking, data theft or other una… |
| 2026-09-29 10:17:12 | [CVE-2026-76720](https://nvd.nist.gov/vuln/detail/CVE-2026-76720) | Medium | 4.3 | A vulnerability in HPE OneView can be remotely exploited to cause a URL redirect. |
| 2026-09-29 10:17:12 | [CVE-2026-7395](https://nvd.nist.gov/vuln/detail/CVE-2026-7395) | High | 8.5 | Asset Suite allows unauthenticated users to access HTTPPublishAdapterTestServlet that can be used for configuration fil… |
| 2026-09-29 10:17:12 | [CVE-2026-81862](https://nvd.nist.gov/vuln/detail/CVE-2026-81862) |  |  | Apache Airflow's Teradata provider embedded cloud storage credentials directly into SQL statements. `S3ToTeradataOperat… |
| 2026-09-29 10:17:12 | [CVE-2026-81914](https://nvd.nist.gov/vuln/detail/CVE-2026-81914) |  |  | Apache Airflow's Google provider built Google Drive search expressions by interpolating file and folder names directly… |
| 2026-09-29 10:17:12 | [CVE-2026-81930](https://nvd.nist.gov/vuln/detail/CVE-2026-81930) |  |  | Apache Airflow's Snowflake provider did not validate the connection's `account` and `region` fields before interpolatin… |
| 2026-09-29 10:17:12 | [CVE-2026-84739](https://nvd.nist.gov/vuln/detail/CVE-2026-84739) | High | 8.7 | GitLab has remediated an issue in GitLab CE/EE affecting all versions from 13.11 before 19.2.7, 19.3 before 19.3.3, and… |
| 2026-09-29 10:17:12 | [CVE-2026-86843](https://nvd.nist.gov/vuln/detail/CVE-2026-86843) |  |  | The Apache Airflow Teradata provider's compute-cluster example Dag declared every one of its Dag Params as unconstraine… |
| 2026-09-29 10:17:13 | [CVE-2026-8065](https://nvd.nist.gov/vuln/detail/CVE-2026-8065) | Critical | 9.1 | An authentication bypass vulnerability in the firmware update endpoint of Hitachi Energy RTU500 allows an unauthenticat… |
| 2026-09-29 10:17:13 | [CVE-2026-8066](https://nvd.nist.gov/vuln/detail/CVE-2026-8066) | Critical | 9.1 | A directory traversal vulnerability in the file upload functionality of Hitachi Energy RTU500 allows an unauthenticated… |
| 2026-09-29 10:17:13 | [CVE-2026-8067](https://nvd.nist.gov/vuln/detail/CVE-2026-8067) | Medium | 6.5 | An improper authorization vulnerability in the RTU500’s web application allows an authenticated user to trigger the RTU… |
| 2026-09-29 10:17:13 | [CVE-2026-8937](https://nvd.nist.gov/vuln/detail/CVE-2026-8937) | Medium | 4.3 | GitLab has remediated an issue in GitLab CE/EE affecting all versions from 19.0 before 19.2.7, 19.3 before 19.3.3, and… |
| 2026-09-29 10:17:14 | [CVE-2026-95386](https://nvd.nist.gov/vuln/detail/CVE-2026-95386) | Medium | 5.5 | TTL file parser infinite loop in 4.6.0 to 4.6.8 allows denial of service |
| 2026-09-29 10:17:14 | [CVE-2026-95387](https://nvd.nist.gov/vuln/detail/CVE-2026-95387) | High | 8.1 | SPDY protocol dissector crash in 4.6.0 to 4.6.8 and 4.4.0 to 4.4.18 allows denial of service |
| 2026-09-29 10:17:14 | [CVE-2026-95388](https://nvd.nist.gov/vuln/detail/CVE-2026-95388) | Medium | 5.5 | Sharkd utility crash in 4.6.0 to 4.6.8 and 4.4.0 to 4.4.18 allows denial of service |
| 2026-09-29 10:17:15 | [CVE-2026-95389](https://nvd.nist.gov/vuln/detail/CVE-2026-95389) | High | 8.1 | SCTP protocol dissector crash in 4.6.0 to 4.6.8 and 4.4.0 to 4.4.18 allows denial of service |
| 2026-09-29 10:17:15 | [CVE-2026-95390](https://nvd.nist.gov/vuln/detail/CVE-2026-95390) | Medium | 5.5 | PEAK CAN TRC file parser crash in 4.6.0 to 4.6.8 allows denial of service |
| 2026-09-29 10:17:15 | [CVE-2026-95391](https://nvd.nist.gov/vuln/detail/CVE-2026-95391) | Medium | 5.5 | ZigBee ZCL protocol dissector crash in 4.6.0 to 4.6.8 allows denial of service |
| 2026-09-29 10:17:15 | [CVE-2026-95392](https://nvd.nist.gov/vuln/detail/CVE-2026-95392) | Medium | 5.5 | MBIM protocol dissector crash in 4.6.0 to 4.6.8 and 4.4.0 to 4.4.18 allows denial of service |
| 2026-09-29 10:17:15 | [CVE-2026-95393](https://nvd.nist.gov/vuln/detail/CVE-2026-95393) | Medium | 4.7 | CSN.1 protocol dissector crash in 4.6.0 to 4.6.8 and 4.4.0 to 4.4.18 allows denial of service |
| 2026-09-29 10:17:15 | [CVE-2026-95394](https://nvd.nist.gov/vuln/detail/CVE-2026-95394) | Medium | 4.7 | Microsoft Network Monitor file parser large loop in 4.6.0 to 4.6.8 and 4.4.0 to 4.4.18 allows denial of service |
| 2026-09-29 10:17:15 | [CVE-2026-95395](https://nvd.nist.gov/vuln/detail/CVE-2026-95395) | Medium | 5.5 | IEEE C37.118 Synchrophasor protocol dissector memory leak in 4.6.0 to 4.6.8 and 4.4.0 to 4.4.18 allows denial of service |
| 2026-09-29 10:17:16 | [CVE-2026-96415](https://nvd.nist.gov/vuln/detail/CVE-2026-96415) | Medium | 5.5 | Catapult DCT2000 protocol dissector crash in 4.6.0 to 4.6.8 and 4.4.0 to 4.4.18 allows denial of service |
| 2026-09-29 10:17:16 | [CVE-2026-96416](https://nvd.nist.gov/vuln/detail/CVE-2026-96416) | Medium | 5.5 | IEEE 802.11 protocol dissector crash in 4.6.0 to 4.6.8 and 4.4.0 to 4.4.18 allows denial of service |
| 2026-09-29 10:17:16 | [CVE-2026-96417](https://nvd.nist.gov/vuln/detail/CVE-2026-96417) | Medium | 5.5 | RF4CE protocol dissector crash in 4.6.0 to 4.6.8 and 4.4.0 to 4.4.18 allows denial of service |
| 2026-09-29 10:17:16 | [CVE-2026-96418](https://nvd.nist.gov/vuln/detail/CVE-2026-96418) | Medium | 5.5 | TIFF protocol dissector infinite loop in 4.6.0 to 4.6.8 and 4.4.0 to 4.4.18 allows denial of service |
| 2026-09-29 10:17:16 | [CVE-2026-96419](https://nvd.nist.gov/vuln/detail/CVE-2026-96419) | Medium | 5.5 | Profile import crash in 4.6.0 to 4.6.8 and 4.4.0 to 4.4.18 allows denial of service and possible code execution |
| 2026-09-29 10:17:16 | [CVE-2026-96420](https://nvd.nist.gov/vuln/detail/CVE-2026-96420) | Medium | 4.7 | Toshiba file parser crash in 4.6.0 to 4.6.8 and 4.4.0 to 4.4.18 allows denial of service |
| 2026-09-29 10:17:16 | [CVE-2026-96421](https://nvd.nist.gov/vuln/detail/CVE-2026-96421) | Medium | 5.5 | USB HID protocol dissector infinite loop and memory leak in 4.6.0 to 4.6.8 and 4.4.0 to 4.4.18 allows denial of service |
| 2026-09-29 10:17:17 | [CVE-2026-96422](https://nvd.nist.gov/vuln/detail/CVE-2026-96422) | Medium | 5.5 | Frame protocol metadissector crash in 4.6.0 to 4.6.8 and 4.4.0 to 4.4.18 allows denial of service |
| 2026-09-29 10:17:17 | [CVE-2026-96423](https://nvd.nist.gov/vuln/detail/CVE-2026-96423) | Medium | 5.5 | X11 protocol dissector crash in 4.6.0 to 4.6.8 and 4.4.0 to 4.4.18 allows denial of service |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
