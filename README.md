# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-01 02:19 UTC

New CVEs published between 2026-10-01 01:18 UTC and 2026-10-01 02:19 UTC.

[Full CSV](data/new-cves-2026-10-01T02-19-19-118161Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-10-01 02:16:53 | [CVE-2026-103532](https://nvd.nist.gov/vuln/detail/CVE-2026-103532) | Medium | 6.9 | A vulnerability has been found in immich-app Immich up to 2.7.5. This affects the function checkSharedLinkAccess of the… |
| 2026-10-01 02:16:53 | [CVE-2026-13313](https://nvd.nist.gov/vuln/detail/CVE-2026-13313) | High | 8.9 | An Active Debug Code vulnerability in certain ASUS router models allows a remote authenticated user, via a crafted HTTP… |
| 2026-10-01 02:16:53 | [CVE-2026-14157](https://nvd.nist.gov/vuln/detail/CVE-2026-14157) | Critical | 9.4 | Use of an Externally Controlled Format String in the ASUS Router modules allow a remote authenticated user to execute a… |
| 2026-10-01 02:16:54 | [CVE-2026-93495](https://nvd.nist.gov/vuln/detail/CVE-2026-93495) | High | 7.0 | Improper initialization in an ASUS certain motherboard allows an physically proximate user to read or write arbitrary m… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
