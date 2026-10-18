# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-18 15:18 UTC

New CVEs published between 2026-10-18 14:19 UTC and 2026-10-18 15:18 UTC.

[Full CSV](data/new-cves-2026-10-18T15-18-44-985661Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-10-18 15:16:51 | [CVE-2026-110024](https://nvd.nist.gov/vuln/detail/CVE-2026-110024) | Medium | 6.8 | @fastify/jwt is a JWT utility plugin for Fastify. In versions prior to 10.2.5, the top-level sign and verify methods re… |
| 2026-10-18 15:16:52 | [CVE-2026-111988](https://nvd.nist.gov/vuln/detail/CVE-2026-111988) | Medium | 5.3 | A security flaw has been discovered in dyad-sh dyad up to 1.16.0. Affected by this issue is some unknown functionality… |
| 2026-10-18 15:16:52 | [CVE-2026-111990](https://nvd.nist.gov/vuln/detail/CVE-2026-111990) | Medium | 5.5 | A weakness has been identified in kishan0725 Hospital Management System up to 777fda46b77a820977a5ba616283dbfbc40bf7e1.… |
| 2026-10-18 15:16:52 | [CVE-2026-111991](https://nvd.nist.gov/vuln/detail/CVE-2026-111991) | Low | 2.1 | A security vulnerability has been detected in WongKinYiu yolov9 0.1. This vulnerability affects the function DetectMult… |
| 2026-10-18 15:16:53 | [CVE-2026-98433](https://nvd.nist.gov/vuln/detail/CVE-2026-98433) |  |  | In the Linux kernel, the following vulnerability has been resolved: KVM: PPC: Book3S HV: fix secure device page leak on… |
| 2026-10-18 15:16:53 | [CVE-2026-98434](https://nvd.nist.gov/vuln/detail/CVE-2026-98434) |  |  | In the Linux kernel, the following vulnerability has been resolved: sysctl: Check range in proc_dointvec_ms_jiffies_min… |
| 2026-10-18 15:16:53 | [CVE-2026-98436](https://nvd.nist.gov/vuln/detail/CVE-2026-98436) |  |  | In the Linux kernel, the following vulnerability has been resolved: accel/amdxdna: Disable device buffer exporting Devi… |
| 2026-10-18 15:16:53 | [CVE-2026-98435](https://nvd.nist.gov/vuln/detail/CVE-2026-98435) |  |  | In the Linux kernel, the following vulnerability has been resolved: EDAC/altera: Use parent device for devres in altr_p… |
| 2026-10-18 15:16:53 | [CVE-2026-98437](https://nvd.nist.gov/vuln/detail/CVE-2026-98437) |  |  | In the Linux kernel, the following vulnerability has been resolved: media: qcom: iris: fix runtime PM reference leaks U… |
| 2026-10-18 15:16:53 | [CVE-2026-98438](https://nvd.nist.gov/vuln/detail/CVE-2026-98438) |  |  | In the Linux kernel, the following vulnerability has been resolved: mptcp: options: fix uninit-value in mptcp_write_dat… |
| 2026-10-18 15:16:53 | [CVE-2026-98439](https://nvd.nist.gov/vuln/detail/CVE-2026-98439) |  |  | In the Linux kernel, the following vulnerability has been resolved: smb/server: cancel async requests when closing conn… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
