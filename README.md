# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-02 00:18 UTC

New CVEs published between 2026-10-01 23:18 UTC and 2026-10-02 00:18 UTC.

[Full CSV](data/new-cves-2026-10-02T00-18-34-202596Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-10-02 00:16:59 | [CVE-2026-103764](https://nvd.nist.gov/vuln/detail/CVE-2026-103764) | Critical | 9.3 | Mooncake transfer engine before 0.3.13 contains an untrusted pointer dereference in ServerSession::readHeader that allo… |
| 2026-10-02 00:16:59 | [CVE-2026-103765](https://nvd.nist.gov/vuln/detail/CVE-2026-103765) | High | 8.8 | Mooncake through 0.3.13.post1 contains a missing authentication vulnerability in the HTTP metadata server /metadata han… |
| 2026-10-02 00:16:59 | [CVE-2026-103766](https://nvd.nist.gov/vuln/detail/CVE-2026-103766) | High | 8.6 | ClipBucket v5 through 5.5.3-#197 contains an sql injection vulnerability that allows authenticated users with ad_manage… |
| 2026-10-02 00:17:04 | [CVE-2026-86345](https://nvd.nist.gov/vuln/detail/CVE-2026-86345) | Critical | 9.0 | A flaw was found in 389-ds-base. The server does not discard plaintext bytes already buffered from a client connection… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
