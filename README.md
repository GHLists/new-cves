# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-24 01:19 UTC

New CVEs published between 2026-10-24 00:19 UTC and 2026-10-24 01:19 UTC.

[Full CSV](data/new-cves-2026-10-24T01-19-27-106342Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-10-24 01:17:08 | [CVE-2026-115929](https://nvd.nist.gov/vuln/detail/CVE-2026-115929) | High | 7.6 | MongoDB Compass relies on Electron, a third-party runtime that carries its own TLS root certificate store. This root ce… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
