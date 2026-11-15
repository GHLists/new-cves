# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-11-15 21:18 UTC

New CVEs published between 2026-11-15 20:20 UTC and 2026-11-15 21:18 UTC.

[Full CSV](data/new-cves-2026-11-15T21-18-39-895786Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-11-15 21:16:53 | [CVE-2026-123006](https://nvd.nist.gov/vuln/detail/CVE-2026-123006) |  |  | The repository search used by the dashboard (`GET /repo/search`) returned the internal commit status object of each rep… |
| 2026-11-15 21:16:54 | [CVE-2026-125423](https://nvd.nist.gov/vuln/detail/CVE-2026-125423) |  |  | A repository created with auto-init accepted pushes before its initialization had finished, and the initial commit was… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
