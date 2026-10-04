# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-04 13:20 UTC

New CVEs published between 2026-10-04 12:20 UTC and 2026-10-04 13:20 UTC.

[Full CSV](data/new-cves-2026-10-04T13-20-10-553199Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-10-04 13:16:54 | [CVE-2026-105147](https://nvd.nist.gov/vuln/detail/CVE-2026-105147) | Medium | 5.5 | A vulnerability was determined in SciPhi-AI R2R up to 3.6.6. This affects an unknown part of the component JWT Secret H… |
| 2026-10-04 13:16:55 | [CVE-2026-105148](https://nvd.nist.gov/vuln/detail/CVE-2026-105148) | Medium | 5.5 | A vulnerability was identified in SciPhi-AI R2R up to 3.6.6. This vulnerability affects unknown code of the file py/sha… |
| 2026-10-04 13:16:55 | [CVE-2026-105149](https://nvd.nist.gov/vuln/detail/CVE-2026-105149) | Medium | 5.5 | A security flaw has been discovered in mooSocial up to 3.2.4. This issue affects some unknown processing of the file /s… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
