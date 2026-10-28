# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-28 20:18 UTC

New CVEs published between 2026-10-28 19:18 UTC and 2026-10-28 20:18 UTC.

[Full CSV](data/new-cves-2026-10-28T20-18-19-628129Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-10-28 20:17:14 | [CVE-2025-14260](https://nvd.nist.gov/vuln/detail/CVE-2025-14260) | High | 8.3 | Due to the improper implementation of access control rules, the WSO2 product accepts user-supplied input related to res… |
| 2026-10-28 20:17:17 | [CVE-2026-109411](https://nvd.nist.gov/vuln/detail/CVE-2026-109411) | High | 8.1 | An access control bypass flaw was found in Samba's vfs_ceph_rgw module in it's openat() function. An authenticated user… |
| 2026-10-28 20:17:20 | [CVE-2026-115415](https://nvd.nist.gov/vuln/detail/CVE-2026-115415) | Medium | 5.9 | Improper neutralization of input used for LLM prompting in the environment tool in Strands Agents Tools before 0.8.6 mi… |
| 2026-10-28 20:17:21 | [CVE-2026-117574](https://nvd.nist.gov/vuln/detail/CVE-2026-117574) | Critical | 9.1 | A flaw was found in ai-gateway-payload-processing. An authenticated remote attacker can exploit this vulnerability by s… |
| 2026-10-28 20:17:21 | [CVE-2026-118266](https://nvd.nist.gov/vuln/detail/CVE-2026-118266) | Medium | 5.3 | Echo is a Go web framework. Prior to 4.16.0 and 5.4.0, Echo's MethodOverride middleware accepts a safe HTTP method as t… |
| 2026-10-28 20:17:21 | [CVE-2026-118650](https://nvd.nist.gov/vuln/detail/CVE-2026-118650) | High | 7.5 | Echo is a Go web framework. Prior to 4.16.0 and 5.4.0, a globally mounted middleware.Static instance can interpret an e… |
| 2026-10-28 20:17:22 | [CVE-2026-118651](https://nvd.nist.gov/vuln/detail/CVE-2026-118651) | Medium | 5.3 | Echo is a Go web framework. From 4.0.0 until 5.4.0, the Proxy middleware can preserve an attacker-supplied X-Real-IP he… |
| 2026-10-28 20:17:22 | [CVE-2026-118652](https://nvd.nist.gov/vuln/detail/CVE-2026-118652) | Medium | 6.1 | Echo is a Go web framework. Prior to 4.16.0 and 5.4.0, Context.JSONP and Context.JSONPBlob concatenate an unvalidated c… |
| 2026-10-28 20:17:22 | [CVE-2026-118653](https://nvd.nist.gov/vuln/detail/CVE-2026-118653) | Medium | 5.3 | Echo is a Go web framework. From 4.0.0 until 5.1.0, Context.RealIP falls back to client-supplied X-Forwarded-For or X-R… |
| 2026-10-28 20:17:22 | [CVE-2026-118654](https://nvd.nist.gov/vuln/detail/CVE-2026-118654) | Medium | 5.9 | Echo is a Go web framework. Prior to 4.16.0 and 5.4.0, Echo's static file handlers can normalize dot segments after rou… |
| 2026-10-28 20:17:22 | [CVE-2026-118655](https://nvd.nist.gov/vuln/detail/CVE-2026-118655) | Medium | 5.9 | Echo is a Go web framework. Prior to 4.15.3 and 5.2.0, middleware.Static can decode an already decoded Request.URL.Path… |
| 2026-10-28 20:17:22 | [CVE-2026-11854](https://nvd.nist.gov/vuln/detail/CVE-2026-11854) | Medium | 6.1 | The authentication endpoint generates an error message that includes reflected data directly from the request without s… |
| 2026-10-28 20:17:23 | [CVE-2026-13451](https://nvd.nist.gov/vuln/detail/CVE-2026-13451) | High | 7.7 | A flaw was found in KServe. A namespace-scoped user with create/update permissions on InferenceService custom resources… |
| 2026-10-28 20:17:24 | [CVE-2026-3583](https://nvd.nist.gov/vuln/detail/CVE-2026-3583) | Low | 3.1 | When the `allowed_scopes` configuration is enabled, the OAuth2 token introspection mechanism does not immediately inval… |
| 2026-10-28 20:18:00 | [CVE-2026-54162](https://nvd.nist.gov/vuln/detail/CVE-2026-54162) | Medium | 4.7 | Ember is a real-time terminal dashboard for Caddy servers with FrankenPHP support. Prior to 1.4.2, interactive TUI row… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
