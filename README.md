# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-09-28 06:18 UTC

New CVEs published between 2026-09-28 05:19 UTC and 2026-09-28 06:18 UTC.

[Full CSV](data/new-cves-2026-09-28T06-18-52-664321Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-09-28 06:16:29 | [CVE-2026-101002](https://nvd.nist.gov/vuln/detail/CVE-2026-101002) | High | 8.6 | A security flaw has been discovered in Netcore NBR200V2 1.3.241127.071246. Affected is the function system of the file… |
| 2026-09-28 06:16:31 | [CVE-2026-101003](https://nvd.nist.gov/vuln/detail/CVE-2026-101003) | Medium | 5.5 | A weakness has been identified in Cesanta Mongoose up to 7.21. Affected by this vulnerability is the function fn of the… |
| 2026-09-28 06:16:31 | [CVE-2026-101004](https://nvd.nist.gov/vuln/detail/CVE-2026-101004) | Medium | 6.9 | A security vulnerability has been detected in notionnext-org NotionNext up to 4.10.10. Affected by this issue is the fu… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
