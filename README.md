# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-09-25 13:18 UTC

New CVEs published between 2026-09-25 12:19 UTC and 2026-09-25 13:18 UTC.

[Full CSV](data/new-cves-2026-09-25T13-18-54-749989Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-09-25 13:17:05 | [CVE-2025-51457](https://nvd.nist.gov/vuln/detail/CVE-2025-51457) |  |  | D-Link DAP-2610 up to 2.06B08r099 contains an authenticated command injection vulnerability within the web interface at… |
| 2026-09-25 13:17:14 | [CVE-2026-51772](https://nvd.nist.gov/vuln/detail/CVE-2026-51772) |  |  | A Server-Side Request Forgery (SSRF) vulnerability exists in the Image API (v2) of OpenStack Glance. When the show_mult… |
| 2026-09-25 13:17:14 | [CVE-2026-51773](https://nvd.nist.gov/vuln/detail/CVE-2026-51773) |  |  | An issue in the VMware datastore driver of OpenStack glance_store. When an authenticated attacker provides a maliciousl… |
| 2026-09-25 13:17:14 | [CVE-2026-52622](https://nvd.nist.gov/vuln/detail/CVE-2026-52622) | High | 7.5 | An issue in Wellav Technologies Co., Ltd Wellav WES Emergency Broadcast Terminal WES100, WES270, WES280, and WES290 bef… |
| 2026-09-25 13:17:16 | [CVE-2026-78902](https://nvd.nist.gov/vuln/detail/CVE-2026-78902) |  |  | Cross Site Scripting vulnerability in Netgate pfSense 26.03.1-RELEASE allows an attacker to execute arbitrary code via… |
| 2026-09-25 13:17:16 | [CVE-2026-79153](https://nvd.nist.gov/vuln/detail/CVE-2026-79153) |  |  | Seclore FileSecure Desktop Client before 3.25.1.0 contains improper access control vulnerability in the kernel-mode dri… |
| 2026-09-25 13:17:16 | [CVE-2026-88420](https://nvd.nist.gov/vuln/detail/CVE-2026-88420) |  |  | A reflected cross-site scripting (XSS) vulnerability in the EntryAbstract.save() component of APSL puput v1.2.1 through… |
| 2026-09-25 13:17:16 | [CVE-2026-88421](https://nvd.nist.gov/vuln/detail/CVE-2026-88421) |  |  | Incorrect access control in the BlogPage.get_entries() component of APSL puput v1.2.1 through v2.2.0 allows unauthentic… |
| 2026-09-25 13:17:24 | [CVE-2026-95832](https://nvd.nist.gov/vuln/detail/CVE-2026-95832) | Critical | 9.3 | Improper Neutralization of Special Elements in Output Used by a Downstream Component in the colour control escape code… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
