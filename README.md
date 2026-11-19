# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-11-19 10:18 UTC

New CVEs published between 2026-11-19 09:22 UTC and 2026-11-19 10:18 UTC.

[Full CSV](data/new-cves-2026-11-19T10-18-48-27253Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-11-19 10:17:26 | [CVE-2026-110728](https://nvd.nist.gov/vuln/detail/CVE-2026-110728) | Medium | 5.3 | The AIKTP plugin for WordPress is vulnerable to Authorization Bypass via Predictable Token in all versions up to, and i… |
| 2026-11-19 10:17:28 | [CVE-2026-126631](https://nvd.nist.gov/vuln/detail/CVE-2026-126631) | High | 7.1 | A flaw was found in OpenSCAP. This vulnerability allows for information disclosure when performing offline scans of unt… |
| 2026-11-19 10:17:28 | [CVE-2026-14491](https://nvd.nist.gov/vuln/detail/CVE-2026-14491) | High | 7.5 | The WP Duplicate – WordPress Migration Plugin plugin for WordPress is vulnerable to Directory Traversal in all versions… |
| 2026-11-19 10:17:28 | [CVE-2026-14492](https://nvd.nist.gov/vuln/detail/CVE-2026-14492) | Critical | 9.8 | The WP Duplicate – WordPress Migration Plugin plugin for WordPress is vulnerable to Remote Code Execution in all versio… |
| 2026-11-19 10:17:29 | [CVE-2026-85776](https://nvd.nist.gov/vuln/detail/CVE-2026-85776) | High | 7.5 | The WP Duplicate – WordPress Migration Plugin plugin for WordPress is vulnerable to Missing Authorization in versions u… |
| 2026-11-19 10:17:29 | [CVE-2026-92613](https://nvd.nist.gov/vuln/detail/CVE-2026-92613) | Low | 1.0 | In Eclipse iceoryx-rs, versions 0.0.11 to 0.0.13 and 0.1.0 as well as on the latest main branch. `SampleReceiver::<T>::… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
