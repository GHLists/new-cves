# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-09-29 14:19 UTC

New CVEs published between 2026-09-29 13:20 UTC and 2026-09-29 14:19 UTC.

[Full CSV](data/new-cves-2026-09-29T14-19-36-068086Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-09-29 14:17:20 | [CVE-2026-102360](https://nvd.nist.gov/vuln/detail/CVE-2026-102360) | High | 8.6 | A missing bounds check in the binary decoder in lib0, versions 0.2.1-0.2.117 and earlier and 1.0.0-rc.32 and earlier, l… |
| 2026-09-29 14:17:20 | [CVE-2026-102521](https://nvd.nist.gov/vuln/detail/CVE-2026-102521) | High | 8.6 | The decoder in `readFromDataView` in lib0 before 0.2.119 can be tricked into reading more than it should from a buffer.… |
| 2026-09-29 14:17:20 | [CVE-2026-4034](https://nvd.nist.gov/vuln/detail/CVE-2026-4034) | High | 8.7 | Injection Vulnerability in Tibco Administrator version 5.13.0 & prior allows an authenticated user to submit specially… |
| 2026-09-29 14:17:20 | [CVE-2026-71897](https://nvd.nist.gov/vuln/detail/CVE-2026-71897) |  |  | An improper authorization check in Apache DolphinScheduler allows an authenticated user to use the batch-copy and batch… |
| 2026-09-29 14:17:21 | [CVE-2026-71898](https://nvd.nist.gov/vuln/detail/CVE-2026-71898) |  |  | An incorrect authorization check in Apache DolphinScheduler allows an authenticated user with only read permission for… |
| 2026-09-29 14:17:21 | [CVE-2026-71899](https://nvd.nist.gov/vuln/detail/CVE-2026-71899) |  |  | A missing authorization vulnerability exists in the `query-dynamic-sub-workflows` API of Apache DolphinScheduler. The A… |
| 2026-09-29 14:17:21 | [CVE-2026-78214](https://nvd.nist.gov/vuln/detail/CVE-2026-78214) |  |  | An authentication bypass vulnerability exists in the protection of Actuator endpoints. The application determines wheth… |
| 2026-09-29 14:17:21 | [CVE-2026-81569](https://nvd.nist.gov/vuln/detail/CVE-2026-81569) |  |  | An improper authorization vulnerability exists in the handling of sub-workflow tasks. An authenticated user who does no… |
| 2026-09-29 14:17:21 | [CVE-2026-86450](https://nvd.nist.gov/vuln/detail/CVE-2026-86450) | High | 7.5 | Insertion of sensitive information into sent data vulnerability in Parla Auto Automotive Trading Limited Company DetaWi… |
| 2026-09-29 14:17:22 | [CVE-2026-97395](https://nvd.nist.gov/vuln/detail/CVE-2026-97395) |  |  | Apache Polaris allows an authenticated principal with permission to create or update Iceberg table properties to set Fi… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
