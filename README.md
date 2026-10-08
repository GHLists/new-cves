# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-08 12:18 UTC

New CVEs published between 2026-10-08 11:19 UTC and 2026-10-08 12:18 UTC.

[Full CSV](data/new-cves-2026-10-08T12-18-37-337721Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-10-08 12:17:14 | [CVE-2026-107275](https://nvd.nist.gov/vuln/detail/CVE-2026-107275) | Medium | 6.8 | @fastify/jwt is a JSON Web Token plugin for the Fastify web framework. In versions before 10.2.3, a time span passed to… |
| 2026-10-08 12:17:14 | [CVE-2026-107570](https://nvd.nist.gov/vuln/detail/CVE-2026-107570) | Low | 2.5 | heap OOB write in convert_file_from_to() via a crafted Content-Type header allows attacker to OOB write when email is u… |
| 2026-10-08 12:17:14 | [CVE-2026-107572](https://nvd.nist.gov/vuln/detail/CVE-2026-107572) | Medium | 6.5 | Inefficient complexity in the Sieve filter evaluation of Progressive Robot hMailServer 6.2.24 through 6.3.5 allows an a… |
| 2026-10-08 12:17:15 | [CVE-2026-107573](https://nvd.nist.gov/vuln/detail/CVE-2026-107573) | High | 7.8 | Incorrect default permissions in the Windows installer of Progressive Robot hMailServer 6.0.0 through 6.3.5 allow a loc… |
| 2026-10-08 12:17:15 | [CVE-2026-107574](https://nvd.nist.gov/vuln/detail/CVE-2026-107574) | High | 7.5 | Inefficient algorithmic complexity in the JSON reader of Progressive Robot hMailServer allows a remote unauthenticated… |
| 2026-10-08 12:17:15 | [CVE-2026-107575](https://nvd.nist.gov/vuln/detail/CVE-2026-107575) | Medium | 5.3 | Inefficient algorithmic complexity in the SPF macro expansion of Progressive Robot hMailServer 6.3.4 and 6.3.5 allows a… |
| 2026-10-08 12:17:15 | [CVE-2026-107576](https://nvd.nist.gov/vuln/detail/CVE-2026-107576) | High | 7.5 | Inefficient algorithmic complexity in the inbound DKIM and ARC signature verification of Progressive Robot hMailServer… |
| 2026-10-08 12:17:15 | [CVE-2026-107577](https://nvd.nist.gov/vuln/detail/CVE-2026-107577) | High | 7.5 | Inefficient algorithmic complexity and a non-terminating loop in the MIME processing of received messages in Progressiv… |
| 2026-10-08 12:17:15 | [CVE-2026-107578](https://nvd.nist.gov/vuln/detail/CVE-2026-107578) | Medium | 6.7 | Improper link resolution and external control of file paths in the administrative command-line operations of hMailServe… |
| 2026-10-08 12:17:15 | [CVE-2026-107579](https://nvd.nist.gov/vuln/detail/CVE-2026-107579) | High | 7.5 | Inefficient algorithmic complexity in the bounce and complaint processing of Progressive Robot hMailServer 6.3.4 and 6.… |
| 2026-10-08 12:17:16 | [CVE-2026-107580](https://nvd.nist.gov/vuln/detail/CVE-2026-107580) | Medium | 6.5 | Inefficient algorithmic complexity in the decoding of message header fields in Progressive Robot hMailServer 6.0.0 thro… |
| 2026-10-08 12:17:16 | [CVE-2026-107581](https://nvd.nist.gov/vuln/detail/CVE-2026-107581) | Medium | 6.5 | Progressive Robot hMailServer 6.0.0 through 6.3.5 processes several IMAP commands from a signed-in account in time quad… |
| 2026-10-08 12:17:16 | [CVE-2026-107582](https://nvd.nist.gov/vuln/detail/CVE-2026-107582) | Medium | 6.5 | Inefficient algorithmic complexity in the REST API (6.3.3 through 6.3.5) and the IMAP PREVIEW response (6.2.22 through… |
| 2026-10-08 12:17:16 | [CVE-2026-107583](https://nvd.nist.gov/vuln/detail/CVE-2026-107583) | Medium | 6.5 | Inefficient algorithmic complexity in the webmail's message view of the REST API in Progressive Robot hMailServer 6.3.2… |
| 2026-10-08 12:17:16 | [CVE-2026-107584](https://nvd.nist.gov/vuln/detail/CVE-2026-107584) | High | 7.4 | Progressive Robot hMailServer 6.0.0 through 6.3.5 fails open when applying DANE (RFC 7672) to outbound SMTP delivery. T… |
| 2026-10-08 12:17:16 | [CVE-2026-107587](https://nvd.nist.gov/vuln/detail/CVE-2026-107587) | Medium | 5.9 | Improper certificate validation in the webmail of Progressive Robot hMailServer 6.3.2 through 6.3.5 allows a remote una… |
| 2026-10-08 12:17:17 | [CVE-2026-19083](https://nvd.nist.gov/vuln/detail/CVE-2026-19083) | High | 8.8 | Authorization bypass through User-Controlled key vulnerability in AKIN Software Computer Import-Export Industry and Tra… |
| 2026-10-08 12:17:18 | [CVE-2026-92555](https://nvd.nist.gov/vuln/detail/CVE-2026-92555) | Critical | 9.1 | Insertion of sensitive information into sent data vulnerability in AKIN Software Computer Import-Export Industry and Tr… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
