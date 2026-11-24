# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-11-24 06:19 UTC

New CVEs published between 2026-11-24 05:19 UTC and 2026-11-24 06:19 UTC.

[Full CSV](data/new-cves-2026-11-24T06-19-53-904943Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-11-24 06:17:06 | [CVE-2026-105303](https://nvd.nist.gov/vuln/detail/CVE-2026-105303) | Medium | 5.1 | The log viewer of Zoraxy admin panel fails to neutralize the output properly, that may cause an arbitrary script to be… |
| 2026-11-24 06:17:06 | [CVE-2026-105304](https://nvd.nist.gov/vuln/detail/CVE-2026-105304) | High | 7.7 | ACME challenge routing logic of Zoraxy fails to validate request URIs properly, that allows an attacker to send an arbi… |
| 2026-11-24 06:17:06 | [CVE-2026-127011](https://nvd.nist.gov/vuln/detail/CVE-2026-127011) |  |  | The Foxtool All-in-One: Contact chat button, Custom login, Media optimize images WordPress plugin through 2.5.4 does no… |
| 2026-11-24 06:17:07 | [CVE-2026-127026](https://nvd.nist.gov/vuln/detail/CVE-2026-127026) |  |  | The 3D Website Builder WordPress plugin through 2.0.3 does not perform any authorisation check in one of its publicly a… |
| 2026-11-24 06:17:07 | [CVE-2026-128793](https://nvd.nist.gov/vuln/detail/CVE-2026-128793) | Medium | 6.9 | Accessible without authentication via /user/resetPasswordFlagTest, forcing a password change prompt on the next admin l… |
| 2026-11-24 06:17:07 | [CVE-2026-128794](https://nvd.nist.gov/vuln/detail/CVE-2026-128794) | Medium | 6.9 | Admin password stored in plaintext at /data/data/com.acer.android.m3.webserver/shared_prefs/userInfo.xml, allowing any… |
| 2026-11-24 06:17:07 | [CVE-2026-128795](https://nvd.nist.gov/vuln/detail/CVE-2026-128795) | Medium | 5.3 | After authentication, /user/getNetworkStatus discloses SIM phone number, cell tower ID (enabling geolocation), and netw… |
| 2026-11-24 06:17:07 | [CVE-2026-128796](https://nvd.nist.gov/vuln/detail/CVE-2026-128796) | High | 8.5 | System service 'antaiuiserver' exposes transaction 14 (sendMyATCmd) & 4, allowing ANY app on device to send arbitrary A… |
| 2026-11-24 06:17:07 | [CVE-2026-128797](https://nvd.nist.gov/vuln/detail/CVE-2026-128797) | Critical | 10.0 | Web administration panel (port 8080) binds to all network interfaces including public IPv6 addresses, making internal A… |
| 2026-11-24 06:17:07 | [CVE-2026-128798](https://nvd.nist.gov/vuln/detail/CVE-2026-128798) | Critical | 10.0 | Any connected WiFi client can fetch device info and meeting recording metadata without credentials. |
| 2026-11-24 06:17:07 | [CVE-2026-129544](https://nvd.nist.gov/vuln/detail/CVE-2026-129544) | Medium | 5.9 | Zoraxy provided by Zoraxy Project does not add HttpOnly attribute to session cookies that allows an attacker to retriev… |
| 2026-11-24 06:17:08 | [CVE-2026-135202](https://nvd.nist.gov/vuln/detail/CVE-2026-135202) | Critical | 9.8 | Several plugins for WordPress published by WP connect (Orders Sync to Airtable for WooCommerce, Add-On for Contact Form… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
