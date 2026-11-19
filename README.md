# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-11-19 05:19 UTC

New CVEs published between 2026-11-19 04:19 UTC and 2026-11-19 05:19 UTC.

[Full CSV](data/new-cves-2026-11-19T05-19-05-062587Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-11-19 05:18:24 | [CVE-2026-104357](https://nvd.nist.gov/vuln/detail/CVE-2026-104357) | Medium | 4.8 | A flaw was found in libtirpc. The SunRPC UDP/datagram server transport reuses a single receive buffer across requests a… |
| 2026-11-19 05:18:33 | [CVE-2026-130888](https://nvd.nist.gov/vuln/detail/CVE-2026-130888) | Medium | 6.1 | A flaw was found in nbdkit. The qcow2dec filter's zstd_compressed_cluster() function incorrectly sets the ZSTD input bu… |
| 2026-11-19 05:18:37 | [CVE-2026-132625](https://nvd.nist.gov/vuln/detail/CVE-2026-132625) | Medium | 5.5 | A vulnerability was determined in SourceCodester Student Project Allocation and Management System 1.0. Affected is an u… |
| 2026-11-19 05:18:38 | [CVE-2026-132626](https://nvd.nist.gov/vuln/detail/CVE-2026-132626) | Medium | 5.5 | A vulnerability was identified in SourceCodester Modern Ticket Reservation System 1.0. Affected by this vulnerability i… |
| 2026-11-19 05:18:38 | [CVE-2026-132627](https://nvd.nist.gov/vuln/detail/CVE-2026-132627) | Medium | 5.5 | A security flaw has been discovered in SourceCodester E-Commerce Shopping Cart Web Application 1.0. Affected by this is… |
| 2026-11-19 05:18:38 | [CVE-2026-132802](https://nvd.nist.gov/vuln/detail/CVE-2026-132802) | Critical | 9.9 | A malicious actor with access to the network and low privileges could exploit an Improper Link Resolution Before File A… |
| 2026-11-19 05:18:38 | [CVE-2026-132803](https://nvd.nist.gov/vuln/detail/CVE-2026-132803) | Critical | 9.9 | A malicious actor with access to the network and low privileges could exploit a series of authenticated SQL Injection v… |
| 2026-11-19 05:18:38 | [CVE-2026-132804](https://nvd.nist.gov/vuln/detail/CVE-2026-132804) | Critical | 9.9 | A malicious actor with access to the network and low privileges could exploit a Server-Side Request Forgery (SSRF) vuln… |
| 2026-11-19 05:18:39 | [CVE-2026-132806](https://nvd.nist.gov/vuln/detail/CVE-2026-132806) | High | 8.8 | A malicious actor with access to the network and low privileges could exploit an authenticated SQL Injection vulnerabil… |
| 2026-11-19 05:18:39 | [CVE-2026-132807](https://nvd.nist.gov/vuln/detail/CVE-2026-132807) | Critical | 9.0 | A malicious actor with access to the network and under certain conditions could exploit an Improper Certificate Validat… |
| 2026-11-19 05:18:39 | [CVE-2026-132808](https://nvd.nist.gov/vuln/detail/CVE-2026-132808) | Critical | 9.9 | A malicious actor with access to the network and low privileges could exploit an Incorrect Authorization vulnerability… |
| 2026-11-19 05:18:39 | [CVE-2026-132805](https://nvd.nist.gov/vuln/detail/CVE-2026-132805) | High | 8.3 | A malicious actor with access to the network could exploit a Server-Side Request Forgery (SSRF) vulnerability found in… |
| 2026-11-19 05:18:40 | [CVE-2026-84998](https://nvd.nist.gov/vuln/detail/CVE-2026-84998) | High | 7.2 | The NextScripts: Social Networks Auto-Poster plugin for WordPress is vulnerable to Stored Cross-Site Scripting via 'com… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
