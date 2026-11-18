# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-11-18 20:22 UTC

New CVEs published between 2026-11-18 19:21 UTC and 2026-11-18 20:22 UTC.

[Full CSV](data/new-cves-2026-11-18T20-22-01-256831Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-11-18 20:18:58 | [CVE-2026-127095](https://nvd.nist.gov/vuln/detail/CVE-2026-127095) | Low | 3.3 | A flaw was found in ansible-builder. The regular expression used to strip comments from a collection's requirements.txt… |
| 2026-11-18 20:18:58 | [CVE-2026-127096](https://nvd.nist.gov/vuln/detail/CVE-2026-127096) | Low | 3.3 | A flaw was found in the Ansible language server shipped with the vscode-ansible extension. The regular expression used… |
| 2026-11-18 20:18:59 | [CVE-2026-128667](https://nvd.nist.gov/vuln/detail/CVE-2026-128667) |  |  | A Cross-Site Request Forgery (CSRF) vulnerability in the admin panel of PHPGurukul News Portal Project V4.1 allows remo… |
| 2026-11-18 20:18:59 | [CVE-2026-128668](https://nvd.nist.gov/vuln/detail/CVE-2026-128668) |  |  | An Unrestricted File Upload vulnerability in the admin panel of PHPGurukul News Portal Project V4.1 allows authenticate… |
| 2026-11-18 20:18:59 | [CVE-2026-128669](https://nvd.nist.gov/vuln/detail/CVE-2026-128669) | High | 7.1 | A Session Fixation vulnerability exists in the admin login endpoint (/admin/index.php) of PHPGurukul News Portal Projec… |
| 2026-11-18 20:18:59 | [CVE-2026-129829](https://nvd.nist.gov/vuln/detail/CVE-2026-129829) | Medium | 5.5 | The rsyslog's`imuxsock` special parser can end up writing into the received message raw buffer when trying to replace t… |
| 2026-11-18 20:19:09 | [CVE-2026-132136](https://nvd.nist.gov/vuln/detail/CVE-2026-132136) | Medium | 5.5 | A weakness has been identified in Directus up to 12.6.1. Affected by this issue is the function getSecret of the file a… |
| 2026-11-18 20:19:10 | [CVE-2026-62245](https://nvd.nist.gov/vuln/detail/CVE-2026-62245) | Medium | 6.5 | X-Road is open-source data exchange layer software. Prior to 7.8.2, 7.7.3, and 7.6.4, HashChainVerifier in the common-m… |
| 2026-11-18 20:19:10 | [CVE-2026-62340](https://nvd.nist.gov/vuln/detail/CVE-2026-62340) | High | 8.0 | X-Road is open-source data exchange layer software. Prior to .8.2, 7.7.3, and 7.6.5, the Security Server writes each do… |
| 2026-11-18 20:19:10 | [CVE-2026-63129](https://nvd.nist.gov/vuln/detail/CVE-2026-63129) | High | 8.8 | mssql-mcp-core is the shared library that powers MSSQL MCP servers. Prior to core and server 0.6.0 and reader and write… |
| 2026-11-18 20:19:10 | [CVE-2026-63483](https://nvd.nist.gov/vuln/detail/CVE-2026-63483) | Medium | 6.6 | X-Road is open-source data exchange layer software. Prior to 7.8.2 and 7.7.3, the Configuration Proxy uses attacker-con… |
| 2026-11-18 20:19:11 | [CVE-2026-68903](https://nvd.nist.gov/vuln/detail/CVE-2026-68903) | High | 7.7 | LLMKube is a Kubernetes operator for self-hosted large language model inference across heterogeneous hardware. Prior to… |
| 2026-11-18 20:19:12 | [CVE-2026-71425](https://nvd.nist.gov/vuln/detail/CVE-2026-71425) | Medium | 6.5 | Outstatic is a static site CMS for Markdown and MDX content stored in GitHub repositories. Prior to 2.2.1, the authenti… |
| 2026-11-18 20:19:12 | [CVE-2026-73504](https://nvd.nist.gov/vuln/detail/CVE-2026-73504) | Medium | 5.5 | cassandra-jdbc-wrapper provides a JDBC-compliant API over the Java driver for Apache Cassandra. Prior to 4.16.4 and 5.0… |
| 2026-11-18 20:19:12 | [CVE-2026-76090](https://nvd.nist.gov/vuln/detail/CVE-2026-76090) | High | 8.4 | Tapir is a Scala library for describing HTTP APIs and exposing, consuming, and documenting them using open standards. P… |
| 2026-11-18 20:19:13 | [CVE-2026-76807](https://nvd.nist.gov/vuln/detail/CVE-2026-76807) | Critical | 9.3 | Todoist MCP Server provides tools that allow AI agents to access and modify a Todoist account. Prior to 10.3.3, the opt… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
