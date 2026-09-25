# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-09-25 04:19 UTC

New CVEs published between 2026-09-25 03:19 UTC and 2026-09-25 04:19 UTC.

[Full CSV](data/new-cves-2026-09-25T04-19-01-156753Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-09-25 04:17:31 | [CVE-2025-14814](https://nvd.nist.gov/vuln/detail/CVE-2025-14814) | Medium | 6.4 | The CSS & JavaScript Toolbox plugin for WordPress is vulnerable to Stored Cross-Site Scripting via the plugin's cjtoolb… |
| 2026-09-25 04:17:50 | [CVE-2026-97732](https://nvd.nist.gov/vuln/detail/CVE-2026-97732) | Medium | 5.1 | IRONMACE Ironshield 1.0.0.167 has a tvk.sys kernel-mode driver that authenticates client executables by checking for ex… |
| 2026-09-25 04:17:50 | [CVE-2026-97735](https://nvd.nist.gov/vuln/detail/CVE-2026-97735) | High | 8.0 | ITFlow before 26.08 allows SVG attachments in the ticket email parser (cron/ticket_email_parser.php) for email messages… |
| 2026-09-25 04:17:50 | [CVE-2026-97736](https://nvd.nist.gov/vuln/detail/CVE-2026-97736) | Medium | 5.4 | tinyauth before 5.1.3 allows rule bypass by appending an allowed route string. This is caused by an unanchored regular… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
