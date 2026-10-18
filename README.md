# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-18 01:18 UTC

New CVEs published between 2026-10-18 00:20 UTC and 2026-10-18 01:18 UTC.

[Full CSV](data/new-cves-2026-10-18T01-18-43-601872Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-10-18 01:16:34 | [CVE-2026-111868](https://nvd.nist.gov/vuln/detail/CVE-2026-111868) | Low | 2.1 | A vulnerability was determined in datastax pulsar-jms up to 9.0.3. This issue affects the function decode of the file p… |
| 2026-10-18 01:16:35 | [CVE-2026-111997](https://nvd.nist.gov/vuln/detail/CVE-2026-111997) | Medium | 6.3 | ip-address before 10.7.4 allows a denial of service (CPU consumption from quadratic complexity, and application stall)… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
