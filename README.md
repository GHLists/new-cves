# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-11-09 16:18 UTC

New CVEs published between 2026-11-09 15:19 UTC and 2026-11-09 16:18 UTC.

[Full CSV](data/new-cves-2026-11-09T16-18-24-672257Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-11-09 16:17:23 | [CVE-2025-10248](https://nvd.nist.gov/vuln/detail/CVE-2025-10248) | High | 7.2 | XSS Vulnerability in OpenText Filr Appliance versions upto 25.1.2 could allow an authenticated user to upload a malicio… |
| 2026-11-09 16:17:26 | [CVE-2026-118492](https://nvd.nist.gov/vuln/detail/CVE-2026-118492) | Low | 2.0 | In Eclipse Langium versions 3.0.0 and later, the langium-sprotty package does not HTML-escape diagnostic messages befor… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
