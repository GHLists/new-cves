# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-11 22:18 UTC

New CVEs published between 2026-10-11 21:20 UTC and 2026-10-11 22:18 UTC.

[Full CSV](data/new-cves-2026-10-11T22-18-36-90842Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-10-11 22:16:50 | [CVE-2026-108769](https://nvd.nist.gov/vuln/detail/CVE-2026-108769) | Low | 2.1 | A security flaw has been discovered in zhayujie CowAgent up to 2.2.0. This affects an unknown part of the file Markdown… |
| 2026-10-11 22:16:50 | [CVE-2026-108978](https://nvd.nist.gov/vuln/detail/CVE-2026-108978) | Medium | 5.5 | Heap-based buffer overflow vulnerability in Samsung Opensource rlottie allows Buffer Overflow via Environment Variables… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
