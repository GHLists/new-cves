# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-11-23 10:21 UTC

New CVEs published between 2026-11-23 09:18 UTC and 2026-11-23 10:21 UTC.

[Full CSV](data/new-cves-2026-11-23T10-21-55-216422Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-11-23 10:17:15 | [CVE-2026-118888](https://nvd.nist.gov/vuln/detail/CVE-2026-118888) | Low | 3.3 | ZTE Z80 Ultra product has an improper access control vulnerability. Successful exploitation of this vulnerability may a… |
| 2026-11-23 10:17:15 | [CVE-2026-121613](https://nvd.nist.gov/vuln/detail/CVE-2026-121613) | Critical | 9.3 | Missing authentication and authorization on an exposed interface allows an unauthenticated remote attacker to send arbi… |
| 2026-11-23 10:17:15 | [CVE-2026-128979](https://nvd.nist.gov/vuln/detail/CVE-2026-128979) | Medium | 6.0 | Improper certificate validation vulnerability in Estonian Information System Authority (RIA) libdigidocpp, Estonian Inf… |
| 2026-11-23 10:17:15 | [CVE-2026-134883](https://nvd.nist.gov/vuln/detail/CVE-2026-134883) | Medium | 5.1 | A security vulnerability has been detected in osCommerce 4.14.63493. Impacted is the function actionOrdersbatch of the… |
| 2026-11-23 10:17:15 | [CVE-2026-134884](https://nvd.nist.gov/vuln/detail/CVE-2026-134884) | Medium | 5.1 | A vulnerability was detected in osCommerce 4.14.63493. The affected element is an unknown function of the component Bac… |
| 2026-11-23 10:17:16 | [CVE-2026-134885](https://nvd.nist.gov/vuln/detail/CVE-2026-134885) | Medium | 6.9 | A flaw has been found in osCommerce up to 4.14.63493. The impacted element is the function actionSuccess of the file li… |
| 2026-11-23 10:17:16 | [CVE-2026-80466](https://nvd.nist.gov/vuln/detail/CVE-2026-80466) | High | 8.7 | A vulnerability in the Web-Based Management (WBM) routing configuration allows a low-privileged remote attacker to inje… |
| 2026-11-23 10:17:16 | [CVE-2026-88850](https://nvd.nist.gov/vuln/detail/CVE-2026-88850) | High | 7.2 | The Web-Based Management (WBM) authorization model does not properly enforce permissions for all PROFIBUS configuration… |
| 2026-11-23 10:17:16 | [CVE-2026-94252](https://nvd.nist.gov/vuln/detail/CVE-2026-94252) | Medium | 4.9 | An unauthenticated stored and reflected cross-site scripting (XSS) vulnerability in the embedded web interface of Front… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
