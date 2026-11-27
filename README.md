# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-11-27 20:22 UTC

New CVEs published between 2026-11-27 19:18 UTC and 2026-11-27 20:22 UTC.

[Full CSV](data/new-cves-2026-11-27T20-22-04-752699Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-11-27 20:18:16 | [CVE-2026-131776](https://nvd.nist.gov/vuln/detail/CVE-2026-131776) | High | 7.1 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in Hai Zheng / Lite… |
| 2026-11-27 20:18:17 | [CVE-2026-137898](https://nvd.nist.gov/vuln/detail/CVE-2026-137898) | High | 7.3 | A flaw was found in pam. When built with libeconf and an unconfigured vendor directory, the pam_econf configuration han… |
| 2026-11-27 20:18:17 | [CVE-2026-138026](https://nvd.nist.gov/vuln/detail/CVE-2026-138026) | Medium | 6.9 | Crypto APIs MCP server packages (@cryptoapis-io/mcp-*) before 0.4.0, mcp-blockchain-events, mcp-blockchain-fees, mcp-br… |
| 2026-11-27 20:18:18 | [CVE-2026-138027](https://nvd.nist.gov/vuln/detail/CVE-2026-138027) | High | 7.7 | Bagel (bagel-mcp) before 2.5.5 exposes unsandboxed DuckDB SQL execution through the read-only annotated query_messages… |
| 2026-11-27 20:18:18 | [CVE-2026-138028](https://nvd.nist.gov/vuln/detail/CVE-2026-138028) | High | 7.7 | Bagel (bagel-mcp) before 2.5.5 contains an argument injection vulnerability in RsyncFilesToLocalDirectory that allows a… |
| 2026-11-27 20:18:18 | [CVE-2026-138029](https://nvd.nist.gov/vuln/detail/CVE-2026-138029) | Medium | 5.3 | Wazuh-MCP-Server before commit 2bbfe12 contains a server-side request forgery vulnerability in the blueteam_check_websh… |
| 2026-11-27 20:18:18 | [CVE-2026-138030](https://nvd.nist.gov/vuln/detail/CVE-2026-138030) | Low | 2.3 | SylphxAI pdf-reader-mcp 2.4.1 through 3.0.14, 3.0.16, and 3.1.2 through 3.1.4 contains a server-side request forgery vu… |
| 2026-11-27 20:18:18 | [CVE-2026-138031](https://nvd.nist.gov/vuln/detail/CVE-2026-138031) | High | 7.6 | Typebot from 2.14.0 before 3.19.0 contains an authorization flaw that allows authenticated bot authors to reference ano… |
| 2026-11-27 20:18:18 | [CVE-2026-138032](https://nvd.nist.gov/vuln/detail/CVE-2026-138032) | Medium | 6.0 | WhoDB from 0.88.0 before 0.132.0 contains an access control bypass in the MCP whodb_query tool, letting callers run fil… |
| 2026-11-27 20:18:19 | [CVE-2026-138033](https://nvd.nist.gov/vuln/detail/CVE-2026-138033) | High | 7.0 | mcp-video-analyzer 0.2.0 before 0.10.1 contains a server-side request forgery vulnerability that allows attackers to re… |
| 2026-11-27 20:18:19 | [CVE-2026-138034](https://nvd.nist.gov/vuln/detail/CVE-2026-138034) | High | 8.7 | bigcommerce-api-mcp before 1.0.1 contains a missing authentication vulnerability that allows remote unauthenticated att… |
| 2026-11-27 20:18:19 | [CVE-2026-138048](https://nvd.nist.gov/vuln/detail/CVE-2026-138048) | Medium | 6.9 | ntfy before v2.38.3 contains a server-side request forgery vulnerability that allows remote attackers to bypass the web… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
