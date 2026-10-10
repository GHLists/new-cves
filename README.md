# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-10 16:18 UTC

New CVEs published between 2026-10-10 15:18 UTC and 2026-10-10 16:18 UTC.

[Full CSV](data/new-cves-2026-10-10T16-18-44-900842Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-10-10 16:16:31 | [CVE-2026-108579](https://nvd.nist.gov/vuln/detail/CVE-2026-108579) | Low | 2.3 | OpenPanel through 2.3.0 contains a CSV formula injection vulnerability that allows unauthenticated attackers to embed s… |
| 2026-10-10 16:16:31 | [CVE-2026-108580](https://nvd.nist.gov/vuln/detail/CVE-2026-108580) | Medium | 6.9 | AniWorld Downloader before 5.3.0 contains an improper restriction of authentication attempts vulnerability in the WebUI… |
| 2026-10-10 16:16:31 | [CVE-2026-108581](https://nvd.nist.gov/vuln/detail/CVE-2026-108581) | High | 7.1 | TencentCloud Octop through 1.0.2b6 contains a missing authorization vulnerability that allows authenticated low-privile… |
| 2026-10-10 16:16:31 | [CVE-2026-108582](https://nvd.nist.gov/vuln/detail/CVE-2026-108582) | Medium | 6.8 | GenOffice through 0.11.505 contains an incorrect permissions vulnerability in its HTTP MCP server file store that allow… |
| 2026-10-10 16:16:31 | [CVE-2026-108583](https://nvd.nist.gov/vuln/detail/CVE-2026-108583) | Low | 2.3 | zotero-mcp 0.10.0 through 0.14.1 contains a server-side request forgery vulnerability that allows attackers to reach in… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
