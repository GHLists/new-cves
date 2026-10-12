# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-12 02:20 UTC

New CVEs published between 2026-10-12 01:20 UTC and 2026-10-12 02:20 UTC.

[Full CSV](data/new-cves-2026-10-12T02-20-43-988658Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-10-12 02:16:56 | [CVE-2026-108782](https://nvd.nist.gov/vuln/detail/CVE-2026-108782) | Low | 2.1 | A weakness has been identified in erzhongxmu JEEWMS up to 2026.09.27-W39. Affected by this issue is the function Common… |
| 2026-10-12 02:16:56 | [CVE-2026-108783](https://nvd.nist.gov/vuln/detail/CVE-2026-108783) | Medium | 5.5 | A security vulnerability has been detected in PRVTPRO Amnezia-Web-Panel up to 1.6.2/1.7.2. This affects an unknown part… |
| 2026-10-12 02:16:56 | [CVE-2026-108784](https://nvd.nist.gov/vuln/detail/CVE-2026-108784) | Medium | 5.5 | A vulnerability was detected in macrozheng mall up to 1.0.3. This vulnerability affects the function AlipayServiceImpl.… |
| 2026-10-12 02:16:56 | [CVE-2026-108785](https://nvd.nist.gov/vuln/detail/CVE-2026-108785) | Low | 2.1 | A flaw has been found in macrozheng mall up to 1.0.3. This issue affects the function JwtTokenUtil.refreshHeadToken of… |
| 2026-10-12 02:16:56 | [CVE-2026-108786](https://nvd.nist.gov/vuln/detail/CVE-2026-108786) | Low | 2.1 | A vulnerability has been found in houtini-ai seo-crawler-mcp up to 2.1.5. Impacted is the function run_seo_audit of the… |
| 2026-10-12 02:16:56 | [CVE-2026-108787](https://nvd.nist.gov/vuln/detail/CVE-2026-108787) | Low | 2.1 | A vulnerability was found in houtini-ai voice-analyser-mcp up to 2.1.1. The affected element is the function fetch of t… |
| 2026-10-12 02:16:57 | [CVE-2026-108788](https://nvd.nist.gov/vuln/detail/CVE-2026-108788) | Low | 1.9 | A vulnerability was determined in deepseek-ai deepseek-harness up to 0.1.1-rc.2. The impacted element is the function s… |
| 2026-10-12 02:16:57 | [CVE-2026-108980](https://nvd.nist.gov/vuln/detail/CVE-2026-108980) | High | 8.8 | Blinko through 1.8.8 allows directory traversal, overwriting startup files as root, via installPlugin. It builds the pl… |
| 2026-10-12 02:16:57 | [CVE-2026-66085](https://nvd.nist.gov/vuln/detail/CVE-2026-66085) | Medium | 5.5 | In modem, there is a possible information disclosure due to missing filtering of sensitive data in crash dumps. This co… |
| 2026-10-12 02:16:57 | [CVE-2026-66086](https://nvd.nist.gov/vuln/detail/CVE-2026-66086) | Critical | 9.8 | In the modem OTA stack, there is a possible stack-based buffer overflow due to improper validation of scheduling inform… |
| 2026-10-12 02:16:57 | [CVE-2026-87765](https://nvd.nist.gov/vuln/detail/CVE-2026-87765) | Medium | 5.5 | In the kernel apsys DVFS driver, there is a possible out-of-bounds read or hardware register corruption due to improper… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
