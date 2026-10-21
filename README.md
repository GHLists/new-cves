# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-21 11:18 UTC

New CVEs published between 2026-10-21 10:19 UTC and 2026-10-21 11:18 UTC.

[Full CSV](data/new-cves-2026-10-21T11-18-59-078897Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-10-21 11:17:07 | [CVE-2026-41114](https://nvd.nist.gov/vuln/detail/CVE-2026-41114) |  |  | Uncontrolled Resource Consumption vulnerability in Apache IoTDB JDBC driver. This issue affects Apache IoTDB JDBC drive… |
| 2026-10-21 11:17:07 | [CVE-2026-58663](https://nvd.nist.gov/vuln/detail/CVE-2026-58663) |  |  | An authentication bypass vulnerability exists in Apache IoTDB's Thrift RPC service This issue affects Apache IoTDB: fro… |
| 2026-10-21 11:17:09 | [CVE-2026-87095](https://nvd.nist.gov/vuln/detail/CVE-2026-87095) | Critical | 9.1 | Sensitive information disclosure and manipulation due to improper authorization checks. The following products are affe… |
| 2026-10-21 11:17:09 | [CVE-2026-87096](https://nvd.nist.gov/vuln/detail/CVE-2026-87096) | Low | 3.3 | Sensitive information disclosure and manipulation due to improper authorization checks. The following products are affe… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
