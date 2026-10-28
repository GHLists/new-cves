# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-28 12:20 UTC

New CVEs published between 2026-10-28 11:18 UTC and 2026-10-28 12:20 UTC.

[Full CSV](data/new-cves-2026-10-28T12-20-34-622052Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-10-28 12:17:39 | [CVE-2026-102790](https://nvd.nist.gov/vuln/detail/CVE-2026-102790) | High | 8.6 | Joomla Extension - icagenda.com - Stored XSS via url-type event Custom Field in iCagenda 3.2.1 to 4.0.16 |
| 2026-10-28 12:17:39 | [CVE-2026-102799](https://nvd.nist.gov/vuln/detail/CVE-2026-102799) | Medium | 5.3 | Joomla Extension - icagenda.com - CSV formula injection in the registrations export in iCagenda 3.5.0 to 4.0.16 |
| 2026-10-28 12:17:39 | [CVE-2026-114278](https://nvd.nist.gov/vuln/detail/CVE-2026-114278) | Critical | 9.8 | The che-machine-exec service constructs a shell command by concatenating user-controlled input (the username and namesp… |
| 2026-10-28 12:17:40 | [CVE-2026-116855](https://nvd.nist.gov/vuln/detail/CVE-2026-116855) | Medium | 5.4 | Missing Authorization vulnerability in wphocus My auctions allegro my-auctions-allegro-free-edition allows Exploiting I… |
| 2026-10-28 12:17:40 | [CVE-2026-118477](https://nvd.nist.gov/vuln/detail/CVE-2026-118477) | High | 8.7 | The ei_git_repo_url parameter in the Git remote configuration endpoint of KaliFast is vulnerable to OS Command Injectio… |
| 2026-10-28 12:17:40 | [CVE-2026-118485](https://nvd.nist.gov/vuln/detail/CVE-2026-118485) | High | 7.0 | Axel Download Accelerator 2.17.14 and earlier performs URL percent-decoding (http_decode()) on the output filename afte… |
| 2026-10-28 12:17:42 | [CVE-2026-81472](https://nvd.nist.gov/vuln/detail/CVE-2026-81472) | Medium | 4.2 | Dell iDRAC Service Module (iSM) for Windows, Dell iDRAC Service Module (iSM) for Linux, and Dell iDRAC Service Module (… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
