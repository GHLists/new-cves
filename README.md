# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-11-11 10:20 UTC

New CVEs published between 2026-11-11 09:21 UTC and 2026-11-11 10:20 UTC.

[Full CSV](data/new-cves-2026-11-11T10-20-27-114546Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-11-11 10:16:42 | [CVE-2026-112174](https://nvd.nist.gov/vuln/detail/CVE-2026-112174) | Critical | 9.3 | Local privilege escalation vulnerability in Iperius Backup 8.8.3, due to insufficient separation between the graphical… |
| 2026-11-11 10:16:43 | [CVE-2026-124250](https://nvd.nist.gov/vuln/detail/CVE-2026-124250) | High | 7.1 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in AyeCode Ltd GeoDi… |
| 2026-11-11 10:16:43 | [CVE-2026-124256](https://nvd.nist.gov/vuln/detail/CVE-2026-124256) | Medium | 6.5 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in CodeRockz Deliver… |
| 2026-11-11 10:16:43 | [CVE-2026-124257](https://nvd.nist.gov/vuln/detail/CVE-2026-124257) | Medium | 6.5 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in wordplus BP Bette… |
| 2026-11-11 10:16:43 | [CVE-2026-124737](https://nvd.nist.gov/vuln/detail/CVE-2026-124737) | High | 7.5 | A flaw was found in BusyBox. When the TFTP (Trivial File Transfer Protocol) client requests a custom small block size a… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
