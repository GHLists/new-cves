# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-11-12 10:18 UTC

New CVEs published between 2026-11-12 09:18 UTC and 2026-11-12 10:18 UTC.

[Full CSV](data/new-cves-2026-11-12T10-18-53-831066Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-11-12 10:17:26 | [CVE-2026-106140](https://nvd.nist.gov/vuln/detail/CVE-2026-106140) | High | 7.3 | In Progress® Telerik® Reporting prior to version 20.3.26.1110, a deserialization of untrusted data vulnerability in the… |
| 2026-11-12 10:17:28 | [CVE-2026-117474](https://nvd.nist.gov/vuln/detail/CVE-2026-117474) |  |  | Rejected reason: none |
| 2026-11-12 10:17:28 | [CVE-2026-117475](https://nvd.nist.gov/vuln/detail/CVE-2026-117475) |  |  | Rejected reason: none |
| 2026-11-12 10:17:28 | [CVE-2026-117476](https://nvd.nist.gov/vuln/detail/CVE-2026-117476) |  |  | Rejected reason: none |
| 2026-11-12 10:17:28 | [CVE-2026-118975](https://nvd.nist.gov/vuln/detail/CVE-2026-118975) | Medium | 6.5 | In Progress® Telerik® Reporting prior to version 20.3.26.1110, improper restriction of XML external entity references i… |
| 2026-11-12 10:17:28 | [CVE-2026-123765](https://nvd.nist.gov/vuln/detail/CVE-2026-123765) |  |  | Improper neutralization of input during web page generation ('cross-site scripting') vulnerability in Apache Sling XSS.… |
| 2026-11-12 10:17:28 | [CVE-2026-124617](https://nvd.nist.gov/vuln/detail/CVE-2026-124617) |  |  | Rejected reason: 歸類為 JSONCPP Open Source 之問題 |
| 2026-11-12 10:17:28 | [CVE-2026-124699](https://nvd.nist.gov/vuln/detail/CVE-2026-124699) | High | 7.8 | In Telerik UI for WinForms, versions prior to 2026.4.1111, an improper control of code generation vulnerability exists… |
| 2026-11-12 10:17:28 | [CVE-2026-127016](https://nvd.nist.gov/vuln/detail/CVE-2026-127016) | Critical | 9.2 | The MISP Modules website component exposes external tool management endpoints (add, delete, change status, and change c… |
| 2026-11-12 10:17:29 | [CVE-2026-76173](https://nvd.nist.gov/vuln/detail/CVE-2026-76173) | High | 8.8 | Blind SQL injection vulnerability in the public endpoint `public/webhook/receiver.php` of the WhatsApp module for Dolib… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
