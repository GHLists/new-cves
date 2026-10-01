# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-01 23:18 UTC

New CVEs published between 2026-10-01 22:18 UTC and 2026-10-01 23:18 UTC.

[Full CSV](data/new-cves-2026-10-01T23-18-41-041761Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-10-01 23:16:46 | [CVE-2025-71427](https://nvd.nist.gov/vuln/detail/CVE-2025-71427) | High | 7.6 | Office-PowerPoint-MCP-Server through 2.0.7 contains a path traversal vulnerability that allows MCP callers to write and… |
| 2026-10-01 23:16:46 | [CVE-2026-103760](https://nvd.nist.gov/vuln/detail/CVE-2026-103760) | High | 8.2 | Mooncake transfer engine through 0.3.13.post1 contains a denial of service vulnerability that allows unauthenticated re… |
| 2026-10-01 23:16:46 | [CVE-2026-103761](https://nvd.nist.gov/vuln/detail/CVE-2026-103761) | High | 8.7 | Mooncake transfer engine through 0.3.13.post1 contains a memory exhaustion vulnerability in TransferMetadata::receivePe… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
