# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-11-14 18:18 UTC

New CVEs published between 2026-11-14 17:19 UTC and 2026-11-14 18:18 UTC.

[Full CSV](data/new-cves-2026-11-14T18-18-23-784082Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-11-14 18:17:20 | [CVE-2026-129267](https://nvd.nist.gov/vuln/detail/CVE-2026-129267) | Low | 2.0 | A vulnerability was found in sergix44 XBackBone up to 3.8.2. Impacted is the function MediaController::getRawById of th… |
| 2026-11-14 18:17:21 | [CVE-2026-129447](https://nvd.nist.gov/vuln/detail/CVE-2026-129447) | Medium | 5.3 | Kroki before 0.36.0 contains a reflected cross-site scripting vulnerability in the /dbml/svg endpoint that allows unaut… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
