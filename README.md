# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-25 20:18 UTC

New CVEs published between 2026-10-25 19:20 UTC and 2026-10-25 20:18 UTC.

[Full CSV](data/new-cves-2026-10-25T20-18-58-843201Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-10-25 20:16:31 | [CVE-2026-114214](https://nvd.nist.gov/vuln/detail/CVE-2026-114214) | Medium | 6.0 | Incorrect Authorization vulnerability in ash-project ash allows a client to read destination records unrelated to the s… |
| 2026-10-25 20:16:32 | [CVE-2026-115627](https://nvd.nist.gov/vuln/detail/CVE-2026-115627) | Medium | 6.0 | Incorrect Authorization vulnerability in ash-project ash_postgres allows a user to load destination records linked to a… |
| 2026-10-25 20:16:32 | [CVE-2026-115635](https://nvd.nist.gov/vuln/detail/CVE-2026-115635) | Medium | 6.0 | Incorrect Authorization vulnerability in ash-project ash_postgres allows a user to read another tenant's record through… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
