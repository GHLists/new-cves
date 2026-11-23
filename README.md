# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-11-23 22:18 UTC

New CVEs published between 2026-11-23 21:21 UTC and 2026-11-23 22:18 UTC.

[Full CSV](data/new-cves-2026-11-23T22-18-37-837396Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-11-23 22:18:29 | [CVE-2026-109480](https://nvd.nist.gov/vuln/detail/CVE-2026-109480) | Critical | 9.6 | Server-side request forgery in Profile Data Roaming Service (PDRS) allows an authorized attacker to elevate privileges… |
| 2026-11-23 22:18:30 | [CVE-2026-109490](https://nvd.nist.gov/vuln/detail/CVE-2026-109490) | Critical | 9.3 | Improper neutralization of input during web page generation ('cross-site scripting') in Authentication Methods Portal E… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
