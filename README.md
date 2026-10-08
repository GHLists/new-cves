# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-08 05:18 UTC

New CVEs published between 2026-10-08 04:18 UTC and 2026-10-08 05:18 UTC.

[Full CSV](data/new-cves-2026-10-08T05-18-33-472137Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-10-08 05:17:03 | [CVE-2023-5648](https://nvd.nist.gov/vuln/detail/CVE-2023-5648) | Medium | 6.5 | In Brocade ASCG before Brocade ASCG v3.0, several security-related HTTP Headers were missing in various Brocade ASCG UR… |
| 2026-10-08 05:17:03 | [CVE-2023-5649](https://nvd.nist.gov/vuln/detail/CVE-2023-5649) | Medium | 6.8 | An Improper Input Validation vulnerability for the registered case credentials in Brocade ASCG before v3.0 could allow… |
| 2026-10-08 05:17:04 | [CVE-2026-107449](https://nvd.nist.gov/vuln/detail/CVE-2026-107449) | Low | 3.4 | linuxserver Heimdall through 2.8.3 applies its SafeUrlFetcher SSRF protection mechanism only to ItemController; the enh… |
| 2026-10-08 05:17:04 | [CVE-2026-107450](https://nvd.nist.gov/vuln/detail/CVE-2026-107450) | High | 8.1 | In Stump through 0.1.10, the updateSmartList and deleteSmartList GraphQL mutations (crates/graphql/src/mutation/smart_l… |
| 2026-10-08 05:17:04 | [CVE-2026-17196](https://nvd.nist.gov/vuln/detail/CVE-2026-17196) | High | 8.8 | The Super Forms – Drag & Drop Form Builder plugin for WordPress is vulnerable to Unrestricted File Type Upload in all v… |
| 2026-10-08 05:17:04 | [CVE-2026-17609](https://nvd.nist.gov/vuln/detail/CVE-2026-17609) | Critical | 9.1 | The Super Forms – Drag & Drop Form Builder plugin for WordPress is vulnerable to Arbitrary Directory Deletion in all ve… |
| 2026-10-08 05:17:05 | [CVE-2026-87661](https://nvd.nist.gov/vuln/detail/CVE-2026-87661) | Medium | 6.8 | Brocade Fabric OS versions before 9.2.2d and 10.0.0 through 10.0.0a1 directly accepts Apache configuration file data du… |
| 2026-10-08 05:17:05 | [CVE-2026-87662](https://nvd.nist.gov/vuln/detail/CVE-2026-87662) | High | 7.0 | Brocade Fabric versions before 9.2.2d and 10.0.0 through 10.0.0a1 handling of specific download protocols utilizes unsa… |
| 2026-10-08 05:17:05 | [CVE-2026-87663](https://nvd.nist.gov/vuln/detail/CVE-2026-87663) | High | 7.1 | An authentication bypass and command injection vulnerability exists in the inter-switch remote execution service of Bro… |
| 2026-10-08 05:17:05 | [CVE-2026-87664](https://nvd.nist.gov/vuln/detail/CVE-2026-87664) | High | 8.5 | A session context forgery vulnerability exists in the web management daemon of Brocade Fabric OS versions 9.2.2d and 10… |
| 2026-10-08 05:17:05 | [CVE-2026-87677](https://nvd.nist.gov/vuln/detail/CVE-2026-87677) | Medium | 5.4 | An OS command injection vulnerability exists in the account management subsystem of Brocade Fabric OS versions before 9… |
| 2026-10-08 05:17:05 | [CVE-2026-94576](https://nvd.nist.gov/vuln/detail/CVE-2026-94576) | Medium | 5.9 | An authentication logic and privilege escalation vulnerability exists in the account management interface of Brocade Fa… |
| 2026-10-08 05:17:06 | [CVE-2026-94577](https://nvd.nist.gov/vuln/detail/CVE-2026-94577) | High | 7.3 | A privilege escalation vulnerability exists in the internal Command-Line Interface (CLI) authorization handling mechani… |
| 2026-10-08 05:17:06 | [CVE-2026-94579](https://nvd.nist.gov/vuln/detail/CVE-2026-94579) | Medium | 5.4 | An OS command injection vulnerability exists in the PAM (Pluggable Authentication Module) session cleanup routines duri… |
| 2026-10-08 05:17:06 | [CVE-2026-94581](https://nvd.nist.gov/vuln/detail/CVE-2026-94581) | High | 8.5 | An OS command injection vulnerability exists in the REST API management interface of Brocade Fabric OS versions before… |
| 2026-10-08 05:17:06 | [CVE-2026-94585](https://nvd.nist.gov/vuln/detail/CVE-2026-94585) | High | 7.7 | An authentication bypass vulnerability exists in the web management interface of Brocade Fabric OS versions before 9.2.… |
| 2026-10-08 05:17:06 | [CVE-2026-94586](https://nvd.nist.gov/vuln/detail/CVE-2026-94586) | High | 8.5 | A command injection vulnerability exists in the WebTools administrative interface handling configuration download or fi… |
| 2026-10-08 05:17:06 | [CVE-2026-94587](https://nvd.nist.gov/vuln/detail/CVE-2026-94587) | Medium | 6.9 | A buffer overflow vulnerability exists in the WebTools administrative interface handling configuration download or file… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
