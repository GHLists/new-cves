# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-20 19:20 UTC

New CVEs published between 2026-10-20 18:20 UTC and 2026-10-20 19:20 UTC.

[Full CSV](data/new-cves-2026-10-20T19-20-27-940935Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-10-20 19:17:11 | [CVE-2026-100132](https://nvd.nist.gov/vuln/detail/CVE-2026-100132) | Medium | 4.3 | Acrobat for Edge is affected by an out-of-bounds read vulnerability that could lead to disclosure of sensitive memory.… |
| 2026-10-20 19:17:11 | [CVE-2026-100134](https://nvd.nist.gov/vuln/detail/CVE-2026-100134) | High | 8.8 | Acrobat for Edge is affected by an out-of-bounds write vulnerability that could result in arbitrary code execution in t… |
| 2026-10-20 19:17:30 | [CVE-2026-111088](https://nvd.nist.gov/vuln/detail/CVE-2026-111088) | Medium | 6.5 | A Stored Cross-Site Scripting vulnerability exists in the SNS VPN log monitoring screen. |
| 2026-10-20 19:17:30 | [CVE-2026-111767](https://nvd.nist.gov/vuln/detail/CVE-2026-111767) | High | 8.6 | MCP TypeScript SDK is the official TypeScript SDK for Model Context Protocol servers and clients. From version 1.24.0 t… |
| 2026-10-20 19:17:32 | [CVE-2026-113643](https://nvd.nist.gov/vuln/detail/CVE-2026-113643) | Medium | 5.3 | A vulnerability was found in EspoCRM up to 9.3.10/10.0.10. This affects the function ImageSourceProvider::get of the fi… |
| 2026-10-20 19:17:33 | [CVE-2026-113708](https://nvd.nist.gov/vuln/detail/CVE-2026-113708) | Critical | 9.9 | Argo CD is a declarative, GitOps continuous delivery tool for Kubernetes. From 2.7.0 until 3.3.15, 3.4.10, 3.5.4, and 3… |
| 2026-10-20 19:17:33 | [CVE-2026-113709](https://nvd.nist.gov/vuln/detail/CVE-2026-113709) | Critical | 9.9 | Argo CD is a declarative, GitOps continuous delivery tool for Kubernetes. From 2.1.0 until 3.3.15, 3.4.10, 3.5.4, and 3… |
| 2026-10-20 19:17:33 | [CVE-2026-113712](https://nvd.nist.gov/vuln/detail/CVE-2026-113712) | Medium | 4.8 | Cachet is an open-source status page system. Versions 2.4.1 and earlier have a stored Cross-Site Scripting (XSS) vulner… |
| 2026-10-20 19:17:33 | [CVE-2026-113713](https://nvd.nist.gov/vuln/detail/CVE-2026-113713) | Medium | 4.4 | virtualenv is a tool for creating isolated virtual python environments. From 21.14.8 until 21.14.10, the app-data seede… |
| 2026-10-20 19:17:34 | [CVE-2026-113714](https://nvd.nist.gov/vuln/detail/CVE-2026-113714) | Low | 2.3 | virtualenv is a tool for creating isolated virtual python environments. From 21.14.8 until 21.14.9, download_wheel() wr… |
| 2026-10-20 19:17:34 | [CVE-2026-113808](https://nvd.nist.gov/vuln/detail/CVE-2026-113808) | High | 7.1 | A Stored Cross-Site Scripting vulnerability exists in the SNS enrollment Portal. Through the captive portal an attacker… |
| 2026-10-20 19:17:34 | [CVE-2026-113810](https://nvd.nist.gov/vuln/detail/CVE-2026-113810) | High | 7.0 | A Stored Cross-Site Scripting vulnerability exists in the SNS enrollment Portal. Through the captive portal an attacker… |
| 2026-10-20 19:17:35 | [CVE-2026-21266](https://nvd.nist.gov/vuln/detail/CVE-2026-21266) |  |  | Rejected reason: this CVE was issued in error. |
| 2026-10-20 19:17:35 | [CVE-2026-21356](https://nvd.nist.gov/vuln/detail/CVE-2026-21356) |  |  | Rejected reason: this CVE was issued in error. |
| 2026-10-20 19:17:35 | [CVE-2026-21270](https://nvd.nist.gov/vuln/detail/CVE-2026-21270) |  |  | Rejected reason: this CVE was issued in error. |
| 2026-10-20 19:17:38 | [CVE-2026-48279](https://nvd.nist.gov/vuln/detail/CVE-2026-48279) |  |  | Rejected reason: this CVE was issued in error. |
| 2026-10-20 19:18:15 | [CVE-2026-75747](https://nvd.nist.gov/vuln/detail/CVE-2026-75747) |  |  | Rejected reason: this CVE was issued in error. |
| 2026-10-20 19:18:15 | [CVE-2026-75751](https://nvd.nist.gov/vuln/detail/CVE-2026-75751) |  |  | Rejected reason: this CVE was issued in error. |
| 2026-10-20 19:18:15 | [CVE-2026-75997](https://nvd.nist.gov/vuln/detail/CVE-2026-75997) |  |  | Rejected reason: this CVE was issued in error. |
| 2026-10-20 19:19:38 | [CVE-2026-97406](https://nvd.nist.gov/vuln/detail/CVE-2026-97406) |  |  | XERJ Console API bearer tokens can bypass the passkey‑only authentication requirement and directly invoke the API‑token… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
