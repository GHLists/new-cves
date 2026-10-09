# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-09 06:18 UTC

New CVEs published between 2026-10-09 05:19 UTC and 2026-10-09 06:18 UTC.

[Full CSV](data/new-cves-2026-10-09T06-18-39-472647Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-10-09 06:17:10 | [CVE-2026-107908](https://nvd.nist.gov/vuln/detail/CVE-2026-107908) | Critical | 9.3 | A heap-based out-of-bounds write in the BoltReadHandler function (src/bolt/bolt_api.c) in FalkorDB before 4.20.0 allows… |
| 2026-10-09 06:17:12 | [CVE-2026-107909](https://nvd.nist.gov/vuln/detail/CVE-2026-107909) | High | 8.8 | A heap-based out-of-bounds write in the ws_read_frame function (src/bolt/ws.c) and the buffer_apply_mask function (src/… |
| 2026-10-09 06:17:12 | [CVE-2026-107910](https://nvd.nist.gov/vuln/detail/CVE-2026-107910) | Critical | 9.2 | An improper authentication vulnerability in the is_authenticated function (src/bolt/bolt_api.c) in FalkorDB before 4.20… |
| 2026-10-09 06:17:12 | [CVE-2026-107911](https://nvd.nist.gov/vuln/detail/CVE-2026-107911) | High | 7.7 | A type confusion vulnerability in the _read_flags function (src/commands/cmd_dispatcher.c) in FalkorDB before 4.20.0 al… |
| 2026-10-09 06:17:12 | [CVE-2026-107914](https://nvd.nist.gov/vuln/detail/CVE-2026-107914) | High | 7.8 | Backdrop CMS 1.34 before 1.34.5 and 1.35 before 1.35.1 doesn't sufficiently protect configuration exports when deliveri… |
| 2026-10-09 06:17:12 | [CVE-2026-87108](https://nvd.nist.gov/vuln/detail/CVE-2026-87108) | Low | 2.3 | An authenticated Ops Manager user with a read-only project role can retrieve a daily host monitoring record associated… |
| 2026-10-09 06:17:13 | [CVE-2026-87109](https://nvd.nist.gov/vuln/detail/CVE-2026-87109) | Medium | 6.0 | An authenticated Ops Manager organization member can retrieve another member's pending authenticator enrollment seed th… |
| 2026-10-09 06:17:13 | [CVE-2026-87110](https://nvd.nist.gov/vuln/detail/CVE-2026-87110) | Medium | 6.9 | An unauthenticated user with network access to the Ops Manager web port can repeatedly request monitoring endpoints tha… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
