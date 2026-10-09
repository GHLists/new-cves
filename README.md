# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-09 07:19 UTC

New CVEs published between 2026-10-09 06:18 UTC and 2026-10-09 07:19 UTC.

[Full CSV](data/new-cves-2026-10-09T07-19-48-088331Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-10-09 07:17:16 | [CVE-2025-15700](https://nvd.nist.gov/vuln/detail/CVE-2025-15700) |  |  | The AWP Classifieds WordPress plugin before 4.4.9 does not validate the type of files extracted from an uploaded ZIP ar… |
| 2026-10-09 07:17:17 | [CVE-2026-101028](https://nvd.nist.gov/vuln/detail/CVE-2026-101028) | Medium | 6.0 | Incorrect Authorization vulnerability in ash-project ash allows an actor to infer data in related records they cannot r… |
| 2026-10-09 07:17:17 | [CVE-2026-106095](https://nvd.nist.gov/vuln/detail/CVE-2026-106095) |  |  | The Code Snippets WordPress plugin before 3.10.0 does not perform a capability check on one of its snippet-management a… |
| 2026-10-09 07:17:17 | [CVE-2026-106097](https://nvd.nist.gov/vuln/detail/CVE-2026-106097) |  |  | The Code Snippets WordPress plugin before 3.10.0 does not sanitise and escape a user-supplied parameter before using it… |
| 2026-10-09 07:17:18 | [CVE-2026-81929](https://nvd.nist.gov/vuln/detail/CVE-2026-81929) | High | 7.2 | The Ocean Pro Demos and Ocean eComm Treasure Box plugins for WordPress is vulnerable to Stored Cross-Site Scripting via… |
| 2026-10-09 07:17:18 | [CVE-2026-86850](https://nvd.nist.gov/vuln/detail/CVE-2026-86850) |  |  | The SKU Error Fixer for WooCommerce WordPress plugin through 1.0 does not perform any capability or nonce checks on two… |
| 2026-10-09 07:17:18 | [CVE-2026-87841](https://nvd.nist.gov/vuln/detail/CVE-2026-87841) |  |  | The UnitechPay WordPress plugin through 1.0.6.3 does not verify the authenticity of the payment notifications it receiv… |
| 2026-10-09 07:17:18 | [CVE-2026-88931](https://nvd.nist.gov/vuln/detail/CVE-2026-88931) |  |  | The Social Web Suite WordPress plugin through 4.1.12 does not restrict which of its settings may be written through an… |
| 2026-10-09 07:17:19 | [CVE-2026-92989](https://nvd.nist.gov/vuln/detail/CVE-2026-92989) |  |  | The SendPress Newsletters WordPress plugin through 1.26.1.20 does not check the user's capability on several newsletter… |
| 2026-10-09 07:17:19 | [CVE-2026-92990](https://nvd.nist.gov/vuln/detail/CVE-2026-92990) |  |  | The SendPress Newsletters WordPress plugin through 1.26.1.20 protects a logging endpoint with a hardcoded token that is… |
| 2026-10-09 07:17:19 | [CVE-2026-93548](https://nvd.nist.gov/vuln/detail/CVE-2026-93548) |  |  | The FooSales WordPress plugin before 1.43.3 does not verify that an authenticated caller is entitled to act as the user… |
| 2026-10-09 07:17:19 | [CVE-2026-97076](https://nvd.nist.gov/vuln/detail/CVE-2026-97076) | High | 7.5 | Executable Regular Expression Error vulnerability in WP Media WP Rocket wp-rocket allows Code Injection.This issue affe… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
