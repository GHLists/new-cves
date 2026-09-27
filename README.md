# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-09-27 22:21 UTC

New CVEs published between 2026-09-27 21:18 UTC and 2026-09-27 22:21 UTC.

[Full CSV](data/new-cves-2026-09-27T22-21-10-531312Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-09-27 22:17:05 | [CVE-2026-100881](https://nvd.nist.gov/vuln/detail/CVE-2026-100881) | Low | 1.2 | A security vulnerability has been detected in zhistaredu StarTraining up to 3.8.1. This issue affects some unknown proc… |
| 2026-09-27 22:17:06 | [CVE-2026-100882](https://nvd.nist.gov/vuln/detail/CVE-2026-100882) | Low | 1.9 | A vulnerability was detected in Krayin laravel-crm up to 2.2.5. Impacted is an unknown function of the file packages/We… |
| 2026-09-27 22:17:06 | [CVE-2026-96282](https://nvd.nist.gov/vuln/detail/CVE-2026-96282) | Low | 3.1 | A malicious Flatpak extension can probe the host filesystem to determine what files and directories exist at arbitrary… |
| 2026-09-27 22:17:06 | [CVE-2026-96283](https://nvd.nist.gov/vuln/detail/CVE-2026-96283) | Low | 3.3 | By calling org.freedesktop.Flatpak.SystemHelper.CancelPull on another user's pull, the pull is not actually cancelled b… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
