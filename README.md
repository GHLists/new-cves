# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-27 20:18 UTC

New CVEs published between 2026-10-27 19:18 UTC and 2026-10-27 20:18 UTC.

[Full CSV](data/new-cves-2026-10-27T20-18-41-743035Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-10-27 20:17:11 | [CVE-2026-103995](https://nvd.nist.gov/vuln/detail/CVE-2026-103995) | Low | 2.0 | Response body and chunk parsing would handle non-hex or negative integers incorrectly which could result in misinterpre… |
| 2026-10-27 20:17:12 | [CVE-2026-112350](https://nvd.nist.gov/vuln/detail/CVE-2026-112350) | High | 8.7 | Sunhillo SureLine before 9.1.5 contains a path traversal vulnerability in the radarUpdater.cgi endpoint that allows una… |
| 2026-10-27 20:17:12 | [CVE-2026-112351](https://nvd.nist.gov/vuln/detail/CVE-2026-112351) | High | 8.7 | Sunhillo SureLine before 9.1.5 contains an OS command injection vulnerability in the networkDiag.cgi endpoint that allo… |
| 2026-10-27 20:17:12 | [CVE-2026-112352](https://nvd.nist.gov/vuln/detail/CVE-2026-112352) | Critical | 9.1 | Sunhillo SureLine before 9.1.5 contains an authentication bypass vulnerability that allows an unauthenticated remote at… |
| 2026-10-27 20:17:13 | [CVE-2026-112355](https://nvd.nist.gov/vuln/detail/CVE-2026-112355) | High | 8.7 | The MembershipWorks plugin for WordPress before 6.17 contains an information disclosure vulnerability that allows unaut… |
| 2026-10-27 20:17:13 | [CVE-2026-116684](https://nvd.nist.gov/vuln/detail/CVE-2026-116684) | Medium | 6.8 | The Model Context Protocol Python SDK is the official Python SDK for Model Context Protocol servers and clients. From 1… |
| 2026-10-27 20:17:13 | [CVE-2026-116685](https://nvd.nist.gov/vuln/detail/CVE-2026-116685) | Medium | 5.9 | The Model Context Protocol Python SDK is the official Python SDK for Model Context Protocol servers and clients. From 1… |
| 2026-10-27 20:17:13 | [CVE-2026-116686](https://nvd.nist.gov/vuln/detail/CVE-2026-116686) | Medium | 6.5 | The Model Context Protocol Python SDK is the official Python SDK for Model Context Protocol servers and clients. From 1… |
| 2026-10-27 20:17:13 | [CVE-2026-116687](https://nvd.nist.gov/vuln/detail/CVE-2026-116687) | Low | 3.1 | CKEditor 5 is a modern JavaScript rich-text editor with an MVC architecture. From 29.0.0 until 47.7.4 and 48.5.1, speci… |
| 2026-10-27 20:17:14 | [CVE-2026-116688](https://nvd.nist.gov/vuln/detail/CVE-2026-116688) | High | 8.1 | CKEditor 5 is a modern JavaScript rich-text editor with an MVC architecture. From 45.0.0 until 47.7.4 and 48.5.1, the e… |
| 2026-10-27 20:17:14 | [CVE-2026-116689](https://nvd.nist.gov/vuln/detail/CVE-2026-116689) | Medium | 5.9 | follow-redirects is a Node.js HTTP and HTTPS client wrapper that automatically follows redirects. From 1.16.0 until 1.1… |
| 2026-10-27 20:17:14 | [CVE-2026-116690](https://nvd.nist.gov/vuln/detail/CVE-2026-116690) | High | 7.5 | MLflow is an open source AI engineering platform for agents, large language models, and machine learning models. From 3… |
| 2026-10-27 20:17:14 | [CVE-2026-116691](https://nvd.nist.gov/vuln/detail/CVE-2026-116691) | Medium | 6.5 | MLflow is an open source AI engineering platform for agents, large language models, and machine learning models. From 2… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
