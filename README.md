# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-11-19 01:19 UTC

New CVEs published between 2026-11-19 00:21 UTC and 2026-11-19 01:19 UTC.

[Full CSV](data/new-cves-2026-11-19T01-19-00-134262Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-11-19 01:16:49 | [CVE-2026-132286](https://nvd.nist.gov/vuln/detail/CVE-2026-132286) | Medium | 5.5 | A security vulnerability has been detected in yangzongzhuan RuoYi up to 4.8.3. The impacted element is an unknown funct… |
| 2026-11-19 01:16:49 | [CVE-2026-132560](https://nvd.nist.gov/vuln/detail/CVE-2026-132560) | Low | 1.9 | A flaw has been found in MemTensor memmy-agent up to 1.1.1. This impacts an unknown function of the file /api/v1/memory… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
