# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-05 12:19 UTC

New CVEs published between 2026-10-05 11:18 UTC and 2026-10-05 12:19 UTC.

[Full CSV](data/new-cves-2026-10-05T12-19-45-515176Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-10-05 12:17:07 | [CVE-2026-103684](https://nvd.nist.gov/vuln/detail/CVE-2026-103684) | Medium | 5.3 | Missing Authorization vulnerability in Arraytics WP Event Solution wp-event-solution allows Exploiting Incorrectly Conf… |
| 2026-10-05 12:17:09 | [CVE-2026-105073](https://nvd.nist.gov/vuln/detail/CVE-2026-105073) | Medium | 5.3 | Exposure of Sensitive System Information to an Unauthorized Control Sphere vulnerability in Arraytics WP Event Solution… |
| 2026-10-05 12:17:09 | [CVE-2026-105307](https://nvd.nist.gov/vuln/detail/CVE-2026-105307) | Medium | 5.5 | A vulnerability was detected in Casdoor up to 3.161.1. Affected is the function ApiFilter of the file routers/authz_fil… |
| 2026-10-05 12:17:09 | [CVE-2026-105396](https://nvd.nist.gov/vuln/detail/CVE-2026-105396) | Medium | 5.3 | Heym before v0.0.112 contains a token leakage vulnerability in build_public_base_url() that allows unauthenticated atta… |
| 2026-10-05 12:17:09 | [CVE-2026-39783](https://nvd.nist.gov/vuln/detail/CVE-2026-39783) | Medium | 4.3 | Missing Authorization vulnerability in WP SYNTEX Polylang polylang allows Retrieve Embedded Sensitive Data.This issue a… |
| 2026-10-05 12:17:10 | [CVE-2026-63266](https://nvd.nist.gov/vuln/detail/CVE-2026-63266) | Medium | 6.8 | LibreOffice Calc can link a cell range to an external data source, and the link is saved in the document. Through such… |
| 2026-10-05 12:17:10 | [CVE-2026-63267](https://nvd.nist.gov/vuln/detail/CVE-2026-63267) | Medium | 6.7 | LibreOffice Calc can link a cell range to an external csv data source, and the link is saved in the document. Such a li… |
| 2026-10-05 12:17:10 | [CVE-2026-63268](https://nvd.nist.gov/vuln/detail/CVE-2026-63268) | Medium | 6.7 | LibreOffice Calc can link a cell range to an external data source, and the link is saved in the document. A link of the… |
| 2026-10-05 12:17:10 | [CVE-2026-63269](https://nvd.nist.gov/vuln/detail/CVE-2026-63269) | Medium | 6.7 | LibreOffice can link to audio and video files from a document, and on Linux it plays them with GStreamer. A linked medi… |
| 2026-10-05 12:17:11 | [CVE-2026-63270](https://nvd.nist.gov/vuln/detail/CVE-2026-63270) | Medium | 6.7 | URLs could be constructed which expanded environment variable or INI file values, so potentially sensitive information… |
| 2026-10-05 12:17:11 | [CVE-2026-63277](https://nvd.nist.gov/vuln/detail/CVE-2026-63277) | High | 8.5 | LibreOffice Calc can link a cell range to an external data source, and the link is saved in the document. A document co… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
