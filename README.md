# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-08 08:18 UTC

New CVEs published between 2026-10-08 07:19 UTC and 2026-10-08 08:18 UTC.

[Full CSV](data/new-cves-2026-10-08T08-18-47-786247Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-10-08 08:16:34 | [CVE-2026-107466](https://nvd.nist.gov/vuln/detail/CVE-2026-107466) | Medium | 6.1 | A flaw was found in flatpak-builder. This vulnerability allows an attacker to cause information disclosure by convincin… |
| 2026-10-08 08:16:34 | [CVE-2026-93699](https://nvd.nist.gov/vuln/detail/CVE-2026-93699) | High | 8.5 | Argument injection in WP Toolkit for cPanel allows local users to execute arbitrary code as other accounts on the same… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
