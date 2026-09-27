# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-09-27 14:19 UTC

New CVEs published between 2026-09-27 13:19 UTC and 2026-09-27 14:19 UTC.

[Full CSV](data/new-cves-2026-09-27T14-19-38-115834Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-09-27 14:16:28 | [CVE-2026-101032](https://nvd.nist.gov/vuln/detail/CVE-2026-101032) | High | 7.3 | navi through 2.24.0 fails to properly escape cheatsheet variable values when substituting them into shell commands. Att… |
| 2026-09-27 14:16:29 | [CVE-2026-101033](https://nvd.nist.gov/vuln/detail/CVE-2026-101033) | Medium | 5.3 | KitchenOwl through 0.7.10 fails to verify that category IDs belong to the caller's household in expense and item operat… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
