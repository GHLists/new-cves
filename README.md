# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-08 03:20 UTC

New CVEs published between 2026-10-08 02:22 UTC and 2026-10-08 03:20 UTC.

[Full CSV](data/new-cves-2026-10-08T03-20-07-445166Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-10-08 03:16:32 | [CVE-2017-20283](https://nvd.nist.gov/vuln/detail/CVE-2017-20283) | Medium | 6.5 | NXP MQX Classic before 5.0 contains an out-of-bounds write vulnerability in the RTCS UDP recvfrom() implementation. Imp… |
| 2026-10-08 03:16:35 | [CVE-2026-87659](https://nvd.nist.gov/vuln/detail/CVE-2026-87659) | High | 7.1 | A critical authorization bypass vulnerability exists in the Management Server handling of Brocade Fabric OS versions be… |
| 2026-10-08 03:16:35 | [CVE-2026-87665](https://nvd.nist.gov/vuln/detail/CVE-2026-87665) | Medium | 6.0 | A stack-based buffer overflow vulnerability exists in the Internet Key Exchange (IKEv2) protocol handler on Brocade Fab… |
| 2026-10-08 03:16:36 | [CVE-2026-87668](https://nvd.nist.gov/vuln/detail/CVE-2026-87668) | Medium | 6.9 | A stack-based buffer overflow vulnerability exists in the diagnostic execution utility of Brocade Fabric OS versions be… |
| 2026-10-08 03:16:36 | [CVE-2026-87669](https://nvd.nist.gov/vuln/detail/CVE-2026-87669) | Medium | 5.1 | A missing authorization check in Brocade Fabric OS versions before 10.0.1 REST API interface of affected platform relea… |
| 2026-10-08 03:16:36 | [CVE-2026-87670](https://nvd.nist.gov/vuln/detail/CVE-2026-87670) | Medium | 5.1 | An authorization logic vulnerability exists in the Brocade Fabric OS versions before 10.0.1 REST API gateway. The inter… |
| 2026-10-08 03:16:36 | [CVE-2026-87671](https://nvd.nist.gov/vuln/detail/CVE-2026-87671) | High | 7.1 | An out-of-bounds memory read vulnerability exists in the web management daemon of Brocade Fabric OS versions before 10.… |
| 2026-10-08 03:16:36 | [CVE-2026-87672](https://nvd.nist.gov/vuln/detail/CVE-2026-87672) | Medium | 6.8 | An information disclosure vulnerability exists in the SupportLink diagnostic collection utilities of Brocade Fabric OS… |
| 2026-10-08 03:16:36 | [CVE-2026-87676](https://nvd.nist.gov/vuln/detail/CVE-2026-87676) | Medium | 6.9 | A stack-based buffer overflow vulnerability exists in the security library component of Brocade Fabric OS versions befo… |
| 2026-10-08 03:16:37 | [CVE-2026-87678](https://nvd.nist.gov/vuln/detail/CVE-2026-87678) | Medium | 6.9 | An input validation and output encoding vulnerability exists in the web management interface of Brocade Fabric OS versi… |
| 2026-10-08 03:16:37 | [CVE-2026-87684](https://nvd.nist.gov/vuln/detail/CVE-2026-87684) | High | 8.7 | A stack-based buffer overflow vulnerability exists in the SNMP daemon request handling of Brocade Fabric versions befor… |
| 2026-10-08 03:16:37 | [CVE-2026-87686](https://nvd.nist.gov/vuln/detail/CVE-2026-87686) | Medium | 5.3 | An authentication and access control bypass vulnerability exists in the web server management interface of Brocade Fabr… |
| 2026-10-08 03:16:37 | [CVE-2026-92861](https://nvd.nist.gov/vuln/detail/CVE-2026-92861) | Medium | 5.1 | The Android application "Ticket Ryutsu Center" contains hard-coded credentials, which may allow an attacker to obtain a… |
| 2026-10-08 03:16:37 | [CVE-2026-92862](https://nvd.nist.gov/vuln/detail/CVE-2026-92862) | Medium | 4.6 | The Android application "Ticket Ryutsu Center" improperly handles custom URL schemes, allowing a malicious application… |
| 2026-10-08 03:16:37 | [CVE-2026-94578](https://nvd.nist.gov/vuln/detail/CVE-2026-94578) | High | 7.5 | Brocade Fabric OS versions before 10.0.1 contain an authorization logic vulnerability in the AAA (Authentication, Autho… |
| 2026-10-08 03:16:37 | [CVE-2026-94582](https://nvd.nist.gov/vuln/detail/CVE-2026-94582) | Medium | 6.8 | A memory buffer overflow vulnerability exists in the internal diagnostic and route validation routines used by the Fabr… |
| 2026-10-08 03:16:38 | [CVE-2026-94583](https://nvd.nist.gov/vuln/detail/CVE-2026-94583) | Low | 2.1 | A race condition vulnerability exists in the request processing logic of the REST management interface on Brocade Fabri… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
