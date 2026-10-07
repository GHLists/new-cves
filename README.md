# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-07 23:19 UTC

New CVEs published between 2026-10-07 22:18 UTC and 2026-10-07 23:19 UTC.

[Full CSV](data/new-cves-2026-10-07T23-19-44-912856Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-10-07 23:17:00 | [CVE-2026-107314](https://nvd.nist.gov/vuln/detail/CVE-2026-107314) | Medium | 5.9 | pgjdbc, the PostgreSQL JDBC Driver, versions 42.7.11 through 42.7.13 enforce no restriction when the requireAuth connec… |
| 2026-10-07 23:17:01 | [CVE-2026-89322](https://nvd.nist.gov/vuln/detail/CVE-2026-89322) | High | 7.2 | Vault and Vault Enterprise did not consistently evaluate ACL policies against the canonical form of resource and policy… |
| 2026-10-07 23:17:01 | [CVE-2026-97664](https://nvd.nist.gov/vuln/detail/CVE-2026-97664) |  |  | Rejected reason: This CVE ID has been rejected or withdrawn by its CVE Numbering Authority. |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
