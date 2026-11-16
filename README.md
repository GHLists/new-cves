# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-11-16 02:19 UTC

New CVEs published between 2026-11-16 01:19 UTC and 2026-11-16 02:19 UTC.

[Full CSV](data/new-cves-2026-11-16T02-19-57-849268Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-11-16 02:17:11 | [CVE-2026-129539](https://nvd.nist.gov/vuln/detail/CVE-2026-129539) | High | 7.1 | SSCMS 7.2.0 through 7.4.0 contains an arbitrary file read vulnerability that allows any registered user-center account… |
| 2026-11-16 02:17:12 | [CVE-2026-129540](https://nvd.nist.gov/vuln/detail/CVE-2026-129540) | High | 8.7 | VoAPI 1.0.0 through 1.2.0 contains a sql injection vulnerability that allows authenticated users to inject SQL by suppl… |
| 2026-11-16 02:17:12 | [CVE-2026-129541](https://nvd.nist.gov/vuln/detail/CVE-2026-129541) | Medium | 5.1 | EdgeChat 2.5.0 through 2.21.0 contains a cross-site scripting vulnerability that allows invited users to inject HTML th… |
| 2026-11-16 02:17:12 | [CVE-2026-129542](https://nvd.nist.gov/vuln/detail/CVE-2026-129542) | Low | 3.1 | Files or directories accessible to external parties vulnerability in Samsung Open Source Starfish allows Probe System F… |
| 2026-11-16 02:17:12 | [CVE-2026-129543](https://nvd.nist.gov/vuln/detail/CVE-2026-129543) | Medium | 6.4 | Access of resource using incompatible type ('type confusion') vulnerability in Samsung Open Source Starfish allows Inpu… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
