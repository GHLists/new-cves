# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-23 04:19 UTC

New CVEs published between 2026-10-23 03:18 UTC and 2026-10-23 04:19 UTC.

[Full CSV](data/new-cves-2026-10-23T04-19-29-861918Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-10-23 04:18:15 | [CVE-2026-115546](https://nvd.nist.gov/vuln/detail/CVE-2026-115546) | High | 8.1 | Okta Access Gateway (OAG) does not validate the selected authentication source during sign-on. An authenticated user wi… |
| 2026-10-23 04:18:16 | [CVE-2026-115547](https://nvd.nist.gov/vuln/detail/CVE-2026-115547) | Critical | 9.1 | An input validation issue in the Okta Access Gateway (OAG) Admin Console allows the processing of specially formatted c… |
| 2026-10-23 04:18:16 | [CVE-2026-115638](https://nvd.nist.gov/vuln/detail/CVE-2026-115638) | Medium | 4.3 | OpenStack Ironic through 39.0.1 allows a denial of service via a configdrive that results in a very large amount of unc… |
| 2026-10-23 04:18:16 | [CVE-2026-54615](https://nvd.nist.gov/vuln/detail/CVE-2026-54615) | Medium | 6.0 | Part-DB is an open source inventory management system for electronic components. Prior to version 2.12.1, LogEntryExtra… |
| 2026-10-23 04:18:17 | [CVE-2026-54630](https://nvd.nist.gov/vuln/detail/CVE-2026-54630) | Critical | 9.6 | Part-DB is an open source inventory management system for electronic components. Prior to version 2.12.1, the part atta… |
| 2026-10-23 04:18:17 | [CVE-2026-54631](https://nvd.nist.gov/vuln/detail/CVE-2026-54631) | Medium | 6.3 | Part-DB is an open source inventory management system for electronic components. Prior to version 2.12.1, the file .env… |
| 2026-10-23 04:18:17 | [CVE-2026-55600](https://nvd.nist.gov/vuln/detail/CVE-2026-55600) | Medium | 5.7 | Part-DB is an open source inventory management system for electronic components. Prior to version 2.12.2, Part-DB rende… |
| 2026-10-23 04:18:19 | [CVE-2026-89419](https://nvd.nist.gov/vuln/detail/CVE-2026-89419) | Medium | 5.0 | OpenStack Ironic before 39.0.1 sometimes allows a user to change the maintenance setting on a node via PATCH to /v1/nod… |
| 2026-10-23 04:18:19 | [CVE-2026-90458](https://nvd.nist.gov/vuln/detail/CVE-2026-90458) | Medium | 5.4 | OpenStack Ironic before 39.0.1 allows DELETE and GET via vendor_passthru, e.g., to delete accounts from the BMC's Redfi… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
