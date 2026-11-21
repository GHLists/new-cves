# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-11-21 23:19 UTC

New CVEs published between 2026-11-21 22:18 UTC and 2026-11-21 23:19 UTC.

[Full CSV](data/new-cves-2026-11-21T23-19-11-803008Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-11-21 23:16:54 | [CVE-2026-115589](https://nvd.nist.gov/vuln/detail/CVE-2026-115589) |  |  | Rejected reason: This CVE ID has been rejected or withdrawn by its CVE Numbering Authority. |
| 2026-11-21 23:16:54 | [CVE-2026-134534](https://nvd.nist.gov/vuln/detail/CVE-2026-134534) | Medium | 5.1 | A security flaw has been discovered in Skyvern-AI Skyvern 1.0.56. The affected element is the function classify_url of… |
| 2026-11-21 23:16:54 | [CVE-2026-134536](https://nvd.nist.gov/vuln/detail/CVE-2026-134536) | Medium | 5.3 | A weakness has been identified in Drakeling Labs Operation Harsh Doorstop up to 0.14.2.1 Build 19523588. The impacted e… |
| 2026-11-21 23:16:55 | [CVE-2026-134540](https://nvd.nist.gov/vuln/detail/CVE-2026-134540) | Medium | 5.5 | A security vulnerability has been detected in ggml-org llama.cpp 0.7.0-dev. This affects the function common_sampler_in… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
