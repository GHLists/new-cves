# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-12 03:18 UTC

New CVEs published between 2026-10-12 02:20 UTC and 2026-10-12 03:18 UTC.

[Full CSV](data/new-cves-2026-10-12T03-18-50-339702Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-10-12 03:17:17 | [CVE-2026-107437](https://nvd.nist.gov/vuln/detail/CVE-2026-107437) | Medium | 6.2 | GV-E-Map Server V18.2.0A contains a plaintext database password embedded within an application component. The credentia… |
| 2026-10-12 03:17:17 | [CVE-2026-108789](https://nvd.nist.gov/vuln/detail/CVE-2026-108789) | Low | 2.0 | A vulnerability was identified in deepseek-ai deepseek-harness up to 0.1.1-rc.2. This affects the function agent of the… |
| 2026-10-12 03:17:18 | [CVE-2026-108790](https://nvd.nist.gov/vuln/detail/CVE-2026-108790) | Low | 2.0 | A security flaw has been discovered in westboy CicadasCMS up to 2431154dac8d0735e04f1fd2a3c3556668fc8dab. This impacts… |
| 2026-10-12 03:17:18 | [CVE-2026-108791](https://nvd.nist.gov/vuln/detail/CVE-2026-108791) | Low | 2.1 | A weakness has been identified in westboy CicadasCMS up to 2431154dac8d0735e04f1fd2a3c3556668fc8dab. Affected is the fu… |
| 2026-10-12 03:17:18 | [CVE-2026-108794](https://nvd.nist.gov/vuln/detail/CVE-2026-108794) | Medium | 5.3 | A security vulnerability has been detected in ZKTeco BioTime 9.5.6 Build 20260130.3206. Affected by this vulnerability… |
| 2026-10-12 03:17:18 | [CVE-2026-108981](https://nvd.nist.gov/vuln/detail/CVE-2026-108981) | Low | 3.6 | ngx_cache_purge before 3.0.4 can allow file deletion via a symlink attack in certain situations where nginx and a serve… |
| 2026-10-12 03:17:18 | [CVE-2026-108982](https://nvd.nist.gov/vuln/detail/CVE-2026-108982) | High | 7.2 | VeraCrypt 1.26.29 (FUSE-T build) on macOS sometimes allows unintended access to decrypted data. It does not terminate t… |
| 2026-10-12 03:17:18 | [CVE-2026-108985](https://nvd.nist.gov/vuln/detail/CVE-2026-108985) | High | 7.1 | ZDR decoding in libnfs through 6.0.2 before 7613236 has an out-of-bounds write related to lib/libnfs-zdr.c with libnfs_… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
