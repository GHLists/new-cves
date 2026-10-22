# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-22 14:18 UTC

New CVEs published between 2026-10-22 13:18 UTC and 2026-10-22 14:18 UTC.

[Full CSV](data/new-cves-2026-10-22T14-18-40-110979Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-10-22 14:17:37 | [CVE-2026-107079](https://nvd.nist.gov/vuln/detail/CVE-2026-107079) |  |  | An issue in Systrome Validation & Certification 1.0 allows an attacker to cause a denial of service via the t URL param… |
| 2026-10-22 14:17:37 | [CVE-2026-111497](https://nvd.nist.gov/vuln/detail/CVE-2026-111497) | Critical | 9.2 | A buffer overflow vulnerability in the Brotli decoder (c/dec/decode.c) in Google Brotli versions 1.0.3 through 1.2.0 on… |
| 2026-10-22 14:17:38 | [CVE-2026-113582](https://nvd.nist.gov/vuln/detail/CVE-2026-113582) | High | 8.7 | UNSUPPORTED WHEN ASSIGNED Improper restriction of XML external entity references in Apache Abdera allows an attacker to… |
| 2026-10-22 14:17:38 | [CVE-2026-115247](https://nvd.nist.gov/vuln/detail/CVE-2026-115247) | Low | 2.1 | A security vulnerability has been detected in subhajitkhan online-clinic-management-system up to e9ee77a8827a1446220fa0… |
| 2026-10-22 14:17:38 | [CVE-2026-115248](https://nvd.nist.gov/vuln/detail/CVE-2026-115248) | Low | 2.1 | A vulnerability was detected in subhajitkhan online-clinic-management-system up to e9ee77a8827a1446220fa07ee693dc4d9a29… |
| 2026-10-22 14:17:38 | [CVE-2026-115249](https://nvd.nist.gov/vuln/detail/CVE-2026-115249) | Low | 2.0 | A flaw has been found in subhajitkhan online-clinic-management-system up to e9ee77a8827a1446220fa07ee693dc4d9a29a578. I… |
| 2026-10-22 14:17:39 | [CVE-2026-115400](https://nvd.nist.gov/vuln/detail/CVE-2026-115400) | Medium | 6.7 | crawlseo before version 0.2.5 contains a cleartext storage vulnerability that allows attackers with database read acces… |
| 2026-10-22 14:17:39 | [CVE-2026-115411](https://nvd.nist.gov/vuln/detail/CVE-2026-115411) | Medium | 5.3 | crawlseo before version 0.2.4 contains a server-side request forgery vulnerability in its crawler engine where isPrivat… |
| 2026-10-22 14:17:43 | [CVE-2026-66279](https://nvd.nist.gov/vuln/detail/CVE-2026-66279) | High | 7.2 | In Connect SDK 4.3.1 and earlier and Flex SDK 3.7.7 and earlier, a message with invalid security settings may bypass au… |
| 2026-10-22 14:17:43 | [CVE-2026-66281](https://nvd.nist.gov/vuln/detail/CVE-2026-66281) | Medium | 6.0 | In EmberZNet 9.1.1 and earlier, a malformed Discover Attributes command can result in a loop with unreachable exit cond… |
| 2026-10-22 14:17:44 | [CVE-2026-66282](https://nvd.nist.gov/vuln/detail/CVE-2026-66282) | Medium | 6.0 | In EmberZNet 9.1.1 and earlier, a malformed Publish Billing Period command can result in a recursive function call that… |
| 2026-10-22 14:17:50 | [CVE-2026-85079](https://nvd.nist.gov/vuln/detail/CVE-2026-85079) | High | 7.5 | In EmberZNet 9.1.1 and earlier, a malformed Simple_Desc_req response can result in an out-of-bounds write potentially l… |
| 2026-10-22 14:17:51 | [CVE-2026-85080](https://nvd.nist.gov/vuln/detail/CVE-2026-85080) | Medium | 6.0 | In EmberZNet 9.1.1 and earlier, a malformed GetGroupMembership message can result in an out-of-bounds write leading to… |
| 2026-10-22 14:17:51 | [CVE-2026-89409](https://nvd.nist.gov/vuln/detail/CVE-2026-89409) | Medium | 5.3 | In Z-Wave SDK 8.1.1 and earlier (for 700/800 series devices) and 6.85.02 and earlier (for 500 series devices), missing… |
| 2026-10-22 14:17:51 | [CVE-2026-89410](https://nvd.nist.gov/vuln/detail/CVE-2026-89410) | Medium | 5.1 | In Z-Wave SDK 8.1.1 and earlier, a malformed NCP SPI command can trigger out-of-bounds reads that leak sensitive inform… |
| 2026-10-22 14:17:51 | [CVE-2026-92709](https://nvd.nist.gov/vuln/detail/CVE-2026-92709) | High | 8.1 | Rsyslog is a rocket-fast system for log processing. From versions 1.15.0 to 8.2610.0, rsyslog's omfile dynaFile facilit… |
| 2026-10-22 14:17:51 | [CVE-2026-94502](https://nvd.nist.gov/vuln/detail/CVE-2026-94502) | High | 7.5 | In EmberZNet 9.1.1 and earlier, a malformed Publish Price Matrix command can result in an out-of-bounds write potential… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
