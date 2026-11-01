# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-11-01 07:18 UTC

New CVEs published between 2026-11-01 06:19 UTC and 2026-11-01 07:18 UTC.

[Full CSV](data/new-cves-2026-11-01T07-18-08-606012Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-11-01 07:17:14 | [CVE-2026-120217](https://nvd.nist.gov/vuln/detail/CVE-2026-120217) | Low | 2.1 | A vulnerability was detected in Delgan loguru 0.7.3. The affected element is the function AnsiParser.feed of the file l… |
| 2026-11-01 07:17:26 | [CVE-2026-120218](https://nvd.nist.gov/vuln/detail/CVE-2026-120218) | Low | 2.0 | A flaw has been found in Typemill up to 2.26.0. The impacted element is the function ControllerApiImage::saveImage of t… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
