# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-11-16 22:18 UTC

New CVEs published between 2026-11-16 21:18 UTC and 2026-11-16 22:18 UTC.

[Full CSV](data/new-cves-2026-11-16T22-18-21-676569Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-11-16 22:18:12 | [CVE-2025-71471](https://nvd.nist.gov/vuln/detail/CVE-2025-71471) | Medium | 6.8 | GPAC before 26.02.0 contains a use of uninitialized memory vulnerability in stbl_AddCTS() that allows attackers to corr… |
| 2026-11-16 22:18:13 | [CVE-2026-110339](https://nvd.nist.gov/vuln/detail/CVE-2026-110339) | High | 7.5 | The Libreswan pluto daemon dereferences a NULL pointer when a CERT payload is received with an empty PKCS#7 payload, ca… |
| 2026-11-16 22:18:14 | [CVE-2026-115846](https://nvd.nist.gov/vuln/detail/CVE-2026-115846) | Low | 3.7 | The Libreswan IKEv2 state machine did not verify that an IKE_INTERMEDIATE exchange was required to satisfy the addke= P… |
| 2026-11-16 22:18:14 | [CVE-2026-120697](https://nvd.nist.gov/vuln/detail/CVE-2026-120697) | High | 8.7 | Wiki.js is an open source wiki app built on Node.js. Prior to 2.5.315, an authenticated user with write:pages can store… |
| 2026-11-16 22:18:14 | [CVE-2026-120698](https://nvd.nist.gov/vuln/detail/CVE-2026-120698) | High | 8.8 | Wiki.js is an open source wiki app built on Node.js. Prior to 2.5.315, an authenticated account with only manage:users… |
| 2026-11-16 22:18:15 | [CVE-2026-123353](https://nvd.nist.gov/vuln/detail/CVE-2026-123353) | Low | 3.3 | Docmost is open-source collaborative wiki and documentation software. Prior to 0.96.0, two concurrent role-demotion req… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
