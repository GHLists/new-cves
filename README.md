# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-11-22 15:18 UTC

New CVEs published between 2026-11-22 14:21 UTC and 2026-11-22 15:18 UTC.

[Full CSV](data/new-cves-2026-11-22T15-18-23-195378Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-11-22 15:17:11 | [CVE-2026-129083](https://nvd.nist.gov/vuln/detail/CVE-2026-129083) | High | 7.1 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in WPKoi WordPress T… |
| 2026-11-22 15:17:12 | [CVE-2026-129085](https://nvd.nist.gov/vuln/detail/CVE-2026-129085) | High | 7.5 | Missing Authorization vulnerability in Aguila Technologies WP Customer Area customer-area allows Exploiting Incorrectly… |
| 2026-11-22 15:17:12 | [CVE-2026-131754](https://nvd.nist.gov/vuln/detail/CVE-2026-131754) | Critical | 9.8 | Deserialization of Untrusted Data vulnerability in Pierre Lannoy APCu Manager apcu-manager allows Object Injection.This… |
| 2026-11-22 15:17:12 | [CVE-2026-131775](https://nvd.nist.gov/vuln/detail/CVE-2026-131775) | High | 7.1 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in nK Ghost Kit ghos… |
| 2026-11-22 15:17:12 | [CVE-2026-131782](https://nvd.nist.gov/vuln/detail/CVE-2026-131782) | Critical | 9.8 | Deserialization of Untrusted Data vulnerability in mra13 / Team Tips and Tricks HQ Simple Shopping Cart wordpress-simpl… |
| 2026-11-22 15:17:12 | [CVE-2026-134748](https://nvd.nist.gov/vuln/detail/CVE-2026-134748) | Medium | 6.9 | Members WordPress plugin by MemberPress 3.2.28 before 3.3.2 contains an authentication bypass vulnerability that allows… |
| 2026-11-22 15:17:12 | [CVE-2026-134749](https://nvd.nist.gov/vuln/detail/CVE-2026-134749) | High | 7.1 | MemberPress Members before 3.3.1, with the Block Permissions add-on enabled, contains a denial of service vulnerability… |
| 2026-11-22 15:17:13 | [CVE-2026-134750](https://nvd.nist.gov/vuln/detail/CVE-2026-134750) | Medium | 6.9 | Members WordPress plugin before 3.3.1 contains a missing authorization vulnerability that allows unauthenticated visito… |
| 2026-11-22 15:17:13 | [CVE-2026-134751](https://nvd.nist.gov/vuln/detail/CVE-2026-134751) | Medium | 6.9 | Members WordPress plugin before 3.3.1 contains a missing authorization vulnerability that allows unauthenticated visito… |
| 2026-11-22 15:17:13 | [CVE-2026-134752](https://nvd.nist.gov/vuln/detail/CVE-2026-134752) | Medium | 5.3 | WPGSI: Spreadsheet Integration before 3.8.5 contains a cross-site request forgery vulnerability that allows unauthentic… |
| 2026-11-22 15:17:13 | [CVE-2026-134753](https://nvd.nist.gov/vuln/detail/CVE-2026-134753) | High | 8.3 | dsniff through 2.5a2 contains an integer underflow in decode_sniffer() in decode_sniffer.c that allows unauthenticated… |
| 2026-11-22 15:17:13 | [CVE-2026-134754](https://nvd.nist.gov/vuln/detail/CVE-2026-134754) | High | 7.1 | anacrolix/torrent before 1.62.0 contains an uncontrolled recursion vulnerability in Decoder.readOneValue in bencode/dec… |
| 2026-11-22 15:17:13 | [CVE-2026-134755](https://nvd.nist.gov/vuln/detail/CVE-2026-134755) | Medium | 6.0 | better-chatbot before 2.0.0 contains a missing authorization vulnerability that lets built-in tools run without user co… |
| 2026-11-22 15:17:13 | [CVE-2026-134756](https://nvd.nist.gov/vuln/detail/CVE-2026-134756) | Medium | 5.3 | Portainer Community Edition and Business Edition 2.39.0 before 2.45.1 contain a server-side request forgery vulnerabili… |
| 2026-11-22 15:17:14 | [CVE-2026-134757](https://nvd.nist.gov/vuln/detail/CVE-2026-134757) | Medium | 6.3 | Anacrolix torrent before 1.63.0 contains an improper certificate validation vulnerability in NewClient within tracker/h… |
| 2026-11-22 15:17:14 | [CVE-2026-134758](https://nvd.nist.gov/vuln/detail/CVE-2026-134758) | Low | 2.3 | Wfuzz through 3.1.1 contains a stored cross-site scripting vulnerability that allows malicious target servers to inject… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
