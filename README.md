# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-04 15:18 UTC

New CVEs published between 2026-10-04 14:19 UTC and 2026-10-04 15:18 UTC.

[Full CSV](data/new-cves-2026-10-04T15-18-36-713429Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-10-04 15:16:30 | [CVE-2026-105156](https://nvd.nist.gov/vuln/detail/CVE-2026-105156) | Low | 2.9 | A weakness has been identified in YzmCMS up to 7.6. Impacted is the function Password of the file /common/function/syst… |
| 2026-10-04 15:16:30 | [CVE-2026-105157](https://nvd.nist.gov/vuln/detail/CVE-2026-105157) | Low | 2.1 | A security vulnerability has been detected in RainyGao DocSys up to 2.02.85. The affected element is the function DocCo… |
| 2026-10-04 15:16:31 | [CVE-2026-105158](https://nvd.nist.gov/vuln/detail/CVE-2026-105158) | Medium | 5.5 | A vulnerability was detected in RainyGao DocSys up to 2.02.85. The impacted element is the function BaseController.crea… |
| 2026-10-04 15:16:31 | [CVE-2026-105205](https://nvd.nist.gov/vuln/detail/CVE-2026-105205) | Medium | 6.9 | SiYuan before 3.8.5 contains an information disclosure vulnerability that allows publish-mode readers to learn backlink… |
| 2026-10-04 15:16:31 | [CVE-2026-105206](https://nvd.nist.gov/vuln/detail/CVE-2026-105206) | Medium | 5.3 | ZITADEL 3.0.0 through 3.4.15 and 4.x before 4.17.3 contains an incorrect authorization flaw in the User Service API, wh… |
| 2026-10-04 15:16:31 | [CVE-2026-105207](https://nvd.nist.gov/vuln/detail/CVE-2026-105207) | Critical | 9.3 | ZITADEL 3.0.0 through 3.4.15 and 4.0.0 before 4.17.3 creates links between user accounts and external identity provider… |
| 2026-10-04 15:16:31 | [CVE-2026-105208](https://nvd.nist.gov/vuln/detail/CVE-2026-105208) | High | 8.7 | ZITADEL 4.x before 4.17.3 and 3.x through 3.4.15 protects IdP intent tokens with unauthenticated, malleable encryption,… |
| 2026-10-04 15:16:32 | [CVE-2026-105209](https://nvd.nist.gov/vuln/detail/CVE-2026-105209) | Critical | 9.3 | ZITADEL 3.x before 3.4.15 and 4.x before 4.17.1 contains an improper authorization vulnerability: when issuing passkey… |
| 2026-10-04 15:16:32 | [CVE-2026-105210](https://nvd.nist.gov/vuln/detail/CVE-2026-105210) | High | 8.8 | ZITADEL 3.x before 3.4.15 and 4.x before 4.17.1 contains a missing authentication flaw in the hosted Login V1 UI, whose… |
| 2026-10-04 15:16:32 | [CVE-2026-105211](https://nvd.nist.gov/vuln/detail/CVE-2026-105211) | Critical | 9.2 | ZITADEL before 4.17.1 contains an authentication bypass vulnerability in Login V2 that allows unauthenticated attackers… |
| 2026-10-04 15:16:32 | [CVE-2026-105212](https://nvd.nist.gov/vuln/detail/CVE-2026-105212) | High | 8.7 | ZITADEL 3.x before 3.4.14 and 4.x before 4.16.2 contains an authentication bypass in the hosted Login V1 and Login V2 U… |
| 2026-10-04 15:16:32 | [CVE-2026-105213](https://nvd.nist.gov/vuln/detail/CVE-2026-105213) | High | 8.8 | ZITADEL 4.x before 4.17.1 does not check an organization's inactive state during Login V2 authentication, verifying onl… |
| 2026-10-04 15:16:32 | [CVE-2026-105214](https://nvd.nist.gov/vuln/detail/CVE-2026-105214) | Low | 2.3 | Zitadel before 4.16.2 contains a server-side request forgery vulnerability that allows attackers to make the server req… |
| 2026-10-04 15:16:32 | [CVE-2026-105215](https://nvd.nist.gov/vuln/detail/CVE-2026-105215) | Critical | 9.3 | ZITADEL before 3.4.14 and 4.x before 4.16.2 contains an authentication bypass in the hosted Login V1 UI because the 'ex… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
