# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-07 11:20 UTC

New CVEs published between 2026-10-07 10:20 UTC and 2026-10-07 11:20 UTC.

[Full CSV](data/new-cves-2026-10-07T11-20-08-728673Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-10-07 11:17:09 | [CVE-2026-103668](https://nvd.nist.gov/vuln/detail/CVE-2026-103668) | High | 8.8 | An SQL Injection vulnerability exists in the Site Search function of Movable Type, which may allow an unauthenticated a… |
| 2026-10-07 11:17:19 | [CVE-2026-42713](https://nvd.nist.gov/vuln/detail/CVE-2026-42713) | High | 7.6 | Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection') vulnerability in Gopiplus Post tit… |
| 2026-10-07 11:17:19 | [CVE-2026-42714](https://nvd.nist.gov/vuln/detail/CVE-2026-42714) | High | 7.6 | Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection') vulnerability in Piggly Dev Pix po… |
| 2026-10-07 11:17:20 | [CVE-2026-92531](https://nvd.nist.gov/vuln/detail/CVE-2026-92531) | High | 7.5 | Operating system command injection vulnerability in the SVN integration component of BugTracker.NET. The application in… |
| 2026-10-07 11:17:20 | [CVE-2026-92532](https://nvd.nist.gov/vuln/detail/CVE-2026-92532) | High | 7.5 | Unrestricted file upload vulnerability in the BugTracker.NET attachment functionality. An authenticated user with admin… |
| 2026-10-07 11:17:20 | [CVE-2026-92533](https://nvd.nist.gov/vuln/detail/CVE-2026-92533) | High | 7.1 | Path traversal vulnerability in the BugTracker.NET file download component. The parameter used to specify the file name… |
| 2026-10-07 11:17:20 | [CVE-2026-96408](https://nvd.nist.gov/vuln/detail/CVE-2026-96408) | Critical | 9.3 | A code injection vulnerability exists in the upgrade script of Movable Type, which may allow an unauthenticated attacke… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
