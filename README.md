# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-19 01:19 UTC

New CVEs published between 2026-10-19 00:18 UTC and 2026-10-19 01:19 UTC.

[Full CSV](data/new-cves-2026-10-19T01-19-12-263747Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-10-19 01:16:36 | [CVE-2026-112033](https://nvd.nist.gov/vuln/detail/CVE-2026-112033) | Low | 2.1 | A security flaw has been discovered in aircheng-org iWebShop-5 up to 5.16. The affected element is the function admin_r… |
| 2026-10-19 01:16:37 | [CVE-2026-112034](https://nvd.nist.gov/vuln/detail/CVE-2026-112034) | Low | 2.1 | A weakness has been identified in aircheng-org iWebShop-5 up to 5.16. The impacted element is the function IController:… |
| 2026-10-19 01:16:37 | [CVE-2026-112035](https://nvd.nist.gov/vuln/detail/CVE-2026-112035) | Low | 2.1 | A security vulnerability has been detected in aircheng-org iWebShop-5 up to 5.16. This affects the function send_messag… |
| 2026-10-19 01:16:37 | [CVE-2026-112036](https://nvd.nist.gov/vuln/detail/CVE-2026-112036) | Low | 2.1 | A vulnerability was detected in Artifex MuPDF up to 1.28.5. This impacts the function free_char_list of the file source… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
