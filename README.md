# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-11-05 07:31 UTC

New CVEs published between 2026-11-05 06:24 UTC and 2026-11-05 07:31 UTC.

[Full CSV](data/new-cves-2026-11-05T07-31-06-214871Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-11-05 07:17:24 | [CVE-2026-123017](https://nvd.nist.gov/vuln/detail/CVE-2026-123017) | Medium | 6.5 | GodotSteam 4.17 through 4.23.2 trusts the peer value of 1 to mean that a player is the server. A grant_gold(1000000) ca… |
| 2026-11-05 07:17:25 | [CVE-2026-123025](https://nvd.nist.gov/vuln/detail/CVE-2026-123025) | Critical | 9.4 | An OS Command Injection vulnerability was discovered in the Google Cloud DNS validation module of the OPNsense os-acme-… |
| 2026-11-05 07:17:26 | [CVE-2026-123029](https://nvd.nist.gov/vuln/detail/CVE-2026-123029) | High | 7.5 | Wowza Streaming Engine before 4.12.2 processes XML external entities, which allows remote attackers to read local files… |
| 2026-11-05 07:17:26 | [CVE-2026-123033](https://nvd.nist.gov/vuln/detail/CVE-2026-123033) | High | 8.3 | Authentication bypass in the HA heartbeat origin check in middlewared in TrueNAS SCALE before 25.10.8 (and in release t… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
