# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-11-17 10:19 UTC

New CVEs published between 2026-11-17 09:18 UTC and 2026-11-17 10:19 UTC.

[Full CSV](data/new-cves-2026-11-17T10-19-53-738345Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-11-17 10:17:21 | [CVE-2026-112209](https://nvd.nist.gov/vuln/detail/CVE-2026-112209) | Medium | 5.3 | A Cross-Site Scripting (XSS) vulnerability reflected in the GET parameters `cod_primaria` and `cod_secundaria` of the N… |
| 2026-11-17 10:17:21 | [CVE-2026-118496](https://nvd.nist.gov/vuln/detail/CVE-2026-118496) | High | 7.5 | The affected products process a server-supplied URL without sufficient validation. An unauthenticated remote attacker c… |
| 2026-11-17 10:17:21 | [CVE-2026-118497](https://nvd.nist.gov/vuln/detail/CVE-2026-118497) | High | 7.4 | The affected products do not sufficiently validate CODESYS Automation Server TLS certificates when a user starts the ce… |
| 2026-11-17 10:17:21 | [CVE-2026-118498](https://nvd.nist.gov/vuln/detail/CVE-2026-118498) | High | 7.5 | The CODESYS Automation Server Connector uses server-supplied file names without sufficient path traversal checks. An un… |
| 2026-11-17 10:17:21 | [CVE-2026-21609](https://nvd.nist.gov/vuln/detail/CVE-2026-21609) | High | 7.1 | This High severity Improper Authorization vulnerability was introduced in versions 5.12.0, 10.3.0, and 11.3.0 of Jira S… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
