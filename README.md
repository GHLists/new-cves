# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-16 21:19 UTC

New CVEs published between 2026-10-16 20:18 UTC and 2026-10-16 21:19 UTC.

[Full CSV](data/new-cves-2026-10-16T21-19-46-623335Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-10-16 21:17:19 | [CVE-2026-108373](https://nvd.nist.gov/vuln/detail/CVE-2026-108373) | Medium | 6.5 | ERPNext is a free and open source Enterprise Resource Planning tool. Prior to 15.118.0 and 16.27.0, certain endpoints i… |
| 2026-10-16 21:17:19 | [CVE-2026-108374](https://nvd.nist.gov/vuln/detail/CVE-2026-108374) | High | 7.7 | ERPNext is a free and open source Enterprise Resource Planning tool. Prior to 15.121.0 and 16.34.0, certain endpoints f… |
| 2026-10-16 21:19:18 | [CVE-2026-55796](https://nvd.nist.gov/vuln/detail/CVE-2026-55796) | Medium | 6.5 | Frappe HR is an open-source human resources management solution (HRMS). Prior to 15.60.3 and 16.7.1, the Salary Payment… |
| 2026-10-16 21:19:19 | [CVE-2026-64862](https://nvd.nist.gov/vuln/detail/CVE-2026-64862) | Medium | 6.5 | Frappe HR is an open-source human resources management solution (HRMS). Prior to 15.58.3 and 16.4.3, HRMS PWA API endpo… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
