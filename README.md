# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-11-26 06:19 UTC

New CVEs published between 2026-11-26 05:18 UTC and 2026-11-26 06:19 UTC.

[Full CSV](data/new-cves-2026-11-26T06-19-38-664126Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-11-26 06:17:02 | [CVE-2026-129838](https://nvd.nist.gov/vuln/detail/CVE-2026-129838) | Low | 3.3 | A flaw was found in rsyslog. This vulnerability allows a local user to spoof sender identity and cause downstream log c… |
| 2026-11-26 06:17:03 | [CVE-2026-135106](https://nvd.nist.gov/vuln/detail/CVE-2026-135106) |  |  | Rejected reason: This CVE has been rejected by Upstream. Ref: https://bugzilla.samba.org/show_bug.cgi?id=16047#c4 |
| 2026-11-26 06:17:03 | [CVE-2026-137311](https://nvd.nist.gov/vuln/detail/CVE-2026-137311) | Medium | 5.5 | A vulnerability was identified in SourceCodester Online Food Ordering System 1.0. Affected by this vulnerability is an… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
