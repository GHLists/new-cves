# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-09-30 01:19 UTC

New CVEs published between 2026-09-30 00:19 UTC and 2026-09-30 01:19 UTC.

[Full CSV](data/new-cves-2026-09-30T01-19-35-740429Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-09-30 01:16:35 | [CVE-2026-102804](https://nvd.nist.gov/vuln/detail/CVE-2026-102804) | Medium | 5.5 | A vulnerability was detected in Nothings stb up to 2c980bb59875b0d32144a71867fbdebb2f77cd20. The impacted element is th… |
| 2026-09-30 01:16:36 | [CVE-2026-102805](https://nvd.nist.gov/vuln/detail/CVE-2026-102805) | Medium | 5.5 | A flaw has been found in Nothings stb up to 1.16. This affects the function stbi_write_png_to_mem/stbi_write_jpg_core/s… |
| 2026-09-30 01:16:36 | [CVE-2026-102842](https://nvd.nist.gov/vuln/detail/CVE-2026-102842) | Low | 2.1 | A vulnerability was identified in gedelumbung HospitalManagement up to c2d45543789a3887067d3915f69d44cfc2cf76a8. Affect… |
| 2026-09-30 01:16:36 | [CVE-2026-103053](https://nvd.nist.gov/vuln/detail/CVE-2026-103053) | Medium | 5.3 | AiSOC versions 9.0.0 before 12.0.0 fail to enforce authentication on the response-action API endpoints when AISOC_DEV_M… |
| 2026-09-30 01:16:36 | [CVE-2026-103054](https://nvd.nist.gov/vuln/detail/CVE-2026-103054) | High | 7.1 | AiSOC versions before 12.0.0 contain an authorization bypass vulnerability in the MSSP module that allows authenticated… |
| 2026-09-30 01:16:36 | [CVE-2026-103055](https://nvd.nist.gov/vuln/detail/CVE-2026-103055) | High | 8.7 | AiSOC versions 7.5.0 before 12.0.0 use a hard-coded constant for JWT verification in the realtime WebSocket and SSE ser… |
| 2026-09-30 01:16:37 | [CVE-2026-103056](https://nvd.nist.gov/vuln/detail/CVE-2026-103056) | Critical | 9.4 | AiSOC versions 7.2.0 before 12.0.0 contain a command injection vulnerability in the actions service that builds CrowdSt… |
| 2026-09-30 01:16:37 | [CVE-2026-103057](https://nvd.nist.gov/vuln/detail/CVE-2026-103057) | Medium | 5.3 | AiSOC versions 5.1.0 before 12.0.0 contain an authentication bypass vulnerability in the realtime service internal endp… |
| 2026-09-30 01:16:37 | [CVE-2026-51936](https://nvd.nist.gov/vuln/detail/CVE-2026-51936) | Low | 2.1 | Zetetic SQLCipher before 4.15.0 allows SQL injection. The sqlcipher_export convenience function can be used to copy the… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
