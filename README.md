# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-24 22:21 UTC

New CVEs published between 2026-10-24 21:18 UTC and 2026-10-24 22:21 UTC.

[Full CSV](data/new-cves-2026-10-24T22-21-10-179625Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-10-24 22:16:27 | [CVE-2026-115981](https://nvd.nist.gov/vuln/detail/CVE-2026-115981) | Low | 1.9 | A security vulnerability has been detected in phpIPAM up to 1.8.3. Affected by this vulnerability is an unknown functio… |
| 2026-10-24 22:16:27 | [CVE-2026-115982](https://nvd.nist.gov/vuln/detail/CVE-2026-115982) | Low | 2.1 | A vulnerability was detected in phpIPAM up to 1.8.3. Affected by this issue is the function create_rack_link of the fil… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
