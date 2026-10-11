# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-11 11:18 UTC

New CVEs published between 2026-10-11 10:19 UTC and 2026-10-11 11:18 UTC.

[Full CSV](data/new-cves-2026-10-11T11-18-35-606803Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-10-11 11:16:58 | [CVE-2026-108569](https://nvd.nist.gov/vuln/detail/CVE-2026-108569) | Low | 2.1 | A vulnerability was identified in Furion .NET Framework up to 4.9.9.92. The impacted element is the function String.Rep… |
| 2026-10-11 11:16:59 | [CVE-2026-108570](https://nvd.nist.gov/vuln/detail/CVE-2026-108570) | Low | 2.1 | A security flaw has been discovered in Furion .NET Framework up to 4.9.9.95. This affects the function RunCompile of th… |
| 2026-10-11 11:17:00 | [CVE-2026-108571](https://nvd.nist.gov/vuln/detail/CVE-2026-108571) | Medium | 5.5 | A weakness has been identified in Xinhu Rainrock RockOA up to 2.7.6. This impacts the function kqjcmdModel::returnchuli… |
| 2026-10-11 11:17:00 | [CVE-2026-108572](https://nvd.nist.gov/vuln/detail/CVE-2026-108572) | Low | 2.1 | A security vulnerability has been detected in Casdoor up to 3.164.0/4.10.0. Affected is the function CasP3ProxyValidate… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
