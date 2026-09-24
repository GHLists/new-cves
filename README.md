# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-09-24 11:19 UTC

New CVEs published between 2026-09-24 10:19 UTC and 2026-09-24 11:19 UTC.

[Full CSV](data/new-cves-2026-09-24T11-19-02-351758Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-09-24 11:16:45 | [CVE-2026-4638](https://nvd.nist.gov/vuln/detail/CVE-2026-4638) | High | 7.1 | PRTG Network Monitor before version 26.2.120.1449 ships a demo EXE/Script sensor that multiplies two integer parameters… |
| 2026-09-24 11:16:47 | [CVE-2026-79680](https://nvd.nist.gov/vuln/detail/CVE-2026-79680) | Medium | 4.5 | Authentication bypass vulnerability in the password authentication mechanism of the Qt VNC Server module. An attacker u… |
| 2026-09-24 11:17:06 | [CVE-2026-97179](https://nvd.nist.gov/vuln/detail/CVE-2026-97179) | Low | 2.1 | A security vulnerability has been detected in O2OA up to 9.5.3/10.0.2. This vulnerability affects the function list of… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
