# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-11-15 10:18 UTC

New CVEs published between 2026-11-15 09:20 UTC and 2026-11-15 10:18 UTC.

[Full CSV](data/new-cves-2026-11-15T10-18-42-312261Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-11-15 10:16:53 | [CVE-2026-129349](https://nvd.nist.gov/vuln/detail/CVE-2026-129349) | Critical | 9.1 | When authentication caching is enabled on DefaultLdapRealm, after a user logs in successfully once, subsequent logins f… |
| 2026-11-15 10:16:53 | [CVE-2026-129445](https://nvd.nist.gov/vuln/detail/CVE-2026-129445) | High | 8.4 | A security flaw has been discovered in D-Link DIR-850L FW1.20WWb03. This impacts an unknown function of the file /usr/s… |
| 2026-11-15 10:16:54 | [CVE-2026-82568](https://nvd.nist.gov/vuln/detail/CVE-2026-82568) | High | 7.5 | The Give - Peer-to-Peer plugin for WordPress is vulnerable to time-based SQL Injection via the 'sort' parameter in all… |
| 2026-11-15 10:16:54 | [CVE-2026-82663](https://nvd.nist.gov/vuln/detail/CVE-2026-82663) | High | 7.5 | The Give - Peer-to-Peer plugin for WordPress is vulnerable to authorization bypass in all versions up to, and including… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
