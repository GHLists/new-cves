# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-07 12:18 UTC

New CVEs published between 2026-10-07 11:20 UTC and 2026-10-07 12:18 UTC.

[Full CSV](data/new-cves-2026-10-07T12-18-35-050469Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-10-07 12:17:08 | [CVE-2026-106056](https://nvd.nist.gov/vuln/detail/CVE-2026-106056) | High | 7.7 | Rundeck before 6.2.0 contains an OS command injection vulnerability that allows authenticated users with job run permis… |
| 2026-10-07 12:17:08 | [CVE-2026-106057](https://nvd.nist.gov/vuln/detail/CVE-2026-106057) | High | 8.5 | patool before 4.0.6 contains an OS command injection vulnerability on Windows because shell_quote_nt fails to escape cm… |
| 2026-10-07 12:17:08 | [CVE-2026-106058](https://nvd.nist.gov/vuln/detail/CVE-2026-106058) | High | 7.7 | GitAhead through 2.7.1 contains an OS command injection vulnerability in src/git/Filter.cpp that allows malicious repos… |
| 2026-10-07 12:17:09 | [CVE-2026-106059](https://nvd.nist.gov/vuln/detail/CVE-2026-106059) | High | 8.7 | GitAhead through 2.7.1 on macOS contains a command injection vulnerability that allows attackers to execute shell comma… |
| 2026-10-07 12:17:09 | [CVE-2026-107159](https://nvd.nist.gov/vuln/detail/CVE-2026-107159) | High | 7.1 | MiniUPnPd through 2.3.11 built with --strict contains a divide-by-zero vulnerability in ProcessSSDPData() that allows u… |
| 2026-10-07 12:17:09 | [CVE-2026-42708](https://nvd.nist.gov/vuln/detail/CVE-2026-42708) | High | 7.6 | Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection') vulnerability in AF themes WP Post… |
| 2026-10-07 12:17:09 | [CVE-2026-42710](https://nvd.nist.gov/vuln/detail/CVE-2026-42710) | High | 7.6 | Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection') vulnerability in 10Web Slider by 1… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
