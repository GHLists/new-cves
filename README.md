# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-11-12 16:20 UTC

New CVEs published between 2026-11-12 15:20 UTC and 2026-11-12 16:20 UTC.

[Full CSV](data/new-cves-2026-11-12T16-20-55-351125Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-11-12 16:19:04 | [CVE-2026-126329](https://nvd.nist.gov/vuln/detail/CVE-2026-126329) | High | 7.3 | Docker Sandboxes reuses existing state and configuration directories without verifying their ownership. If sbx or sandb… |
| 2026-11-12 16:19:04 | [CVE-2026-126330](https://nvd.nist.gov/vuln/detail/CVE-2026-126330) | Low | 2.4 | Docker Sandboxes can silently republish a sandbox service after an operator removes its automatically assigned host-por… |
| 2026-11-12 16:19:07 | [CVE-2026-127109](https://nvd.nist.gov/vuln/detail/CVE-2026-127109) |  |  | A code injection vulnerability in promzard’s template-loading functionality allows an attacker who can control property… |
| 2026-11-12 16:19:07 | [CVE-2026-127111](https://nvd.nist.gov/vuln/detail/CVE-2026-127111) | Critical | 9.1 | SOGo before 5.12.13 contains an improper restriction of excessive authentication attempts vulnerability that allows una… |
| 2026-11-12 16:19:07 | [CVE-2026-127121](https://nvd.nist.gov/vuln/detail/CVE-2026-127121) | High | 7.1 | SOGo before 5.12.13 contains an improper cryptographic signature verification vulnerability that allows remote attacker… |
| 2026-11-12 16:19:07 | [CVE-2026-127131](https://nvd.nist.gov/vuln/detail/CVE-2026-127131) | Critical | 9.1 | SOGo before 5.12.13 contains a missing rate limiting vulnerability in its web login TOTP verification that allows attac… |
| 2026-11-12 16:19:08 | [CVE-2026-127135](https://nvd.nist.gov/vuln/detail/CVE-2026-127135) | Medium | 5.3 | SOGo before 5.12.13 contains a Sieve script injection vulnerability that allows authenticated users to inject arbitrary… |
| 2026-11-12 16:19:08 | [CVE-2026-127141](https://nvd.nist.gov/vuln/detail/CVE-2026-127141) | High | 7.1 | SOGo before 5.12.13 contains a denial of service vulnerability that allows authenticated attackers to exhaust all worke… |
| 2026-11-12 16:19:08 | [CVE-2026-127145](https://nvd.nist.gov/vuln/detail/CVE-2026-127145) | Medium | 5.3 | SOGo before 5.12.13 contains a server-side request forgery vulnerability that allows authenticated users to make the se… |
| 2026-11-12 16:19:08 | [CVE-2026-19809](https://nvd.nist.gov/vuln/detail/CVE-2026-19809) | Low | 3.3 | The user-mode system call verifier z_vrfy_charger_get_prop() in drivers/charger/charger_handlers.c declares an uninitia… |
| 2026-11-12 16:19:12 | [CVE-2026-70641](https://nvd.nist.gov/vuln/detail/CVE-2026-70641) |  |  | Rejected reason: This CVE ID has been rejected or withdrawn by its CVE Numbering Authority as a duplicate of CVE-2026-8… |
| 2026-11-12 16:19:13 | [CVE-2026-70642](https://nvd.nist.gov/vuln/detail/CVE-2026-70642) | Medium | 5.3 | ToolJet before 3.21.94, fixed in commit e5f387a, contains an authorization bypass vulnerability in the app environments… |
| 2026-11-12 16:19:21 | [CVE-2026-91007](https://nvd.nist.gov/vuln/detail/CVE-2026-91007) | High | 7.8 | The user-mode syscall verifiers for the charger driver API in drivers/charger/charger_handlers.c did not inspect the pr… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
