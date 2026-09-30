# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-09-30 17:18 UTC

New CVEs published between 2026-09-30 16:18 UTC and 2026-09-30 17:18 UTC.

[Full CSV](data/new-cves-2026-09-30T17-18-37-098745Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-09-30 16:19:10 | [CVE-2026-80490](https://nvd.nist.gov/vuln/detail/CVE-2026-80490) |  |  | Algorithm::AhoCorasick::XS versions through 0.04 for Perl read the haystack string length before the scalar is stringif… |
| 2026-09-30 17:16:40 | [CVE-2026-102489](https://nvd.nist.gov/vuln/detail/CVE-2026-102489) | Critical | 9.4 | Zammad versions 6.3.0 to 6.5.4 are vulnerable a session hijack vulnerability that leads to remote code execution as the… |
| 2026-09-30 17:16:40 | [CVE-2026-102490](https://nvd.nist.gov/vuln/detail/CVE-2026-102490) | Critical | 9.4 | All versions of Zammad including the latest alpha enable the local zammad user to escalate privileges to root. |
| 2026-09-30 17:16:42 | [CVE-2026-103233](https://nvd.nist.gov/vuln/detail/CVE-2026-103233) | Low | 2.1 | A security vulnerability has been detected in AdithyaYelloju Restaurant-Management-System up to 7f0e7e84255e8fcfd488e83… |
| 2026-09-30 17:16:42 | [CVE-2026-103241](https://nvd.nist.gov/vuln/detail/CVE-2026-103241) | Medium | 5.5 | A flaw has been found in vllm-project vLLM up to 0.26.0. This vulnerability affects unknown code of the file rust/src/p… |
| 2026-09-30 17:16:42 | [CVE-2026-103232](https://nvd.nist.gov/vuln/detail/CVE-2026-103232) | Medium | 5.5 | A weakness has been identified in AdithyaYelloju Restaurant-Management-System up to 7f0e7e84255e8fcfd488e83f8f91451bbbf… |
| 2026-09-30 17:16:43 | [CVE-2026-103443](https://nvd.nist.gov/vuln/detail/CVE-2026-103443) | Low | 1.1 | Improper neutralization of Script-Related HTML tags in a web page (basic XSS) vulnerability in The Wikimedia Foundation… |
| 2026-09-30 17:16:43 | [CVE-2026-103444](https://nvd.nist.gov/vuln/detail/CVE-2026-103444) | Low | 1.1 | Improper neutralization of Script-Related HTML tags in a web page (basic XSS) vulnerability in The Wikimedia Foundation… |
| 2026-09-30 17:16:45 | [CVE-2026-19445](https://nvd.nist.gov/vuln/detail/CVE-2026-19445) | Critical | 9.2 | A remote, unauthenticated TLS client can make a server crash or call through a freed pointer if its sni_callback assign… |
| 2026-09-30 17:16:45 | [CVE-2026-19553](https://nvd.nist.gov/vuln/detail/CVE-2026-19553) | High | 7.6 | ssl.SSLContext.wrap_bio() didn't require the server_hostname argument to not be None if ssl.SSLContext.check_hostname w… |
| 2026-09-30 17:16:46 | [CVE-2026-46711](https://nvd.nist.gov/vuln/detail/CVE-2026-46711) | High | 8.3 | Soft Machine is a Virtual Machine–based agentic development environment / Cloud OS. In versions 0.2.247 and prior, the… |
| 2026-09-30 17:16:46 | [CVE-2026-55176](https://nvd.nist.gov/vuln/detail/CVE-2026-55176) | Critical | 9.0 | Soft Machine is a Virtual Machine–based agentic development environment / Cloud OS. In versions 0.2.247 and prior, two… |
| 2026-09-30 17:16:46 | [CVE-2026-55177](https://nvd.nist.gov/vuln/detail/CVE-2026-55177) | High | 7.6 | CloudTAK is a browser-based Common Operating Picture and situational awareness tool compatible with TAK. Prior to versi… |
| 2026-09-30 17:16:46 | [CVE-2026-55181](https://nvd.nist.gov/vuln/detail/CVE-2026-55181) | Critical | 9.4 | Tugtainer is a self-hosted app for automating updates of Docker containers. Prior to version 1.30.3, Tugtainer's OIDC a… |
| 2026-09-30 17:16:47 | [CVE-2026-55494](https://nvd.nist.gov/vuln/detail/CVE-2026-55494) | Critical | 9.8 | Tugtainer is a self-hosted app for automating updates of Docker containers. Prior to version 1.30.4, Tugtainer Agent al… |
| 2026-09-30 17:16:49 | [CVE-2026-62308](https://nvd.nist.gov/vuln/detail/CVE-2026-62308) | Critical | 9.1 | Tugtainer is a self-hosted app for automating updates of Docker containers. Prior to version 1.30.6, Tugtainer allows a… |
| 2026-09-30 17:16:49 | [CVE-2026-75969](https://nvd.nist.gov/vuln/detail/CVE-2026-75969) | Critical | 9.1 | Missing authentication for critical function vulnerability for all PTZOptics cameras and the Firmware Upgrade Tool - Fi… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
