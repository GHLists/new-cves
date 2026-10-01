# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-01 01:18 UTC

New CVEs published between 2026-10-01 00:22 UTC and 2026-10-01 01:18 UTC.

[Full CSV](data/new-cves-2026-10-01T01-18-56-490834Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-10-01 01:16:35 | [CVE-2026-103531](https://nvd.nist.gov/vuln/detail/CVE-2026-103531) | Medium | 5.1 | A flaw has been found in OpenSC up to 0.27.1. The impacted element is the function setcos_construct_fci_44 of the file… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
