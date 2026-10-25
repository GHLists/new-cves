# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-25 23:19 UTC

New CVEs published between 2026-10-25 22:18 UTC and 2026-10-25 23:19 UTC.

[Full CSV](data/new-cves-2026-10-25T23-19-25-637823Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-10-25 23:17:41 | [CVE-2026-116095](https://nvd.nist.gov/vuln/detail/CVE-2026-116095) | Medium | 5.5 | A vulnerability was identified in smg-project smg 1.7.0/1.8.0/1.9.0/1.10.0/1.10.1. Affected is the function jpeg_turbo:… |
| 2026-10-25 23:17:41 | [CVE-2026-116096](https://nvd.nist.gov/vuln/detail/CVE-2026-116096) | Low | 1.9 | A weakness has been identified in ggml-org llama.cpp. Affected by this issue is the function list_pockettts_state_slots… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
