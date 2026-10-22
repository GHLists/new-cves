# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-22 17:22 UTC

New CVEs published between 2026-10-22 16:21 UTC and 2026-10-22 17:22 UTC.

[Full CSV](data/new-cves-2026-10-22T17-22-03-139413Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-10-22 17:16:56 | [CVE-2026-104068](https://nvd.nist.gov/vuln/detail/CVE-2026-104068) | High | 8.6 | JetBackup plugin for WordPress before 3.1.24.10 contains a symlink-based arbitrary file write vulnerability that allows… |
| 2026-10-22 17:16:58 | [CVE-2026-114605](https://nvd.nist.gov/vuln/detail/CVE-2026-114605) | High | 7.5 | dnspython is a DNS toolkit for Python. Prior to 2.9.0, dns.name.from_wire_parser follows attacker-controlled DNS compre… |
| 2026-10-22 17:16:58 | [CVE-2026-114606](https://nvd.nist.gov/vuln/detail/CVE-2026-114606) | Medium | 5.6 | draw.io Desktop is the official Electron build of draw.io. Prior to 31.4.4, draw.io Desktop is vulnerable to arbitrary… |
| 2026-10-22 17:16:58 | [CVE-2026-114607](https://nvd.nist.gov/vuln/detail/CVE-2026-114607) | Critical | 9.1 | Better Auth is an authentication and authorization library for TypeScript. From 1.4.0-beta.18 until 1.7.7, deployments… |
| 2026-10-22 17:16:58 | [CVE-2026-114608](https://nvd.nist.gov/vuln/detail/CVE-2026-114608) | Medium | 5.4 | Pylint is a static code analyser for Python. From 0.15.2 until 4.0.9, Pylint stores module statistics in predictable fi… |
| 2026-10-22 17:16:58 | [CVE-2026-115416](https://nvd.nist.gov/vuln/detail/CVE-2026-115416) | Medium | 6.3 | Incorrect authorization checks in Amazon Athena engine version 3 query processing could have allowed an authenticated u… |
| 2026-10-22 17:16:59 | [CVE-2026-115502](https://nvd.nist.gov/vuln/detail/CVE-2026-115502) | Medium | 6.3 | A missing authorization check allows anyone having access to a "link without login" for a DataApp to list and potential… |
| 2026-10-22 17:16:59 | [CVE-2026-115513](https://nvd.nist.gov/vuln/detail/CVE-2026-115513) | Medium | 6.3 | OpenCATS before 0.12.0 contains a stored cross-site scripting vulnerability that allows a low-privileged authenticated… |
| 2026-10-22 17:16:59 | [CVE-2026-67597](https://nvd.nist.gov/vuln/detail/CVE-2026-67597) |  |  | Rejected reason: This CVE ID has been rejected or withdrawn by its CVE Numbering Authority. |
| 2026-10-22 17:16:59 | [CVE-2026-75507](https://nvd.nist.gov/vuln/detail/CVE-2026-75507) | High | 7.5 | GraphQL-core is a Python port of the GraphQL.js reference implementation. From 3.0.0 until 3.2.12 and 3.3.0rc1, the Ove… |
| 2026-10-22 17:16:59 | [CVE-2026-75508](https://nvd.nist.gov/vuln/detail/CVE-2026-75508) | High | 7.5 | GraphQL-core is a Python port of the GraphQL.js reference implementation. From 3.2.3 until 3.2.12 and 3.3.0rc1, the par… |
| 2026-10-22 17:17:02 | [CVE-2026-97631](https://nvd.nist.gov/vuln/detail/CVE-2026-97631) | Critical | 9.5 | EDK2 contains a vulnerability in BIOS where a user may cause “Out-of-bounds Write”, Classic Buffer Overflow, and “Incor… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
