# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-09-29 02:20 UTC

New CVEs published between 2026-09-29 01:18 UTC and 2026-09-29 02:20 UTC.

[Full CSV](data/new-cves-2026-09-29T02-20-59-744232Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-09-29 02:16:53 | [CVE-2026-101354](https://nvd.nist.gov/vuln/detail/CVE-2026-101354) | High | 8.6 | A security flaw has been discovered in FAST FAC1203R 20200116_2.0.4. The affected element is the function _tWlanTask of… |
| 2026-09-29 02:16:54 | [CVE-2026-101858](https://nvd.nist.gov/vuln/detail/CVE-2026-101858) | Low | 2.0 | A flaw has been found in RaspAP raspap-webgui up to 3.5.5. Affected is the function WiFiManager::writeWpaSupplicant of… |
| 2026-09-29 02:16:54 | [CVE-2026-101859](https://nvd.nist.gov/vuln/detail/CVE-2026-101859) | Low | 2.1 | A vulnerability has been found in RaspAP raspap-webgui up to 3.5.5. Affected by this vulnerability is the function esca… |
| 2026-09-29 02:16:54 | [CVE-2026-101860](https://nvd.nist.gov/vuln/detail/CVE-2026-101860) | High | 7.4 | A vulnerability was found in RaspAP raspap-webgui up to 3.5.5. Affected by this issue is the function PluginInstaller::… |
| 2026-09-29 02:16:54 | [CVE-2026-101878](https://nvd.nist.gov/vuln/detail/CVE-2026-101878) | High | 7.7 | Bitwarden Server 2025.6.0 before 2026.5.0 declares the @ExternalId parameter of the User_ReadBySsoUserOrganizationIdExt… |
| 2026-09-29 02:16:55 | [CVE-2026-102240](https://nvd.nist.gov/vuln/detail/CVE-2026-102240) | Critical | 9.3 | A vulnerability was found in Netcore NAP930 0.1.241010.141410. This affects the function eval of the file /www/cgi-bin/… |
| 2026-09-29 02:16:55 | [CVE-2026-96326](https://nvd.nist.gov/vuln/detail/CVE-2026-96326) | High | 7.2 | The HT Contact Form – Drag & Drop Form Builder for WordPress plugin for WordPress is vulnerable to Stored Cross-Site Sc… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
