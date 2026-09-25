# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-09-25 10:19 UTC

New CVEs published between 2026-09-25 09:19 UTC and 2026-09-25 10:19 UTC.

[Full CSV](data/new-cves-2026-09-25T10-19-13-467853Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-09-25 10:17:08 | [CVE-2026-92106](https://nvd.nist.gov/vuln/detail/CVE-2026-92106) | Low | 2.3 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in dashbitco lazy_ht… |
| 2026-09-25 10:17:08 | [CVE-2026-97898](https://nvd.nist.gov/vuln/detail/CVE-2026-97898) | High | 8.4 | Insecure Direct Object Reference / missing object-level authorization in the Akia keyless entry cloud service. The unlo… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
