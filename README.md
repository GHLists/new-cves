# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-13 03:19 UTC

New CVEs published between 2026-10-13 02:19 UTC and 2026-10-13 03:19 UTC.

[Full CSV](data/new-cves-2026-10-13T03-19-36-793847Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-10-13 03:16:40 | [CVE-2026-108957](https://nvd.nist.gov/vuln/detail/CVE-2026-108957) | Low | 2.1 | A security flaw has been discovered in TinyLLaVA TinyLLaVA_Factory up to 1abc6ac5e76a68d0fd087a071b56da968e69ca9b. The… |
| 2026-10-13 03:16:40 | [CVE-2026-108958](https://nvd.nist.gov/vuln/detail/CVE-2026-108958) | Low | 2.1 | A weakness has been identified in TensorLayer up to 2.2.4. This affects the function load_hdf5_graph of the file tensor… |
| 2026-10-13 03:16:40 | [CVE-2026-108959](https://nvd.nist.gov/vuln/detail/CVE-2026-108959) | Low | 2.1 | A security vulnerability has been detected in itsourcecode Online Cake Ordering System 1.0. This impacts an unknown fun… |
| 2026-10-13 03:16:40 | [CVE-2026-108960](https://nvd.nist.gov/vuln/detail/CVE-2026-108960) | Low | 1.9 | A vulnerability was detected in Tiiny-AI PowerInfer up to 8bd56d69906c9d2dba4d3bf6899763401e01a9a4. Affected is the fun… |
| 2026-10-13 03:16:40 | [CVE-2026-109786](https://nvd.nist.gov/vuln/detail/CVE-2026-109786) | Medium | 5.3 | In fail2ban 0.10.5 through 1.1.1 before ddd879d, the sshd filter (config/filter.d/sshd.conf) accepts an "on <token>" su… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
