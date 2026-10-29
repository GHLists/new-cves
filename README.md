# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-29 01:19 UTC

New CVEs published between 2026-10-29 00:20 UTC and 2026-10-29 01:19 UTC.

[Full CSV](data/new-cves-2026-10-29T01-19-46-988126Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-10-29 01:17:22 | [CVE-2026-113957](https://nvd.nist.gov/vuln/detail/CVE-2026-113957) |  |  | An attacker who controls the registry, a mirror, or the network path to it may be able to serve arbitrary image content… |
| 2026-10-29 01:17:22 | [CVE-2026-118590](https://nvd.nist.gov/vuln/detail/CVE-2026-118590) | Medium | 6.9 | A security vulnerability has been detected in nipy nibabel up to 5.4.2. The affected element is the function array_from… |
| 2026-10-29 01:17:23 | [CVE-2026-21157](https://nvd.nist.gov/vuln/detail/CVE-2026-21157) | High | 8.3 | Improper input validation in Bixby prior to version 4.0.85.6 allows privileged local attackers to launch arbitrary acti… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
