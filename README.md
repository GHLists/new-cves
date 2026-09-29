# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-09-29 12:21 UTC

New CVEs published between 2026-09-29 11:18 UTC and 2026-09-29 12:21 UTC.

[Full CSV](data/new-cves-2026-09-29T12-21-27-001724Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-09-29 12:17:09 | [CVE-2026-101266](https://nvd.nist.gov/vuln/detail/CVE-2026-101266) | Low | 1.3 | A logic flaw in the checkout flow allows users to bypass validations performed during the check-in by skipping entire c… |
| 2026-09-29 12:17:09 | [CVE-2026-102495](https://nvd.nist.gov/vuln/detail/CVE-2026-102495) |  |  | Apache XmlSchema doesn't limit how deeply schema imports and includes can be nested, so a malicious schema can make par… |
| 2026-09-29 12:17:09 | [CVE-2026-102496](https://nvd.nist.gov/vuln/detail/CVE-2026-102496) |  |  | Apache XmlSchema doesn't limit how deeply schema structures can be nested when it builds its schema model, so a malicio… |
| 2026-09-29 12:17:09 | [CVE-2026-102497](https://nvd.nist.gov/vuln/detail/CVE-2026-102497) |  |  | The Apache XmlSchema walker (xmlschema-walker) doesn't detect cycles in type derivation, substitution groups, model gro… |
| 2026-09-29 12:17:09 | [CVE-2026-102507](https://nvd.nist.gov/vuln/detail/CVE-2026-102507) | Medium | 6.8 | Sliver C2 framework version 1.7.7 and earlier contains an unhandled panic vulnerability in the operator gRPC handler th… |
| 2026-09-29 12:17:10 | [CVE-2026-41875](https://nvd.nist.gov/vuln/detail/CVE-2026-41875) | Medium | 6.9 | Quick.Cart is vulnerable to Cross-Site Request Forgery in admin config panel. Malicious attacker can craft special webs… |
| 2026-09-29 12:17:10 | [CVE-2026-66083](https://nvd.nist.gov/vuln/detail/CVE-2026-66083) |  |  | The /datasources/unauth-datasource endpoint does not properly enforce data source authorization. An authenticated user… |
| 2026-09-29 12:17:11 | [CVE-2026-73593](https://nvd.nist.gov/vuln/detail/CVE-2026-73593) | Low | 3.0 | Dell Secure Connect Gateway (SCG) Policy Manager, versions prior to 5.34.00.16, contains an Active Debug Code vulnerabi… |
| 2026-09-29 12:17:11 | [CVE-2026-73594](https://nvd.nist.gov/vuln/detail/CVE-2026-73594) | Medium | 6.4 | Dell Secure Connect Gateway (SCG) Policy Manager, versions prior to 5.34.00.16, Versions prior to 5.36, contains an Imp… |
| 2026-09-29 12:17:11 | [CVE-2026-73595](https://nvd.nist.gov/vuln/detail/CVE-2026-73595) | Medium | 4.7 | Dell Secure Connect Gateway (SCG) Policy Manager, versions prior to 5.34.00.16, Versions prior to 5.36, contains a Down… |
| 2026-09-29 12:17:11 | [CVE-2026-73596](https://nvd.nist.gov/vuln/detail/CVE-2026-73596) | Low | 3.8 | Dell Secure Connect Gateway (SCG) Policy Manager, versions prior to 5.34.00.16, contains an Initialization of a Resourc… |
| 2026-09-29 12:17:11 | [CVE-2026-73597](https://nvd.nist.gov/vuln/detail/CVE-2026-73597) | Medium | 6.5 | Dell Secure Connect Gateway (SCG) Policy Manager, versions prior to 5.34.00.16, contains a Cross-Site Request Forgery (… |
| 2026-09-29 12:17:12 | [CVE-2026-85520](https://nvd.nist.gov/vuln/detail/CVE-2026-85520) | Critical | 9.3 | Google Merchant Center Feed (gmfeed) module for PrestaShop is vulnerable to unauthenticated arbitrary file write in the… |
| 2026-09-29 12:17:12 | [CVE-2026-87748](https://nvd.nist.gov/vuln/detail/CVE-2026-87748) | High | 8.8 | Missing Authorization vulnerability in Interprobe Information Technologies Inc. Qorela DC allows Privilege Abuse. This… |
| 2026-09-29 12:17:12 | [CVE-2026-95520](https://nvd.nist.gov/vuln/detail/CVE-2026-95520) | High | 7.1 | A heap-based buffer overflow flaw was found in rpm. Parsing a symlink entry in an untrusted RPM package whose declared… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
