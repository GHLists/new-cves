# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-11-13 04:18 UTC

New CVEs published between 2026-11-13 03:18 UTC and 2026-11-13 04:18 UTC.

[Full CSV](data/new-cves-2026-11-13T04-18-41-256672Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-11-13 04:17:36 | [CVE-2026-107415](https://nvd.nist.gov/vuln/detail/CVE-2026-107415) | Critical | 9.3 | Memory overflow in Email OTP authentication can lead to unpredictable or erroneous behavior or Denial of Service in Cit… |
| 2026-11-13 04:17:36 | [CVE-2026-111340](https://nvd.nist.gov/vuln/detail/CVE-2026-111340) | High | 8.7 | Memory overflow in KBA (knowledge-based authentication) can lead to unpredictable or erroneous behavior or Denial of Se… |
| 2026-11-13 04:17:36 | [CVE-2026-111341](https://nvd.nist.gov/vuln/detail/CVE-2026-111341) | High | 8.7 | Memory overflow in client-certificate authentication can lead to unpredictable or erroneous behavior or Denial of Servi… |
| 2026-11-13 04:17:36 | [CVE-2026-111342](https://nvd.nist.gov/vuln/detail/CVE-2026-111342) | High | 8.7 | Memory overflow in LDAP authentication can lead to unpredictable or erroneous behavior or Denial of Service in Citrix N… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
