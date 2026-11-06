# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-11-06 14:19 UTC

New CVEs published between 2026-11-06 13:19 UTC and 2026-11-06 14:19 UTC.

[Full CSV](data/new-cves-2026-11-06T14-19-48-176731Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-11-06 14:17:10 | [CVE-2026-123653](https://nvd.nist.gov/vuln/detail/CVE-2026-123653) | Low | 2.1 | A security vulnerability has been detected in esengine DeepSeek-Reasonix up to 2.52.0. Affected is the function discove… |
| 2026-11-06 14:17:11 | [CVE-2026-21849](https://nvd.nist.gov/vuln/detail/CVE-2026-21849) | Low | 3.7 | HCL AION is affected by a missing encryption vulnerability in the WebSocket connection set up by the GenAI web interfac… |
| 2026-11-06 14:17:11 | [CVE-2026-21850](https://nvd.nist.gov/vuln/detail/CVE-2026-21850) | Medium | 6.5 | HCL AION is affected by a vulnerability where user-controlled input could be included in HTTP response headers without… |
| 2026-11-06 14:17:11 | [CVE-2026-35102](https://nvd.nist.gov/vuln/detail/CVE-2026-35102) | Medium | 4.7 | HCL AION is affected by an open redirect vulnerability in the navigation bar of the GenAI web interface (Navbar compone… |
| 2026-11-06 14:17:11 | [CVE-2026-35103](https://nvd.nist.gov/vuln/detail/CVE-2026-35103) | Medium | 4.7 | HCL AION is affected by an open redirect vulnerability on the role assignment pending page (RoleAssignPending component… |
| 2026-11-06 14:17:11 | [CVE-2026-35104](https://nvd.nist.gov/vuln/detail/CVE-2026-35104) | Medium | 4.7 | HCL AION is affected by an open redirect vulnerability on the user registration page (Signup component). The redirect p… |
| 2026-11-06 14:17:12 | [CVE-2026-35105](https://nvd.nist.gov/vuln/detail/CVE-2026-35105) | Medium | 4.7 | HCL AION is affected by an open redirect vulnerability in the session-handling logic of the GenAI web interface (UserCo… |
| 2026-11-06 14:17:12 | [CVE-2026-35106](https://nvd.nist.gov/vuln/detail/CVE-2026-35106) | Medium | 4.7 | HCL AION is affected by an open redirect vulnerability in the session-handling logic of the GenAI web interface (UserCo… |
| 2026-11-06 14:17:12 | [CVE-2026-35107](https://nvd.nist.gov/vuln/detail/CVE-2026-35107) | Medium | 4.7 | HCL AION is affected by an open redirect vulnerability in the user menu of the GenAI web interface (UserMenu component)… |
| 2026-11-06 14:17:12 | [CVE-2026-35109](https://nvd.nist.gov/vuln/detail/CVE-2026-35109) | Low | 3.7 | HCL AION is affected by a vulnerability where pages served over HTTPS could be cached by the browser or intermediate pr… |
| 2026-11-06 14:17:12 | [CVE-2026-35110](https://nvd.nist.gov/vuln/detail/CVE-2026-35110) | Medium | 5.4 | HCL AION is affected by a vulnerability where encrypted (HTTPS) communication was not enforced for all requests. Data m… |
| 2026-11-06 14:17:12 | [CVE-2026-35111](https://nvd.nist.gov/vuln/detail/CVE-2026-35111) | Medium | 4.8 | HCL AION is affected by a vulnerability where the Cross-Origin-Resource-Policy (CORP) header was missing or insecure, a… |
| 2026-11-06 14:17:12 | [CVE-2026-35112](https://nvd.nist.gov/vuln/detail/CVE-2026-35112) | Medium | 4.2 | HCL AION is affected by a vulnerability where the Cross-Origin-Embedder-Policy (COEP) header was missing or insecure, s… |
| 2026-11-06 14:17:13 | [CVE-2026-35113](https://nvd.nist.gov/vuln/detail/CVE-2026-35113) | Medium | 4.8 | HCL AION is affected by a vulnerability where the Cross-Origin-Opener-Policy (COOP) header was missing or insecure, all… |
| 2026-11-06 14:17:13 | [CVE-2026-5345](https://nvd.nist.gov/vuln/detail/CVE-2026-5345) | Low | 3.7 | HCL AION is affected by a missing encryption vulnerability in a second WebSocket connection defined in the GenAI web in… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
