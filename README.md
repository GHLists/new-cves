# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-02 17:18 UTC

New CVEs published between 2026-10-02 16:19 UTC and 2026-10-02 17:18 UTC.

[Full CSV](data/new-cves-2026-10-02T17-18-33-192435Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-10-02 17:17:03 | [CVE-2026-104848](https://nvd.nist.gov/vuln/detail/CVE-2026-104848) | Critical | 9.5 | Tinypool is a minimal Node.js worker thread pool implementation. Prior to 2.1.1, Tinypool constructs ThreadPool.options… |
| 2026-10-02 17:17:03 | [CVE-2026-104849](https://nvd.nist.gov/vuln/detail/CVE-2026-104849) | Critical | 9.5 | Tinypool is a minimal Node.js worker thread pool implementation. Prior to 2.1.2, Tinypool reads filename from a caller-… |
| 2026-10-02 17:17:03 | [CVE-2026-104851](https://nvd.nist.gov/vuln/detail/CVE-2026-104851) | High | 8.8 | fsspec is a specification and Python implementation framework for filesystem interfaces. From 0.9.0 until 2026.6.0, fss… |
| 2026-10-02 17:17:03 | [CVE-2026-104853](https://nvd.nist.gov/vuln/detail/CVE-2026-104853) | Medium | 5.8 | Nx is a monorepo solution for TypeScript and polyglot codebases. From 13.10.0 until 22.7.10 and 23.2.1, Nx migration pl… |
| 2026-10-02 17:17:04 | [CVE-2026-104854](https://nvd.nist.gov/vuln/detail/CVE-2026-104854) | High | 8.5 | Nx is a monorepo solution for TypeScript and polyglot codebases. From 14.6.0 until 22.7.9 and 23.1.2, Nx creates Unix d… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
