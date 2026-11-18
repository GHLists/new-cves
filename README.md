# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-11-18 15:19 UTC

New CVEs published between 2026-11-18 14:20 UTC and 2026-11-18 15:19 UTC.

[Full CSV](data/new-cves-2026-11-18T15-19-03-832968Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-11-18 15:17:31 | [CVE-2026-107511](https://nvd.nist.gov/vuln/detail/CVE-2026-107511) | Medium | 4.8 | Dell PowerStore contains a CSV Injection vulnerability. A high-privileged attacker could exploit this vulnerability, po… |
| 2026-11-18 15:17:32 | [CVE-2026-109908](https://nvd.nist.gov/vuln/detail/CVE-2026-109908) | High | 7.8 | A heap buffer overflow in reading encoding files in X.Org libfontenc before 1.11.0 could be used by local attackers abl… |
| 2026-11-18 15:17:32 | [CVE-2026-111507](https://nvd.nist.gov/vuln/detail/CVE-2026-111507) | High | 8.1 | Dell PowerStore contains an authorization bypass vulnerability. A remote attacker could exploit this vulnerability to a… |
| 2026-11-18 15:17:32 | [CVE-2026-116446](https://nvd.nist.gov/vuln/detail/CVE-2026-116446) | Critical | 9.8 | Dell PowerStore SDNAS contains an out-of-bounds memory vulnerability in the NAS NFS service that an unauthenticated rem… |
| 2026-11-18 15:17:32 | [CVE-2026-116447](https://nvd.nist.gov/vuln/detail/CVE-2026-116447) | High | 8.8 | Dell PowerStore SDNAS contains a local privilege-escalation vulnerability that could allow a low-privileged attacker to… |
| 2026-11-18 15:17:33 | [CVE-2026-116448](https://nvd.nist.gov/vuln/detail/CVE-2026-116448) | Critical | 9.8 | Dell PowerStore SDNAS contains an OS Command Injection vulnerability that could allow an attacker with internal network… |
| 2026-11-18 15:17:35 | [CVE-2026-128717](https://nvd.nist.gov/vuln/detail/CVE-2026-128717) |  |  | An issue in PHPGurukul Employee Leaves Management System (ELMS) Version 2.1 allows a remote attacker to escalate privil… |
| 2026-11-18 15:17:41 | [CVE-2026-131653](https://nvd.nist.gov/vuln/detail/CVE-2026-131653) | Medium | 4.3 | Tanium addressed an improper input validation vulnerability in Discover. |
| 2026-11-18 15:17:41 | [CVE-2026-131801](https://nvd.nist.gov/vuln/detail/CVE-2026-131801) | High | 7.7 | Tanium addressed an improper input validation vulnerability in Threat Response. |
| 2026-11-18 15:17:41 | [CVE-2026-132038](https://nvd.nist.gov/vuln/detail/CVE-2026-132038) | High | 7.8 | Rapid7 Metasploit Framework versions prior to 6.5.10 suffer from an Improper Access Control issue in the msfdb database… |
| 2026-11-18 15:17:41 | [CVE-2026-132150](https://nvd.nist.gov/vuln/detail/CVE-2026-132150) | High | 7.8 | A flaw was found in the file-xmc plugin in GIMP. When processing a specially crafted XMC image file, the plugin does no… |
| 2026-11-18 15:17:42 | [CVE-2026-15263](https://nvd.nist.gov/vuln/detail/CVE-2026-15263) | High | 7.1 | A server-side request forgery (SSRF) vulnerability in the Pure Storage FlashArray extension for Windows Admin Center ve… |
| 2026-11-18 15:17:42 | [CVE-2026-3232](https://nvd.nist.gov/vuln/detail/CVE-2026-3232) | High | 7.2 | The Easy Appointments plugin for WordPress is vulnerable to Stored Cross-Site Scripting via the 'name' and 'phone' fiel… |
| 2026-11-18 15:17:43 | [CVE-2026-82171](https://nvd.nist.gov/vuln/detail/CVE-2026-82171) | High | 8.0 | Dell PowerStore contains an XML External Entity (XXE) Injection vulnerability. A high-privileged attacker could exploit… |
| 2026-11-18 15:17:43 | [CVE-2026-86866](https://nvd.nist.gov/vuln/detail/CVE-2026-86866) | Medium | 6.5 | Tanium addressed a SQL injection vulnerability in multiple products. |
| 2026-11-18 15:17:44 | [CVE-2026-95791](https://nvd.nist.gov/vuln/detail/CVE-2026-95791) | Medium | 4.9 | A vulnerability in the web management and file transfer component of AOS web could allow an authenticated remote attack… |
| 2026-11-18 15:17:44 | [CVE-2026-95823](https://nvd.nist.gov/vuln/detail/CVE-2026-95823) | High | 7.5 | tcp_pkt_linearize() in subsys/net/ip/tcp.c is used by th_get() whenever a received TCP header is not contiguous in a si… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
