# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-11-13 16:18 UTC

New CVEs published between 2026-11-13 15:18 UTC and 2026-11-13 16:18 UTC.

[Full CSV](data/new-cves-2026-11-13T16-18-43-624773Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-11-13 16:17:18 | [CVE-2024-58406](https://nvd.nist.gov/vuln/detail/CVE-2024-58406) | High | 8.7 | Huatian Dynamic OA8000 collaborative office system contains an unauthenticated path traversal vulnerability in /OAapp/j… |
| 2026-11-13 16:17:21 | [CVE-2026-103813](https://nvd.nist.gov/vuln/detail/CVE-2026-103813) | Critical | 9.1 | Dell PowerStore contains an OS Command Injection vulnerability. An authenticated user with limited privileges could pot… |
| 2026-11-13 16:17:21 | [CVE-2026-105622](https://nvd.nist.gov/vuln/detail/CVE-2026-105622) | Medium | 6.3 | Improper restriction of excessive authentication attempts in the WAMP-CRA (challenge-response) authentication path in Z… |
| 2026-11-13 16:17:22 | [CVE-2026-105623](https://nvd.nist.gov/vuln/detail/CVE-2026-105623) | Medium | 6.9 | The web interface in Zenitel Connect before 1.11.0 serves production JavaScript source maps without authentication, whi… |
| 2026-11-13 16:17:23 | [CVE-2026-105624](https://nvd.nist.gov/vuln/detail/CVE-2026-105624) | Medium | 6.9 | The login flow in Zenitel Connect before 1.11.0 applies per-account lockout on repeated failed login attempts, which al… |
| 2026-11-13 16:17:23 | [CVE-2026-105625](https://nvd.nist.gov/vuln/detail/CVE-2026-105625) | Medium | 5.1 | The web interface in Zenitel Connect before 1.11.0 loads an integration iframe without sandboxing or origin restriction… |
| 2026-11-13 16:17:23 | [CVE-2026-105671](https://nvd.nist.gov/vuln/detail/CVE-2026-105671) | Medium | 6.9 | The login flow in Zenitel Connect before 1.11.0 returns different error responses depending on whether a submitted user… |
| 2026-11-13 16:17:25 | [CVE-2026-109091](https://nvd.nist.gov/vuln/detail/CVE-2026-109091) | High | 7.8 | A buffer overflow in handling EDID Display-Range descriptors in X.Org xwayland before 24.1.15 and X Server before 21.1.… |
| 2026-11-13 16:17:26 | [CVE-2026-111545](https://nvd.nist.gov/vuln/detail/CVE-2026-111545) | High | 8.8 | Dell PowerStore contains a SQL Injection vulnerability. An authenticated attacker could exploit this vulnerability, pot… |
| 2026-11-13 16:17:36 | [CVE-2026-121808](https://nvd.nist.gov/vuln/detail/CVE-2026-121808) | High | 8.2 | Improper Handling of Highly Compressed Data (Data Amplification) vulnerability in elixir-grpc grpc_core and grpc allows… |
| 2026-11-13 16:17:37 | [CVE-2026-123635](https://nvd.nist.gov/vuln/detail/CVE-2026-123635) | Medium | 6.3 | Missing Release of Resource after Effective Lifetime vulnerability in elixir-grpc grpc_server allows a client to stall… |
| 2026-11-13 16:17:39 | [CVE-2026-124278](https://nvd.nist.gov/vuln/detail/CVE-2026-124278) | High | 7.6 | Authorization Bypass Through User-Controlled Key vulnerability in elixir-grpc grpc_server and grpc allows an attacker t… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
