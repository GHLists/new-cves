# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-01 18:21 UTC

New CVEs published between 2026-10-01 17:18 UTC and 2026-10-01 18:21 UTC.

[Full CSV](data/new-cves-2026-10-01T18-21-44-360506Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-10-01 18:17:11 | [CVE-2023-54404](https://nvd.nist.gov/vuln/detail/CVE-2023-54404) | High | 8.2 | Zod schema-validation library through 4.6.5 contains an uncontrolled resource consumption vulnerability that allows att… |
| 2026-10-01 18:17:12 | [CVE-2026-102294](https://nvd.nist.gov/vuln/detail/CVE-2026-102294) | High | 8.5 | TP-Link TL-WR841N contains an authenticated OS command injection vulnerability in the IPv6 WAN configuration. A crafted… |
| 2026-10-01 18:17:12 | [CVE-2026-102369](https://nvd.nist.gov/vuln/detail/CVE-2026-102369) | High | 8.7 | Tapo C120 v1 and C200 V5 do not adequately protect login challenge data or sanitize attacker-controlled input processed… |
| 2026-10-01 18:17:12 | [CVE-2026-103884](https://nvd.nist.gov/vuln/detail/CVE-2026-103884) | Medium | 6.5 | A flaw was found in the X.509 client certificate authenticator of Keycloak. When CRL Distribution Point checking is ena… |
| 2026-10-01 18:17:12 | [CVE-2026-103922](https://nvd.nist.gov/vuln/detail/CVE-2026-103922) | Critical | 9.3 | Capacitor is a cross-platform native runtime for web applications. From 6.0.0 until 6.2.2, 7.6.9, 8.3.5, 8.4.3, and 8.5… |
| 2026-10-01 18:17:13 | [CVE-2026-103923](https://nvd.nist.gov/vuln/detail/CVE-2026-103923) | Low | 2.1 | KaTeX is a fast, easy-to-use JavaScript library for TeX math rendering on the web. From 0.11.0 until 0.18.2, KaTeX uses… |
| 2026-10-01 18:17:14 | [CVE-2026-104018](https://nvd.nist.gov/vuln/detail/CVE-2026-104018) | High | 8.8 | An improper privilege management vulnerability (CWE-269) exists in the command shell of Wind River VxWorks 7 all versio… |
| 2026-10-01 18:17:15 | [CVE-2026-12542](https://nvd.nist.gov/vuln/detail/CVE-2026-12542) | Medium | 5.3 | A flaw was found in Foreman. The foreman-tail utility is vulnerable to OS command injection due to the unsafe use of th… |
| 2026-10-01 18:17:15 | [CVE-2026-12545](https://nvd.nist.gov/vuln/detail/CVE-2026-12545) | Medium | 6.7 | A flaw was found in rubygem-hammer_cli. A command injection vulnerability exists in Hammer CLI and the Railties (Ruby o… |
| 2026-10-01 18:17:19 | [CVE-2026-56097](https://nvd.nist.gov/vuln/detail/CVE-2026-56097) | Medium | 6.5 | A flaw was found in rubygem-katello. An SQL injection vulnerability exists in the Red Hat Satellite Katello Registry Pr… |
| 2026-10-01 18:17:19 | [CVE-2026-56098](https://nvd.nist.gov/vuln/detail/CVE-2026-56098) | Medium | 4.3 | A flaw was found in rubygem-katello. The RegistryProxiesController in Katello contains an authorization bypass vulnerab… |
| 2026-10-01 18:17:27 | [CVE-2026-68495](https://nvd.nist.gov/vuln/detail/CVE-2026-68495) | High | 7.5 | The CBOR parser in FasterXML jackson-dataformats-binary never invokes StreamReadConstraints.validateNameLength() when d… |
| 2026-10-01 18:17:27 | [CVE-2026-68496](https://nvd.nist.gov/vuln/detail/CVE-2026-68496) | High | 7.5 | The Smile parser in FasterXML jackson-dataformats-binary never invokes StreamReadConstraints.validateNameLength() when… |
| 2026-10-01 18:17:27 | [CVE-2026-73976](https://nvd.nist.gov/vuln/detail/CVE-2026-73976) | High | 7.1 | djehuty is a research data repository system developed by 4TU.ResearchData. Prior to version 26.3.2, An unauthenticated… |
| 2026-10-01 18:17:27 | [CVE-2026-78577](https://nvd.nist.gov/vuln/detail/CVE-2026-78577) | Medium | 5.3 | Tapo C120 v1 and C200 V5 contain a vulnerability in the HTTPS onboarding scan function due to missing authentication. A… |
| 2026-10-01 18:17:27 | [CVE-2026-78578](https://nvd.nist.gov/vuln/detail/CVE-2026-78578) | High | 7.1 | Tapo C120 v1 and C200 v5 do not enforce authentication for do method HTTPS onboarding connect actions after initial set… |
| 2026-10-01 18:17:29 | [CVE-2026-97662](https://nvd.nist.gov/vuln/detail/CVE-2026-97662) | Medium | 6.9 | An argument injection issue in the diff scan operation in AWS security-agent-mcp-server before version 0.2.0 might allo… |
| 2026-10-01 18:17:29 | [CVE-2026-9032](https://nvd.nist.gov/vuln/detail/CVE-2026-9032) | High | 7.1 | Tapo C120 v1 and C200 v5 contain a NULL pointer dereference in the HTTPS onboarding connect request parser. The interfa… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
