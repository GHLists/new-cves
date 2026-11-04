# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-11-04 02:18 UTC

New CVEs published between 2026-11-04 01:18 UTC and 2026-11-04 02:18 UTC.

[Full CSV](data/new-cves-2026-11-04T02-18-18-279489Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-11-04 02:17:14 | [CVE-2026-110464](https://nvd.nist.gov/vuln/detail/CVE-2026-110464) | Medium | 6.9 | Missing authorization in ASUS Armoury Crate allows a local attacker to write content into a specific file or registry l… |
| 2026-11-04 02:17:14 | [CVE-2026-112116](https://nvd.nist.gov/vuln/detail/CVE-2026-112116) | High | 8.5 | An exposed IOCTL with insufficient access control in ASUS System Control Interface allows a local, low-privileged user… |
| 2026-11-04 02:17:19 | [CVE-2026-121607](https://nvd.nist.gov/vuln/detail/CVE-2026-121607) | Critical | 9.3 | A vulnerability was found in Qihoo 360 D603-2, D600-2, D606-6 and D706 up to 6.4.9. This affects the function testspeed… |
| 2026-11-04 02:17:20 | [CVE-2026-121609](https://nvd.nist.gov/vuln/detail/CVE-2026-121609) | Critical | 9.3 | A vulnerability was identified in Qihoo 360 Whole Home Router M5 4.0.17.1566. This issue affects the function Home of t… |
| 2026-11-04 02:17:20 | [CVE-2026-121610](https://nvd.nist.gov/vuln/detail/CVE-2026-121610) | Medium | 5.5 | A security flaw has been discovered in funadmin 7.1.0. Impacted is the function Curd::selectList of the file /frontend/… |
| 2026-11-04 02:17:20 | [CVE-2026-121608](https://nvd.nist.gov/vuln/detail/CVE-2026-121608) | Medium | 5.5 | A vulnerability was determined in Qihoo 360 D603-2, D600-2 and D606-6 up to 6.3.2. This vulnerability affects the funct… |
| 2026-11-04 02:17:21 | [CVE-2026-84729](https://nvd.nist.gov/vuln/detail/CVE-2026-84729) | High | 7.2 | Out-of-bounds write in certain ASUS Router firmware allow an unauthenticated nearby attacker to write data beyond the i… |
| 2026-11-04 02:17:21 | [CVE-2026-84730](https://nvd.nist.gov/vuln/detail/CVE-2026-84730) | High | 8.7 | Stack-based buffer overflow in certain ASUS Router firmware allows an unauthenticated nearby attacker to execute arbitr… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
