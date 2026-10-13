# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-13 11:20 UTC

New CVEs published between 2026-10-13 10:18 UTC and 2026-10-13 11:20 UTC.

[Full CSV](data/new-cves-2026-10-13T11-20-21-935484Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-10-13 11:17:14 | [CVE-2026-109153](https://nvd.nist.gov/vuln/detail/CVE-2026-109153) | Medium | 5.3 | A vulnerability was detected in MosaicML Composer up to 0.32.1. This affects the function tarball.extractall of the fil… |
| 2026-10-13 11:17:14 | [CVE-2026-109155](https://nvd.nist.gov/vuln/detail/CVE-2026-109155) | Medium | 5.3 | A flaw has been found in DeepPavlov up to 1.7.0. This impacts the function untar of the component Model Download Handle… |
| 2026-10-13 11:17:14 | [CVE-2026-109156](https://nvd.nist.gov/vuln/detail/CVE-2026-109156) | Medium | 5.3 | A vulnerability has been found in SeldonIO MLServer up to 1.6.1. Affected is the function _extract_env of the file mlse… |
| 2026-10-13 11:17:14 | [CVE-2026-109157](https://nvd.nist.gov/vuln/detail/CVE-2026-109157) | High | 8.6 | A vulnerability was found in TRENDnet TEW-432BRP 3.10B20. Affected by this vulnerability is the function formTcpipSetup… |
| 2026-10-13 11:17:15 | [CVE-2026-109160](https://nvd.nist.gov/vuln/detail/CVE-2026-109160) | Low | 2.1 | A vulnerability was determined in PublicCMS up to 5.202608.a. Affected by this issue is the function SafeConfigComponen… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
