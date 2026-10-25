# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-25 00:20 UTC

New CVEs published between 2026-10-24 23:18 UTC and 2026-10-25 00:20 UTC.

[Full CSV](data/new-cves-2026-10-25T00-20-27-489282Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-10-25 00:16:45 | [CVE-2026-115997](https://nvd.nist.gov/vuln/detail/CVE-2026-115997) | Low | 2.1 | A flaw has been found in pig-mesh pig up to 4.1.0. This impacts the function orderItem.getColumn of the file pig-common… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
