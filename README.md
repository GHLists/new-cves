# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-15 11:20 UTC

New CVEs published between 2026-10-15 10:21 UTC and 2026-10-15 11:20 UTC.

[Full CSV](data/new-cves-2026-10-15T11-20-24-03048Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-10-15 11:17:19 | [CVE-2026-108491](https://nvd.nist.gov/vuln/detail/CVE-2026-108491) | High | 7.1 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in Everest Forms Eve… |
| 2026-10-15 11:17:19 | [CVE-2026-108497](https://nvd.nist.gov/vuln/detail/CVE-2026-108497) | Critical | 9.3 | Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection') vulnerability in TMS Amelia amelia… |
| 2026-10-15 11:17:19 | [CVE-2026-108498](https://nvd.nist.gov/vuln/detail/CVE-2026-108498) | High | 7.1 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in bannersky BSK PDF… |
| 2026-10-15 11:17:24 | [CVE-2026-109694](https://nvd.nist.gov/vuln/detail/CVE-2026-109694) | Critical | 9.8 | Incorrect Privilege Assignment vulnerability in WP ManageNinja LLC Fluent CRM fluent-crm allows Privilege Escalation.Th… |
| 2026-10-15 11:17:27 | [CVE-2026-109695](https://nvd.nist.gov/vuln/detail/CVE-2026-109695) | High | 7.5 | Insertion of Sensitive Information Into Sent Data vulnerability in WPManageNinja FluentCart fluent-cart allows Retrieve… |
| 2026-10-15 11:17:28 | [CVE-2026-17525](https://nvd.nist.gov/vuln/detail/CVE-2026-17525) | Medium | 5.1 | Incomplete cleanup vulnerability in ABB My Control System. This issue affects My Control System: 26.4 and 26.5. |
| 2026-10-15 11:17:50 | [CVE-2026-79830](https://nvd.nist.gov/vuln/detail/CVE-2026-79830) | Medium | 6.6 | A vulnerability in HPE NonStop Kernel Level Thread Model Lib can cause stack buffer overflow which can allow arbitrary… |
| 2026-10-15 11:17:50 | [CVE-2026-79831](https://nvd.nist.gov/vuln/detail/CVE-2026-79831) | Medium | 6.6 | A heap buffer overflow in HPE NonStop Posix User Threads may allow arbitrary code execution. |
| 2026-10-15 11:17:50 | [CVE-2026-79832](https://nvd.nist.gov/vuln/detail/CVE-2026-79832) | High | 7.6 | A stack buffer overflow vulnerability in HPE NonStop SQL/MX Executor may potentially result in information disclosure o… |
| 2026-10-15 11:17:50 | [CVE-2026-79833](https://nvd.nist.gov/vuln/detail/CVE-2026-79833) | High | 7.5 | A vulnerability in HPE NonStop ANSI SQLUTIL may allow a remote unauthenticated actor to cause an affected service to te… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
