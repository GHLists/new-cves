# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-14 05:19 UTC

New CVEs published between 2026-10-14 04:20 UTC and 2026-10-14 05:19 UTC.

[Full CSV](data/new-cves-2026-10-14T05-19-48-256416Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-10-14 05:16:41 | [CVE-2026-101924](https://nvd.nist.gov/vuln/detail/CVE-2026-101924) | High | 7.2 | The NewStatPress plugin for WordPress is vulnerable to Stored Cross-Site Scripting in versions up to, and including, 1.… |
| 2026-10-14 05:16:42 | [CVE-2026-101926](https://nvd.nist.gov/vuln/detail/CVE-2026-101926) | Medium | 6.5 | The Hyyan WooCommerce Polylang Integration plugin for WordPress is vulnerable to SQL Injection via the 'variation_ids'… |
| 2026-10-14 05:16:42 | [CVE-2026-103369](https://nvd.nist.gov/vuln/detail/CVE-2026-103369) | Medium | 6.4 | The Social Share Buttons & Analytics Plugin – GetSocial.io plugin for WordPress is vulnerable to Stored Cross-Site Scri… |
| 2026-10-14 05:16:42 | [CVE-2026-105429](https://nvd.nist.gov/vuln/detail/CVE-2026-105429) | High | 8.9 | Improper neutralization of special elements in the NetBird client SSH configuration manager (client/ssh/config/manager.… |
| 2026-10-14 05:16:42 | [CVE-2026-106931](https://nvd.nist.gov/vuln/detail/CVE-2026-106931) | High | 8.5 | SiteGuard Server Edition contains an OS command injection vulnerability, which may allow an attacker to execute arbitra… |
| 2026-10-14 05:16:42 | [CVE-2026-110450](https://nvd.nist.gov/vuln/detail/CVE-2026-110450) | High | 8.0 | Nix before 2.35.3 and Lix before 2.95.4 allow privilege escalation via a repair operation because it could destroy and… |
| 2026-10-14 05:16:43 | [CVE-2026-110451](https://nvd.nist.gov/vuln/detail/CVE-2026-110451) | Medium | 4.3 | Nix before 2.35.3 and Lix before 2.95.4 on macOS allow a Seatbelt sandbox escape (for an unconfined build) because a ce… |
| 2026-10-14 05:16:43 | [CVE-2026-110452](https://nvd.nist.gov/vuln/detail/CVE-2026-110452) | Medium | 4.0 | The multi-user installer in Nix before 2.35.3 sets the ownership of store contents to the user (who invoked the install… |
| 2026-10-14 05:16:43 | [CVE-2026-110453](https://nvd.nist.gov/vuln/detail/CVE-2026-110453) | Medium | 4.3 | Nix before 2.35.3, when unsandboxed on macOS or FreeBSD, incorrectly allows connections made by build users from daemon… |
| 2026-10-14 05:16:43 | [CVE-2026-110454](https://nvd.nist.gov/vuln/detail/CVE-2026-110454) | Medium | 5.3 | A malicious actor with access to the network could exploit an Improper Access Control vulnerability found in UniFi Prot… |
| 2026-10-14 05:16:43 | [CVE-2026-110455](https://nvd.nist.gov/vuln/detail/CVE-2026-110455) | High | 8.1 | A malicious actor with access to the network and under certain conditions could exploit an Improper Input Validation vu… |
| 2026-10-14 05:16:43 | [CVE-2026-110456](https://nvd.nist.gov/vuln/detail/CVE-2026-110456) | Medium | 5.3 | A malicious actor with access to the network and under certain conditions could exploit an Improper Access Control vuln… |
| 2026-10-14 05:16:44 | [CVE-2026-46449](https://nvd.nist.gov/vuln/detail/CVE-2026-46449) | Medium | 6.7 | The Akamai Guardicore Platform Agent (GPA) before 7.4 for macOS is affected by a local privilege escalation vulnerabili… |
| 2026-10-14 05:16:44 | [CVE-2026-50215](https://nvd.nist.gov/vuln/detail/CVE-2026-50215) |  |  | A use-after-free exists in the Windows WFP packet-capture driver shipped with Akamai Guardicore Platform Agent (GPA) be… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
