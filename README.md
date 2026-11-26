# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-11-26 07:20 UTC

New CVEs published between 2026-11-26 06:19 UTC and 2026-11-26 07:20 UTC.

[Full CSV](data/new-cves-2026-11-26T07-20-19-931762Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-11-26 07:16:36 | [CVE-2017-20291](https://nvd.nist.gov/vuln/detail/CVE-2017-20291) | High | 8.7 | An XML External Entity (XXE) injection vulnerability in the Federation Web Services component (/affwebservices/router/s… |
| 2026-11-26 07:16:40 | [CVE-2026-137312](https://nvd.nist.gov/vuln/detail/CVE-2026-137312) | Medium | 5.5 | A security flaw has been discovered in SourceCodester Online Food Ordering System 1.0. Affected by this issue is some u… |
| 2026-11-26 07:16:41 | [CVE-2026-137313](https://nvd.nist.gov/vuln/detail/CVE-2026-137313) | Low | 2.1 | A weakness has been identified in SourceCodester Online Food Ordering System 1.0. This affects an unknown part of the f… |
| 2026-11-26 07:16:41 | [CVE-2026-137314](https://nvd.nist.gov/vuln/detail/CVE-2026-137314) | Low | 2.0 | A security vulnerability has been detected in SourceCodester Online Food Ordering System 1.0. This vulnerability affect… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
