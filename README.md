# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-11-03 08:18 UTC

New CVEs published between 2026-11-03 07:19 UTC and 2026-11-03 08:18 UTC.

[Full CSV](data/new-cves-2026-11-03T08-18-19-331016Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-11-03 08:17:13 | [CVE-2026-103653](https://nvd.nist.gov/vuln/detail/CVE-2026-103653) | Medium | 6.7 | An out-of-bounds read vulnerability in the Qt CoAP message parsing (QCoapInternalReply::createFromFrame()) of the Qt Co… |
| 2026-11-03 08:17:15 | [CVE-2026-120988](https://nvd.nist.gov/vuln/detail/CVE-2026-120988) |  |  | billboard.js before 4.1.3 allows an attacker to execute malicious JavaScript due to improper sanitization of series ids… |
| 2026-11-03 08:17:15 | [CVE-2026-13594](https://nvd.nist.gov/vuln/detail/CVE-2026-13594) | Critical | 9.1 | Zoho Corporation's ManageEngine Log360 and EventLog Analyzer versions 13062 and below are vulnerable to an issue that c… |
| 2026-11-03 08:17:15 | [CVE-2026-16900](https://nvd.nist.gov/vuln/detail/CVE-2026-16900) | High | 7.5 | Zohocorp ManageEngine Log360 and EventLog Analyzer versions 13071 and below are vulnerable to an authentication bypass… |
| 2026-11-03 08:17:15 | [CVE-2026-4052](https://nvd.nist.gov/vuln/detail/CVE-2026-4052) | Critical | 9.8 | This issue only impacts deployments where WSO2 Identity Server is configured as a Resident Key Manager with database sh… |
| 2026-11-03 08:17:15 | [CVE-2026-74846](https://nvd.nist.gov/vuln/detail/CVE-2026-74846) |  |  | Catalyst::Plugin::Authentication versions before 0.10029 for Perl allow timing attacks on stored passwords via eq compa… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
