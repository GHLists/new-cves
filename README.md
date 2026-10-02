# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-02 04:18 UTC

New CVEs published between 2026-10-02 03:19 UTC and 2026-10-02 04:18 UTC.

[Full CSV](data/new-cves-2026-10-02T04-18-34-312987Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-10-02 04:18:06 | [CVE-2026-14378](https://nvd.nist.gov/vuln/detail/CVE-2026-14378) | Critical | 9.8 | The DevKit Pro plugin for WordPress is vulnerable to Authentication Bypass Leading to Administrator Account Takeover in… |
| 2026-10-02 04:18:09 | [CVE-2026-93367](https://nvd.nist.gov/vuln/detail/CVE-2026-93367) | High | 7.2 | The Visitors Traffic Real Time Statistics Pro plugin for WordPress is vulnerable to unauthenticated stored Cross-Site S… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
