# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-11-20 05:20 UTC

New CVEs published between 2026-11-20 04:20 UTC and 2026-11-20 05:20 UTC.

[Full CSV](data/new-cves-2026-11-20T05-20-28-414321Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-11-20 05:18:53 | [CVE-2026-133484](https://nvd.nist.gov/vuln/detail/CVE-2026-133484) | Low | 1.9 | A vulnerability was found in ByteDance Lark Desktop 8.0.0.14. This vulnerability affects the function FUN_18001b770/FUN… |
| 2026-11-20 05:18:54 | [CVE-2026-133486](https://nvd.nist.gov/vuln/detail/CVE-2026-133486) | Low | 2.1 | A vulnerability was identified in hasan-py Hayroo up to fd0fbe763153f72bfaa04ed1e1e4a1bb6f7c61df. Affected by this issu… |
| 2026-11-20 05:18:54 | [CVE-2026-133487](https://nvd.nist.gov/vuln/detail/CVE-2026-133487) | Low | 2.1 | A security flaw has been discovered in nodejs undici up to 7.24.0. This affects the function Object.assign of the file… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
