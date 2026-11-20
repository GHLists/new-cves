# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-11-20 19:21 UTC

New CVEs published between 2026-11-20 18:19 UTC and 2026-11-20 19:21 UTC.

[Full CSV](data/new-cves-2026-11-20T19-21-16-783598Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-11-20 19:18:34 | [CVE-2026-106075](https://nvd.nist.gov/vuln/detail/CVE-2026-106075) |  |  | Rocket.Chat's POST /api/v1/chat.sendMessage endpoint improperly validates nested message properties, allowing authentic… |
| 2026-11-20 19:18:38 | [CVE-2026-124281](https://nvd.nist.gov/vuln/detail/CVE-2026-124281) | Medium | 5.3 | The affected products use an unprotected firmware-update channel, which may allow for unauthorized firmware modificatio… |
| 2026-11-20 19:18:39 | [CVE-2026-125132](https://nvd.nist.gov/vuln/detail/CVE-2026-125132) | High | 8.8 | libumqtt is vulnerable to an integer underflow which may allow a remote attacker to cause a denial of service, memory c… |
| 2026-11-20 19:18:39 | [CVE-2026-125273](https://nvd.nist.gov/vuln/detail/CVE-2026-125273) | High | 8.5 | No replay or command-integrity protection. Commands lack sequence numbers, nonces, or session tokens; captured commands… |
| 2026-11-20 19:18:42 | [CVE-2026-129007](https://nvd.nist.gov/vuln/detail/CVE-2026-129007) | High | 7.1 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in Knit Pay Knit Pay… |
| 2026-11-20 19:18:42 | [CVE-2026-129029](https://nvd.nist.gov/vuln/detail/CVE-2026-129029) | High | 7.2 | Server-Side Request Forgery (SSRF) vulnerability in Brainstorm Force OttoKit suretriggers allows Server Side Request Fo… |
| 2026-11-20 19:18:42 | [CVE-2026-129033](https://nvd.nist.gov/vuln/detail/CVE-2026-129033) | High | 7.1 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in Ays Pro Quiz Make… |
| 2026-11-20 19:18:43 | [CVE-2026-129037](https://nvd.nist.gov/vuln/detail/CVE-2026-129037) | High | 7.1 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in Ahmad WP Job Port… |
| 2026-11-20 19:18:43 | [CVE-2026-129042](https://nvd.nist.gov/vuln/detail/CVE-2026-129042) | High | 7.1 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in Tribulant Softwar… |
| 2026-11-20 19:18:43 | [CVE-2026-129054](https://nvd.nist.gov/vuln/detail/CVE-2026-129054) | High | 7.5 | Insertion of Sensitive Information Into Sent Data vulnerability in Datasolution AcyMailing SMTP Newsletter acymailing a… |
| 2026-11-20 19:18:43 | [CVE-2026-129055](https://nvd.nist.gov/vuln/detail/CVE-2026-129055) | Medium | 6.5 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in Codepeople Appoin… |
| 2026-11-20 19:18:43 | [CVE-2026-129063](https://nvd.nist.gov/vuln/detail/CVE-2026-129063) | High | 7.1 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in Brainstorm Force… |
| 2026-11-20 19:18:44 | [CVE-2026-129995](https://nvd.nist.gov/vuln/detail/CVE-2026-129995) | High | 8.8 | mcp-ssh-manager is an MCP server for managing servers over SSH with human approval, an encrypted vault, and a live audi… |
| 2026-11-20 19:18:44 | [CVE-2026-130601](https://nvd.nist.gov/vuln/detail/CVE-2026-130601) | High | 7.1 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in BdThemes Element… |
| 2026-11-20 19:18:44 | [CVE-2026-130602](https://nvd.nist.gov/vuln/detail/CVE-2026-130602) | High | 7.1 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in BdThemes Prime Sl… |
| 2026-11-20 19:18:44 | [CVE-2026-130901](https://nvd.nist.gov/vuln/detail/CVE-2026-130901) | Medium | 5.8 | Improper limitation of a pathname to a restricted directory in the file access checks in Amazon awslabs.document-loader… |
| 2026-11-20 19:18:51 | [CVE-2026-133949](https://nvd.nist.gov/vuln/detail/CVE-2026-133949) | Critical | 9.3 | pip prior to v26.2.2 the certifi bundled with pip contains the compromised eMudhra certificates. Upgrading to a secure… |
| 2026-11-20 19:18:51 | [CVE-2026-133968](https://nvd.nist.gov/vuln/detail/CVE-2026-133968) | Critical | 9.8 | monailabel (aka MONAI Label) through 0.8.5 allows directory traversal, with resultant remote code execution, via the im… |
| 2026-11-20 19:18:51 | [CVE-2026-48118](https://nvd.nist.gov/vuln/detail/CVE-2026-48118) | High | 8.2 | NukeViet CMS is a multi Content Management System. Prior to 4.5.09, the Comment module accepts attacker-controlled base… |
| 2026-11-20 19:18:52 | [CVE-2026-49259](https://nvd.nist.gov/vuln/detail/CVE-2026-49259) | High | 8.7 | NukeViet CMS is a multi Content Management System. From the 4.x release line until 4.5.09, a low-privileged authenticat… |
| 2026-11-20 19:18:52 | [CVE-2026-54064](https://nvd.nist.gov/vuln/detail/CVE-2026-54064) | High | 8.7 | NukeViet CMS is a multi Content Management System. Prior to 4.5.09, a user with news-posting permission can bypass Nuke… |
| 2026-11-20 19:18:52 | [CVE-2026-54065](https://nvd.nist.gov/vuln/detail/CVE-2026-54065) | High | 8.7 | NukeViet CMS is a multi Content Management System. Prior to 4.5.09, an authenticated administrator can submit a crafted… |
| 2026-11-20 19:18:52 | [CVE-2026-55372](https://nvd.nist.gov/vuln/detail/CVE-2026-55372) | High | 7.2 | NukeViet CMS is a multi Content Management System. Prior to 4.5.09, an unauthenticated attacker can submit the __server… |
| 2026-11-20 19:18:52 | [CVE-2026-61832](https://nvd.nist.gov/vuln/detail/CVE-2026-61832) | High | 7.5 | NukeViet CMS is a multi Content Management System. Prior to 4.6.00, a network attacker who can alter outbound traffic t… |
| 2026-11-20 19:18:53 | [CVE-2026-77323](https://nvd.nist.gov/vuln/detail/CVE-2026-77323) | Medium | 5.3 | MapServer is a system for developing web-based GIS applications. Prior to 8.6.5, an unauthenticated reflected cross-sit… |
| 2026-11-20 19:18:53 | [CVE-2026-77324](https://nvd.nist.gov/vuln/detail/CVE-2026-77324) | High | 7.5 | MapServer is a system for developing web-based GIS applications. From 4.4.0 until 8.6.5, an unauthenticated remote atta… |
| 2026-11-20 19:18:53 | [CVE-2026-77325](https://nvd.nist.gov/vuln/detail/CVE-2026-77325) | Medium | 6.1 | MapServer is a system for developing web-based GIS applications. From 6.0 until 8.6.5, MapServer's WMS OpenLayers outpu… |
| 2026-11-20 19:18:54 | [CVE-2026-77326](https://nvd.nist.gov/vuln/detail/CVE-2026-77326) | High | 8.6 | MapServer is a system for developing web-based GIS applications. From 8.2.0 until 8.6.5, an unauthenticated attacker ca… |
| 2026-11-20 19:18:54 | [CVE-2026-77327](https://nvd.nist.gov/vuln/detail/CVE-2026-77327) | Medium | 6.9 | MapServer is a system for developing web-based GIS applications. Prior to 8.6.5, MapServer's MySQL JOIN implementation… |
| 2026-11-20 19:18:54 | [CVE-2026-77328](https://nvd.nist.gov/vuln/detail/CVE-2026-77328) | Medium | 6.9 | MapServer is a system for developing web-based GIS applications. Prior to 8.6.5, MapServer's PostgreSQL JOIN implementa… |
| 2026-11-20 19:18:54 | [CVE-2026-77346](https://nvd.nist.gov/vuln/detail/CVE-2026-77346) | Medium | 6.3 | Pozeiden is a MermaidJS renderer written in Zig. Prior to 0.3.0, Pozeiden emits attacker-controlled Mermaid values into… |
| 2026-11-20 19:18:54 | [CVE-2026-77347](https://nvd.nist.gov/vuln/detail/CVE-2026-77347) | High | 8.8 | Pozeiden is a MermaidJS renderer written in Zig. Prior to 0.3.0, src/renderers/c4.zig, src/renderers/class.zig, src/ren… |
| 2026-11-20 19:18:54 | [CVE-2026-77355](https://nvd.nist.gov/vuln/detail/CVE-2026-77355) | High | 8.8 | isomorphic-git is a pure JavaScript implementation of Git for Node.js and browsers. Prior to 1.38.7, tree-entry validat… |
| 2026-11-20 19:18:55 | [CVE-2026-77383](https://nvd.nist.gov/vuln/detail/CVE-2026-77383) | High | 8.7 | mcp-ssh-manager is an MCP server for managing servers over SSH with human approval, an encrypted vault, and a live audi… |
| 2026-11-20 19:18:55 | [CVE-2026-86017](https://nvd.nist.gov/vuln/detail/CVE-2026-86017) | High | 8.0 | isomorphic-git is a pure JavaScript implementation of Git for Node.js and browsers. Prior to 1.38.8, git cherry-pick ap… |
| 2026-11-20 19:18:55 | [CVE-2026-94561](https://nvd.nist.gov/vuln/detail/CVE-2026-94561) | High | 7.2 | NukeViet CMS is a multi Content Management System. In 4.6.00, an unauthenticated attacker can place the configured doma… |
| 2026-11-20 19:18:56 | [CVE-2026-94562](https://nvd.nist.gov/vuln/detail/CVE-2026-94562) | High | 7.2 | NukeViet CMS is a multi Content Management System. Prior to 4.6.01, a super-administrator satisfying the NV_IS_SPADMIN… |
| 2026-11-20 19:18:56 | [CVE-2026-94563](https://nvd.nist.gov/vuln/detail/CVE-2026-94563) | Medium | 6.0 | NukeViet CMS is a multi Content Management System. From 4.5.00 until 4.6.01, an authenticated settings-module administr… |
| 2026-11-20 19:18:56 | [CVE-2026-94564](https://nvd.nist.gov/vuln/detail/CVE-2026-94564) | High | 8.2 | NukeViet CMS is a multi Content Management System. Prior to 4.6.01, an unauthenticated visitor can submit Contact modul… |
| 2026-11-20 19:18:56 | [CVE-2026-94565](https://nvd.nist.gov/vuln/detail/CVE-2026-94565) | Critical | 9.3 | NukeViet CMS is a multi Content Management System. From the 3.x release line until 4.6.01, an unauthenticated visitor c… |
| 2026-11-20 19:18:56 | [CVE-2026-94566](https://nvd.nist.gov/vuln/detail/CVE-2026-94566) | Medium | 5.3 | NukeViet CMS is a multi Content Management System. In 4.6.00, an unauthenticated attacker can rotate X-Forwarded-For be… |
| 2026-11-20 19:18:56 | [CVE-2026-94567](https://nvd.nist.gov/vuln/detail/CVE-2026-94567) | Critical | 9.3 | NukeViet CMS is a multi Content Management System. Prior to 4.5.12 and 4.6.02, an attacker with access to an SVG upload… |
| 2026-11-20 19:18:56 | [CVE-2026-94597](https://nvd.nist.gov/vuln/detail/CVE-2026-94597) | High | 7.5 | NukeViet CMS is a multi Content Management System. Prior to 4.5.12 and 4.6.02, an attacker who can reach an image-uploa… |
| 2026-11-20 19:18:57 | [CVE-2026-94598](https://nvd.nist.gov/vuln/detail/CVE-2026-94598) | High | 8.2 | NukeViet CMS is a multi Content Management System. From 4.5.08 until 4.5.12 and 4.6.02, an attacker can place NukeViet'… |
| 2026-11-20 19:18:57 | [CVE-2026-94599](https://nvd.nist.gov/vuln/detail/CVE-2026-94599) | Medium | 6.1 | NukeViet CMS is a multi Content Management System. From 4.5.00 until 4.5.13 and 4.6.02, an unauthenticated attacker can… |
| 2026-11-20 19:18:58 | [CVE-2026-96805](https://nvd.nist.gov/vuln/detail/CVE-2026-96805) | High | 8.5 | The affected products have an unauthenticated command injection, which may allow an in-range BLE device to gain access… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
