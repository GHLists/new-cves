# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-23 21:19 UTC

New CVEs published between 2026-10-23 20:18 UTC and 2026-10-23 21:19 UTC.

[Full CSV](data/new-cves-2026-10-23T21-19-18-686538Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-10-23 21:17:21 | [CVE-2026-113877](https://nvd.nist.gov/vuln/detail/CVE-2026-113877) |  |  | HTTP::Headers::ActionPack versions before 0.10 for Perl allow CPU exhaustion via Accept-Language ranges matched as regu… |
| 2026-10-23 21:17:21 | [CVE-2026-113951](https://nvd.nist.gov/vuln/detail/CVE-2026-113951) |  |  | If an attacker can write to the filesystem of a container k8s cluster container, they can plant an exec credential plug… |
| 2026-10-23 21:17:22 | [CVE-2026-115774](https://nvd.nist.gov/vuln/detail/CVE-2026-115774) | Medium | 4.9 | Twisted is an event-based framework for internet applications, supporting Python 3.6+. Prior to 26.10.0rc1, twisted.mai… |
| 2026-10-23 21:17:23 | [CVE-2026-115775](https://nvd.nist.gov/vuln/detail/CVE-2026-115775) | High | 8.7 | Twisted is an event-based framework for internet applications, supporting Python 3.6+. Prior to 26.10.0rc1, the twisted… |
| 2026-10-23 21:17:23 | [CVE-2026-115776](https://nvd.nist.gov/vuln/detail/CVE-2026-115776) | High | 7.5 | Twisted is an event-based framework for internet applications, supporting Python 3.6+. Prior to 26.10.0rc1, twisted.wor… |
| 2026-10-23 21:17:23 | [CVE-2026-115778](https://nvd.nist.gov/vuln/detail/CVE-2026-115778) | High | 7.5 | Twisted is an event-based framework for internet applications, supporting Python 3.6+. Prior to 26.10.0rc1, twisted.con… |
| 2026-10-23 21:17:23 | [CVE-2026-115800](https://nvd.nist.gov/vuln/detail/CVE-2026-115800) | Low | 1.9 | A vulnerability was identified in UbiquitousLearning mllm up to 2.0.2. The affected element is the function load_model… |
| 2026-10-23 21:17:23 | [CVE-2026-115877](https://nvd.nist.gov/vuln/detail/CVE-2026-115877) | Medium | 5.4 | Twisted is an event-based framework for internet applications, supporting Python 3.6+. Prior to 26.10.0rc1, twisted.web… |
| 2026-10-23 21:17:24 | [CVE-2026-57849](https://nvd.nist.gov/vuln/detail/CVE-2026-57849) |  |  | Rejected reason: This CVE ID has been rejected or withdrawn by its CVE Numbering Authority. |
| 2026-10-23 21:17:24 | [CVE-2026-58202](https://nvd.nist.gov/vuln/detail/CVE-2026-58202) | High | 8.3 | OpenReception's appointment booking software provides an end-to-end encrypted appointment booking platform. Prior to ve… |
| 2026-10-23 21:17:24 | [CVE-2026-65824](https://nvd.nist.gov/vuln/detail/CVE-2026-65824) | High | 7.4 | OpenReception's appointment booking software provides an end-to-end encrypted appointment booking platform. Prior to ve… |
| 2026-10-23 21:17:24 | [CVE-2026-65825](https://nvd.nist.gov/vuln/detail/CVE-2026-65825) | High | 7.5 | OpenReception's appointment booking software provides an end-to-end encrypted appointment booking platform. In versions… |
| 2026-10-23 21:17:25 | [CVE-2026-75524](https://nvd.nist.gov/vuln/detail/CVE-2026-75524) | Medium | 5.4 | OpenReception's appointment booking software provides an end-to-end encrypted appointment booking platform. Prior to ve… |
| 2026-10-23 21:17:25 | [CVE-2026-75525](https://nvd.nist.gov/vuln/detail/CVE-2026-75525) | Medium | 5.3 | OpenReception's appointment booking software provides an end-to-end encrypted appointment booking platform. In versions… |
| 2026-10-23 21:17:25 | [CVE-2026-83813](https://nvd.nist.gov/vuln/detail/CVE-2026-83813) | Low | 3.1 | Twisted is an event-based framework for internet applications, supporting Python 3.6+. Prior to 26.10.0rc1, twisted.nam… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
