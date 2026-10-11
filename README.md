# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-11 16:19 UTC

New CVEs published between 2026-10-11 15:18 UTC and 2026-10-11 16:19 UTC.

[Full CSV](data/new-cves-2026-10-11T16-19-25-450979Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-10-11 16:16:30 | [CVE-2026-107761](https://nvd.nist.gov/vuln/detail/CVE-2026-107761) | Medium | 5.3 | Several Postiz endpoints return the complete database row of the record they operate on instead of only the fields the… |
| 2026-10-11 16:16:31 | [CVE-2026-108913](https://nvd.nist.gov/vuln/detail/CVE-2026-108913) | High | 7.1 | omarchy-theme-set in Omarchy 4 before 4.0.1 allows code execution via a third-party theme because the files placed into… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
