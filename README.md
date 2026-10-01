# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-01 19:18 UTC

New CVEs published between 2026-10-01 18:21 UTC and 2026-10-01 19:18 UTC.

[Full CSV](data/new-cves-2026-10-01T19-18-39-025468Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-10-01 19:17:19 | [CVE-2026-104056](https://nvd.nist.gov/vuln/detail/CVE-2026-104056) |  |  | Authlib version 1.7.2 and below contains a vulnerability where discovery JSON metadata is cached without validation or… |
| 2026-10-01 19:17:19 | [CVE-2026-104057](https://nvd.nist.gov/vuln/detail/CVE-2026-104057) | High | 8.7 | Podgrab contains an unauthenticated denial-of-service vulnerability caused by unsynchronized concurrent access to share… |
| 2026-10-01 19:17:19 | [CVE-2026-104058](https://nvd.nist.gov/vuln/detail/CVE-2026-104058) | Medium | 6.3 | Podgrab contains a missing authentication vulnerability in which the /ws WebSocket route is registered on the root gin… |
| 2026-10-01 19:17:19 | [CVE-2026-104059](https://nvd.nist.gov/vuln/detail/CVE-2026-104059) | High | 7.0 | Lektor 3.3.14 and 3.4.0b15 contains a cross-site request forgery vulnerability in the admin API blueprint that allows u… |
| 2026-10-01 19:17:19 | [CVE-2026-15911](https://nvd.nist.gov/vuln/detail/CVE-2026-15911) | High | 7.4 | Confluent Kafka Python client's HashiCorp Vault KMS integration could allow a remote attacker to obtain sensitive infor… |
| 2026-10-01 19:17:20 | [CVE-2026-27872](https://nvd.nist.gov/vuln/detail/CVE-2026-27872) | Medium | 5.6 | - Improper Privilege Management vulnerability in Johnson Controls Easy IO FG allows (Brute Force). This issue affects E… |
| 2026-10-01 19:17:21 | [CVE-2026-55083](https://nvd.nist.gov/vuln/detail/CVE-2026-55083) | Critical | 9.1 | DHIS2 is a flexible information system for data capture, management, validation, analytics and visualization. From vers… |
| 2026-10-01 19:17:21 | [CVE-2026-55230](https://nvd.nist.gov/vuln/detail/CVE-2026-55230) | High | 8.7 | Vvveb is a powerful and easy to use CMS with page builder to build websites, blogs or ecommerce stores. Prior to versio… |
| 2026-10-01 19:17:21 | [CVE-2026-55231](https://nvd.nist.gov/vuln/detail/CVE-2026-55231) | High | 7.2 | Vvveb is a powerful and easy to use CMS with page builder to build websites, blogs or ecommerce stores. Prior to versio… |
| 2026-10-01 19:17:21 | [CVE-2026-55232](https://nvd.nist.gov/vuln/detail/CVE-2026-55232) | High | 7.6 | Vvveb is a powerful and easy to use CMS with page builder to build websites, blogs or ecommerce stores. Prior to versio… |
| 2026-10-01 19:17:24 | [CVE-2026-63721](https://nvd.nist.gov/vuln/detail/CVE-2026-63721) |  |  | Rejected reason: This CVE ID has been rejected or withdrawn by its CVE Numbering Authority. |
| 2026-10-01 19:17:24 | [CVE-2026-63724](https://nvd.nist.gov/vuln/detail/CVE-2026-63724) |  |  | Rejected reason: This CVE ID has been rejected or withdrawn by its CVE Numbering Authority. |
| 2026-10-01 19:17:24 | [CVE-2026-84682](https://nvd.nist.gov/vuln/detail/CVE-2026-84682) | High | 7.7 | A command injection vulnerability exists in the TDDPv2 service (/usr/bin/tddp) on Archer AX90 V1. An unauthenticated ad… |
| 2026-10-01 19:17:25 | [CVE-2026-8618](https://nvd.nist.gov/vuln/detail/CVE-2026-8618) | High | 7.7 | A stack-based buffer overflow vulnerability exists in the TDDPv2 service (/usr/bin/tddp) on Deco M9 Plus due to insuffi… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
