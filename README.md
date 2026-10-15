# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-15 06:19 UTC

New CVEs published between 2026-10-15 05:19 UTC and 2026-10-15 06:19 UTC.

[Full CSV](data/new-cves-2026-10-15T06-19-39-569191Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-10-15 06:17:01 | [CVE-2026-110923](https://nvd.nist.gov/vuln/detail/CVE-2026-110923) | Medium | 6.5 | A flaw was found in OpenSSH. During an sftp copy, a malicious server can supply an empty name, a slash-only path, or a… |
| 2026-10-15 06:17:01 | [CVE-2026-110925](https://nvd.nist.gov/vuln/detail/CVE-2026-110925) | Medium | 5.4 | A flaw was found in OpenSSH. A username entered on the ssh command line can still contain '$' or a non-trailing backsla… |
| 2026-10-15 06:17:01 | [CVE-2026-110926](https://nvd.nist.gov/vuln/detail/CVE-2026-110926) | Medium | 5.3 | A flaw was found in OpenSSH. When compression is negotiated, channels on the same connection share one LZ77 dictionary.… |
| 2026-10-15 06:17:02 | [CVE-2026-15090](https://nvd.nist.gov/vuln/detail/CVE-2026-15090) | High | 7.5 | The Link Library plugin for WordPress is vulnerable to time-based SQL Injection via the 'link_url' parameter in all ver… |
| 2026-10-15 06:17:02 | [CVE-2026-15180](https://nvd.nist.gov/vuln/detail/CVE-2026-15180) | Medium | 6.1 | The Tracking Code Manager plugin for WordPress is vulnerable to Reflected Cross-Site Scripting via 'TCM_ErrorMessages'… |
| 2026-10-15 06:17:02 | [CVE-2026-17001](https://nvd.nist.gov/vuln/detail/CVE-2026-17001) | Medium | 6.4 | The Import and export users and customers plugin for WordPress is vulnerable to Stored Cross-Site Scripting via Custom… |
| 2026-10-15 06:17:02 | [CVE-2026-17031](https://nvd.nist.gov/vuln/detail/CVE-2026-17031) | High | 8.1 | The Checkout Field Manager (Checkout Manager) for WooCommerce plugin for WordPress is vulnerable to authorization bypas… |
| 2026-10-15 06:17:03 | [CVE-2026-18548](https://nvd.nist.gov/vuln/detail/CVE-2026-18548) | High | 7.2 | The Groundhogg — CRM, Newsletters, and Marketing Automation plugin for WordPress is vulnerable to Stored Cross-Site Scr… |
| 2026-10-15 06:17:03 | [CVE-2026-18557](https://nvd.nist.gov/vuln/detail/CVE-2026-18557) | Medium | 6.1 | The Photo Gallery by 10Web – Mobile-Friendly Image Gallery plugin for WordPress is vulnerable to Reflected Cross-Site S… |
| 2026-10-15 06:17:03 | [CVE-2026-18586](https://nvd.nist.gov/vuln/detail/CVE-2026-18586) | High | 7.2 | The Premium Packages – Sell Digital Products Securely plugin for WordPress is vulnerable to Unauthenticated Stored Cros… |
| 2026-10-15 06:17:04 | [CVE-2026-78001](https://nvd.nist.gov/vuln/detail/CVE-2026-78001) | Medium | 6.4 | The Post and Page Builder by BoldGrid – Visual Drag and Drop Editor plugin for WordPress is vulnerable to Stored Cross-… |
| 2026-10-15 06:17:04 | [CVE-2026-78087](https://nvd.nist.gov/vuln/detail/CVE-2026-78087) | Medium | 6.4 | The VK Blocks plugin for WordPress is vulnerable to Stored Cross-Site Scripting via Group Block 'linkToPost' Feature in… |
| 2026-10-15 06:17:05 | [CVE-2026-86803](https://nvd.nist.gov/vuln/detail/CVE-2026-86803) | Medium | 6.5 | The The Ocean Extra plugin for WordPress is vulnerable to arbitrary shortcode execution in all versions up to, and incl… |
| 2026-10-15 06:17:05 | [CVE-2026-88043](https://nvd.nist.gov/vuln/detail/CVE-2026-88043) | High | 7.2 | The Mang Board WP plugin for WordPress is vulnerable to Stored Cross-Site Scripting via the 'data_type' parameter in al… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
