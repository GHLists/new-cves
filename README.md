# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-11-17 13:19 UTC

New CVEs published between 2026-11-17 12:18 UTC and 2026-11-17 13:19 UTC.

[Full CSV](data/new-cves-2026-11-17T13-19-35-612813Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-11-17 13:17:32 | [CVE-2026-124645](https://nvd.nist.gov/vuln/detail/CVE-2026-124645) | High | 8.7 | This vulnerability exists in e-Sushrut HIMS due to the use of a static and predictable value in the client-side passwor… |
| 2026-11-17 13:17:32 | [CVE-2026-124646](https://nvd.nist.gov/vuln/detail/CVE-2026-124646) | High | 8.7 | This vulnerability exists in e-Sushrut HMIS due to insufficient server side object level authorization validation in th… |
| 2026-11-17 13:17:33 | [CVE-2026-127138](https://nvd.nist.gov/vuln/detail/CVE-2026-127138) | Medium | 6.8 | pretix provides a mechanism where ticket QR codes are cryptographically signed and can be verified by our pretixSCAN ap… |
| 2026-11-17 13:17:33 | [CVE-2026-127139](https://nvd.nist.gov/vuln/detail/CVE-2026-127139) | Medium | 4.4 | pretixSCAN Proxy does not use a secure random generator to generate initialization tokens and API keys for the connecti… |
| 2026-11-17 13:17:33 | [CVE-2026-127140](https://nvd.nist.gov/vuln/detail/CVE-2026-127140) | Low | 3.8 | Our WordPress plugin for the pretix Widget performs HTTP calls to pre-fetch CSS and JS files into a local cache and sto… |
| 2026-11-17 13:17:33 | [CVE-2026-127174](https://nvd.nist.gov/vuln/detail/CVE-2026-127174) | Medium | 5.1 | When changing the settings of a scheduled export, no permission checks are done to see whether the user making the chan… |
| 2026-11-17 13:17:34 | [CVE-2026-12239](https://nvd.nist.gov/vuln/detail/CVE-2026-12239) | High | 8.8 | The WP Abstracts plugin for WordPress is vulnerable to Privilege Escalation in all versions up to, and including, 2.7.6… |
| 2026-11-17 13:17:34 | [CVE-2026-130384](https://nvd.nist.gov/vuln/detail/CVE-2026-130384) | Medium | 5.3 | Zammad before 7.2.3 contains a missing authorization vulnerability that allows authenticated customers to delete agents… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
