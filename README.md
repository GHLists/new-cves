# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-22 22:18 UTC

New CVEs published between 2026-10-22 21:19 UTC and 2026-10-22 22:18 UTC.

[Full CSV](data/new-cves-2026-10-22T22-18-46-682948Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-10-22 22:17:52 | [CVE-2026-105014](https://nvd.nist.gov/vuln/detail/CVE-2026-105014) | Critical | 9.1 | Improper neutralization of special elements used in a command ('command injection') in Azure Pipelines allows an unauth… |
| 2026-10-22 22:17:52 | [CVE-2026-105265](https://nvd.nist.gov/vuln/detail/CVE-2026-105265) | Medium | 6.0 | A vulnerability exists in the the time zone parameter and does not properly validate user input, which may allow an aut… |
| 2026-10-22 22:17:58 | [CVE-2026-108456](https://nvd.nist.gov/vuln/detail/CVE-2026-108456) | High | 7.7 | Server-side request forgery (ssrf) in Azure AI Foundry allows an authorized attacker to elevate privileges over a netwo… |
| 2026-10-22 22:17:59 | [CVE-2026-109122](https://nvd.nist.gov/vuln/detail/CVE-2026-109122) | Critical | 9.4 | The network management service on affected Kiloview E3 NDI encoder firmware fails to sanitize one field used when confi… |
| 2026-10-22 22:18:00 | [CVE-2026-110063](https://nvd.nist.gov/vuln/detail/CVE-2026-110063) | Critical | 10.0 | Improper link resolution before file access ('link following') in VM Inspector for Azure Virtual Machines allows an una… |
| 2026-10-22 22:18:00 | [CVE-2026-111100](https://nvd.nist.gov/vuln/detail/CVE-2026-111100) | Medium | 6.9 | The ONVIF device service on the E3 responds to certain informational requests without requiring authentication. A remot… |
| 2026-10-22 22:18:01 | [CVE-2026-111594](https://nvd.nist.gov/vuln/detail/CVE-2026-111594) | Critical | 9.2 | InterSystems IRIS for Health has TLS/SSL encryption turned off by default, which may enable an attacker to view transmi… |
| 2026-10-22 22:18:04 | [CVE-2026-114615](https://nvd.nist.gov/vuln/detail/CVE-2026-114615) | High | 7.4 | Authlib is a Python library which builds OAuth and OpenID Connect servers. From 1.3.1 until 1.9.0, OctKey.import_key()… |
| 2026-10-22 22:18:04 | [CVE-2026-114616](https://nvd.nist.gov/vuln/detail/CVE-2026-114616) | High | 7.4 | Authlib is a Python library which builds OAuth and OpenID Connect servers. Prior to 1.9.1, Authlib's OctKey.import_key(… |
| 2026-10-22 22:18:04 | [CVE-2026-114617](https://nvd.nist.gov/vuln/detail/CVE-2026-114617) | Medium | 4.2 | Authlib is a Python library which builds OAuth and OpenID Connect servers. Prior to 1.9.0, OpenIDMixin.parse_id_token()… |
| 2026-10-22 22:18:04 | [CVE-2026-114618](https://nvd.nist.gov/vuln/detail/CVE-2026-114618) | Medium | 6.8 | Authlib is a Python library which builds OAuth and OpenID Connect servers. Prior to 1.9.0, the default RFC 7523 JWTBear… |
| 2026-10-22 22:18:04 | [CVE-2026-114619](https://nvd.nist.gov/vuln/detail/CVE-2026-114619) | Medium | 4.6 | Authlib is a Python library which builds OAuth and OpenID Connect servers. Prior to 1.9.0, OpenIDImplicitGrant.validate… |
| 2026-10-22 22:18:05 | [CVE-2026-114620](https://nvd.nist.gov/vuln/detail/CVE-2026-114620) | Medium | 5.4 | Authlib is a Python library which builds OAuth and OpenID Connect servers. Prior to 1.9.0, Authlib's RFC 9101 JWTAuthen… |
| 2026-10-22 22:18:06 | [CVE-2026-115221](https://nvd.nist.gov/vuln/detail/CVE-2026-115221) | Medium | 5.4 | A flaw was found in FreeIPA. An improper authorization check allows an authenticated host to retrieve and revoke digita… |
| 2026-10-22 22:18:06 | [CVE-2026-115424](https://nvd.nist.gov/vuln/detail/CVE-2026-115424) | Medium | 5.5 | A flaw was found in the OpenShift client oc. When extracting container image layers with oc image extract, the applicat… |
| 2026-10-22 22:18:06 | [CVE-2026-115449](https://nvd.nist.gov/vuln/detail/CVE-2026-115449) | Low | 3.5 | A flaw was found in libslirp. When handling ICMP echo requests, the reply length is not updated to match the actual dat… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
