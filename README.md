# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-02 21:18 UTC

New CVEs published between 2026-10-02 20:18 UTC and 2026-10-02 21:18 UTC.

[Full CSV](data/new-cves-2026-10-02T21-18-38-777408Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-10-02 21:16:54 | [CVE-2026-104055](https://nvd.nist.gov/vuln/detail/CVE-2026-104055) | Medium | 5.3 | The postgresql-operator charm runs a Prometheus postgres_exporter to collect database metrics using a dedicated "monito… |
| 2026-10-02 21:16:54 | [CVE-2026-104874](https://nvd.nist.gov/vuln/detail/CVE-2026-104874) | Medium | 5.3 | Multidict is an implementation of a multidict data structure. From 6.7.0 until 6.9.1, the C extension's items-view refl… |
| 2026-10-02 21:16:56 | [CVE-2026-75937](https://nvd.nist.gov/vuln/detail/CVE-2026-75937) | Critical | 9.4 | A specially crafted HTTP POST request to the web administration interface allows an unauthenticated attacker to execute… |
| 2026-10-02 21:16:56 | [CVE-2026-82041](https://nvd.nist.gov/vuln/detail/CVE-2026-82041) | Medium | 6.5 | UTMStack before 11.2.16 contains a missing authorization vulnerability in UTMIncidentCommandWebsocket.processCommand(),… |
| 2026-10-02 21:16:56 | [CVE-2026-82042](https://nvd.nist.gov/vuln/detail/CVE-2026-82042) | Critical | 9.3 | UTMStack before 11.2.16 contains an authentication bypass vulnerability that allows remote attackers to gain full admin… |
| 2026-10-02 21:16:56 | [CVE-2026-82043](https://nvd.nist.gov/vuln/detail/CVE-2026-82043) | Medium | 6.9 | UTMStack before 11.2.16 contains an account enumeration vulnerability that allows unauthenticated attackers to determin… |
| 2026-10-02 21:16:56 | [CVE-2026-82044](https://nvd.nist.gov/vuln/detail/CVE-2026-82044) | Medium | 6.3 | UTMStack before 11.2.16 contains a server-side request forgery vulnerability that allows authenticated attackers to mak… |
| 2026-10-02 21:16:57 | [CVE-2026-82045](https://nvd.nist.gov/vuln/detail/CVE-2026-82045) | High | 7.1 | UTMStack before 11.2.16 contains a JPQL injection vulnerability that allows authenticated attackers to read arbitrary e… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
