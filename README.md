# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-11-03 19:18 UTC

New CVEs published between 2026-11-03 18:19 UTC and 2026-11-03 19:18 UTC.

[Full CSV](data/new-cves-2026-11-03T19-18-22-860313Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-11-03 19:17:53 | [CVE-2026-112917](https://nvd.nist.gov/vuln/detail/CVE-2026-112917) | Critical | 9.2 | In Docker Desktop for Windows with the WSL2 backend, an unprivileged Linux container can use 32-bit socketcall to bypas… |
| 2026-11-03 19:17:57 | [CVE-2026-119922](https://nvd.nist.gov/vuln/detail/CVE-2026-119922) | High | 8.7 | Improper access control in the Babelfish for PostgreSQL extension versions 1.2-1.5, 2.1-2.15, 3.1-3.12, 4.0-4.8, 5.1-5.… |
| 2026-11-03 19:17:59 | [CVE-2026-120673](https://nvd.nist.gov/vuln/detail/CVE-2026-120673) | Medium | 6.8 | A component of the MongoDB Rust Driver that records diagnostic tracing data can capture command content before automati… |
| 2026-11-03 19:17:59 | [CVE-2026-120678](https://nvd.nist.gov/vuln/detail/CVE-2026-120678) | High | 8.7 | A memory management flaw in the MongoDB C Driver's handling of compressed responses may cause the client library to hol… |
| 2026-11-03 19:18:00 | [CVE-2026-120684](https://nvd.nist.gov/vuln/detail/CVE-2026-120684) | Medium | 6.0 | A memory-initialization flaw in the legacy GridFS file handling of the MongoDB C Driver can cause uninitialized process… |
| 2026-11-03 19:18:00 | [CVE-2026-120953](https://nvd.nist.gov/vuln/detail/CVE-2026-120953) | Medium | 5.1 | A URI redirection weakness exists in the authentication component of the Atlas SQL JDBC Driver. During an interactive s… |
| 2026-11-03 19:18:00 | [CVE-2026-120954](https://nvd.nist.gov/vuln/detail/CVE-2026-120954) | Medium | 6.3 | A weakness in the BSON library's handling of a specialized binary vector data type allows an arithmetic wraparound when… |
| 2026-11-03 19:18:00 | [CVE-2026-120955](https://nvd.nist.gov/vuln/detail/CVE-2026-120955) | High | 8.7 | The GridFS file download API in the MongoDB C Driver does not check the result of an internal operation under certain e… |
| 2026-11-03 19:18:00 | [CVE-2026-120956](https://nvd.nist.gov/vuln/detail/CVE-2026-120956) | High | 7.1 | The MongoDB C Driver does not validate the type or format of a namespace field returned by the server in a query respon… |
| 2026-11-03 19:18:01 | [CVE-2026-121382](https://nvd.nist.gov/vuln/detail/CVE-2026-121382) | High | 7.7 | A vulnerability was determined in Netcore NBR100V2 1.3.240614.030928. Affected by this issue is the function msg_aes_de… |
| 2026-11-03 19:18:04 | [CVE-2026-121501](https://nvd.nist.gov/vuln/detail/CVE-2026-121501) | Low | 2.1 | A vulnerability was determined in mathurvishal CloudClassroom-PHP-Project. The affected element is the function session… |
| 2026-11-03 19:18:05 | [CVE-2026-121652](https://nvd.nist.gov/vuln/detail/CVE-2026-121652) | Medium | 4.8 | Cross-site scripting (XSS) issue in AWS Amplify maplibre-gl-js-amplify before 4.0.3 might allow remote authenticated us… |
| 2026-11-03 19:18:05 | [CVE-2026-39379](https://nvd.nist.gov/vuln/detail/CVE-2026-39379) | High | 7.1 | GeoNetwork is a catalog application to manage spatially referenced resources. From 3.0.0 until 4.2.15 and 4.4.10, reque… |
| 2026-11-03 19:18:05 | [CVE-2026-46487](https://nvd.nist.gov/vuln/detail/CVE-2026-46487) | High | 7.5 | GeoNetwork is a catalog application to manage spatially referenced resources. From 4.0.0-alpha.1 until 4.2.16 and 4.4.1… |
| 2026-11-03 19:18:06 | [CVE-2026-57154](https://nvd.nist.gov/vuln/detail/CVE-2026-57154) | High | 8.1 | OPNsense is a FreeBSD based firewall and routing platform. Prior to 26.1.11 and 26.4.1p1, authenticated Web UI or API u… |
| 2026-11-03 19:18:08 | [CVE-2026-63197](https://nvd.nist.gov/vuln/detail/CVE-2026-63197) | High | 7.3 | traQ is a messenger application built for Digital Creators Club traP. Prior to 3.28.3, instances configured with TRAQ_S… |
| 2026-11-03 19:18:09 | [CVE-2026-63198](https://nvd.nist.gov/vuln/detail/CVE-2026-63198) | High | 7.3 | traQ is a messenger application built for Digital Creators Club traP. Prior to 3.28.3, OAuth2 silent authorization requ… |
| 2026-11-03 19:18:09 | [CVE-2026-63417](https://nvd.nist.gov/vuln/detail/CVE-2026-63417) | High | 8.2 | Logging Redactor is a Python library designed to redact sensitive data in logs based on regex patterns and / or diction… |
| 2026-11-03 19:18:10 | [CVE-2026-82976](https://nvd.nist.gov/vuln/detail/CVE-2026-82976) | High | 7.1 | A flaw was found in the image-customization-controller used in OpenShift's bare metal provisioning stack. The controlle… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
