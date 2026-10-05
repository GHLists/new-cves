# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-05 13:18 UTC

New CVEs published between 2026-10-05 12:19 UTC and 2026-10-05 13:18 UTC.

[Full CSV](data/new-cves-2026-10-05T13-18-59-326908Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-10-05 13:16:52 | [CVE-2026-105315](https://nvd.nist.gov/vuln/detail/CVE-2026-105315) | Low | 2.0 | A vulnerability has been found in django-haystack up to 3.3.0. Affected is the function _to_python of the file haystack… |
| 2026-10-05 13:16:54 | [CVE-2026-77802](https://nvd.nist.gov/vuln/detail/CVE-2026-77802) | Medium | 6.3 | In Progress® Telerik® Fiddler® Classic for Windows, versions prior to v6.0.20262.10021, HTTP request smuggling is possi… |
| 2026-10-05 13:16:54 | [CVE-2026-77803](https://nvd.nist.gov/vuln/detail/CVE-2026-77803) | Low | 3.6 | In Progress® Telerik® Fiddler® Classic for Windows, versions prior to v6.0.20262.10021, front-end request desynchroniza… |
| 2026-10-05 13:16:54 | [CVE-2026-77804](https://nvd.nist.gov/vuln/detail/CVE-2026-77804) | Medium | 6.6 | In Progress® Telerik® Fiddler® Classic for Windows, versions prior to v6.0.20262.10021, a time-of-check time-of-use (TO… |
| 2026-10-05 13:16:54 | [CVE-2026-77805](https://nvd.nist.gov/vuln/detail/CVE-2026-77805) | High | 7.9 | In Progress® Telerik® Fiddler® Classic for Windows, versions prior to v6.0.20262.10021, the integrity check applied to… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
