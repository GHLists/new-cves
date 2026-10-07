# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-07 09:19 UTC

New CVEs published between 2026-10-07 08:18 UTC and 2026-10-07 09:19 UTC.

[Full CSV](data/new-cves-2026-10-07T09-19-16-483968Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-10-07 09:17:03 | [CVE-2025-64391](https://nvd.nist.gov/vuln/detail/CVE-2025-64391) | Medium | 4.1 | This vulnerability in Veeam Agent for Microsoft Windows allows a low-privileged local user to make the agent write file… |
| 2026-10-07 09:17:04 | [CVE-2025-64392](https://nvd.nist.gov/vuln/detail/CVE-2025-64392) | Medium | 4.8 | This vulnerability in Veeam Backup Enterprise Manager allows an attacker to execute script in the browser of a portal u… |
| 2026-10-07 09:17:04 | [CVE-2025-64393](https://nvd.nist.gov/vuln/detail/CVE-2025-64393) | Critical | 9.4 | This vulnerability in Veeam Backup & Replication allows a Backup Viewer to execute arbitrary code as SYSTEM on the back… |
| 2026-10-07 09:17:04 | [CVE-2026-102781](https://nvd.nist.gov/vuln/detail/CVE-2026-102781) | Medium | 6.9 | Joomla Extension - ordasoft.com - Unauthenticated Destructive CRUD in OrdaSoft Touch Slider < 5.4.6 - modOsTouchSliderH… |
| 2026-10-07 09:17:04 | [CVE-2026-102782](https://nvd.nist.gov/vuln/detail/CVE-2026-102782) | Critical | 9.3 | Joomla Extension - ordasoft.com - Unauthenticated SQL injection in OrdaSoft Simple Membership < 7.4.0 - site/simplememb… |
| 2026-10-07 09:17:04 | [CVE-2026-103416](https://nvd.nist.gov/vuln/detail/CVE-2026-103416) | Critical | 9.3 | Out-of-bounds write via the TLS 1.3 handshake message cache in NetX Duo in Eclipse ThreadX NetX Duo 6.5.1.202602 allows… |
| 2026-10-07 09:17:04 | [CVE-2026-107102](https://nvd.nist.gov/vuln/detail/CVE-2026-107102) | Critical | 9.3 | This vulnerability exists in the ERP system due to improper validation of payment callback parameters and inadequate au… |
| 2026-10-07 09:17:04 | [CVE-2026-107103](https://nvd.nist.gov/vuln/detail/CVE-2026-107103) | Critical | 9.3 | This vulnerability exists in the ERP system due to insufficient validation and parameterization of user supplied input… |
| 2026-10-07 09:17:05 | [CVE-2026-107104](https://nvd.nist.gov/vuln/detail/CVE-2026-107104) | Critical | 9.3 | This vulnerability exists in the ERP system due to unsafe deserialization of user controlled data in the affected funct… |
| 2026-10-07 09:17:05 | [CVE-2026-15894](https://nvd.nist.gov/vuln/detail/CVE-2026-15894) | High | 8.8 | The Bluetooth Mesh On-Demand Private Proxy solicitation handler in subsys/bluetooth/mesh/solicitation.c copies a receiv… |
| 2026-10-07 09:17:05 | [CVE-2026-19186](https://nvd.nist.gov/vuln/detail/CVE-2026-19186) | High | 8.1 | ieee802154_decipher_data_frame() in subsys/net/l2/ieee802154/ieee802154_frame.c computed payload_len = net_pkt_get_len(… |
| 2026-10-07 09:17:05 | [CVE-2026-58068](https://nvd.nist.gov/vuln/detail/CVE-2026-58068) | Medium | 6.8 | This vulnerability in Veeam Agent for Microsoft Windows allows any local user to terminate arbitrary processes on the s… |
| 2026-10-07 09:17:05 | [CVE-2026-58069](https://nvd.nist.gov/vuln/detail/CVE-2026-58069) | High | 8.3 | This vulnerability in Veeam Backup & Replication allows an authenticated Cloud Connect tenant to read arbitrary files o… |
| 2026-10-07 09:17:05 | [CVE-2026-5703](https://nvd.nist.gov/vuln/detail/CVE-2026-5703) | High | 7.1 | Path traversal vulnerability in the Satel Iberia SenNet Datalogger Serie 200, specifically in the web portal provided b… |
| 2026-10-07 09:17:05 | [CVE-2026-89417](https://nvd.nist.gov/vuln/detail/CVE-2026-89417) | High | 7.2 | The OMGF \| GDPR/DSGVO Compliant, Faster Google Fonts. Easy. plugin for WordPress is vulnerable to Stored Cross-Site Scr… |
| 2026-10-07 09:17:05 | [CVE-2026-90466](https://nvd.nist.gov/vuln/detail/CVE-2026-90466) |  |  | Path traversal of 'trusted_jar_paths' in Impala 4.5.2 allows an attacker-controlled JAR to be loaded via a relative pat… |
| 2026-10-07 09:17:06 | [CVE-2026-93026](https://nvd.nist.gov/vuln/detail/CVE-2026-93026) | Medium | 6.1 | This vulnerability in Veeam Backup & Replication allows a Backup Viewer to modify the Enterprise Manager master key and… |
| 2026-10-07 09:17:06 | [CVE-2026-93684](https://nvd.nist.gov/vuln/detail/CVE-2026-93684) |  |  | An SQL user using Impala up to and including version 4.5.2 with only SELECT permission can put JavaScript in a table al… |
| 2026-10-07 09:17:06 | [CVE-2026-97720](https://nvd.nist.gov/vuln/detail/CVE-2026-97720) |  |  | Incorrect implementation of JWT/OAuth authentication in Impala executors in Apache Impala versions up to and including… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
