# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-19 04:18 UTC

New CVEs published between 2026-10-19 03:21 UTC and 2026-10-19 04:18 UTC.

[Full CSV](data/new-cves-2026-10-19T04-18-58-074299Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-10-19 04:17:03 | [CVE-2026-111440](https://nvd.nist.gov/vuln/detail/CVE-2026-111440) | High | 7.0 | 在 openGauss-connector-jdbc 的 pgjdbc/src/main/java/org/postgresql/log/LogFactory.java 中，LogFactory 根据 JDBC 连接参数中的 logger… |
| 2026-10-19 04:17:08 | [CVE-2026-112045](https://nvd.nist.gov/vuln/detail/CVE-2026-112045) | Low | 2.1 | A vulnerability was detected in donetick up to 0.1.82. The impacted element is the function CanDeleteHistory of the fil… |
| 2026-10-19 04:17:08 | [CVE-2026-112073](https://nvd.nist.gov/vuln/detail/CVE-2026-112073) | Low | 2.1 | A vulnerability was identified in Tencent ncnn up to 44b02dabdcf97499281a4692ebd65bad73dcf8b6. Affected by this vulnera… |
| 2026-10-19 04:17:08 | [CVE-2026-112074](https://nvd.nist.gov/vuln/detail/CVE-2026-112074) | Low | 2.1 | A security flaw has been discovered in Tencent ncnn up to 44b02dabdcf97499281a4692ebd65bad73dcf8b6. Affected by this is… |
| 2026-10-19 04:17:09 | [CVE-2026-112075](https://nvd.nist.gov/vuln/detail/CVE-2026-112075) | Low | 2.1 | A weakness has been identified in unslothai unsloth up to 0.1.501-beta. This affects the function FastSentenceTransform… |
| 2026-10-19 04:17:09 | [CVE-2026-112076](https://nvd.nist.gov/vuln/detail/CVE-2026-112076) | Low | 2.9 | A security vulnerability has been detected in alexta69 MeTube up to 2026.09.28. This vulnerability affects the function… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
