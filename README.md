# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-28 14:18 UTC

New CVEs published between 2026-10-28 13:18 UTC and 2026-10-28 14:18 UTC.

[Full CSV](data/new-cves-2026-10-28T14-18-25-659721Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-10-28 14:16:56 | [CVE-2026-105420](https://nvd.nist.gov/vuln/detail/CVE-2026-105420) | Critical | 9.4 | Wing FTP Server does not verify user's base folder. An attacker with admin privileges can add user directories via scri… |
| 2026-10-28 14:16:57 | [CVE-2026-115590](https://nvd.nist.gov/vuln/detail/CVE-2026-115590) | High | 7.2 | Deserialization of Untrusted Data vulnerability in weDevs Dokan dokan-lite allows Object Injection.This issue affects D… |
| 2026-10-28 14:16:57 | [CVE-2026-115603](https://nvd.nist.gov/vuln/detail/CVE-2026-115603) | High | 8.5 | Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection') vulnerability in Advanced Ads GmbH… |
| 2026-10-28 14:16:58 | [CVE-2026-115968](https://nvd.nist.gov/vuln/detail/CVE-2026-115968) | Critical | 9.8 | Deserialization of Untrusted Data vulnerability in Ultimate Member Ultimate Member ultimate-member allows Object Inject… |
| 2026-10-28 14:16:58 | [CVE-2026-116078](https://nvd.nist.gov/vuln/detail/CVE-2026-116078) | High | 8.7 | Allocation of Resources Without Limits or Throttling vulnerability in the HTTP/2 request body reader of mtrudel bandit… |
| 2026-10-28 14:16:58 | [CVE-2026-116389](https://nvd.nist.gov/vuln/detail/CVE-2026-116389) | High | 8.8 | Deserialization of Untrusted Data vulnerability in crossi72 Phoenix Media Rename phoenix-media-rename allows Object Inj… |
| 2026-10-28 14:16:58 | [CVE-2026-116390](https://nvd.nist.gov/vuln/detail/CVE-2026-116390) | High | 7.2 | Deserialization of Untrusted Data vulnerability in stepasyuk Filter Everything&nbsp;— WordPress &amp; WooCommerce Filte… |
| 2026-10-28 14:17:03 | [CVE-2026-50541](https://nvd.nist.gov/vuln/detail/CVE-2026-50541) | Medium | 6.5 | Xibo is an open source digital signage platform with a web content management system and Windows display player softwar… |
| 2026-10-28 14:17:04 | [CVE-2026-52729](https://nvd.nist.gov/vuln/detail/CVE-2026-52729) | High | 7.1 | Xibo is an open source digital signage platform with a web content management system and Windows display player softwar… |
| 2026-10-28 14:17:04 | [CVE-2026-59164](https://nvd.nist.gov/vuln/detail/CVE-2026-59164) | High | 7.1 | NORA is a self-hosted artifact registry and pull-through cache. Prior to 0.9.5, `nora-registry` authenticates the token… |
| 2026-10-28 14:17:04 | [CVE-2026-59172](https://nvd.nist.gov/vuln/detail/CVE-2026-59172) | High | 7.8 | Joker is a small Clojure interpreter, linter and formatter written in Go. Prior to 1.8.2, `joker --lint <file>` walks u… |
| 2026-10-28 14:17:04 | [CVE-2026-59176](https://nvd.nist.gov/vuln/detail/CVE-2026-59176) | High | 7.8 | Functype is a family of TypeScript functional programming libraries. Prior to 1.4.4, the `set_functype_version` MCP too… |
| 2026-10-28 14:17:04 | [CVE-2026-59177](https://nvd.nist.gov/vuln/detail/CVE-2026-59177) | High | 8.8 | ESPHome Device Builder Dashboard is a dashboard for the ESPHome home management software. Prior to 1.0.10, the `Home As… |
| 2026-10-28 14:17:04 | [CVE-2026-59179](https://nvd.nist.gov/vuln/detail/CVE-2026-59179) | High | 8.3 | OpenHop is a tool for creating interactive data-flow diagrams. Prior to 0.3.7, `@openhop/server` passes unauthenticated… |
| 2026-10-28 14:17:05 | [CVE-2026-59185](https://nvd.nist.gov/vuln/detail/CVE-2026-59185) | High | 8.5 | identrail is a machine identity security platform for AWS, GitHub/OIDC, and Kubernetes. Prior to 1.0.2, the default-on… |
| 2026-10-28 14:17:05 | [CVE-2026-59959](https://nvd.nist.gov/vuln/detail/CVE-2026-59959) | Medium | 4.8 | SAIL is a cross-platform library for loading and saving images with support for animation, metadata, and ICC profiles.… |
| 2026-10-28 14:17:08 | [CVE-2026-93517](https://nvd.nist.gov/vuln/detail/CVE-2026-93517) | High | 8.5 | A heap buffer overflow in handling GLX RenderLarge request where dataBytes exceeds cmdlen in X.org X server before 21.1… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
