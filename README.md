# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-09-26 15:18 UTC

New CVEs published between 2026-09-26 14:18 UTC and 2026-09-26 15:18 UTC.

[Full CSV](data/new-cves-2026-09-26T15-18-56-141562Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-09-26 15:16:54 | [CVE-2026-94131](https://nvd.nist.gov/vuln/detail/CVE-2026-94131) | High | 8.3 | Joomla Extension - acymailing.com - Unauthenticated arbitrary file deletion in AcyMailing Enterprise extension < 11.1.0… |
| 2026-09-26 15:16:55 | [CVE-2026-94132](https://nvd.nist.gov/vuln/detail/CVE-2026-94132) | Critical | 9.5 | Joomla Extension - acymailing.com - Remote Code Execution vulnerability in mailbox action feature in AcyMailing Enterpr… |
| 2026-09-26 15:16:55 | [CVE-2026-97160](https://nvd.nist.gov/vuln/detail/CVE-2026-97160) | Critical | 9.4 | Joomla Extension - lomart.fr - Authenticated, privileged PHP command injection in UP plugin extension 5.0.0-5.2.0, 6.0.… |
| 2026-09-26 15:16:55 | [CVE-2026-97161](https://nvd.nist.gov/vuln/detail/CVE-2026-97161) | Critical | 9.2 | Joomla Extension - lomart.fr - Various path traversal / file access vectors in UP plugin extension 5.0.0-5.2.0, 6.0.0-6… |
| 2026-09-26 15:16:55 | [CVE-2026-97162](https://nvd.nist.gov/vuln/detail/CVE-2026-97162) | High | 8.3 | Joomla Extension - lomart.fr - Various SQL injection vectors in UP plugin extension 5.0.0-5.2.0, 6.0.0-6.0.29 |
| 2026-09-26 15:16:55 | [CVE-2026-97163](https://nvd.nist.gov/vuln/detail/CVE-2026-97163) | Critical | 10.0 | Joomla Extension - lomart.fr - Unauthenticated remote code installation in UP plugin extension 5.0.0-5.2.0, 6.0.0-6.0.29 |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
