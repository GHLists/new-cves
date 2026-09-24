# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-09-24 10:19 UTC

New CVEs published between 2026-09-24 09:19 UTC and 2026-09-24 10:19 UTC.

[Full CSV](data/new-cves-2026-09-24T10-19-20-026335Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-09-24 10:17:32 | [CVE-2026-12227](https://nvd.nist.gov/vuln/detail/CVE-2026-12227) | Critical | 9.8 | The Visual Composer Website Builder plugin for WordPress is vulnerable to Local File Inclusion in all versions up to, a… |
| 2026-09-24 10:17:36 | [CVE-2026-15731](https://nvd.nist.gov/vuln/detail/CVE-2026-15731) | Medium | 6.4 | The WP Multilang – Translation and Multilingual Plugin plugin for WordPress is vulnerable to Stored Cross-Site Scriptin… |
| 2026-09-24 10:17:37 | [CVE-2026-18335](https://nvd.nist.gov/vuln/detail/CVE-2026-18335) | Medium | 5.4 | The Kirki – Freeform Page Builder, Website Builder & Customizer plugin for WordPress is vulnerable to Blind Server-Side… |
| 2026-09-24 10:17:37 | [CVE-2026-4637](https://nvd.nist.gov/vuln/detail/CVE-2026-4637) | Medium | 5.1 | Paessler PRTG Network Monitor before version 26.2.120.1449 is affected by a reflected Cross-Site Scripting (XSS) vulner… |
| 2026-09-24 10:17:38 | [CVE-2026-57590](https://nvd.nist.gov/vuln/detail/CVE-2026-57590) |  |  | A missing authorization vulnerability exists in the Task Group APIs of Apache DolphinScheduler. The affected APIs do no… |
| 2026-09-24 10:17:38 | [CVE-2026-92905](https://nvd.nist.gov/vuln/detail/CVE-2026-92905) | Medium | 5.3 | ZohoCorp ManageEngine EventLog Analyzer and Log360 before build 13071 were vulnerable to a DoS vulnerability that allow… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
