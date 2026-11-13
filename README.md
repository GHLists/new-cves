# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-11-13 11:18 UTC

New CVEs published between 2026-11-13 10:18 UTC and 2026-11-13 11:18 UTC.

[Full CSV](data/new-cves-2026-11-13T11-18-45-151219Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-11-13 11:17:14 | [CVE-2026-109903](https://nvd.nist.gov/vuln/detail/CVE-2026-109903) | High | 7.8 | A buffer overread caused by casting a negative integer to CARD32 in XvQueryImageAttributes in X.Org X Server before 21.… |
| 2026-11-13 11:17:15 | [CVE-2026-109904](https://nvd.nist.gov/vuln/detail/CVE-2026-109904) | Medium | 6.9 | A buffer overread caused by an integer-overflow in Proc/SProcXResQueryClientIds in X.Org xwayland before 24.1.15 and X… |
| 2026-11-13 11:17:15 | [CVE-2026-112182](https://nvd.nist.gov/vuln/detail/CVE-2026-112182) | High | 8.7 | Unauthorization vulnerability in the management of workflow definitions in OpenKM Community Edition. The REST endpoints… |
| 2026-11-13 11:17:16 | [CVE-2026-123274](https://nvd.nist.gov/vuln/detail/CVE-2026-123274) |  |  | Out-of-bounds Write vulnerability in Apache DataSketches C++. An application that deserializes a KLL sketch from an unt… |
| 2026-11-13 11:17:16 | [CVE-2026-123338](https://nvd.nist.gov/vuln/detail/CVE-2026-123338) |  |  | Out-of-bounds Write vulnerability in Apache DataSketches C++. An application that deserializes a REQ sketch from an unt… |
| 2026-11-13 11:17:16 | [CVE-2026-125659](https://nvd.nist.gov/vuln/detail/CVE-2026-125659) | Low | 2.1 | This vulnerability exists in the eMudhra emBridge due to missing authorization checks in the FileBrowser API endpoints.… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
