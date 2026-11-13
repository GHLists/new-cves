# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-11-13 23:20 UTC

New CVEs published between 2026-11-13 22:19 UTC and 2026-11-13 23:20 UTC.

[Full CSV](data/new-cves-2026-11-13T23-20-07-696638Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-11-13 23:17:17 | [CVE-2026-128134](https://nvd.nist.gov/vuln/detail/CVE-2026-128134) | High | 7.8 | NLTK (Natural Language Toolkit) is a suite of open source Python modules, data sets, and tutorials supporting research… |
| 2026-11-13 23:17:18 | [CVE-2026-129173](https://nvd.nist.gov/vuln/detail/CVE-2026-129173) | Medium | 6.9 | A security flaw has been discovered in Stirling-Tools Stirling-PDF up to 3.3.0. Affected is the function WorkflowPartic… |
| 2026-11-13 23:17:19 | [CVE-2026-129180](https://nvd.nist.gov/vuln/detail/CVE-2026-129180) | Medium | 5.5 | A flaw has been found in projectworlds Visitor Management System 1.0. This vulnerability affects the function mysqli_qu… |
| 2026-11-13 23:17:19 | [CVE-2026-71519](https://nvd.nist.gov/vuln/detail/CVE-2026-71519) | High | 8.6 | PrestaShop before 8.2.9 and 9.2.1 contains a broken access control vulnerability that allows an authenticated Webservic… |
| 2026-11-13 23:17:19 | [CVE-2026-71531](https://nvd.nist.gov/vuln/detail/CVE-2026-71531) | High | 8.6 | PrestaShop before 8.2.9 and 9.2.1 contains an authorization flaw in the Webservice API that allows an attacker holding… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
