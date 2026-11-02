# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-11-02 22:19 UTC

New CVEs published between 2026-11-02 21:18 UTC and 2026-11-02 22:19 UTC.

[Full CSV](data/new-cves-2026-11-02T22-19-47-81616Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-11-02 22:17:18 | [CVE-2026-115215](https://nvd.nist.gov/vuln/detail/CVE-2026-115215) | High | 8.7 | In Eclipse ThreadX NetX Duo versions 6.0 through 6.5.2.202603a, the NetX Secure DTLS server allocates a session from it… |
| 2026-11-02 22:17:18 | [CVE-2026-115403](https://nvd.nist.gov/vuln/detail/CVE-2026-115403) | High | 8.2 | In Eclipse ThreadX NetX Duo versions 6.0 through 6.5.2.202603a, built with BSD raw socket and IPv6 support, the IPv6 ra… |
| 2026-11-02 22:17:19 | [CVE-2026-116635](https://nvd.nist.gov/vuln/detail/CVE-2026-116635) | Medium | 6.9 | Improper limitation of a pathname to a restricted directory in the deployment status component of the AWS Serverless MC… |
| 2026-11-02 22:17:20 | [CVE-2026-120091](https://nvd.nist.gov/vuln/detail/CVE-2026-120091) | High | 8.7 | Temporal Server compiles a Worker Controller Instance module, go.temporal.io/auto-scaled-workers, into its Worker Servi… |
| 2026-11-02 22:17:21 | [CVE-2026-120740](https://nvd.nist.gov/vuln/detail/CVE-2026-120740) | Low | 2.0 | A flaw was found in hivex. By supplying a specially crafted Windows registry hive file, an attacker can trigger an out-… |
| 2026-11-02 22:17:23 | [CVE-2026-86596](https://nvd.nist.gov/vuln/detail/CVE-2026-86596) | Critical | 9.8 | The s2Member plugin for WordPress is vulnerable to Remote Code Execution in all versions up to, and including, <= 26092… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
