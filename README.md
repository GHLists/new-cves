# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-11-01 01:19 UTC

New CVEs published between 2026-11-01 00:18 UTC and 2026-11-01 01:19 UTC.

[Full CSV](data/new-cves-2026-11-01T01-19-30-76056Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-11-01 01:17:16 | [CVE-2026-120189](https://nvd.nist.gov/vuln/detail/CVE-2026-120189) | Critical | 9.3 | A vulnerability was identified in D-Link DIR-505 1.10B02. Affected is the function save_upload_file/mp_upload_file of t… |
| 2026-11-01 01:17:17 | [CVE-2026-120190](https://nvd.nist.gov/vuln/detail/CVE-2026-120190) | Low | 2.0 | A security flaw has been discovered in PostyBirb Plus up to 3.1.75. Affected by this vulnerability is an unknown functi… |
| 2026-11-01 01:17:17 | [CVE-2026-120191](https://nvd.nist.gov/vuln/detail/CVE-2026-120191) | Medium | 5.5 | A weakness has been identified in Presenton up to 0.9.11-beta. Affected by this issue is some unknown functionality of… |
| 2026-11-01 01:17:17 | [CVE-2026-120243](https://nvd.nist.gov/vuln/detail/CVE-2026-120243) | Medium | 6.8 | FFmpeg 2.0 through 9.0.2 contains a use of uninitialized variable vulnerability in the Go2Meeting decoder that allows a… |
| 2026-11-01 01:17:17 | [CVE-2026-120244](https://nvd.nist.gov/vuln/detail/CVE-2026-120244) | Medium | 6.8 | FFmpeg 2.1 through 9.0.2 contains a use of uninitialized resource vulnerability in the PCX decoder that allows attacker… |
| 2026-11-01 01:17:17 | [CVE-2026-120245](https://nvd.nist.gov/vuln/detail/CVE-2026-120245) | Medium | 6.8 | FFmpeg 0.10 through 9.0.2 contains a use of uninitialized resource vulnerability in sunrast_decode_frame() that leaks h… |
| 2026-11-01 01:17:18 | [CVE-2026-120246](https://nvd.nist.gov/vuln/detail/CVE-2026-120246) | Medium | 6.8 | FFmpeg 4.4 through 9.0.2 contains a use of uninitialized variable vulnerability in the CDXL decoder that leaks stack me… |
| 2026-11-01 01:17:18 | [CVE-2026-120247](https://nvd.nist.gov/vuln/detail/CVE-2026-120247) | Medium | 6.8 | FFmpeg 2.3 through 9.0.2 contains a use of uninitialized resource vulnerability in the Huffyuv decoder that allows atta… |
| 2026-11-01 01:17:18 | [CVE-2026-120248](https://nvd.nist.gov/vuln/detail/CVE-2026-120248) | Medium | 4.6 | Thelia before 3.1.1 contains a stored cross-site scripting vulnerability that allows authenticated back-office administ… |
| 2026-11-01 01:17:18 | [CVE-2026-120249](https://nvd.nist.gov/vuln/detail/CVE-2026-120249) | Medium | 6.9 | Thelia Back-office Default Twig Template before 1.1.1 contains a cross-site request forgery vulnerability in the /admin… |
| 2026-11-01 01:17:18 | [CVE-2026-120250](https://nvd.nist.gov/vuln/detail/CVE-2026-120250) | Medium | 6.0 | OpenAlgo 1.0.0.29 before 2.0.3.1 contains an improper certificate validation vulnerability in utils/email_utils.py and… |
| 2026-11-01 01:17:19 | [CVE-2026-120251](https://nvd.nist.gov/vuln/detail/CVE-2026-120251) | Medium | 6.8 | imagecodecs 2026.3.6 through 2026.10.10 contains an infinite loop vulnerability in ccitt_fax4_decode_size() that allows… |
| 2026-11-01 01:17:19 | [CVE-2026-120252](https://nvd.nist.gov/vuln/detail/CVE-2026-120252) | Medium | 6.8 | imagecodecs 2023.1.23 through 2026.10.10 contains a stack-based buffer overflow vulnerability in the lossless JPEG Defi… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
