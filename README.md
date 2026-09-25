# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-09-25 21:18 UTC

New CVEs published between 2026-09-25 20:18 UTC and 2026-09-25 21:18 UTC.

[Full CSV](data/new-cves-2026-09-25T21-18-57-755819Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-09-25 21:17:19 | [CVE-2025-14181](https://nvd.nist.gov/vuln/detail/CVE-2025-14181) | Medium | 6.5 | The SOAP HTTP client guards its response buffer growth with a check that relies on signed integer overflow, which is un… |
| 2026-09-25 21:17:20 | [CVE-2025-1218](https://nvd.nist.gov/vuln/detail/CVE-2025-1218) | Low | 3.4 | The mysqlnd wire protocol parser reads fields out of server packets before checking that the packet still holds enough… |
| 2026-09-25 21:17:21 | [CVE-2026-100369](https://nvd.nist.gov/vuln/detail/CVE-2026-100369) | High | 8.4 | CliInvoke and its formerly named `AlastairLundy.CliInvoke` package are .NET libraries for invoking command-line program… |
| 2026-09-25 21:17:21 | [CVE-2026-100376](https://nvd.nist.gov/vuln/detail/CVE-2026-100376) | Medium | 4.8 | Improper Neutralization of Input During Web Page Generation (XSS or 'Cross-site Scripting') vulnerability in Wikimedia… |
| 2026-09-25 21:17:21 | [CVE-2026-100377](https://nvd.nist.gov/vuln/detail/CVE-2026-100377) | Medium | 6.9 | Exposure of Sensitive Information to an Unauthorized Actor vulnerability in Wikimedia Foundation Mediawiki - WikiLambda… |
| 2026-09-25 21:17:21 | [CVE-2026-100378](https://nvd.nist.gov/vuln/detail/CVE-2026-100378) | Medium | 5.3 | Missing Authorization vulnerability in Wikimedia Foundation Mediawiki - Translate Extension allows Accessing Functional… |
| 2026-09-25 21:17:21 | [CVE-2026-100379](https://nvd.nist.gov/vuln/detail/CVE-2026-100379) | Medium | 5.3 | Exposure of Sensitive Information to an Unauthorized Actor vulnerability in Wikimedia Foundation Wikipedia Android App… |
| 2026-09-25 21:17:22 | [CVE-2026-100380](https://nvd.nist.gov/vuln/detail/CVE-2026-100380) | Medium | 5.3 | Improper Neutralization of Input During Web Page Generation (XSS or 'Cross-site Scripting') vulnerability in Wikimedia… |
| 2026-09-25 21:17:22 | [CVE-2026-100387](https://nvd.nist.gov/vuln/detail/CVE-2026-100387) | High | 7.2 | pgPointcloud through 1.2.5 contains a heap out-of-bounds read vulnerability in dimensional patch WKB deserialization th… |
| 2026-09-25 21:17:22 | [CVE-2026-100388](https://nvd.nist.gov/vuln/detail/CVE-2026-100388) | Medium | 5.3 | RustDesk versions before 1.5.0 fail to properly validate file transfer permissions on incoming file clipboard messages… |
| 2026-09-25 21:17:22 | [CVE-2026-100389](https://nvd.nist.gov/vuln/detail/CVE-2026-100389) | Critical | 9.2 | GestSup versions before 3.2.61 contain a remote code execution vulnerability in the basic IMAP connector's attachment h… |
| 2026-09-25 21:17:22 | [CVE-2026-100390](https://nvd.nist.gov/vuln/detail/CVE-2026-100390) | Critical | 9.1 | Zoraxy versions 3.2.3 through 3.3.4 fail to properly parse IPv6 addresses in the RemoteAddr field when setting forwarde… |
| 2026-09-25 21:17:22 | [CVE-2026-100391](https://nvd.nist.gov/vuln/detail/CVE-2026-100391) | High | 8.8 | MediaFlow Proxy through 2.4.9 contains a server-side request forgery vulnerability in the /proxy routes due to missing… |
| 2026-09-25 21:17:22 | [CVE-2026-100417](https://nvd.nist.gov/vuln/detail/CVE-2026-100417) | Low | 2.3 | RustDesk before 1.5.0 on Windows fails to enforce the one-way file transfer option against peer clipboard file requests… |
| 2026-09-25 21:17:23 | [CVE-2026-10758](https://nvd.nist.gov/vuln/detail/CVE-2026-10758) | High | 7.5 | Esri LERC is an open-source image or raster format which supports rapid encoding and decoding for any pixel type. A Hea… |
| 2026-09-25 21:17:23 | [CVE-2026-17545](https://nvd.nist.gov/vuln/detail/CVE-2026-17545) | Medium | 6.9 | On Windows, PHP's filesystem and stream APIs do not reject reserved device names such as CON, PRN, AUX, NUL, COM1 to CO… |
| 2026-09-25 21:17:23 | [CVE-2026-57443](https://nvd.nist.gov/vuln/detail/CVE-2026-57443) | High | 7.5 | SCBE-AETHERMOORE is a geometric AI governance and evaluation framework. Starting in version 4.0.2 and prior to version… |
| 2026-09-25 21:17:23 | [CVE-2026-57864](https://nvd.nist.gov/vuln/detail/CVE-2026-57864) |  |  | Rejected reason: This CVE ID has been rejected or withdrawn by its CVE Numbering Authority. |
| 2026-09-25 21:17:23 | [CVE-2026-6103](https://nvd.nist.gov/vuln/detail/CVE-2026-6103) | Medium | 4.3 | phar_tar_number() parses the octal size field of a TAR header into a uint32_t with no overflow check. The field is 11 o… |
| 2026-09-25 21:17:24 | [CVE-2026-91765](https://nvd.nist.gov/vuln/detail/CVE-2026-91765) | High | 7.5 | cleanup_xml_node() in the SOAP XML parser recurses once per XML nesting level with no depth limit. An unauthenticated a… |
| 2026-09-25 21:17:24 | [CVE-2026-91766](https://nvd.nist.gov/vuln/detail/CVE-2026-91766) | Medium | 5.9 | When the http:// stream wrapper follows a redirect it forwards the user-supplied Authorization, Cookie and Proxy-Author… |
| 2026-09-25 21:17:24 | [CVE-2026-91767](https://nvd.nist.gov/vuln/detail/CVE-2026-91767) | Medium | 6.5 | php_openssl_matches_wildcard_name() in ext/openssl/xp_ssl.c underflows the length argument passed to memchr() when a TL… |
| 2026-09-25 21:17:24 | [CVE-2026-91769](https://nvd.nist.gov/vuln/detail/CVE-2026-91769) | Medium | 4.3 | PHP's OpenSSL stream peer verification checks the certificate's subjectAltName entries first and, whenever no entry mat… |
| 2026-09-25 21:17:25 | [CVE-2026-96879](https://nvd.nist.gov/vuln/detail/CVE-2026-96879) | Medium | 6.9 | Improper removal of sensitive information before storage or transfer vulnerability in Wikimedia Foundation's Mediawiki… |
| 2026-09-25 21:17:25 | [CVE-2026-9313](https://nvd.nist.gov/vuln/detail/CVE-2026-9313) |  |  | Rejected reason: This CVE ID has been rejected or withdrawn by its CVE Numbering Authority. |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
