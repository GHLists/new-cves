# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-24 10:18 UTC

New CVEs published between 2026-10-24 09:18 UTC and 2026-10-24 10:18 UTC.

[Full CSV](data/new-cves-2026-10-24T10-18-41-396166Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-10-24 10:17:08 | [CVE-2026-114194](https://nvd.nist.gov/vuln/detail/CVE-2026-114194) | Medium | 6.5 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in Igor Funa Ad Inse… |
| 2026-10-24 10:17:10 | [CVE-2026-114705](https://nvd.nist.gov/vuln/detail/CVE-2026-114705) | Medium | 6.5 | Missing Authorization vulnerability in quadlayers WP Social Feed Gallery insta-gallery allows Exploiting Incorrectly Co… |
| 2026-10-24 10:17:10 | [CVE-2026-115994](https://nvd.nist.gov/vuln/detail/CVE-2026-115994) | Medium | 5.4 | BOLA Allows Cross-Project Target Tampering in Cervantes version v1.3-beta could allow an attacker modify or delete targ… |
| 2026-10-24 10:17:10 | [CVE-2026-115998](https://nvd.nist.gov/vuln/detail/CVE-2026-115998) | Medium | 4.3 | IDOR in Cervantes version v1.3-beta could allow an authenticated attacker ca access sensitive findings, proof-of-concep… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
