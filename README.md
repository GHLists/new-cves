# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-11-18 05:20 UTC

New CVEs published between 2026-11-18 04:18 UTC and 2026-11-18 05:20 UTC.

[Full CSV](data/new-cves-2026-11-18T05-20-17-564016Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-11-18 05:19:01 | [CVE-2026-117657](https://nvd.nist.gov/vuln/detail/CVE-2026-117657) | Low | 2.3 | A Cleartext Transmission of Sensitive Information (CWE-319) vulnerability exists in the Android application "Imperial P… |
| 2026-11-18 05:19:02 | [CVE-2026-118900](https://nvd.nist.gov/vuln/detail/CVE-2026-118900) | High | 8.4 | An OS command injection vulnerability exists in the Android application "Imperial Palaces Guide" provided by The Imperi… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
