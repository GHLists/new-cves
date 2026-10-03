# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-03 09:19 UTC

New CVEs published between 2026-10-03 08:21 UTC and 2026-10-03 09:19 UTC.

[Full CSV](data/new-cves-2026-10-03T09-19-16-151028Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-10-03 09:17:04 | [CVE-2026-18040](https://nvd.nist.gov/vuln/detail/CVE-2026-18040) | Medium | 5.9 | In Bouncy Castle for Java before 1.86, HQC leaked secret-derived data through two side channels: its GF(2^8) arithmetic… |
| 2026-10-03 09:17:04 | [CVE-2026-71883](https://nvd.nist.gov/vuln/detail/CVE-2026-71883) | High | 8.2 | In Bouncy Castle for Java LTS before 2.73.13, the one-shot native packet ciphers for AES-CBC, CCM, CFB, CTR, GCM and GC… |
| 2026-10-03 09:17:04 | [CVE-2026-71885](https://nvd.nist.gov/vuln/detail/CVE-2026-71885) | Critical | 9.2 | In Bouncy Castle for Java before 1.86, the Messaging Layer Security (MLS, RFC 9420) implementation did not bind an X.50… |
| 2026-10-03 09:17:04 | [CVE-2026-71886](https://nvd.nist.gov/vuln/detail/CVE-2026-71886) | High | 8.2 | In Bouncy Castle for Java before 1.86, the high-level OpenPGP certificate API accepted a third-party certification or t… |
| 2026-10-03 09:17:05 | [CVE-2026-71887](https://nvd.nist.gov/vuln/detail/CVE-2026-71887) | High | 8.2 | In Bouncy Castle for Java before 1.86, the high-level OpenPGP API accepted a data signature made by a signing subkey wh… |
| 2026-10-03 09:17:05 | [CVE-2026-71888](https://nvd.nist.gov/vuln/detail/CVE-2026-71888) | High | 8.7 | In Bouncy Castle for Java before 1.86, the streaming CMS AuthenticatedData parser accepted a message whose digestAlgori… |
| 2026-10-03 09:17:05 | [CVE-2026-71889](https://nvd.nist.gov/vuln/detail/CVE-2026-71889) | High | 8.7 | In Bouncy Castle for Java before 1.86, neither copy of PKIXCertPathReviewer - org.bouncycastle.pkix.jcajce.PKIXCertPath… |
| 2026-10-03 09:17:05 | [CVE-2026-71890](https://nvd.nist.gov/vuln/detail/CVE-2026-71890) | High | 8.7 | In Bouncy Castle for Java before 1.86, validation of an MLS (RFC 9420) external commit's proposal list, org.bouncycastl… |
| 2026-10-03 09:17:05 | [CVE-2026-71891](https://nvd.nist.gov/vuln/detail/CVE-2026-71891) | High | 7.1 | In Bouncy Castle for Java before 1.86, BLS12_381BasicScheme.keyValidate, and so BLSPublicKeyParameters and every BasicS… |
| 2026-10-03 09:17:05 | [CVE-2026-71892](https://nvd.nist.gov/vuln/detail/CVE-2026-71892) | Medium | 6.9 | In Bouncy Castle for Java before 1.86, the opt-in key-size validation on CMS key-transport recipients, org.bouncycastle… |
| 2026-10-03 09:17:06 | [CVE-2026-85515](https://nvd.nist.gov/vuln/detail/CVE-2026-85515) | High | 8.2 | In Bouncy Castle for Java before 1.86, a truncated OpenPGP encrypted message was accepted with no error reported, and o… |
| 2026-10-03 09:17:06 | [CVE-2026-97873](https://nvd.nist.gov/vuln/detail/CVE-2026-97873) | Medium | 5.3 | In Bouncy Castle for Java before 1.86, the raw JCA provider's legacy PBES1 (PKCS#5 scheme 1) and PKCS#12 PBE families r… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
