# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-11-25 05:18 UTC

New CVEs published between 2026-11-25 04:19 UTC and 2026-11-25 05:18 UTC.

[Full CSV](data/new-cves-2026-11-25T05-18-45-285051Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-11-25 05:18:27 | [CVE-2026-118898](https://nvd.nist.gov/vuln/detail/CVE-2026-118898) | High | 8.7 | Deserialization of Untrusted Data vulnerability in lasp-lang partisan allows an unauthenticated remote attacker to abor… |
| 2026-11-25 05:18:29 | [CVE-2026-130336](https://nvd.nist.gov/vuln/detail/CVE-2026-130336) | High | 7.5 | Improper Neutralization of Directives in Dynamically Evaluated Code ('Eval Injection') in the HWBridge custom methods c… |
| 2026-11-25 05:18:30 | [CVE-2026-132145](https://nvd.nist.gov/vuln/detail/CVE-2026-132145) | Medium | 5.9 | A flaw was found in rsyslog. When using the Datagram Transport Layer Security (DTLS) output module (omdtls) configured… |
| 2026-11-25 05:18:35 | [CVE-2026-136547](https://nvd.nist.gov/vuln/detail/CVE-2026-136547) | Critical | 9.3 | A vulnerability was determined in Tenda RX3 16.03.13.11_multi. Impacted is the function R7WebsSecurityHandler of the co… |
| 2026-11-25 05:18:35 | [CVE-2026-136679](https://nvd.nist.gov/vuln/detail/CVE-2026-136679) | Low | 3.3 | NULL Pointer Dereference vulnerability in Samsung Open Source Walrus allows Input Data Manipulation. |
| 2026-11-25 05:18:35 | [CVE-2026-136680](https://nvd.nist.gov/vuln/detail/CVE-2026-136680) | Medium | 5.5 | Reachable Assertion vulnerability in Samsung Open Source Walrus allows Input Data Manipulation. |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
