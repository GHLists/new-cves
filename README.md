# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-27 19:18 UTC

New CVEs published between 2026-10-27 18:18 UTC and 2026-10-27 19:18 UTC.

[Full CSV](data/new-cves-2026-10-27T19-18-37-289021Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-10-27 19:17:10 | [CVE-2026-115413](https://nvd.nist.gov/vuln/detail/CVE-2026-115413) | High | 7.3 | Missing token audience validation in the OAuth authentication mode of AWS API MCP Server before version 1.6.0 might all… |
| 2026-10-27 19:17:11 | [CVE-2026-116683](https://nvd.nist.gov/vuln/detail/CVE-2026-116683) | High | 7.1 | CTFer.io's CTFd Terraform Provider manages CTFd resources as code. From 0.1.5 until 2.8.2, ctfd_team.password is stored… |
| 2026-10-27 19:17:28 | [CVE-2026-118170](https://nvd.nist.gov/vuln/detail/CVE-2026-118170) |  |  | The strapi/review-workflows package is vulnerable to a broken access control vulnerability allowing updates to be made… |
| 2026-10-27 19:17:28 | [CVE-2026-118171](https://nvd.nist.gov/vuln/detail/CVE-2026-118171) |  |  | The strapi/content-manager package is missing content-scope authorization in the content manager preview URL endpoint.… |
| 2026-10-27 19:17:28 | [CVE-2026-118172](https://nvd.nist.gov/vuln/detail/CVE-2026-118172) |  |  | The strapi/strapi (Core Admin / Webhook Runner) package is vulnerable to a semi-blind SSRF via a webhook follow-redirec… |
| 2026-10-27 19:17:28 | [CVE-2026-118173](https://nvd.nist.gov/vuln/detail/CVE-2026-118173) | Medium | 6.1 | MISP Guard, a proxy that enforces security policies on MISP feed data, contained an incomplete validation check for req… |
| 2026-10-27 19:17:29 | [CVE-2026-118174](https://nvd.nist.gov/vuln/detail/CVE-2026-118174) |  |  | When a message containing an OpenPGP key attachment was displayed, Thunderbird automatically loaded the attachment's co… |
| 2026-10-27 19:17:29 | [CVE-2026-118175](https://nvd.nist.gov/vuln/detail/CVE-2026-118175) |  |  | When replying to, forwarding, or editing a crafted email message as new, Thunderbird could embed parts of a different m… |
| 2026-10-27 19:17:29 | [CVE-2026-118176](https://nvd.nist.gov/vuln/detail/CVE-2026-118176) |  |  | Thunderbird's check that prevents mailbox: URLs from accessing files on remote Windows network shares could be bypassed… |
| 2026-10-27 19:17:29 | [CVE-2026-118177](https://nvd.nist.gov/vuln/detail/CVE-2026-118177) |  |  | When looking for calendars in a directory on a server, during account setup or when adding a new network calendar, Thun… |
| 2026-10-27 19:17:29 | [CVE-2026-118178](https://nvd.nist.gov/vuln/detail/CVE-2026-118178) |  |  | A remote RSS feed could use the itunes:new-feed-url or newLocation element to permanently change its stored subscriptio… |
| 2026-10-27 19:17:29 | [CVE-2026-118179](https://nvd.nist.gov/vuln/detail/CVE-2026-118179) |  |  | Clicking a news: or snews: link that referenced a message-ID made Thunderbird connect, without asking, to the host and… |
| 2026-10-27 19:17:29 | [CVE-2026-118180](https://nvd.nist.gov/vuln/detail/CVE-2026-118180) |  |  | When logging in to a Matrix account, Thunderbird used the homeserver address provided in the server's login response wi… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
