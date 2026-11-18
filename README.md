# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-11-18 04:18 UTC

New CVEs published between 2026-11-18 03:21 UTC and 2026-11-18 04:18 UTC.

[Full CSV](data/new-cves-2026-11-18T04-18-59-544737Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-11-18 04:17:12 | [CVE-2026-101113](https://nvd.nist.gov/vuln/detail/CVE-2026-101113) | High | 8.6 | Multiple ELECOM wireless LAN routers contain an OS command injection vulnerability that may cause an arbitrary OS comma… |
| 2026-11-18 04:17:14 | [CVE-2026-130121](https://nvd.nist.gov/vuln/detail/CVE-2026-130121) | High | 7.2 | The AI Puffer - MCP Server for Claude & ChatGPT, with AI Chatbot plugin for WordPress is vulnerable to Stored Cross-Sit… |
| 2026-11-18 04:17:14 | [CVE-2026-130644](https://nvd.nist.gov/vuln/detail/CVE-2026-130644) | High | 8.1 | A path traversal flaw was found in ansible-core. When installing a collection with ansible-galaxy collection install, t… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
