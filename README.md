# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-06 10:19 UTC

New CVEs published between 2026-10-06 09:18 UTC and 2026-10-06 10:19 UTC.

[Full CSV](data/new-cves-2026-10-06T10-19-15-995306Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-10-06 10:16:52 | [CVE-2026-80327](https://nvd.nist.gov/vuln/detail/CVE-2026-80327) | Medium | 5.1 | An open redirect vulnerability exists in the PingGateway Fragment Filter feature. This issue affects PingGateway versio… |
| 2026-10-06 10:16:54 | [CVE-2026-84854](https://nvd.nist.gov/vuln/detail/CVE-2026-84854) | High | 7.0 | In the WibuKey driver for Windows below Version 6.72, insufficient validation of user input when calculating the size o… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
