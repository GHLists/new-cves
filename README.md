# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-05 01:19 UTC

New CVEs published between 2026-10-05 00:19 UTC and 2026-10-05 01:19 UTC.

[Full CSV](data/new-cves-2026-10-05T01-19-51-105323Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-10-05 01:16:27 | [CVE-2026-105172](https://nvd.nist.gov/vuln/detail/CVE-2026-105172) | Medium | 5.5 | A vulnerability was detected in itsourcecode Online Admission System 1.0. Affected by this issue is some unknown functi… |
| 2026-10-05 01:16:27 | [CVE-2026-105173](https://nvd.nist.gov/vuln/detail/CVE-2026-105173) | Low | 2.0 | A flaw has been found in code-projects Human Resource Management 1.0. This affects an unknown part of the file /humanre… |
| 2026-10-05 01:16:28 | [CVE-2026-105174](https://nvd.nist.gov/vuln/detail/CVE-2026-105174) | Low | 2.1 | A vulnerability has been found in Gerapy up to 0.9.13. This vulnerability affects the function project_create of the fi… |
| 2026-10-05 01:16:28 | [CVE-2026-105175](https://nvd.nist.gov/vuln/detail/CVE-2026-105175) | Medium | 5.5 | A vulnerability was found in SourceCodester Drug Recommendation System 1.0. This issue affects some unknown processing… |
| 2026-10-05 01:16:28 | [CVE-2026-105223](https://nvd.nist.gov/vuln/detail/CVE-2026-105223) | Critical | 9.1 | maclof kubernetes-client 0.17.0 before 0.32.0 disables TLS certificate verification in parseKubeconfig() and parseKubec… |
| 2026-10-05 01:16:28 | [CVE-2026-105292](https://nvd.nist.gov/vuln/detail/CVE-2026-105292) | Medium | 6.0 | Chaterm before 0.12.1 contains a login cross-site request forgery vulnerability that allows remote attackers to inject… |
| 2026-10-05 01:16:28 | [CVE-2026-105293](https://nvd.nist.gov/vuln/detail/CVE-2026-105293) | Critical | 9.2 | Legcord 1.1.0 through 1.3.0 contains a path traversal vulnerability in theme IPC handlers that allows script in the Dis… |
| 2026-10-05 01:16:28 | [CVE-2026-105294](https://nvd.nist.gov/vuln/detail/CVE-2026-105294) | Critical | 9.1 | Legcord 1.1.0 through 1.3.0 contains a configuration injection vulnerability that allows script in the Discord page to… |
| 2026-10-05 01:16:29 | [CVE-2026-105295](https://nvd.nist.gov/vuln/detail/CVE-2026-105295) | High | 7.7 | GitAhead 2.5.0 through 2.7.1 contains an insecure update mechanism that installs downloaded updates without integrity o… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
