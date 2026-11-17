# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-11-17 04:18 UTC

New CVEs published between 2026-11-17 03:19 UTC and 2026-11-17 04:18 UTC.

[Full CSV](data/new-cves-2026-11-17T04-18-29-063135Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-11-17 04:17:25 | [CVE-2026-107901](https://nvd.nist.gov/vuln/detail/CVE-2026-107901) | Medium | 6.8 | TELLUS and TELLUS Lite provided by FUJI ELECTRIC CO., LTD. contain an out-of-bounds read vulnerability. Opening a speci… |
| 2026-11-17 04:17:26 | [CVE-2026-107902](https://nvd.nist.gov/vuln/detail/CVE-2026-107902) | High | 8.4 | TELLUS and TELLUS Lite provided by FUJI ELECTRIC CO., LTD. contain a use after free vulnerability. Opening a specially… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
