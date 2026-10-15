# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-15 16:22 UTC

New CVEs published between 2026-10-15 15:20 UTC and 2026-10-15 16:22 UTC.

[Full CSV](data/new-cves-2026-10-15T16-22-15-162676Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-10-15 16:17:30 | [CVE-2026-100347](https://nvd.nist.gov/vuln/detail/CVE-2026-100347) | Medium | 5.3 | kin-openapi is a Go project for handling OpenAPI files. Prior to 0.145.0, openapi3filter.ValidationHandler uses the rou… |
| 2026-10-15 16:17:30 | [CVE-2026-100348](https://nvd.nist.gov/vuln/detail/CVE-2026-100348) | Medium | 5.3 | kin-openapi is a Go project for handling OpenAPI files. Prior to 0.145.0, openapi3.Loader can dereference a nil SchemaR… |
| 2026-10-15 16:17:30 | [CVE-2026-100349](https://nvd.nist.gov/vuln/detail/CVE-2026-100349) | High | 8.2 | kin-openapi is a Go project for handling OpenAPI files. Prior to 0.146.0, openapi3filter.ValidateResponse passes a nil… |
| 2026-10-15 16:17:30 | [CVE-2026-100350](https://nvd.nist.gov/vuln/detail/CVE-2026-100350) | Medium | 5.3 | kin-openapi is a Go project for handling OpenAPI files. From 0.145.0 until 0.146.0, openapi3filter repeatedly calls reg… |
| 2026-10-15 16:17:31 | [CVE-2026-100351](https://nvd.nist.gov/vuln/detail/CVE-2026-100351) | High | 7.4 | kin-openapi is a Go project for handling OpenAPI files. From 0.144.0 until 0.147.0, openapi3filter.ValidationHandler va… |
| 2026-10-15 16:17:31 | [CVE-2026-100352](https://nvd.nist.gov/vuln/detail/CVE-2026-100352) | High | 7.5 | kin-openapi is a Go project for handling OpenAPI files. Prior to 0.148.0, the OpenAPI 3.1 validation path passes YAML N… |
| 2026-10-15 16:17:34 | [CVE-2026-105474](https://nvd.nist.gov/vuln/detail/CVE-2026-105474) | Critical | 9.4 | A server-side template injection exists in SolusVM 2 up to version 2.0.0-44576 that allows remote authenticated users t… |
| 2026-10-15 16:17:43 | [CVE-2026-109449](https://nvd.nist.gov/vuln/detail/CVE-2026-109449) | High | 8.7 | In Symfony Expression Language versions prior to 5.4.54, 6.4.48, 7.4.21, and 8.1.9, the parser of the ExpressionLanguag… |
| 2026-10-15 16:17:48 | [CVE-2026-110958](https://nvd.nist.gov/vuln/detail/CVE-2026-110958) | Critical | 9.3 | A vulnerability was found in Wavlink WN530HG4B M30HG4B_V260724. The impacted element is an unknown function of the file… |
| 2026-10-15 16:17:48 | [CVE-2026-111091](https://nvd.nist.gov/vuln/detail/CVE-2026-111091) | High | 7.8 | In JetBrains Junie CLI before 26.8.3 code execution was possible via an untrusted project's MCP server configuration |
| 2026-10-15 16:17:48 | [CVE-2026-111092](https://nvd.nist.gov/vuln/detail/CVE-2026-111092) | Medium | 6.5 | In JetBrains YouTrack before 2026.2.19575 2026.3.16075 2026.3.16397 2026.3.16402 mail rules allowed a project admin to… |
| 2026-10-15 16:17:48 | [CVE-2026-111093](https://nvd.nist.gov/vuln/detail/CVE-2026-111093) | High | 7.5 | In JetBrains Datalore before 2026.2.1 unauthenticated path traversal via the report blob endpoint allowed reading arbit… |
| 2026-10-15 16:17:48 | [CVE-2026-111094](https://nvd.nist.gov/vuln/detail/CVE-2026-111094) | High | 8.1 | In JetBrains TeamCity before 2026.2, 2026.1.4, 2025.11.8 remote code execution via a whitelist bypass in the build mess… |
| 2026-10-15 16:17:49 | [CVE-2026-111095](https://nvd.nist.gov/vuln/detail/CVE-2026-111095) | High | 8.0 | In JetBrains TeamCity before 2026.2, 2026.1.4, 2025.11.8 stored XSS in the classic project overview was possible |
| 2026-10-15 16:17:49 | [CVE-2026-111096](https://nvd.nist.gov/vuln/detail/CVE-2026-111096) | Medium | 6.7 | In JetBrains TeamCity before 2026.2, 2026.1.4, 2025.11.8 stored XSS in the classic build log was possible |
| 2026-10-15 16:18:10 | [CVE-2026-45449](https://nvd.nist.gov/vuln/detail/CVE-2026-45449) | High | 8.3 | : Improper Neutralization of Special Elements used in an OS Command ('OS Command Injection') vulnerability in Unitronic… |
| 2026-10-15 16:18:11 | [CVE-2026-45450](https://nvd.nist.gov/vuln/detail/CVE-2026-45450) | High | 8.3 | : Improper Restriction of Operations within the Bounds of a Memory Buffer vulnerability in Unitronics Unitronics UniStr… |
| 2026-10-15 16:18:11 | [CVE-2026-45451](https://nvd.nist.gov/vuln/detail/CVE-2026-45451) | High | 8.3 | : Improper Authentication vulnerability in Unitronics Unitronics UniStream Pro/UniLogic. This issue affects Unitronics… |
| 2026-10-15 16:18:11 | [CVE-2026-45452](https://nvd.nist.gov/vuln/detail/CVE-2026-45452) | High | 8.3 | Use of Externally-Controlled format string vulnerability in Unitronics Unitronics UniStream Pro/UniLogic. This issue af… |
| 2026-10-15 16:18:12 | [CVE-2026-52167](https://nvd.nist.gov/vuln/detail/CVE-2026-52167) |  |  | A stack overflow in the gensub_ParsePsb() function of AOC LC32D1320 v2.05 allows attackers to cause a Denial of Service… |
| 2026-10-15 16:18:12 | [CVE-2026-53582](https://nvd.nist.gov/vuln/detail/CVE-2026-53582) | High | 7.1 | OPNsense is a FreeBSD based firewall and routing platform. Prior to version 26.1.10, the Trust module stores attacker-c… |
| 2026-10-15 16:18:17 | [CVE-2026-57155](https://nvd.nist.gov/vuln/detail/CVE-2026-57155) | Critical | 9.9 | OPNsense is a FreeBSD based firewall and routing platform. Prior to version 26.1.11, the Firewall Alias GeoIP importer'… |
| 2026-10-15 16:18:17 | [CVE-2026-58390](https://nvd.nist.gov/vuln/detail/CVE-2026-58390) | High | 8.0 | OPNsense is a FreeBSD based firewall and routing platform. Prior to version 26.1.11, the OpenVPN connection-status dash… |
| 2026-10-15 16:18:18 | [CVE-2026-58391](https://nvd.nist.gov/vuln/detail/CVE-2026-58391) | Medium | 5.4 | OPNsense is a FreeBSD based firewall and routing platform. Prior to version 26.1.11, Firewall Rules and NAT views place… |
| 2026-10-15 16:18:18 | [CVE-2026-58392](https://nvd.nist.gov/vuln/detail/CVE-2026-58392) | Medium | 5.4 | OPNsense is a FreeBSD based firewall and routing platform. Prior to version 26.1.11, the NTP GPS page stores the operat… |
| 2026-10-15 16:18:18 | [CVE-2026-58393](https://nvd.nist.gov/vuln/detail/CVE-2026-58393) | Medium | 5.9 | OPNsense is a FreeBSD based firewall and routing platform. Prior to version 26.1.11, the OpenVPN Client Specific Overri… |
| 2026-10-15 16:18:18 | [CVE-2026-58394](https://nvd.nist.gov/vuln/detail/CVE-2026-58394) | Medium | 5.2 | OPNsense is a FreeBSD based firewall and routing platform. Prior to version 26.1.11, src/www/system_advanced_admin.php… |
| 2026-10-15 16:18:18 | [CVE-2026-58395](https://nvd.nist.gov/vuln/detail/CVE-2026-58395) | Medium | 4.3 | OPNsense is a FreeBSD based firewall and routing platform. Prior to version 26.1.11, the safe-delete path reached throu… |
| 2026-10-15 16:18:19 | [CVE-2026-63442](https://nvd.nist.gov/vuln/detail/CVE-2026-63442) | High | 8.1 | OPNsense is a FreeBSD based firewall and routing platform. Prior to version 26.1.11, the unauthenticated WebGUI login u… |
| 2026-10-15 16:18:19 | [CVE-2026-71490](https://nvd.nist.gov/vuln/detail/CVE-2026-71490) | High | 7.1 | OPNsense is a FreeBSD based firewall and routing platform. Prior to 26.1.11, OPNsense\Core\ACL::hasPrivilege() appends… |
| 2026-10-15 16:18:20 | [CVE-2026-75505](https://nvd.nist.gov/vuln/detail/CVE-2026-75505) | Medium | 6.0 | EspoCRM is an open source customer relationship management application. Prior to 10.0.2, an authenticated user with mas… |
| 2026-10-15 16:18:22 | [CVE-2026-88753](https://nvd.nist.gov/vuln/detail/CVE-2026-88753) |  |  | A Regular-Expression Denial of Service (ReDoS) in the Markdown2. extract_metadata() function (lib/markdown2.py) of tren… |
| 2026-10-15 16:18:23 | [CVE-2026-92982](https://nvd.nist.gov/vuln/detail/CVE-2026-92982) | High | 8.5 | A flaw was found in Ansible Operator Plugins. A low-privileged Kubernetes user can exploit a Jinja2 template injection… |
| 2026-10-15 16:18:24 | [CVE-2026-95155](https://nvd.nist.gov/vuln/detail/CVE-2026-95155) |  |  | FasterXML Jackson 1.x, confirmed in jackson-mapper-asl versions 1.8.3, 1.9.2, 1.9.11, 1.9.12, and 1.9.13, allows attack… |
| 2026-10-15 16:18:25 | [CVE-2026-97394](https://nvd.nist.gov/vuln/detail/CVE-2026-97394) | High | 7.5 | kin-openapi is a Go project for handling OpenAPI files. From 0.136.0 until 0.143.0, openapi3filter accepts OpenAPI 3.1… |
| 2026-10-15 16:18:25 | [CVE-2026-97665](https://nvd.nist.gov/vuln/detail/CVE-2026-97665) | High | 7.1 | A missing authorization check in Nexus Repository 3's NuGet Components API upload path allows an account holding only r… |
| 2026-10-15 16:18:25 | [CVE-2026-97666](https://nvd.nist.gov/vuln/detail/CVE-2026-97666) | Medium | 6.9 | Sonatype Nexus Repository 3 allows an unauthenticated remote attacker to supply attacker-controlled input to a Java cla… |
| 2026-10-15 16:18:25 | [CVE-2026-97667](https://nvd.nist.gov/vuln/detail/CVE-2026-97667) | Medium | 5.1 | Sonatype Nexus Repository 3 allows a user account that holds the edit permission on a hosted R repository to store scri… |
| 2026-10-15 16:18:26 | [CVE-2026-97712](https://nvd.nist.gov/vuln/detail/CVE-2026-97712) | High | 8.7 | Sonatype Nexus Repository 3 allows a user that holds the role create or role update permission to grant roles and privi… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
