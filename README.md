# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-19 08:19 UTC

New CVEs published between 2026-10-19 07:18 UTC and 2026-10-19 08:19 UTC.

[Full CSV](data/new-cves-2026-10-19T08-19-40-337095Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-10-19 08:17:02 | [CVE-2026-111439](https://nvd.nist.gov/vuln/detail/CVE-2026-111439) | Medium | 4.3 | 在 openGauss-server的 src/common/backend/utils/adt/genfile.cpp 模块中，内置函数 pg_read_binary_file_blocks() 存在权限校验逻辑缺陷。该函数在入口处仅校… |
| 2026-10-19 08:17:02 | [CVE-2026-112090](https://nvd.nist.gov/vuln/detail/CVE-2026-112090) | Low | 2.1 | A vulnerability was detected in Dav-ee dairy-management-system 31ace9692d1e1e6d64339a42c463b361319c615c/f31a584c3330c01… |
| 2026-10-19 08:17:03 | [CVE-2026-112091](https://nvd.nist.gov/vuln/detail/CVE-2026-112091) | Medium | 5.5 | A flaw has been found in Dav-ee dairy-management-system 31ace9692d1e1e6d64339a42c463b361319c615c/f31a584c3330c013b61f8b… |
| 2026-10-19 08:17:03 | [CVE-2026-112092](https://nvd.nist.gov/vuln/detail/CVE-2026-112092) | Low | 2.1 | A flaw has been found in subhajitkhan online-clinic-management-system up to e9ee77a8827a1446220fa07ee693dc4d9a29a578. T… |
| 2026-10-19 08:17:03 | [CVE-2026-112093](https://nvd.nist.gov/vuln/detail/CVE-2026-112093) | Low | 2.1 | A vulnerability has been found in subhajitkhan online-clinic-management-system up to e9ee77a8827a1446220fa07ee693dc4d9a… |
| 2026-10-19 08:17:03 | [CVE-2026-112094](https://nvd.nist.gov/vuln/detail/CVE-2026-112094) | Low | 2.0 | A security vulnerability has been detected in michaelrsweet mxml 4.0.5/4.0.6. This affects the function mxml_load_data… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
