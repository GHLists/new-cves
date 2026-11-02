# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-11-02 12:18 UTC

New CVEs published between 2026-11-02 11:18 UTC and 2026-11-02 12:18 UTC.

[Full CSV](data/new-cves-2026-11-02T12-18-13-081594Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-11-02 12:16:57 | [CVE-2024-9517](https://nvd.nist.gov/vuln/detail/CVE-2024-9517) | Medium | 4.9 | The refresh token grant type in WSO2 products fails to re-validate account status before issuing new access tokens. Thi… |
| 2026-11-02 12:16:58 | [CVE-2026-100140](https://nvd.nist.gov/vuln/detail/CVE-2026-100140) | Low | 1.9 | An integer overflow vulnerability in the Qt XML parsing (Qt5Compat / QXmlSimpleReader) functionality of Qt. |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
