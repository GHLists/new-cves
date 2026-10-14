# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-14 03:19 UTC

New CVEs published between 2026-10-14 02:21 UTC and 2026-10-14 03:19 UTC.

[Full CSV](data/new-cves-2026-10-14T03-19-52-867026Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-10-14 03:17:12 | [CVE-2026-102251](https://nvd.nist.gov/vuln/detail/CVE-2026-102251) | High | 7.5 | The Abandoned Cart Pro for WooCommerce plugin for WordPress is vulnerable to generic SQL Injection via the 'validate' p… |
| 2026-10-14 03:17:14 | [CVE-2026-103422](https://nvd.nist.gov/vuln/detail/CVE-2026-103422) | High | 7.2 | The AnyComment plugin for WordPress is vulnerable to Stored Cross-Site Scripting via the 'email' parameter in versions… |
| 2026-10-14 03:17:20 | [CVE-2026-110002](https://nvd.nist.gov/vuln/detail/CVE-2026-110002) | Critical | 9.8 | The Snazzy Social Media Feed plugin for WordPress is vulnerable to Arbitrary File Upload in all versions up to, and inc… |
| 2026-10-14 03:17:20 | [CVE-2026-110444](https://nvd.nist.gov/vuln/detail/CVE-2026-110444) | High | 8.6 | TeamPlus Messenger developed by Teamplus Technology has a Code Injection vulnerability. Unauthenticated remote attacker… |
| 2026-10-14 03:17:20 | [CVE-2026-110445](https://nvd.nist.gov/vuln/detail/CVE-2026-110445) | High | 8.6 | TeamPlus Messenger developed by Teamplus Technology has a Code Injection vulnerability. Unauthenticated remote attacker… |
| 2026-10-14 03:17:20 | [CVE-2026-110447](https://nvd.nist.gov/vuln/detail/CVE-2026-110447) | Critical | 9.2 | Collabora Online Built-in CODE Server before 26.4.303 (richdocumentscode), a Nextcloud app, allows remote code executio… |
| 2026-10-14 03:17:21 | [CVE-2026-14765](https://nvd.nist.gov/vuln/detail/CVE-2026-14765) | High | 7.7 | Epic Games Unreal Engine versions up to and including 5.8.0 ship with an insecure default configuration for the LaunchU… |
| 2026-10-14 03:17:37 | [CVE-2026-97657](https://nvd.nist.gov/vuln/detail/CVE-2026-97657) | Critical | 9.8 | The Abandoned Cart Pro for WooCommerce plugin for WordPress is vulnerable to Authentication Bypass via Malleable Encryp… |
| 2026-10-14 03:17:37 | [CVE-2026-97668](https://nvd.nist.gov/vuln/detail/CVE-2026-97668) | Critical | 9.8 | The Abandoned Cart Pro for WooCommerce plugin for WordPress is vulnerable to SQL Injection via the guest cart persisten… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
