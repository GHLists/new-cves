# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-11-19 07:20 UTC

New CVEs published between 2026-11-19 06:21 UTC and 2026-11-19 07:20 UTC.

[Full CSV](data/new-cves-2026-11-19T07-20-50-899339Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-11-19 07:17:08 | [CVE-2026-110461](https://nvd.nist.gov/vuln/detail/CVE-2026-110461) | Critical | 9.3 | The Comelit 1456B Multi-User Gateway, in firmware versions up to and including 2.10.0, is configured with static defaul… |
| 2026-11-19 07:17:09 | [CVE-2026-110462](https://nvd.nist.gov/vuln/detail/CVE-2026-110462) | High | 8.6 | The Comelit 1456B Multi-User Gateway, in firmware versions up to and including 2.10.0, allows a user authenticated to t… |
| 2026-11-19 07:17:11 | [CVE-2026-132825](https://nvd.nist.gov/vuln/detail/CVE-2026-132825) | High | 7.4 | Ruby before 3.3.14, 3.4.13, and 4.0.10 has a heap-based buffer overflow during case conversion. One byte can be written… |
| 2026-11-19 07:17:12 | [CVE-2026-19609](https://nvd.nist.gov/vuln/detail/CVE-2026-19609) | High | 8.6 | Cross-site scripting in the embedded co-browsing feature in Unblu inc. Unblu Spark 7.0 through 7.57.9 and 8.0 before 8.… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
