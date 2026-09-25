# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-09-25 00:20 UTC

New CVEs published between 2026-09-24 23:20 UTC and 2026-09-25 00:20 UTC.

[Full CSV](data/new-cves-2026-09-25T00-20-05-586952Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-09-25 00:16:57 | [CVE-2026-84283](https://nvd.nist.gov/vuln/detail/CVE-2026-84283) | Medium | 6.8 | Secure Folder 1.2 stores files selected for its password-protected vault as unencrypted files in the Android shared-sto… |
| 2026-09-25 00:16:57 | [CVE-2026-85082](https://nvd.nist.gov/vuln/detail/CVE-2026-85082) | High | 8.5 | Root Browser Classic 3.3.0 passes the path of a selected SQLite database to an operating-system shell without safely se… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
