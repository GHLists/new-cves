# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-11 05:20 UTC

New CVEs published between 2026-10-11 04:19 UTC and 2026-10-11 05:20 UTC.

[Full CSV](data/new-cves-2026-10-11T05-20-19-082587Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-10-11 05:16:52 | [CVE-2026-108523](https://nvd.nist.gov/vuln/detail/CVE-2026-108523) | Low | 2.1 | A vulnerability was determined in Studio-Saelix Sencho up to 0.94.1. This vulnerability affects unknown code of the fil… |
| 2026-10-11 05:16:53 | [CVE-2026-108538](https://nvd.nist.gov/vuln/detail/CVE-2026-108538) | Low | 2.1 | A security vulnerability has been detected in GPAC up to 26.07.0. The impacted element is the function gf_mx_v of the f… |
| 2026-10-11 05:16:53 | [CVE-2026-108539](https://nvd.nist.gov/vuln/detail/CVE-2026-108539) | Low | 2.1 | A vulnerability was detected in GPAC up to 26.07.0. This affects the function gf_fq_pop of the file filter_core/filter_… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
