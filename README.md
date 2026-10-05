# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-05 11:18 UTC

New CVEs published between 2026-10-05 10:18 UTC and 2026-10-05 11:18 UTC.

[Full CSV](data/new-cves-2026-10-05T11-18-37-507157Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-10-05 11:16:46 | [CVE-2026-105289](https://nvd.nist.gov/vuln/detail/CVE-2026-105289) | Low | 2.0 | A vulnerability was found in feelec-yishu feelcrm-os 1.0.0. Affected by this issue is the function htmlspecialchars_dec… |
| 2026-10-05 11:16:46 | [CVE-2026-105290](https://nvd.nist.gov/vuln/detail/CVE-2026-105290) | Medium | 5.5 | A vulnerability was determined in feelec-yishu feelcrm-os 1.0.0. This affects an unknown part of the file App/Feelcrm/I… |
| 2026-10-05 11:16:46 | [CVE-2026-105291](https://nvd.nist.gov/vuln/detail/CVE-2026-105291) | Low | 2.1 | A vulnerability was identified in feelec-yishu feelcrm-os 1.0.0. This vulnerability affects the function GroupControlle… |
| 2026-10-05 11:16:53 | [CVE-2026-39763](https://nvd.nist.gov/vuln/detail/CVE-2026-39763) | Medium | 4.3 | Missing Authorization vulnerability in Deepak Anand WP Dummy Content Generator wp-dummy-content-generator allows Exploi… |
| 2026-10-05 11:16:59 | [CVE-2026-59782](https://nvd.nist.gov/vuln/detail/CVE-2026-59782) | Medium | 6.9 | The JavaScript preprocessing (Duktape) engine on Zabbix server has a vulnerability where a limited administrator is abl… |
| 2026-10-05 11:16:59 | [CVE-2026-59783](https://nvd.nist.gov/vuln/detail/CVE-2026-59783) | Low | 2.3 | The Zabbix Server/Proxy has a vulnerability where binary items can crash the Server/Proxy on certain NULL byte input le… |
| 2026-10-05 11:16:59 | [CVE-2026-59785](https://nvd.nist.gov/vuln/detail/CVE-2026-59785) | Medium | 5.1 | Host search in Frontend allows filtering by fields that are not displayed, including stored IPMI and PSK credentials. A… |
| 2026-10-05 11:16:59 | [CVE-2026-59786](https://nvd.nist.gov/vuln/detail/CVE-2026-59786) | Medium | 6.9 | Zabbix Server and Proxy accept the active agent heartbeat message regardless of the configured PSK or certificate authe… |
| 2026-10-05 11:16:59 | [CVE-2026-59787](https://nvd.nist.gov/vuln/detail/CVE-2026-59787) | Medium | 5.3 | The Perl SNMP trap receiver script shipped with Zabbix does not properly neutralize the ZBXTRAP record delimiter in tra… |
| 2026-10-05 11:17:00 | [CVE-2026-59788](https://nvd.nist.gov/vuln/detail/CVE-2026-59788) | Medium | 5.7 | The email media type OAuth form passes the Authorization endpoint value to window.open() without validating the URL sch… |
| 2026-10-05 11:17:01 | [CVE-2026-94669](https://nvd.nist.gov/vuln/detail/CVE-2026-94669) | Medium | 5.3 | Missing Authorization vulnerability in WP ManageNinja LLC Fluent Forms Pro Add On Pack fluentformpro allows Exploiting… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
