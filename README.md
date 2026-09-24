# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-09-24 23:20 UTC

New CVEs published between 2026-09-24 22:20 UTC and 2026-09-24 23:20 UTC.

[Full CSV](data/new-cves-2026-09-24T23-20-21-347613Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-09-24 23:19:22 | [CVE-2026-97230](https://nvd.nist.gov/vuln/detail/CVE-2026-97230) |  |  | IO::Socket::SSL::SelfCertificate versions 1.00 for Perl contains malware which executes Python code from an obfuscated… |
| 2026-09-24 23:19:23 | [CVE-2026-97387](https://nvd.nist.gov/vuln/detail/CVE-2026-97387) |  |  | Rejected reason: This CVE is a duplicate of another CVE. |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
