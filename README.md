# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-11-20 22:21 UTC

New CVEs published between 2026-11-20 21:18 UTC and 2026-11-20 22:21 UTC.

[Full CSV](data/new-cves-2026-11-20T22-21-05-810189Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-11-20 22:17:48 | [CVE-2026-128113](https://nvd.nist.gov/vuln/detail/CVE-2026-128113) |  |  | Rejected reason: ** REJECT ** DO NOT USE THIS CANDIDATE NUMBER. Reason: This candidate was issued in error. Notes: All… |
| 2026-11-20 22:17:50 | [CVE-2026-133835](https://nvd.nist.gov/vuln/detail/CVE-2026-133835) | Medium | 5.5 | A flaw has been found in hankcs HanLP up to 2.1.6. Impacted is the function uncompress of the file hanlp/utils/io_util.… |
| 2026-11-20 22:17:50 | [CVE-2026-133836](https://nvd.nist.gov/vuln/detail/CVE-2026-133836) | Low | 2.1 | A vulnerability has been found in hankcs HanLP up to 2.1.6. The affected element is the function RNNLanguageModel.load_… |
| 2026-11-20 22:17:50 | [CVE-2026-133937](https://nvd.nist.gov/vuln/detail/CVE-2026-133937) | Medium | 5.5 | A flaw has been found in highlight highlight.js up to 11.12.0. The affected element is the function hljs.highlight of t… |
| 2026-11-20 22:17:50 | [CVE-2026-134136](https://nvd.nist.gov/vuln/detail/CVE-2026-134136) | Medium | 4.8 | OceanWP WordPress Theme before 4.2.9 contains a stored cross-site scripting vulnerability in the oceanwp_edd_terms_list… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
