# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-11-20 17:19 UTC

New CVEs published between 2026-11-20 16:19 UTC and 2026-11-20 17:19 UTC.

[Full CSV](data/new-cves-2026-11-20T17-19-56-690842Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-11-20 17:18:07 | [CVE-2026-115407](https://nvd.nist.gov/vuln/detail/CVE-2026-115407) | Critical | 9.1 | In `github.com/eclipse-keypont/crypto11/v2` versions `<= 2.0.0-rc8` (and the deprecated v1 module paths `github.com/ecl… |
| 2026-11-20 17:18:07 | [CVE-2026-122244](https://nvd.nist.gov/vuln/detail/CVE-2026-122244) | High | 7.7 | Budibase is an open-source low-code platform. Prior to 3.50.0, a BASIC application user, or an unauthenticated visitor… |
| 2026-11-20 17:18:08 | [CVE-2026-122247](https://nvd.nist.gov/vuln/detail/CVE-2026-122247) | High | 8.2 | Budibase is an open-source low-code platform. Prior to 3.50.0, the public POST /api/global/users/init endpoint on a sel… |
| 2026-11-20 17:18:12 | [CVE-2026-132275](https://nvd.nist.gov/vuln/detail/CVE-2026-132275) | High | 7.5 | svglib reads SVG files and converts them to other formats. Prior to 2.3.1, the svg2rlg() renderer recursively expands n… |
| 2026-11-20 17:18:12 | [CVE-2026-132276](https://nvd.nist.gov/vuln/detail/CVE-2026-132276) | Medium | 5.9 | wcmatch is a Python library for wildcard file-name matching. Prior to 11.2, under the default flags, matching a non-mat… |
| 2026-11-20 17:18:12 | [CVE-2026-132277](https://nvd.nist.gov/vuln/detail/CVE-2026-132277) | Medium | 5.3 | Inscriptis is a Python library for converting HTML to text. From 2.0.0 until 2.7.6, when the parent is block-level, tab… |
| 2026-11-20 17:18:17 | [CVE-2026-133199](https://nvd.nist.gov/vuln/detail/CVE-2026-133199) | Medium | 5.8 | Incorrect privilege assignment in the user and group reconciliation logic in AWS ssosync before 2.9.5 might allow an au… |
| 2026-11-20 17:18:24 | [CVE-2026-133871](https://nvd.nist.gov/vuln/detail/CVE-2026-133871) | Medium | 5.1 | Pydici through 2026.11.1 contains a stored cross-site scripting vulnerability that allows authenticated users to inject… |
| 2026-11-20 17:18:24 | [CVE-2026-133872](https://nvd.nist.gov/vuln/detail/CVE-2026-133872) | Critical | 9.1 | LessPass self-hosted sync server backend before commit 9469b0c lacks rate limiting on the JWT login endpoints /tokens/a… |
| 2026-11-20 17:18:24 | [CVE-2026-133873](https://nvd.nist.gov/vuln/detail/CVE-2026-133873) | Medium | 5.3 | Cloud Mail before 3.6.0 contains a stored cross-site scripting vulnerability in attService.addAtt that allows unauthent… |
| 2026-11-20 17:18:24 | [CVE-2026-133874](https://nvd.nist.gov/vuln/detail/CVE-2026-133874) | High | 8.6 | Iceburg CRM through 5.0.0 contains an incorrect authorization vulnerability in Module::saveRecord() that allows authent… |
| 2026-11-20 17:18:24 | [CVE-2026-133875](https://nvd.nist.gov/vuln/detail/CVE-2026-133875) | Medium | 5.3 | one-hub through 0.14.27 contains a server-side request forgery vulnerability in GetImageFromUrl in common/image/image.g… |
| 2026-11-20 17:18:24 | [CVE-2026-133876](https://nvd.nist.gov/vuln/detail/CVE-2026-133876) | Medium | 5.1 | Kartones flask-calendar before commit bfde72e contains a stored cross-site scripting vulnerability because task_details… |
| 2026-11-20 17:18:25 | [CVE-2026-133878](https://nvd.nist.gov/vuln/detail/CVE-2026-133878) | Medium | 4.3 | Mattermost versions 11.11.x <= 11.11.1, 11.7.x <= 11.7.14, 11.10.x <= 11.10.4 fail to restrict the broadcast scope of g… |
| 2026-11-20 17:18:25 | [CVE-2026-133879](https://nvd.nist.gov/vuln/detail/CVE-2026-133879) | High | 7.7 | A flaw was found in KubeVirt/containerized-data-importer. When a VirtualMachine with an embedded DataVolumeTemplate car… |
| 2026-11-20 17:18:25 | [CVE-2026-23871](https://nvd.nist.gov/vuln/detail/CVE-2026-23871) | Low | 3.5 | Incomplete validation of external ad-reply URLs in WhatsApp for Android and WhatsApp Business for Android before 2.26.1… |
| 2026-11-20 17:18:26 | [CVE-2026-77329](https://nvd.nist.gov/vuln/detail/CVE-2026-77329) | High | 8.8 | Tapo provides Rust and Python APIs and an MCP server for TP-Link Tapo smart devices. From 0.3.1 until 0.5.0, the Stream… |
| 2026-11-20 17:18:27 | [CVE-2026-77331](https://nvd.nist.gov/vuln/detail/CVE-2026-77331) | Low | 2.0 | memtomem-stm is a short-term memory proxy gateway with proactive memory surfacing for AI agents. From 0.1.2 until 0.1.3… |
| 2026-11-20 17:18:27 | [CVE-2026-77332](https://nvd.nist.gov/vuln/detail/CVE-2026-77332) | Low | 2.3 | memtomem-stm is a short-term memory proxy gateway with proactive memory surfacing for AI agents. From 0.1.0 until 0.1.3… |
| 2026-11-20 17:18:27 | [CVE-2026-79751](https://nvd.nist.gov/vuln/detail/CVE-2026-79751) | High | 7.6 | SportEase is a web application for managing school sports events, class rosters, and competition teams. Prior to 1.3, a… |
| 2026-11-20 17:18:27 | [CVE-2026-82675](https://nvd.nist.gov/vuln/detail/CVE-2026-82675) | High | 8.1 | The GiveWP – Donation Plugin and Fundraising Platform plugin for WordPress is vulnerable to donor account account takeo… |
| 2026-11-20 17:18:27 | [CVE-2026-82676](https://nvd.nist.gov/vuln/detail/CVE-2026-82676) | Medium | 4.3 | The GiveWP – Donation Plugin and Fundraising Platform plugin for WordPress is vulnerable to Cross-Site Request Forgery… |
| 2026-11-20 17:18:28 | [CVE-2026-95824](https://nvd.nist.gov/vuln/detail/CVE-2026-95824) | Medium | 6.5 | The IPv6 Neighbor Discovery code in subsys/net/ip/ipv6_nbr.c flushes a neighbour's queued packets at the end of handle_… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
