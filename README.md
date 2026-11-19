# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-11-19 02:19 UTC

New CVEs published between 2026-11-19 01:19 UTC and 2026-11-19 02:19 UTC.

[Full CSV](data/new-cves-2026-11-19T02-19-22-277319Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-11-19 02:17:20 | [CVE-2026-131914](https://nvd.nist.gov/vuln/detail/CVE-2026-131914) | Critical | 9.3 | Deserialization of untrusted data in double-submit cookie vs. form field validation in Idunno.AntiCsrf versions through… |
| 2026-11-19 02:17:20 | [CVE-2026-132601](https://nvd.nist.gov/vuln/detail/CVE-2026-132601) | Low | 2.1 | A security vulnerability has been detected in SEO Panel 6.0.0. This affects the function mime_content_type of the file… |
| 2026-11-19 02:17:20 | [CVE-2026-132602](https://nvd.nist.gov/vuln/detail/CVE-2026-132602) | Low | 2.1 | A vulnerability was detected in SEO Panel 6.0.0. This impacts an unknown function of the file controllers/siteauditor.c… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
