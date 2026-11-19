# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-11-19 13:18 UTC

New CVEs published between 2026-11-19 12:21 UTC and 2026-11-19 13:18 UTC.

[Full CSV](data/new-cves-2026-11-19T13-18-52-004763Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-11-19 13:17:26 | [CVE-2026-110337](https://nvd.nist.gov/vuln/detail/CVE-2026-110337) | Low | 3.5 | The Strava datasource plugin's resource handler POST /strava-api forwards a client-supplied endpoint string, and its qu… |
| 2026-11-19 13:17:27 | [CVE-2026-111509](https://nvd.nist.gov/vuln/detail/CVE-2026-111509) | Critical | 9.1 | Dell PowerStore SDNAS contains a cryptographically weak PRNG vulnerability that could allow a network attacker to decry… |
| 2026-11-19 13:17:27 | [CVE-2026-115342](https://nvd.nist.gov/vuln/detail/CVE-2026-115342) | High | 8.5 | Argument injection in OpenVPN version 2.4.0 through 2.6.23 and 2.7_alpha1 through 2.7.8 on Windows allows local authent… |
| 2026-11-19 13:17:27 | [CVE-2026-116439](https://nvd.nist.gov/vuln/detail/CVE-2026-116439) | Critical | 9.8 | Dell PowerStore SDNAS contains a path traversal vulnerability that could allow an unauthenticated attacker to read, mod… |
| 2026-11-19 13:17:27 | [CVE-2026-116440](https://nvd.nist.gov/vuln/detail/CVE-2026-116440) | Critical | 9.8 | Dell PowerStore SDNAS contains a buffer overflow vulnerability that could allow an unauthenticated remote attacker to c… |
| 2026-11-19 13:17:28 | [CVE-2026-129034](https://nvd.nist.gov/vuln/detail/CVE-2026-129034) | High | 7.1 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in WP Chill Strong T… |
| 2026-11-19 13:17:28 | [CVE-2026-133076](https://nvd.nist.gov/vuln/detail/CVE-2026-133076) | High | 7.5 | In JetBrains TeamCity before 2026.2.2, 2026.1.6 remote code execution was possible via local repository URLs in Subvers… |
| 2026-11-19 13:17:28 | [CVE-2026-133077](https://nvd.nist.gov/vuln/detail/CVE-2026-133077) | High | 7.2 | In JetBrains TeamCity before 2026.2.2, 2026.1.6 privilege escalation to system administrator was possible via Project I… |
| 2026-11-19 13:17:28 | [CVE-2026-133078](https://nvd.nist.gov/vuln/detail/CVE-2026-133078) | High | 7.2 | In JetBrains TeamCity before 2026.2.2, 2026.1.6 remote code execution was possible via security context spoofing in the… |
| 2026-11-19 13:17:28 | [CVE-2026-133079](https://nvd.nist.gov/vuln/detail/CVE-2026-133079) | High | 7.2 | In JetBrains TeamCity before 2026.2.2, 2026.1.6 remote code execution was possible via Maven dependencies of Kotlin DSL… |
| 2026-11-19 13:17:28 | [CVE-2026-133080](https://nvd.nist.gov/vuln/detail/CVE-2026-133080) | High | 8.8 | In JetBrains TeamCity before 2026.2.2, 2026.1.6 remote code execution was possible via Maven repository settings |
| 2026-11-19 13:17:29 | [CVE-2026-133081](https://nvd.nist.gov/vuln/detail/CVE-2026-133081) | High | 7.5 | In JetBrains TeamCity before 2026.2.2, 2026.1.6 remote code execution was possible via Git VCS root URLs |
| 2026-11-19 13:17:29 | [CVE-2026-133082](https://nvd.nist.gov/vuln/detail/CVE-2026-133082) | High | 7.5 | In JetBrains TeamCity before 2026.2.2, 2026.1.6 a DoS attack was possible via unauthenticated multipart requests |
| 2026-11-19 13:17:29 | [CVE-2026-133083](https://nvd.nist.gov/vuln/detail/CVE-2026-133083) | High | 8.0 | In JetBrains TeamCity before 2026.2.2, 2026.1.6 stored XSS in Server Health reports was possible |
| 2026-11-19 13:17:29 | [CVE-2026-133084](https://nvd.nist.gov/vuln/detail/CVE-2026-133084) | High | 7.7 | In JetBrains TeamCity before 2026.2.2, 2026.1.6 vCS root credentials could be exposed via change viewer links |
| 2026-11-19 13:17:29 | [CVE-2026-133085](https://nvd.nist.gov/vuln/detail/CVE-2026-133085) | High | 7.6 | In JetBrains TeamCity before 2026.2.2, 2026.1.6 an XXE was possible in the TFS helper process |
| 2026-11-19 13:17:29 | [CVE-2026-133086](https://nvd.nist.gov/vuln/detail/CVE-2026-133086) | High | 8.8 | In JetBrains TeamCity before 2026.2.2, 2026.1.6 remote code execution was possible via a URL stream handler in the Kotl… |
| 2026-11-19 13:17:29 | [CVE-2026-133087](https://nvd.nist.gov/vuln/detail/CVE-2026-133087) | High | 8.8 | In JetBrains TeamCity before 2026.2.2, 2026.1.6 remote code execution was possible via a time zone callback in the Kotl… |
| 2026-11-19 13:17:29 | [CVE-2026-133088](https://nvd.nist.gov/vuln/detail/CVE-2026-133088) | High | 7.2 | In JetBrains TeamCity before 2026.2.2, 2026.1.6 remote code execution was possible via FreeMarker notification templates |
| 2026-11-19 13:17:30 | [CVE-2026-133089](https://nvd.nist.gov/vuln/detail/CVE-2026-133089) | High | 8.1 | In JetBrains TeamCity before 2026.2.2, 2026.1.6 the TFS helper process exposed an unauthenticated command server |
| 2026-11-19 13:17:30 | [CVE-2026-133090](https://nvd.nist.gov/vuln/detail/CVE-2026-133090) | High | 7.2 | In JetBrains TeamCity before 2026.2.2, 2026.1.6 improper authorization allowed overwriting versioned settings of other… |
| 2026-11-19 13:17:30 | [CVE-2026-133091](https://nvd.nist.gov/vuln/detail/CVE-2026-133091) | High | 8.0 | In JetBrains TeamCity before 2026.2.2, 2026.1.6 stored XSS on the Users page was possible |
| 2026-11-19 13:17:30 | [CVE-2026-133092](https://nvd.nist.gov/vuln/detail/CVE-2026-133092) | High | 8.8 | In JetBrains TeamCity before 2026.2.2, 2026.1.6 remote code execution was possible via Git submodule URLs |
| 2026-11-19 13:17:30 | [CVE-2026-133093](https://nvd.nist.gov/vuln/detail/CVE-2026-133093) | High | 7.2 | In JetBrains TeamCity before 2026.2.2, 2026.1.6 code injection in parent project Kotlin DSL was possible via subproject… |
| 2026-11-19 13:17:30 | [CVE-2026-133094](https://nvd.nist.gov/vuln/detail/CVE-2026-133094) | High | 7.7 | In JetBrains TeamCity before 2026.2.2 missing authorization allowed project developers to read arbitrary HashiCorp Vaul… |
| 2026-11-19 13:17:30 | [CVE-2026-133095](https://nvd.nist.gov/vuln/detail/CVE-2026-133095) | High | 8.1 | In JetBrains TeamCity before 2026.2.2, 2026.1.6 a CSRF attack was possible on the Hub integration settings |
| 2026-11-19 13:17:30 | [CVE-2026-133096](https://nvd.nist.gov/vuln/detail/CVE-2026-133096) | High | 7.1 | In JetBrains TeamCity before 2026.2.2, 2026.1.6 improper authorization allowed queuing builds with personal changes of… |
| 2026-11-19 13:17:31 | [CVE-2026-133097](https://nvd.nist.gov/vuln/detail/CVE-2026-133097) | High | 7.4 | In JetBrains TeamCity before 2026.2.2, 2026.1.6 agent Push authorization keys were predictable |
| 2026-11-19 13:17:31 | [CVE-2026-133098](https://nvd.nist.gov/vuln/detail/CVE-2026-133098) | Medium | 6.8 | In JetBrains TeamCity before 2026.2.2 stored XSS in GitHub issue tracker suggestions was possible |
| 2026-11-19 13:17:31 | [CVE-2026-133099](https://nvd.nist.gov/vuln/detail/CVE-2026-133099) | Medium | 6.5 | In JetBrains TeamCity before 2026.2.2 vCS root passwords could be extracted via the REST API property locator |
| 2026-11-19 13:17:31 | [CVE-2026-133100](https://nvd.nist.gov/vuln/detail/CVE-2026-133100) | Medium | 6.8 | In JetBrains TeamCity before 2026.2.2, 2026.1.6 command injection in Project Import artifact copy scripts was possible |
| 2026-11-19 13:17:31 | [CVE-2026-133101](https://nvd.nist.gov/vuln/detail/CVE-2026-133101) | Medium | 6.5 | In JetBrains TeamCity before 2026.2.2 a CSRF attack was possible on the diagnostic page |
| 2026-11-19 13:17:31 | [CVE-2026-133102](https://nvd.nist.gov/vuln/detail/CVE-2026-133102) | Medium | 4.9 | In JetBrains TeamCity before 2026.2.2, 2026.1.6 out-of-band data exfiltration via DNS resolution was possible in the Ko… |
| 2026-11-19 13:17:31 | [CVE-2026-133103](https://nvd.nist.gov/vuln/detail/CVE-2026-133103) | Medium | 6.8 | In JetBrains TeamCity before 2026.2.2, 2026.1.6 stored XSS in the enforced settings restriction tooltip was possible |
| 2026-11-19 13:17:32 | [CVE-2026-133104](https://nvd.nist.gov/vuln/detail/CVE-2026-133104) | Medium | 6.4 | In JetBrains TeamCity before 2026.2.2 stored XSS in external change viewer links was possible |
| 2026-11-19 13:17:32 | [CVE-2026-133105](https://nvd.nist.gov/vuln/detail/CVE-2026-133105) | Medium | 6.1 | In JetBrains TeamCity before 2026.2.2, 2026.1.6 reflected XSS on the Edit VCS Root page was possible |
| 2026-11-19 13:17:32 | [CVE-2026-133106](https://nvd.nist.gov/vuln/detail/CVE-2026-133106) | Medium | 6.8 | In JetBrains TeamCity before 2026.2.2, 2026.1.6 stored XSS on the Projects Import page was possible |
| 2026-11-19 13:17:32 | [CVE-2026-133107](https://nvd.nist.gov/vuln/detail/CVE-2026-133107) | Low | 2.4 | In JetBrains TeamCity before 2026.2.2, 2026.1.6 hTML injection in pipeline notification emails was possible via commit… |
| 2026-11-19 13:17:32 | [CVE-2026-133108](https://nvd.nist.gov/vuln/detail/CVE-2026-133108) | Low | 2.7 | In JetBrains TeamCity before 2026.2.2 the current request details debug endpoint exposed authentication headers and ses… |
| 2026-11-19 13:17:32 | [CVE-2026-133109](https://nvd.nist.gov/vuln/detail/CVE-2026-133109) | Low | 2.4 | In JetBrains TeamCity before 2026.2.2, 2026.1.6 hTML injection in pipeline notification emails was possible via user an… |
| 2026-11-19 13:17:32 | [CVE-2026-133117](https://nvd.nist.gov/vuln/detail/CVE-2026-133117) | High | 8.8 | WebToffee Product Feed before 2.4.4 for WordPress contains a use of hard-coded cryptographic key vulnerability that all… |
| 2026-11-19 13:17:33 | [CVE-2026-87956](https://nvd.nist.gov/vuln/detail/CVE-2026-87956) | Medium | 6.1 | When Private data source connect (PDC) or a secure SOCKS proxy is used, the MQTT data source plugin does not apply TLS… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
