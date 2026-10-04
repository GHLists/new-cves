# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-04 23:19 UTC

New CVEs published between 2026-10-04 22:18 UTC and 2026-10-04 23:19 UTC.

[Full CSV](data/new-cves-2026-10-04T23-19-47-503134Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-10-04 23:16:58 | [CVE-2026-105165](https://nvd.nist.gov/vuln/detail/CVE-2026-105165) | Medium | 5.3 | A vulnerability has been found in devopspolis secrets-replicator up to 0.4.0. Impacted is the function process_single_s… |
| 2026-10-04 23:16:59 | [CVE-2026-105166](https://nvd.nist.gov/vuln/detail/CVE-2026-105166) | Medium | 5.5 | A vulnerability was found in kishor-23 food-waste-management-system 411989e3ecb82895e53dca7865f72145f03d7d93/b3a70b2c49… |
| 2026-10-04 23:16:59 | [CVE-2026-105167](https://nvd.nist.gov/vuln/detail/CVE-2026-105167) | Medium | 5.5 | A vulnerability was determined in kishor-23 food-waste-management-system 411989e3ecb82895e53dca7865f72145f03d7d93/b3a70… |
| 2026-10-04 23:16:59 | [CVE-2026-105220](https://nvd.nist.gov/vuln/detail/CVE-2026-105220) | High | 8.5 | Twine 2 desktop through 2.12.0 contains a cross-site scripting vulnerability in importStories() that executes markup fr… |
| 2026-10-04 23:16:59 | [CVE-2026-105221](https://nvd.nist.gov/vuln/detail/CVE-2026-105221) | Critical | 9.1 | The gist RubyGem before 6.1.0 contains an improper certificate validation vulnerability that allows on-path attackers t… |
| 2026-10-04 23:16:59 | [CVE-2026-105222](https://nvd.nist.gov/vuln/detail/CVE-2026-105222) | Critical | 9.1 | The alexpechkarev/google-maps Laravel package through 12.16 disables TLS certificate verification by default because th… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
