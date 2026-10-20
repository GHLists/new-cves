# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-20 00:18 UTC

New CVEs published between 2026-10-19 23:18 UTC and 2026-10-20 00:18 UTC.

[Full CSV](data/new-cves-2026-10-20T00-18-58-527448Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-10-20 00:17:23 | [CVE-2026-105453](https://nvd.nist.gov/vuln/detail/CVE-2026-105453) | High | 8.4 | IBM Sterling Connect Direct for Unix 6.3.0.0 through 6.3.0.7 and 6.4.0.0 through 6.4.0.6 could allow a local attacker t… |
| 2026-10-20 00:17:25 | [CVE-2026-107366](https://nvd.nist.gov/vuln/detail/CVE-2026-107366) | High | 8.3 | IBM Langflow OSS 1.0.0 through 1.12.4 contains three message endpoints that perform no ownership verification. Any auth… |
| 2026-10-20 00:17:25 | [CVE-2026-107400](https://nvd.nist.gov/vuln/detail/CVE-2026-107400) | High | 8.8 | IBM TRIRIGA Application Platform 5.0.0 through 5.0.8 could allow a remote authenticated attacker to execute arbitrary c… |
| 2026-10-20 00:17:30 | [CVE-2026-109126](https://nvd.nist.gov/vuln/detail/CVE-2026-109126) | High | 8.8 | IBM Verify Identity Access 11.0.3.1 and IBM Security Verify Access 10.0.9.3 Appliance could allow a physically proximat… |
| 2026-10-20 00:17:30 | [CVE-2026-112373](https://nvd.nist.gov/vuln/detail/CVE-2026-112373) | Medium | 5.7 | A security vulnerability has been detected in H3C Magic NX15 NX15V100R017. This impacts the function sub_416874 of the… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
