# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-11-06 05:18 UTC

New CVEs published between 2026-11-06 04:18 UTC and 2026-11-06 05:18 UTC.

[Full CSV](data/new-cves-2026-11-06T05-18-42-907005Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-11-06 05:18:20 | [CVE-2026-114366](https://nvd.nist.gov/vuln/detail/CVE-2026-114366) | Low | 2.3 | An information disclosure vulnerability in the Qt Framework QWebSocket authentication handling of the Qt WebSockets mod… |
| 2026-11-06 05:18:20 | [CVE-2026-119431](https://nvd.nist.gov/vuln/detail/CVE-2026-119431) | High | 7.7 | A server-side request forgery (SSRF) vulnerability exists in Foxit Workspace's file-upload functionality. Insufficient… |
| 2026-11-06 05:18:20 | [CVE-2026-119432](https://nvd.nist.gov/vuln/detail/CVE-2026-119432) | High | 8.7 | A stored cross-site scripting (XSS) vulnerability exists in the Foxit Workspace's file share preview functionality. An… |
| 2026-11-06 05:18:20 | [CVE-2026-119433](https://nvd.nist.gov/vuln/detail/CVE-2026-119433) | High | 7.7 | A server-side request forgery (SSRF) vulnerability exists in an undocumented API endpoint of Foxit Workspace due to ins… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
