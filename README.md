# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-11-26 09:18 UTC

New CVEs published between 2026-11-26 08:19 UTC and 2026-11-26 09:18 UTC.

[Full CSV](data/new-cves-2026-11-26T09-18-45-644077Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-11-26 09:17:08 | [CVE-2026-131916](https://nvd.nist.gov/vuln/detail/CVE-2026-131916) | Medium | 5.1 | GENAI Web provided by Digital Agency contains a server-side request forgery (SSRF) vulnerability. An attacker may be ab… |
| 2026-11-26 09:17:09 | [CVE-2026-133339](https://nvd.nist.gov/vuln/detail/CVE-2026-133339) | High | 8.6 | Joomla Extension - vi-solutions - SQL injection via form IDs in administrative form export in Visforms extension 1.0.0-… |
| 2026-11-26 09:17:09 | [CVE-2026-133340](https://nvd.nist.gov/vuln/detail/CVE-2026-133340) | Medium | 5.1 | Joomla Extension - vi-solutions - Missing data export permission check in administrative form export in Visforms extens… |
| 2026-11-26 09:17:09 | [CVE-2026-133341](https://nvd.nist.gov/vuln/detail/CVE-2026-133341) | Medium | 6.9 | Joomla Extension - vi-solutions - Missing SQL statement permission check in Maxsubmissions plugin in Visforms extension… |
| 2026-11-26 09:17:09 | [CVE-2026-136638](https://nvd.nist.gov/vuln/detail/CVE-2026-136638) | Medium | 5.9 | Pydantic AI Harness's PlaywrightBrowser applies an egress policy to the requests a page makes. It treated any URL conta… |
| 2026-11-26 09:17:09 | [CVE-2026-137324](https://nvd.nist.gov/vuln/detail/CVE-2026-137324) | Medium | 5.5 | A flaw has been found in shemaikuzwe Attendance_Management_system up to b37dbeb5bf4d9eab07480e7b6213db889fc3ebf9. Affec… |
| 2026-11-26 09:17:09 | [CVE-2026-137389](https://nvd.nist.gov/vuln/detail/CVE-2026-137389) | High | 8.7 | MailGates/MailAudit developed by Openfind has a Command Injection vulnerability.Authenticated remote attackers can inje… |
| 2026-11-26 09:17:10 | [CVE-2026-137390](https://nvd.nist.gov/vuln/detail/CVE-2026-137390) | High | 8.7 | Mail2000 developed by Openfind has an OS Command Injection vulnerability.Authenticated remote attackers can inject arbi… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
