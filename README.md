# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-11-09 14:18 UTC

New CVEs published between 2026-11-09 13:21 UTC and 2026-11-09 14:18 UTC.

[Full CSV](data/new-cves-2026-11-09T14-18-22-731106Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-11-09 14:17:06 | [CVE-2026-119274](https://nvd.nist.gov/vuln/detail/CVE-2026-119274) | Medium | 4.8 | Stored XSS attacks occur when an attacker injects a malicious script in Global Smart Folders feature in NIOS |
| 2026-11-09 14:17:06 | [CVE-2026-119743](https://nvd.nist.gov/vuln/detail/CVE-2026-119743) | Medium | 6.3 | pdfmake before 0.3.14 contains a shared resource caching vulnerability that allows attackers to access cross-document c… |
| 2026-11-09 14:17:08 | [CVE-2026-121841](https://nvd.nist.gov/vuln/detail/CVE-2026-121841) |  |  | Other issue in Firefox for iOS. This vulnerability was fixed in Firefox for iOS 160.0. |
| 2026-11-09 14:17:08 | [CVE-2026-121842](https://nvd.nist.gov/vuln/detail/CVE-2026-121842) |  |  | Privilege escalation in the Reader View component in Firefox for iOS. This vulnerability was fixed in Firefox for iOS 1… |
| 2026-11-09 14:17:08 | [CVE-2026-121843](https://nvd.nist.gov/vuln/detail/CVE-2026-121843) |  |  | Privilege escalation in Firefox for iOS. This vulnerability was fixed in Firefox for iOS 160.0. |
| 2026-11-09 14:17:16 | [CVE-2026-124624](https://nvd.nist.gov/vuln/detail/CVE-2026-124624) | Medium | 5.5 | A weakness has been identified in PipraPay 3.0.0. Affected by this vulnerability is the function hash_hmac of the file… |
| 2026-11-09 14:17:16 | [CVE-2026-124625](https://nvd.nist.gov/vuln/detail/CVE-2026-124625) | Low | 2.1 | A security vulnerability has been detected in PipraPay 3.0.0. Affected by this issue is the function deleteData of the… |
| 2026-11-09 14:17:16 | [CVE-2026-124635](https://nvd.nist.gov/vuln/detail/CVE-2026-124635) | Medium | 5.1 | A vulnerability was identified in kevquirk PureBlog up to 3.7.2. Impacted is an unknown function of the file admin/uplo… |
| 2026-11-09 14:17:16 | [CVE-2026-16283](https://nvd.nist.gov/vuln/detail/CVE-2026-16283) | High | 8.8 | Improper neutralization of special elements used in an OS command ('OS command injection') vulnerability in Osbil Techn… |
| 2026-11-09 14:17:24 | [CVE-2026-95778](https://nvd.nist.gov/vuln/detail/CVE-2026-95778) | High | 8.8 | A remote code execution vulnerability exists in HPE Morpheus Software. |
| 2026-11-09 14:17:25 | [CVE-2026-95779](https://nvd.nist.gov/vuln/detail/CVE-2026-95779) | High | 8.8 | An exposure of the appliance’s confidential certificate information vulnerability exists in HPE Morpheus manager softwa… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
