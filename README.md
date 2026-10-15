# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-15 04:19 UTC

New CVEs published between 2026-10-15 03:19 UTC and 2026-10-15 04:19 UTC.

[Full CSV](data/new-cves-2026-10-15T04-19-25-484581Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-10-15 04:18:22 | [CVE-2026-110911](https://nvd.nist.gov/vuln/detail/CVE-2026-110911) | Critical | 9.8 | Wheels 1.1.8 through 4.1.1 allows SQL injection when caller-supplied quoted values are parsed again as SQL by dynamic f… |
| 2026-10-15 04:18:23 | [CVE-2026-110912](https://nvd.nist.gov/vuln/detail/CVE-2026-110912) | High | 7.1 | In DragonFly BSD through 6.4.2 before 4bb22ff, the ARP input handlers arpintr() and in_arpinput() (sys/netinet/if_ether… |
| 2026-10-15 04:18:26 | [CVE-2026-76664](https://nvd.nist.gov/vuln/detail/CVE-2026-76664) | Medium | 6.4 | A security vulnerability in HPE NonStop EXPAND may result in out-of-bounds memory read/write operations |
| 2026-10-15 04:18:30 | [CVE-2026-93483](https://nvd.nist.gov/vuln/detail/CVE-2026-93483) | Critical | 9.5 | In Znuny through 7.3.6, an attacker can bypass specific standard login procedures and gain unauthorized access to sensi… |
| 2026-10-15 04:18:30 | [CVE-2026-93484](https://nvd.nist.gov/vuln/detail/CVE-2026-93484) | High | 8.6 | Znuny through 7.3.6 constructs a ticket-search database query by directly concatenating user-supplied input into the SQ… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
