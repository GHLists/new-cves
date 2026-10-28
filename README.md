# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-28 02:20 UTC

New CVEs published between 2026-10-28 01:20 UTC and 2026-10-28 02:20 UTC.

[Full CSV](data/new-cves-2026-10-28T02-20-07-148876Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-10-28 02:17:01 | [CVE-2026-106013](https://nvd.nist.gov/vuln/detail/CVE-2026-106013) | Critical | 9.8 | The Jupiter X Core plugin for WordPress is vulnerable to Authentication Bypass via the Twitter/X Social Login handler i… |
| 2026-10-28 02:17:07 | [CVE-2026-118271](https://nvd.nist.gov/vuln/detail/CVE-2026-118271) | Low | 2.1 | A security vulnerability has been detected in a2ui-project a2ui up to 0.10.6. This impacts an unknown function of the f… |
| 2026-10-28 02:17:07 | [CVE-2026-118272](https://nvd.nist.gov/vuln/detail/CVE-2026-118272) | Low | 2.1 | A vulnerability was detected in a2ui-project a2ui up to 0.10.6. Affected is the function DataContext.dispatchExpression… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
