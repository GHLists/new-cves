# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-11-23 05:18 UTC

New CVEs published between 2026-11-23 04:20 UTC and 2026-11-23 05:18 UTC.

[Full CSV](data/new-cves-2026-11-23T05-18-41-234162Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-11-23 05:17:44 | [CVE-2026-134854](https://nvd.nist.gov/vuln/detail/CVE-2026-134854) | Medium | 5.5 | A vulnerability was found in andreasgal node-wav up to 0.0.2. Impacted is the function decode of the file index.js of t… |
| 2026-11-23 05:17:45 | [CVE-2026-134855](https://nvd.nist.gov/vuln/detail/CVE-2026-134855) | Medium | 5.5 | A vulnerability was determined in kchapelier qoijs 1.0.0. The affected element is the function decode of the file src/d… |
| 2026-11-23 05:17:49 | [CVE-2026-134856](https://nvd.nist.gov/vuln/detail/CVE-2026-134856) | Low | 1.9 | A vulnerability was identified in Snes9x up to 1.63. The impacted element is the function S9xUnfreezeFromStream of the… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
