# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-04 22:18 UTC

New CVEs published between 2026-10-04 21:18 UTC and 2026-10-04 22:18 UTC.

[Full CSV](data/new-cves-2026-10-04T22-18-58-689149Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-10-04 22:16:58 | [CVE-2026-105163](https://nvd.nist.gov/vuln/detail/CVE-2026-105163) | Medium | 6.9 | A vulnerability was detected in crossplane crossplane-runtime up to 2.2.2/2.3.2. This vulnerability affects the functio… |
| 2026-10-04 22:16:59 | [CVE-2026-105164](https://nvd.nist.gov/vuln/detail/CVE-2026-105164) | Medium | 5.1 | A flaw has been found in NASA cFS up to 7.0.1. This issue affects the function CFE_FS_ParseInputFileNameEx of the file… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
