# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-11-06 02:18 UTC

New CVEs published between 2026-11-06 01:20 UTC and 2026-11-06 02:18 UTC.

[Full CSV](data/new-cves-2026-11-06T02-18-46-730586Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-11-06 02:17:52 | [CVE-2026-77299](https://nvd.nist.gov/vuln/detail/CVE-2026-77299) | High | 7.5 | Regexp2 is a feature-rich RegExp engine for Go. Prior to version 2.3.0, when regexp2 compiles and matches a pattern con… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
