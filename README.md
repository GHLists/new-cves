# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-22 21:19 UTC

New CVEs published between 2026-10-22 20:18 UTC and 2026-10-22 21:19 UTC.

[Full CSV](data/new-cves-2026-10-22T21-19-16-55858Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-10-22 21:17:16 | [CVE-2026-114583](https://nvd.nist.gov/vuln/detail/CVE-2026-114583) | Medium | 6.9 | tarfile.tar_filter could be bypassed using crafted link entries, including symlinks with empty or directory-like names,… |
| 2026-10-22 21:17:16 | [CVE-2026-114614](https://nvd.nist.gov/vuln/detail/CVE-2026-114614) | Low | 2.6 | Authlib is a Python library which builds OAuth and OpenID Connect servers. From 0.13 until 1.8.0, authlib.common.securi… |
| 2026-10-22 21:17:16 | [CVE-2026-114625](https://nvd.nist.gov/vuln/detail/CVE-2026-114625) | Critical | 9.4 | VeloCloud Orchestrator (VCO) on-prem has a security issue where this issue may allow a remote attacker to access privil… |
| 2026-10-22 21:17:17 | [CVE-2026-115417](https://nvd.nist.gov/vuln/detail/CVE-2026-115417) | High | 8.2 | Memory allocation with excessive size value in the MQTT 3.1.1 compatibility adapter in AWS aws-c-mqtt before 0.16.2 mig… |
| 2026-10-22 21:17:17 | [CVE-2026-115419](https://nvd.nist.gov/vuln/detail/CVE-2026-115419) | High | 8.6 | The A2A server component in Amazon Strands Agents SDK for Python before 1.43.0 and Amazon Strands Agents SDK for TypeSc… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
