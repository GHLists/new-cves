# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-11-15 03:18 UTC

New CVEs published between 2026-11-15 02:18 UTC and 2026-11-15 03:18 UTC.

[Full CSV](data/new-cves-2026-11-15T03-18-44-587266Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-11-15 03:16:46 | [CVE-2026-129357](https://nvd.nist.gov/vuln/detail/CVE-2026-129357) | Low | 2.1 | A vulnerability was determined in Linux Foundation Magma up to 1.9.0. This issue affects the function hostOrgMiddleware… |
| 2026-11-15 03:16:51 | [CVE-2026-129358](https://nvd.nist.gov/vuln/detail/CVE-2026-129358) | Low | 1.9 | A vulnerability was identified in Linux Foundation Magma up to 1.9.0. Impacted is the function handleReact of the file… |
| 2026-11-15 03:16:51 | [CVE-2026-129359](https://nvd.nist.gov/vuln/detail/CVE-2026-129359) | Medium | 5.5 | A security flaw has been discovered in Linux Foundation Magma up to 1.9.0. The affected element is an unknown function… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
