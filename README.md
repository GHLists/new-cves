# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-11-03 06:18 UTC

New CVEs published between 2026-11-03 05:20 UTC and 2026-11-03 06:18 UTC.

[Full CSV](data/new-cves-2026-11-03T06-18-19-23504Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-11-03 06:17:35 | [CVE-2026-103379](https://nvd.nist.gov/vuln/detail/CVE-2026-103379) |  |  | The WATI Chat and Notification WordPress plugin through 1.1.8 does not require a valid, non-empty secret on a public en… |
| 2026-11-03 06:17:37 | [CVE-2026-104647](https://nvd.nist.gov/vuln/detail/CVE-2026-104647) |  |  | The weMail WordPress plugin through 2.1.6 does not correctly verify user capabilities in its REST API permission checks… |
| 2026-11-03 06:17:37 | [CVE-2026-104648](https://nvd.nist.gov/vuln/detail/CVE-2026-104648) |  |  | The weMail WordPress plugin through 2.1.6 does not restrict a site-wide third-party email-service API key to administra… |
| 2026-11-03 06:17:37 | [CVE-2026-105967](https://nvd.nist.gov/vuln/detail/CVE-2026-105967) |  |  | The Gallery for Social Photo WordPress plugin through 1.0.0.41 does not validate a user-supplied URL before using it to… |
| 2026-11-03 06:17:37 | [CVE-2026-105993](https://nvd.nist.gov/vuln/detail/CVE-2026-105993) |  |  | The DT Directory Lite Addon WordPress plugin through 1.1 does not perform nonce or capability checks on its settings ha… |
| 2026-11-03 06:17:37 | [CVE-2026-106004](https://nvd.nist.gov/vuln/detail/CVE-2026-106004) |  |  | The DT LMS WordPress plugin through 1.2 does not perform capability or nonce checks on one of its AJAX actions, allowin… |
| 2026-11-03 06:17:37 | [CVE-2026-115205](https://nvd.nist.gov/vuln/detail/CVE-2026-115205) |  |  | The AZEXO Store Locator WordPress plugin through 1.4 does not have a capability check or any authorization control when… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
