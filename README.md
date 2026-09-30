# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-09-30 14:18 UTC

New CVEs published between 2026-09-30 13:21 UTC and 2026-09-30 14:18 UTC.

[Full CSV](data/new-cves-2026-09-30T14-18-52-891718Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-09-30 14:17:27 | [CVE-2026-103118](https://nvd.nist.gov/vuln/detail/CVE-2026-103118) | Medium | 5.3 | A vulnerability was detected in GraphicsMagick up to 1.3.47. Affected by this vulnerability is the function ExtractPost… |
| 2026-09-30 14:17:31 | [CVE-2026-82307](https://nvd.nist.gov/vuln/detail/CVE-2026-82307) | Critical | 9.8 | Improper neutralization of special elements used in an SQL command ('SQL injection') vulnerability in Dolusoft Software… |
| 2026-09-30 14:17:34 | [CVE-2026-91860](https://nvd.nist.gov/vuln/detail/CVE-2026-91860) | Medium | 6.3 | A prototype pollution vulnerability exists in the deep merge helpers of Vaadin Charts and Vaadin Component Base. Mergin… |
| 2026-09-30 14:17:34 | [CVE-2026-93547](https://nvd.nist.gov/vuln/detail/CVE-2026-93547) | Medium | 5.3 | A missing authorization check in the Vaadin Spreadsheet component allows an authenticated user of an application that r… |
| 2026-09-30 14:17:37 | [CVE-2026-93903](https://nvd.nist.gov/vuln/detail/CVE-2026-93903) | Critical | 9.4 | LiteSpeed Web Server (LSWS) before 6.3.7 build 1 mishandles internal redirect URL validation in a certain "corner case." |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
