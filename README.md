# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-11-20 16:19 UTC

New CVEs published between 2026-11-20 15:20 UTC and 2026-11-20 16:19 UTC.

[Full CSV](data/new-cves-2026-11-20T16-19-32-458903Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-11-20 16:17:59 | [CVE-2026-102769](https://nvd.nist.gov/vuln/detail/CVE-2026-102769) | Medium | 6.8 | A SQL injection vulnerability when the recipient tapped on a specially crafted “order details” message from an unoffici… |
| 2026-11-20 16:18:04 | [CVE-2026-44908](https://nvd.nist.gov/vuln/detail/CVE-2026-44908) | Medium | 4.8 | Improper following of a certificate’s chain of trust in the remote-attestation verifier used to establish trust with Me… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
