# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-11-23 20:20 UTC

New CVEs published between 2026-11-23 19:22 UTC and 2026-11-23 20:20 UTC.

[Full CSV](data/new-cves-2026-11-23T20-20-50-690549Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-11-23 20:17:59 | [CVE-2026-12422](https://nvd.nist.gov/vuln/detail/CVE-2026-12422) |  |  | Rejected reason: This issue was not considered a security vulnerability. |
| 2026-11-23 20:17:59 | [CVE-2026-134056](https://nvd.nist.gov/vuln/detail/CVE-2026-134056) | High | 8.3 | An out-of-bounds write issue exists in padded block cipher decryption in AWS-LC. It affects applications that decrypt C… |
| 2026-11-23 20:18:03 | [CVE-2026-135120](https://nvd.nist.gov/vuln/detail/CVE-2026-135120) | Medium | 5.5 | A security flaw has been discovered in RainyGao DocSys up to 2.02.91. Affected by this vulnerability is the function do… |
| 2026-11-23 20:18:03 | [CVE-2026-135126](https://nvd.nist.gov/vuln/detail/CVE-2026-135126) | Low | 2.1 | A weakness has been identified in FredrikNoren ungit 1.5.30. Affected by this issue is the function credentialsOption o… |
| 2026-11-23 20:18:03 | [CVE-2026-135127](https://nvd.nist.gov/vuln/detail/CVE-2026-135127) | Low | 2.1 | A security vulnerability has been detected in FredrikNoren ungit 1.5.30. This affects the function writeUserConfig of t… |
| 2026-11-23 20:18:04 | [CVE-2026-135470](https://nvd.nist.gov/vuln/detail/CVE-2026-135470) | High | 8.7 | WPC Product Options for WooCommerce before 4.0.9 contains a price manipulation vulnerability that allows unauthenticate… |
| 2026-11-23 20:18:04 | [CVE-2026-135471](https://nvd.nist.gov/vuln/detail/CVE-2026-135471) | Medium | 5.1 | Dynamic Product Gallery for WooCommerce before 3.6.2 contains a stored cross-site scripting vulnerability that allows a… |
| 2026-11-23 20:18:05 | [CVE-2026-95793](https://nvd.nist.gov/vuln/detail/CVE-2026-95793) | High | 8.8 | An arbitrary remote code execution vulnerability exists in HPE Morpheus Manager. |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
