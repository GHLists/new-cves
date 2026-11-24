# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-11-24 12:21 UTC

New CVEs published between 2026-11-24 11:18 UTC and 2026-11-24 12:21 UTC.

[Full CSV](data/new-cves-2026-11-24T12-21-41-563745Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-11-24 12:17:13 | [CVE-2026-103333](https://nvd.nist.gov/vuln/detail/CVE-2026-103333) | High | 7.7 | Improper input validation in some SPARQL functions available in Apache Jena ARQ allows users to submit SPARQL queries t… |
| 2026-11-24 12:17:14 | [CVE-2026-103756](https://nvd.nist.gov/vuln/detail/CVE-2026-103756) | Medium | 5.4 | Improper neutralization of input during web page generation ('cross-site scripting') vulnerability in ITG Bilgisayar Te… |
| 2026-11-24 12:17:15 | [CVE-2026-104813](https://nvd.nist.gov/vuln/detail/CVE-2026-104813) |  |  | Improper limitation of a pathname to a restricted directory ('path traversal') vulnerability in Apache BuildStream allo… |
| 2026-11-24 12:17:16 | [CVE-2026-10765](https://nvd.nist.gov/vuln/detail/CVE-2026-10765) | High | 8.2 | RTU500 contains a denial-of-service vulnerability in its IEC 61850 MMS server implementation. A malicious user with acc… |
| 2026-11-24 12:17:17 | [CVE-2026-111600](https://nvd.nist.gov/vuln/detail/CVE-2026-111600) |  |  | UNIX symbolic link (symlink) following vulnerability in Apache BuildStream allows source plugins to inadvertently read… |
| 2026-11-24 12:17:17 | [CVE-2026-117593](https://nvd.nist.gov/vuln/detail/CVE-2026-117593) | Critical | 9.1 | Weak Password Recovery Mechanism for Forgotten Password vulnerability in ITG Bilgisayar Teknoloji Grubu Tic. Ltd. Şti.… |
| 2026-11-24 12:17:17 | [CVE-2026-119543](https://nvd.nist.gov/vuln/detail/CVE-2026-119543) | High | 8.8 | Authorization bypass through User-Controlled key vulnerability in ITG Bilgisayar Teknoloji Grubu Tic. Ltd. Şti. VSRM al… |
| 2026-11-24 12:17:17 | [CVE-2026-119582](https://nvd.nist.gov/vuln/detail/CVE-2026-119582) | Critical | 9.8 | Improper neutralization of special elements used in an SQL command ('SQL injection') vulnerability in ITG Bilgisayar Te… |
| 2026-11-24 12:17:17 | [CVE-2026-121375](https://nvd.nist.gov/vuln/detail/CVE-2026-121375) | High | 8.6 | Reflected cross-site scripting in the versioned REST API documentation page in Checkmk versions 2.5.0 before 2.5.0p21 a… |
| 2026-11-24 12:17:19 | [CVE-2026-125735](https://nvd.nist.gov/vuln/detail/CVE-2026-125735) | High | 8.6 | SQL injection in the CabinPaq manual code entry module, versions v.1.2.94 and v.1.2.136. The application constructs SQL… |
| 2026-11-24 12:17:19 | [CVE-2026-126605](https://nvd.nist.gov/vuln/detail/CVE-2026-126605) | Medium | 5.3 | Authentication bypass in the Face ID app lock in Proton Pass for iOS before v. 1.21.1 allows an attacker with physical… |
| 2026-11-24 12:17:20 | [CVE-2026-128420](https://nvd.nist.gov/vuln/detail/CVE-2026-128420) | Low | 2.0 | A heap buffer overflow issue exists in the rms_mqtt daemon on Teltonika Networks devices. An authenticated attacker wit… |
| 2026-11-24 12:17:22 | [CVE-2026-134858](https://nvd.nist.gov/vuln/detail/CVE-2026-134858) |  |  | In Apache Pinot 0.7.1 through 1.5.1, a caller who can submit URI ingestion jobs can select local files readable by the… |
| 2026-11-24 12:17:22 | [CVE-2026-135660](https://nvd.nist.gov/vuln/detail/CVE-2026-135660) |  |  | Improper Neutralization of Script-Related HTML Tags in a Web Page (Basic XSS) vulnerability in Apache Allura's ticket t… |
| 2026-11-24 12:17:22 | [CVE-2026-135747](https://nvd.nist.gov/vuln/detail/CVE-2026-135747) |  |  | Apache IoTDB MCP Server logs the IoTDB connection password in plaintext during startup, allowing anyone with access to… |
| 2026-11-24 12:17:23 | [CVE-2026-13137](https://nvd.nist.gov/vuln/detail/CVE-2026-13137) | High | 8.7 | A stack-based buffer overflow vulnerability exists in multiple parsers of RTU500 components of User management, REST re… |
| 2026-11-24 12:17:24 | [CVE-2026-59697](https://nvd.nist.gov/vuln/detail/CVE-2026-59697) | High | 7.6 | Server-Side Request Forgery (SSRF) vulnerability in ex_aws (instance metadata token provider). This vulnerability is as… |
| 2026-11-24 12:17:24 | [CVE-2026-59698](https://nvd.nist.gov/vuln/detail/CVE-2026-59698) | High | 7.4 | Relative path traversal in ex_aws allows an attacker who controls an S3 object key to escape the intended bucket or key… |
| 2026-11-24 12:17:25 | [CVE-2026-62269](https://nvd.nist.gov/vuln/detail/CVE-2026-62269) | Medium | 5.1 | Improper Encoding or Escaping of Output vulnerability in ex_aws (S3 request URL construction). This vulnerability is as… |
| 2026-11-24 12:17:25 | [CVE-2026-84785](https://nvd.nist.gov/vuln/detail/CVE-2026-84785) |  |  | Issue summary: A QUIC peer that sends many small out-of-order STREAM fragments while withholding the first byte of the… |
| 2026-11-24 12:17:26 | [CVE-2026-94365](https://nvd.nist.gov/vuln/detail/CVE-2026-94365) | Medium | 5.4 | Improper neutralization of input during web page generation ('cross-site scripting') vulnerability in ITG Bilgisayar Te… |
| 2026-11-24 12:17:26 | [CVE-2026-96438](https://nvd.nist.gov/vuln/detail/CVE-2026-96438) | Medium | 6.5 | Unrestricted upload of file with dangerous type vulnerability in ITG Bilgisayar Teknolojileri Grubu Ltd. Şti. VSRM allo… |
| 2026-11-24 12:17:26 | [CVE-2026-97198](https://nvd.nist.gov/vuln/detail/CVE-2026-97198) | Medium | 6.5 | Authorization bypass through User-Controlled key vulnerability in ITG Bilgisayar Teknolojileri Grubu Ltd. Şti. VSRM all… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
