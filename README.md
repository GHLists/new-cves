# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-09-28 12:19 UTC

New CVEs published between 2026-09-28 11:18 UTC and 2026-09-28 12:19 UTC.

[Full CSV](data/new-cves-2026-09-28T12-19-00-341808Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-09-28 12:17:35 | [CVE-2026-101052](https://nvd.nist.gov/vuln/detail/CVE-2026-101052) | Medium | 5.5 | A security vulnerability has been detected in refly-ai refly up to 1.1.0. This issue affects some unknown processing of… |
| 2026-09-28 12:17:36 | [CVE-2026-101053](https://nvd.nist.gov/vuln/detail/CVE-2026-101053) | Medium | 5.5 | A vulnerability was determined in Thinkware U3000 up to 1.02.04. This impacts the function PUT_FILE of the file /tmp/wp… |
| 2026-09-28 12:17:36 | [CVE-2026-101054](https://nvd.nist.gov/vuln/detail/CVE-2026-101054) | Medium | 5.5 | A vulnerability was identified in Thinkware U3000 up to 1.02.04. Affected is the function get_file of the file /tmp/wpa… |
| 2026-09-28 12:17:36 | [CVE-2026-12264](https://nvd.nist.gov/vuln/detail/CVE-2026-12264) | High | 8.8 | Zohocorp ManageEngine DDI Central versions before 6201 are vulnerable to Arbitrary file write via HA Failover Config sy… |
| 2026-09-28 12:17:36 | [CVE-2026-19444](https://nvd.nist.gov/vuln/detail/CVE-2026-19444) | Medium | 6.5 | A path traversal vulnerability was discovered in the Kubernetes kubectl client's kubectl cp command on Windows. When co… |
| 2026-09-28 12:17:40 | [CVE-2026-78424](https://nvd.nist.gov/vuln/detail/CVE-2026-78424) | High | 8.8 | Improper parameter handling in NeuVector allows any authenticated user who holds the namespaced Runtime Policies (write… |
| 2026-09-28 12:17:41 | [CVE-2026-87752](https://nvd.nist.gov/vuln/detail/CVE-2026-87752) | Medium | 6.1 | Improper neutralization of input during web page generation ('cross-site scripting') vulnerability in Rolantis Informat… |
| 2026-09-28 12:17:41 | [CVE-2026-91043](https://nvd.nist.gov/vuln/detail/CVE-2026-91043) | High | 8.2 | Allocation of Resources Without Limits or Throttling vulnerability in elixir-mint mint allows a malicious HTTP/2 server… |
| 2026-09-28 12:17:41 | [CVE-2026-92103](https://nvd.nist.gov/vuln/detail/CVE-2026-92103) | Medium | 6.3 | Allocation of Resources Without Limits or Throttling vulnerability in elixir-mint mint allows a malicious HTTP/2 server… |
| 2026-09-28 12:17:42 | [CVE-2026-94194](https://nvd.nist.gov/vuln/detail/CVE-2026-94194) | Medium | 6.3 | Inconsistent Interpretation of HTTP Requests ('HTTP Request/Response Smuggling') vulnerability in elixir-mint mint allo… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
