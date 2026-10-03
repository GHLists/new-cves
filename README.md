# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-03 02:21 UTC

New CVEs published between 2026-10-03 01:18 UTC and 2026-10-03 02:21 UTC.

[Full CSV](data/new-cves-2026-10-03T02-21-40-056627Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-10-03 02:17:18 | [CVE-2026-105083](https://nvd.nist.gov/vuln/detail/CVE-2026-105083) | Low | 1.8 | ImageMagick before 7.1.2-32 and 6.9.13-57 contains a policy bypass vulnerability in LoadPolicyCache that silently skips… |
| 2026-10-03 02:17:18 | [CVE-2026-105090](https://nvd.nist.gov/vuln/detail/CVE-2026-105090) | Medium | 5.1 | Formbricks before 5.4.4 and 6 before 6.0.1 allows stored XSS. The survey-level Custom Head Scripts feature did not enfo… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
