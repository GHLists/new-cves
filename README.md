# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-09-27 21:18 UTC

New CVEs published between 2026-09-27 20:20 UTC and 2026-09-27 21:18 UTC.

[Full CSV](data/new-cves-2026-09-27T21-18-55-296502Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-09-27 21:17:00 | [CVE-2026-100877](https://nvd.nist.gov/vuln/detail/CVE-2026-100877) | Low | 2.1 | A vulnerability was determined in mathurvishal CloudClassroom-PHP-Project up to 5dadec098bfbbf3300d60c3494db3fb95b66e7b… |
| 2026-09-27 21:17:01 | [CVE-2026-100878](https://nvd.nist.gov/vuln/detail/CVE-2026-100878) | Low | 2.1 | A vulnerability was identified in zhistaredu StarTraining up to 3.8.1. Affected by this issue is the function SysUser.i… |
| 2026-09-27 21:17:01 | [CVE-2026-100879](https://nvd.nist.gov/vuln/detail/CVE-2026-100879) | Low | 2.1 | A security flaw has been discovered in zhistaredu StarTraining up to 3.8.1. This affects the function checkRoleAllowed… |
| 2026-09-27 21:17:01 | [CVE-2026-100880](https://nvd.nist.gov/vuln/detail/CVE-2026-100880) | Low | 2.0 | A weakness has been identified in zhistaredu StarTraining up to 3.8.1. This vulnerability affects unknown code of the f… |
| 2026-09-27 21:17:01 | [CVE-2026-101062](https://nvd.nist.gov/vuln/detail/CVE-2026-101062) | High | 8.7 | Obot before v0.23.0 (affected versions <= v0.22.1) running with OBOT_SERVER_ENABLE_AUTHENTICATION=true exposes OAuth dy… |
| 2026-09-27 21:17:01 | [CVE-2026-101063](https://nvd.nist.gov/vuln/detail/CVE-2026-101063) | Medium | 6.9 | Obot versions before v0.23.0 fail to enforce authentication on MCP Registry endpoints under /v0.1/* when registry authe… |
| 2026-09-27 21:17:01 | [CVE-2026-101064](https://nvd.nist.gov/vuln/detail/CVE-2026-101064) | High | 8.3 | Obot before v0.23.0 contains a server-side request forgery vulnerability in remote MCP server registration that allows… |
| 2026-09-27 21:17:02 | [CVE-2026-101065](https://nvd.nist.gov/vuln/detail/CVE-2026-101065) | Critical | 9.3 | Obot is an open-source AI agent/MCP platform. In all versions up to and including commit d7e6970, the Docker quickstart… |
| 2026-09-27 21:17:02 | [CVE-2026-101084](https://nvd.nist.gov/vuln/detail/CVE-2026-101084) | Critical | 9.3 | obot versions before v0.21.1 fail to enforce Access Control Rules on the /mcp-connect endpoint, allowing any authentica… |
| 2026-09-27 21:17:02 | [CVE-2026-101085](https://nvd.nist.gov/vuln/detail/CVE-2026-101085) | High | 7.1 | Nezha before 2.3.8 fails to validate alert rule type and duration bounds, allowing authenticated non-administrator user… |
| 2026-09-27 21:17:02 | [CVE-2026-101086](https://nvd.nist.gov/vuln/detail/CVE-2026-101086) | High | 7.1 | Nezha Dashboard versions before 2.3.5 fail to restrict service monitor task types to supported probe types, allowing au… |
| 2026-09-27 21:17:02 | [CVE-2026-101087](https://nvd.nist.gov/vuln/detail/CVE-2026-101087) | Medium | 5.3 | Nezha versions 2.0.10 through 2.3.2 use a restricted HTTP client to validate user-configurable notification and DDNS we… |
| 2026-09-27 21:17:02 | [CVE-2026-101088](https://nvd.nist.gov/vuln/detail/CVE-2026-101088) | Medium | 6.0 | Nezha is a server and website monitoring tool. In versions >= 2.2.11 and < 2.3.1, the service sentinel worker (service/… |
| 2026-09-27 21:17:02 | [CVE-2026-101089](https://nvd.nist.gov/vuln/detail/CVE-2026-101089) | Low | 2.3 | Nezha before 2.2.7 contains an information disclosure vulnerability in the GET /api/v1/profile endpoint that returns th… |
| 2026-09-27 21:17:03 | [CVE-2026-101090](https://nvd.nist.gov/vuln/detail/CVE-2026-101090) | Critical | 9.3 | Nezha 2.2.3 contains a Host header injection regression in the OAuth2 redirect endpoint. When the new optional dashboar… |
| 2026-09-27 21:17:04 | [CVE-2026-96280](https://nvd.nist.gov/vuln/detail/CVE-2026-96280) | High | 7.5 | The OCI delta stream parser read sizes as guint64 but passed them to GLib I/O and allocation functions expecting gsize… |
| 2026-09-27 21:17:04 | [CVE-2026-96281](https://nvd.nist.gov/vuln/detail/CVE-2026-96281) |  |  | On a multi-user system, a user with an active local login session could downgrade a system-wide Flatpak app to an older… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
