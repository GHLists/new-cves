# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-30 11:18 UTC

New CVEs published between 2026-10-30 10:22 UTC and 2026-10-30 11:18 UTC.

[Full CSV](data/new-cves-2026-10-30T11-18-54-314808Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-10-30 11:17:31 | [CVE-2025-31704](https://nvd.nist.gov/vuln/detail/CVE-2025-31704) | Critical | 9.8 | A vulnerability has been found in the Dahua Intelligent Connection Center. A remote attacker could send a specially cra… |
| 2026-10-30 11:17:32 | [CVE-2026-116366](https://nvd.nist.gov/vuln/detail/CVE-2026-116366) | Critical | 9.5 | An issue has been discovered in ClickHouse Server that, under certain conditions, could allow an unauthenticated user w… |
| 2026-10-30 11:17:32 | [CVE-2026-22105](https://nvd.nist.gov/vuln/detail/CVE-2026-22105) | High | 8.7 | Delta UFC500 charging stations derive the default credentials of the Service account from character positions of the de… |
| 2026-10-30 11:17:32 | [CVE-2026-22109](https://nvd.nist.gov/vuln/detail/CVE-2026-22109) | High | 8.4 | The shipped WebUI template database retains the factory default passwords for all five account types in cleartext. Defa… |
| 2026-10-30 11:17:33 | [CVE-2026-22110](https://nvd.nist.gov/vuln/detail/CVE-2026-22110) | High | 8.7 | The web server does not check authentication on POST or PUT. An unauthenticated attacker can reboot the charger; by bru… |
| 2026-10-30 11:17:33 | [CVE-2026-22114](https://nvd.nist.gov/vuln/detail/CVE-2026-22114) | Medium | 5.3 | HTTP basic auth enforces no retry limit or backoff. Combined with the default service password, the keyspace is exhaust… |
| 2026-10-30 11:17:33 | [CVE-2026-85268](https://nvd.nist.gov/vuln/detail/CVE-2026-85268) | High | 8.7 | A Cross-Site Scripting (XSS) (CWE-79) vulnerability in the auth/handler in Google Cloud Identity Platform and Firebase… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
