# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-19 03:21 UTC

New CVEs published between 2026-10-19 02:20 UTC and 2026-10-19 03:21 UTC.

[Full CSV](data/new-cves-2026-10-19T03-21-46-961203Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-10-19 03:16:58 | [CVE-2026-102503](https://nvd.nist.gov/vuln/detail/CVE-2026-102503) | Critical | 9.3 | Missing Authentication for Critical Function (CWE-306) and Missing Authorization (CWE-862) in the /libp2p-http ingress… |
| 2026-10-19 03:16:58 | [CVE-2026-103091](https://nvd.nist.gov/vuln/detail/CVE-2026-103091) | Critical | 9.3 | Missing Authorization (CWE-862) and Initialization of a Resource with an Insecure Default (CWE-1188) in the MCP proxy (… |
| 2026-10-19 03:16:58 | [CVE-2026-111441](https://nvd.nist.gov/vuln/detail/CVE-2026-111441) | High | 8.1 | 在 openGauss-server 的 src/gausskernel/cbb/utils/hll/hll.cpp 中，内置函数 HllObjectUnpack() 存在长度校验缺陷。该函数从用户提供的 packed HLL 解析 le… |
| 2026-10-19 03:16:58 | [CVE-2026-112042](https://nvd.nist.gov/vuln/detail/CVE-2026-112042) | Low | 2.0 | A security flaw has been discovered in diem-project diem up to 116974edfb9a5b8bd69cb13586dc62bcdbb485ad. This issue aff… |
| 2026-10-19 03:16:58 | [CVE-2026-112043](https://nvd.nist.gov/vuln/detail/CVE-2026-112043) | Medium | 5.3 | A weakness has been identified in calcom cal.com and cal.diy up to 6.2.0. Impacted is the function createWebhookProcedu… |
| 2026-10-19 03:16:59 | [CVE-2026-112044](https://nvd.nist.gov/vuln/detail/CVE-2026-112044) | Medium | 5.5 | A security vulnerability has been detected in dotnet eShop up to 913acea66708a59595351174cee9b29f37179d29. The affected… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
