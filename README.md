# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-11-18 07:19 UTC

New CVEs published between 2026-11-18 06:20 UTC and 2026-11-18 07:19 UTC.

[Full CSV](data/new-cves-2026-11-18T07-19-00-390554Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-11-18 07:17:22 | [CVE-2026-131920](https://nvd.nist.gov/vuln/detail/CVE-2026-131920) | Medium | 6.9 | In OpenStack Cinder before 29.1.1, by making an os-initialize_connection request with an IQN that includes a path trave… |
| 2026-11-18 07:17:22 | [CVE-2026-131922](https://nvd.nist.gov/vuln/detail/CVE-2026-131922) | Medium | 4.3 | In OpenStack keystonemiddleware before 13.0.3, by supplying a malicious regular expression when creating an application… |
| 2026-11-18 07:17:22 | [CVE-2026-1209](https://nvd.nist.gov/vuln/detail/CVE-2026-1209) | Medium | 4.3 | The BuddyPress plugin for WordPress is vulnerable to unauthorized modification of data due to a misconfigured capabilit… |
| 2026-11-18 07:17:22 | [CVE-2026-2841](https://nvd.nist.gov/vuln/detail/CVE-2026-2841) | Medium | 4.3 | The Advanced Custom Fields (ACF) plugin for WordPress is vulnerable to incorrect authorization in all versions up to, a… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
