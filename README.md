# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-06 11:19 UTC

New CVEs published between 2026-10-06 10:19 UTC and 2026-10-06 11:19 UTC.

[Full CSV](data/new-cves-2026-10-06T11-19-55-240435Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-10-06 11:17:13 | [CVE-2026-103831](https://nvd.nist.gov/vuln/detail/CVE-2026-103831) | High | 7.5 | CVE-2026-103831: Insecure deserialization vulnerability in the Psr16CacheAdapter component of the TrueLayer Magento 2 P… |
| 2026-10-06 11:17:16 | [CVE-2026-105985](https://nvd.nist.gov/vuln/detail/CVE-2026-105985) | High | 8.7 | Craft CMS 5.10.13.2 contains an authenticated remote code execution vulnerability in the Control Panel action app/rende… |
| 2026-10-06 11:17:29 | [CVE-2026-75818](https://nvd.nist.gov/vuln/detail/CVE-2026-75818) | Low | 1.8 | GNU Aspell prezip-bin contains a heap-based buffer overflow vulnerability in the decompressor in prog/prezip.c. The dec… |
| 2026-10-06 11:17:29 | [CVE-2026-75819](https://nvd.nist.gov/vuln/detail/CVE-2026-75819) | Low | 1.8 | GNU Aspell contains an out-of-bounds read vulnerability in ReadOnlyDict::load() in readonly_ws.cpp. When loading a bina… |
| 2026-10-06 11:17:30 | [CVE-2026-75820](https://nvd.nist.gov/vuln/detail/CVE-2026-75820) | Low | 1.8 | GNU Aspell contains an integer truncation vulnerability in the WritableDict::add() function in modules/speller/default/… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
