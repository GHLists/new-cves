# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-11-03 07:19 UTC

New CVEs published between 2026-11-03 06:18 UTC and 2026-11-03 07:19 UTC.

[Full CSV](data/new-cves-2026-11-03T07-19-51-82531Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-11-03 07:17:19 | [CVE-2025-1397](https://nvd.nist.gov/vuln/detail/CVE-2025-1397) | Medium | 4.8 | When utilizing JWT Bearer or SAML2 Bearer grant types, the system fails to validate the status of the Identity Provider… |
| 2026-11-03 07:17:41 | [CVE-2025-5769](https://nvd.nist.gov/vuln/detail/CVE-2025-5769) | Medium | 6.1 | The authentication endpoint does not properly encode user-supplied input before rendering it within the web page. This… |
| 2026-11-03 07:18:21 | [CVE-2026-120987](https://nvd.nist.gov/vuln/detail/CVE-2026-120987) |  |  | Whale Browser before 5.39.412.57 allows an attacker to bypass the iframe sandbox in a dual-tab environment. |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
