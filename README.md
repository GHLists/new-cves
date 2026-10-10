# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-10 11:18 UTC

New CVEs published between 2026-10-10 10:18 UTC and 2026-10-10 11:18 UTC.

[Full CSV](data/new-cves-2026-10-10T11-18-38-946193Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-10-10 11:17:34 | [CVE-2026-103501](https://nvd.nist.gov/vuln/detail/CVE-2026-103501) |  |  | Heap buffer overflow in the HLL sketch deserialization of Apache DataSketches C++ (repo: datasketches-cpp). When deseri… |
| 2026-10-10 11:17:35 | [CVE-2026-103513](https://nvd.nist.gov/vuln/detail/CVE-2026-103513) |  |  | Out-of-bounds read and write in the CPC sketch deserialization of Apache DataSketches C++ (repo: datasketches-cpp). A c… |
| 2026-10-10 11:17:35 | [CVE-2026-103635](https://nvd.nist.gov/vuln/detail/CVE-2026-103635) |  |  | Out-of-bounds read in the compact Theta sketch deserialization of Apache DataSketches C++ (repo: datasketches-cpp). com… |
| 2026-10-10 11:17:36 | [CVE-2026-103636](https://nvd.nist.gov/vuln/detail/CVE-2026-103636) |  |  | Out-of-bounds read in the VarOpt union deserialization of Apache DataSketches C++ (repo: datasketches-cpp). var_opt_uni… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
