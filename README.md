# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-09-29 22:22 UTC

New CVEs published between 2026-09-29 21:22 UTC and 2026-09-29 22:22 UTC.

[Full CSV](data/new-cves-2026-09-29T22-22-41-465863Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-09-29 22:17:07 | [CVE-2026-102621](https://nvd.nist.gov/vuln/detail/CVE-2026-102621) | Low | 1.9 | A vulnerability was identified in Freedesktop Poppler up to 26.08.0. Affected is the function SplashClip::clipToPath of… |
| 2026-09-29 22:17:08 | [CVE-2026-102771](https://nvd.nist.gov/vuln/detail/CVE-2026-102771) | Low | 2.0 | A security vulnerability has been detected in Naichen ThinkCMF up to 8.0.7. Affected by this issue is the function Mail… |
| 2026-09-29 22:17:11 | [CVE-2026-63713](https://nvd.nist.gov/vuln/detail/CVE-2026-63713) | High | 8.5 | The "search" parameter in the view audit logs feature within the utilities section is susceptible to a time-based blind… |
| 2026-09-29 22:17:15 | [CVE-2026-68068](https://nvd.nist.gov/vuln/detail/CVE-2026-68068) | High | 8.5 | The "screenID" parameter in the electronic transaction queue viewer feature within the manual transactions section is s… |
| 2026-09-29 22:17:21 | [CVE-2026-68954](https://nvd.nist.gov/vuln/detail/CVE-2026-68954) | High | 8.5 | The "pattern" parameter used in search function in the home page of the TMS application is vulnerable to time-based bli… |
| 2026-09-29 22:17:58 | [CVE-2026-69662](https://nvd.nist.gov/vuln/detail/CVE-2026-69662) | Low | 2.1 | The application uses unsafe functions that allow execution of inline scripts and string evaluation functions. |
| 2026-09-29 22:18:16 | [CVE-2026-70356](https://nvd.nist.gov/vuln/detail/CVE-2026-70356) | Critical | 9.4 | The TMS file upload endpoint fails to enforce server-side file type restrictions, allowing an attacker to upload and ex… |
| 2026-09-29 22:18:18 | [CVE-2026-71189](https://nvd.nist.gov/vuln/detail/CVE-2026-71189) | Medium | 4.8 | An attacker can construct a request that, if issued by another application user, will cause JavaScript code supplied by… |
| 2026-09-29 22:18:18 | [CVE-2026-71302](https://nvd.nist.gov/vuln/detail/CVE-2026-71302) | High | 7.5 | The application accepts user-supplied session identifiers and does not regenerate the session ID after authentication.… |
| 2026-09-29 22:18:21 | [CVE-2026-71379](https://nvd.nist.gov/vuln/detail/CVE-2026-71379) | Critical | 10.0 | The file export endpoint allows any unauthenticated attacker to export arbitrary database tables by sending a crafted P… |
| 2026-09-29 22:18:21 | [CVE-2026-71971](https://nvd.nist.gov/vuln/detail/CVE-2026-71971) | High | 8.8 | U-Boot before 2026.10-rc3 with CONFIG_IP_DEFRAG enabled contains an out-of-bounds write vulnerability in the __net_defr… |
| 2026-09-29 22:18:21 | [CVE-2026-71972](https://nvd.nist.gov/vuln/detail/CVE-2026-71972) | Medium | 6.0 | U-Boot through 2026.10-rc5 contains an out-of-bounds write vulnerability in the video_display_rle8_bitmap function in d… |
| 2026-09-29 22:18:22 | [CVE-2026-71973](https://nvd.nist.gov/vuln/detail/CVE-2026-71973) | Medium | 5.2 | U-Boot before 2026.10-rc4 contains an integer overflow vulnerability in sqfs_read_directory_table() function when alloc… |
| 2026-09-29 22:18:22 | [CVE-2026-71974](https://nvd.nist.gov/vuln/detail/CVE-2026-71974) | Medium | 4.3 | U-Boot before 2026.10-rc3 contains an out-of-bounds write vulnerability in read_slotted_partition() that fails to valid… |
| 2026-09-29 22:18:22 | [CVE-2026-72507](https://nvd.nist.gov/vuln/detail/CVE-2026-72507) | High | 8.5 | The "reportType" parameter in the product summary report feature within the balancing reports section is susceptible to… |
| 2026-09-29 22:18:22 | [CVE-2026-72510](https://nvd.nist.gov/vuln/detail/CVE-2026-72510) | High | 8.5 | The "supplier_no" parameter used in the business allocation search feature is vulnerable to time-based blind SQL inject… |
| 2026-09-29 22:18:33 | [CVE-2026-74220](https://nvd.nist.gov/vuln/detail/CVE-2026-74220) | High | 8.8 | U-Boot before 2026.10-rc5 contains a buffer overflow in nfs_read_reply() function in net/nfs-common.c that allows attac… |
| 2026-09-29 22:18:33 | [CVE-2026-74221](https://nvd.nist.gov/vuln/detail/CVE-2026-74221) | High | 8.8 | U-Boot before 2026.10-rc5 contains a buffer overflow in nfs_readlink_reply() function in net/nfs-common.c when processi… |
| 2026-09-29 22:18:33 | [CVE-2026-74222](https://nvd.nist.gov/vuln/detail/CVE-2026-74222) | High | 8.8 | U-Boot before 2026.10-rc5 contains a use-after-free vulnerability in the httpc_recv_cb() function within the lwIP wget… |
| 2026-09-29 22:18:33 | [CVE-2026-74225](https://nvd.nist.gov/vuln/detail/CVE-2026-74225) | High | 7.1 | U-Boot before 2026.10-rc5 contains out-of-bounds memory access in dhcp6_parse_options() that fails to validate SERVERID… |
| 2026-09-29 22:19:01 | [CVE-2026-84409](https://nvd.nist.gov/vuln/detail/CVE-2026-84409) | High | 7.7 | The device's update mechanism retrieves metadata for software updates over an unencrypted HTTP connection and stores po… |
| 2026-09-29 22:19:03 | [CVE-2026-91191](https://nvd.nist.gov/vuln/detail/CVE-2026-91191) | High | 7.7 | The device's update mechanism includes conditions that allow unauthorized software packages to be accepted as authentic… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
