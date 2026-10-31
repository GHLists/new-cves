# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-31 15:19 UTC

New CVEs published between 2026-10-31 14:19 UTC and 2026-10-31 15:19 UTC.

[Full CSV](data/new-cves-2026-10-31T15-19-34-905187Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-10-31 15:16:53 | [CVE-2026-78188](https://nvd.nist.gov/vuln/detail/CVE-2026-78188) |  |  | WebDyne versions from 2.014 before 3.022 for Perl issue session cookies without the Secure, HttpOnly and SameSite attri… |
| 2026-10-31 15:16:54 | [CVE-2026-78189](https://nvd.nist.gov/vuln/detail/CVE-2026-78189) |  |  | WebDyne versions from 3.007 before 3.022 for Perl execute .psp files outside the document root via path traversal in th… |
| 2026-10-31 15:16:54 | [CVE-2026-78190](https://nvd.nist.gov/vuln/detail/CVE-2026-78190) |  |  | WebDyne versions from 2.014 before 3.022 for Perl reflect request parameters unescaped into form field values, allowing… |
| 2026-10-31 15:16:54 | [CVE-2026-78191](https://nvd.nist.gov/vuln/detail/CVE-2026-78191) |  |  | WebDyne versions from 2.031 before 3.022 for Perl execute files with .psp anywhere in the name as Perl pages. WebDyne d… |
| 2026-10-31 15:16:54 | [CVE-2026-78192](https://nvd.nist.gov/vuln/detail/CVE-2026-78192) |  |  | WebDyne versions from 2.022 before 3.022 for Perl disclose application source to unauthenticated clients via the viewer… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
