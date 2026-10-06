# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-06 08:20 UTC

New CVEs published between 2026-10-06 07:18 UTC and 2026-10-06 08:20 UTC.

[Full CSV](data/new-cves-2026-10-06T08-20-50-77901Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-10-06 08:16:35 | [CVE-2026-105305](https://nvd.nist.gov/vuln/detail/CVE-2026-105305) | Medium | 5.4 | A flaw was found in the OIDC implementation of Keycloak, specifically within the Device Authorization Grant flow. This… |
| 2026-10-06 08:16:36 | [CVE-2026-105807](https://nvd.nist.gov/vuln/detail/CVE-2026-105807) | Medium | 6.9 | A vulnerability was found in SourceCodester Simple Student Information System 1.0. This affects an unknown part of the… |
| 2026-10-06 08:16:37 | [CVE-2026-85153](https://nvd.nist.gov/vuln/detail/CVE-2026-85153) | Critical | 9.3 | This vulnerability exists in the Schmooze app due to the use of hardcoded credentials and cryptographic keys in the cli… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
