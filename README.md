# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-11-25 00:18 UTC

New CVEs published between 2026-11-24 23:20 UTC and 2026-11-25 00:18 UTC.

[Full CSV](data/new-cves-2026-11-25T00-18-50-503718Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-11-25 00:17:10 | [CVE-2026-133459](https://nvd.nist.gov/vuln/detail/CVE-2026-133459) | Medium | 5.3 | AutoGPT is a workflow automation platform for creating, deploying, and managing continuous artificial intelligence agen… |
| 2026-11-25 00:17:10 | [CVE-2026-133462](https://nvd.nist.gov/vuln/detail/CVE-2026-133462) | High | 8.7 | AutoGPT is a workflow automation platform for creating, deploying, and managing continuous artificial intelligence agen… |
| 2026-11-25 00:17:10 | [CVE-2026-136136](https://nvd.nist.gov/vuln/detail/CVE-2026-136136) | Critical | 9.3 | A vulnerability was identified in Netis WF2409E up to 20261026. Affected by this issue is some unknown functionality of… |
| 2026-11-25 00:17:10 | [CVE-2026-136139](https://nvd.nist.gov/vuln/detail/CVE-2026-136139) | Low | 2.1 | A vulnerability was determined in Zefan-Cai R-KV up to 6715468b9872442be72e5c97322e4d9c9a2abf55. This impacts the funct… |
| 2026-11-25 00:17:10 | [CVE-2026-136141](https://nvd.nist.gov/vuln/detail/CVE-2026-136141) | Low | 2.1 | A vulnerability was identified in Backdrop CMS up to 1.35.2. Affected is the function get_argument of the file core/mod… |
| 2026-11-25 00:17:11 | [CVE-2026-16666](https://nvd.nist.gov/vuln/detail/CVE-2026-16666) | Medium | 5.7 | When MCUboot resumes an interrupted image swap it takes the number of bytes to move straight from the flash-resident st… |
| 2026-11-25 00:17:11 | [CVE-2026-16667](https://nvd.nist.gov/vuln/detail/CVE-2026-16667) | Medium | 6.2 | The Cypress/PSoC6 flash-map backend in boot/cypress/cy_flash_pal/cy_flash_map.c guards every flash access with assert()… |
| 2026-11-25 00:17:11 | [CVE-2026-16669](https://nvd.nist.gov/vuln/detail/CVE-2026-16669) | Low | 2.0 | MCUboot's Espressif port omits zeroization of two sensitive stack buffers in boot/espressif/hal/src/flash_encrypt.c. In… |
| 2026-11-25 00:17:12 | [CVE-2026-16670](https://nvd.nist.gov/vuln/detail/CVE-2026-16670) | Medium | 4.0 | MCUboot's PSA-crypto ECDSA adapter parses the RFC 5480 DER signature with parse_signature_from_rfc5480_encoding() in bo… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
