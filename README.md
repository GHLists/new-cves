# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-09-30 04:19 UTC

New CVEs published between 2026-09-30 03:20 UTC and 2026-09-30 04:19 UTC.

[Full CSV](data/new-cves-2026-09-30T04-19-45-17184Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-09-30 04:18:27 | [CVE-2026-102910](https://nvd.nist.gov/vuln/detail/CVE-2026-102910) | Medium | 5.5 | A security flaw has been discovered in SourceCodester Online Reviewer Management System 1.0. The affected element is an… |
| 2026-09-30 04:18:28 | [CVE-2026-102911](https://nvd.nist.gov/vuln/detail/CVE-2026-102911) | High | 8.6 | A flaw has been found in zosmaai pi-llm-wiki up to 0.11.7. Affected is an unknown function of the file mcp/index.ts of… |
| 2026-09-30 04:18:28 | [CVE-2026-102912](https://nvd.nist.gov/vuln/detail/CVE-2026-102912) | Low | 2.0 | A vulnerability was identified in SourceCodester Online Leave Management System 1.0. This issue affects some unknown pr… |
| 2026-09-30 04:18:29 | [CVE-2026-103110](https://nvd.nist.gov/vuln/detail/CVE-2026-103110) | Critical | 9.8 | Pexip Infinity before 38.2, plus 39.0, 39.1 and 40.0, is affected by improper input validation that allows a remote att… |
| 2026-09-30 04:18:33 | [CVE-2026-86134](https://nvd.nist.gov/vuln/detail/CVE-2026-86134) | High | 8.7 | A NULL pointer dereference vulnerability in the WatchGuard Fireware OS authentication process allows a remote, unauthen… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
