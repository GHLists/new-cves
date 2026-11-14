# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-11-14 11:18 UTC

New CVEs published between 2026-11-14 10:18 UTC and 2026-11-14 11:18 UTC.

[Full CSV](data/new-cves-2026-11-14T11-18-18-237777Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-11-14 11:17:06 | [CVE-2026-129247](https://nvd.nist.gov/vuln/detail/CVE-2026-129247) | Medium | 5.1 | A security flaw has been discovered in yangzongzhuan RuoYi up to 4.8.3. Impacted is the function VelocityUtils.getFileN… |
| 2026-11-14 11:17:07 | [CVE-2026-129248](https://nvd.nist.gov/vuln/detail/CVE-2026-129248) | Medium | 5.3 | A weakness has been identified in Akaunting up to 3.3.0. The affected element is the function calculation_to_quantity o… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
