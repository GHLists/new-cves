# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-11-02 10:18 UTC

New CVEs published between 2026-11-02 09:19 UTC and 2026-11-02 10:18 UTC.

[Full CSV](data/new-cves-2026-11-02T10-18-12-564413Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-11-02 10:17:10 | [CVE-2024-7075](https://nvd.nist.gov/vuln/detail/CVE-2024-7075) | Medium | 4.6 | The user search function within the management console fails to properly encode user-supplied input before rendering it… |
| 2026-11-02 10:17:10 | [CVE-2025-13647](https://nvd.nist.gov/vuln/detail/CVE-2025-13647) | Medium | 5.8 | The affected component fails to enforce expected validation constraints on the `content-type` header when processing ce… |
| 2026-11-02 10:17:11 | [CVE-2026-118871](https://nvd.nist.gov/vuln/detail/CVE-2026-118871) | Medium | 6.5 | SQL injection vulnerability classified as an internal threat level.Attackers can steal database information via SQL inj… |
| 2026-11-02 10:17:11 | [CVE-2026-18800](https://nvd.nist.gov/vuln/detail/CVE-2026-18800) | Medium | 4.4 | When an Event Publisher output adapter is configured with properties that are irrelevant to its function, the affected… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
