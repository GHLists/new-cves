# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-09-24 22:20 UTC

New CVEs published between 2026-09-24 21:18 UTC and 2026-09-24 22:20 UTC.

[Full CSV](data/new-cves-2026-09-24T22-20-22-024224Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-09-24 21:18:58 | [CVE-2026-93353](https://nvd.nist.gov/vuln/detail/CVE-2026-93353) | Medium | 6.0 | copyparty contains a volume restriction bypass vulnerability in its SFTP front end that allows authenticated SFTP users… |
| 2026-09-24 21:18:58 | [CVE-2026-95699](https://nvd.nist.gov/vuln/detail/CVE-2026-95699) | High | 8.4 | Prior to 9/18/2026, the iSteamX mobile application's AWS policy could grant authenticated users access to wildcard MQTT… |
| 2026-09-24 21:18:58 | [CVE-2026-97366](https://nvd.nist.gov/vuln/detail/CVE-2026-97366) | Low | 2.1 | A security flaw has been discovered in jhen0409 react-native-debugger up to 0.14.0. The impacted element is the functio… |
| 2026-09-24 21:18:58 | [CVE-2026-97368](https://nvd.nist.gov/vuln/detail/CVE-2026-97368) | Low | 2.1 | A weakness has been identified in chillzhuang SpringBlade up to 5.0.2. This affects the function UserServiceImpl.userIn… |
| 2026-09-24 22:17:02 | [CVE-2026-85491](https://nvd.nist.gov/vuln/detail/CVE-2026-85491) |  |  | Catalyst::Seal versions before 0.03 for Perl allow one request to disable a path or route a later one past an authoriza… |
| 2026-09-24 22:17:02 | [CVE-2026-87720](https://nvd.nist.gov/vuln/detail/CVE-2026-87720) | High | 7.6 | Incorrect Authorization (CWE-863) in project name normalization (ProjectUtil.stripGitSuffix) and ProjectCache eviction… |
| 2026-09-24 22:17:02 | [CVE-2026-87721](https://nvd.nist.gov/vuln/detail/CVE-2026-87721) | High | 8.7 | Uncontrolled Resource Consumption (CWE-400 / CWE-407) in the ANTLR 3 search query parser (QueryParser / Query.g) in Ger… |
| 2026-09-24 22:17:02 | [CVE-2026-87722](https://nvd.nist.gov/vuln/detail/CVE-2026-87722) | High | 8.7 | Uncontrolled Resource Consumption (CWE-400 / CWE-1333) in regex search query predicates (such as RegexProjectPredicate,… |
| 2026-09-24 22:17:02 | [CVE-2026-97636](https://nvd.nist.gov/vuln/detail/CVE-2026-97636) |  |  | Apache Airflow HashiCorp provider: the HashiCorp Vault secrets backend's team-scope guard can be bypassed with a user-c… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
