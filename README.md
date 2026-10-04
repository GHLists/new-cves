# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-04 11:20 UTC

New CVEs published between 2026-10-04 10:19 UTC and 2026-10-04 11:20 UTC.

[Full CSV](data/new-cves-2026-10-04T11-20-14-404088Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-10-04 11:16:31 | [CVE-2026-105145](https://nvd.nist.gov/vuln/detail/CVE-2026-105145) | Medium | 5.5 | A vulnerability has been found in Weaviate Verba up to 2.1.3. Affected by this vulnerability is the function get_enviro… |
| 2026-10-04 11:16:32 | [CVE-2026-105146](https://nvd.nist.gov/vuln/detail/CVE-2026-105146) | Low | 2.0 | A vulnerability was found in Comsenz Discuz! X5.0-20260801/X5.0-20260820/X5.0-20260910. Affected by this issue is the f… |
| 2026-10-04 11:16:33 | [CVE-2026-97307](https://nvd.nist.gov/vuln/detail/CVE-2026-97307) | High | 7.5 | Insertion of Sensitive Information Into Sent Data vulnerability in StylemixThemes Cost Calculator Builder cost-calculat… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
