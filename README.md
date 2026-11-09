# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-11-09 02:18 UTC

New CVEs published between 2026-11-09 01:18 UTC and 2026-11-09 02:18 UTC.

[Full CSV](data/new-cves-2026-11-09T02-18-22-978639Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-11-09 02:16:58 | [CVE-2026-124508](https://nvd.nist.gov/vuln/detail/CVE-2026-124508) | Medium | 5.5 | A vulnerability was determined in floci-io Floci up to 2.4.0. Impacted is the function BuildspecParser.parseArtifacts o… |
| 2026-11-09 02:16:59 | [CVE-2026-124509](https://nvd.nist.gov/vuln/detail/CVE-2026-124509) | Medium | 5.5 | A vulnerability was identified in floci-io Floci up to 2.1.0. The affected element is the function S3Destination.bucket… |
| 2026-11-09 02:16:59 | [CVE-2026-124554](https://nvd.nist.gov/vuln/detail/CVE-2026-124554) | Medium | 5.5 | A security flaw has been discovered in JeecgBoot 3.9.5. This affects an unknown part of the file /jeecg-boot/drag/onlDr… |
| 2026-11-09 02:16:59 | [CVE-2026-124555](https://nvd.nist.gov/vuln/detail/CVE-2026-124555) | Low | 2.1 | A weakness has been identified in JeecgBoot 3.9.5. This vulnerability affects the function JimuFormApiService.getTableD… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
