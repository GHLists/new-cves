# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-11-04 04:19 UTC

New CVEs published between 2026-11-04 03:20 UTC and 2026-11-04 04:19 UTC.

[Full CSV](data/new-cves-2026-11-04T04-19-08-43496Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-11-04 04:17:33 | [CVE-2026-121803](https://nvd.nist.gov/vuln/detail/CVE-2026-121803) | Critical | 9.3 | In UFS Field Firmware Update (FFU) functionality, there is a possible out-of-bounds write due to missing bounds checkin… |
| 2026-11-04 04:17:37 | [CVE-2026-79405](https://nvd.nist.gov/vuln/detail/CVE-2026-79405) | High | 7.5 | In Modem Firmware, there is a possible system crash due to improper input validation of dedicated PUCCH configuration.… |
| 2026-11-04 04:17:37 | [CVE-2026-80335](https://nvd.nist.gov/vuln/detail/CVE-2026-80335) | High | 7.6 | In the bootloader download module, there is a possible out-of-bounds write due to a failure to reset a global offset va… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
