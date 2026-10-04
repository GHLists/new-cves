# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-04 16:18 UTC

New CVEs published between 2026-10-04 15:18 UTC and 2026-10-04 16:18 UTC.

[Full CSV](data/new-cves-2026-10-04T16-18-42-827906Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-10-04 16:16:28 | [CVE-2026-104402](https://nvd.nist.gov/vuln/detail/CVE-2026-104402) | Medium | 4.3 | Insertion of Sensitive Information Into Sent Data vulnerability in farvisun Mindio Magic MCP mindio-magic-mcp allows Re… |
| 2026-10-04 16:16:30 | [CVE-2026-105086](https://nvd.nist.gov/vuln/detail/CVE-2026-105086) | Critical | 9.3 | WWBN AVideo 12.4 through 29.2.0 contains a stored cross-site scripting vulnerability that allows authenticated uploader… |
| 2026-10-04 16:16:30 | [CVE-2026-105089](https://nvd.nist.gov/vuln/detail/CVE-2026-105089) | Critical | 9.3 | WWBN AVideo through 29.2.0 contains a stored cross-site scripting vulnerability that allows users with upload permissio… |
| 2026-10-04 16:16:30 | [CVE-2026-105224](https://nvd.nist.gov/vuln/detail/CVE-2026-105224) | Medium | 5.1 | YesWiki before 4.6.7 contains a cross-site scripting vulnerability in the Bazar valeur action that allows page editors… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
