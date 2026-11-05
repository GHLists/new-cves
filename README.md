# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-11-05 01:18 UTC

New CVEs published between 2026-11-05 00:21 UTC and 2026-11-05 01:18 UTC.

[Full CSV](data/new-cves-2026-11-05T01-18-43-041723Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-11-05 01:17:21 | [CVE-2026-109849](https://nvd.nist.gov/vuln/detail/CVE-2026-109849) | High | 7.1 | Incorrect privilege assignment issue exists in Hinemos. If this vulnerability is exploited, an attacker who can access… |
| 2026-11-05 01:17:21 | [CVE-2026-122052](https://nvd.nist.gov/vuln/detail/CVE-2026-122052) | Medium | 5.3 | A vulnerability has been found in laspy up to 2.7.0. Affected by this issue is some unknown functionality of the file l… |
| 2026-11-05 01:17:21 | [CVE-2026-122144](https://nvd.nist.gov/vuln/detail/CVE-2026-122144) | Low | 2.1 | A security flaw has been discovered in nliautaud pico-content-editor up to 02d5ad6c820c5050c542ab9505819b5e0a0ba1af. Th… |
| 2026-11-05 01:17:22 | [CVE-2026-122146](https://nvd.nist.gov/vuln/detail/CVE-2026-122146) | Medium | 5.5 | A weakness has been identified in 101arrowz fflate up to 0.8.3. This issue affects the function unzipSync of the file e… |
| 2026-11-05 01:17:22 | [CVE-2026-122151](https://nvd.nist.gov/vuln/detail/CVE-2026-122151) | Low | 2.1 | A security vulnerability has been detected in Presenton up to 0.9.11-beta. Impacted is the function JSON.parse of the f… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
