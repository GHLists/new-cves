# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-20 05:21 UTC

New CVEs published between 2026-10-20 04:19 UTC and 2026-10-20 05:21 UTC.

[Full CSV](data/new-cves-2026-10-20T05-21-11-346523Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-10-20 05:16:53 | [CVE-2026-109831](https://nvd.nist.gov/vuln/detail/CVE-2026-109831) | Medium | 5.1 | UnRTF by GNU Project is vulnerable to out-of-bounds write. If a user opens an RTF file crafted by an attacker, it may l… |
| 2026-10-20 05:16:54 | [CVE-2026-113380](https://nvd.nist.gov/vuln/detail/CVE-2026-113380) | Critical | 9.3 | In the RingRTC library before 2.72.0 for Signal, a peer that saturates a call's FSM queue can interfere with the abilit… |
| 2026-10-20 05:16:54 | [CVE-2026-113386](https://nvd.nist.gov/vuln/detail/CVE-2026-113386) | High | 7.1 | Roundcube Webmail before 1.6.20 and 1.7.x before 1.7.5 are affected by IMAP command injection. A remote authenticated a… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
