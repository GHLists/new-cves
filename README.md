# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-16 11:20 UTC

New CVEs published between 2026-10-16 10:22 UTC and 2026-10-16 11:20 UTC.

[Full CSV](data/new-cves-2026-10-16T11-20-39-959008Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-10-16 11:17:00 | [CVE-2026-109118](https://nvd.nist.gov/vuln/detail/CVE-2026-109118) | Medium | 4.6 | Improper path containment check in ikus060 rdiffweb 7.1.1 allows an authenticated user to cause the browse, restore, hi… |
| 2026-10-16 11:17:00 | [CVE-2026-109119](https://nvd.nist.gov/vuln/detail/CVE-2026-109119) | High | 8.8 | Improper Privilege Management in the user management API endpoint (/api/users/{username_or_id}) in Rdiffweb allows auth… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
