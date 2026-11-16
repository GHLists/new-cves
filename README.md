# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-11-16 04:18 UTC

New CVEs published between 2026-11-16 03:20 UTC and 2026-11-16 04:18 UTC.

[Full CSV](data/new-cves-2026-11-16T04-18-50-783885Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-11-16 04:16:44 | [CVE-2026-107520](https://nvd.nist.gov/vuln/detail/CVE-2026-107520) | Medium | 5.4 | Dell PowerStore contains a stored cross-site scripting (XSS) vulnerability. A low-privileged authenticated attacker cou… |
| 2026-11-16 04:16:44 | [CVE-2026-82156](https://nvd.nist.gov/vuln/detail/CVE-2026-82156) | High | 8.8 | Dell PowerStore contains an authorization-bypass vulnerability. A low-privileged attacker could exploit it, potentially… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
