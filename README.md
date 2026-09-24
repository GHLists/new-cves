# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-09-24 21:18 UTC

New CVEs published between 2026-09-24 20:20 UTC and 2026-09-24 21:18 UTC.

[Full CSV](data/new-cves-2026-09-24T21-18-58-007543Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-09-24 21:17:10 | [CVE-2026-14441](https://nvd.nist.gov/vuln/detail/CVE-2026-14441) | Medium | 6.9 | A logic flaw in Java cache key handling object comparison handling could lead to improper identifier resolution when pr… |
| 2026-09-24 21:17:11 | [CVE-2026-14442](https://nvd.nist.gov/vuln/detail/CVE-2026-14442) | Medium | 6.9 | An information exposure vulnerability in the job scheduling component of SANnav allows sensitive credentials to be writ… |
| 2026-09-24 21:17:12 | [CVE-2026-14443](https://nvd.nist.gov/vuln/detail/CVE-2026-14443) | High | 8.4 | Incomplete log sanitization during bulk IPsec policy collection in Brocade SANnav versions before 3.0.1a permit extensi… |
| 2026-09-24 21:18:36 | [CVE-2026-75558](https://nvd.nist.gov/vuln/detail/CVE-2026-75558) | Medium | 6.0 | The Botslab G980H dash camera firmware uses a hard-coded cryptographic key and initialization vector to protect WiFi cr… |
| 2026-09-24 21:18:44 | [CVE-2026-79959](https://nvd.nist.gov/vuln/detail/CVE-2026-79959) | High | 7.0 | The Botslab G980H dash camera firmware contains a hard-coded root account password that cannot be changed by the user.… |
| 2026-09-24 21:18:48 | [CVE-2026-81630](https://nvd.nist.gov/vuln/detail/CVE-2026-81630) | Critical | 9.2 | The Botslab G980H dash camera firmware does not adequately verify the authenticity of firmware updates. The update proc… |
| 2026-09-24 21:18:50 | [CVE-2026-82585](https://nvd.nist.gov/vuln/detail/CVE-2026-82585) | High | 7.1 | The Botslab G980H dash camera firmware transmits sensitive information over unencrypted HTTP and RTSP connections. An a… |
| 2026-09-24 21:18:50 | [CVE-2026-82708](https://nvd.nist.gov/vuln/detail/CVE-2026-82708) | High | 7.1 | The Botslab G980H dash camera firmware contains a path traversal vulnerability in its HTTP server. An attacker with acc… |
| 2026-09-24 21:18:50 | [CVE-2026-82716](https://nvd.nist.gov/vuln/detail/CVE-2026-82716) | Medium | 5.1 | The Botslab G980H dash camera firmware includes sensitive configuration information, including WiFi credentials, in dia… |
| 2026-09-24 21:18:55 | [CVE-2026-84403](https://nvd.nist.gov/vuln/detail/CVE-2026-84403) | Medium | 6.9 | The Botslab G980H dash camera firmware does not require authenticated pairing or client binding before permitting acces… |
| 2026-09-24 21:18:56 | [CVE-2026-87118](https://nvd.nist.gov/vuln/detail/CVE-2026-87118) | Medium | 6.9 | The Botslab G980H dash camera firmware contains an out of bounds write vulnerability in its command processing function… |
| 2026-09-24 21:18:57 | [CVE-2026-88386](https://nvd.nist.gov/vuln/detail/CVE-2026-88386) |  |  | libsndfile 1.2.2 contains a misaligned memory access issue in psf_binheader_readf() while parsing WAV fmt chunks. A spe… |
| 2026-09-24 21:18:57 | [CVE-2026-88387](https://nvd.nist.gov/vuln/detail/CVE-2026-88387) |  |  | LibRaw 0.22.0 contains an incorrect numeric conversion vulnerability in LibRaw::parse_tiff_ifd() when processing TIFF t… |
| 2026-09-24 21:18:57 | [CVE-2026-88388](https://nvd.nist.gov/vuln/detail/CVE-2026-88388) |  |  | Espruino 2v29 (commit bffc6d0) contains a stack-based buffer overflow vulnerability in the JavaScript error stack-trace… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
