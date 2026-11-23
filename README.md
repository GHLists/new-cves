# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-11-23 12:18 UTC

New CVEs published between 2026-11-23 11:18 UTC and 2026-11-23 12:18 UTC.

[Full CSV](data/new-cves-2026-11-23T12-18-31-493032Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-11-23 12:18:15 | [CVE-2026-101282](https://nvd.nist.gov/vuln/detail/CVE-2026-101282) | Medium | 5.8 | Mattermost versions 11.7.x <= 11.7.13, 11.10.x <= 11.10.3, 11.11.x <= 11.11.3 fail to mark the plugin configuration set… |
| 2026-11-23 12:18:16 | [CVE-2026-134890](https://nvd.nist.gov/vuln/detail/CVE-2026-134890) | Medium | 5.3 | A security flaw has been discovered in osCommerce 4.14.63493. Affected by this issue is the function save_products of t… |
| 2026-11-23 12:18:16 | [CVE-2026-134891](https://nvd.nist.gov/vuln/detail/CVE-2026-134891) | Medium | 6.9 | A weakness has been identified in osCommerce 4.14.63493. This affects the function actionGiftCard of the file lib/front… |
| 2026-11-23 12:18:16 | [CVE-2026-134892](https://nvd.nist.gov/vuln/detail/CVE-2026-134892) | Medium | 5.5 | A security vulnerability has been detected in SourceCodester Cosmetics and Beauty Product Online Store 1.0. This vulner… |
| 2026-11-23 12:18:16 | [CVE-2026-134924](https://nvd.nist.gov/vuln/detail/CVE-2026-134924) | Medium | 5.3 | A vulnerability was identified in chillzhuang SpringBlade up to 5.0.2. This impacts the function AvueIframe of the file… |
| 2026-11-23 12:18:16 | [CVE-2026-13408](https://nvd.nist.gov/vuln/detail/CVE-2026-13408) | Low | 3.1 | Mattermost versions 11.7.x <= 11.7.13 fail to verify that the requesting user has read permission for a post's channel… |
| 2026-11-23 12:18:17 | [CVE-2026-19531](https://nvd.nist.gov/vuln/detail/CVE-2026-19531) | Medium | 6.5 | Mattermost versions 11.7.x <= 11.7.13, 11.10.x <= 11.10.3, 11.11.x <= 11.11.3 fail to verify that the requesting user h… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
