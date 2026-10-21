# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-21 08:18 UTC

New CVEs published between 2026-10-21 07:22 UTC and 2026-10-21 08:18 UTC.

[Full CSV](data/new-cves-2026-10-21T08-18-58-892535Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-10-21 08:16:41 | [CVE-2026-107435](https://nvd.nist.gov/vuln/detail/CVE-2026-107435) | High | 7.1 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in WP Chill Strong T… |
| 2026-10-21 08:16:42 | [CVE-2026-110899](https://nvd.nist.gov/vuln/detail/CVE-2026-110899) | High | 7.1 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in Kevin Stover Ninj… |
| 2026-10-21 08:16:42 | [CVE-2026-111074](https://nvd.nist.gov/vuln/detail/CVE-2026-111074) | High | 8.7 | In Eclipse OpenJ9 versions prior to 0.63.0, the JITServer component is vulnerable to a pre-authentication remote denial… |
| 2026-10-21 08:16:42 | [CVE-2026-111075](https://nvd.nist.gov/vuln/detail/CVE-2026-111075) | High | 8.7 | In Eclipse OpenJ9 versions prior to 0.63.0, the JITServer component fails to perform cross-field validation on attacker… |
| 2026-10-21 08:16:43 | [CVE-2026-17557](https://nvd.nist.gov/vuln/detail/CVE-2026-17557) | Medium | 6.5 | A flaw was found in the `lm-evaluation-harness` component of Red Hat OpenShift AI. An authenticated user, able to submi… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
