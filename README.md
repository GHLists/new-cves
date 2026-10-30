# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-30 08:18 UTC

New CVEs published between 2026-10-30 07:20 UTC and 2026-10-30 08:18 UTC.

[Full CSV](data/new-cves-2026-10-30T08-18-54-023614Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-10-30 08:16:55 | [CVE-2026-114690](https://nvd.nist.gov/vuln/detail/CVE-2026-114690) | Medium | 6.2 | A flaw was found in GCC. An out-of-bounds memory access vulnerability exists in the libstdc++ parallel search implement… |
| 2026-10-30 08:16:55 | [CVE-2026-114691](https://nvd.nist.gov/vuln/detail/CVE-2026-114691) | Medium | 5.9 | A flaw was found in the libstdc++ component of GCC. An attacker who can provide an excessively large element count to a… |
| 2026-10-30 08:16:55 | [CVE-2026-115455](https://nvd.nist.gov/vuln/detail/CVE-2026-115455) | Medium | 6.5 | A flaw was found in GCC libstdc++. When an application extracts data into a bitset from a wide-character stream, intern… |
| 2026-10-30 08:17:00 | [CVE-2026-82104](https://nvd.nist.gov/vuln/detail/CVE-2026-82104) | Critical | 9.4 | In Teltonika Networks RUTOS devices running versions from 7.22 through 7.24.2 and TSWOS devices running versions 1.9 th… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
