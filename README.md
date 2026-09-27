# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-09-27 12:19 UTC

New CVEs published between 2026-09-27 11:19 UTC and 2026-09-27 12:19 UTC.

[Full CSV](data/new-cves-2026-09-27T12-19-48-653493Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-09-27 12:17:10 | [CVE-2026-100747](https://nvd.nist.gov/vuln/detail/CVE-2026-100747) | Medium | 5.1 | Joomla Extension - svenbluege.de - CSRF in image upload in Event Gallery extension < 6.5.0 - Due to lack of an CSRF tok… |
| 2026-09-27 12:17:11 | [CVE-2026-100748](https://nvd.nist.gov/vuln/detail/CVE-2026-100748) | Medium | 6.9 | Joomla Extension - svenbluege.de - CSRF in various cart actions in Event Gallery extension < 6.5.0 |
| 2026-09-27 12:17:11 | [CVE-2026-100749](https://nvd.nist.gov/vuln/detail/CVE-2026-100749) | Medium | 5.1 | Joomla Extension - svenbluege.de - CSRF in backend cleanup actions in Event Gallery extension < 6.5.0 - Only orphaned f… |
| 2026-09-27 12:17:11 | [CVE-2026-97164](https://nvd.nist.gov/vuln/detail/CVE-2026-97164) | High | 7.0 | Joomla Extension - svenbluege.de - Authenticated arbitrary path deletion in `clear cache` task in Event Gallery extensi… |
| 2026-09-27 12:17:12 | [CVE-2026-97165](https://nvd.nist.gov/vuln/detail/CVE-2026-97165) | Medium | 5.3 | Joomla Extension - svenbluege.de - Reflected XSS and open redirect in Event Gallery extension < 6.5.0 - The “return” pa… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
