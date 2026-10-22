# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-22 05:19 UTC

New CVEs published between 2026-10-22 04:21 UTC and 2026-10-22 05:19 UTC.

[Full CSV](data/new-cves-2026-10-22T05-19-28-538549Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-10-22 05:16:49 | [CVE-2026-114219](https://nvd.nist.gov/vuln/detail/CVE-2026-114219) | Critical | 9.1 | NT OneAPP developed by NewType Infortech has a Hard-coded Credentials vulnerability. Unauthenticated remote attackers c… |
| 2026-10-22 05:16:50 | [CVE-2026-114220](https://nvd.nist.gov/vuln/detail/CVE-2026-114220) | Critical | 9.3 | NT OneAPP developed by NewType Infortech has an Improper Certificate Validation vulnerability. Unauthenticated network-… |
| 2026-10-22 05:16:50 | [CVE-2026-114221](https://nvd.nist.gov/vuln/detail/CVE-2026-114221) | Medium | 5.9 | NT OneAPP developed by NewType Infortech has a Credential Disclosure vulnerability. Unauthenticated remote attackers ca… |
| 2026-10-22 05:16:50 | [CVE-2026-114222](https://nvd.nist.gov/vuln/detail/CVE-2026-114222) | Medium | 6.9 | NT OneAPP developed by NewType Infortech has an Authentication Bypass vulnerability. Unauthenticated local attackers ca… |
| 2026-10-22 05:16:50 | [CVE-2026-114223](https://nvd.nist.gov/vuln/detail/CVE-2026-114223) | Medium | 6.7 | NT OneAPP developed by NewType Infortech has an Exposure of Sensitive Information vulnerability. Unauthenticated local… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
