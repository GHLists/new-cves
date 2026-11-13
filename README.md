# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-11-13 07:18 UTC

New CVEs published between 2026-11-13 06:19 UTC and 2026-11-13 07:18 UTC.

[Full CSV](data/new-cves-2026-11-13T07-18-37-717534Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-11-13 07:17:20 | [CVE-2026-128424](https://nvd.nist.gov/vuln/detail/CVE-2026-128424) | Medium | 5.3 | A flaw was found in Kroxylicious. The ACL authorizer's rules-file parser unquotes `matching /…/` regular-expression lit… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
