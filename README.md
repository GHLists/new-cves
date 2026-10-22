# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-22 10:18 UTC

New CVEs published between 2026-10-22 09:18 UTC and 2026-10-22 10:18 UTC.

[Full CSV](data/new-cves-2026-10-22T10-18-42-150306Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-10-22 10:17:07 | [CVE-2026-106017](https://nvd.nist.gov/vuln/detail/CVE-2026-106017) | Medium | 6.3 | Improper certificate validation in the OpenVPN 3 Core library version 3.4 through 3.11.7 allows attackers to circumvent… |
| 2026-10-22 10:17:08 | [CVE-2026-112085](https://nvd.nist.gov/vuln/detail/CVE-2026-112085) | High | 8.2 | webpack-dev-server is a development server that provides live reloading for webpack projects. In versions before 5.2.7… |
| 2026-10-22 10:17:08 | [CVE-2026-114348](https://nvd.nist.gov/vuln/detail/CVE-2026-114348) | Medium | 5.3 | webpack-dev-server is a development server that provides live reloading for webpack projects. In versions from 5.1.0 be… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
