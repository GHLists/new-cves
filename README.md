# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-23 18:19 UTC

New CVEs published between 2026-10-23 17:20 UTC and 2026-10-23 18:19 UTC.

[Full CSV](data/new-cves-2026-10-23T18-19-53-143272Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-10-23 18:17:20 | [CVE-2026-110975](https://nvd.nist.gov/vuln/detail/CVE-2026-110975) | High | 7.4 | A flaw was found in Kruize Autotune. Its REST API ships without an authentication layer, and the endpoints that return… |
| 2026-10-23 18:17:21 | [CVE-2026-115567](https://nvd.nist.gov/vuln/detail/CVE-2026-115567) | Medium | 5.8 | Tokio is a runtime for writing applications with Rust. In 1.54.0, a race condition between tokio::time::Interval::poll_… |
| 2026-10-23 18:17:21 | [CVE-2026-115812](https://nvd.nist.gov/vuln/detail/CVE-2026-115812) | Critical | 9.3 | Relative path traversal during model archive extraction in Amazon Web Services Multi Model Server 1.1.11 and earlier mi… |
| 2026-10-23 18:17:21 | [CVE-2026-115813](https://nvd.nist.gov/vuln/detail/CVE-2026-115813) | Medium | 6.9 | Server-side request forgery in the model download path in Amazon Web Services Multi Model Server 1.1.11 and earlier mig… |
| 2026-10-23 18:17:21 | [CVE-2026-115863](https://nvd.nist.gov/vuln/detail/CVE-2026-115863) | High | 7.6 | ConnMan through 2.0 has a stack-based buffer overflow via a DHCPv6 Reply message. This occurs in get_domains in gdhcp/c… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
