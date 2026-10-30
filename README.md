# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-30 05:19 UTC

New CVEs published between 2026-10-30 04:18 UTC and 2026-10-30 05:19 UTC.

[Full CSV](data/new-cves-2026-10-30T05-19-49-979715Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-10-30 05:16:57 | [CVE-2026-103963](https://nvd.nist.gov/vuln/detail/CVE-2026-103963) | High | 7.5 | A flaw was found in glib-networking. When establishing connections using Transport Layer Security (TLS) version 1.3, th… |
| 2026-10-30 05:16:57 | [CVE-2026-104368](https://nvd.nist.gov/vuln/detail/CVE-2026-104368) | High | 8.8 | The Export and Import Users and Customers plugin for WordPress is vulnerable to Privilege Escalation in all versions up… |
| 2026-10-30 05:16:59 | [CVE-2026-5461](https://nvd.nist.gov/vuln/detail/CVE-2026-5461) | Medium | 6.5 | The Forminator Forms plugin for WordPress is vulnerable to Limited File Deletion in all versions up to, and including,… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
