# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-16 15:19 UTC

New CVEs published between 2026-10-16 14:19 UTC and 2026-10-16 15:19 UTC.

[Full CSV](data/new-cves-2026-10-16T15-19-04-823931Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-10-16 14:19:27 | [CVE-2026-97470](https://nvd.nist.gov/vuln/detail/CVE-2026-97470) | Medium | 6.4 | The Tourfic – AI Powered Travel Booking, Hotel Booking & Car Rental plugin for WordPress is vulnerable to Stored Cross-… |
| 2026-10-16 14:19:36 | [CVE-2026-97858](https://nvd.nist.gov/vuln/detail/CVE-2026-97858) | Medium | 6.9 | An attacker can cause the server to unbind the target device from its current owner and rebind it to the requesting acc… |
| 2026-10-16 15:16:50 | [CVE-2025-52097](https://nvd.nist.gov/vuln/detail/CVE-2025-52097) |  |  | Cross Site Scripting vulnerability in InstantASP ltd, InstantForum.NET v.4.1.4 allows an attacker to execute arbitrary… |
| 2026-10-16 15:16:58 | [CVE-2026-101021](https://nvd.nist.gov/vuln/detail/CVE-2026-101021) | High | 8.7 | MultipartInputStream performs inefficient boundary matching and unnecessary buffer copying. Crafted multipart input can… |
| 2026-10-16 15:17:03 | [CVE-2026-105273](https://nvd.nist.gov/vuln/detail/CVE-2026-105273) | High | 8.7 | MP4Parser does not adequately validate MP4 box sizes. A malformed box can cause parsing to make no forward progress and… |
| 2026-10-16 15:17:04 | [CVE-2026-105279](https://nvd.nist.gov/vuln/detail/CVE-2026-105279) | Critical | 9.3 | In the default configuration, the archive accepts DICOM associations from an unregistered calling AE. A remote peer can… |
| 2026-10-16 15:17:04 | [CVE-2026-105667](https://nvd.nist.gov/vuln/detail/CVE-2026-105667) | High | 8.7 | In the default configuration, the HL7 listener accepts ADT^A40 patient-merge messages without authenticating the sendin… |
| 2026-10-16 15:17:04 | [CVE-2026-106705](https://nvd.nist.gov/vuln/detail/CVE-2026-106705) | High | 8.8 | ELADMIN (eladmin-mp) up to 2.7 contains an improper access control vulnerability in the role management module. The end… |
| 2026-10-16 15:17:05 | [CVE-2026-107621](https://nvd.nist.gov/vuln/detail/CVE-2026-107621) | High | 8.7 | JPEGParser can enter an infinite loop while parsing a specially crafted or truncated stream. |
| 2026-10-16 15:17:05 | [CVE-2026-107777](https://nvd.nist.gov/vuln/detail/CVE-2026-107777) | High | 7.1 | Thermo Fisher Torrent Suite Software is vulnerable to a path traversal, which could allow an authenticated attacker to… |
| 2026-10-16 15:17:15 | [CVE-2026-111728](https://nvd.nist.gov/vuln/detail/CVE-2026-111728) | Medium | 5.3 | Seanime v3.7.0 to v3.10.3 contains an argument injection vulnerability reachable through improper authorization, allowi… |
| 2026-10-16 15:17:33 | [CVE-2026-88755](https://nvd.nist.gov/vuln/detail/CVE-2026-88755) |  |  | Z.ai ZCode v3.11.2.6792 was discovered to automatically establish connections with MCP servers declared inside a reposi… |
| 2026-10-16 15:17:36 | [CVE-2026-95182](https://nvd.nist.gov/vuln/detail/CVE-2026-95182) |  |  | An untrusted search path in DeepSeek Harness (dsh) commit c291e796 allows attackers to execute arbitrary code via suppl… |
| 2026-10-16 15:17:37 | [CVE-2026-95183](https://nvd.nist.gov/vuln/detail/CVE-2026-95183) |  |  | An issue in the context-compaction feature of DeepSeek Harness (dsh) commit c291e796 allows attackers to execute a prom… |
| 2026-10-16 15:17:38 | [CVE-2026-97851](https://nvd.nist.gov/vuln/detail/CVE-2026-97851) | High | 8.8 | The storage status-change REST service allows location records still associated with DICOM instances to be changed to d… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
