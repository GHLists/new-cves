# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-09-29 07:19 UTC

New CVEs published between 2026-09-29 06:19 UTC and 2026-09-29 07:19 UTC.

[Full CSV](data/new-cves-2026-09-29T07-19-04-785891Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-09-29 07:16:35 | [CVE-2026-86157](https://nvd.nist.gov/vuln/detail/CVE-2026-86157) | Medium | 5.6 | Exposure of privileged IPC functionality in Progress Telerik Fiddler Everywhere before version 8.2.0 allows a local, lo… |
| 2026-09-29 07:16:35 | [CVE-2026-86158](https://nvd.nist.gov/vuln/detail/CVE-2026-86158) | High | 7.7 | Missing authentication in the local .NET backend (Fiddler.WebUi) of Progress Software Fiddler Everywhere 8.0.2 allows a… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
