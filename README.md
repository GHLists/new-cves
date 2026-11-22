# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-11-22 01:18 UTC

New CVEs published between 2026-11-22 00:21 UTC and 2026-11-22 01:18 UTC.

[Full CSV](data/new-cves-2026-11-22T01-18-23-78344Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-11-22 01:16:52 | [CVE-2026-134553](https://nvd.nist.gov/vuln/detail/CVE-2026-134553) | Medium | 5.3 | A vulnerability was determined in wiroai Wiro-MCP up to 1.3.0. This affects the function upload_file of the file src/to… |
| 2026-11-22 01:16:53 | [CVE-2026-134560](https://nvd.nist.gov/vuln/detail/CVE-2026-134560) | Medium | 4.8 | A weakness has been identified in twogood unshield up to 1.6.2. Impacted is the function unshield_get_cab_descriptor of… |
| 2026-11-22 01:16:53 | [CVE-2026-134566](https://nvd.nist.gov/vuln/detail/CVE-2026-134566) | Low | 2.1 | A security vulnerability has been detected in itsourcecode Document Management System 1.0. The affected element is an u… |
| 2026-11-22 01:16:53 | [CVE-2026-134567](https://nvd.nist.gov/vuln/detail/CVE-2026-134567) | Low | 2.1 | A vulnerability was detected in itsourcecode Document Management System 1.0. The impacted element is an unknown functio… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
