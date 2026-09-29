# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-09-29 11:18 UTC

New CVEs published between 2026-09-29 10:18 UTC and 2026-09-29 11:18 UTC.

[Full CSV](data/new-cves-2026-09-29T11-18-59-277993Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-09-29 11:16:43 | [CVE-2026-95509](https://nvd.nist.gov/vuln/detail/CVE-2026-95509) | High | 8.8 | Strings optimized for Latin-1 displaying Latin-1 characters cause incorrect String.arg() formatting by an incorrect buf… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
