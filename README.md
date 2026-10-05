# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-05 21:19 UTC

New CVEs published between 2026-10-05 20:19 UTC and 2026-10-05 21:19 UTC.

[Full CSV](data/new-cves-2026-10-05T21-19-26-664857Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-10-05 21:16:32 | [CVE-2026-101893](https://nvd.nist.gov/vuln/detail/CVE-2026-101893) | Medium | 5.1 | Newell Brands DYMO ID 1.5.1.71 parses job files using XmlDocument.Load() without disabling DTD processing. The PC Job F… |
| 2026-10-05 21:16:32 | [CVE-2026-102262](https://nvd.nist.gov/vuln/detail/CVE-2026-102262) | High | 7.0 | Newell Brands DYMO ID 1.5.1.71 resolves its plugin Modules directory relative to the process working directory. An atta… |
| 2026-10-05 21:16:34 | [CVE-2026-105438](https://nvd.nist.gov/vuln/detail/CVE-2026-105438) | Low | 2.1 | A flaw has been found in O2OA up to 10.0.1-ce. This affects the function ActionUploadExcelWithUrl of the file /x_genera… |
| 2026-10-05 21:16:34 | [CVE-2026-105444](https://nvd.nist.gov/vuln/detail/CVE-2026-105444) | Low | 2.1 | A security flaw has been discovered in dotnet eShop .NET 8. The impacted element is the function GetOrderAsync of the f… |
| 2026-10-05 21:16:34 | [CVE-2026-105447](https://nvd.nist.gov/vuln/detail/CVE-2026-105447) | Medium | 5.5 | A flaw was found in Quay. When handling build trigger requests, the application incorrectly exposes trigger configurati… |
| 2026-10-05 21:16:35 | [CVE-2026-105697](https://nvd.nist.gov/vuln/detail/CVE-2026-105697) | Critical | 9.9 | Langflow is a tool for building and deploying AI-powered agents and workflows. Before Langflow 1.10.3, the MCP stdio tr… |
| 2026-10-05 21:16:35 | [CVE-2026-105698](https://nvd.nist.gov/vuln/detail/CVE-2026-105698) | Medium | 5.4 | Langflow is a tool for building and deploying AI-powered agents and workflows. From 1.0.0 until 1.10.1, Langflow did no… |
| 2026-10-05 21:16:35 | [CVE-2026-105699](https://nvd.nist.gov/vuln/detail/CVE-2026-105699) | High | 7.1 | Langflow is a tool for building and deploying AI-powered agents and workflows. From 1.6.8 until 1.9.1, Langflow authent… |
| 2026-10-05 21:16:35 | [CVE-2026-105740](https://nvd.nist.gov/vuln/detail/CVE-2026-105740) | Critical | 9.9 | Langflow is a tool for building and deploying AI-powered agents and workflows. Prior to 1.9.0, any authenticated Langfl… |
| 2026-10-05 21:16:35 | [CVE-2026-105741](https://nvd.nist.gov/vuln/detail/CVE-2026-105741) | High | 7.1 | Langflow is a tool for building and deploying AI-powered agents and workflows. From 1.5.0 until 1.10.3, an IP spoofing… |
| 2026-10-05 21:16:35 | [CVE-2026-105768](https://nvd.nist.gov/vuln/detail/CVE-2026-105768) | Medium | 6.3 | apko allows users to build and publish OCI container images built from apk packages. From version 0.2.0 to before versi… |
| 2026-10-05 21:16:36 | [CVE-2026-105773](https://nvd.nist.gov/vuln/detail/CVE-2026-105773) | High | 7.3 | Canimaan Software ClamXAV versions 3.3 - 3.11 contains a local privilege escalation vulnerability in the Privileged Hel… |
| 2026-10-05 21:16:37 | [CVE-2026-77226](https://nvd.nist.gov/vuln/detail/CVE-2026-77226) | Critical | 9.2 | Camunda 7.24.0 before 7.24.15 contains an incorrect authorization vulnerability in the Admin web application's first-ru… |
| 2026-10-05 21:16:37 | [CVE-2026-84900](https://nvd.nist.gov/vuln/detail/CVE-2026-84900) | Medium | 6.8 | Previous versions of HP ThinPro (prior to HP ThinPro 8.1 SP10) could potentially contain security vulnerabilities. HP h… |
| 2026-10-05 21:16:37 | [CVE-2026-93326](https://nvd.nist.gov/vuln/detail/CVE-2026-93326) | Medium | 6.0 | A build step for a Git source, crafted in a specific way, can bypass some policy validation rules. A malicious build de… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
