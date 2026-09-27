# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-09-27 10:18 UTC

New CVEs published between 2026-09-27 09:19 UTC and 2026-09-27 10:18 UTC.

[Full CSV](data/new-cves-2026-09-27T10-18-54-192826Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-09-27 10:16:56 | [CVE-2026-15442](https://nvd.nist.gov/vuln/detail/CVE-2026-15442) | Low | 2.3 | In all builds that make use of (D)TLS, including default builds, there is a series of conditional states during the TLS… |
| 2026-09-27 10:16:58 | [CVE-2026-89102](https://nvd.nist.gov/vuln/detail/CVE-2026-89102) | High | 8.3 | In wolfSSL versions 5.7.2 through 5.9.2 there is a client-side implementation flaw in RFC 6961, multiple OCSP response… |
| 2026-09-27 10:16:58 | [CVE-2026-89133](https://nvd.nist.gov/vuln/detail/CVE-2026-89133) | Medium | 6.3 | wolfSSL versions 5.9.2 and earlier contain a flaw in the X.509 certificate validation logic where it fails to properly… |
| 2026-09-27 10:16:59 | [CVE-2026-89134](https://nvd.nist.gov/vuln/detail/CVE-2026-89134) | Medium | 6.3 | A certificate with no dNSName SAN but another SAN type present (e.g. registeredID or iPAddress) bypassed the Subject CN… |
| 2026-09-27 10:16:59 | [CVE-2026-89135](https://nvd.nist.gov/vuln/detail/CVE-2026-89135) | Medium | 6.3 | A failed X509_verify_cert call permanently plants an unverified attacker CA in the shared CertManager, bypassing certif… |
| 2026-09-27 10:16:59 | [CVE-2026-89136](https://nvd.nist.gov/vuln/detail/CVE-2026-89136) | High | 8.3 | When using RPK (Raw Public Key), the client side of a TLS 1.2, 1.3 and DTLS 1.2 connection could accept an unsolicited… |
| 2026-09-27 10:16:59 | [CVE-2026-93302](https://nvd.nist.gov/vuln/detail/CVE-2026-93302) | High | 8.3 | MatchTrustedPeer ignores the public key used, leading to forged CA clones passing verification. Affected builds are any… |
| 2026-09-27 10:16:59 | [CVE-2026-93304](https://nvd.nist.gov/vuln/detail/CVE-2026-93304) | Medium | 6.3 | A (D)TLS 1.2 client can accept a ChangeCipherSpec message before it has sent its ClientKeyExchange. No master secret ha… |
| 2026-09-27 10:16:59 | [CVE-2026-94417](https://nvd.nist.gov/vuln/detail/CVE-2026-94417) | Low | 2.3 | When an application enables both OCSP and CRL revocation checking on one WOLFSSL_CTX or certificate manager, wolfSSL sk… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
