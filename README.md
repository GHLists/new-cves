# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-19 05:19 UTC

New CVEs published between 2026-10-19 04:18 UTC and 2026-10-19 05:19 UTC.

[Full CSV](data/new-cves-2026-10-19T05-19-12-642859Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-10-19 05:17:04 | [CVE-2026-112077](https://nvd.nist.gov/vuln/detail/CVE-2026-112077) | Medium | 6.3 | A vulnerability was detected in radareorg radare2 6.2.0/6.2.2. This issue affects the function r_core_cmd_str_pipe in t… |
| 2026-10-19 05:17:04 | [CVE-2026-112078](https://nvd.nist.gov/vuln/detail/CVE-2026-112078) | Low | 2.1 | A flaw has been found in RVC-Project Retrieval-based-Voice-Conversion-WebUI up to 2.3.260718. Impacted is the function… |
| 2026-10-19 05:17:04 | [CVE-2026-112079](https://nvd.nist.gov/vuln/detail/CVE-2026-112079) | Low | 2.1 | A vulnerability has been found in hankcs HanLP up to 2.1.0-beta.64. The affected element is the function load_word2vec_… |
| 2026-10-19 05:17:04 | [CVE-2026-112080](https://nvd.nist.gov/vuln/detail/CVE-2026-112080) | Low | 2.1 | A vulnerability was found in LlamaChinese Llama-Chinese up to 6fa0fffb0dd82fe3cfaa1449ee54a5806d26ae9b. The impacted el… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
