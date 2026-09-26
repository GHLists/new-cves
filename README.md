# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-09-26 18:18 UTC

New CVEs published between 2026-09-26 17:19 UTC and 2026-09-26 18:18 UTC.

[Full CSV](data/new-cves-2026-09-26T18-18-53-19127Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-09-26 18:16:29 | [CVE-2026-77203](https://nvd.nist.gov/vuln/detail/CVE-2026-77203) | High | 8.8 | The Groups – Memberships and Access Control plugin for WordPress is vulnerable to Privilege Escalation in all versions… |
| 2026-09-26 18:16:31 | [CVE-2026-85984](https://nvd.nist.gov/vuln/detail/CVE-2026-85984) | Critical | 9.8 | The miniOrange OTP Login, Verification and SMS Notifications plugin for WordPress is vulnerable to Authentication Bypas… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
