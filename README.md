# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-19 17:23 UTC

New CVEs published between 2026-10-19 16:18 UTC and 2026-10-19 17:23 UTC.

[Full CSV](data/new-cves-2026-10-19T17-23-18-077073Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-10-19 17:16:57 | [CVE-2024-4412](https://nvd.nist.gov/vuln/detail/CVE-2024-4412) | Low | 2.7 | The software accepts user-supplied data without sufficient validation, allowing for the injection of malicious Expressi… |
| 2026-10-19 17:16:59 | [CVE-2025-10149](https://nvd.nist.gov/vuln/detail/CVE-2025-10149) | High | 8.2 | The SCIM endpoint does not sufficiently validate authorization for federated users when performing operations against t… |
| 2026-10-19 17:16:59 | [CVE-2025-13173](https://nvd.nist.gov/vuln/detail/CVE-2025-13173) | Medium | 6.5 | Tokens associated with user sessions are not revoked when the corresponding user session is terminated, unless another… |
| 2026-10-19 17:16:59 | [CVE-2025-13591](https://nvd.nist.gov/vuln/detail/CVE-2025-13591) | Medium | 5.3 | The authentication endpoint of WSO2 Identity Server fails to provide a consistent system response when a username does… |
| 2026-10-19 17:16:59 | [CVE-2025-6623](https://nvd.nist.gov/vuln/detail/CVE-2025-6623) | Medium | 4.3 | The carbon console accepts user-supplied XML input without sufficiently encoding potentially executable content, allowi… |
| 2026-10-19 17:16:59 | [CVE-2025-7043](https://nvd.nist.gov/vuln/detail/CVE-2025-7043) | Medium | 5.4 | The ForgeRock client fails to correctly validate refresh tokens. This allows a refresh token to be treated as a valid a… |
| 2026-10-19 17:17:00 | [CVE-2025-7203](https://nvd.nist.gov/vuln/detail/CVE-2025-7203) | Medium | 4.9 | The Management Console and product files expose sensitive data, including remote log server credentials, truststore pas… |
| 2026-10-19 17:17:00 | [CVE-2026-103038](https://nvd.nist.gov/vuln/detail/CVE-2026-103038) | High | 8.6 | PingTools Network Utilities 4.64 Free accepts an arbitrary value in the Host field of a Watcher ICMP service, incorpora… |
| 2026-10-19 17:17:00 | [CVE-2026-107082](https://nvd.nist.gov/vuln/detail/CVE-2026-107082) |  |  | Slims (Senayan Library Management Systems) 9 Bulian 9.8.0 allows an authenticated staff user to perform SQL injection v… |
| 2026-10-19 17:17:00 | [CVE-2026-107083](https://nvd.nist.gov/vuln/detail/CVE-2026-107083) |  |  | SENAYAN Library Management System (SLiMS) Bulian (slims9_bulian) 9.8.0 is vulnerable to SQL Injection in admin/modules/… |
| 2026-10-19 17:17:00 | [CVE-2026-107186](https://nvd.nist.gov/vuln/detail/CVE-2026-107186) | High | 8.6 | An unauthenticated user can send a DWR request with isPasswordUppercase as one call method and the next call method can… |
| 2026-10-19 17:17:00 | [CVE-2026-107187](https://nvd.nist.gov/vuln/detail/CVE-2026-107187) | High | 8.5 | A user can access any database details, such as usernames and passwords by sending a DWR request with a specified workf… |
| 2026-10-19 17:17:01 | [CVE-2026-107188](https://nvd.nist.gov/vuln/detail/CVE-2026-107188) | Critical | 9.6 | A user can upload export reports with any file contents and specify any contents. JSP code can be uploaded, JSPX can be… |
| 2026-10-19 17:17:01 | [CVE-2026-10572](https://nvd.nist.gov/vuln/detail/CVE-2026-10572) | High | 8.8 | IBM MQ could allow an authenticated attacker to cause a denial of service or potentially execute arbitrary code due to… |
| 2026-10-19 17:17:01 | [CVE-2026-10574](https://nvd.nist.gov/vuln/detail/CVE-2026-10574) | High | 8.8 | IBM MQ could allow an authenticated attacker to cause a denial of service or potentially execute arbitrary code due to… |
| 2026-10-19 17:17:02 | [CVE-2026-10743](https://nvd.nist.gov/vuln/detail/CVE-2026-10743) | High | 8.8 | IBM MQ could allow an authenticated attacker to cause a denial of service or corrupt memory due to improper validation… |
| 2026-10-19 17:17:02 | [CVE-2026-111059](https://nvd.nist.gov/vuln/detail/CVE-2026-111059) | Medium | 6.1 | Mercury is a Python framework for sharing Jupyter notebooks as web applications and dashboards. From 3.0.0 until 3.2.11… |
| 2026-10-19 17:17:03 | [CVE-2026-111061](https://nvd.nist.gov/vuln/detail/CVE-2026-111061) | Medium | 4.3 | russh is a Rust SSH client and server library that includes an SSH agent protocol implementation. Prior to 0.64.1, the… |
| 2026-10-19 17:17:03 | [CVE-2026-111063](https://nvd.nist.gov/vuln/detail/CVE-2026-111063) | Medium | 6.3 | AIOHTTP is an asynchronous HTTP client/server framework for asyncio and Python. Prior to 3.14.4, the Secure attribute f… |
| 2026-10-19 17:17:03 | [CVE-2026-111064](https://nvd.nist.gov/vuln/detail/CVE-2026-111064) | High | 8.2 | AIOHTTP is an asynchronous HTTP client/server framework for asyncio and Python. Prior to 3.14.4, keepalive timeout hand… |
| 2026-10-19 17:17:03 | [CVE-2026-111065](https://nvd.nist.gov/vuln/detail/CVE-2026-111065) | Medium | 6.9 | AIOHTTP is an asynchronous HTTP client/server framework for asyncio and Python. Prior to 3.14.4, Max-Age processing can… |
| 2026-10-19 17:17:03 | [CVE-2026-111066](https://nvd.nist.gov/vuln/detail/CVE-2026-111066) | High | 8.2 | AIOHTTP is an asynchronous HTTP client/server framework for asyncio and Python. From 2.0.0 until 3.14.4, multipart requ… |
| 2026-10-19 17:17:03 | [CVE-2026-111748](https://nvd.nist.gov/vuln/detail/CVE-2026-111748) | Medium | 6.3 | AIOHTTP is an asynchronous HTTP client/server framework for asyncio and Python. Prior to 3.14.4, an attacker can send a… |
| 2026-10-19 17:17:04 | [CVE-2026-111749](https://nvd.nist.gov/vuln/detail/CVE-2026-111749) | Low | 2.3 | AIOHTTP is an asynchronous HTTP client/server framework for asyncio and Python. Prior to 3.14.4, Host-Only scope on an… |
| 2026-10-19 17:17:04 | [CVE-2026-111750](https://nvd.nist.gov/vuln/detail/CVE-2026-111750) | Medium | 6.3 | AIOHTTP is an asynchronous HTTP client/server framework for asyncio and Python. Prior to 3.14.4, the pure Python parser… |
| 2026-10-19 17:17:04 | [CVE-2026-111862](https://nvd.nist.gov/vuln/detail/CVE-2026-111862) | Critical | 9.8 | Rank Math SEO PRO for WordPress is affected by a supply-chain compromise in a subset of version 3.0.123 packages downlo… |
| 2026-10-19 17:17:13 | [CVE-2026-112159](https://nvd.nist.gov/vuln/detail/CVE-2026-112159) | Low | 2.0 | A security vulnerability has been detected in JumpServer up to 4.10.19. The affected element is an unknown function of… |
| 2026-10-19 17:17:14 | [CVE-2026-112190](https://nvd.nist.gov/vuln/detail/CVE-2026-112190) | Medium | 5.5 | A security vulnerability has been detected in Webkul Aureus ERP up to 1.6.0. This issue affects some unknown processing… |
| 2026-10-19 17:17:14 | [CVE-2026-112193](https://nvd.nist.gov/vuln/detail/CVE-2026-112193) | Low | 2.9 | A vulnerability was detected in Webkul Aureus ERP up to 1.6.0. Impacted is an unknown function of the file plugins/webk… |
| 2026-10-19 17:17:14 | [CVE-2026-112195](https://nvd.nist.gov/vuln/detail/CVE-2026-112195) | Low | 2.0 | A flaw has been found in FusionPBX up to 5.4.4/5.5.7/5.6.5. The affected element is an unknown function of the file app… |
| 2026-10-19 17:17:16 | [CVE-2026-11828](https://nvd.nist.gov/vuln/detail/CVE-2026-11828) | Medium | 5.9 | IBM MQ could allow a remote attacker with queue manager control or man-in-the-middle access on unencrypted channels to… |
| 2026-10-19 17:17:16 | [CVE-2026-11829](https://nvd.nist.gov/vuln/detail/CVE-2026-11829) | Medium | 6.5 | IBM MQ could allow an authenticated attacker to cause a denial of service due to improper validation of offset values i… |
| 2026-10-19 17:17:16 | [CVE-2026-11831](https://nvd.nist.gov/vuln/detail/CVE-2026-11831) | Medium | 5.4 | IBM MQ could allow an authenticated attacker to cause a limited denial of service and obtain very limited information a… |
| 2026-10-19 17:17:17 | [CVE-2026-12148](https://nvd.nist.gov/vuln/detail/CVE-2026-12148) | High | 7.5 | IBM MQ Operator could allow an authenticated attacker to cause a denial of service or potentially execute arbitrary cod… |
| 2026-10-19 17:17:17 | [CVE-2026-12155](https://nvd.nist.gov/vuln/detail/CVE-2026-12155) | Medium | 6.5 | IBM MQ could allow an authenticated attacker to cause a denial of service by sending specially crafted multicast status… |
| 2026-10-19 17:17:17 | [CVE-2026-12343](https://nvd.nist.gov/vuln/detail/CVE-2026-12343) | Medium | 6.5 | IBM MQ could allow an authenticated attacker to cause a denial of service due to improper validation of RFH2 message he… |
| 2026-10-19 17:17:18 | [CVE-2026-12350](https://nvd.nist.gov/vuln/detail/CVE-2026-12350) | Medium | 6.5 | IBM MQ could allow an authenticated attacker to cause a denial of service by sending a specially crafted asynchronous c… |
| 2026-10-19 17:17:18 | [CVE-2026-12660](https://nvd.nist.gov/vuln/detail/CVE-2026-12660) | Low | 2.7 | IBM MQ Web Console could allow an authenticated administrator to write files outside the intended directory due to impr… |
| 2026-10-19 17:17:18 | [CVE-2026-12665](https://nvd.nist.gov/vuln/detail/CVE-2026-12665) | High | 8.1 | IBM MQ could allow a remote attacker to execute arbitrary code due to a stack buffer overflow when processing TLS certi… |
| 2026-10-19 17:17:19 | [CVE-2026-12669](https://nvd.nist.gov/vuln/detail/CVE-2026-12669) | Low | 3.1 | IBM MQ could allow an authenticated attacker to trigger a minor out-of-bounds read when sending malformed compressed da… |
| 2026-10-19 17:17:19 | [CVE-2026-12670](https://nvd.nist.gov/vuln/detail/CVE-2026-12670) | Medium | 5.3 | IBM MQ could allow an authenticated attacker to cause a denial of service through a specially crafted message that trig… |
| 2026-10-19 17:17:19 | [CVE-2026-12727](https://nvd.nist.gov/vuln/detail/CVE-2026-12727) | Medium | 4.3 | IBM MQ could allow an authenticated attacker to cause potential process instability due to an off-by-one buffer overflo… |
| 2026-10-19 17:17:20 | [CVE-2026-14511](https://nvd.nist.gov/vuln/detail/CVE-2026-14511) | Medium | 6.5 | IBM MQ 9.4.5.0 through 9.4.5.1 could allow an authenticated user to cause a denial of service by sending a specially cr… |
| 2026-10-19 17:17:20 | [CVE-2026-15661](https://nvd.nist.gov/vuln/detail/CVE-2026-15661) | Medium | 5.3 | IBM Concert 1.0 through 3.0.0 could allow an unauthorized user to inject data into log messages due to improper neutral… |
| 2026-10-19 17:17:21 | [CVE-2026-6930](https://nvd.nist.gov/vuln/detail/CVE-2026-6930) | Low | 3.7 | IBM Concert 1.0 through 3.0.0 uses weaker than expected cryptographic algorithms that could allow an attacker to decryp… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
