# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-11-09 18:19 UTC

New CVEs published between 2026-11-09 17:21 UTC and 2026-11-09 18:19 UTC.

[Full CSV](data/new-cves-2026-11-09T18-19-13-734646Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-11-09 18:17:22 | [CVE-2026-119755](https://nvd.nist.gov/vuln/detail/CVE-2026-119755) | High | 7.5 | Tasmota through 16.0.0, fixed in commit 1cb7ebc, contains a cross-site request forgery vulnerability that allows unauth… |
| 2026-11-09 18:17:22 | [CVE-2026-119756](https://nvd.nist.gov/vuln/detail/CVE-2026-119756) | Critical | 9.3 | Tasmota through 16.0.0, fixed in commit e97e1e4, contains a heap out-of-bounds write vulnerability in SendReceiveDevice… |
| 2026-11-09 18:17:25 | [CVE-2026-123270](https://nvd.nist.gov/vuln/detail/CVE-2026-123270) | Critical | 9.8 | Redpanda Connect versions 4.39 to 4.110 contain a missing authentication vulnerability that enables unauthenticated rem… |
| 2026-11-09 18:17:25 | [CVE-2026-123367](https://nvd.nist.gov/vuln/detail/CVE-2026-123367) | High | 7.4 | Thor Vector Graphics (ThorVG) is a production-ready vector graphics engine. Prior to 1.1.2, the bundled jpgd JPEG decod… |
| 2026-11-09 18:17:25 | [CVE-2026-123368](https://nvd.nist.gov/vuln/detail/CVE-2026-123368) | Low | 2.3 | compose-lint is a Docker Compose security linter that identifies dangerous misconfigurations before deployment. From 0.… |
| 2026-11-09 18:17:25 | [CVE-2026-123369](https://nvd.nist.gov/vuln/detail/CVE-2026-123369) | Medium | 5.3 | compose-lint is a Docker Compose security linter that identifies dangerous misconfigurations before deployment. Prior t… |
| 2026-11-09 18:17:25 | [CVE-2026-123370](https://nvd.nist.gov/vuln/detail/CVE-2026-123370) | Medium | 5.1 | compose-lint is a Docker Compose security linter that identifies dangerous misconfigurations before deployment. From 0.… |
| 2026-11-09 18:17:26 | [CVE-2026-123371](https://nvd.nist.gov/vuln/detail/CVE-2026-123371) | Low | 2.3 | compose-lint is a Docker Compose security linter that identifies dangerous misconfigurations before deployment. From 0.… |
| 2026-11-09 18:17:26 | [CVE-2026-123372](https://nvd.nist.gov/vuln/detail/CVE-2026-123372) | Low | 2.3 | compose-lint is a Docker Compose security linter that identifies dangerous misconfigurations before deployment. From 0.… |
| 2026-11-09 18:17:26 | [CVE-2026-123373](https://nvd.nist.gov/vuln/detail/CVE-2026-123373) | Low | 2.3 | compose-lint is a Docker Compose security linter that identifies dangerous misconfigurations before deployment. From 0.… |
| 2026-11-09 18:17:26 | [CVE-2026-123796](https://nvd.nist.gov/vuln/detail/CVE-2026-123796) | Low | 2.3 | compose-lint is a Docker Compose security linter that identifies dangerous misconfigurations before deployment. From 0.… |
| 2026-11-09 18:17:26 | [CVE-2026-123797](https://nvd.nist.gov/vuln/detail/CVE-2026-123797) | High | 7.5 | SuperTokens Core is an open source authentication server. Prior to 11.3.6, 11.4.6, and 12.0.8, app-specific management… |
| 2026-11-09 18:17:27 | [CVE-2026-125063](https://nvd.nist.gov/vuln/detail/CVE-2026-125063) | Medium | 4.3 | A flaw was found in the rrule validation of schedules in automation controller. Several non-anchored regular expression… |
| 2026-11-09 18:17:27 | [CVE-2026-19706](https://nvd.nist.gov/vuln/detail/CVE-2026-19706) | High | 8.3 | During ABI bootstrap, the bootstrap node's approve-csr.service approves and signs every CSR without identity validation… |
| 2026-11-09 18:17:29 | [CVE-2026-60117](https://nvd.nist.gov/vuln/detail/CVE-2026-60117) | Medium | 6.9 | The Android implementation of the Flutter/Dart receive_sharing_intent package, versions 1.4.1 through 1.9.0, contains a… |
| 2026-11-09 18:17:34 | [CVE-2026-84503](https://nvd.nist.gov/vuln/detail/CVE-2026-84503) | Medium | 6.7 | A flaw was found in ansible-core's ansible.builtin.git module. The module invokes git (ls-remote, clone, fetch) with th… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
