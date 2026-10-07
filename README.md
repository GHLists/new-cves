# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-07 13:21 UTC

New CVEs published between 2026-10-07 12:18 UTC and 2026-10-07 13:21 UTC.

[Full CSV](data/new-cves-2026-10-07T13-21-20-447613Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-10-07 13:17:16 | [CVE-2026-102255](https://nvd.nist.gov/vuln/detail/CVE-2026-102255) |  |  | A Pre-authentication SSRF vulnerability exists in the SMA1000 Appliance Work Place interface due to an unintended alter… |
| 2026-10-07 13:17:16 | [CVE-2026-102256](https://nvd.nist.gov/vuln/detail/CVE-2026-102256) |  |  | Post-authentication Improper Neutralization of Special Elements used in an OS Command ('OS Command Injection') vulnerab… |
| 2026-10-07 13:17:16 | [CVE-2026-103435](https://nvd.nist.gov/vuln/detail/CVE-2026-103435) | High | 7.7 | Claude Code validated that a target file path resided within the project working directory at permission-check time, bu… |
| 2026-10-07 13:17:16 | [CVE-2026-105138](https://nvd.nist.gov/vuln/detail/CVE-2026-105138) | High | 7.1 | Obot 0.12.0 before 0.26.2 contains an insufficiently protected credentials vulnerability that allows authenticated user… |
| 2026-10-07 13:17:19 | [CVE-2026-105139](https://nvd.nist.gov/vuln/detail/CVE-2026-105139) | Medium | 5.3 | Obot 0.26.0 before 0.26.2 contains an authorization bypass vulnerability that allows authenticated users matching any v… |
| 2026-10-07 13:17:19 | [CVE-2026-105140](https://nvd.nist.gov/vuln/detail/CVE-2026-105140) | Low | 2.3 | Obot 0.25.0 before 0.25.6 and 0.26.0 before 0.26.1 contains a race condition in auth provider group refreshes that can… |
| 2026-10-07 13:17:19 | [CVE-2026-107151](https://nvd.nist.gov/vuln/detail/CVE-2026-107151) | Medium | 5.9 | Missing authentication has been found in remote-execution task updates in the smart_proxy_dynflow package. The progress… |
| 2026-10-07 13:17:19 | [CVE-2026-107162](https://nvd.nist.gov/vuln/detail/CVE-2026-107162) | High | 7.6 | Express Gateway through 1.16.11 contains an authentication bypass vulnerability in the OAuth 2.0 refresh_token grant th… |
| 2026-10-07 13:17:20 | [CVE-2026-107168](https://nvd.nist.gov/vuln/detail/CVE-2026-107168) | Medium | 6.2 | A flaw was found in m17n-lib. By providing crafted input containing an invalid UTF-8 character sequence, an attacker ca… |
| 2026-10-07 13:17:20 | [CVE-2026-107170](https://nvd.nist.gov/vuln/detail/CVE-2026-107170) | Low | 2.9 | A flaw was found in m17n-lib. A partial failure during library initialization can leave an internal driver pointer unin… |
| 2026-10-07 13:17:20 | [CVE-2026-107175](https://nvd.nist.gov/vuln/detail/CVE-2026-107175) | Medium | 5.3 | MISP contains a defect in its event save workflow that prevents the correlation engine from recalculating correlations… |
| 2026-10-07 13:17:20 | [CVE-2026-107177](https://nvd.nist.gov/vuln/detail/CVE-2026-107177) | High | 7.4 | Express Gateway through 1.16.11 contains a hardcoded cryptographic key vulnerability that allows attackers with datasto… |
| 2026-10-07 13:17:22 | [CVE-2026-107180](https://nvd.nist.gov/vuln/detail/CVE-2026-107180) | High | 7.1 | On MISP instances configured to require TOTP enrolment (Security.otp_required), the enforcement of the mandatory two-fa… |
| 2026-10-07 13:17:22 | [CVE-2026-41958](https://nvd.nist.gov/vuln/detail/CVE-2026-41958) | Medium | 6.5 | A path traversal vulnerability exists in the unzip_http RemoteZipFile extract functionality of VisiData (version(s): de… |
| 2026-10-07 13:17:22 | [CVE-2026-42532](https://nvd.nist.gov/vuln/detail/CVE-2026-42532) | Medium | 5.5 | A path traversal vulnerability exists in the EmailSheet extract_parts functionality of VisiData (version(s): dev (commi… |
| 2026-10-07 13:17:22 | [CVE-2026-98373](https://nvd.nist.gov/vuln/detail/CVE-2026-98373) |  |  | In the Linux kernel, the following vulnerability has been resolved: mm/hugetlb: preserve mremap address delta when skip… |
| 2026-10-07 13:17:23 | [CVE-2026-98374](https://nvd.nist.gov/vuln/detail/CVE-2026-98374) |  |  | In the Linux kernel, the following vulnerability has been resolved: tcp: fix use-after-free of retransmit_skb_hint in t… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
