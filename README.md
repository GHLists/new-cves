# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-29 00:20 UTC

New CVEs published between 2026-10-28 23:19 UTC and 2026-10-29 00:20 UTC.

[Full CSV](data/new-cves-2026-10-29T00-20-22-623889Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-10-29 00:17:25 | [CVE-2026-118585](https://nvd.nist.gov/vuln/detail/CVE-2026-118585) | Low | 2.0 | A vulnerability was identified in configuroweb inventariobasico c9377cdba474deb3eb5a0704d197b5733af16b47/f9db0c0a04d79a… |
| 2026-10-29 00:17:26 | [CVE-2026-118586](https://nvd.nist.gov/vuln/detail/CVE-2026-118586) | Medium | 6.9 | A security flaw has been discovered in dfm feedfinder2 up to 0.0.4. This issue affects the function find_feeds of the f… |
| 2026-10-29 00:17:26 | [CVE-2026-118589](https://nvd.nist.gov/vuln/detail/CVE-2026-118589) | Medium | 6.9 | A weakness has been identified in nschloe meshio up to 5.3.5. Impacted is an unknown function of the file meshio/_vtk_4… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
