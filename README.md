# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-11-24 07:18 UTC

New CVEs published between 2026-11-24 06:19 UTC and 2026-11-24 07:18 UTC.

[Full CSV](data/new-cves-2026-11-24T07-18-38-816571Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-11-24 07:17:19 | [CVE-2026-120932](https://nvd.nist.gov/vuln/detail/CVE-2026-120932) | Medium | 5.1 | A format string vulnerability has been reported in the Internal Backup of ADM. User-controlled input from the source_fo… |
| 2026-11-24 07:17:19 | [CVE-2026-120951](https://nvd.nist.gov/vuln/detail/CVE-2026-120951) | High | 8.6 | An externally-controlled format string vulnerability exists in the authenticated upload_wireguard action of settings/vp… |
| 2026-11-24 07:17:19 | [CVE-2026-134893](https://nvd.nist.gov/vuln/detail/CVE-2026-134893) | Medium | 5.1 | An externally controlled format string vulnerability in the Snapshot CGI components of ADM allows an authenticated admi… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
