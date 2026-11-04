# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-11-04 12:20 UTC

New CVEs published between 2026-11-04 10:21 UTC and 2026-11-04 12:20 UTC.

[Full CSV](data/new-cves-2026-11-04T12-20-25-696029Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-11-04 11:17:04 | [CVE-2026-100235](https://nvd.nist.gov/vuln/detail/CVE-2026-100235) | Medium | 6.0 | Incorrect authorization due to a time-of-check to time-of-use (TOCTOU) race condition in the setACL request handling of… |
| 2026-11-04 11:17:06 | [CVE-2026-100252](https://nvd.nist.gov/vuln/detail/CVE-2026-100252) | High | 8.6 | Improper Authorization vulnerability in Apache ZooKeeper. When SASL authentication is enabled on the client port, the s… |
| 2026-11-04 11:17:06 | [CVE-2026-100300](https://nvd.nist.gov/vuln/detail/CVE-2026-100300) | High | 8.7 | Improper handling of exceptional conditions in the quota subsystem of Apache ZooKeeper allows an attacker able to write… |
| 2026-11-04 11:17:07 | [CVE-2026-100302](https://nvd.nist.gov/vuln/detail/CVE-2026-100302) | High | 7.1 | Allocation of Resources Without Limits or Throttling in the multiRead request handler of Apache ZooKeeper allows a remo… |
| 2026-11-04 11:17:07 | [CVE-2026-102703](https://nvd.nist.gov/vuln/detail/CVE-2026-102703) |  |  | [This CNA information record relates to multiple CVEs; the text explains which aspects/vulnerabilities correspond to wh… |
| 2026-11-04 11:17:07 | [CVE-2026-102704](https://nvd.nist.gov/vuln/detail/CVE-2026-102704) |  |  | [This CNA information record relates to multiple CVEs; the text explains which aspects/vulnerabilities correspond to wh… |
| 2026-11-04 11:17:13 | [CVE-2026-103582](https://nvd.nist.gov/vuln/detail/CVE-2026-103582) |  |  | Unbounded memory allocation and missing frame size validation in Apache NMS ActiveMQ (the .NET OpenWire client, package… |
| 2026-11-04 11:17:13 | [CVE-2026-108500](https://nvd.nist.gov/vuln/detail/CVE-2026-108500) |  |  | Input validation vulnerability in Apache ActiveMQ configured to use the LDAPAuthorizationMapPlugin allows an authentica… |
| 2026-11-04 11:17:13 | [CVE-2026-108946](https://nvd.nist.gov/vuln/detail/CVE-2026-108946) |  |  | Improper input validation vulnerability in Apache ActiveMQ, Apache ActiveMQ KahaDB. The ActiveMQ broker resolves connec… |
| 2026-11-04 11:17:14 | [CVE-2026-115448](https://nvd.nist.gov/vuln/detail/CVE-2026-115448) | High | 8.7 | Uncontrolled recursion in Apache ZooKeeper. The server serializes its data tree to a snapshot by recursing one stack fr… |
| 2026-11-04 11:17:16 | [CVE-2026-59263](https://nvd.nist.gov/vuln/detail/CVE-2026-59263) | Low | 1.9 | A manipulated document opened in Apache OpenOffice 4.1.16 or earlier may allow substituted content to be displayed mani… |
| 2026-11-04 11:17:16 | [CVE-2026-59264](https://nvd.nist.gov/vuln/detail/CVE-2026-59264) |  |  | The Windows installers of Apache OpenOffice 4.1.16 and earlier allow an already manipulated system to run external code… |
| 2026-11-04 11:17:16 | [CVE-2026-59268](https://nvd.nist.gov/vuln/detail/CVE-2026-59268) |  |  | An out-of-bounds Write vulnerability in Apache OpenOffice versions through 4.1.16 could allow an attacker to craft a Mi… |
| 2026-11-04 11:17:18 | [CVE-2026-90624](https://nvd.nist.gov/vuln/detail/CVE-2026-90624) |  |  | An unchecked memory access in the PDF import code of Apache OpenOffice versions through 4.1.16 on allows a crafted PDF… |
| 2026-11-04 11:17:19 | [CVE-2026-90626](https://nvd.nist.gov/vuln/detail/CVE-2026-90626) |  |  | An uncontrolled memory access in the PDF import code of Apache OpenOffice versions through 4.1.16 allows a crafted PDF… |
| 2026-11-04 11:17:19 | [CVE-2026-90627](https://nvd.nist.gov/vuln/detail/CVE-2026-90627) |  |  | The flat file database driver in Apache Openoffice versions through 4.1.16 allows a crafted document to read the conten… |
| 2026-11-04 11:17:19 | [CVE-2026-90628](https://nvd.nist.gov/vuln/detail/CVE-2026-90628) |  |  | An uncontrolled memory access in the PDF export code of Apache OpenOffice versions through 4.1.16 allows a crafted CFF… |
| 2026-11-04 11:17:19 | [CVE-2026-90629](https://nvd.nist.gov/vuln/detail/CVE-2026-90629) |  |  | An uncontrolled memory access in the WMF import code of Apache OpenOffice versions through 4.1.16 allows a crafted WMF… |
| 2026-11-04 11:17:19 | [CVE-2026-90631](https://nvd.nist.gov/vuln/detail/CVE-2026-90631) |  |  | Apache OpenOffice documents can contain links. A missing Authorization vulnerability in Apache OpenOffice allowed an at… |
| 2026-11-04 11:17:19 | [CVE-2026-90632](https://nvd.nist.gov/vuln/detail/CVE-2026-90632) |  |  | Apache OpenOffice documents can include multimedia content (audio, video, etc.) A crafted document could exploit the GS… |
| 2026-11-04 11:17:19 | [CVE-2026-90634](https://nvd.nist.gov/vuln/detail/CVE-2026-90634) |  |  | An uncontrolled memory access in the PDF import code of Apache OpenOffice versions through 4.1.16 allows a crafted PDF… |
| 2026-11-04 12:17:05 | [CVE-2026-104799](https://nvd.nist.gov/vuln/detail/CVE-2026-104799) | High | 8.8 | The Mobile builder plugin for WordPress is vulnerable to Privilege Escalation in all versions up to, and including, 1.4… |
| 2026-11-04 12:17:06 | [CVE-2026-114456](https://nvd.nist.gov/vuln/detail/CVE-2026-114456) | Medium | 6.5 | Multiple Snowflake client drivers implementing the `authenticator=externalbrowser` single sign-on flow could have allow… |
| 2026-11-04 12:17:06 | [CVE-2026-121925](https://nvd.nist.gov/vuln/detail/CVE-2026-121925) | Medium | 6.6 | A stack-based buffer overflow in libsnowflakeclient and the Snowflake PHP PDO Driver could, under specific conditions,… |
| 2026-11-04 12:17:06 | [CVE-2026-59267](https://nvd.nist.gov/vuln/detail/CVE-2026-59267) | Medium | 5.8 | A crafted DXF document causes a heap buffer overflow in Draw in Apache OpenOffice 4.1.16 and earlier. This could cause… |
| 2026-11-04 12:17:07 | [CVE-2026-97397](https://nvd.nist.gov/vuln/detail/CVE-2026-97397) | High | 7.2 | The Remove Google Fonts – Disable, Block, or Replace with Bunny Fonts for GDPR Compliance plugin for WordPress is vulne… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
