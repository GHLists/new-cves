# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-20 09:18 UTC

New CVEs published between 2026-10-20 08:18 UTC and 2026-10-20 09:18 UTC.

[Full CSV](data/new-cves-2026-10-20T09-18-55-116544Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-10-20 09:17:08 | [CVE-2026-101201](https://nvd.nist.gov/vuln/detail/CVE-2026-101201) | Medium | 4.3 | A malformed header in the binary file fed to QBinaryJson::fromBinaryData() can cause undefined behaviour because of out… |
| 2026-10-20 09:17:09 | [CVE-2026-113465](https://nvd.nist.gov/vuln/detail/CVE-2026-113465) | Medium | 6.6 | It is possible to execute a DOM-based Cross-Site Scripting attack against Stormshield’s web administration panel. To ex… |
| 2026-10-20 09:17:09 | [CVE-2026-113469](https://nvd.nist.gov/vuln/detail/CVE-2026-113469) | High | 7.5 | A failure has been identified in the SNS during dynamic data files signature check. A logic error in the signature veri… |
| 2026-10-20 09:17:09 | [CVE-2026-11959](https://nvd.nist.gov/vuln/detail/CVE-2026-11959) | Medium | 6.9 | Stored Cross-Site Scripting (XSS) in FacturaScripts, version 2025.61, caused by a lack of adequate validation or saniti… |
| 2026-10-20 09:17:09 | [CVE-2026-11960](https://nvd.nist.gov/vuln/detail/CVE-2026-11960) | Medium | 6.9 | Enumeration of unauthenticated users in FacturaScripts, version 2025.61. The application returns different responses wh… |
| 2026-10-20 09:17:09 | [CVE-2026-43836](https://nvd.nist.gov/vuln/detail/CVE-2026-43836) | Critical | 9.3 | A vulnerability could allow an attacker to forge a packet to execute arbitrary commands with maximum privileges. |
| 2026-10-20 09:17:10 | [CVE-2026-43837](https://nvd.nist.gov/vuln/detail/CVE-2026-43837) | High | 7.5 | A buffer overflow vulnerability in the password verification functionality could allow an attacker with guest authentic… |
| 2026-10-20 09:17:10 | [CVE-2026-43838](https://nvd.nist.gov/vuln/detail/CVE-2026-43838) | Critical | 9.2 | A stack-based buffer overflow vulnerability in the login functionality could allow an attacker to achieve code executio… |
| 2026-10-20 09:17:10 | [CVE-2026-43839](https://nvd.nist.gov/vuln/detail/CVE-2026-43839) | High | 8.7 | A NULL pointer dereference vulnerability in the logs management functionality could allow an unauthenticated attacker t… |
| 2026-10-20 09:17:10 | [CVE-2026-43840](https://nvd.nist.gov/vuln/detail/CVE-2026-43840) | Medium | 6.9 | A NULL pointer dereference vulnerability in the license manager service could allow an unauthenticated attacker to cras… |
| 2026-10-20 09:17:10 | [CVE-2026-43841](https://nvd.nist.gov/vuln/detail/CVE-2026-43841) | Medium | 6.9 | A NULL pointer dereference vulnerability in the license manager service could allow an unauthenticated attacker to cras… |
| 2026-10-20 09:17:10 | [CVE-2026-43842](https://nvd.nist.gov/vuln/detail/CVE-2026-43842) | Medium | 6.9 | A NULL pointer dereference vulnerability in the license manager service could allow an unauthenticated attacker to cras… |
| 2026-10-20 09:17:10 | [CVE-2026-43843](https://nvd.nist.gov/vuln/detail/CVE-2026-43843) | Medium | 6.9 | An integer overflow vulnerability in the license manager service could allow an unauthenticated attacker to crash the s… |
| 2026-10-20 09:17:10 | [CVE-2026-43844](https://nvd.nist.gov/vuln/detail/CVE-2026-43844) | Critical | 9.3 | A vulnerability in the proprietary protocol could allow an attacker to bypass the authentication mechanism. |
| 2026-10-20 09:17:10 | [CVE-2026-43845](https://nvd.nist.gov/vuln/detail/CVE-2026-43845) | Critical | 9.2 | A vulnerability in the password reset mechanism could allow an attacker to bypass the authentication mechanism. |
| 2026-10-20 09:17:11 | [CVE-2026-43846](https://nvd.nist.gov/vuln/detail/CVE-2026-43846) | High | 8.6 | A stack-based buffer overflow vulnerability in a non-functional feature could allow an authenticated attacker to achiev… |
| 2026-10-20 09:17:11 | [CVE-2026-43847](https://nvd.nist.gov/vuln/detail/CVE-2026-43847) | High | 8.2 | A vulnerability in the proprietary protocol could allow an attacker to brute force the administrator password without r… |
| 2026-10-20 09:17:11 | [CVE-2026-43848](https://nvd.nist.gov/vuln/detail/CVE-2026-43848) | Medium | 6.9 | A vulnerability in the bulk port configuration functionality could allow an unauthenticated attacker to crash the servi… |
| 2026-10-20 09:17:12 | [CVE-2026-92287](https://nvd.nist.gov/vuln/detail/CVE-2026-92287) |  |  | Pass-through of unvalidated KMS URLs to KMS clients in Apache C++ Parquet and PyArrow versions 4.0.0 to 25.0.1. This af… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
