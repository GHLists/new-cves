# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-11-09 15:19 UTC

New CVEs published between 2026-11-09 14:18 UTC and 2026-11-09 15:19 UTC.

[Full CSV](data/new-cves-2026-11-09T15-19-37-263971Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-11-09 15:17:04 | [CVE-2026-104620](https://nvd.nist.gov/vuln/detail/CVE-2026-104620) | High | 8.5 | A path traversal attack in simulation of actions in the Zypp backend of PackageKit before 1.4.1 could be used by local… |
| 2026-11-09 15:17:07 | [CVE-2026-119474](https://nvd.nist.gov/vuln/detail/CVE-2026-119474) | High | 7.8 | Incorrect Permission Assignment for Critical Resource vulnerability in HAVELSAN Inc. Liman Render Engine allows Privile… |
| 2026-11-09 15:17:14 | [CVE-2026-124249](https://nvd.nist.gov/vuln/detail/CVE-2026-124249) | Medium | 6.3 | http.cookiejar.CookieJar deleted a stored cookie when a response carried an already expired Set-Cookie header for it, u… |
| 2026-11-09 15:17:18 | [CVE-2026-124636](https://nvd.nist.gov/vuln/detail/CVE-2026-124636) | Medium | 5.1 | A security flaw has been discovered in kevquirk PureBlog up to 3.7.2. The affected element is the function save_page of… |
| 2026-11-09 15:17:19 | [CVE-2026-124850](https://nvd.nist.gov/vuln/detail/CVE-2026-124850) | High | 7.3 | A SQL injection vulnerability exists in a database migration script in flowintel. The migration process reads stored co… |
| 2026-11-09 15:17:19 | [CVE-2026-124916](https://nvd.nist.gov/vuln/detail/CVE-2026-124916) |  |  | PrestaShop contains an authenticated PHP code injection vulnerability in the back-office Performance debug-mode configu… |
| 2026-11-09 15:17:19 | [CVE-2026-124959](https://nvd.nist.gov/vuln/detail/CVE-2026-124959) |  |  | The loadIndex function in nmslib hnswlib and Spotify Voyager does not verify that the element count in a serialized HNS… |
| 2026-11-09 15:17:21 | [CVE-2026-19552](https://nvd.nist.gov/vuln/detail/CVE-2026-19552) | None | 0.0 | When ca_certs parameter was supplied to ssl.get_server_certificate() function, the identity of the certificate is not c… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
