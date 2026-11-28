# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-11-28 10:21 UTC

New CVEs published between 2026-11-28 09:19 UTC and 2026-11-28 10:21 UTC.

[Full CSV](data/new-cves-2026-11-28T10-21-31-338579Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-11-28 10:17:00 | [CVE-2026-138005](https://nvd.nist.gov/vuln/detail/CVE-2026-138005) | Critical | 9.3 | A vulnerability was detected in TRENDnet TEW-751DR 1.03B01. Affected by this vulnerability is the function gena.php::GE… |
| 2026-11-28 10:17:00 | [CVE-2026-138036](https://nvd.nist.gov/vuln/detail/CVE-2026-138036) | Medium | 5.5 | A vulnerability was detected in Free5GC up to 4.3.0. The impacted element is the function PostPoliciesProcedure of the… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
