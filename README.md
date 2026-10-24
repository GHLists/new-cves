# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-24 18:18 UTC

New CVEs published between 2026-10-24 17:18 UTC and 2026-10-24 18:18 UTC.

[Full CSV](data/new-cves-2026-10-24T18-18-37-735596Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-10-24 18:16:48 | [CVE-2026-115970](https://nvd.nist.gov/vuln/detail/CVE-2026-115970) | Medium | 5.5 | A vulnerability has been found in Travisun Opptrix 0.4.0. This impacts an unknown function of the file /api/system-upda… |
| 2026-10-24 18:16:48 | [CVE-2026-115971](https://nvd.nist.gov/vuln/detail/CVE-2026-115971) | Medium | 5.5 | A vulnerability was found in Travisun Opptrix 0.4.0. Affected is the function Buffer.concat of the file /api/channels/w… |
| 2026-10-24 18:16:48 | [CVE-2026-115972](https://nvd.nist.gov/vuln/detail/CVE-2026-115972) | Medium | 6.9 | A vulnerability was determined in FaveoSuite Faveo Helpdesk up to 2.0.3. Affected by this vulnerability is the function… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
