# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-11-20 07:18 UTC

New CVEs published between 2026-11-20 06:21 UTC and 2026-11-20 07:18 UTC.

[Full CSV](data/new-cves-2026-11-20T07-18-49-910197Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-11-20 07:16:50 | [CVE-2026-129971](https://nvd.nist.gov/vuln/detail/CVE-2026-129971) | High | 8.7 | A buffer overflow vulnerability exists in the SNMP service of the Ethernet Remote I/Os products. An unauthenticated rem… |
| 2026-11-20 07:16:55 | [CVE-2026-129972](https://nvd.nist.gov/vuln/detail/CVE-2026-129972) | High | 8.7 | A buffer overflow vulnerability exists in the web management service of the Ethernet Remote I/Os products. An unauthent… |
| 2026-11-20 07:16:58 | [CVE-2026-133491](https://nvd.nist.gov/vuln/detail/CVE-2026-133491) | Medium | 5.3 | A flaw has been found in Konstanty libmodplug up to 0.8.9.1. The affected element is the function abc_add_drum of the f… |
| 2026-11-20 07:17:05 | [CVE-2026-133492](https://nvd.nist.gov/vuln/detail/CVE-2026-133492) | Medium | 5.5 | A vulnerability has been found in TRENDnet TEW-657BRM 1.00.1. The impacted element is an unknown function of the file /… |
| 2026-11-20 07:17:10 | [CVE-2026-133493](https://nvd.nist.gov/vuln/detail/CVE-2026-133493) | Critical | 9.3 | A vulnerability was identified in D-Link DIR-600L 2.17b02. Affected is the function genacgi_main of the file gena.cgi o… |
| 2026-11-20 07:17:14 | [CVE-2026-133495](https://nvd.nist.gov/vuln/detail/CVE-2026-133495) | Medium | 5.5 | A weakness has been identified in D-Link DIR-600L 2.17b02. Affected by this issue is some unknown functionality of the… |
| 2026-11-20 07:17:15 | [CVE-2026-133577](https://nvd.nist.gov/vuln/detail/CVE-2026-133577) | High | 7.7 | A flaw was found in the Kuadrant WebAssembly (WASM) shim shipped in Red Hat Connectivity Link 1.5. When a TokenRateLimi… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
