# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-11-01 15:18 UTC

New CVEs published between 2026-11-01 14:18 UTC and 2026-11-01 15:18 UTC.

[Full CSV](data/new-cves-2026-11-01T15-18-11-574752Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-11-01 14:18:51 | [CVE-2026-117680](https://nvd.nist.gov/vuln/detail/CVE-2026-117680) | Low | 2.1 | Improper Check for Unusual or Exceptional Conditions vulnerability in the pattern and patternProperties keywords in lud… |
| 2026-11-01 14:18:52 | [CVE-2026-120228](https://nvd.nist.gov/vuln/detail/CVE-2026-120228) | High | 8.6 | A flaw has been found in WAVLINK WN553X1-B V260403_2.0.0. This vulnerability affects the function sub_416D88 of the fil… |
| 2026-11-01 14:18:53 | [CVE-2026-120229](https://nvd.nist.gov/vuln/detail/CVE-2026-120229) | High | 8.5 | A vulnerability has been found in WAVLINK WN553X1-B 260403_2.0.0. This issue affects the function sub_416B50 of the fil… |
| 2026-11-01 15:17:22 | [CVE-2026-120230](https://nvd.nist.gov/vuln/detail/CVE-2026-120230) | High | 8.6 | A vulnerability was found in WAVLINK WN701AE 260105. Impacted is the function del_vlan_group of the component ioos Web… |
| 2026-11-01 15:17:23 | [CVE-2026-120231](https://nvd.nist.gov/vuln/detail/CVE-2026-120231) | High | 8.6 | A vulnerability was determined in WAVLINK WN553X1-B V260403_2.0.0. The affected element is the function sub_416568 of t… |
| 2026-11-01 15:17:23 | [CVE-2026-120232](https://nvd.nist.gov/vuln/detail/CVE-2026-120232) | High | 8.5 | A vulnerability was identified in Horizon DataSys Reboot Restore Standard up to 13.2. The impacted element is the funct… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
