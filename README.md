# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-11-27 15:18 UTC

New CVEs published between 2026-11-27 14:18 UTC and 2026-11-27 15:18 UTC.

[Full CSV](data/new-cves-2026-11-27T15-18-45-611009Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-11-27 15:17:33 | [CVE-2026-110739](https://nvd.nist.gov/vuln/detail/CVE-2026-110739) | Critical | 9.0 | An Incomplete List of Disallowed Inputs in the namespace onboarding API in Google Cloud GKE Fleet versions prior to 202… |
| 2026-11-27 15:17:36 | [CVE-2026-124825](https://nvd.nist.gov/vuln/detail/CVE-2026-124825) | Medium | 5.3 | A flaw was found in 389-ds-base. An integer truncation in the Content Synchronization plugin's changelog-refresh logic… |
| 2026-11-27 15:17:36 | [CVE-2026-129817](https://nvd.nist.gov/vuln/detail/CVE-2026-129817) |  |  | ** UNSUPPORTED WHEN ASSIGNED ** Improper Authentication vulnerability in Apache Submarine. This issue affects Apache Su… |
| 2026-11-27 15:17:40 | [CVE-2026-4641](https://nvd.nist.gov/vuln/detail/CVE-2026-4641) | High | 7.5 | Incorrect Authorization vulnerability in ABB Relion Protection Relays REX610, ABB Relion Protection Relays RE_611 IEC/C… |
| 2026-11-27 15:17:40 | [CVE-2026-4642](https://nvd.nist.gov/vuln/detail/CVE-2026-4642) | High | 7.5 | Incorrect Authorization vulnerability in ABB Relion Protection Relays REX610, ABB Relion Protection Relays RE_611 IEC/C… |
| 2026-11-27 15:17:41 | [CVE-2026-80505](https://nvd.nist.gov/vuln/detail/CVE-2026-80505) | High | 7.3 | Dell Secure Connect Gateway - Virtual Edition, versions prior to 5.36.00.16, contains an Improper Access Control vulner… |
| 2026-11-27 15:17:41 | [CVE-2026-80506](https://nvd.nist.gov/vuln/detail/CVE-2026-80506) | Medium | 5.5 | Dell Secure Connect Gateway - Virtual Edition, versions prior to 5.36.00.16, contains a Use of Hard-coded Cryptographic… |
| 2026-11-27 15:17:41 | [CVE-2026-80507](https://nvd.nist.gov/vuln/detail/CVE-2026-80507) | High | 8.4 | Dell Secure Connect Gateway - Virtual Edition, versions prior to 5.36.00.16, contains a Heap-based Buffer Overflow vuln… |
| 2026-11-27 15:17:41 | [CVE-2026-80508](https://nvd.nist.gov/vuln/detail/CVE-2026-80508) | Medium | 6.8 | Dell Secure Connect Gateway - Virtual Edition, versions prior to 5.36.00.16, contains an Authentication Bypass by Spoof… |
| 2026-11-27 15:17:41 | [CVE-2026-85252](https://nvd.nist.gov/vuln/detail/CVE-2026-85252) | High | 7.1 | A SQL Injection vulnerability in the Revenue Reports API in Google Cloud Apigee Edge Monetization versions prior to 202… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
