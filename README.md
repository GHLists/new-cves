# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-11-19 23:21 UTC

New CVEs published between 2026-11-19 22:21 UTC and 2026-11-19 23:21 UTC.

[Full CSV](data/new-cves-2026-11-19T23-21-40-215613Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-11-19 23:19:24 | [CVE-2026-122676](https://nvd.nist.gov/vuln/detail/CVE-2026-122676) | High | 8.5 | Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection') vulnerability in PublishPress Publ… |
| 2026-11-19 23:19:29 | [CVE-2026-133327](https://nvd.nist.gov/vuln/detail/CVE-2026-133327) | Low | 2.1 | A vulnerability was identified in Dolibarr ERP CRM up to 23.0.4. This affects the function dol_convert_file in the libr… |
| 2026-11-19 23:19:29 | [CVE-2026-133435](https://nvd.nist.gov/vuln/detail/CVE-2026-133435) | Low | 3.7 | A flaw was found in Keycloak. When configured with a database that uses case-insensitive collation, Keycloak resolves r… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
