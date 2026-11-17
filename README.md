# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-11-17 09:18 UTC

New CVEs published between 2026-11-17 08:21 UTC and 2026-11-17 09:18 UTC.

[Full CSV](data/new-cves-2026-11-17T09-18-18-201616Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-11-17 09:17:25 | [CVE-2026-107493](https://nvd.nist.gov/vuln/detail/CVE-2026-107493) |  |  | Issue summary: When an application passes a stack to PEM_X509_INFO_read_bio_ex() to add entries to, and reading fails,… |
| 2026-11-17 09:17:26 | [CVE-2026-109138](https://nvd.nist.gov/vuln/detail/CVE-2026-109138) | High | 8.3 | In the Aliro access control reference applications of the Nordic Semiconductor nRF Door Lock and Access Control Add-on… |
| 2026-11-17 09:17:26 | [CVE-2026-109148](https://nvd.nist.gov/vuln/detail/CVE-2026-109148) | High | 7.0 | In the Aliro access control reference applications of the Nordic Semiconductor nRF Door Lock and Access Control Add-on… |
| 2026-11-17 09:17:26 | [CVE-2026-109151](https://nvd.nist.gov/vuln/detail/CVE-2026-109151) | High | 7.0 | In the Matter and Aliro Door Lock Application of the Nordic Semiconductor nRF Door Lock and Access Control Add-on v1.0.… |
| 2026-11-17 09:17:26 | [CVE-2026-109154](https://nvd.nist.gov/vuln/detail/CVE-2026-109154) | High | 7.0 | In the Matter door lock applications of the Nordic Semiconductor nRF Door Lock and Access Control Add-on v1.0.0 through… |
| 2026-11-17 09:17:26 | [CVE-2026-119643](https://nvd.nist.gov/vuln/detail/CVE-2026-119643) | High | 7.2 | The MembershipWorks - Membership, Events & Directory plugin for WordPress is vulnerable to Stored Cross-Site Scripting… |
| 2026-11-17 09:17:26 | [CVE-2026-121864](https://nvd.nist.gov/vuln/detail/CVE-2026-121864) | High | 7.7 | In nanobot, when sandboxed exec is enabled, the shell executable used to run commands can be selected by the caller and… |
| 2026-11-17 09:17:27 | [CVE-2026-121865](https://nvd.nist.gov/vuln/detail/CVE-2026-121865) | High | 7.2 | In nanobot, the WebSocket gateway allows a standard client holding a valid client token to select an existing directory… |
| 2026-11-17 09:17:27 | [CVE-2026-124709](https://nvd.nist.gov/vuln/detail/CVE-2026-124709) |  |  | Issue summary: A QUIC server that rejects a stream opened by the peer may retain that stream's state for the lifetime o… |
| 2026-11-17 09:17:27 | [CVE-2026-35190](https://nvd.nist.gov/vuln/detail/CVE-2026-35190) |  |  | Issue summary: A server configured with the Suite B certificate flag through SSL_CTX_set_cert_flags() and with TLS 1.3… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
