# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-09-27 18:19 UTC

New CVEs published between 2026-09-27 17:20 UTC and 2026-09-27 18:19 UTC.

[Full CSV](data/new-cves-2026-09-27T18-19-12-351584Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-09-27 18:16:29 | [CVE-2026-101043](https://nvd.nist.gov/vuln/detail/CVE-2026-101043) | High | 8.3 | pnpm versions 11.0.0 before 11.11.0 and 10.7.0 before 10.34.5 expand ${VAR} environment-variable placeholders in the ht… |
| 2026-09-27 18:16:30 | [CVE-2026-101044](https://nvd.nist.gov/vuln/detail/CVE-2026-101044) | High | 7.1 | pacquet, the Rust package-manager component shipped in the pnpm npm package versions >=12.0.0-alpha.0 and <12.0.0-alpha… |
| 2026-09-27 18:16:30 | [CVE-2026-101045](https://nvd.nist.gov/vuln/detail/CVE-2026-101045) | High | 8.9 | Fleet-maintained app install and uninstall scripts for macOS are generated from Homebrew cask metadata. In manifests ge… |
| 2026-09-27 18:16:31 | [CVE-2026-101046](https://nvd.nist.gov/vuln/detail/CVE-2026-101046) | Low | 2.3 | Fleet before 4.89.0 contains an SQL injection vulnerability in the activity list endpoints (GET /api/v1/fleet/activitie… |
| 2026-09-27 18:16:31 | [CVE-2026-101047](https://nvd.nist.gov/vuln/detail/CVE-2026-101047) | Medium | 6.9 | Fleet before 4.87.0 does not protect the two endpoints that serve in-house iOS application packages and manifests (ente… |
| 2026-09-27 18:16:31 | [CVE-2026-101048](https://nvd.nist.gov/vuln/detail/CVE-2026-101048) | Medium | 5.3 | Cloudreve before 4.17.0 registers the administrative node test endpoints (POST /api/v4/admin/node/test and POST /api/v4… |
| 2026-09-27 18:16:31 | [CVE-2026-101051](https://nvd.nist.gov/vuln/detail/CVE-2026-101051) | Low | 2.3 | Cloudreve before 4.16.1 fails to properly sanitize file paths returned by remote downloaders, allowing authenticated us… |
| 2026-09-27 18:16:31 | [CVE-2026-101056](https://nvd.nist.gov/vuln/detail/CVE-2026-101056) | Medium | 6.9 | Cloudreve before 4.16.1 fails to revalidate share access when restoring cached navigator state from a context_hint UUID… |
| 2026-09-27 18:16:31 | [CVE-2026-101057](https://nvd.nist.gov/vuln/detail/CVE-2026-101057) | Low | 2.3 | utcp-mcp (the MCP plugin of python-utcp) through 1.1.2 connects to the HTTP and WebSocket MCP server URLs given in a ca… |
| 2026-09-27 18:16:31 | [CVE-2026-101058](https://nvd.nist.gov/vuln/detail/CVE-2026-101058) | High | 7.1 | python-utcp (pip package utcp-http) before 1.1.12 does not verify whether tool URLs declared in a hand-written UTCP man… |
| 2026-09-27 18:16:32 | [CVE-2026-101059](https://nvd.nist.gov/vuln/detail/CVE-2026-101059) | High | 7.1 | utcp-http before 1.1.4 fails to validate the OAuth2 tokenUrl field from remote OpenAPI specifications, allowing attacke… |
| 2026-09-27 18:16:32 | [CVE-2026-101060](https://nvd.nist.gov/vuln/detail/CVE-2026-101060) | High | 8.4 | python-utcp versions before 1.1.4 contain a server-side request forgery vulnerability in HttpCommunicationProtocol.call… |
| 2026-09-27 18:16:32 | [CVE-2026-101061](https://nvd.nist.gov/vuln/detail/CVE-2026-101061) | Low | 2.3 | utcp-gql before 1.1.1 and utcp-websocket before 1.1.1 contain server-side request forgery vulnerabilities due to incomp… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
