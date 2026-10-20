# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-20 14:20 UTC

New CVEs published between 2026-10-20 13:18 UTC and 2026-10-20 14:20 UTC.

[Full CSV](data/new-cves-2026-10-20T14-20-46-282955Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-10-20 14:16:54 | [CVE-2026-101296](https://nvd.nist.gov/vuln/detail/CVE-2026-101296) |  |  | A missing critical step in authentication vulnerability in Apache Tomcat when the JNDI realm was configured with with a… |
| 2026-10-20 14:16:55 | [CVE-2026-101356](https://nvd.nist.gov/vuln/detail/CVE-2026-101356) |  |  | Incorrect object recycling and re-use vulnerability in Apache Tomcat affecting HTTP/2 processing of asynchronous servle… |
| 2026-10-20 14:16:56 | [CVE-2026-103119](https://nvd.nist.gov/vuln/detail/CVE-2026-103119) |  |  | Buffer under-read vulnerability in Apache Tomcat meant that a large non-blocking write could result in the response bod… |
| 2026-10-20 14:16:58 | [CVE-2026-113393](https://nvd.nist.gov/vuln/detail/CVE-2026-113393) | Low | 2.1 | A vulnerability was determined in DrayTek Vigor2960 1.5.1.6 Revision 8218. This issue affects some unknown processing o… |
| 2026-10-20 14:16:59 | [CVE-2026-113394](https://nvd.nist.gov/vuln/detail/CVE-2026-113394) | Low | 2.1 | A vulnerability was identified in DrayTek Vigor2960 1.5.1.6 Revision 8218. Impacted is the function setSWMProfile of th… |
| 2026-10-20 14:16:59 | [CVE-2026-113395](https://nvd.nist.gov/vuln/detail/CVE-2026-113395) | Low | 2.1 | A security flaw has been discovered in DrayTek Vigor2960 1.5.1.6 Revision 8218. The affected element is the function cg… |
| 2026-10-20 14:16:59 | [CVE-2026-113396](https://nvd.nist.gov/vuln/detail/CVE-2026-113396) | Low | 2.1 | A weakness has been identified in DrayTek Vigor2960 1.5.1.6 Revision 8218. The impacted element is the function rename_… |
| 2026-10-20 14:17:00 | [CVE-2026-74048](https://nvd.nist.gov/vuln/detail/CVE-2026-74048) |  |  | Not Failing Securely ('Failing Open') vulnerability in Apache Tomcat. If the OpenSSLLifecycleListener is configured to… |
| 2026-10-20 14:17:00 | [CVE-2026-74049](https://nvd.nist.gov/vuln/detail/CVE-2026-74049) |  |  | Execution After Redirect (EAR) vulnerability in Apache Tomcat. This issue affects Apache Tomcat: from 11.0.0-M1 through… |
| 2026-10-20 14:17:03 | [CVE-2026-80353](https://nvd.nist.gov/vuln/detail/CVE-2026-80353) |  |  | Time-of-check time-of-use (TOCTOU) race condition vulnerability in Apache Tomcat when creating unix domain sockets for… |
| 2026-10-20 14:17:04 | [CVE-2026-88041](https://nvd.nist.gov/vuln/detail/CVE-2026-88041) |  |  | Incomplete cleanup vulnerability in Apache Tomcat allowed an trailer information from a previous request to leak into a… |
| 2026-10-20 14:17:04 | [CVE-2026-91041](https://nvd.nist.gov/vuln/detail/CVE-2026-91041) | High | 7.8 | Mounting an attacker-controlled FAT image with fault tolerance enabled causes an out-of-bounds heap write during log re… |
| 2026-10-20 14:17:04 | [CVE-2026-93446](https://nvd.nist.gov/vuln/detail/CVE-2026-93446) |  |  | Incomplete cleanup vulnerability in Apache Tomcat could cause TLS 1.3 connections to fail intermittently. This issue af… |
| 2026-10-20 14:17:04 | [CVE-2026-96406](https://nvd.nist.gov/vuln/detail/CVE-2026-96406) | Medium | 4.9 | A VideoStreaming interface reports the size of its whole class-specific descriptor block in the `wTotalLength` field of… |
| 2026-10-20 14:17:04 | [CVE-2026-96582](https://nvd.nist.gov/vuln/detail/CVE-2026-96582) | Medium | 4.9 | A HID report descriptor is a sequence of items, each declaring in its header how many data bytes follow. The USBX host… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
