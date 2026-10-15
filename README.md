# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-15 12:19 UTC

New CVEs published between 2026-10-15 11:20 UTC and 2026-10-15 12:19 UTC.

[Full CSV](data/new-cves-2026-10-15T12-19-40-099997Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-10-15 12:16:37 | [CVE-2026-110726](https://nvd.nist.gov/vuln/detail/CVE-2026-110726) |  |  | In `api-gateway` versions till `1.7.3`, The default rate-limit key resolver, `ClientIpKeyResolver`, derives the per-cli… |
| 2026-10-15 12:16:39 | [CVE-2026-79834](https://nvd.nist.gov/vuln/detail/CVE-2026-79834) | High | 7.4 | A security vulnerability in HPE NonStop SQL/MX SQLCAT may allow an unauthenticated user to perform unauthorized command… |
| 2026-10-15 12:16:39 | [CVE-2026-79835](https://nvd.nist.gov/vuln/detail/CVE-2026-79835) | Low | 2.8 | A crafted input message can cause a buffer overflow in HPE Nonstop KMS Server. |
| 2026-10-15 12:16:39 | [CVE-2026-79836](https://nvd.nist.gov/vuln/detail/CVE-2026-79836) | Medium | 6.4 | A vulnerability HPE NonStop SQL/MX Run-Time Statistics may allow an attacker to cause memory corruption and null pointe… |
| 2026-10-15 12:16:39 | [CVE-2026-8145](https://nvd.nist.gov/vuln/detail/CVE-2026-8145) | Medium | 5.4 | The WholesaleX – B2B & Wholesale Plugin for WooCommerce with Wholesale Prices plugin for WordPress is vulnerable to Lim… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
