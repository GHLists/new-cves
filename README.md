# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-15 22:19 UTC

New CVEs published between 2026-10-15 21:19 UTC and 2026-10-15 22:19 UTC.

[Full CSV](data/new-cves-2026-10-15T22-19-08-126647Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-10-15 22:18:06 | [CVE-2024-58397](https://nvd.nist.gov/vuln/detail/CVE-2024-58397) | Medium | 6.9 | MP4v2 through 2.1.3 contains a heap-based out-of-bounds read in MP4File::GetChapters() that allows attackers to read pa… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
