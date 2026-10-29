# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-29 22:19 UTC

New CVEs published between 2026-10-29 21:19 UTC and 2026-10-29 22:19 UTC.

[Full CSV](data/new-cves-2026-10-29T22-19-15-564597Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-10-29 22:17:00 | [CVE-2026-115943](https://nvd.nist.gov/vuln/detail/CVE-2026-115943) |  |  | Spreadsheet::XLSX versions before 0.19 for Perl allow code execution via string eval of number format conditions in Exc… |
| 2026-10-29 22:17:00 | [CVE-2026-119282](https://nvd.nist.gov/vuln/detail/CVE-2026-119282) | High | 7.3 | Nx is a monorepo solution for TypeScript and polyglot codebases. From 22.0.2 until 22.7.9 and 23.1.2 for @nx/maven, and… |
| 2026-10-29 22:17:01 | [CVE-2026-119283](https://nvd.nist.gov/vuln/detail/CVE-2026-119283) | High | 7.5 | joserfc is a Python library that provides an implementation of several JSON Object Signing and Encryption (JOSE) standa… |
| 2026-10-29 22:17:01 | [CVE-2026-119284](https://nvd.nist.gov/vuln/detail/CVE-2026-119284) | Medium | 6.9 | joserfc is a Python library that provides an implementation of several JSON Object Signing and Encryption (JOSE) standa… |
| 2026-10-29 22:17:01 | [CVE-2026-119285](https://nvd.nist.gov/vuln/detail/CVE-2026-119285) | Medium | 5.9 | Fiber is an Express inspired web framework written in Go. From 2.52.1 until 2.52.3, the CORS middleware's validateDomai… |
| 2026-10-29 22:17:01 | [CVE-2026-119286](https://nvd.nist.gov/vuln/detail/CVE-2026-119286) | High | 7.5 | GraphQL-core is a Python port of the GraphQL.js reference implementation. From 3.3.0a3 until 3.3.1, validate() reuses a… |
| 2026-10-29 22:17:01 | [CVE-2026-119317](https://nvd.nist.gov/vuln/detail/CVE-2026-119317) | Medium | 6.0 | On Linux, an authenticated, low-privileged Nessus user with scan-creation rights could read arbitrary text files on the… |
| 2026-10-29 22:17:02 | [CVE-2026-45049](https://nvd.nist.gov/vuln/detail/CVE-2026-45049) | High | 8.3 | Open Access Management (OpenAM) is an access management solution. Prior to 16.1.1, the `Cross-Domain Single Sign-On` (`… |
| 2026-10-29 22:17:04 | [CVE-2026-61645](https://nvd.nist.gov/vuln/detail/CVE-2026-61645) | Critical | 9.1 | Docat is a tool for hosting versioned static documentation. In the affected implementation, an arbitrary file upload vu… |
| 2026-10-29 22:17:05 | [CVE-2026-61654](https://nvd.nist.gov/vuln/detail/CVE-2026-61654) | High | 8.3 | Lightdash is an open source business intelligence platform. In affected versions through 0.3213.0, the dbt Cloud webhoo… |
| 2026-10-29 22:17:05 | [CVE-2026-61671](https://nvd.nist.gov/vuln/detail/CVE-2026-61671) | High | 8.1 | WeGIA is a web manager for charitable institutions. Prior to the advisory's stated patched version 3.8.7, the `/control… |
| 2026-10-29 22:17:05 | [CVE-2026-61673](https://nvd.nist.gov/vuln/detail/CVE-2026-61673) | Medium | 6.3 | WeGIA is a web manager for charitable institutions. Prior to 3.8.7, a stored DOM cross-site scripting vulnerability in… |
| 2026-10-29 22:17:05 | [CVE-2026-61707](https://nvd.nist.gov/vuln/detail/CVE-2026-61707) | Critical | 9.0 | SOCFortress CoPilot focuses on providing a single pane of glass for all your security operations needs. Prior to 0.1.76… |
| 2026-10-29 22:17:05 | [CVE-2026-61719](https://nvd.nist.gov/vuln/detail/CVE-2026-61719) | High | 8.9 | WeGIA is a web manager for charitable institutions. Prior to 3.8.7, a stored cross-site scripting vulnerability in `sau… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
