# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-01 04:18 UTC

New CVEs published between 2026-10-01 03:18 UTC and 2026-10-01 04:18 UTC.

[Full CSV](data/new-cves-2026-10-01T04-18-33-908563Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-10-01 04:18:04 | [CVE-2026-103534](https://nvd.nist.gov/vuln/detail/CVE-2026-103534) | Low | 2.1 | A vulnerability was determined in David-Crty databasement up to 1.7.1. Affected is the function SnapshotPolicy.viewAny/… |
| 2026-10-01 04:18:04 | [CVE-2026-103641](https://nvd.nist.gov/vuln/detail/CVE-2026-103641) | Medium | 5.5 | A flaw was found in GEGL. The Radiance HDR loader reads past the end of a memory-mapped image when an uncompressed scan… |
| 2026-10-01 04:18:21 | [CVE-2026-91109](https://nvd.nist.gov/vuln/detail/CVE-2026-91109) | Medium | 6.5 | The Simply Schedule Appointments plugin for WordPress is vulnerable to Insecure Direct Object Reference in all versions… |
| 2026-10-01 04:18:21 | [CVE-2026-92245](https://nvd.nist.gov/vuln/detail/CVE-2026-92245) | High | 7.5 | The Simply Schedule Appointments plugin for WordPress is vulnerable to Sensitive Information Exposure in all versions u… |
| 2026-10-01 04:18:22 | [CVE-2026-96561](https://nvd.nist.gov/vuln/detail/CVE-2026-96561) | High | 7.2 | The AI Engine – The Chatbot, AI Framework & MCP for WordPress plugin for WordPress is vulnerable to Stored Cross-Site S… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
