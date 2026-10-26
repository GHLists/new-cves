# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-26 06:19 UTC

New CVEs published between 2026-10-26 05:20 UTC and 2026-10-26 06:19 UTC.

[Full CSV](data/new-cves-2026-10-26T06-19-29-733125Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-10-26 06:17:38 | [CVE-2026-116120](https://nvd.nist.gov/vuln/detail/CVE-2026-116120) | Medium | 6.3 | A vulnerability was determined in NocoDB up to 2026.07.0. This vulnerability affects the function UserRefreshToken.dele… |
| 2026-10-26 06:17:41 | [CVE-2026-116121](https://nvd.nist.gov/vuln/detail/CVE-2026-116121) | Medium | 6.3 | A vulnerability was identified in NocoDB up to 2026.08.0. This issue affects some unknown processing of the file users.… |
| 2026-10-26 06:17:41 | [CVE-2026-116122](https://nvd.nist.gov/vuln/detail/CVE-2026-116122) | Medium | 6.3 | A security flaw has been discovered in NocoDB up to 2026.07.0. Impacted is the function AuthService.validateUser of the… |
| 2026-10-26 06:17:41 | [CVE-2026-116123](https://nvd.nist.gov/vuln/detail/CVE-2026-116123) | Medium | 6.3 | A weakness has been identified in NocoDB up to 2026.07.0. The affected element is the function validatePassword of the… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
