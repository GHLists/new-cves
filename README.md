# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-11-25 06:20 UTC

New CVEs published between 2026-11-25 05:18 UTC and 2026-11-25 06:20 UTC.

[Full CSV](data/new-cves-2026-11-25T06-20-30-058128Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-11-25 06:17:13 | [CVE-2026-136548](https://nvd.nist.gov/vuln/detail/CVE-2026-136548) | Critical | 9.3 | A vulnerability was identified in Tenda RX3 16.03.13.11. The affected element is an unknown function of the file /bin/a… |
| 2026-11-25 06:17:15 | [CVE-2026-136549](https://nvd.nist.gov/vuln/detail/CVE-2026-136549) | Critical | 9.3 | A security flaw has been discovered in Tenda RX3 16.03.13.11_multi. The impacted element is the function formSetSafeWan… |
| 2026-11-25 06:17:15 | [CVE-2026-136550](https://nvd.nist.gov/vuln/detail/CVE-2026-136550) | High | 8.5 | A weakness has been identified in Tenda RX3 16.03.13.11_multi. This affects the function fromAdvSetMacMtuWan of the fil… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
