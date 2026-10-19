# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-19 00:18 UTC

New CVEs published between 2026-10-18 23:20 UTC and 2026-10-19 00:18 UTC.

[Full CSV](data/new-cves-2026-10-19T00-18-54-078284Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-10-19 00:16:30 | [CVE-2026-112030](https://nvd.nist.gov/vuln/detail/CVE-2026-112030) | Low | 2.1 | A vulnerability was found in diem-project diem up to 5.1.3. This vulnerability affects unknown code of the file dmCoreP… |
| 2026-10-19 00:16:31 | [CVE-2026-112031](https://nvd.nist.gov/vuln/detail/CVE-2026-112031) | Low | 2.0 | A vulnerability was determined in Chamilo LMS up to 1.11.40/2.0.3/3.0.1. This issue affects the function TicketManager:… |
| 2026-10-19 00:16:31 | [CVE-2026-112032](https://nvd.nist.gov/vuln/detail/CVE-2026-112032) | Low | 2.0 | A vulnerability was identified in aircheng-org iWebShop-5 up to 5.16. Impacted is the function Util::search of the file… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
