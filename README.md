# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-11-01 12:19 UTC

New CVEs published between 2026-11-01 11:18 UTC and 2026-11-01 12:19 UTC.

[Full CSV](data/new-cves-2026-11-01T12-19-57-069854Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-11-01 11:18:57 | [CVE-2026-120224](https://nvd.nist.gov/vuln/detail/CVE-2026-120224) | High | 8.6 | A security flaw has been discovered in Oray Pugongying X5 Pro up to 7.6.1. Affected is the function run_apis_by_json/ru… |
| 2026-11-01 11:18:57 | [CVE-2026-120225](https://nvd.nist.gov/vuln/detail/CVE-2026-120225) | High | 8.5 | A weakness has been identified in Oray Pugongying X5 Pro up to 7.6.1. Affected by this vulnerability is the function co… |
| 2026-11-01 11:18:58 | [CVE-2026-13575](https://nvd.nist.gov/vuln/detail/CVE-2026-13575) |  |  | HTTP::Session versions before 0.54 for Perl allow memcached command injection via unfiltered session ids in HTTP::Sessi… |
| 2026-11-01 12:17:09 | [CVE-2026-120226](https://nvd.nist.gov/vuln/detail/CVE-2026-120226) | Low | 1.9 | A security vulnerability has been detected in Hangzhou Xiongmai Technology P2PAPI.dll 1.3.3.32 on Windows. Affected by… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
