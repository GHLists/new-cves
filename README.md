# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-11-12 01:18 UTC

New CVEs published between 2026-11-12 00:19 UTC and 2026-11-12 01:18 UTC.

[Full CSV](data/new-cves-2026-11-12T01-18-42-765099Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-11-12 01:17:11 | [CVE-2026-125785](https://nvd.nist.gov/vuln/detail/CVE-2026-125785) | Medium | 6.5 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in Crocoblock JetEng… |
| 2026-11-12 01:17:11 | [CVE-2026-125786](https://nvd.nist.gov/vuln/detail/CVE-2026-125786) | Medium | 5.3 | Improper Neutralization of Script-Related HTML Tags in a Web Page (Basic XSS) vulnerability in ExpressTech Quiz And Sur… |
| 2026-11-12 01:17:11 | [CVE-2026-125787](https://nvd.nist.gov/vuln/detail/CVE-2026-125787) | Medium | 5.4 | Missing Authorization vulnerability in ExpressTech Quiz And Survey Master quiz-master-next allows Exploiting Incorrectl… |
| 2026-11-12 01:17:11 | [CVE-2026-126673](https://nvd.nist.gov/vuln/detail/CVE-2026-126673) |  |  | Data::Dump::Streamer versions before 3.00 for Perl allow code injection via unescaped Regexp patterns in _dump_qr. A Re… |
| 2026-11-12 01:17:11 | [CVE-2026-126785](https://nvd.nist.gov/vuln/detail/CVE-2026-126785) | Critical | 9.3 | A vulnerability has been found in rmalright TR-VISION HOME 2.0.5. Impacted is the function sub_11504 in the library WFa… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
