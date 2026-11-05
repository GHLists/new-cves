# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-11-05 09:18 UTC

New CVEs published between 2026-11-05 08:18 UTC and 2026-11-05 09:18 UTC.

[Full CSV](data/new-cves-2026-11-05T09-18-48-697247Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-11-05 09:17:04 | [CVE-2026-117679](https://nvd.nist.gov/vuln/detail/CVE-2026-117679) | Medium | 5.1 | A cross-site scripting vulnerability exists in SHIRASAGI, which may allow an authenticated attacker to execute arbitrar… |
| 2026-11-05 09:17:05 | [CVE-2026-118869](https://nvd.nist.gov/vuln/detail/CVE-2026-118869) | High | 8.7 | An OS command injection vulnerability exists in SHIRASAGI, which may allow an authenticated attacker to execute arbitra… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
