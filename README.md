# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-27 07:19 UTC

New CVEs published between 2026-10-27 06:18 UTC and 2026-10-27 07:19 UTC.

[Full CSV](data/new-cves-2026-10-27T07-19-04-4574Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-10-27 07:16:31 | [CVE-2026-103325](https://nvd.nist.gov/vuln/detail/CVE-2026-103325) | Low | 3.7 | The TiendaCrypto para WooCommerce WordPress plugin through 1.2.1 does not correctly verify the authenticity of its paym… |
| 2026-10-27 07:16:31 | [CVE-2026-103359](https://nvd.nist.gov/vuln/detail/CVE-2026-103359) | Medium | 5.3 | The PayDunya WooCommerce Payment Gateway WordPress plugin through 1.1.6 does not verify the authenticity of incoming pa… |
| 2026-10-27 07:16:31 | [CVE-2026-105946](https://nvd.nist.gov/vuln/detail/CVE-2026-105946) | Medium | 5.3 | Out-of-bounds read in the QAuthenticator NTLM authentication handling in the Qt Network module in Qt Group Qt allows re… |
| 2026-10-27 07:16:32 | [CVE-2026-106174](https://nvd.nist.gov/vuln/detail/CVE-2026-106174) | High | 7.5 | A improper locking vulnerability in Fortinet FortiOS 8.0.0, FortiOS 7.6.4 through 7.6.6 may allow an unauthenticated at… |
| 2026-10-27 07:16:32 | [CVE-2026-110910](https://nvd.nist.gov/vuln/detail/CVE-2026-110910) | Medium | 6.3 | ### Summary `qs.stringify` with `allowEmptyArrays: true` writes the key of an empty array without encoding it, even tho… |
| 2026-10-27 07:16:32 | [CVE-2026-75891](https://nvd.nist.gov/vuln/detail/CVE-2026-75891) | High | 8.8 | The Kirki plugin for WordPress is vulnerable to Privilege Escalation via PHP Object Injection in all versions up to, an… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
