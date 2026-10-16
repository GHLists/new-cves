# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-16 00:19 UTC

New CVEs published between 2026-10-15 23:20 UTC and 2026-10-16 00:19 UTC.

[Full CSV](data/new-cves-2026-10-16T00-19-40-488665Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-10-16 00:17:04 | [CVE-2026-111210](https://nvd.nist.gov/vuln/detail/CVE-2026-111210) | Medium | 5.5 | A vulnerability was determined in bitcoinj up to 0.17. Affected is the function url.openConnection of the file PaymentS… |
| 2026-10-16 00:17:05 | [CVE-2026-16754](https://nvd.nist.gov/vuln/detail/CVE-2026-16754) | Medium | 5.9 | A potential improper certificate validation vulnerability was reported in Lenovo Smart Camera C33, distributed exclusiv… |
| 2026-10-16 00:17:05 | [CVE-2026-16755](https://nvd.nist.gov/vuln/detail/CVE-2026-16755) | Medium | 6.0 | A potential vulnerability was reported in Lenovo Smart Camera C33, distributed exclusively in the Chinese market, that… |
| 2026-10-16 00:17:05 | [CVE-2026-75941](https://nvd.nist.gov/vuln/detail/CVE-2026-75941) | High | 8.6 | A potential vulnerability was reported in the Lenovo Legion Zone application, distributed exclusively in the Chinese ma… |
| 2026-10-16 00:17:05 | [CVE-2026-84823](https://nvd.nist.gov/vuln/detail/CVE-2026-84823) | High | 7.1 | A flaw was found in WildFly. A user with the `Monitor` role, which is the lowest standard Role-Based Access Control (RB… |
| 2026-10-16 00:17:06 | [CVE-2026-89057](https://nvd.nist.gov/vuln/detail/CVE-2026-89057) | High | 7.0 | A potential authentication bypass vulnerability was reported in some Lenovo tablets that could allow a user with physic… |
| 2026-10-16 00:17:07 | [CVE-2026-89062](https://nvd.nist.gov/vuln/detail/CVE-2026-89062) | Medium | 6.8 | A potential out-of-bounds write vulnerability was reported in the Lenovo Energy Management driver that could allow a lo… |
| 2026-10-16 00:17:07 | [CVE-2026-92629](https://nvd.nist.gov/vuln/detail/CVE-2026-92629) | High | 7.0 | A potential improper authorization vulnerability was reported in Lenovo Baiying PC Client, distributed exclusively in t… |
| 2026-10-16 00:17:07 | [CVE-2026-92777](https://nvd.nist.gov/vuln/detail/CVE-2026-92777) | Medium | 5.4 | A potential vulnerability was reported in some Lenovo Tablets that could allow a user with physical access to an unlock… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
