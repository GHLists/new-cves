# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-07 00:19 UTC

New CVEs published between 2026-10-06 23:18 UTC and 2026-10-07 00:19 UTC.

[Full CSV](data/new-cves-2026-10-07T00-19-10-054922Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-10-07 00:17:20 | [CVE-2026-104335](https://nvd.nist.gov/vuln/detail/CVE-2026-104335) | High | 8.8 | IBM Langflow OSS 1.0.0 through 1.12.2 could allow a remote authenticated attacker to execute arbitrary code due to impr… |
| 2026-10-07 00:17:20 | [CVE-2026-106583](https://nvd.nist.gov/vuln/detail/CVE-2026-106583) | Low | 2.5 | In ssh in OpenSSH before 10.6, a $ or \ character can occur in a command-line username, leading to injection. |
| 2026-10-07 00:17:21 | [CVE-2026-80048](https://nvd.nist.gov/vuln/detail/CVE-2026-80048) |  |  | A flaw was found in `sssd-kcm`. A local user or process able to connect to the `sssd-kcm` UNIX socket can exploit this… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
