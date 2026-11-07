# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-11-07 14:21 UTC

New CVEs published between 2026-11-07 13:19 UTC and 2026-11-07 14:21 UTC.

[Full CSV](data/new-cves-2026-11-07T14-21-40-772443Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-11-07 14:17:01 | [CVE-2026-120984](https://nvd.nist.gov/vuln/detail/CVE-2026-120984) | Critical | 9.1 | A flaw was found in the Keycloak server's client management component. When a client is created or imported with author… |
| 2026-11-07 14:17:01 | [CVE-2026-123966](https://nvd.nist.gov/vuln/detail/CVE-2026-123966) | Critical | 9.3 | A vulnerability was determined in Tenda AC19 16.03.10.07. Affected by this issue is the function saveParentControlInfo… |
| 2026-11-07 14:17:02 | [CVE-2026-123988](https://nvd.nist.gov/vuln/detail/CVE-2026-123988) | Medium | 5.5 | A vulnerability has been found in SililaWijesinghe Food Ordering System up to ba314e897e3365600461e5ea59432e39ceaa0fa5.… |
| 2026-11-07 14:17:02 | [CVE-2026-99271](https://nvd.nist.gov/vuln/detail/CVE-2026-99271) |  |  | In the Linux kernel, the following vulnerability has been resolved: ALSA: line6: Clear prev_fbuf on capture buffer rele… |
| 2026-11-07 14:17:02 | [CVE-2026-99272](https://nvd.nist.gov/vuln/detail/CVE-2026-99272) |  |  | In the Linux kernel, the following vulnerability has been resolved: smb: client: validate the data area in SMB2_read()… |
| 2026-11-07 14:17:02 | [CVE-2026-99273](https://nvd.nist.gov/vuln/detail/CVE-2026-99273) |  |  | In the Linux kernel, the following vulnerability has been resolved: ksmbd: reserve space for the UTF-16 terminator in s… |
| 2026-11-07 14:17:02 | [CVE-2026-99274](https://nvd.nist.gov/vuln/detail/CVE-2026-99274) |  |  | In the Linux kernel, the following vulnerability has been resolved: smb: client: fix fiemap wild read on empty truncate… |
| 2026-11-07 14:17:02 | [CVE-2026-99275](https://nvd.nist.gov/vuln/detail/CVE-2026-99275) |  |  | In the Linux kernel, the following vulnerability has been resolved: smb: client: reject short SESSION_SETUP responses s… |
| 2026-11-07 14:17:02 | [CVE-2026-99276](https://nvd.nist.gov/vuln/detail/CVE-2026-99276) |  |  | In the Linux kernel, the following vulnerability has been resolved: ksmbd: defer connection scavenging while session lo… |
| 2026-11-07 14:17:03 | [CVE-2026-99277](https://nvd.nist.gov/vuln/detail/CVE-2026-99277) |  |  | In the Linux kernel, the following vulnerability has been resolved: ksmbd: hold a connection reference for each session… |
| 2026-11-07 14:17:03 | [CVE-2026-99278](https://nvd.nist.gov/vuln/detail/CVE-2026-99278) |  |  | In the Linux kernel, the following vulnerability has been resolved: ksmbd: limit sessions on each connection The pendin… |
| 2026-11-07 14:17:03 | [CVE-2026-99279](https://nvd.nist.gov/vuln/detail/CVE-2026-99279) |  |  | In the Linux kernel, the following vulnerability has been resolved: ksmbd: reclaim ended sessions on logoff and expirat… |
| 2026-11-07 14:17:03 | [CVE-2026-99280](https://nvd.nist.gov/vuln/detail/CVE-2026-99280) |  |  | In the Linux kernel, the following vulnerability has been resolved: ksmbd: drain session procfs readers before dropping… |
| 2026-11-07 14:17:03 | [CVE-2026-99281](https://nvd.nist.gov/vuln/detail/CVE-2026-99281) |  |  | In the Linux kernel, the following vulnerability has been resolved: tun: Require CAP_NET_ADMIN to attach to an ownerles… |
| 2026-11-07 14:17:03 | [CVE-2026-99282](https://nvd.nist.gov/vuln/detail/CVE-2026-99282) |  |  | In the Linux kernel, the following vulnerability has been resolved: net/sched: sch_teql: fix use-after-free on lower qd… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
