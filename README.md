# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-11-27 04:20 UTC

New CVEs published between 2026-11-27 03:19 UTC and 2026-11-27 04:20 UTC.

[Full CSV](data/new-cves-2026-11-27T04-20-23-367049Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-11-27 04:16:39 | [CVE-2026-111315](https://nvd.nist.gov/vuln/detail/CVE-2026-111315) | Medium | 6.5 | The Smaily Connect plugin for WordPress is vulnerable to Insecure Direct Object Reference in versions up to, and includ… |
| 2026-11-27 04:16:39 | [CVE-2026-116771](https://nvd.nist.gov/vuln/detail/CVE-2026-116771) | Medium | 4.4 | The Product Options and Price Calculation Formulas for WooCommerce – Uni CPO plugin for WordPress is vulnerable to Stor… |
| 2026-11-27 04:16:40 | [CVE-2026-135626](https://nvd.nist.gov/vuln/detail/CVE-2026-135626) | High | 7.5 | The Simple Membership plugin for WordPress is vulnerable to Privilege Escalation in all versions up to, and including,… |
| 2026-11-27 04:16:40 | [CVE-2026-135627](https://nvd.nist.gov/vuln/detail/CVE-2026-135627) | High | 7.5 | The Simple Membership plugin for WordPress is vulnerable to Privilege Escalation in all versions up to, and including,… |
| 2026-11-27 04:16:40 | [CVE-2026-137679](https://nvd.nist.gov/vuln/detail/CVE-2026-137679) | Medium | 5.5 | A vulnerability was detected in code-projects Online Job Portal 1.0. This affects the function GetSQLValueString of the… |
| 2026-11-27 04:16:40 | [CVE-2026-137713](https://nvd.nist.gov/vuln/detail/CVE-2026-137713) | Medium | 6.4 | Webmin through 2.670 before ae8feb1 allows XSS via an SVG attachment in a mail queue, relevant if an authenticated user… |
| 2026-11-27 04:16:40 | [CVE-2026-19443](https://nvd.nist.gov/vuln/detail/CVE-2026-19443) | Medium | 6.1 | A flaw was found in CRI-O. An attacker with access to the kubelet or CRI-O socket can exploit a path traversal vulnerab… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
