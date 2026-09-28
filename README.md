# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-09-28 19:21 UTC

New CVEs published between 2026-09-28 18:20 UTC and 2026-09-28 19:21 UTC.

[Full CSV](data/new-cves-2026-09-28T19-21-01-239787Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-09-28 19:16:46 | [CVE-2026-100752](https://nvd.nist.gov/vuln/detail/CVE-2026-100752) | Critical | 9.3 | Joomla Extension - ordasoft.com - Unauthenticated SQL Injection in Real Estate Manager (Free) < 6.7.9 - site/realestate… |
| 2026-09-28 19:16:46 | [CVE-2026-100753](https://nvd.nist.gov/vuln/detail/CVE-2026-100753) | Medium | 5.3 | Joomla Extension - ordasoft.com - Reflected Cross-Site Scripting in Real Estate Manager (Free) < 6.7.9 - The public pro… |
| 2026-09-28 19:16:46 | [CVE-2026-101105](https://nvd.nist.gov/vuln/detail/CVE-2026-101105) | Low | 2.1 | A vulnerability was determined in code-projects Matrimonial System 1.0. The affected element is the function processpro… |
| 2026-09-28 19:16:46 | [CVE-2026-101108](https://nvd.nist.gov/vuln/detail/CVE-2026-101108) | Critical | 9.3 | Joomla Extension - ordasoft.com - Unauthenticated SQL Injection in Vehicle Manager (Free) < 6.5.8 - site/vehiclemanager… |
| 2026-09-28 19:16:47 | [CVE-2026-101109](https://nvd.nist.gov/vuln/detail/CVE-2026-101109) | Medium | 5.3 | Joomla Extension - ordasoft.com - Reflected Cross-Site Scripting in Vehicle Manager (Free) < 6.5.8 - The public vehicle… |
| 2026-09-28 19:16:47 | [CVE-2026-101110](https://nvd.nist.gov/vuln/detail/CVE-2026-101110) | Critical | 9.3 | Joomla Extension - ordasoft.com - Unauthenticated SQL Injection in Book Library (Free) < 6.4.6 - site/booklibrary.php’s… |
| 2026-09-28 19:16:47 | [CVE-2026-101111](https://nvd.nist.gov/vuln/detail/CVE-2026-101111) | Medium | 5.3 | Joomla Extension - ordasoft.com - Reflected Cross-Site Scripting in Book Library (Free) < 6.4.6 - The public book-detai… |
| 2026-09-28 19:16:47 | [CVE-2026-101131](https://nvd.nist.gov/vuln/detail/CVE-2026-101131) | Low | 1.9 | A vulnerability was identified in deepseek-ai deepseek-harness up to 0.1.5-rc.3. Impacted is an unknown function of the… |
| 2026-09-28 19:16:47 | [CVE-2026-101132](https://nvd.nist.gov/vuln/detail/CVE-2026-101132) | Low | 1.3 | A security flaw has been discovered in DeepSeek deepseek-harness up to 0.1.7-rc.2. The affected element is the function… |
| 2026-09-28 19:16:47 | [CVE-2026-101139](https://nvd.nist.gov/vuln/detail/CVE-2026-101139) | Low | 2.0 | A vulnerability was detected in Webkul Bagisto up to 2.4.6. This impacts an unknown function of the file /admin/sales/i… |
| 2026-09-28 19:16:48 | [CVE-2026-102010](https://nvd.nist.gov/vuln/detail/CVE-2026-102010) | High | 7.0 | A flaw was found in GCC. When an application calls the erase_if function on a binary heap priority queue in libstdc++,… |
| 2026-09-28 19:16:49 | [CVE-2026-13018](https://nvd.nist.gov/vuln/detail/CVE-2026-13018) |  |  | Insufficient validation of untrusted input in Codecs in Google Chrome prior to 147.0.7727.55 allowed a remote attacker… |
| 2026-09-28 19:16:50 | [CVE-2026-84894](https://nvd.nist.gov/vuln/detail/CVE-2026-84894) |  |  | In moxygen before commit 004123dd24c3, MoQSession::dataStreamReadLoop keeps using a stream read handle after reading a… |
| 2026-09-28 19:16:50 | [CVE-2026-97023](https://nvd.nist.gov/vuln/detail/CVE-2026-97023) | High | 7.1 | A path traversal vulnerability in Flatpak's handling of the export/bin directory during app deployment allows a malicio… |
| 2026-09-28 19:16:50 | [CVE-2026-97686](https://nvd.nist.gov/vuln/detail/CVE-2026-97686) | Medium | 5.5 | Wind River VxWorks 7 prior to 26.09, specific system call arguments can result in the IPNET subsystem failing to proper… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
