# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-24 15:18 UTC

New CVEs published between 2026-10-24 14:18 UTC and 2026-10-24 15:18 UTC.

[Full CSV](data/new-cves-2026-10-24T15-18-42-121305Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-10-24 15:17:33 | [CVE-2026-115557](https://nvd.nist.gov/vuln/detail/CVE-2026-115557) | Critical | 9.4 | Python has added a denylist for known compromised certificates to the "ssl" module to ensure user safety even without c… |
| 2026-10-24 15:17:33 | [CVE-2026-115933](https://nvd.nist.gov/vuln/detail/CVE-2026-115933) | Critical | 9.9 | Postiz signs its session, invitation and password reset tokens with one shared secret and without any marker of what a… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
