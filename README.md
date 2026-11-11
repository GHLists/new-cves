# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-11-11 15:19 UTC

New CVEs published between 2026-11-11 14:18 UTC and 2026-11-11 15:19 UTC.

[Full CSV](data/new-cves-2026-11-11T15-19-18-774163Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-11-11 15:17:12 | [CVE-2026-102589](https://nvd.nist.gov/vuln/detail/CVE-2026-102589) | High | 7.1 | When independent Grafana instances share the same [rendering] renderer_token, an image renderer key issued by one insta… |
| 2026-11-11 15:17:13 | [CVE-2026-106023](https://nvd.nist.gov/vuln/detail/CVE-2026-106023) |  |  | NULL pointer dereference vulnerability in Apache HTTP Server's mod_md during HTTP request processing. This issue affect… |
| 2026-11-11 15:17:13 | [CVE-2026-107509](https://nvd.nist.gov/vuln/detail/CVE-2026-107509) | Medium | 6.5 | A user with the Viewer role can make Grafana allocate an unbounded amount of memory, and crash it, with a single SQL Ex… |
| 2026-11-11 15:17:14 | [CVE-2026-109163](https://nvd.nist.gov/vuln/detail/CVE-2026-109163) |  |  | Stack-based buffer overflow vulnerability in Apache HTTP Server's mod_vhost_alias (after CVE-2026-63292) This issue aff… |
| 2026-11-11 15:17:14 | [CVE-2026-110289](https://nvd.nist.gov/vuln/detail/CVE-2026-110289) | Medium | 5.5 | A user with the Organization Admin role could point the server or token URL of a Git Sync connection at a loopback or i… |
| 2026-11-11 15:17:14 | [CVE-2026-110992](https://nvd.nist.gov/vuln/detail/CVE-2026-110992) | Medium | 6.5 | A user who can create Git Sync provisioning jobs (the Editor role by default) could delete or move files outside the co… |
| 2026-11-11 15:17:14 | [CVE-2026-111000](https://nvd.nist.gov/vuln/detail/CVE-2026-111000) | High | 7.1 | A user with the Editor role who can edit a folder can move it, through the folders resource API, under a folder they ad… |
| 2026-11-11 15:17:14 | [CVE-2026-111024](https://nvd.nist.gov/vuln/detail/CVE-2026-111024) | High | 7.1 | A user with the Viewer or Editor role could bypass folder permissions on Git Sync managed resources through the reposit… |
| 2026-11-11 15:17:15 | [CVE-2026-119618](https://nvd.nist.gov/vuln/detail/CVE-2026-119618) |  |  | Concurrent Execution using Shared Resource with Improper Synchronization vulnerability in Apache HTTP Server's mod_http… |
| 2026-11-11 15:17:18 | [CVE-2026-123710](https://nvd.nist.gov/vuln/detail/CVE-2026-123710) | Critical | 9.8 | A flaw was found in Red Hat Quay. An unauthenticated client can obtain an anonymous registry token with an audience it… |
| 2026-11-11 15:17:19 | [CVE-2026-124746](https://nvd.nist.gov/vuln/detail/CVE-2026-124746) | Medium | 5.5 | A flaw was found in BusyBox. An integer overflow occurs in the volume_id component when calculating buffer boundaries w… |
| 2026-11-11 15:17:22 | [CVE-2026-126325](https://nvd.nist.gov/vuln/detail/CVE-2026-126325) | Critical | 9.2 | A critical remote code execution (RCE) vulnerability has been reported in PTC Windchill and PTC FlexPLM. The vulnerabil… |
| 2026-11-11 15:17:22 | [CVE-2026-13721](https://nvd.nist.gov/vuln/detail/CVE-2026-13721) | Medium | 6.5 | A user with edit access to one folder could modify, move or delete Git Sync provisioned resources in folders where they… |
| 2026-11-11 15:17:22 | [CVE-2026-14242](https://nvd.nist.gov/vuln/detail/CVE-2026-14242) | Medium | 6.5 | A user with the Editor role could delete, move, push or pull Git Sync managed resources in folders where they only had… |
| 2026-11-11 15:17:23 | [CVE-2026-44929](https://nvd.nist.gov/vuln/detail/CVE-2026-44929) |  |  | Server-Side Request Forgery (SSRF) vulnerability in Apache XML Graphics Batik. This issue affects Apache XML Graphics B… |
| 2026-11-11 15:17:24 | [CVE-2026-71395](https://nvd.nist.gov/vuln/detail/CVE-2026-71395) |  |  | unsafe deserialization in hyphenation loading vulnerability in Apache XML Graphics FOP. This issue affects Apache XML G… |
| 2026-11-11 15:17:25 | [CVE-2026-82014](https://nvd.nist.gov/vuln/detail/CVE-2026-82014) | Medium | 4.3 | Any authenticated user, including a Viewer, could change the preferences of any team, such as its home dashboard, theme… |
| 2026-11-11 15:17:25 | [CVE-2026-85632](https://nvd.nist.gov/vuln/detail/CVE-2026-85632) | Critical | 9.1 | Missing authentication for critical function and Improper validation of integrity check value vulnerability in Sipay El… |
| 2026-11-11 15:17:25 | [CVE-2026-89326](https://nvd.nist.gov/vuln/detail/CVE-2026-89326) |  |  | Origin Validation Error vulnerability in Apache XML Graphics Batik: the external resource same-origin check does not co… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
