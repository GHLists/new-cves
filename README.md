# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-11-05 00:21 UTC

New CVEs published between 2026-11-04 23:19 UTC and 2026-11-05 00:21 UTC.

[Full CSV](data/new-cves-2026-11-05T00-21-07-382852Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-11-05 00:17:22 | [CVE-2026-122049](https://nvd.nist.gov/vuln/detail/CVE-2026-122049) | Low | 2.9 | A flaw has been found in Campcodes Bitcoin Wallet System 1.0. This affects the function random_int of the file core/app… |
| 2026-11-05 00:17:23 | [CVE-2026-122050](https://nvd.nist.gov/vuln/detail/CVE-2026-122050) | Medium | 5.5 | A vulnerability was found in Campcodes Complete Sales and Inventory System with Credit Management 1.0. This issue affec… |
| 2026-11-05 00:17:24 | [CVE-2026-122051](https://nvd.nist.gov/vuln/detail/CVE-2026-122051) | Critical | 9.3 | A flaw has been found in Edimax BR-6208AC 1.32. Affected by this vulnerability is an unknown functionality of the file… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
