# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-11 19:18 UTC

New CVEs published between 2026-10-11 18:19 UTC and 2026-10-11 19:18 UTC.

[Full CSV](data/new-cves-2026-10-11T19-18-31-634925Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-10-11 19:16:32 | [CVE-2026-108768](https://nvd.nist.gov/vuln/detail/CVE-2026-108768) | Low | 2.1 | A vulnerability was identified in zhayujie CowAgent up to 2.2.0. Affected by this issue is the function json.loads of t… |
| 2026-10-11 19:16:33 | [CVE-2026-108925](https://nvd.nist.gov/vuln/detail/CVE-2026-108925) | Medium | 6.1 | Improper neutralization of Script-Related HTML tags in a web page (basic XSS) vulnerability in Cohesity NetBackup Admin… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
