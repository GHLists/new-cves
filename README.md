# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-09-24 14:21 UTC

New CVEs published between 2026-09-24 13:19 UTC and 2026-09-24 14:21 UTC.

[Full CSV](data/new-cves-2026-09-24T14-21-20-746327Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-09-24 14:17:11 | [CVE-2026-17413](https://nvd.nist.gov/vuln/detail/CVE-2026-17413) | Medium | 5.1 | IBM PowerVM Hypervisor FW1120.00 through FW1120.01, FW1110.00 through FW1110.31, FW1060.00 through FW1060.81, and FW950… |
| 2026-09-24 14:17:12 | [CVE-2026-17503](https://nvd.nist.gov/vuln/detail/CVE-2026-17503) | Medium | 5.1 | IBM PowerVM Hypervisor FW1120.00 through FW1120.01, FW1110.00 through FW1110.31, FW1060.00 through FW1060.81, and FW950… |
| 2026-09-24 14:17:12 | [CVE-2026-17504](https://nvd.nist.gov/vuln/detail/CVE-2026-17504) | Medium | 5.1 | IBM PowerVM Hypervisor FW1120.00 through FW1120.01, FW1110.00 through FW1110.31, FW1060.00 through FW1060.81, and FW950… |
| 2026-09-24 14:17:12 | [CVE-2026-17511](https://nvd.nist.gov/vuln/detail/CVE-2026-17511) | Low | 3.4 | IBM PowerVM Hypervisor FW1120.00 through FW1120.01, FW1110.00 through FW1110.31, FW1060.00 through FW1060.81, and FW950… |
| 2026-09-24 14:17:12 | [CVE-2026-18104](https://nvd.nist.gov/vuln/detail/CVE-2026-18104) | Low | 3.3 | IBM Db2 Mirror for i 7.6, 7.5, and 7.4 could allow a local attacker to obtain sensitive information due to the use of t… |
| 2026-09-24 14:17:12 | [CVE-2026-18857](https://nvd.nist.gov/vuln/detail/CVE-2026-18857) | Low | 3.4 | IBM OPENBMC FW1120.00 through FW1120.01, FW1110.00 through FW1110.31, and FW1060.00 through FW1060.81 is affected by a… |
| 2026-09-24 14:18:17 | [CVE-2026-77797](https://nvd.nist.gov/vuln/detail/CVE-2026-77797) | Low | 3.6 | Velociraptor's prefetch library contains an out of bound vulnerability which may cause a crash when parsing certain mal… |
| 2026-09-24 14:18:17 | [CVE-2026-77798](https://nvd.nist.gov/vuln/detail/CVE-2026-77798) | Medium | 6.5 | Velociraptor contains a deadlock condition that may be triggered by authenticated users. The issue stems from a lock ma… |
| 2026-09-24 14:18:18 | [CVE-2026-88359](https://nvd.nist.gov/vuln/detail/CVE-2026-88359) |  |  | libfyaml 0.9.6 contains a stack exhaustion vulnerability in fy_atom_iter_format(). When processing a specially crafted… |
| 2026-09-24 14:18:18 | [CVE-2026-88360](https://nvd.nist.gov/vuln/detail/CVE-2026-88360) |  |  | libvips 8.19.0 contains a memory access vulnerability when processing little-endian PFM images. If the PFM text header… |
| 2026-09-24 14:18:18 | [CVE-2026-91187](https://nvd.nist.gov/vuln/detail/CVE-2026-91187) | Critical | 9.3 | Improper Verification of Cryptographic Signature vulnerability in dashbit nimble_zta allows an unauthenticated remote a… |
| 2026-09-24 14:18:20 | [CVE-2026-95519](https://nvd.nist.gov/vuln/detail/CVE-2026-95519) | High | 7.8 | A flaw was found in rpm. An attacker can supply a crafted manifest file that, when processed by a user or automation us… |
| 2026-09-24 14:18:20 | [CVE-2026-95521](https://nvd.nist.gov/vuln/detail/CVE-2026-95521) | High | 7.8 | A command injection flaw was found in rpm. Installing or rebuilding a source RPM whose source or spec file basenames co… |
| 2026-09-24 14:18:21 | [CVE-2026-97057](https://nvd.nist.gov/vuln/detail/CVE-2026-97057) | High | 8.7 | redis-parser through 3.0.0 fails to validate the multi-bulk length value in RESP protocol parsing, allowing attackers t… |
| 2026-09-24 14:18:21 | [CVE-2026-97058](https://nvd.nist.gov/vuln/detail/CVE-2026-97058) | Medium | 6.9 | sprintf-js through 1.1.3 passes unbounded precision specifiers to toFixed, toExponential, and toPrecision methods witho… |
| 2026-09-24 14:18:21 | [CVE-2026-97059](https://nvd.nist.gov/vuln/detail/CVE-2026-97059) | High | 8.8 | DCMTK through 3.7.0 contains a heap over-read vulnerability in ConcatenationLoader that copies pixel data frames withou… |
| 2026-09-24 14:18:22 | [CVE-2026-97061](https://nvd.nist.gov/vuln/detail/CVE-2026-97061) | Medium | 5.3 | Black Candy through 3.2.1 fails to scope playlist search queries to the authenticated session user, allowing any authen… |
| 2026-09-24 14:18:22 | [CVE-2026-97062](https://nvd.nist.gov/vuln/detail/CVE-2026-97062) | Medium | 5.1 | Aureus ERP through 1.6.0 stores uploaded SVG files on its public disk and serves them from the application origin, allo… |
| 2026-09-24 14:18:22 | [CVE-2026-97359](https://nvd.nist.gov/vuln/detail/CVE-2026-97359) | Critical | 10.0 | HFS2 version 2.4.0 and earlier contains a template injection vulnerability in the multipart upload handler that allows… |
| 2026-09-24 14:18:22 | [CVE-2026-97360](https://nvd.nist.gov/vuln/detail/CVE-2026-97360) | Critical | 10.0 | HFS2 version 2.4.0 and earlier contains an unauthenticated arbitrary file access vulnerability that allows unauthentica… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
