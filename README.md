# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-11-02 00:20 UTC

New CVEs published between 2026-11-01 23:18 UTC and 2026-11-02 00:20 UTC.

[Full CSV](data/new-cves-2026-11-02T00-20-37-349426Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-11-02 00:18:09 | [CVE-2026-120276](https://nvd.nist.gov/vuln/detail/CVE-2026-120276) | Critical | 9.3 | A weakness has been identified in WAVLINK WN536AX6-A V260507_2.0.0. This vulnerability affects the function sub_416760… |
| 2026-11-02 00:18:10 | [CVE-2026-120277](https://nvd.nist.gov/vuln/detail/CVE-2026-120277) | Critical | 9.3 | A security vulnerability has been detected in WAVLINK WN536AX6-A V260507_2.0.0. This issue affects the function sub_41a… |
| 2026-11-02 00:18:11 | [CVE-2026-120278](https://nvd.nist.gov/vuln/detail/CVE-2026-120278) | Medium | 5.5 | A vulnerability was detected in WAVLINK WN536AX6-A V260507_2.0.0. Impacted is the function sub_416d48/sub_41a7c0 of the… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
