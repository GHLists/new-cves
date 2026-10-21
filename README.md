# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-21 16:20 UTC

New CVEs published between 2026-10-21 15:18 UTC and 2026-10-21 16:20 UTC.

[Full CSV](data/new-cves-2026-10-21T16-20-02-664892Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-10-21 16:17:13 | [CVE-2025-60469](https://nvd.nist.gov/vuln/detail/CVE-2025-60469) |  |  | A NULL pointer dereference in the gf_ac4_presentation_ch_mode function (/media_tools/av_parsers.c) of GPAC Project/MP4B… |
| 2026-10-21 16:17:13 | [CVE-2025-60476](https://nvd.nist.gov/vuln/detail/CVE-2025-60476) |  |  | A heap use-after-free in the gf_odf_ac4_cfg_clean_list function (/odf/descriptors.c) of GPAC Project/MP4Box before 2.5… |
| 2026-10-21 16:17:13 | [CVE-2026-102483](https://nvd.nist.gov/vuln/detail/CVE-2026-102483) | High | 7.5 | Reachable exit in NTPsec ntpd 1.1.4 through 1.2.5 allows a remote attacker to terminate the daemon via an NTS request w… |
| 2026-10-21 16:17:14 | [CVE-2026-102484](https://nvd.nist.gov/vuln/detail/CVE-2026-102484) | Medium | 6.4 | Heap-based buffer overflow in the JJY refclock driver in NTPsec ntpd before 1.2.6 allows an attacker who controls the T… |
| 2026-10-21 16:17:14 | [CVE-2026-102485](https://nvd.nist.gov/vuln/detail/CVE-2026-102485) | Medium | 5.2 | Out-of-bounds read in the Motorola Oncore refclock driver in NTPsec ntpd before 1.2.6 allows an attacker who controls t… |
| 2026-10-21 16:17:14 | [CVE-2026-102486](https://nvd.nist.gov/vuln/detail/CVE-2026-102486) | High | 7.5 | Out-of-bounds read in NTS extension field parsing in NTPsec ntpd 1.1.4 through 1.2.5 allows a remote attacker to crash… |
| 2026-10-21 16:17:14 | [CVE-2026-102536](https://nvd.nist.gov/vuln/detail/CVE-2026-102536) |  |  | Rejected reason: This CVE has been rejected because it was issued to a development-only issue with no affected distribu… |
| 2026-10-21 16:17:26 | [CVE-2026-113787](https://nvd.nist.gov/vuln/detail/CVE-2026-113787) | Medium | 6.1 | odf-kit allows users to generate, fill, read, and convert OpenDocument Format files (.odt, .ods) in TypeScript and Java… |
| 2026-10-21 16:17:26 | [CVE-2026-113788](https://nvd.nist.gov/vuln/detail/CVE-2026-113788) | Critical | 9.4 | Lagoon is an application delivery platform for Kubernetes. Versions prior to 2.33.1 have a vulnerability in the `ssh` s… |
| 2026-10-21 16:17:26 | [CVE-2026-113789](https://nvd.nist.gov/vuln/detail/CVE-2026-113789) | Medium | 6.0 | pypdf is a free and open-source pure-python PDF library. Prior to 6.21.0, an attacker can craft a PDF that causes large… |
| 2026-10-21 16:17:26 | [CVE-2026-113790](https://nvd.nist.gov/vuln/detail/CVE-2026-113790) | Medium | 6.0 | pypdf is a free and open-source pure-python PDF library. Prior to 6.21.0, an attacker can craft a PDF containing arrays… |
| 2026-10-21 16:17:27 | [CVE-2026-113791](https://nvd.nist.gov/vuln/detail/CVE-2026-113791) | Medium | 6.0 | pypdf is a free and open-source pure-python PDF library. Prior to 6.21.0, an attacker can craft a PDF containing a cont… |
| 2026-10-21 16:17:27 | [CVE-2026-113792](https://nvd.nist.gov/vuln/detail/CVE-2026-113792) | Medium | 6.0 | pypdf is a free and open-source pure-python PDF library. Prior to 6.20.1, calling PdfWriter.find_outline_item on a craf… |
| 2026-10-21 16:17:27 | [CVE-2026-113793](https://nvd.nist.gov/vuln/detail/CVE-2026-113793) | Medium | 6.0 | pypdf is a free and open-source pure-python PDF library. Prior to 6.20.1, removing an object from a crafted cyclic PDF… |
| 2026-10-21 16:17:28 | [CVE-2026-113794](https://nvd.nist.gov/vuln/detail/CVE-2026-113794) | Medium | 6.0 | pypdf is a free and open-source pure-python PDF library. Prior to 6.20.0, an attacker can craft an incomplete PDF that… |
| 2026-10-21 16:17:28 | [CVE-2026-113795](https://nvd.nist.gov/vuln/detail/CVE-2026-113795) | Medium | 6.0 | pypdf is a free and open-source pure-python PDF library. Prior to 6.20.0, accessing a crafted PDF stream with a large n… |
| 2026-10-21 16:17:32 | [CVE-2026-114253](https://nvd.nist.gov/vuln/detail/CVE-2026-114253) | Low | 2.1 | A vulnerability was determined in oretnom23 file-management-system-php up to 2e3c1ebe60f121e8df4fb3f544f0e9591d9a01e4.… |
| 2026-10-21 16:17:32 | [CVE-2026-114254](https://nvd.nist.gov/vuln/detail/CVE-2026-114254) | Medium | 5.5 | A vulnerability was identified in oretnom23 file-management-system-php up to 2e3c1ebe60f121e8df4fb3f544f0e9591d9a01e4.… |
| 2026-10-21 16:17:32 | [CVE-2026-114255](https://nvd.nist.gov/vuln/detail/CVE-2026-114255) | Medium | 5.5 | A security flaw has been discovered in oretnom23 file-management-system-php up to 2e3c1ebe60f121e8df4fb3f544f0e9591d9a0… |
| 2026-10-21 16:17:32 | [CVE-2026-114256](https://nvd.nist.gov/vuln/detail/CVE-2026-114256) | Medium | 5.5 | A weakness has been identified in oretnom23 file-management-system-php up to 2e3c1ebe60f121e8df4fb3f544f0e9591d9a01e4.… |
| 2026-10-21 16:17:33 | [CVE-2026-114370](https://nvd.nist.gov/vuln/detail/CVE-2026-114370) | Low | 3.7 | A flaw was found in the PathResourceManager component of the Undertow web server. This component is responsible for ser… |
| 2026-10-21 16:17:33 | [CVE-2026-114462](https://nvd.nist.gov/vuln/detail/CVE-2026-114462) | Medium | 6.0 | Improper link resolution before file access ('link following') vulnerability in Velneo vServer. This issue affects vSer… |
| 2026-10-21 16:17:33 | [CVE-2026-114257](https://nvd.nist.gov/vuln/detail/CVE-2026-114257) | Medium | 5.5 | A security vulnerability has been detected in oretnom23 file-management-system-php up to 2e3c1ebe60f121e8df4fb3f544f0e9… |
| 2026-10-21 16:17:34 | [CVE-2026-114463](https://nvd.nist.gov/vuln/detail/CVE-2026-114463) |  |  | The webhook platform gateway in Nous Research Hermes Agent versions builds the session chat_id as webhook:{route_name}:… |
| 2026-10-21 16:17:34 | [CVE-2026-114470](https://nvd.nist.gov/vuln/detail/CVE-2026-114470) | Medium | 5.3 | Cross-site request forgery in the REST API of Progressive Robot hMailServer 6.0.0 through 6.3.6 allows a remote attacke… |
| 2026-10-21 16:17:34 | [CVE-2026-114471](https://nvd.nist.gov/vuln/detail/CVE-2026-114471) | Medium | 4.7 | Insertion of sensitive information into a log file in the SMTP server of Progressive Robot hMailServer 6.0.0 through 6.… |
| 2026-10-21 16:17:34 | [CVE-2026-114472](https://nvd.nist.gov/vuln/detail/CVE-2026-114472) | Low | 3.7 | Insufficient resource pool in the ACME HTTP-01 challenge responder of Progressive Robot hMailServer 6.0.0 through 6.3.6… |
| 2026-10-21 16:17:34 | [CVE-2026-114473](https://nvd.nist.gov/vuln/detail/CVE-2026-114473) | Medium | 5.0 | Incorrect authorization in the Sender Rewriting Scheme (SRS) of Progressive Robot hMailServer 6.2.1 through 6.3.6 allow… |
| 2026-10-21 16:17:34 | [CVE-2026-114474](https://nvd.nist.gov/vuln/detail/CVE-2026-114474) | Medium | 5.9 | Use of a less trusted source for the envelope sender in the external-account download of Progressive Robot hMailServer… |
| 2026-10-21 16:17:34 | [CVE-2026-114475](https://nvd.nist.gov/vuln/detail/CVE-2026-114475) | Medium | 6.5 | Missing authorization in the REST role-management routes of Progressive Robot hMailServer 6.3.4 through 6.3.6 allows a… |
| 2026-10-21 16:17:34 | [CVE-2026-114476](https://nvd.nist.gov/vuln/detail/CVE-2026-114476) | High | 7.5 | Incorrect authorization in the REST administration API of Progressive Robot hMailServer 6.3.4 through 6.3.6 allows a re… |
| 2026-10-21 16:17:35 | [CVE-2026-114477](https://nvd.nist.gov/vuln/detail/CVE-2026-114477) | Medium | 4.3 | Missing authorization in the REST metrics route of Progressive Robot hMailServer 6.2.25 through 6.3.6 allows a remote a… |
| 2026-10-21 16:17:35 | [CVE-2026-114478](https://nvd.nist.gov/vuln/detail/CVE-2026-114478) | Medium | 5.9 | Insufficient preservation of the original sender in the forwarding of Progressive Robot hMailServer 6.0.0 through 6.3.6… |
| 2026-10-21 16:17:35 | [CVE-2026-114479](https://nvd.nist.gov/vuln/detail/CVE-2026-114479) | Medium | 5.8 | Not failing securely in the anti-virus attachment-stripping action of Progressive Robot hMailServer 6.0.0 through 6.3.6… |
| 2026-10-21 16:17:35 | [CVE-2026-114489](https://nvd.nist.gov/vuln/detail/CVE-2026-114489) | High | 8.1 | Missing authorization in the REST and COM administration APIs of Progressive Robot hMailServer 6.0.0 through 6.3.6 allo… |
| 2026-10-21 16:17:35 | [CVE-2026-114490](https://nvd.nist.gov/vuln/detail/CVE-2026-114490) | High | 7.8 | Incorrect authorization in the COM administration API of Progressive Robot hMailServer 6.3.4 through 6.3.6 allows an ac… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
