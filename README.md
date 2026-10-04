# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-04 00:20 UTC

New CVEs published between 2026-10-03 23:18 UTC and 2026-10-04 00:20 UTC.

[Full CSV](data/new-cves-2026-10-04T00-20-26-08771Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-10-04 00:16:35 | [CVE-2026-105123](https://nvd.nist.gov/vuln/detail/CVE-2026-105123) | High | 8.7 | W (vincent-peugnet/wcms) through 3.18.0 contains a remote code execution vulnerability that allows authenticated editor… |
| 2026-10-04 00:16:35 | [CVE-2026-105124](https://nvd.nist.gov/vuln/detail/CVE-2026-105124) | Medium | 5.3 | W (vincent-peugnet/wcms) through 3.18.0 contains a stored cross-site scripting vulnerability that allows unauthenticate… |
| 2026-10-04 00:16:35 | [CVE-2026-105125](https://nvd.nist.gov/vuln/detail/CVE-2026-105125) | Medium | 6.3 | LaraDashboard before 1.4.8 contains a path traversal vulnerability that allows unauthenticated attackers to read JSON f… |
| 2026-10-04 00:16:36 | [CVE-2026-105126](https://nvd.nist.gov/vuln/detail/CVE-2026-105126) | High | 8.6 | LaraDashboard before 1.4.8 contains an improper privilege management vulnerability that allows authenticated Admin user… |
| 2026-10-04 00:16:36 | [CVE-2026-105127](https://nvd.nist.gov/vuln/detail/CVE-2026-105127) | Medium | 6.9 | LaraDashboard 1.4.2 before 1.4.8 applies advanced email validation to unauthenticated forgot-password and reset-passwor… |
| 2026-10-04 00:16:36 | [CVE-2026-105128](https://nvd.nist.gov/vuln/detail/CVE-2026-105128) | Medium | 5.3 | LaraDashboard before 1.4.8 contains an open redirect vulnerability that allows remote attackers to redirect users by su… |
| 2026-10-04 00:16:36 | [CVE-2026-105129](https://nvd.nist.gov/vuln/detail/CVE-2026-105129) | High | 7.1 | LaraDashboard before 1.4.8 contains an incorrect authorization vulnerability that allows authenticated users with only… |
| 2026-10-04 00:16:36 | [CVE-2026-105130](https://nvd.nist.gov/vuln/detail/CVE-2026-105130) | Medium | 6.3 | LaraDashboard from 1.4.0 before 1.4.8 contains a race condition vulnerability in RegisterController::register that allo… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
