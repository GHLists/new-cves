# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-11-21 11:21 UTC

New CVEs published between 2026-11-21 10:21 UTC and 2026-11-21 11:21 UTC.

[Full CSV](data/new-cves-2026-11-21T11-21-13-006013Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-11-21 11:16:37 | [CVE-2022-4998](https://nvd.nist.gov/vuln/detail/CVE-2022-4998) | Low | 2.1 | A vulnerability was identified in kanishka-linux reminiscence 0.3 on Windows. This issue affects the function convert_h… |
| 2026-11-21 11:16:38 | [CVE-2026-128361](https://nvd.nist.gov/vuln/detail/CVE-2026-128361) | High | 8.2 | Improper Input Validation vulnerability in phoenixframework phoenix (Phoenix.Presence) allows an attacker who can join… |
| 2026-11-21 11:16:39 | [CVE-2026-129344](https://nvd.nist.gov/vuln/detail/CVE-2026-129344) | High | 8.2 | Uncaught Exception vulnerability in phoenixframework phoenix allows an unauthenticated attacker to cause a denial of se… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
