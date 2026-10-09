# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-09 04:18 UTC

New CVEs published between 2026-10-09 03:18 UTC and 2026-10-09 04:18 UTC.

[Full CSV](data/new-cves-2026-10-09T04-18-43-631439Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-10-09 04:18:04 | [CVE-2026-107885](https://nvd.nist.gov/vuln/detail/CVE-2026-107885) | Low | 3.3 | OpenPrinting CUPS through 2.4.20 contains a resource-exhaustion vulnerability in the submission-timeout handling of cup… |
| 2026-10-09 04:18:05 | [CVE-2026-107886](https://nvd.nist.gov/vuln/detail/CVE-2026-107886) | Low | 2.3 | OpenPrinting CUPS before 2.4.20 contains a double-free in printer-class management. When CUPS-Add-Modify-Class replaces… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
