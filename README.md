# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-11-23 02:20 UTC

New CVEs published between 2026-11-23 01:18 UTC and 2026-11-23 02:20 UTC.

[Full CSV](data/new-cves-2026-11-23T02-20-32-100443Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-11-23 02:16:37 | [CVE-2026-134782](https://nvd.nist.gov/vuln/detail/CVE-2026-134782) | Low | 2.1 | A flaw has been found in Open Asset Import Library Assimp up to 6.0.6. This impacts the function Assimp::ColladaLoader:… |
| 2026-11-23 02:16:37 | [CVE-2026-134783](https://nvd.nist.gov/vuln/detail/CVE-2026-134783) | Medium | 5.3 | A vulnerability has been found in xuxueli xxl-job 3.5.0/3.5.1-SNAPSHOT. Affected is the function difyWorkflowJobHandler… |
| 2026-11-23 02:16:37 | [CVE-2026-134784](https://nvd.nist.gov/vuln/detail/CVE-2026-134784) | Medium | 6.9 | A vulnerability was found in DumbWareio DumbDrop up to ff8f813f493e89c7da056e7a3101ce2ef48e3960. Affected by this vulne… |
| 2026-11-23 02:16:38 | [CVE-2026-134785](https://nvd.nist.gov/vuln/detail/CVE-2026-134785) | Medium | 6.9 | A vulnerability was identified in Bagisto MangoPay Payment Gateway up to c061edcc7973cb37a77a9f9ae523db170c3e28ed. Affe… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
