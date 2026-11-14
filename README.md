# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-11-14 13:20 UTC

New CVEs published between 2026-11-14 12:18 UTC and 2026-11-14 13:20 UTC.

[Full CSV](data/new-cves-2026-11-14T13-20-34-19873Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-11-14 13:17:19 | [CVE-2025-71464](https://nvd.nist.gov/vuln/detail/CVE-2025-71464) | Medium | 5.3 | @kolkov/angular-editor before 3.0.4 contains a cross-site scripting vulnerability in toggleEditorMode() that assigns so… |
| 2026-11-14 13:17:20 | [CVE-2025-71465](https://nvd.nist.gov/vuln/detail/CVE-2025-71465) | Medium | 5.3 | @kolkov/angular-editor before 3.0.3 contains a cross-site scripting vulnerability in refreshView() that writes HTML fro… |
| 2026-11-14 13:17:20 | [CVE-2026-120522](https://nvd.nist.gov/vuln/detail/CVE-2026-120522) | Critical | 9.8 | The Cloud Storage Manager for Fluent Forms – Google Drive, Dropbox, OneDrive, S3 Uploads plugin for WordPress is vulner… |
| 2026-11-14 13:17:21 | [CVE-2026-129254](https://nvd.nist.gov/vuln/detail/CVE-2026-129254) | Low | 2.1 | A flaw has been found in Opixido OCMS up to b7c15660aba83d96677c1a9abaa69c082a24f21c. This impacts an unknown function… |
| 2026-11-14 13:17:21 | [CVE-2026-129255](https://nvd.nist.gov/vuln/detail/CVE-2026-129255) | Critical | 9.3 | A vulnerability was identified in CoolerMaster MASTERPLUS+ 1.9.6. This affects the function sub_11504 in the library Wi… |
| 2026-11-14 13:17:22 | [CVE-2026-129428](https://nvd.nist.gov/vuln/detail/CVE-2026-129428) | Medium | 5.3 | Pulse from 5.0.17 before 6.8.0 contains a missing authorization vulnerability in the /api/ai/approvals endpoints that a… |
| 2026-11-14 13:17:22 | [CVE-2026-129429](https://nvd.nist.gov/vuln/detail/CVE-2026-129429) | High | 7.1 | Frappe india-payroll before 16.0.4 contains a missing authorization vulnerability in the get_employee_details, compute_… |
| 2026-11-14 13:17:22 | [CVE-2026-129430](https://nvd.nist.gov/vuln/detail/CVE-2026-129430) | Medium | 5.1 | Axeloz Filesharing before 2.14.3 contains a stored cross-site scripting vulnerability that allows authenticated users t… |
| 2026-11-14 13:17:22 | [CVE-2026-129431](https://nvd.nist.gov/vuln/detail/CVE-2026-129431) | High | 7.1 | Ettercap through 0.8.5.1 contains a heap out-of-bounds read vulnerability in dissector_socks() in src/dissectors/ec_soc… |
| 2026-11-14 13:17:22 | [CVE-2026-129432](https://nvd.nist.gov/vuln/detail/CVE-2026-129432) | High | 7.1 | Ettercap through 0.8.5.1 contains a heap out-of-bounds read vulnerability in dissector_mountd() in src/dissectors/ec_mo… |
| 2026-11-14 13:17:22 | [CVE-2026-129433](https://nvd.nist.gov/vuln/detail/CVE-2026-129433) | Critical | 9.4 | Dokploy before 0.31.1 contains an OS command injection vulnerability in getComposeContainerCommand() that allows authen… |
| 2026-11-14 13:17:22 | [CVE-2026-18053](https://nvd.nist.gov/vuln/detail/CVE-2026-18053) | High | 8.8 | The MemberDash plugin for WordPress is vulnerable to Privilege Escalation in all versions up to, and including, 1.8.7.… |
| 2026-11-14 13:17:23 | [CVE-2026-19907](https://nvd.nist.gov/vuln/detail/CVE-2026-19907) | Critical | 9.8 | The Shipo plugin for WordPress is vulnerable to Authentication Bypass in versions 1.6 through 1.8.0. This is due to the… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
