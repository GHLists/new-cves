# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-11-25 02:21 UTC

New CVEs published between 2026-11-25 01:18 UTC and 2026-11-25 02:21 UTC.

[Full CSV](data/new-cves-2026-11-25T02-21-00-711005Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-11-25 02:17:39 | [CVE-2026-126536](https://nvd.nist.gov/vuln/detail/CVE-2026-126536) | High | 7.0 | Akaunting 3.3.0 contains a stored cross-site scripting vulnerability in the XLSX tax-import workflow. An authenticated… |
| 2026-11-25 02:17:41 | [CVE-2026-135768](https://nvd.nist.gov/vuln/detail/CVE-2026-135768) | Medium | 6.8 | A flaw was found in the keycloak-services component of Keycloak, which is used for managing authentication and authoriz… |
| 2026-11-25 02:17:41 | [CVE-2026-136445](https://nvd.nist.gov/vuln/detail/CVE-2026-136445) | Low | 2.1 | A flaw has been found in JaguarJack catch-admin up to 5.4.1. The impacted element is the function store of the file mod… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
