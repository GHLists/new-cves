# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-25 03:18 UTC

New CVEs published between 2026-10-25 02:18 UTC and 2026-10-25 03:18 UTC.

[Full CSV](data/new-cves-2026-10-25T03-18-41-419709Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-10-25 03:16:26 | [CVE-2026-116000](https://nvd.nist.gov/vuln/detail/CVE-2026-116000) | Medium | 5.5 | A security flaw has been discovered in Zylon PrivateGPT 1.0.0/1.0.1. This vulnerability affects the function load_file_… |
| 2026-10-25 03:16:27 | [CVE-2026-116004](https://nvd.nist.gov/vuln/detail/CVE-2026-116004) | Low | 2.0 | A security vulnerability has been detected in onyx-dot-app Onyx up to 5.0.0. Impacted is an unknown function of the fil… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
