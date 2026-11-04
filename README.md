# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-11-04 15:18 UTC

New CVEs published between 2026-11-04 14:18 UTC and 2026-11-04 15:18 UTC.

[Full CSV](data/new-cves-2026-11-04T15-18-23-624897Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-11-04 15:17:21 | [CVE-2026-100407](https://nvd.nist.gov/vuln/detail/CVE-2026-100407) | Medium | 4.4 | Git for Windows is the Windows port of Git. From 2.44.0.windows.1 until 2.55.0.windows.3, the git-credential-wincred st… |
| 2026-11-04 15:17:21 | [CVE-2026-100408](https://nvd.nist.gov/vuln/detail/CVE-2026-100408) | Medium | 4.4 | Git for Windows is the Windows port of Git. From 2.43.0.windows.1 until 2.55.0.windows.3, when a matching git:* credent… |
| 2026-11-04 15:17:35 | [CVE-2026-114627](https://nvd.nist.gov/vuln/detail/CVE-2026-114627) |  |  | Web::Simple versions before 0.036 for Perl do not escape values interpolated into double-quoted strings in HTML::Tags o… |
| 2026-11-04 15:17:41 | [CVE-2026-119776](https://nvd.nist.gov/vuln/detail/CVE-2026-119776) | Medium | 6.1 | In all prior released versions of FRRouting, the OSPFv3 (for IPv6) implementation does not check that OSPFv3 packets ha… |
| 2026-11-04 15:17:41 | [CVE-2026-120421](https://nvd.nist.gov/vuln/detail/CVE-2026-120421) | Medium | 6.1 | In Eclipse Mojarra versions 2.2.0 through 4.0.28, 4.1.0 through 4.1.19, and 5.0.0-M1 through 5.0.0-M11, when URL client… |
| 2026-11-04 15:17:41 | [CVE-2026-121007](https://nvd.nist.gov/vuln/detail/CVE-2026-121007) |  |  | SQL::Abstract versions from 1.90_01 before 2.000001_04 for Perl allow SQL injection via the where values of a nested st… |
| 2026-11-04 15:17:41 | [CVE-2026-121008](https://nvd.nist.gov/vuln/detail/CVE-2026-121008) |  |  | SQL::Abstract::Tree versions before 2.000001_04 for Perl allow cross-site scripting via unescaped SQL text and bind val… |
| 2026-11-04 15:17:42 | [CVE-2026-121632](https://nvd.nist.gov/vuln/detail/CVE-2026-121632) |  |  | Data::MuForm versions through 0.05 for Perl render attribute values and option labels into HTML without escaping. proce… |
| 2026-11-04 15:17:42 | [CVE-2026-121637](https://nvd.nist.gov/vuln/detail/CVE-2026-121637) | High | 8.9 | An improper integrity validation vulnerability in WatchGuard AuthPoint Gateway's LDAP authentication callback allows a… |
| 2026-11-04 15:17:42 | [CVE-2026-121638](https://nvd.nist.gov/vuln/detail/CVE-2026-121638) | Critical | 9.1 | An Improper Certificate Validation vulnerability in WatchGuard AuthPoint Gateway allows an attacker with an on-path net… |
| 2026-11-04 15:17:42 | [CVE-2026-121639](https://nvd.nist.gov/vuln/detail/CVE-2026-121639) | Critical | 9.2 | A Missing Authentication for Critical Function vulnerability in WatchGuard AuthPoint Gateway allows a remote unauthenti… |
| 2026-11-04 15:17:42 | [CVE-2026-121640](https://nvd.nist.gov/vuln/detail/CVE-2026-121640) | Critical | 9.1 | An Authentication Bypass by Capture-replay vulnerability in WatchGuard AuthPoint Gateway allows an attacker who has obs… |
| 2026-11-04 15:17:42 | [CVE-2026-122006](https://nvd.nist.gov/vuln/detail/CVE-2026-122006) | Critical | 9.8 | The activestorage gem before 8.1.4.1 for Ruby on Rails, when ImageMagick attachment processing occurs, can allow server… |
| 2026-11-04 15:17:42 | [CVE-2026-121009](https://nvd.nist.gov/vuln/detail/CVE-2026-121009) |  |  | SQL::Abstract versions from 1.90_01 before 2.000001_04 for Perl skip the injection_guard check for function names given… |
| 2026-11-04 15:17:43 | [CVE-2026-122007](https://nvd.nist.gov/vuln/detail/CVE-2026-122007) | High | 7.4 | Oqtane Framework before 10.3.0 contains a broken access control vulnerability in SettingController.cs that allows an au… |
| 2026-11-04 15:17:43 | [CVE-2026-122008](https://nvd.nist.gov/vuln/detail/CVE-2026-122008) | Medium | 5.3 | Oqtane Framework before 10.3.0 contains a server-side request forgery vulnerability in the UploadFile endpoint of FileC… |
| 2026-11-04 15:17:44 | [CVE-2026-39430](https://nvd.nist.gov/vuln/detail/CVE-2026-39430) |  |  | On HP Poly EagleEye Cube USB 1.3.1-001267 devices, the administrator authentication flow is broken: session management… |
| 2026-11-04 15:17:44 | [CVE-2026-39431](https://nvd.nist.gov/vuln/detail/CVE-2026-39431) |  |  | On HP Poly EagleEye Cube USB 1.3.1-001267 devices, one of the API functions available on a management service accessibl… |
| 2026-11-04 15:17:47 | [CVE-2026-66736](https://nvd.nist.gov/vuln/detail/CVE-2026-66736) |  |  | Rejected reason: This CVE ID has been rejected or withdrawn by its CVE Numbering Authority. |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
