# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-09-30 07:18 UTC

New CVEs published between 2026-09-30 06:19 UTC and 2026-09-30 07:18 UTC.

[Full CSV](data/new-cves-2026-09-30T07-18-38-317667Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-09-30 07:16:30 | [CVE-2026-89294](https://nvd.nist.gov/vuln/detail/CVE-2026-89294) | High | 7.5 | The Simply Schedule Appointments plugin for WordPress is vulnerable to Local File Inclusion in all versions up to, and… |
| 2026-09-30 07:16:31 | [CVE-2026-97196](https://nvd.nist.gov/vuln/detail/CVE-2026-97196) | Critical | 9.1 | Improper Validation of Unsafe Equivalence in Input vulnerability in Liquid Web / StellarWP GiveWP allows Authentication… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
