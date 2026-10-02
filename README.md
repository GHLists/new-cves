# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-02 23:19 UTC

New CVEs published between 2026-10-02 22:18 UTC and 2026-10-02 23:19 UTC.

[Full CSV](data/new-cves-2026-10-02T23-19-05-04633Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-10-02 23:16:57 | [CVE-2026-105048](https://nvd.nist.gov/vuln/detail/CVE-2026-105048) | Medium | 4.0 | The Playground feature of Zilliz Attu before 3.0.0 allows SSRF (proxying of requests to private IP addresses). |
| 2026-10-02 23:16:57 | [CVE-2026-105049](https://nvd.nist.gov/vuln/detail/CVE-2026-105049) | Medium | 5.8 | Zilliz Attu before 3.0.0 has a Playground feature that does not require authentication for proxying arbitrary HTTP and… |
| 2026-10-02 23:16:58 | [CVE-2026-105050](https://nvd.nist.gov/vuln/detail/CVE-2026-105050) | High | 7.1 | PeaZip before 11.3.0, in a non-default configuration, is vulnerable to OS command injection via a filename in an archiv… |
| 2026-10-02 23:16:58 | [CVE-2026-105051](https://nvd.nist.gov/vuln/detail/CVE-2026-105051) | Low | 1.9 | Denuvo Anti-Tamper through 2026-03-04 allows bypass of a hypervisor presence check via CPUID interception (SimpleSvm.sy… |
| 2026-10-02 23:16:58 | [CVE-2026-84411](https://nvd.nist.gov/vuln/detail/CVE-2026-84411) | Critical | 9.3 | The web management service in affected RouterOS versions contains an integer underflow in its HTTP request body handlin… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
