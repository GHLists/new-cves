# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-11-23 04:20 UTC

New CVEs published between 2026-11-23 03:18 UTC and 2026-11-23 04:20 UTC.

[Full CSV](data/new-cves-2026-11-23T04-20-35-097694Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-11-23 04:17:58 | [CVE-2026-129830](https://nvd.nist.gov/vuln/detail/CVE-2026-129830) | Medium | 4.7 | When the rsyslog's `imuxsock` is parsing the TAG field from a message with a accepted shorter timestamp, the cursor use… |
| 2026-11-23 04:17:58 | [CVE-2026-134850](https://nvd.nist.gov/vuln/detail/CVE-2026-134850) | Medium | 6.9 | A security vulnerability has been detected in aceberg WatchYourLAN up to 2.1.4. Affected by this issue is the function… |
| 2026-11-23 04:17:59 | [CVE-2026-134851](https://nvd.nist.gov/vuln/detail/CVE-2026-134851) | Medium | 6.9 | A vulnerability was detected in leonkhoo123 self-hosting-file-uploader up to 473e38ff8fba494f33a485730c6d95c5d8c536ea.… |
| 2026-11-23 04:17:59 | [CVE-2026-134852](https://nvd.nist.gov/vuln/detail/CVE-2026-134852) | Medium | 5.5 | A flaw has been found in shaozilee bmp-js up to 0.1.0. This vulnerability affects the function BmpDecoder.parseRGBA of… |
| 2026-11-23 04:17:59 | [CVE-2026-134853](https://nvd.nist.gov/vuln/detail/CVE-2026-134853) | Medium | 5.5 | A vulnerability has been found in vthibault tga-js up to 1.1.1. This issue affects the function _decodeRLE of the file… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
