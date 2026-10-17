# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-17 06:18 UTC

New CVEs published between 2026-10-17 05:19 UTC and 2026-10-17 06:18 UTC.

[Full CSV](data/new-cves-2026-10-17T06-18-24-183906Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-10-17 06:16:30 | [CVE-2026-103376](https://nvd.nist.gov/vuln/detail/CVE-2026-103376) |  |  | The PeachPay — Payments & Express Checkout for WooCommerce (supports Stripe, PayPal, Square, Authorize.net, NMI) WordPr… |
| 2026-10-17 06:16:33 | [CVE-2026-104122](https://nvd.nist.gov/vuln/detail/CVE-2026-104122) |  |  | The Ukr-To-Lat WordPress plugin through 1.3.5 does not sanitize and escape a term name before using it in a SQL query,… |
| 2026-10-17 06:16:33 | [CVE-2026-104246](https://nvd.nist.gov/vuln/detail/CVE-2026-104246) |  |  | The Contact Form 7 Signature Addon WordPress plugin through 4.2.2 does not sanitize a signature field value before buil… |
| 2026-10-17 06:16:33 | [CVE-2026-106470](https://nvd.nist.gov/vuln/detail/CVE-2026-106470) |  |  | The WP Data Access WordPress plugin before 5.5.88 does not have authorisation and CSRF checks in one of its actions, al… |
| 2026-10-17 06:16:33 | [CVE-2026-110527](https://nvd.nist.gov/vuln/detail/CVE-2026-110527) |  |  | The WP User Manager WordPress plugin before 2.9.20 does not roll back the WordPress account it creates during payment-g… |
| 2026-10-17 06:16:33 | [CVE-2026-81343](https://nvd.nist.gov/vuln/detail/CVE-2026-81343) |  |  | The ACF Frontend Admin by DynamiApps WordPress plugin through 3.29.13 does not perform a capability check on one of its… |
| 2026-10-17 06:16:33 | [CVE-2026-81344](https://nvd.nist.gov/vuln/detail/CVE-2026-81344) |  |  | The ACF Frontend Admin by DynamiApps WordPress plugin through 3.29.13 does not restrict which PHP classes may be instan… |
| 2026-10-17 06:16:33 | [CVE-2026-91074](https://nvd.nist.gov/vuln/detail/CVE-2026-91074) |  |  | The BSK PDF Manager WordPress plugin through 3.8.1 does not properly sanitise and escape a parameter before using it in… |
| 2026-10-17 06:16:34 | [CVE-2026-92431](https://nvd.nist.gov/vuln/detail/CVE-2026-92431) |  |  | The Patreon WordPress plugin before 1.10.0 does not perform an authorization check on some of its functionality, allowi… |
| 2026-10-17 06:16:34 | [CVE-2026-92432](https://nvd.nist.gov/vuln/detail/CVE-2026-92432) |  |  | The Patreon WordPress plugin before 1.10.0 does not validate a user-supplied redirect destination before redirecting, a… |
| 2026-10-17 06:16:34 | [CVE-2026-92433](https://nvd.nist.gov/vuln/detail/CVE-2026-92433) |  |  | The Patreon WordPress plugin before 1.10.0 does not verify a nonce when connecting the site to a Patreon account, allow… |
| 2026-10-17 06:16:34 | [CVE-2026-97314](https://nvd.nist.gov/vuln/detail/CVE-2026-97314) |  |  | The ThirstyAffiliates WordPress plugin before 3.12.1 does not check the status or type of the object requested by its l… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
