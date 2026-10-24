# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-24 07:20 UTC

New CVEs published between 2026-10-24 06:19 UTC and 2026-10-24 07:20 UTC.

[Full CSV](data/new-cves-2026-10-24T07-20-02-272318Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-10-24 07:16:44 | [CVE-2026-108013](https://nvd.nist.gov/vuln/detail/CVE-2026-108013) | Medium | 6.8 | BigFix Platform uses Mozilla CA certificate bundle (PEM). Versions of the bundle dated before 2026/10/20 still trust ce… |
| 2026-10-24 07:16:46 | [CVE-2026-115802](https://nvd.nist.gov/vuln/detail/CVE-2026-115802) | Low | 2.1 | A weakness has been identified in InternScience InternAgent 1.5.0. This affects the function train of the file tasks/Au… |
| 2026-10-24 07:16:46 | [CVE-2026-115803](https://nvd.nist.gov/vuln/detail/CVE-2026-115803) | Low | 2.1 | A flaw has been found in Scada-LTS 2.8.0. Affected by this vulnerability is the function HttpServletRequest.getParamete… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
