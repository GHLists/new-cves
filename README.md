# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-11-02 23:18 UTC

New CVEs published between 2026-11-02 22:19 UTC and 2026-11-02 23:18 UTC.

[Full CSV](data/new-cves-2026-11-02T23-18-19-787026Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-11-02 23:17:19 | [CVE-2026-111565](https://nvd.nist.gov/vuln/detail/CVE-2026-111565) |  |  | Rejected reason: This CVE ID has been rejected or withdrawn by its CVE Numbering Authority. |
| 2026-11-02 23:17:19 | [CVE-2026-120597](https://nvd.nist.gov/vuln/detail/CVE-2026-120597) | Low | 2.1 | A vulnerability was identified in Welcart e-Commerce Plugin up to 2.12.6 on WordPress. This affects the function ESCOTT… |
| 2026-11-02 23:17:20 | [CVE-2026-120752](https://nvd.nist.gov/vuln/detail/CVE-2026-120752) | High | 7.7 | PyMuPDF 1.25.3 before 2.0 contains a stack-based buffer overflow vulnerability in JM_set_annot_callout_line() that copi… |
| 2026-11-02 23:17:21 | [CVE-2026-71450](https://nvd.nist.gov/vuln/detail/CVE-2026-71450) | High | 8.7 | Authentication bypass using an alternate path or channel vulnerability in Johnson Controls EasyIO Neo EC and CW Edge Co… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
