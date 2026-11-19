# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-11-19 06:21 UTC

New CVEs published between 2026-11-19 05:19 UTC and 2026-11-19 06:21 UTC.

[Full CSV](data/new-cves-2026-11-19T06-21-31-894747Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-11-19 06:16:51 | [CVE-2026-108687](https://nvd.nist.gov/vuln/detail/CVE-2026-108687) |  |  | The SAML SSO Login WordPress plugin through 1.5.2 does not verify that the SAML assertion whose signature it validates… |
| 2026-11-19 06:16:52 | [CVE-2026-109555](https://nvd.nist.gov/vuln/detail/CVE-2026-109555) | High | 8.0 | The WP STAGING and WP STAGING Pro plugins for WordPress are vulnerable to PHP Object Injection in all versions up to, a… |
| 2026-11-19 06:16:53 | [CVE-2026-117678](https://nvd.nist.gov/vuln/detail/CVE-2026-117678) | Medium | 6.9 | Inefficient Algorithmic Complexity vulnerability in benoitc idna allows an attacker who controls a hostname passed to t… |
| 2026-11-19 06:16:53 | [CVE-2026-121852](https://nvd.nist.gov/vuln/detail/CVE-2026-121852) |  |  | The AppPresser WordPress plugin before 5.0.0 does not properly escape the contents of its debug log when displaying it… |
| 2026-11-19 06:16:53 | [CVE-2026-129446](https://nvd.nist.gov/vuln/detail/CVE-2026-129446) |  |  | The WPO365 \| SEAMLESS WORDPRESS + MICROSOFT INTEGRATION (WPO365 \| LOGIN) WordPress plugin before 45.4 does not ensure t… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
