# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-30 13:18 UTC

New CVEs published between 2026-10-30 12:20 UTC and 2026-10-30 13:18 UTC.

[Full CSV](data/new-cves-2026-10-30T13-18-55-589129Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-10-30 13:18:28 | [CVE-2026-111501](https://nvd.nist.gov/vuln/detail/CVE-2026-111501) | Medium | 5.4 | Dell OpenManage Enterprise, versions prior to 4.8.0, contains an Improper Restriction of Excessive Authentication Attem… |
| 2026-10-30 13:18:28 | [CVE-2026-111502](https://nvd.nist.gov/vuln/detail/CVE-2026-111502) | Medium | 4.3 | Dell OpenManage Enterprise, versions prior to 4.8.0, contains an Insufficiently Protected Credentials vulnerability. A… |
| 2026-10-30 13:18:28 | [CVE-2026-111503](https://nvd.nist.gov/vuln/detail/CVE-2026-111503) | High | 7.1 | Dell OpenManage Enterprise, versions prior to 4.8.0, contains an Improper Neutralization of Special Elements used in an… |
| 2026-10-30 13:18:29 | [CVE-2026-112374](https://nvd.nist.gov/vuln/detail/CVE-2026-112374) | Medium | 5.1 | FOSSBilling before 0.8.9 contains a Cross-Site Request Forgery vulnerability in the staff guest login endpoint (POST /a… |
| 2026-10-30 13:18:30 | [CVE-2026-115865](https://nvd.nist.gov/vuln/detail/CVE-2026-115865) |  |  | Starlet versions before 0.33 for Perl allow a request declaring a large Content-Length to kill a worker by exhausting m… |
| 2026-10-30 13:18:31 | [CVE-2026-115866](https://nvd.nist.gov/vuln/detail/CVE-2026-115866) |  |  | Starlet versions from 0.20 before 0.33 for Perl allow CPU exhaustion via regular expression backtracking when decoding… |
| 2026-10-30 13:18:31 | [CVE-2026-116127](https://nvd.nist.gov/vuln/detail/CVE-2026-116127) |  |  | Starlet versions before 0.33 for Perl send a body in responses to HEAD requests, corrupting the next response on a pers… |
| 2026-10-30 13:18:31 | [CVE-2026-116128](https://nvd.nist.gov/vuln/detail/CVE-2026-116128) |  |  | Starlet versions from 0.20 before 0.33 for Perl allow memory exhaustion via unbounded buffering when decoding chunked r… |
| 2026-10-30 13:18:31 | [CVE-2026-116130](https://nvd.nist.gov/vuln/detail/CVE-2026-116130) |  |  | HTTP::Parser::XS versions before 0.18 for Perl truncate PATH_INFO at an encoded NUL byte in parse_http_request. The XS… |
| 2026-10-30 13:18:31 | [CVE-2026-118988](https://nvd.nist.gov/vuln/detail/CVE-2026-118988) |  |  | CallBackery versions before 0.60.1 for Perl let unauthenticated clients read the POD of any file via path traversal in… |
| 2026-10-30 13:18:31 | [CVE-2026-118990](https://nvd.nist.gov/vuln/detail/CVE-2026-118990) |  |  | CallBackery versions before 0.62.0 for Perl leave a world-readable dump of the configuration database in /tmp when taki… |
| 2026-10-30 13:18:31 | [CVE-2026-118991](https://nvd.nist.gov/vuln/detail/CVE-2026-118991) |  |  | CallBackery versions before 0.62.0 for Perl encrypt configuration backups with the padded password as the AES key. getC… |
| 2026-10-30 13:18:31 | [CVE-2026-118992](https://nvd.nist.gov/vuln/detail/CVE-2026-118992) |  |  | CallBackery versions before 0.62.0 for Perl allow OS command execution via sqlite3 shell commands in a restored configu… |
| 2026-10-30 13:18:32 | [CVE-2026-118993](https://nvd.nist.gov/vuln/detail/CVE-2026-118993) |  |  | CallBackery versions before 0.62.0 for Perl allow denial of service via the request path interpolated as a regular expr… |
| 2026-10-30 13:18:32 | [CVE-2026-118994](https://nvd.nist.gov/vuln/detail/CVE-2026-118994) |  |  | CallBackery versions before 0.62.0 for Perl allow log injection via newlines in the login name. login() writes the logi… |
| 2026-10-30 13:18:32 | [CVE-2026-118995](https://nvd.nist.gov/vuln/detail/CVE-2026-118995) |  |  | CallBackery versions before 0.62.0 for Perl accept unintended values in form fields checked by createRxValidator. creat… |
| 2026-10-30 13:18:32 | [CVE-2026-118996](https://nvd.nist.gov/vuln/detail/CVE-2026-118996) |  |  | CallBackery versions before 0.62.0 for Perl send users their own password hash and the admin-only user note via getUser… |
| 2026-10-30 13:18:32 | [CVE-2026-119036](https://nvd.nist.gov/vuln/detail/CVE-2026-119036) |  |  | Business::GoCardless versions before 1.01 for Perl allow memory exhaustion by flattening legacy webhook payloads before… |
| 2026-10-30 13:18:32 | [CVE-2026-119037](https://nvd.nist.gov/vuln/detail/CVE-2026-119037) |  |  | Business::GoCardless versions before 1.01 for Perl accept forged webhooks when a configured webhook secret is undef or… |
| 2026-10-30 13:18:32 | [CVE-2026-119038](https://nvd.nist.gov/vuln/detail/CVE-2026-119038) |  |  | Business::GoCardless versions before 1.01 for Perl complete redirect flows without checking the session token, letting… |
| 2026-10-30 13:18:32 | [CVE-2026-13576](https://nvd.nist.gov/vuln/detail/CVE-2026-13576) |  |  | CallBackery versions before 0.62.0 for Perl store user passwords as unsalted HMAC-SHA1 hashes. Passwords are hashed wit… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
