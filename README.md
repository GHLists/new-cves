# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-29 02:18 UTC

New CVEs published between 2026-10-29 01:19 UTC and 2026-10-29 02:18 UTC.

[Full CSV](data/new-cves-2026-10-29T02-18-42-525874Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-10-29 02:16:49 | [CVE-2026-113387](https://nvd.nist.gov/vuln/detail/CVE-2026-113387) | High | 8.6 | The Ortto plugin for WordPress before 1.0.25 did not authenticate configuration update requests, relying only on a secr… |
| 2026-10-29 02:16:50 | [CVE-2026-113409](https://nvd.nist.gov/vuln/detail/CVE-2026-113409) | Medium | 4.8 | The Ortto plugin for WordPress before 1.0.25 did not escape stored settings on its admin settings page, leading to stor… |
| 2026-10-29 02:16:50 | [CVE-2026-114173](https://nvd.nist.gov/vuln/detail/CVE-2026-114173) | Medium | 5.3 | The Ortto plugin for WordPress before 1.0.25 did not filter the WooCommerce product data it embedded in public storefro… |
| 2026-10-29 02:16:51 | [CVE-2026-16889](https://nvd.nist.gov/vuln/detail/CVE-2026-16889) | Medium | 4.8 | In openEQUELLA before 2026.1, the pre-login notice image upload endpoint (PUT /api/preloginnotice/image/{name}) does no… |
| 2026-10-29 02:16:52 | [CVE-2026-66088](https://nvd.nist.gov/vuln/detail/CVE-2026-66088) | Critical | 9.4 | In openEQUELLA before 2026.1, the system.execute() function available to the scripting engine runs supplied operating s… |
| 2026-10-29 02:16:52 | [CVE-2026-66089](https://nvd.nist.gov/vuln/detail/CVE-2026-66089) | Medium | 6.1 | In openEQUELLA before 2026.1, the SOAP API parses XML supplied in the stopEdit operation with a parser that resolves ex… |
| 2026-10-29 02:16:52 | [CVE-2026-66090](https://nvd.nist.gov/vuln/detail/CVE-2026-66090) | High | 7.1 | In openEQUELLA before 2026.1, the XML parser used for item metadata does not disable external entity resolution. A user… |
| 2026-10-29 02:16:52 | [CVE-2026-66091](https://nvd.nist.gov/vuln/detail/CVE-2026-66091) | Medium | 6.9 | In openEQUELLA before 2026.1, the GET /api/userquery/userinfobackup endpoint performs no authentication or authorisatio… |
| 2026-10-29 02:16:53 | [CVE-2026-66092](https://nvd.nist.gov/vuln/detail/CVE-2026-66092) | Medium | 4.8 | In openEQUELLA before 2026.2, the pre-login notice is stored as HTML and rendered on the legacy logon page without enco… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
