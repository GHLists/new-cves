# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-11-18 23:20 UTC

New CVEs published between 2026-11-18 22:21 UTC and 2026-11-18 23:20 UTC.

[Full CSV](data/new-cves-2026-11-18T23-20-12-830082Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-11-18 23:17:17 | [CVE-2026-125353](https://nvd.nist.gov/vuln/detail/CVE-2026-125353) | Medium | 5.1 | An incorrect permission assignment vulnerability in Omada SDN Controller prior to 6.2.20 may cause a database backup ge… |
| 2026-11-18 23:17:18 | [CVE-2026-129316](https://nvd.nist.gov/vuln/detail/CVE-2026-129316) | Critical | 9.9 | Dokploy is a free, self-hostable Platform as a Service (PaaS). From 0.29.13 until 0.31.0, the Docker terminal, containe… |
| 2026-11-18 23:17:18 | [CVE-2026-129985](https://nvd.nist.gov/vuln/detail/CVE-2026-129985) | High | 8.7 | Dokploy is a free, self-hostable Platform as a Service (PaaS). Prior to 0.31.1, a user-controlled schedule appName is j… |
| 2026-11-18 23:17:18 | [CVE-2026-129986](https://nvd.nist.gov/vuln/detail/CVE-2026-129986) | Critical | 9.9 | Dokploy is a free, self-hostable Platform as a Service (PaaS). Prior to 0.31.1, mount.deleteFileMount passes a path con… |
| 2026-11-18 23:17:18 | [CVE-2026-129989](https://nvd.nist.gov/vuln/detail/CVE-2026-129989) | Critical | 9.9 | Dokploy is a free, self-hostable Platform as a Service (PaaS). Prior to 0.31.1, the Nixpacks publishDirectory build set… |
| 2026-11-18 23:17:18 | [CVE-2026-129990](https://nvd.nist.gov/vuln/detail/CVE-2026-129990) | High | 8.3 | Dokploy is a free, self-hostable Platform as a Service (PaaS). Prior to 0.31.1, every network.* procedure is only authe… |
| 2026-11-18 23:17:18 | [CVE-2026-129315](https://nvd.nist.gov/vuln/detail/CVE-2026-129315) | High | 8.5 | Dokploy is a free, self-hostable Platform as a Service (PaaS). In 0.31.0 and earlier, the hosted installer and manual i… |
| 2026-11-18 23:17:19 | [CVE-2026-129991](https://nvd.nist.gov/vuln/detail/CVE-2026-129991) | Critical | 9.9 | Dokploy is a free, self-hostable Platform as a Service (PaaS). Prior to 0.31.1, the backup prefix field is only checked… |
| 2026-11-18 23:17:19 | [CVE-2026-129992](https://nvd.nist.gov/vuln/detail/CVE-2026-129992) | Medium | 6.3 | Dokploy is a free, self-hostable Platform as a Service (PaaS). Prior to 0.31.0, failed Railpack builds and database bac… |
| 2026-11-18 23:17:20 | [CVE-2026-132279](https://nvd.nist.gov/vuln/detail/CVE-2026-132279) | Low | 2.1 | A flaw has been found in elunez eladmin up to 2.7. Affected by this vulnerability is the function SqlUtils.sanitizeJdcU… |
| 2026-11-18 23:17:20 | [CVE-2026-132280](https://nvd.nist.gov/vuln/detail/CVE-2026-132280) | Low | 2.1 | A vulnerability has been found in elunez eladmin up to 2.7. Affected by this issue is the function CheckBean of the fil… |
| 2026-11-18 23:17:21 | [CVE-2026-71500](https://nvd.nist.gov/vuln/detail/CVE-2026-71500) | Medium | 6.8 | Mareforma is a local verification layer for AI-assisted research. From 0.3.0 until 0.3.8, _maybe_update_replicated_unlo… |
| 2026-11-18 23:17:21 | [CVE-2026-71533](https://nvd.nist.gov/vuln/detail/CVE-2026-71533) | Medium | 6.8 | Mareforma is a local verification layer for AI-assisted research. From 0.3.7 until 0.3.8, search_claims in mareforma/db… |
| 2026-11-18 23:17:21 | [CVE-2026-71534](https://nvd.nist.gov/vuln/detail/CVE-2026-71534) | Medium | 6.9 | Mareforma is a local verification layer for AI-assisted research. From 0.3.0 until 0.3.8, restore logic in mareforma/db… |
| 2026-11-18 23:17:21 | [CVE-2026-71535](https://nvd.nist.gov/vuln/detail/CVE-2026-71535) | High | 7.1 | Mareforma is a local verification layer for AI-assisted research. From 0.3.0 until 0.3.7, the _maybe_update_replicated_… |
| 2026-11-18 23:17:21 | [CVE-2026-71536](https://nvd.nist.gov/vuln/detail/CVE-2026-71536) | High | 7.0 | Mareforma is a local verification layer for AI-assisted research. From 0.3.0 until 0.3.8, verify_bundle in mareforma/ex… |
| 2026-11-18 23:17:21 | [CVE-2026-77283](https://nvd.nist.gov/vuln/detail/CVE-2026-77283) | High | 8.8 | obsidian-sync-mcp is an MCP server that gives AI agents access to Obsidian vaults. Prior to 0.5.7, deployments running… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
