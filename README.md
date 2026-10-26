# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-26 12:19 UTC

New CVEs published between 2026-10-26 11:18 UTC and 2026-10-26 12:19 UTC.

[Full CSV](data/new-cves-2026-10-26T12-19-21-956385Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-10-26 12:17:01 | [CVE-2012-20006](https://nvd.nist.gov/vuln/detail/CVE-2012-20006) |  |  | Rejected reason: This CVE ID has been rejected or withdrawn by its CVE Numbering Authority. |
| 2026-10-26 12:17:02 | [CVE-2026-105947](https://nvd.nist.gov/vuln/detail/CVE-2026-105947) | Medium | 6.5 | Improper Limitation of a Pathname to a Restricted Directory ('Path Traversal') vulnerability in Innotim Software, Telec… |
| 2026-10-26 12:17:04 | [CVE-2026-115717](https://nvd.nist.gov/vuln/detail/CVE-2026-115717) | Medium | 6.3 | Frappe Builder versions before 1.36.1 contain a server-side request forgery vulnerability in the convert_to_webp API en… |
| 2026-10-26 12:17:05 | [CVE-2026-115718](https://nvd.nist.gov/vuln/detail/CVE-2026-115718) | Medium | 5.3 | Frappe Builder versions 1.33.0 before1.36.0 contain a missing authorization vulnerability in the improve_prompt endpoin… |
| 2026-10-26 12:17:05 | [CVE-2026-115720](https://nvd.nist.gov/vuln/detail/CVE-2026-115720) | Medium | 5.3 | Frappe Builder before 1.36.1 contains a server-side request forgery vulnerability in builder/api.py where the assert_no… |
| 2026-10-26 12:17:06 | [CVE-2026-116260](https://nvd.nist.gov/vuln/detail/CVE-2026-116260) | Medium | 5.5 | A weakness has been identified in libimobiledevice up to 1.4.0. This issue affects the function service_receive of the… |
| 2026-10-26 12:17:06 | [CVE-2026-116261](https://nvd.nist.gov/vuln/detail/CVE-2026-116261) | Low | 2.0 | A security vulnerability has been detected in libimobiledevice up to 1.4.0. Impacted is the function afc_file_open of t… |
| 2026-10-26 12:17:06 | [CVE-2026-116262](https://nvd.nist.gov/vuln/detail/CVE-2026-116262) | Low | 2.1 | A vulnerability was detected in libimobiledevice up to 1.4.0. The affected element is the function webinspector_receive… |
| 2026-10-26 12:17:07 | [CVE-2026-116263](https://nvd.nist.gov/vuln/detail/CVE-2026-116263) | Low | 1.2 | A flaw has been found in HaschekSolutions PictShare up to 3.7.1. The impacted element is the function architect of the… |
| 2026-10-26 12:17:08 | [CVE-2026-94380](https://nvd.nist.gov/vuln/detail/CVE-2026-94380) | High | 8.1 | Weak Password Recovery Mechanism for Forgotten Password vulnerability in HAVELSAN Inc. Liman MYS allows Password Recove… |
| 2026-10-26 12:17:08 | [CVE-2026-96432](https://nvd.nist.gov/vuln/detail/CVE-2026-96432) | Low | 2.1 | A malicious or compromised HTTP/2 server withholding SETTINGS ACK can send RST_STREAM on a completed stream, planting a… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
