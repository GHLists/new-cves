# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-11 12:21 UTC

New CVEs published between 2026-10-11 11:18 UTC and 2026-10-11 12:21 UTC.

[Full CSV](data/new-cves-2026-10-11T12-21-58-880303Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-10-11 12:16:52 | [CVE-2026-108573](https://nvd.nist.gov/vuln/detail/CVE-2026-108573) | Medium | 5.1 | A vulnerability was detected in Open Asset Import Library Assimp up to 6.0.5. Affected by this vulnerability is the fun… |
| 2026-10-11 12:16:52 | [CVE-2026-108574](https://nvd.nist.gov/vuln/detail/CVE-2026-108574) | Low | 2.1 | A flaw has been found in BerriAI LiteLLM up to 1.95.0. Affected by this issue is the function ui_view_session_spend_log… |
| 2026-10-11 12:16:53 | [CVE-2026-108575](https://nvd.nist.gov/vuln/detail/CVE-2026-108575) | Low | 2.1 | A vulnerability has been found in BerriAI LiteLLM up to 1.94.0. This affects the function get_secret of the file secret… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
