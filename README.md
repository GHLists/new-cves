# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-25 17:18 UTC

New CVEs published between 2026-10-25 16:18 UTC and 2026-10-25 17:18 UTC.

[Full CSV](data/new-cves-2026-10-25T17-18-41-62114Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-10-25 17:17:00 | [CVE-2026-115817](https://nvd.nist.gov/vuln/detail/CVE-2026-115817) |  |  | Starman versions before 0.4019 for Perl allow a stalled request body to hold a worker indefinitely, as read_timeout cov… |
| 2026-10-25 17:17:01 | [CVE-2026-115822](https://nvd.nist.gov/vuln/detail/CVE-2026-115822) |  |  | Starman versions before 0.4019 for Perl allow CPU exhaustion via quadratic regex backtracking when parsing chunked requ… |
| 2026-10-25 17:17:01 | [CVE-2026-115823](https://nvd.nist.gov/vuln/detail/CVE-2026-115823) |  |  | Starman versions before 0.4019 for Perl send response bodies for HEAD requests, desynchronizing responses on keep-alive… |
| 2026-10-25 17:17:01 | [CVE-2026-115824](https://nvd.nist.gov/vuln/detail/CVE-2026-115824) |  |  | Starman versions before 0.4019 for Perl allow memory exhaustion via unbounded buffering of chunked request bodies. The… |
| 2026-10-25 17:17:01 | [CVE-2026-115825](https://nvd.nist.gov/vuln/detail/CVE-2026-115825) |  |  | HTTP::Server::PSGI versions before 1.0056 for Perl allow a single request to crash the server by declaring a large Cont… |
| 2026-10-25 17:17:02 | [CVE-2026-116060](https://nvd.nist.gov/vuln/detail/CVE-2026-116060) | Medium | 5.5 | A vulnerability was determined in SourceCodester Performance Indicator System 1.0. This affects an unknown part of the… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
