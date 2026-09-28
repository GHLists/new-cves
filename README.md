# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-09-28 15:19 UTC

New CVEs published between 2026-09-28 14:20 UTC and 2026-09-28 15:19 UTC.

[Full CSV](data/new-cves-2026-09-28T15-19-47-973919Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-09-28 15:17:12 | [CVE-2026-101073](https://nvd.nist.gov/vuln/detail/CVE-2026-101073) | Medium | 5.5 | A security flaw has been discovered in Netcore NR289-GE 1.4.5102. Impacted is an unknown function of the file /bin/boa… |
| 2026-09-28 15:17:12 | [CVE-2026-101074](https://nvd.nist.gov/vuln/detail/CVE-2026-101074) | High | 8.9 | A weakness has been identified in Netcore NR289-GE 1.4.5102. The affected element is the function password-check of the… |
| 2026-09-28 15:17:13 | [CVE-2026-101075](https://nvd.nist.gov/vuln/detail/CVE-2026-101075) | Critical | 9.3 | A security vulnerability has been detected in Netcore NR289-GE 1.4.5102. The impacted element is the function system of… |
| 2026-09-28 15:17:13 | [CVE-2026-101333](https://nvd.nist.gov/vuln/detail/CVE-2026-101333) | Low | 3.7 | A flaw was found in the Micrometer user-event metrics listener of Keycloak, a solution for integrated identity and acce… |
| 2026-09-28 15:17:17 | [CVE-2026-4556](https://nvd.nist.gov/vuln/detail/CVE-2026-4556) | High | 7.8 | Exam4 is affected by a local privilege escalation vulnerability in the com.extegrity.LogTool privileged helper, which c… |
| 2026-09-28 15:17:23 | [CVE-2026-70413](https://nvd.nist.gov/vuln/detail/CVE-2026-70413) | Medium | 5.6 | Dell Live Optics Collector, versions prior to 27.2.13.310, contain(s) a Use of Hard-coded Password vulnerability. A low… |
| 2026-09-28 15:17:23 | [CVE-2026-80357](https://nvd.nist.gov/vuln/detail/CVE-2026-80357) | High | 7.0 | Dell Boot Optimized Server Storage (BOSS), versions prior to 2.2.13.2038, contains an On-Chip Debug and Test Interface… |
| 2026-09-28 15:17:23 | [CVE-2026-80358](https://nvd.nist.gov/vuln/detail/CVE-2026-80358) | Medium | 5.1 | Dell Boot Optimized Server Storage (BOSS), versions prior to 2.2.13.2038, contains an On-Chip Debug and Test Interface… |
| 2026-09-28 15:17:24 | [CVE-2026-80359](https://nvd.nist.gov/vuln/detail/CVE-2026-80359) | Medium | 6.8 | Dell Boot Optimized Server Storage (BOSS), versions prior to 2.2.13.2038, contains an On-Chip Debug and Test Interface… |
| 2026-09-28 15:17:24 | [CVE-2026-93538](https://nvd.nist.gov/vuln/detail/CVE-2026-93538) | High | 7.1 | A cross-tenant authorization issue was discovered in SUSE Rancher Fleet. During agent-initiated cluster registration, c… |
| 2026-09-28 15:17:25 | [CVE-2026-93539](https://nvd.nist.gov/vuln/detail/CVE-2026-93539) | Medium | 5.4 | A vulnerability was discovered in Fleet's Git webhook receiver (the gitjob webhook service). When a webhook secret is n… |
| 2026-09-28 15:17:25 | [CVE-2026-93540](https://nvd.nist.gov/vuln/detail/CVE-2026-93540) | Medium | 6.5 | A privilege mismatch was found in Fleet. When a bundle requested namespace labels or annotations through the namespaceL… |
| 2026-09-28 15:17:25 | [CVE-2026-96538](https://nvd.nist.gov/vuln/detail/CVE-2026-96538) | High | 8.7 | WarehousePG (WHPG) 7.x before 7.6.0-WHPG is affected by a missing authorization vulnerability (CWE-862) in the built-in… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
