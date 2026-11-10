# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-11-10 10:19 UTC

New CVEs published between 2026-11-10 09:20 UTC and 2026-11-10 10:19 UTC.

[Full CSV](data/new-cves-2026-11-10T10-19-44-852627Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-11-10 10:16:42 | [CVE-2026-104619](https://nvd.nist.gov/vuln/detail/CVE-2026-104619) | High | 7.8 | Untrusted users could roll back security updates when using the PackageKit Zypp Backend before 1.4.1, allowing privileg… |
| 2026-11-10 10:16:43 | [CVE-2026-124503](https://nvd.nist.gov/vuln/detail/CVE-2026-124503) | Low | 2.1 | A vulnerability was identified in sooperset mcp-atlassian up to 0.24.0. This issue affects the function validate_safe_p… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
