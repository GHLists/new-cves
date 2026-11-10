# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-11-10 02:19 UTC

New CVEs published between 2026-11-10 01:19 UTC and 2026-11-10 02:19 UTC.

[Full CSV](data/new-cves-2026-11-10T02-19-43-746187Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-11-10 02:16:45 | [CVE-2026-88707](https://nvd.nist.gov/vuln/detail/CVE-2026-88707) | High | 7.1 | An out-of-bounds write in certain ASUS Router firmware allows an unauthenticated nearby user to send an HTTP request co… |
| 2026-11-10 02:16:45 | [CVE-2026-88708](https://nvd.nist.gov/vuln/detail/CVE-2026-88708) | Medium | 5.3 | An off-by-one error in certain ASUS Router firmware allows an unauthenticated nearby user to send a packet with a speci… |
| 2026-11-10 02:16:45 | [CVE-2026-88709](https://nvd.nist.gov/vuln/detail/CVE-2026-88709) | High | 7.0 | Improper neutralization of special elements used in an OS command in certain ASUS Router firmware allows an user with p… |
| 2026-11-10 02:16:45 | [CVE-2026-88710](https://nvd.nist.gov/vuln/detail/CVE-2026-88710) | High | 8.7 | Improper neutralization of special elements used in an OS command in certain ASUS Router firmware allows an unauthentic… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
