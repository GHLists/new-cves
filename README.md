# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-15 02:19 UTC

New CVEs published between 2026-10-15 01:19 UTC and 2026-10-15 02:19 UTC.

[Full CSV](data/new-cves-2026-10-15T02-19-32-951096Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-10-15 01:19:27 | [CVE-2026-0993](https://nvd.nist.gov/vuln/detail/CVE-2026-0993) | High | 8.7 | SODOLA SL902-SWTGW124AS firmware before 200.2.12 contains a buffer overflow vulnerability that allows unauthenticated r… |
| 2026-10-15 01:19:27 | [CVE-2026-110810](https://nvd.nist.gov/vuln/detail/CVE-2026-110810) | Low | 0.9 | A vulnerability was detected in ggml-org whisper.cpp up to 1.9.4. This affects the function whisper_model_load of the f… |
| 2026-10-15 02:18:37 | [CVE-2026-109430](https://nvd.nist.gov/vuln/detail/CVE-2026-109430) | High | 8.7 | Ellucian WebAdvisor 3.2 contains an unauthenticated XML External Entity (XXE) injection vulnerability that allows remot… |
| 2026-10-15 02:18:37 | [CVE-2026-110904](https://nvd.nist.gov/vuln/detail/CVE-2026-110904) | Medium | 5.3 | ApostropheCMS before 4.33.0 allows authentication bypass for REST API page reading, as demonstrated by a /api/v1/@apost… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
