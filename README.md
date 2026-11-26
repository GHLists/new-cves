# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-11-26 22:20 UTC

New CVEs published between 2026-11-26 21:18 UTC and 2026-11-26 22:20 UTC.

[Full CSV](data/new-cves-2026-11-26T22-20-47-911088Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-11-26 22:17:55 | [CVE-2026-137621](https://nvd.nist.gov/vuln/detail/CVE-2026-137621) | Medium | 4.8 | A weakness has been identified in RT-Thread up to 5.3.0. Affected by this vulnerability is the function bl_adc_get_valu… |
| 2026-11-26 22:17:58 | [CVE-2026-4981](https://nvd.nist.gov/vuln/detail/CVE-2026-4981) | Medium | 5.4 | A flaw was found in Red Hat Advanced Cluster Security (ACS). An unauthenticated remote attacker can exploit a vulnerabi… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
