# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-02 05:19 UTC

New CVEs published between 2026-10-02 04:18 UTC and 2026-10-02 05:19 UTC.

[Full CSV](data/new-cves-2026-10-02T05-19-59-32046Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-10-02 05:16:36 | [CVE-2026-10026](https://nvd.nist.gov/vuln/detail/CVE-2026-10026) | High | 7.2 | The CTX Feed Pro plugin for WordPress is vulnerable to Code Injection in all versions up to, and including, 7.6.12. Thi… |
| 2026-10-02 05:16:38 | [CVE-2026-19660](https://nvd.nist.gov/vuln/detail/CVE-2026-19660) | Critical | 9.8 | The Divi Membership plugin for WordPress is vulnerable to Authentication Bypass in all versions up to, and including, 2… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
