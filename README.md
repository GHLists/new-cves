# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-11-05 05:19 UTC

New CVEs published between 2026-11-05 04:18 UTC and 2026-11-05 05:19 UTC.

[Full CSV](data/new-cves-2026-11-05T05-19-06-815071Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-11-05 05:18:18 | [CVE-2026-104812](https://nvd.nist.gov/vuln/detail/CVE-2026-104812) | Medium | 6.4 | The Redux Framework plugin for WordPress is vulnerable to Stored Cross-Site Scripting via 'multi_media' Field Array Key… |
| 2026-11-05 05:18:19 | [CVE-2026-116617](https://nvd.nist.gov/vuln/detail/CVE-2026-116617) | High | 8.1 | The Motors – Car Dealership & Classified Listings Plugin plugin for WordPress is vulnerable to File Deletion in all ver… |
| 2026-11-05 05:18:19 | [CVE-2026-118193](https://nvd.nist.gov/vuln/detail/CVE-2026-118193) | High | 8.8 | The GiveWP – Donation Plugin and Fundraising Platform plugin for WordPress is vulnerable to Privilege Escalation in all… |
| 2026-11-05 05:18:20 | [CVE-2026-120533](https://nvd.nist.gov/vuln/detail/CVE-2026-120533) | Medium | 6.4 | The Redux Framework plugin for WordPress is vulnerable to Stored Cross-Site Scripting via theme_opts Parameter via User… |
| 2026-11-05 05:18:20 | [CVE-2026-120553](https://nvd.nist.gov/vuln/detail/CVE-2026-120553) | Medium | 6.4 | The Customer Reviews for WooCommerce plugin for WordPress is vulnerable to Stored Cross-Site Scripting via the 'slides_… |
| 2026-11-05 05:18:36 | [CVE-2026-123010](https://nvd.nist.gov/vuln/detail/CVE-2026-123010) | High | 7.2 | @twilio-labs/netlify-okta-auth through 1.0.2 relies on an unverified iss claim. This affects an outbound HTTP request t… |
| 2026-11-05 05:18:36 | [CVE-2026-123011](https://nvd.nist.gov/vuln/detail/CVE-2026-123011) | Medium | 4.2 | STMicroelectronics st-mems-android-linux-sensors-hal before 7bdf334 does not check whether the allowed number of channe… |
| 2026-11-05 05:18:36 | [CVE-2026-123012](https://nvd.nist.gov/vuln/detail/CVE-2026-123012) | High | 7.1 | In Gogs 0.14.3, the Git Smart HTTP authorization layer in internal/route/repo/http.go allows a push when only read acce… |
| 2026-11-05 05:18:40 | [CVE-2026-93389](https://nvd.nist.gov/vuln/detail/CVE-2026-93389) | High | 8.2 | The LiteSpeed Cache plugin for WordPress is vulnerable to unauthenticated disclosure of sensitive WooCommerce customer… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
