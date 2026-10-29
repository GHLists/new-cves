# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-29 23:20 UTC

New CVEs published between 2026-10-29 22:19 UTC and 2026-10-29 23:20 UTC.

[Full CSV](data/new-cves-2026-10-29T23-20-37-642263Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-10-29 23:16:54 | [CVE-2023-22793](https://nvd.nist.gov/vuln/detail/CVE-2023-22793) | Critical | 9.3 | A vulnerability allowing an unauthenticated attacker to perform remote code execution (RCE) on servers running the Veea… |
| 2026-10-29 23:16:54 | [CVE-2026-107238](https://nvd.nist.gov/vuln/detail/CVE-2026-107238) | High | 8.7 | A vulnerability allowing an authenticated domain user to perform remote code execution (RCE) as the LocalSystem account… |
| 2026-10-29 23:16:54 | [CVE-2026-107239](https://nvd.nist.gov/vuln/detail/CVE-2026-107239) | High | 8.8 | A vulnerability allowing a member of the Veeam Virtualization Extensions Users group to perform remote code execution (… |
| 2026-10-29 23:16:55 | [CVE-2026-112211](https://nvd.nist.gov/vuln/detail/CVE-2026-112211) |  |  | Rejected reason: This CVE ID has been rejected or withdrawn by its CVE Numbering Authority. |
| 2026-10-29 23:17:02 | [CVE-2026-92744](https://nvd.nist.gov/vuln/detail/CVE-2026-92744) | High | 8.7 | Under certain conditions, privilege manager agent allows a remote unauthenticated attacker to execute arbitrary code as… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
