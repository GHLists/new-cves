# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-11-21 18:18 UTC

New CVEs published between 2026-11-21 17:20 UTC and 2026-11-21 18:18 UTC.

[Full CSV](data/new-cves-2026-11-21T18-18-42-373492Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-11-21 18:16:53 | [CVE-2026-133990](https://nvd.nist.gov/vuln/detail/CVE-2026-133990) | Low | 2.9 | A vulnerability was identified in Cockpit-HQ Cockpit up to 2.14.1. Affected by this issue is some unknown functionality… |
| 2026-11-21 18:16:54 | [CVE-2026-133993](https://nvd.nist.gov/vuln/detail/CVE-2026-133993) | Critical | 9.3 | A security flaw has been discovered in D-Link DIR-600L 2.17b02. This affects the function FUN_0040efb0 of the file gena… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
