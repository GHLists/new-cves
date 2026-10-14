# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-14 10:19 UTC

New CVEs published between 2026-10-14 09:20 UTC and 2026-10-14 10:19 UTC.

[Full CSV](data/new-cves-2026-10-14T10-19-38-357562Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-10-14 10:17:50 | [CVE-2026-100231](https://nvd.nist.gov/vuln/detail/CVE-2026-100231) | Medium | 6.1 | A flaw was found in the GStreamer multimedia framework's ASF muxer plugin (asfmux). When writing string metadata tags c… |
| 2026-10-14 10:17:51 | [CVE-2026-109969](https://nvd.nist.gov/vuln/detail/CVE-2026-109969) | Medium | 4.7 | A flaw was found in the clevis PKCS#11 pin. The clevis-pkcs11-afunix-socket-unlock daemon creates AF_UNIX sockets witho… |
| 2026-10-14 10:17:52 | [CVE-2026-109970](https://nvd.nist.gov/vuln/detail/CVE-2026-109970) | Medium | 4.7 | A flaw was found in the clevis PKCS#11 pin. The clevis-luks-pkcs11-askpin script writes the PKCS#11 token PIN in plaint… |
| 2026-10-14 10:17:53 | [CVE-2026-109971](https://nvd.nist.gov/vuln/detail/CVE-2026-109971) | Medium | 4.7 | A flaw was found in the clevis PKCS#11 pin. The clevis-decrypt-pkcs11 script passes the PKCS#11 token PIN as a command-… |
| 2026-10-14 10:17:54 | [CVE-2026-73791](https://nvd.nist.gov/vuln/detail/CVE-2026-73791) | Low | 2.0 | A security vulnerability in HPE NonStop Hpjmeter can cause stack and heap buffer overflow. |
| 2026-10-14 10:17:56 | [CVE-2026-73792](https://nvd.nist.gov/vuln/detail/CVE-2026-73792) | Low | 3.8 | A security vulnerability in HPE NonStop Java JToolkit can allow command Injection and buffer overflow. |
| 2026-10-14 10:17:56 | [CVE-2026-73793](https://nvd.nist.gov/vuln/detail/CVE-2026-73793) | High | 7.9 | HPE NonStop Middleware software has secret key handling and data deserialization vulnerability. |
| 2026-10-14 10:17:56 | [CVE-2026-73794](https://nvd.nist.gov/vuln/detail/CVE-2026-73794) | Medium | 4.6 | HPE NonStop MODULAR NSJ contains a predictable seed vulnerability in Random Number Generation (PRNG) |
| 2026-10-14 10:17:56 | [CVE-2026-86476](https://nvd.nist.gov/vuln/detail/CVE-2026-86476) | High | 8.4 | A flaw was found in gst-plugins-base. A heap buffer overflow can be triggered when processing video buffers whose attac… |
| 2026-10-14 10:17:57 | [CVE-2026-88829](https://nvd.nist.gov/vuln/detail/CVE-2026-88829) | High | 7.2 | A flaw was found in BusyBox httpd's reverse proxy feature. When the proxy is configured to forward requests matching a… |
| 2026-10-14 10:17:57 | [CVE-2026-90954](https://nvd.nist.gov/vuln/detail/CVE-2026-90954) | High | 7.8 | A flaw was found in BusyBox's dpkg-deb archive extraction. The ar archive handler flushes deferred symlinks after each… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
