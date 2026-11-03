# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-11-03 01:18 UTC

New CVEs published between 2026-11-03 00:20 UTC and 2026-11-03 01:18 UTC.

[Full CSV](data/new-cves-2026-11-03T01-18-24-206099Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-11-03 01:16:44 | [CVE-2026-105770](https://nvd.nist.gov/vuln/detail/CVE-2026-105770) | Medium | 5.3 | Octo STS (github.com/octo-sts/app) before 0.11.2 returns trust policy configuration to callers whose OIDC token does no… |
| 2026-11-03 01:16:52 | [CVE-2026-120833](https://nvd.nist.gov/vuln/detail/CVE-2026-120833) | High | 8.5 | labbench before 0.46.1 contains a deserialization of untrusted data vulnerability in read() and read_relational() that… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
