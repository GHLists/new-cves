# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-09-29 16:19 UTC

New CVEs published between 2026-09-29 15:19 UTC and 2026-09-29 16:19 UTC.

[Full CSV](data/new-cves-2026-09-29T16-19-16-986737Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-09-29 16:17:04 | [CVE-2023-54400](https://nvd.nist.gov/vuln/detail/CVE-2023-54400) | Critical | 9.3 | Fumasoft Fumeng Cloud contains a SQL injection vulnerability in the AjaxMethod.ashx endpoint that allows unauthenticate… |
| 2026-09-29 16:17:04 | [CVE-2026-100286](https://nvd.nist.gov/vuln/detail/CVE-2026-100286) |  |  | Missing authorization in the data source settings API in Devolutions Server 2026.3.5.0 and earlier allows an authentica… |
| 2026-09-29 16:17:04 | [CVE-2026-100287](https://nvd.nist.gov/vuln/detail/CVE-2026-100287) |  |  | Missing authorization in the attachment history API in Devolutions Server 2026.3.5.0 and earlier allows an authenticate… |
| 2026-09-29 16:17:04 | [CVE-2026-100288](https://nvd.nist.gov/vuln/detail/CVE-2026-100288) |  |  | Cleartext storage of sensitive information in the database in Devolutions Server 2026.3.5.0 and earlier allows an attac… |
| 2026-09-29 16:17:04 | [CVE-2026-100289](https://nvd.nist.gov/vuln/detail/CVE-2026-100289) |  |  | Missing authorization in the gateway network scan token API in Devolutions Server 2026.3.5.0 and earlier allows an auth… |
| 2026-09-29 16:17:04 | [CVE-2026-100308](https://nvd.nist.gov/vuln/detail/CVE-2026-100308) | High | 8.4 | Deserialization of untrusted data in the model loading component in Amazon GluonTS before 0.17.0 might allow context-de… |
| 2026-09-29 16:17:06 | [CVE-2026-102598](https://nvd.nist.gov/vuln/detail/CVE-2026-102598) | Medium | 6.3 | Werkzeug is a comprehensive WSGI web application library. Prior to 3.1.9, the safe_join function used by send_from_dire… |
| 2026-09-29 16:17:06 | [CVE-2026-102600](https://nvd.nist.gov/vuln/detail/CVE-2026-102600) | High | 7.5 | Socket.IO enables bidirectional and low-latency communication for every platform. Prior to 0.1.1, @socket.io/cluster-en… |
| 2026-09-29 16:17:06 | [CVE-2026-102601](https://nvd.nist.gov/vuln/detail/CVE-2026-102601) | Low | 3.5 | Flysystem is an open source file storage library for PHP. Prior to 3.35.3, the default WhitespacePathNormalizer in src/… |
| 2026-09-29 16:17:06 | [CVE-2026-102630](https://nvd.nist.gov/vuln/detail/CVE-2026-102630) | Low | 2.3 | UnoPim versions before 2.0.1 and 2.1.1 trust all connecting clients as proxies and honor the X-Forwarded-Host header wi… |
| 2026-09-29 16:17:07 | [CVE-2026-19743](https://nvd.nist.gov/vuln/detail/CVE-2026-19743) | High | 7.8 | Improper path validation in the local IPC service of TeamViewer Full Client and Host on Windows, Linux, and macOS prior… |
| 2026-09-29 16:17:07 | [CVE-2026-35189](https://nvd.nist.gov/vuln/detail/CVE-2026-35189) |  |  | Issue summary: A certificate with many nameRelativeToCRLIssuer CRL distribution points causes disproportionate heap gro… |
| 2026-09-29 16:17:07 | [CVE-2026-35191](https://nvd.nist.gov/vuln/detail/CVE-2026-35191) |  |  | Issue summary: The OpenSSL QUIC server, when configured to not preform address validation, can be forced to count incom… |
| 2026-09-29 16:17:07 | [CVE-2026-42772](https://nvd.nist.gov/vuln/detail/CVE-2026-42772) |  |  | Issue summary: The QUIC stream reassembly algorithm performance deteriorates progressively as packets are arriving out… |
| 2026-09-29 16:17:08 | [CVE-2026-54872](https://nvd.nist.gov/vuln/detail/CVE-2026-54872) |  |  | Issue summary: The generic elliptic-curve scalar multiplication used for ECDSA and SM2 signature operations with curves… |
| 2026-09-29 16:17:08 | [CVE-2026-54873](https://nvd.nist.gov/vuln/detail/CVE-2026-54873) |  |  | Issue summary: QUIC process may keep memory for QUIC packet buffer for much longer period than necessary. Impact summar… |
| 2026-09-29 16:17:08 | [CVE-2026-54875](https://nvd.nist.gov/vuln/detail/CVE-2026-54875) |  |  | Issue summary: A non-constant-time optimized implementation of scalar point multiplication is used for SM2 private key… |
| 2026-09-29 16:17:09 | [CVE-2026-72897](https://nvd.nist.gov/vuln/detail/CVE-2026-72897) |  |  | Issue summary: A TLS server that calls SSL_set_SSL_CTX() to switch a connection to a different SSL_CTX part way through… |
| 2026-09-29 16:17:10 | [CVE-2026-75804](https://nvd.nist.gov/vuln/detail/CVE-2026-75804) |  |  | Issue summary: OpenSSL QUIC stack does not enforce connection level flow control for streams. Remote peers may send mor… |
| 2026-09-29 16:17:11 | [CVE-2026-75805](https://nvd.nist.gov/vuln/detail/CVE-2026-75805) |  |  | Issue summary: A CMP client that requests certificate revocation on the basis of a PKCS#10 CSR may dereference a NULL p… |
| 2026-09-29 16:17:11 | [CVE-2026-75806](https://nvd.nist.gov/vuln/detail/CVE-2026-75806) |  |  | Issue summary: An established DTLS 1.2 association using an AEAD cipher suite can be terminated by a single unauthentic… |
| 2026-09-29 16:17:11 | [CVE-2026-77177](https://nvd.nist.gov/vuln/detail/CVE-2026-77177) |  |  | Open GenAI Stack (aka ogx-ai) 2026-06-11, as used in the Meta AI backend for WhatsApp and other products, allows code e… |
| 2026-09-29 16:17:11 | [CVE-2026-77696](https://nvd.nist.gov/vuln/detail/CVE-2026-77696) |  |  | Issue summary: SM2 signature generation uses non-constant-time arithmetic on secret values, forming a timing side-chann… |
| 2026-09-29 16:17:12 | [CVE-2026-84782](https://nvd.nist.gov/vuln/detail/CVE-2026-84782) |  |  | Issue summary: The DTLS retransmission logic does not correctly handle a handshake message write that is suspended part… |
| 2026-09-29 16:17:12 | [CVE-2026-84783](https://nvd.nist.gov/vuln/detail/CVE-2026-84783) |  |  | Issue summary: The first concurrent use of the same X.509 certificate by several threads may cause its cached extension… |
| 2026-09-29 16:17:12 | [CVE-2026-84784](https://nvd.nist.gov/vuln/detail/CVE-2026-84784) |  |  | Issue summary: A malicious remote peer may flood the local QUIC stack with NEW_CONNECTION_ID frames by avoiding a limit… |
| 2026-09-29 16:17:14 | [CVE-2026-92368](https://nvd.nist.gov/vuln/detail/CVE-2026-92368) | High | 7.8 | TeamViewer Full Client and Host for Linux and macOS prior version 15.82 contain a heap-based buffer overflow vulnerabil… |
| 2026-09-29 16:17:14 | [CVE-2026-92369](https://nvd.nist.gov/vuln/detail/CVE-2026-92369) | High | 7.3 | TeamViewer Full Client and Host prior to version 15.82 on Windows contain a TOCTOU race condition in the installer roll… |
| 2026-09-29 16:17:15 | [CVE-2026-92370](https://nvd.nist.gov/vuln/detail/CVE-2026-92370) | High | 8.8 | An improper access control vulnerability in TeamViewer Full Client, Host, and related affected modules on Windows, Linu… |
| 2026-09-29 16:17:15 | [CVE-2026-92371](https://nvd.nist.gov/vuln/detail/CVE-2026-92371) | High | 7.0 | TeamViewer Full Client and Host for Linux prior version 15.82 contains an improper path validation vulnerability in the… |
| 2026-09-29 16:17:15 | [CVE-2026-93330](https://nvd.nist.gov/vuln/detail/CVE-2026-93330) | Medium | 4.3 | Improper rule enforcement in the PAM Active Directory provider in Devolutions Server 2026.3.5 allows a user with PAM ed… |
| 2026-09-29 16:17:15 | [CVE-2026-93332](https://nvd.nist.gov/vuln/detail/CVE-2026-93332) |  |  | Improper access control in the partial connection API in Devolutions Server 2026.3.5.0 and earlier allows an authentica… |
| 2026-09-29 16:17:18 | [CVE-2026-97687](https://nvd.nist.gov/vuln/detail/CVE-2026-97687) | High | 7.6 | urllib3 is an HTTP client library for Python. From 1.26.0 until 2.8.0, the proxy_ssl_context, proxy_assert_hostname, pr… |
| 2026-09-29 16:17:18 | [CVE-2026-97688](https://nvd.nist.gov/vuln/detail/CVE-2026-97688) | Medium | 6.9 | urllib3 is an HTTP client library for Python. From 2.6.2 until 2.8.0, HTTPResponse.stream and HTTPResponse.read_chunked… |
| 2026-09-29 16:17:18 | [CVE-2026-97689](https://nvd.nist.gov/vuln/detail/CVE-2026-97689) | High | 8.9 | urllib3 is an HTTP client library for Python. From 1.10.3 until 2.8.0, the HTTPResponse.read_chunked and HTTPResponse.s… |
| 2026-09-29 16:17:19 | [CVE-2026-97711](https://nvd.nist.gov/vuln/detail/CVE-2026-97711) | Low | 2.3 | Serialize JavaScript serializes JavaScript values to a superset of JSON that includes regular expressions and functions… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
