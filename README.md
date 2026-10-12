# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-12 12:18 UTC

New CVEs published between 2026-10-12 11:19 UTC and 2026-10-12 12:18 UTC.

[Full CSV](data/new-cves-2026-10-12T12-18-38-771258Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-10-12 12:17:12 | [CVE-2026-105283](https://nvd.nist.gov/vuln/detail/CVE-2026-105283) | Medium | 6.3 | Generation of Error Message Containing Sensitive Information vulnerability in ash-project ash_typescript allows an unau… |
| 2026-10-12 12:17:14 | [CVE-2026-108827](https://nvd.nist.gov/vuln/detail/CVE-2026-108827) | Low | 1.2 | A vulnerability was determined in Zen Cart up to 2.2.2. Affected is the function zen_call_function of the file admin/in… |
| 2026-10-12 12:17:14 | [CVE-2026-108828](https://nvd.nist.gov/vuln/detail/CVE-2026-108828) | Low | 1.2 | A vulnerability was identified in Zen Cart 2.2.2. Affected by this vulnerability is the function eval of the file admin… |
| 2026-10-12 12:17:14 | [CVE-2026-108829](https://nvd.nist.gov/vuln/detail/CVE-2026-108829) | Low | 2.0 | A security flaw has been discovered in Zen Cart up to 2.2.2. Affected by this issue is some unknown functionality of th… |
| 2026-10-12 12:17:14 | [CVE-2026-108830](https://nvd.nist.gov/vuln/detail/CVE-2026-108830) | Low | 1.3 | A weakness has been identified in meetecho janus-gateway up to 1.4.2. This affects an unknown part of the file src/plug… |
| 2026-10-12 12:17:15 | [CVE-2026-85499](https://nvd.nist.gov/vuln/detail/CVE-2026-85499) |  |  | Improper Authorization vulnerability in Apache SkyWalking BanyanDB. The Canopy includes incomplete proof-of-concept rol… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
