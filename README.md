# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-27 09:18 UTC

New CVEs published between 2026-10-27 08:19 UTC and 2026-10-27 09:18 UTC.

[Full CSV](data/new-cves-2026-10-27T09-18-41-432116Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-10-27 09:16:33 | [CVE-2026-65211](https://nvd.nist.gov/vuln/detail/CVE-2026-65211) | High | 7.2 | This issue may allow an authenticated IPMI Administrator to read and write arbitrary BMC physical memory and thereby ex… |
| 2026-10-27 09:16:34 | [CVE-2026-65213](https://nvd.nist.gov/vuln/detail/CVE-2026-65213) | Medium | 6.6 | This issue may allow an IPMI authenticated administrator to execute commands as the operating system root user on the B… |
| 2026-10-27 09:16:34 | [CVE-2026-92885](https://nvd.nist.gov/vuln/detail/CVE-2026-92885) | Critical | 9.8 | The Qode Membership plugin for WordPress is vulnerable to Authentication Bypass leading to Account Takeover in all vers… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
