# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-11-16 09:22 UTC

New CVEs published between 2026-11-16 08:18 UTC and 2026-11-16 09:22 UTC.

[Full CSV](data/new-cves-2026-11-16T09-22-05-065497Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-11-16 09:17:12 | [CVE-2026-114453](https://nvd.nist.gov/vuln/detail/CVE-2026-114453) | Low | 3.7 | The Kadence Memberships WordPress plugin before 4.0.6 does not check that the membership level submitted when renewing… |
| 2026-11-16 09:17:13 | [CVE-2026-124672](https://nvd.nist.gov/vuln/detail/CVE-2026-124672) | High | 7.3 | The Burst Statistics WordPress plugin before 3.7.5 does not verify that a request is actually being routed to its own R… |
| 2026-11-16 09:17:13 | [CVE-2026-129703](https://nvd.nist.gov/vuln/detail/CVE-2026-129703) | High | 7.8 | In the vulnerability-lookup web application, the authentication decorators for feed-key requests (auth_feedkey_func in… |
| 2026-11-16 09:17:13 | [CVE-2026-129706](https://nvd.nist.gov/vuln/detail/CVE-2026-129706) | Medium | 5.3 | In the vulnerability-lookup web application, the Flask-Login session identifier was set to the bare numeric user ID (Us… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
