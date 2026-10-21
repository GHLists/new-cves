# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-21 04:18 UTC

New CVEs published between 2026-10-21 03:19 UTC and 2026-10-21 04:18 UTC.

[Full CSV](data/new-cves-2026-10-21T04-18-54-816109Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-10-21 04:18:09 | [CVE-2026-114039](https://nvd.nist.gov/vuln/detail/CVE-2026-114039) | Low | 2.1 | A weakness has been identified in projectworlds Advanced Library Management System 1.0. Impacted is the function mysqli… |
| 2026-10-21 04:18:10 | [CVE-2026-114040](https://nvd.nist.gov/vuln/detail/CVE-2026-114040) | Low | 2.0 | A security vulnerability has been detected in DT42 BerryNet up to 3.10.2. The affected element is the function DLModelM… |
| 2026-10-21 04:18:11 | [CVE-2026-92822](https://nvd.nist.gov/vuln/detail/CVE-2026-92822) | Medium | 6.2 | A flaw was found in libmodulemd. When parsing module metadata, the xmd field is converted into nested GVariant values t… |
| 2026-10-21 04:18:12 | [CVE-2026-92823](https://nvd.nist.gov/vuln/detail/CVE-2026-92823) | Medium | 6.2 | A flaw was found in libmodulemd. In builds with rpmio support enabled, compressed modulemd YAML is decompressed through… |
| 2026-10-21 04:18:12 | [CVE-2026-92824](https://nvd.nist.gov/vuln/detail/CVE-2026-92824) | Medium | 6.2 | A flaw was found in libmodulemd. In the module stream v2 rpm-map emission path, an inner loop incorrectly uses the coun… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
