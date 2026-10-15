# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-15 03:19 UTC

New CVEs published between 2026-10-15 02:19 UTC and 2026-10-15 03:19 UTC.

[Full CSV](data/new-cves-2026-10-15T03-19-44-093537Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-10-15 02:20:15 | [CVE-2026-73799](https://nvd.nist.gov/vuln/detail/CVE-2026-73799) | High | 7.5 | A security vulnerability in HPE NonStop SNMP Trap Multiplexer may cause memory corruption |
| 2026-10-15 02:20:15 | [CVE-2026-76066](https://nvd.nist.gov/vuln/detail/CVE-2026-76066) | High | 8.7 | IntentKit through 2.6.3 contains an authorization bypass vulnerability where the executor validates tool calls against… |
| 2026-10-15 02:20:15 | [CVE-2026-76656](https://nvd.nist.gov/vuln/detail/CVE-2026-76656) | Medium | 5.3 | A vulnerability in HPE NonStop TCP/IP UTILITIES could allow an unauthenticated remote attacker to cause a denial of ser… |
| 2026-10-15 02:20:15 | [CVE-2026-76659](https://nvd.nist.gov/vuln/detail/CVE-2026-76659) | High | 7.5 | A vulnerability in the finger daemon of HPE NonStop TCP/IP UTILITIES could allow an unauthenticated remote attacker to… |
| 2026-10-15 02:20:16 | [CVE-2026-76660](https://nvd.nist.gov/vuln/detail/CVE-2026-76660) | High | 8.7 | A vulnerability in HPE NonStop CIPSAM allows an out-of-bounds write that can corrupt buffer data. |
| 2026-10-15 02:20:16 | [CVE-2026-76661](https://nvd.nist.gov/vuln/detail/CVE-2026-76661) | High | 7.6 | A vulnerability in HPE NonStop QIOMON allows an out-of-bounds write that can corrupt buffer data. |
| 2026-10-15 02:20:16 | [CVE-2026-77931](https://nvd.nist.gov/vuln/detail/CVE-2026-77931) | High | 8.7 | MoviePilot through 3.1.5 contains a command injection vulnerability that allows attackers to execute arbitrary OS comma… |
| 2026-10-15 03:17:10 | [CVE-2026-110907](https://nvd.nist.gov/vuln/detail/CVE-2026-110907) | High | 7.5 | Backdrop CMS Core 1.35.x before 1.35.2 and 1.34.x before 1.34.6 mishandles tokens. A token is a small placeholder strin… |
| 2026-10-15 03:17:10 | [CVE-2026-110908](https://nvd.nist.gov/vuln/detail/CVE-2026-110908) | High | 8.8 | Netgate pfSense FRR package (pfSense-pkg-frr) 2.0.2_1 and source revision 2.1.2_1 contain an OS command injection vulne… |
| 2026-10-15 03:17:10 | [CVE-2026-110909](https://nvd.nist.gov/vuln/detail/CVE-2026-110909) | Medium | 5.0 | Wheels CLI through 4.1.0 does not verify that the local development server answering its HTTP requests belongs to the c… |
| 2026-10-15 03:17:11 | [CVE-2026-76662](https://nvd.nist.gov/vuln/detail/CVE-2026-76662) | Medium | 5.9 | A buffer overflow vulnerability in HPE NonStop TELSERV can cause memory corruption and DoS. |
| 2026-10-15 03:17:11 | [CVE-2026-76663](https://nvd.nist.gov/vuln/detail/CVE-2026-76663) | High | 7.5 | A stack-based buffer overflow vulnerability in HPE NonStop TELSERV can cause memory corruption that may result in DoS. |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
