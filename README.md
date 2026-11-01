# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-11-01 18:18 UTC

New CVEs published between 2026-11-01 17:18 UTC and 2026-11-01 18:18 UTC.

[Full CSV](data/new-cves-2026-11-01T18-18-13-228205Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-11-01 18:17:13 | [CVE-2026-120237](https://nvd.nist.gov/vuln/detail/CVE-2026-120237) | Low | 2.1 | A flaw has been found in ag-ui-protocol ag-ui up to 0.0.58. Affected by this issue is the function isInterruptExpired o… |
| 2026-11-01 18:17:13 | [CVE-2026-120238](https://nvd.nist.gov/vuln/detail/CVE-2026-120238) | High | 8.6 | A vulnerability has been found in WAVLINK WN553X1-B 260403_2.0.0. This affects the function sub_4162A8 of the file /bin… |
| 2026-11-01 18:17:13 | [CVE-2026-120239](https://nvd.nist.gov/vuln/detail/CVE-2026-120239) | High | 8.6 | A vulnerability was found in WAVLINK WN553X1-B V260403_2.0.0. This vulnerability affects the function sub_419DA8 of the… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
