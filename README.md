# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-11-15 02:18 UTC

New CVEs published between 2026-11-15 01:18 UTC and 2026-11-15 02:18 UTC.

[Full CSV](data/new-cves-2026-11-15T02-18-17-736618Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-11-15 02:17:20 | [CVE-2026-129356](https://nvd.nist.gov/vuln/detail/CVE-2026-129356) | Low | 1.3 | A vulnerability was found in vllm-project vllm 0.30.0/0.31.0. This vulnerability affects unknown code of the file singl… |
| 2026-11-15 02:17:21 | [CVE-2026-129454](https://nvd.nist.gov/vuln/detail/CVE-2026-129454) | High | 7.1 | Zr.Admin.NET commit 85cff6a through commit eb9228a contains an insecure direct object reference vulnerability in GET /w… |
| 2026-11-15 02:17:21 | [CVE-2026-129455](https://nvd.nist.gov/vuln/detail/CVE-2026-129455) | Medium | 5.3 | Zr.Admin.NET commit e6ceaf4 through commit eb9228a contains an insecure direct object reference vulnerability in FrontA… |
| 2026-11-15 02:17:21 | [CVE-2026-129464](https://nvd.nist.gov/vuln/detail/CVE-2026-129464) | High | 8.7 | Zr.Admin.NET commit 0ee1ab8 through commit eb9228a contains a path traversal vulnerability that allows any logged-in us… |
| 2026-11-15 02:17:21 | [CVE-2026-129465](https://nvd.nist.gov/vuln/detail/CVE-2026-129465) | High | 8.7 | Zr.Admin.NET commit af07ffc through commit eb9228a contains an insecure direct object reference vulnerability in SysPro… |
| 2026-11-15 02:17:21 | [CVE-2026-129466](https://nvd.nist.gov/vuln/detail/CVE-2026-129466) | Medium | 5.3 | Zr.Admin.NET commit 1845017 through commit eb9228a contains a missing authorization vulnerability in TasksController.Ge… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
