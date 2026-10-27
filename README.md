# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-27 15:18 UTC

New CVEs published between 2026-10-27 14:18 UTC and 2026-10-27 15:18 UTC.

[Full CSV](data/new-cves-2026-10-27T15-18-49-638438Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-10-27 15:16:31 | [CVE-2026-105987](https://nvd.nist.gov/vuln/detail/CVE-2026-105987) | Medium | 5.1 | KGS Software tia Viewer is vulnerable to Stored XSS via the annotation API. Due to the lack of input validation, an aut… |
| 2026-10-27 15:16:57 | [CVE-2026-117505](https://nvd.nist.gov/vuln/detail/CVE-2026-117505) | Medium | 5.3 | A security flaw has been discovered in a2aproject a2a-java up to 1.2.0.Final. The impacted element is the function queu… |
| 2026-10-27 15:16:57 | [CVE-2026-117506](https://nvd.nist.gov/vuln/detail/CVE-2026-117506) | Medium | 5.3 | A weakness has been identified in a2aproject a2a-java up to 1.2.0.Final. This affects the function InMemoryPushNotifica… |
| 2026-10-27 15:16:57 | [CVE-2026-117507](https://nvd.nist.gov/vuln/detail/CVE-2026-117507) | Medium | 5.3 | A security vulnerability has been detected in a2aproject a2a-java up to 1.2.0.Final. This impacts the function TaskMana… |
| 2026-10-27 15:16:57 | [CVE-2026-117604](https://nvd.nist.gov/vuln/detail/CVE-2026-117604) | High | 8.7 | Grav from 1.7.53.3 before 1.7.53.6 contains an authorization bypass in Debugger::isDebuggerRequestAuthorized() that all… |
| 2026-10-27 15:17:00 | [CVE-2026-78845](https://nvd.nist.gov/vuln/detail/CVE-2026-78845) |  |  | Aidot products Linkind Matter Smart Plug 1.01.32, OREiN Matter Smart Light Bulb 3.15.21, and Linkind Wi-Fi Smart Light… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
