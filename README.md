# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-11-23 13:19 UTC

New CVEs published between 2026-11-23 12:18 UTC and 2026-11-23 13:19 UTC.

[Full CSV](data/new-cves-2026-11-23T13-19-41-564575Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-11-23 13:17:02 | [CVE-2026-116001](https://nvd.nist.gov/vuln/detail/CVE-2026-116001) |  |  | NULL pointer dereference vulnerability in Apache Perl. This issue affects Apache Perl: from 1.99_04 through 2.0.13. Use… |
| 2026-11-23 13:17:02 | [CVE-2026-116005](https://nvd.nist.gov/vuln/detail/CVE-2026-116005) |  |  | Fixed-size stack buffer overflow vulnerability in Apache Perl. This issue affects Apache Perl: from 1.99_01 through 2.0… |
| 2026-11-23 13:17:02 | [CVE-2026-116032](https://nvd.nist.gov/vuln/detail/CVE-2026-116032) |  |  | Stack buffer overflow vulnerability in Apache Perl. This issue affects Apache Perl: from 1.99_01 through 2.0.13. Users… |
| 2026-11-23 13:17:02 | [CVE-2026-116043](https://nvd.nist.gov/vuln/detail/CVE-2026-116043) |  |  | NULL pointer dereference, Out-of-bounds read vulnerability in Apache Perl. This issue affects Apache Perl: from 1.99_01… |
| 2026-11-23 13:17:03 | [CVE-2026-116772](https://nvd.nist.gov/vuln/detail/CVE-2026-116772) |  |  | OOB read vulnerability in Apache Perl. This issue affects Apache Perl: from 1.99_07 through 2.0.13. Users are recommend… |
| 2026-11-23 13:17:03 | [CVE-2026-116799](https://nvd.nist.gov/vuln/detail/CVE-2026-116799) |  |  | OOB read vulnerability in Apache Perl. This issue affects Apache Perl: from 1.99_01 through 2.0.13. Note: The over-read… |
| 2026-11-23 13:17:03 | [CVE-2026-125651](https://nvd.nist.gov/vuln/detail/CVE-2026-125651) |  |  | Cleartext storage in encrypted parquet file vulnerability in Apache Arrow Rust (`parquet` crate), from version 55.0.0 t… |
| 2026-11-23 13:17:05 | [CVE-2026-134925](https://nvd.nist.gov/vuln/detail/CVE-2026-134925) | Medium | 5.1 | A security flaw has been discovered in yangzongzhuan RuoYi up to 4.8.3. Affected is the function renderUserCards of the… |
| 2026-11-23 13:17:05 | [CVE-2026-53672](https://nvd.nist.gov/vuln/detail/CVE-2026-53672) | Medium | 6.5 | A bug related to the Zookeeper HTTP endpoints in Apache Solr allows an authenticated attacker with zk-read permission t… |
| 2026-11-23 13:17:06 | [CVE-2026-86312](https://nvd.nist.gov/vuln/detail/CVE-2026-86312) | High | 8.8 | Under some configurations a request to the ping endpoint could carry out more than a simple health check. In deployment… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
