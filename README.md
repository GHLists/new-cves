# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-16 12:21 UTC

New CVEs published between 2026-10-16 11:20 UTC and 2026-10-16 12:21 UTC.

[Full CSV](data/new-cves-2026-10-16T12-21-09-853251Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-10-16 12:16:31 | [CVE-2026-105959](https://nvd.nist.gov/vuln/detail/CVE-2026-105959) | High | 7.5 | A flaw was found in spice-server. The GLZ encoder dictionary restore path truncates a size_t allocation size to int whe… |
| 2026-10-16 12:16:32 | [CVE-2026-107648](https://nvd.nist.gov/vuln/detail/CVE-2026-107648) | High | 7.2 | The WP Sessions Time Monitoring Full Automatic plugin for WordPress is vulnerable to Stored Cross-Site Scripting via th… |
| 2026-10-16 12:16:32 | [CVE-2026-109930](https://nvd.nist.gov/vuln/detail/CVE-2026-109930) | Medium | 5.3 | The MAIO WordPress plugin before 7.3.22 does not properly restrict access to its analytics data, treating a credential… |
| 2026-10-16 12:16:32 | [CVE-2026-110029](https://nvd.nist.gov/vuln/detail/CVE-2026-110029) | Medium | 5.4 | The Squeeze WordPress plugin before 1.8.1 does not perform a capability check on one of its AJAX actions, allowing auth… |
| 2026-10-16 12:16:33 | [CVE-2026-111390](https://nvd.nist.gov/vuln/detail/CVE-2026-111390) | Medium | 6.0 | Erupt through 2.3.0 contains an HQL injection vulnerability that allows authenticated users to bypass tree-scoped data… |
| 2026-10-16 12:16:33 | [CVE-2026-111391](https://nvd.nist.gov/vuln/detail/CVE-2026-111391) | Critical | 9.2 | SGLang 0.5.10 through 0.5.22 contains a code injection vulnerability in _evaluate_filter() that allows remote attackers… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
