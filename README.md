# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-19 21:20 UTC

New CVEs published between 2026-10-19 20:19 UTC and 2026-10-19 21:20 UTC.

[Full CSV](data/new-cves-2026-10-19T21-20-25-718271Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-10-19 20:20:03 | [CVE-2026-71169](https://nvd.nist.gov/vuln/detail/CVE-2026-71169) | High | 7.0 | Dell Application Store, versions prior to 26.05.0.7, contain an Incorrect Permission Assignment for Critical Resource v… |
| 2026-10-19 20:20:03 | [CVE-2026-71170](https://nvd.nist.gov/vuln/detail/CVE-2026-71170) | High | 7.8 | Dell Application Store, versions prior to 26.05.0.7, contains an Uncontrolled Path Element vulnerability. A low privile… |
| 2026-10-19 20:20:06 | [CVE-2026-82166](https://nvd.nist.gov/vuln/detail/CVE-2026-82166) | High | 8.8 | Dell Application Store, versions prior to 26.05.0.7, contain a Missing Authentication for Critical Function vulnerabili… |
| 2026-10-19 21:17:06 | [CVE-2026-111946](https://nvd.nist.gov/vuln/detail/CVE-2026-111946) |  |  | Plack::Middleware::ETag versions from 0.04 before 0.06 for Perl disclose file inode numbers in the default ETag header.… |
| 2026-10-19 21:17:06 | [CVE-2026-112299](https://nvd.nist.gov/vuln/detail/CVE-2026-112299) | Low | 2.1 | A vulnerability was determined in smrealms smr up to f40380c017bc35cd8db6ffdb9d4e78bf65b9d43d. Affected is the function… |
| 2026-10-19 21:17:06 | [CVE-2026-112300](https://nvd.nist.gov/vuln/detail/CVE-2026-112300) | Medium | 6.9 | A vulnerability was identified in DiffSK configobj up to 5.0.9. Affected by this vulnerability is the function _section… |
| 2026-10-19 21:17:06 | [CVE-2026-112301](https://nvd.nist.gov/vuln/detail/CVE-2026-112301) | Medium | 5.5 | A security flaw has been discovered in orbitale imagemagick-php up to 3.3.5. Affected by this issue is the function Com… |
| 2026-10-19 21:17:07 | [CVE-2026-112302](https://nvd.nist.gov/vuln/detail/CVE-2026-112302) | Low | 2.1 | A weakness has been identified in kiwilan php-archive up to 2.3.02. This affects the function ArchiveZip::extract of th… |
| 2026-10-19 21:17:07 | [CVE-2026-112390](https://nvd.nist.gov/vuln/detail/CVE-2026-112390) | High | 8.2 | Pillow is a Python imaging library. From 7.2.0 until 13.0.0, Pillow can enter an infinite loop while determining the fr… |
| 2026-10-19 21:17:07 | [CVE-2026-112391](https://nvd.nist.gov/vuln/detail/CVE-2026-112391) | Medium | 6.3 | Pillow is a Python imaging library. From 5.1.0 until 13.0.0, Pillow's PdfParser.get_value() can recurse without a limit… |
| 2026-10-19 21:17:07 | [CVE-2026-112393](https://nvd.nist.gov/vuln/detail/CVE-2026-112393) | Critical | 9.2 | Pillow is a Python imaging library. From 2.0.0 until 13.0.0, Pillow has a heap buffer overflow and stale-heap disclosur… |
| 2026-10-19 21:17:07 | [CVE-2026-112394](https://nvd.nist.gov/vuln/detail/CVE-2026-112394) | Medium | 6.3 | Pillow is a Python imaging library. Prior to 13.0.0, Pillow's P;2L and P;4L raw decoders can read past the end of an in… |
| 2026-10-19 21:17:07 | [CVE-2026-112395](https://nvd.nist.gov/vuln/detail/CVE-2026-112395) | Medium | 6.5 | Pillow is a Python imaging library. From 8.2.0 until 13.0.0, Pillow's tiled-TIFF decoder can read past the tile buffer… |
| 2026-10-19 21:18:01 | [CVE-2026-76787](https://nvd.nist.gov/vuln/detail/CVE-2026-76787) | Medium | 5.9 | The UpdateHub firmware-over-the-air client parses the CoAP probe response with Zephyr's JSON library in z_impl_updatehu… |
| 2026-10-19 21:18:01 | [CVE-2026-76788](https://nvd.nist.gov/vuln/detail/CVE-2026-76788) | High | 8.8 | The OSDP Control Panel reply parser cp_decode_response() in subsys/mgmt/osdp/src/osdp_cp.c decodes replies from a Perip… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
