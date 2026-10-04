# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-04 18:18 UTC

New CVEs published between 2026-10-04 17:18 UTC and 2026-10-04 18:18 UTC.

[Full CSV](data/new-cves-2026-10-04T18-18-38-881829Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-10-04 18:16:33 | [CVE-2026-105161](https://nvd.nist.gov/vuln/detail/CVE-2026-105161) | Medium | 6.9 | A flaw has been found in invariant-systems-ai aiir up to 1.7.0. The affected element is an unknown function of the comp… |
| 2026-10-04 18:16:34 | [CVE-2026-105216](https://nvd.nist.gov/vuln/detail/CVE-2026-105216) | Critical | 9.1 | go-micro before 6.0.0 contains an improper certificate validation vulnerability that allows network attackers to impers… |
| 2026-10-04 18:16:34 | [CVE-2026-105217](https://nvd.nist.gov/vuln/detail/CVE-2026-105217) | Low | 2.3 | Cockpit CMS 2.12.0 before 2.14.1 disables TLS certificate verification in the cron.php web worker restart request, allo… |
| 2026-10-04 18:16:34 | [CVE-2026-105218](https://nvd.nist.gov/vuln/detail/CVE-2026-105218) | Critical | 9.1 | gopay before 1.5.119 disables TLS certificate verification in defaultClient() in pkg/xhttp/client.go, allowing man-in-t… |
| 2026-10-04 18:16:34 | [CVE-2026-105219](https://nvd.nist.gov/vuln/detail/CVE-2026-105219) | High | 8.7 | Mammoth.js 1.3.0 before 1.12.3 contains a regular expression denial of service vulnerability in the style map tokeniser… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
