# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-09-29 23:18 UTC

New CVEs published between 2026-09-29 22:22 UTC and 2026-09-29 23:18 UTC.

[Full CSV](data/new-cves-2026-09-29T23-18-35-837609Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-09-29 23:17:21 | [CVE-2026-102792](https://nvd.nist.gov/vuln/detail/CVE-2026-102792) | High | 8.5 | A vulnerability was detected in Ziroom ZHOME A0101 1.0.1.0. This affects the function set_syslog of the file /api/ZRnet… |
| 2026-09-29 23:17:21 | [CVE-2026-103040](https://nvd.nist.gov/vuln/detail/CVE-2026-103040) | Critical | 9.3 | LightLLM through 1.2.0 contains a remote code execution vulnerability in the router profiler service when started with… |
| 2026-09-29 23:17:21 | [CVE-2026-103041](https://nvd.nist.gov/vuln/detail/CVE-2026-103041) | Critical | 9.3 | LightLLM through 1.2.0 multimodal deployments expose an unauthenticated RPyC cache service with pickle deserialization… |
| 2026-09-29 23:17:21 | [CVE-2026-103042](https://nvd.nist.gov/vuln/detail/CVE-2026-103042) | High | 8.7 | LightLLM through 1.2.0 contains a memory exhaustion vulnerability in the NCCL control channel when started with --pd_tr… |
| 2026-09-29 23:17:22 | [CVE-2026-103043](https://nvd.nist.gov/vuln/detail/CVE-2026-103043) | High | 8.7 | anchorme through 3.0.8 contains a regular expression denial of service vulnerability in the IPv6 host extraction regex… |
| 2026-09-29 23:17:22 | [CVE-2026-103044](https://nvd.nist.gov/vuln/detail/CVE-2026-103044) |  |  | XML injection (aka blind XPath injection) vulnerability in The Wikimedia Foundation Mediawiki - EasyTimeline extension… |
| 2026-09-29 23:17:22 | [CVE-2026-103045](https://nvd.nist.gov/vuln/detail/CVE-2026-103045) |  |  | Improper neutralization of input during web page generation ('cross-site scripting') vulnerability in The Wikimedia Fou… |
| 2026-09-29 23:17:22 | [CVE-2026-103046](https://nvd.nist.gov/vuln/detail/CVE-2026-103046) |  |  | Improper neutralization of input during web page generation ('cross-site scripting') vulnerability in Wikimedia Foundat… |
| 2026-09-29 23:17:22 | [CVE-2026-103047](https://nvd.nist.gov/vuln/detail/CVE-2026-103047) |  |  | Improper neutralization of input during web page generation ('cross-site scripting') vulnerability in The Wikimedia Fou… |
| 2026-09-29 23:17:22 | [CVE-2026-15278](https://nvd.nist.gov/vuln/detail/CVE-2026-15278) |  |  | Rejected reason: This CVE ID has been rejected or withdrawn by its CVE Numbering Authority. |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
