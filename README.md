# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-11-10 06:18 UTC

New CVEs published between 2026-11-10 05:19 UTC and 2026-11-10 06:18 UTC.

[Full CSV](data/new-cves-2026-11-10T06-18-51-410625Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-11-10 06:17:07 | [CVE-2026-104676](https://nvd.nist.gov/vuln/detail/CVE-2026-104676) |  |  | The Zion Builder WordPress plugin through 3.6.17 does not sanitize uploaded SVG files or validate their contents before… |
| 2026-11-10 06:17:07 | [CVE-2026-110516](https://nvd.nist.gov/vuln/detail/CVE-2026-110516) |  |  | The All in One Addons For WPBakery Page Builder (formerly Visual Composer) WordPress plugin through 1.2 does not valida… |
| 2026-11-10 06:17:08 | [CVE-2026-119273](https://nvd.nist.gov/vuln/detail/CVE-2026-119273) |  |  | The BulletProof Security WordPress plugin through 7.2 does not sufficiently protect its security log files or prevent s… |
| 2026-11-10 06:17:08 | [CVE-2026-12389](https://nvd.nist.gov/vuln/detail/CVE-2026-12389) | High | 8.4 | A vulnerability that could lead to a high privileged authenticated user performing a remote code execution attack. |
| 2026-11-10 06:17:08 | [CVE-2026-12963](https://nvd.nist.gov/vuln/detail/CVE-2026-12963) | High | 7.4 | A vulnerability that could allow a viewer account to gain unauthorized access to network attached storage devices on th… |
| 2026-11-10 06:17:08 | [CVE-2026-12964](https://nvd.nist.gov/vuln/detail/CVE-2026-12964) | High | 8.0 | A vulnerability allowing for privileged escalation of the viewer account to gain administrator privileges. |
| 2026-11-10 06:17:08 | [CVE-2026-13312](https://nvd.nist.gov/vuln/detail/CVE-2026-13312) | Critical | 9.9 | A vulnerability that could allow an attacker to compromise a system. |
| 2026-11-10 06:17:08 | [CVE-2026-13387](https://nvd.nist.gov/vuln/detail/CVE-2026-13387) | Low | 3.5 | A vulnerability related to URL redirection handling during the sign-out flow that could allow a user to be redirected t… |
| 2026-11-10 06:17:08 | [CVE-2026-13409](https://nvd.nist.gov/vuln/detail/CVE-2026-13409) | Medium | 4.3 | The VAPIX API dynamicoverlay.cgi which results in a Denial-of-Service of the overlay functionality. This flaw can only… |
| 2026-11-10 06:17:08 | [CVE-2026-14542](https://nvd.nist.gov/vuln/detail/CVE-2026-14542) | Medium | 6.7 | The VAPIX SIP configuration API lacked sufficient input validation, which could potentially lead to privilege escalatio… |
| 2026-11-10 06:17:09 | [CVE-2026-14543](https://nvd.nist.gov/vuln/detail/CVE-2026-14543) | Low | 3.9 | The VAPIX Edge storage API, enabling the escalation of user privileges by circumventing filesystem isolation, granting… |
| 2026-11-10 06:17:09 | [CVE-2026-14918](https://nvd.nist.gov/vuln/detail/CVE-2026-14918) | Medium | 5.3 | The Signed Video Framework contained a out-of-bounds read issue in the Signed Video Framework which could lead the appl… |
| 2026-11-10 06:17:09 | [CVE-2026-4762](https://nvd.nist.gov/vuln/detail/CVE-2026-4762) | High | 8.8 | A vulnerability to perform a privilege escalation attack on the server as a non-admin user. |
| 2026-11-10 06:17:09 | [CVE-2026-63282](https://nvd.nist.gov/vuln/detail/CVE-2026-63282) | Medium | 6.5 | Improper shell quote escaping when processing user-controlled input, potentially allowing command injection, which coul… |
| 2026-11-10 06:17:10 | [CVE-2026-63287](https://nvd.nist.gov/vuln/detail/CVE-2026-63287) | Medium | 6.5 | It was possible for an authenticated non-admin user to modify certain data objects without having the appropriate permi… |
| 2026-11-10 06:17:10 | [CVE-2026-63288](https://nvd.nist.gov/vuln/detail/CVE-2026-63288) | High | 8.3 | A WebSocket request sent to a specific API endpoint allows unauthorized access to a separate API endpoint. This bypasse… |
| 2026-11-10 06:17:10 | [CVE-2026-8372](https://nvd.nist.gov/vuln/detail/CVE-2026-8372) | High | 8.8 | A vulnerability that could allow an attacker to gain unauthorized access. |
| 2026-11-10 06:17:10 | [CVE-2026-9063](https://nvd.nist.gov/vuln/detail/CVE-2026-9063) | Medium | 6.7 | A locally authenticated user can achieve privilege escalation via an insecure configuration that leads to unauthorized… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
