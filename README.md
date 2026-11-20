# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-11-20 03:20 UTC

New CVEs published between 2026-11-20 02:18 UTC and 2026-11-20 03:20 UTC.

[Full CSV](data/new-cves-2026-11-20T03-20-58-920142Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-11-20 03:17:34 | [CVE-2026-133477](https://nvd.nist.gov/vuln/detail/CVE-2026-133477) | Medium | 6.3 | A weakness has been identified in sofastack sofa-bolt up to 1.6.12. This impacts the function initSSLContext of the fil… |
| 2026-11-20 03:17:34 | [CVE-2026-133478](https://nvd.nist.gov/vuln/detail/CVE-2026-133478) | Medium | 5.5 | A security vulnerability has been detected in rajesh2211 Doctor-Appointment-System up to ee974dcf4c50da85e6ea026e27f437… |
| 2026-11-20 03:17:35 | [CVE-2026-133479](https://nvd.nist.gov/vuln/detail/CVE-2026-133479) | Low | 2.0 | A vulnerability was detected in WebKul QloApps up to 1.8.0. Affected by this vulnerability is the function postProcessD… |
| 2026-11-20 03:17:35 | [CVE-2026-133534](https://nvd.nist.gov/vuln/detail/CVE-2026-133534) | High | 8.7 | PowerLink developed by Neotroni Lighting has a SQL Injection vulnerability, allowing unauthenticated remote attackers t… |
| 2026-11-20 03:17:35 | [CVE-2026-133535](https://nvd.nist.gov/vuln/detail/CVE-2026-133535) | Medium | 4.3 | A flaw was found in Hawtio. An authenticated remote attacker can cause a Denial of Service (DoS) by sending a specially… |
| 2026-11-20 03:17:35 | [CVE-2026-24205](https://nvd.nist.gov/vuln/detail/CVE-2026-24205) | Medium | 6.4 | NVIDIA TensorRT-LLM for any platform contains a vulnerability where a user may cause a race condition by running concur… |
| 2026-11-20 03:17:36 | [CVE-2026-65094](https://nvd.nist.gov/vuln/detail/CVE-2026-65094) | Critical | 9.0 | NVIDIA VIRTIO-Net for Bluefield contains a vulnerability in Virtio-Net where a VM user may cause a Write-What-Where con… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
