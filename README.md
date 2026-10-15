# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-15 09:22 UTC

New CVEs published between 2026-10-15 08:19 UTC and 2026-10-15 09:22 UTC.

[Full CSV](data/new-cves-2026-10-15T09-22-21-6861Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-10-15 09:17:13 | [CVE-2023-32198](https://nvd.nist.gov/vuln/detail/CVE-2023-32198) | High | 8.0 | A vulnerability has been identified in Steve where by default it was using an insecure option that did not validate the… |
| 2026-10-15 09:17:14 | [CVE-2024-22031](https://nvd.nist.gov/vuln/detail/CVE-2024-22031) | High | 8.5 | A vulnerability has been identified within Rancher where a user with the ability to create a project, on a certain clus… |
| 2026-10-15 09:17:14 | [CVE-2025-23390](https://nvd.nist.gov/vuln/detail/CVE-2025-23390) | Medium | 6.3 | A vulnerability has been identified within Fleet where, by default, Fleet will automatically trust a remote server’s ce… |
| 2026-10-15 09:17:14 | [CVE-2026-101287](https://nvd.nist.gov/vuln/detail/CVE-2026-101287) | Critical | 9.3 | Authentication bypass vulnerability in Stela, versions prior to 1.60.1, due to the use of a cookie named “authProcess”… |
| 2026-10-15 09:17:14 | [CVE-2026-101290](https://nvd.nist.gov/vuln/detail/CVE-2026-101290) | High | 7.5 | A remote attacker may send a specially crafted network packet that causes the affected application to perform an out-of… |
| 2026-10-15 09:17:14 | [CVE-2026-102461](https://nvd.nist.gov/vuln/detail/CVE-2026-102461) | High | 8.7 | In Eclipse Vert.x versions [4.0.0, 4.5.34] or [5.0.0,5.0.12] or [5.1.0,5.1.9] or [5.2.0, 5.2.0], the uniqueItems keywor… |
| 2026-10-15 09:17:15 | [CVE-2026-102462](https://nvd.nist.gov/vuln/detail/CVE-2026-102462) | High | 8.2 | In Eclipse Vert.x versions [4.0.0, 4.5.34] or [5.0.0,5.0.12] or [5.1.0,5.1.9] or [5.2.0, 5.2.0], the TDS message decode… |
| 2026-10-15 09:17:15 | [CVE-2026-102463](https://nvd.nist.gov/vuln/detail/CVE-2026-102463) | High | 8.2 | In Eclipse Vert.x versions [4.0.0, 4.5.34] or [5.0.0,5.0.12] or [5.1.0,5.1.9] or [5.2.0, 5.2.0], the binary array decod… |
| 2026-10-15 09:17:15 | [CVE-2026-102464](https://nvd.nist.gov/vuln/detail/CVE-2026-102464) | High | 8.2 | In Eclipse Vert.x versions [4.0.0, 4.5.34] or [5.0.0,5.0.12] or [5.1.0,5.1.9] or [5.2.0, 5.2.0], the Eclipse Vert.x MQT… |
| 2026-10-15 09:17:15 | [CVE-2026-102466](https://nvd.nist.gov/vuln/detail/CVE-2026-102466) | High | 8.2 | In Eclipse Vert.x versions [4.0.0, 4.5.34] or [5.0.0,5.0.12] or [5.1.0,5.1.9] or [5.2.0, 5.2.0], the Vert.x MySQL clien… |
| 2026-10-15 09:17:15 | [CVE-2026-102469](https://nvd.nist.gov/vuln/detail/CVE-2026-102469) | Critical | 9.2 | In Eclipse Vert.x versions [4.0.0, 4.5.34] or [5.0.0,5.0.12] or [5.1.0,5.1.9] or [5.2.0, 5.2.0], the Vert.x DB2 client… |
| 2026-10-15 09:17:15 | [CVE-2026-102477](https://nvd.nist.gov/vuln/detail/CVE-2026-102477) | High | 8.7 | In Eclipse Vert.x versions [4.0.0, 4.5.34] or [5.0.0,5.0.12] or [5.1.0,5.1.9] or [5.2.0, 5.2.0], a gRPC endpoint does h… |
| 2026-10-15 09:17:15 | [CVE-2026-103223](https://nvd.nist.gov/vuln/detail/CVE-2026-103223) | High | 8.2 | In Eclipse Vert.x versions [4.0.0, 4.5.34] or [5.0.0,5.0.12] or [5.1.0,5.1.9] or [5.2.0, 5.2.0], the PostgreSQL message… |
| 2026-10-15 09:17:15 | [CVE-2026-103224](https://nvd.nist.gov/vuln/detail/CVE-2026-103224) | High | 8.2 | In Eclipse Vert.x versions [4.0.0, 4.5.34] or [5.0.0,5.0.12] or [5.1.0,5.1.9] or [5.2.0, 5.2.0], the MySQL message deco… |
| 2026-10-15 09:17:16 | [CVE-2026-104617](https://nvd.nist.gov/vuln/detail/CVE-2026-104617) | Medium | 5.9 | There are two invocations of `qrencode` to display a QR code for scanning. These invocations leak the private data $pin… |
| 2026-10-15 09:17:16 | [CVE-2026-104618](https://nvd.nist.gov/vuln/detail/CVE-2026-104618) | Medium | 6.9 | On request the `sdbootutil` script creates a world-readable debug log in /var/log/sdbootutil.log. The log file is creat… |
| 2026-10-15 09:17:16 | [CVE-2026-105271](https://nvd.nist.gov/vuln/detail/CVE-2026-105271) | Medium | 5.1 | "ゲオアプリ" provided by GEO CORPORATION contains an issue with cleartext storage of sensitive information, which may allow… |
| 2026-10-15 09:17:16 | [CVE-2026-109855](https://nvd.nist.gov/vuln/detail/CVE-2026-109855) | High | 7.5 | undici is an HTTP client library for Node.js. In versions 8.11.0 and 8.11.1, its experimental WebSocket client, which i… |
| 2026-10-15 09:17:16 | [CVE-2026-16436](https://nvd.nist.gov/vuln/detail/CVE-2026-16436) | Critical | 9.2 | Weak Password Recovery Mechanism for Forgotten Password vulnerability in Mitsubishi Electric GENESIS versions 11.03 and… |
| 2026-10-15 09:17:16 | [CVE-2026-16437](https://nvd.nist.gov/vuln/detail/CVE-2026-16437) | High | 7.1 | Weak Password Recovery Mechanism for Forgotten Password vulnerability in Mitsubishi Electric GENESIS versions 11.03 and… |
| 2026-10-15 09:17:17 | [CVE-2026-16438](https://nvd.nist.gov/vuln/detail/CVE-2026-16438) | Critical | 9.4 | Incorrect Privilege Assignment vulnerability in Mitsubishi Electric GENESIS64 versions 10.97.3 and prior, ICONICS Suite… |
| 2026-10-15 09:17:17 | [CVE-2026-18661](https://nvd.nist.gov/vuln/detail/CVE-2026-18661) | High | 8.8 | In Eclipse Jetty, across various versions of `jetty-annotations`, and `jetty-eeN-annotations`, the Jakarta Spec authori… |
| 2026-10-15 09:17:17 | [CVE-2026-35088](https://nvd.nist.gov/vuln/detail/CVE-2026-35088) | High | 8.2 | Slican telephone exchanges use symmetric encryption for TCP/IP communication. Secret key is hardcoded in multiple binar… |
| 2026-10-15 09:17:17 | [CVE-2026-63314](https://nvd.nist.gov/vuln/detail/CVE-2026-63314) | High | 8.7 | WebCTI service for Slican IPx telephone exchanges is vulnerable to SQL Injection in /webcti/admin_json.php enpoint. Imp… |
| 2026-10-15 09:17:17 | [CVE-2026-63315](https://nvd.nist.gov/vuln/detail/CVE-2026-63315) | High | 8.2 | WebCTI service for Slican IPx telephone exchanges stores temporary subscriber password in plaintext. An attacker with a… |
| 2026-10-15 09:17:17 | [CVE-2026-72528](https://nvd.nist.gov/vuln/detail/CVE-2026-72528) | Medium | 5.1 | "Handmade Marketplace App - Creema" provided by CREEMA LTD. contains an open redirect vulnerability. When accessing a s… |
| 2026-10-15 09:17:18 | [CVE-2026-75559](https://nvd.nist.gov/vuln/detail/CVE-2026-75559) | Medium | 6.9 | The smartphone application "Vehicle Inspection Certificate Viewer" contains a vulnerability in which sensitive informat… |
| 2026-10-15 09:17:18 | [CVE-2026-76182](https://nvd.nist.gov/vuln/detail/CVE-2026-76182) | Medium | 6.9 | In Eclipse Jetty, `TryPathsHandler` and `TryFilesFilter` can be configured to forward requests to template URIs such as… |
| 2026-10-15 09:17:18 | [CVE-2026-76184](https://nvd.nist.gov/vuln/detail/CVE-2026-76184) | High | 8.2 | In Eclipse Jetty, HttpClient may receive a redirect of the form: ``` /secure/../evil ``` If an attacker is able to cont… |
| 2026-10-15 09:17:18 | [CVE-2026-77711](https://nvd.nist.gov/vuln/detail/CVE-2026-77711) | High | 8.2 | When Jetty's `HttpClient` make a request to a server through a forward proxy, the server may reply with a 407 (Proxy Au… |
| 2026-10-15 09:17:18 | [CVE-2026-79823](https://nvd.nist.gov/vuln/detail/CVE-2026-79823) | Medium | 4.0 | HPE NonStop EMS Distributor is vulnerable to buffer overflow condition that may result in undesirable behavior. |
| 2026-10-15 09:17:18 | [CVE-2026-96614](https://nvd.nist.gov/vuln/detail/CVE-2026-96614) | Medium | 5.1 | "ゲオアプリ" provided by GEO CORPORATION is vulnerable to improper authorization in handler for a custom URL scheme. An atta… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
