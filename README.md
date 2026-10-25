# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-25 12:18 UTC

New CVEs published between 2026-10-25 11:18 UTC and 2026-10-25 12:18 UTC.

[Full CSV](data/new-cves-2026-10-25T12-18-41-795907Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-10-25 12:16:27 | [CVE-2026-116066](https://nvd.nist.gov/vuln/detail/CVE-2026-116066) | High | 7.0 | Firecrawl before 2.11.586 contains a server-side request forgery vulnerability in the Playwright service SSRF proxy tha… |
| 2026-10-25 12:16:28 | [CVE-2026-116067](https://nvd.nist.gov/vuln/detail/CVE-2026-116067) | High | 8.8 | Paisa before 0.7.8 contains a path traversal vulnerability in the GetFile, GetSheet, DeleteBackups, and DeleteSheetBack… |
| 2026-10-25 12:16:29 | [CVE-2026-116068](https://nvd.nist.gov/vuln/detail/CVE-2026-116068) | High | 8.7 | Dokploy through 0.30.10 contains an authorization bypass vulnerability that allows owners or admins of any organization… |
| 2026-10-25 12:16:29 | [CVE-2026-116069](https://nvd.nist.gov/vuln/detail/CVE-2026-116069) | Medium | 6.9 | NiubiGEO before 0.3.2 contains an unauthenticated server-side request forgery vulnerability that allows remote attacker… |
| 2026-10-25 12:16:29 | [CVE-2026-116070](https://nvd.nist.gov/vuln/detail/CVE-2026-116070) | Medium | 6.9 | Docker-Proxy through 5.1.9 contains a missing authentication vulnerability in the hubcmdui routes/config.js that allows… |
| 2026-10-25 12:16:29 | [CVE-2026-116071](https://nvd.nist.gov/vuln/detail/CVE-2026-116071) | High | 8.2 | rotki before 1.44.2 contains a weak key derivation vulnerability that allows attackers to brute-force backups because t… |
| 2026-10-25 12:16:29 | [CVE-2026-116072](https://nvd.nist.gov/vuln/detail/CVE-2026-116072) | Medium | 5.3 | Infinity for Reddit through 8.3.4 contains a login cross-site request forgery vulnerability that allows attackers to lo… |
| 2026-10-25 12:16:29 | [CVE-2026-116073](https://nvd.nist.gov/vuln/detail/CVE-2026-116073) | Medium | 6.9 | Leon before commit 50df142 contains a path traversal vulnerability in getModelFileNameFromURL() that allows attackers t… |
| 2026-10-25 12:16:30 | [CVE-2026-116136](https://nvd.nist.gov/vuln/detail/CVE-2026-116136) | Medium | 6.0 | ProjectSend 2.0.0 through 2.7.1 contains an incomplete authorization vulnerability in FileVersions::link() that allows… |
| 2026-10-25 12:16:30 | [CVE-2026-116137](https://nvd.nist.gov/vuln/detail/CVE-2026-116137) | Medium | 6.3 | adm-zip through 0.6.1 contains a duplicate-entry validation bypass that allows attackers to evade the readEntries() che… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
