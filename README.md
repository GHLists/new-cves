# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-09-30 20:18 UTC

New CVEs published between 2026-09-30 19:20 UTC and 2026-09-30 20:18 UTC.

[Full CSV](data/new-cves-2026-09-30T20-18-38-178641Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-09-30 20:17:18 | [CVE-2026-101879](https://nvd.nist.gov/vuln/detail/CVE-2026-101879) | High | 7.1 | OpenClaw Windows Node before 2026.7.1-3 contains a missing authorization vulnerability in NodeService capture handlers… |
| 2026-09-30 20:17:18 | [CVE-2026-101880](https://nvd.nist.gov/vuln/detail/CVE-2026-101880) | High | 8.7 | OpenClaw Windows Node before 2026.7.1 contains an incorrect authorization vulnerability in the system.run exec-approval… |
| 2026-09-30 20:17:19 | [CVE-2026-101881](https://nvd.nist.gov/vuln/detail/CVE-2026-101881) | High | 7.1 | OpenClaw Windows Node before 2026.7.1 contains an allocation of resources without limits vulnerability in the gateway W… |
| 2026-09-30 20:17:19 | [CVE-2026-101882](https://nvd.nist.gov/vuln/detail/CVE-2026-101882) | High | 8.7 | OpenClaw Windows Node before 2026.7.1 contains an incomplete validation vulnerability in system.execApprovals.set that… |
| 2026-09-30 20:17:20 | [CVE-2026-101883](https://nvd.nist.gov/vuln/detail/CVE-2026-101883) | Medium | 5.3 | OpenClaw Windows Node through 2026.9.4 contains a server-side request forgery vulnerability in the canvas.present capab… |
| 2026-09-30 20:17:20 | [CVE-2026-101884](https://nvd.nist.gov/vuln/detail/CVE-2026-101884) | High | 7.7 | OpenClaw Windows Node before 2026.7.1 contains an incomplete environment-variable sanitizer in system.run that fails to… |
| 2026-09-30 20:17:21 | [CVE-2026-101885](https://nvd.nist.gov/vuln/detail/CVE-2026-101885) | High | 8.5 | ZeroClaw versions before 0.8.5 built with plugins-wasm feature contain a path traversal vulnerability in plugin install… |
| 2026-09-30 20:17:26 | [CVE-2026-102990](https://nvd.nist.gov/vuln/detail/CVE-2026-102990) | High | 8.2 | basic-ftp is an FTP client for Node.js. Prior to 6.2.1, Client.list() can be forced by a malicious or compromised FTP s… |
| 2026-09-30 20:17:26 | [CVE-2026-102991](https://nvd.nist.gov/vuln/detail/CVE-2026-102991) | Medium | 6.5 | Mako is a template library written in Python. Prior to 1.4.2, on Windows, TemplateLookup.get_template() in mako/lookup.… |
| 2026-09-30 20:17:27 | [CVE-2026-102992](https://nvd.nist.gov/vuln/detail/CVE-2026-102992) | Critical | 9.2 | piscina is a node.js worker pool implementation. Prior to 4.9.4, 5.3.2, and 6.0.0-rc.5, Piscina stores ThreadPool.optio… |
| 2026-09-30 20:17:27 | [CVE-2026-102993](https://nvd.nist.gov/vuln/detail/CVE-2026-102993) | High | 8.7 | pypdf is a free and open-source pure-python PDF library. Prior to 6.17.0, a crafted PDF can provide unusually large Rom… |
| 2026-09-30 20:17:28 | [CVE-2026-102994](https://nvd.nist.gov/vuln/detail/CVE-2026-102994) | High | 8.7 | pypdf is a free and open-source pure-python PDF library. Prior to 6.18.0, a crafted PDF containing indirect-object iden… |
| 2026-09-30 20:17:30 | [CVE-2026-103387](https://nvd.nist.gov/vuln/detail/CVE-2026-103387) | Low | 2.1 | A weakness has been identified in garycourt uri-js up to 4.4.1. This affects the function URI.parse of the file src/sch… |
| 2026-09-30 20:17:31 | [CVE-2026-103547](https://nvd.nist.gov/vuln/detail/CVE-2026-103547) | Critical | 9.2 | In ldapd in OpenBSD 7.8 before errata 057 and 7.9 before errata 021, delegated BSD authentication results are correlate… |
| 2026-09-30 20:17:31 | [CVE-2026-103548](https://nvd.nist.gov/vuln/detail/CVE-2026-103548) | Medium | 5.3 | Improperly stored passwords in the config file in Itron MV-90 xi 3.0 allows attackers to decode the passwords and passw… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
