# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-05 08:18 UTC

New CVEs published between 2026-10-05 07:18 UTC and 2026-10-05 08:18 UTC.

[Full CSV](data/new-cves-2026-10-05T08-18-47-1169Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-10-05 08:17:15 | [CVE-2026-105247](https://nvd.nist.gov/vuln/detail/CVE-2026-105247) | Medium | 5.5 | A vulnerability was determined in SourceCodester Online Reviewer Management System 1.0. The affected element is an unkn… |
| 2026-10-05 08:17:15 | [CVE-2026-105248](https://nvd.nist.gov/vuln/detail/CVE-2026-105248) | Medium | 5.3 | A security flaw has been discovered in vgmstream up to r2117. This affects the function parse_params/txtp_parse of the… |
| 2026-10-05 08:17:15 | [CVE-2026-105249](https://nvd.nist.gov/vuln/detail/CVE-2026-105249) | Low | 2.4 | A weakness has been identified in vgmstream up to r2117. This impacts the function make_group_random of the file src/me… |
| 2026-10-05 08:17:15 | [CVE-2026-105250](https://nvd.nist.gov/vuln/detail/CVE-2026-105250) | Medium | 5.3 | A security vulnerability has been detected in vgmstream up to r2117. Affected is the function decode_ms_ima of the file… |
| 2026-10-05 08:17:15 | [CVE-2026-105314](https://nvd.nist.gov/vuln/detail/CVE-2026-105314) | High | 7.5 | Papermerge 3.5.3 allows remote code execution by a standard user via directory traversal in a /api/documents/upload cal… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
