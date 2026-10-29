# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-29 09:20 UTC

New CVEs published between 2026-10-29 08:20 UTC and 2026-10-29 09:20 UTC.

[Full CSV](data/new-cves-2026-10-29T09-20-22-915163Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-10-29 09:17:07 | [CVE-2026-114358](https://nvd.nist.gov/vuln/detail/CVE-2026-114358) | Critical | 9.3 | This vulnerability exists in the Radius Xenia M2M Platform due to insufficient validation of user supplied input in the… |
| 2026-10-29 09:17:08 | [CVE-2026-115303](https://nvd.nist.gov/vuln/detail/CVE-2026-115303) | Low | 3.7 | The Contact Form by Supsystic WordPress plugin before 1.11.1 does not strip CR/LF characters or re-validate submitted f… |
| 2026-10-29 09:17:08 | [CVE-2026-7190](https://nvd.nist.gov/vuln/detail/CVE-2026-7190) | Medium | 5.1 | A cross-site scripting (XSS) vulnerability in the ICTBroadcast software, which affects the demo environment. The vulner… |
| 2026-10-29 09:17:08 | [CVE-2026-85498](https://nvd.nist.gov/vuln/detail/CVE-2026-85498) | Low | 3.5 | A flaw was found in polkit. When processing input that begins with a null byte, an arithmetic error in the authenticati… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
