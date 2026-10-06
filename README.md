# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-06 13:18 UTC

New CVEs published between 2026-10-06 12:19 UTC and 2026-10-06 13:18 UTC.

[Full CSV](data/new-cves-2026-10-06T13-18-34-879958Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-10-06 13:16:46 | [CVE-2026-105834](https://nvd.nist.gov/vuln/detail/CVE-2026-105834) | High | 7.1 | Rundeck before 6.2.0 contains a path traversal vulnerability that allows users holding only the project configure ACL t… |
| 2026-10-06 13:16:46 | [CVE-2026-105835](https://nvd.nist.gov/vuln/detail/CVE-2026-105835) | Critical | 9.1 | PLANKA 2.2.0 through 2.2.1 fails to limit incorrect TOTP codes submitted to POST /api/access-tokens/verify-totp, allowi… |
| 2026-10-06 13:16:46 | [CVE-2026-105836](https://nvd.nist.gov/vuln/detail/CVE-2026-105836) | Medium | 5.3 | QloApps through 1.7.0 contains an authorization bypass vulnerability in AdminProductsController::ajaxProcessBulkUpdateR… |
| 2026-10-06 13:16:47 | [CVE-2026-105919](https://nvd.nist.gov/vuln/detail/CVE-2026-105919) | Medium | 5.5 | A vulnerability was found in Kusalkasilva Learning-Management-System up to ffeb873f8803f1e9664384ff75000c7da45466d2. Th… |
| 2026-10-06 13:16:47 | [CVE-2026-106016](https://nvd.nist.gov/vuln/detail/CVE-2026-106016) |  |  | Mitigation bypass in the File Handling component. This vulnerability was fixed in Firefox 157.0.1. |
| 2026-10-06 13:16:50 | [CVE-2026-82531](https://nvd.nist.gov/vuln/detail/CVE-2026-82531) | Critical | 9.2 | Smarty before 4.5.8 and 5.x before 5.8.5 contains a code injection vulnerability where the top-level nocache_hash is ne… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
