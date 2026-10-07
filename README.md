# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-07 18:19 UTC

New CVEs published between 2026-10-07 17:18 UTC and 2026-10-07 18:19 UTC.

[Full CSV](data/new-cves-2026-10-07T18-19-59-277272Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-10-07 18:17:16 | [CVE-2026-106066](https://nvd.nist.gov/vuln/detail/CVE-2026-106066) | Medium | 6.3 | A heap-based buffer overflow was found in GIMP’s raw data export plug-in. When exporting very large images, g_malloc()… |
| 2026-10-07 18:17:16 | [CVE-2026-106067](https://nvd.nist.gov/vuln/detail/CVE-2026-106067) | Medium | 6.3 | A heap-based buffer overflow was found in GIMP’s Hot color filter plug-in. For very large images, a pixel buffer is all… |
| 2026-10-07 18:17:18 | [CVE-2026-107211](https://nvd.nist.gov/vuln/detail/CVE-2026-107211) | High | 8.7 | Excelize is a Go language library for reading and writing Microsoft Excel spreadsheets. From 2.8.1 to 2.11.0, separatel… |
| 2026-10-07 18:17:18 | [CVE-2026-107212](https://nvd.nist.gov/vuln/detail/CVE-2026-107212) | High | 7.5 | Excelize is a Go language library for reading and writing Microsoft Excel spreadsheets. From 2.1.0 to 2.11.0, Rows.Colu… |
| 2026-10-07 18:17:18 | [CVE-2026-107213](https://nvd.nist.gov/vuln/detail/CVE-2026-107213) | High | 8.7 | Excelize is a Go language library for reading and writing Microsoft Excel spreadsheets. From 2.9.0 to 2.11.0, GetSlicer… |
| 2026-10-07 18:17:19 | [CVE-2026-107214](https://nvd.nist.gov/vuln/detail/CVE-2026-107214) | High | 7.5 | Excelize is a Go language library for reading and writing Microsoft Excel spreadsheets. From 2.3.1 to 2.11.0, the decry… |
| 2026-10-07 18:17:19 | [CVE-2026-107215](https://nvd.nist.gov/vuln/detail/CVE-2026-107215) | High | 7.5 | Excelize is a Go language library for reading and writing Microsoft Excel spreadsheets. From 2.3.1 to 2.11.0, extractPa… |
| 2026-10-07 18:17:19 | [CVE-2026-107216](https://nvd.nist.gov/vuln/detail/CVE-2026-107216) | High | 7.5 | Excelize is a Go language library for reading and writing Microsoft Excel spreadsheets. From 2.8.1 to 2.11.0, ANCHORARR… |
| 2026-10-07 18:17:20 | [CVE-2026-56851](https://nvd.nist.gov/vuln/detail/CVE-2026-56851) |  |  | The Nickname profile can panic with an out-of-bounds slice error when transforming crafted input into a short destinati… |
| 2026-10-07 18:17:32 | [CVE-2026-96335](https://nvd.nist.gov/vuln/detail/CVE-2026-96335) | High | 7.5 | Missing Authorization vulnerability in WPMU DEV Forminator allows Exploiting Incorrectly Configured Access Control Secu… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
