# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-11-13 08:19 UTC

New CVEs published between 2026-11-13 07:18 UTC and 2026-11-13 08:19 UTC.

[Full CSV](data/new-cves-2026-11-13T08-19-49-911887Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-11-13 08:17:15 | [CVE-2026-111333](https://nvd.nist.gov/vuln/detail/CVE-2026-111333) | Medium | 6.9 | Memory overflow in an authentication request can lead to unpredictable or erroneous behavior or Denial of Service in Ci… |
| 2026-11-13 08:17:15 | [CVE-2026-111334](https://nvd.nist.gov/vuln/detail/CVE-2026-111334) | Critical | 9.3 | Memory overflow in Endpoint Analysis (EPA/EPAS) can lead to unpredictable or erroneous behavior or a Denial of Service… |
| 2026-11-13 08:17:15 | [CVE-2026-111335](https://nvd.nist.gov/vuln/detail/CVE-2026-111335) | Medium | 6.9 | Improper request handling can lead to a denial-of-service / reboot-loop condition in Citrix NetScaler ADC and Citrix Ne… |
| 2026-11-13 08:17:15 | [CVE-2026-111336](https://nvd.nist.gov/vuln/detail/CVE-2026-111336) | High | 8.3 | Memory overflow in HTTP/2 handling can lead to unpredictable or erroneous behavior or Denial of Service in Citrix NetSc… |
| 2026-11-13 08:17:15 | [CVE-2026-111337](https://nvd.nist.gov/vuln/detail/CVE-2026-111337) | High | 8.7 | Memory overflow in Base64 decoding in advanced policy expressions leading to unpredictable or erroneous behavior or Den… |
| 2026-11-13 08:17:16 | [CVE-2026-111338](https://nvd.nist.gov/vuln/detail/CVE-2026-111338) | Medium | 6.9 | Sensitive authentication material written to a log file in Citrix NetScaler ADC and Citrix NetScaler Gateway. |
| 2026-11-13 08:17:16 | [CVE-2026-111339](https://nvd.nist.gov/vuln/detail/CVE-2026-111339) | Medium | 6.9 | Memory overflow in Application Firewall data decompression/inspection can lead to unpredictable or erroneous behavior o… |
| 2026-11-13 08:17:16 | [CVE-2026-116432](https://nvd.nist.gov/vuln/detail/CVE-2026-116432) | Medium | 4.3 | Dell PowerScale InsightIQ, versions 6.3.0 through 6.4.0, contains an Insertion of Sensitive Information into Log File v… |
| 2026-11-13 08:17:16 | [CVE-2026-120860](https://nvd.nist.gov/vuln/detail/CVE-2026-120860) | High | 8.7 | Memory overflow in protocol load-balancing traffic handling (Diameter, SIP-over-TCP, MQTT, RADIUS) can lead to unpredic… |
| 2026-11-13 08:17:16 | [CVE-2026-120861](https://nvd.nist.gov/vuln/detail/CVE-2026-120861) | High | 8.7 | Memory overflow / improper handling in GSLB and geolocation (MEP, static-proximity, config-sync) can lead to unpredicta… |
| 2026-11-13 08:17:16 | [CVE-2026-120862](https://nvd.nist.gov/vuln/detail/CVE-2026-120862) | High | 8.7 | Memory overflow in SIP ALG (LSN) and DNS answer-section logging datapaths can lead to unpredictable or erroneous behavi… |
| 2026-11-13 08:17:17 | [CVE-2026-120863](https://nvd.nist.gov/vuln/detail/CVE-2026-120863) | High | 8.7 | Memory overflow in the management plane can lead to unpredictable or erroneous behavior or Denial of Service in Citrix… |
| 2026-11-13 08:17:17 | [CVE-2026-128637](https://nvd.nist.gov/vuln/detail/CVE-2026-128637) | Medium | 5.1 | The MISP Modules website component contains an open redirect vulnerability in its login endpoint. The /login route acce… |
| 2026-11-13 08:17:17 | [CVE-2026-59074](https://nvd.nist.gov/vuln/detail/CVE-2026-59074) | High | 8.7 | Edito CMS is vulnerable to improper cryptographic signature verification in the JWT refresh logic. An authenticated low… |
| 2026-11-13 08:17:17 | [CVE-2026-59075](https://nvd.nist.gov/vuln/detail/CVE-2026-59075) | High | 7.1 | Edito CMS is vulnerable to Dynamic LINQ injection. Due to improper input validation, an authenticated attacker can inje… |
| 2026-11-13 08:17:17 | [CVE-2026-59076](https://nvd.nist.gov/vuln/detail/CVE-2026-59076) | Medium | 5.1 | Edito CMS is vulnerable to Stored Cross-Site Scripting (XSS). Due to improper input validation, an authenticated attack… |
| 2026-11-13 08:17:17 | [CVE-2026-59077](https://nvd.nist.gov/vuln/detail/CVE-2026-59077) | Medium | 5.1 | Edito CMS is vulnerable to Stored XSS via content parameter in Tiny editor functionality. Authenticated attacker can in… |
| 2026-11-13 08:17:17 | [CVE-2026-59078](https://nvd.nist.gov/vuln/detail/CVE-2026-59078) | Medium | 5.1 | Edito CMS is vulnerable to Stored XSS in avatar upload functionality. Authenticated attacker can inject arbitrary HTML… |
| 2026-11-13 08:17:18 | [CVE-2026-59079](https://nvd.nist.gov/vuln/detail/CVE-2026-59079) | High | 7.1 | Edito CMS restricts the ability to upload files via the UI to specific file types. However, an avatar upload functional… |
| 2026-11-13 08:17:18 | [CVE-2026-59080](https://nvd.nist.gov/vuln/detail/CVE-2026-59080) | Low | 2.1 | Edito CMS sends JWT token via GET requests. This allows a local attacker with access to browser history to obtain valid… |
| 2026-11-13 08:17:18 | [CVE-2026-59081](https://nvd.nist.gov/vuln/detail/CVE-2026-59081) | High | 8.4 | Edito CMS deserializes JSON data without further validation. A user (even an administrator) cannot exploit this vulnera… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
