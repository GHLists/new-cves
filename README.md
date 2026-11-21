# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-11-21 04:20 UTC

New CVEs published between 2026-11-21 03:19 UTC and 2026-11-21 04:20 UTC.

[Full CSV](data/new-cves-2026-11-21T04-20-14-123773Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-11-21 04:17:20 | [CVE-2026-131651](https://nvd.nist.gov/vuln/detail/CVE-2026-131651) | Medium | 6.4 | The rtMedia for WordPress, BuddyPress and bbPress plugin for WordPress is vulnerable to Stored DOM-Based Cross-Site Scr… |
| 2026-11-21 04:17:20 | [CVE-2026-19793](https://nvd.nist.gov/vuln/detail/CVE-2026-19793) | High | 8.8 | The WP Import Export Lite plugin for WordPress is vulnerable to Limited Code Injection in all versions up to, and inclu… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
