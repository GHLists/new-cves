# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-11-25 18:20 UTC

New CVEs published between 2026-11-25 17:20 UTC and 2026-11-25 18:20 UTC.

[Full CSV](data/new-cves-2026-11-25T18-20-05-659753Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-11-25 18:18:45 | [CVE-2026-110470](https://nvd.nist.gov/vuln/detail/CVE-2026-110470) | Low | 2.3 | Stack-based buffer overflow in the mkevent helper in Checkmk <2.5.0p21, <2.4.0p42 and 2.3.0 (EOL) allows an attacker wh… |
| 2026-11-25 18:18:47 | [CVE-2026-123265](https://nvd.nist.gov/vuln/detail/CVE-2026-123265) |  |  | Rejected reason: this CVE was issued in error. |
| 2026-11-25 18:18:49 | [CVE-2026-135135](https://nvd.nist.gov/vuln/detail/CVE-2026-135135) | High | 7.1 | Mongoid builds an incomplete automatic encryption schema for certain embedded document associations. As a result, value… |
| 2026-11-25 18:18:50 | [CVE-2026-135138](https://nvd.nist.gov/vuln/detail/CVE-2026-135138) | Medium | 6.0 | Mongoid does not consistently apply its read-only attribute protection when attribute names are supplied dynamically by… |
| 2026-11-25 18:18:50 | [CVE-2026-135139](https://nvd.nist.gov/vuln/detail/CVE-2026-135139) | Medium | 6.0 | Mongoid contains an incorrect authorization weakness in the handling of caller-supplied filters for bulk removal throug… |
| 2026-11-25 18:18:50 | [CVE-2026-135140](https://nvd.nist.gov/vuln/detail/CVE-2026-135140) | Medium | 5.3 | Mongoid may omit a field from the client-side encryption settings it generates for a collection when that same field is… |
| 2026-11-25 18:18:50 | [CVE-2026-135141](https://nvd.nist.gov/vuln/detail/CVE-2026-135141) | High | 8.6 | A logic flaw in the query-building layer of the Mongoid object-document mapper causes a model-level default restriction… |
| 2026-11-25 18:18:50 | [CVE-2026-135146](https://nvd.nist.gov/vuln/detail/CVE-2026-135146) | Critical | 9.1 | An improper certificate revocation check in the MongoDB Python Driver's optional TLS revocation-checking support allows… |
| 2026-11-25 18:18:50 | [CVE-2026-135225](https://nvd.nist.gov/vuln/detail/CVE-2026-135225) | Medium | 5.7 | An information exposure weakness in the connection string handling of the MongoDB Ruby Driver can place credential mate… |
| 2026-11-25 18:18:50 | [CVE-2026-135226](https://nvd.nist.gov/vuln/detail/CVE-2026-135226) | High | 8.7 | A type-confusion weakness in the Extended JSON parsing component of BSON for Ruby allows a party who can supply parser… |
| 2026-11-25 18:18:51 | [CVE-2026-135227](https://nvd.nist.gov/vuln/detail/CVE-2026-135227) | High | 8.3 | An improper restriction of dynamically determined object attributes in the object-document mapping library's associatio… |
| 2026-11-25 18:18:51 | [CVE-2026-135898](https://nvd.nist.gov/vuln/detail/CVE-2026-135898) | High | 8.8 | An out-of-bounds read in the native C BSON decoding extension of the MongoDB Python Driver may allow an unauthenticated… |
| 2026-11-25 18:18:51 | [CVE-2026-136697](https://nvd.nist.gov/vuln/detail/CVE-2026-136697) | Medium | 5.3 | A flaw has been found in LibrePhotos up to 1.2.1. Affected by this issue is the function write_metadata of the file app… |
| 2026-11-25 18:18:52 | [CVE-2026-136721](https://nvd.nist.gov/vuln/detail/CVE-2026-136721) | Low | 2.1 | A vulnerability was determined in coleifer peewee up to 4.5.3. This affects the function _print_table of the file pwiz.… |
| 2026-11-25 18:18:52 | [CVE-2026-136722](https://nvd.nist.gov/vuln/detail/CVE-2026-136722) | Medium | 5.5 | A vulnerability was identified in Zhengzhou Weiwei Information Technology mayicms up to 5.8E. This vulnerability affect… |
| 2026-11-25 18:18:55 | [CVE-2026-81405](https://nvd.nist.gov/vuln/detail/CVE-2026-81405) | High | 7.1 | Nmap before 7.992 contains an uncontrolled resource consumption vulnerability in the Comm.ReceivePacket function of the… |
| 2026-11-25 18:18:55 | [CVE-2026-81406](https://nvd.nist.gov/vuln/detail/CVE-2026-81406) | High | 7.1 | Nmap before 7.992 contains an uncontrolled resource consumption vulnerability in the read_db2_packet function of the db… |
| 2026-11-25 18:18:55 | [CVE-2026-81407](https://nvd.nist.gov/vuln/detail/CVE-2026-81407) | Medium | 6.0 | Nmap before 7.992 contains a hardcoded cryptographic key vulnerability in the DHCAST128 login of the NSE afp.lua librar… |
| 2026-11-25 18:18:55 | [CVE-2026-81408](https://nvd.nist.gov/vuln/detail/CVE-2026-81408) | High | 7.1 | Nmap before 7.992 contains a loop with an unreachable exit condition in the parameter-list parsing of the NSE drda.lua… |
| 2026-11-25 18:18:55 | [CVE-2026-81409](https://nvd.nist.gov/vuln/detail/CVE-2026-81409) | Medium | 5.3 | Nmap before 7.992 contains a server-side request forgery vulnerability in the http-cisco-anyconnect.nse script and the… |
| 2026-11-25 18:18:55 | [CVE-2026-81410](https://nvd.nist.gov/vuln/detail/CVE-2026-81410) | Low | 2.1 | Nmap before 7.992 contains a server-side request forgery vulnerability in the broadcast-upnp-info.nse script and the up… |
| 2026-11-25 18:18:55 | [CVE-2026-81411](https://nvd.nist.gov/vuln/detail/CVE-2026-81411) | High | 7.1 | Nmap before 7.992 contains an infinite loop vulnerability in the ConfCreateResponse GCC block parser of the NSE rdp.lua… |
| 2026-11-25 18:18:56 | [CVE-2026-81412](https://nvd.nist.gov/vuln/detail/CVE-2026-81412) | High | 7.1 | Nmap before 7.992 contains an excessive memory allocation vulnerability in the unmarshall_array function of the NSE msr… |
| 2026-11-25 18:18:56 | [CVE-2026-81413](https://nvd.nist.gov/vuln/detail/CVE-2026-81413) | Medium | 6.0 | Nmap before 7.992 contains an uncontrolled resource consumption vulnerability in the inline AXFR response reader of the… |
| 2026-11-25 18:18:56 | [CVE-2026-81414](https://nvd.nist.gov/vuln/detail/CVE-2026-81414) | Medium | 6.0 | Nmap before 7.992 contains an uncontrolled resource consumption vulnerability in the sendPacketsTCP function of the NSE… |
| 2026-11-25 18:18:56 | [CVE-2026-81415](https://nvd.nist.gov/vuln/detail/CVE-2026-81415) | Medium | 6.0 | Nmap before 7.992 contains an infinite loop vulnerability in the negotiate_tn3270 function of the NSE tn3270.lua librar… |
| 2026-11-25 18:18:56 | [CVE-2026-81416](https://nvd.nist.gov/vuln/detail/CVE-2026-81416) | Medium | 6.0 | Nmap before 7.992 contains an infinite loop vulnerability in the process_write function of the NSE tn3270.lua library,… |
| 2026-11-25 18:18:56 | [CVE-2026-81417](https://nvd.nist.gov/vuln/detail/CVE-2026-81417) | Medium | 6.0 | Nmap before 7.992 contains an infinite loop vulnerability in the dispatcher of the NSE tftp.lua library, which removes… |
| 2026-11-25 18:18:57 | [CVE-2026-81418](https://nvd.nist.gov/vuln/detail/CVE-2026-81418) | Medium | 5.9 | Nmap before 7.992 contains an uncontrolled resource consumption vulnerability in the TLV.AUTH parser of the NSE eigrp.l… |
| 2026-11-25 18:18:57 | [CVE-2026-81419](https://nvd.nist.gov/vuln/detail/CVE-2026-81419) | Medium | 5.9 | Nmap before 7.992 contains an infinite loop vulnerability in the LSUpdate.parse function of the NSE ospf.lua library, w… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
