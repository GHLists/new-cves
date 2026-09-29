# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-09-29 01:18 UTC

New CVEs published between 2026-09-29 00:19 UTC and 2026-09-29 01:18 UTC.

[Full CSV](data/new-cves-2026-09-29T01-18-54-692552Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-09-29 01:16:43 | [CVE-2026-101278](https://nvd.nist.gov/vuln/detail/CVE-2026-101278) | Low | 2.1 | A weakness has been identified in Trusted Domain Project OpenDMARC up to 1.4.2. This affects the function opendmarc_get… |
| 2026-09-29 01:16:43 | [CVE-2026-101279](https://nvd.nist.gov/vuln/detail/CVE-2026-101279) | Medium | 5.5 | A security vulnerability has been detected in Trusted Domain Project OpenDMARC up to 1.4.2. This impacts an unknown fun… |
| 2026-09-29 01:16:44 | [CVE-2026-101280](https://nvd.nist.gov/vuln/detail/CVE-2026-101280) | Medium | 5.5 | A vulnerability was detected in Trusted Domain Project OpenDMARC up to 1.4.2. Affected is the function opendmarc_policy… |
| 2026-09-29 01:16:44 | [CVE-2026-101281](https://nvd.nist.gov/vuln/detail/CVE-2026-101281) | Medium | 5.5 | A flaw has been found in Trusted Domain Project OpenDMARC up to 1.4.2. Affected by this vulnerability is the function o… |
| 2026-09-29 01:16:44 | [CVE-2026-102372](https://nvd.nist.gov/vuln/detail/CVE-2026-102372) | Medium | 5.3 | GestSup versions before 3.2.62 fail to properly sanitize HTML email bodies in the IMAP LOGIN connector, allowing unauth… |
| 2026-09-29 01:16:44 | [CVE-2026-102373](https://nvd.nist.gov/vuln/detail/CVE-2026-102373) | High | 7.1 | GestSup versions before 3.2.62 fail to validate ticket ownership when loading comments via the threadedit parameter in… |
| 2026-09-29 01:16:44 | [CVE-2026-102374](https://nvd.nist.gov/vuln/detail/CVE-2026-102374) | Medium | 5.3 | GestSup versions before 3.2.62 contain a stored cross-site scripting vulnerability in the IMAP OAuth connector that dou… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
