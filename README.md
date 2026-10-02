# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-02 01:19 UTC

New CVEs published between 2026-10-02 00:18 UTC and 2026-10-02 01:19 UTC.

[Full CSV](data/new-cves-2026-10-02T01-19-37-24701Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-10-02 01:16:42 | [CVE-2026-103096](https://nvd.nist.gov/vuln/detail/CVE-2026-103096) | High | 7.5 | API key is hardcoded and retrievable from the application package. Since Android applications can be reverse engineered… |
| 2026-10-02 01:16:43 | [CVE-2026-103097](https://nvd.nist.gov/vuln/detail/CVE-2026-103097) | High | 7.5 | An API key is hardcoded and retrievable from the application package. Since Android applications can be reverse enginee… |
| 2026-10-02 01:16:43 | [CVE-2026-103098](https://nvd.nist.gov/vuln/detail/CVE-2026-103098) | High | 7.5 | Transmission of a sensitive key in the URL over an unencrypted HTTP connection. The request is sent over HTTP rather th… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
