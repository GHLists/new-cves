# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-05 07:18 UTC

New CVEs published between 2026-10-05 06:19 UTC and 2026-10-05 07:18 UTC.

[Full CSV](data/new-cves-2026-10-05T07-18-39-868688Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-10-05 07:16:29 | [CVE-2017-20285](https://nvd.nist.gov/vuln/detail/CVE-2017-20285) |  |  | YAML versions before 1.30 for Perl allow a loaded document to trigger the DESTROY method of arbitrary classes. A perl/h… |
| 2026-10-05 07:16:29 | [CVE-2019-25777](https://nvd.nist.gov/vuln/detail/CVE-2019-25777) |  |  | YAML versions before 1.27_001 for Perl allow a loaded perl/glob document to replace any package variable, which can lea… |
| 2026-10-05 07:16:29 | [CVE-2026-100727](https://nvd.nist.gov/vuln/detail/CVE-2026-100727) | Medium | 6.9 | An improper access control vulnerability exists in GROWI, which allow an unauthenticated attacker to read files contain… |
| 2026-10-05 07:16:30 | [CVE-2026-105238](https://nvd.nist.gov/vuln/detail/CVE-2026-105238) | Medium | 5.5 | A flaw has been found in ChatGPTNextWeb NextChat up to 2.16.1. This vulnerability affects the function proxyHandler of… |
| 2026-10-05 07:16:30 | [CVE-2026-105245](https://nvd.nist.gov/vuln/detail/CVE-2026-105245) | Low | 2.9 | A vulnerability has been found in sgl-project sglang up to 0.5.21. This issue affects the function server_info of the f… |
| 2026-10-05 07:16:30 | [CVE-2026-105246](https://nvd.nist.gov/vuln/detail/CVE-2026-105246) | Medium | 5.5 | A vulnerability was found in SourceCodester Online Reviewer Management System 1.0. Impacted is an unknown function of t… |
| 2026-10-05 07:16:30 | [CVE-2026-19954](https://nvd.nist.gov/vuln/detail/CVE-2026-19954) |  |  | Net::Whois::Raw versions before 2.99044 for Perl ship a pwhois command-line tool that queries WHOIS for the wrong domai… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
