# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-11-07 17:19 UTC

New CVEs published between 2026-11-07 16:18 UTC and 2026-11-07 17:19 UTC.

[Full CSV](data/new-cves-2026-11-07T17-19-41-154903Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-11-07 17:16:34 | [CVE-2026-123990](https://nvd.nist.gov/vuln/detail/CVE-2026-123990) | Medium | 5.5 | A security vulnerability has been detected in DataEase up to 2.10.27/3.1.0. Affected is the function ExtWhere2Str.extWh… |
| 2026-11-07 17:16:34 | [CVE-2026-123991](https://nvd.nist.gov/vuln/detail/CVE-2026-123991) | Medium | 5.5 | A vulnerability was detected in DataEase up to 2.10.27. Affected by this vulnerability is the function WhitelistUtils.e… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
