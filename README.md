# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-04 04:20 UTC

New CVEs published between 2026-10-04 03:19 UTC and 2026-10-04 04:20 UTC.

[Full CSV](data/new-cves-2026-10-04T04-20-58-930319Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-10-04 04:16:36 | [CVE-2026-105098](https://nvd.nist.gov/vuln/detail/CVE-2026-105098) | Low | 2.1 | A security flaw has been discovered in Omega Solution CoinEx Crypto 2025. Affected is an unknown function of the file /… |
| 2026-10-04 04:16:43 | [CVE-2026-88779](https://nvd.nist.gov/vuln/detail/CVE-2026-88779) | High | 8.7 | Vulnerability in NetScaler ADC and NetScaler Gateway. This issue affects ADC: before 14.1-73.41, before 13.1-64.28, bef… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
