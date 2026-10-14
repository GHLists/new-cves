# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-14 22:19 UTC

New CVEs published between 2026-10-14 21:20 UTC and 2026-10-14 22:19 UTC.

[Full CSV](data/new-cves-2026-10-14T22-19-05-252433Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-10-14 22:17:22 | [CVE-2026-102298](https://nvd.nist.gov/vuln/detail/CVE-2026-102298) | High | 7.5 | In Omada Controller MSP mode, the user-confirmation endpoint fails to enforce the required permission check. An authent… |
| 2026-10-14 22:17:22 | [CVE-2026-108335](https://nvd.nist.gov/vuln/detail/CVE-2026-108335) | Critical | 9.1 | When the password reset functionality is enabled, and email is configured, an attacker could take over any account usin… |
| 2026-10-14 22:17:22 | [CVE-2026-108336](https://nvd.nist.gov/vuln/detail/CVE-2026-108336) | Critical | 9.1 | When the default self-signed certificate is used, an attacker could gain administrative access to the application. The… |
| 2026-10-14 22:17:22 | [CVE-2026-108337](https://nvd.nist.gov/vuln/detail/CVE-2026-108337) | High | 7.4 | An administrator could retrieve the password reset code for any user and take over the account. The password reset code… |
| 2026-10-14 22:17:22 | [CVE-2026-110695](https://nvd.nist.gov/vuln/detail/CVE-2026-110695) | Low | 2.1 | A vulnerability was detected in turboderp ExLlamaV2 up to 0.3.2. Affected is the function STFile.get_tensor of the file… |
| 2026-10-14 22:17:22 | [CVE-2026-110696](https://nvd.nist.gov/vuln/detail/CVE-2026-110696) | Medium | 5.5 | A weakness has been identified in itsmeravitejak Online-Examination-System up to e6208e630b14657999bbfe4c9912302d2a1e24… |
| 2026-10-14 22:17:23 | [CVE-2026-110698](https://nvd.nist.gov/vuln/detail/CVE-2026-110698) | Low | 2.1 | A security vulnerability has been detected in Praat up to 7.0.02. Affected is the function whisper_model_load of the fi… |
| 2026-10-14 22:17:23 | [CVE-2026-110816](https://nvd.nist.gov/vuln/detail/CVE-2026-110816) | Medium | 6.3 | ### Summary `qs.stringify` with `arrayFormat: 'comma'` throws `TypeError: Cannot convert object to primitive value` whe… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
