# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-11-15 01:18 UTC

New CVEs published between 2026-11-15 00:18 UTC and 2026-11-15 01:18 UTC.

[Full CSV](data/new-cves-2026-11-15T01-18-17-174653Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-11-15 01:18:03 | [CVE-2026-129354](https://nvd.nist.gov/vuln/detail/CVE-2026-129354) | Critical | 9.3 | A flaw has been found in D-Link DIR-600L 2.17b02. Affected by this issue is the function hnap_main of the file htdocs/c… |
| 2026-11-15 01:18:03 | [CVE-2026-129355](https://nvd.nist.gov/vuln/detail/CVE-2026-129355) | Medium | 6.9 | A vulnerability has been found in sigoden dufs up to 0.46.0. This affects an unknown part of the file src/server.rs of… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
