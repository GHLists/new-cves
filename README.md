# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-09-26 01:18 UTC

New CVEs published between 2026-09-26 00:19 UTC and 2026-09-26 01:18 UTC.

[Full CSV](data/new-cves-2026-09-26T01-18-56-192096Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-09-26 01:16:59 | [CVE-2026-100503](https://nvd.nist.gov/vuln/detail/CVE-2026-100503) | Medium | 4.8 | Ghidra versions through 12.1.4 contain a heap use-after-free vulnerability in the decompiler's Funcdata::opInsertAfter… |
| 2026-09-26 01:17:00 | [CVE-2026-100504](https://nvd.nist.gov/vuln/detail/CVE-2026-100504) | High | 7.3 | Ghidra versions through 12.1.4 contain a stack-based out-of-bounds write vulnerability in the decompiler's leftshift128… |
| 2026-09-26 01:17:00 | [CVE-2026-100505](https://nvd.nist.gov/vuln/detail/CVE-2026-100505) | Medium | 4.8 | Ghidra versions 11.2 through 12.1.4 contain a heap out-of-bounds read vulnerability in StringManager::getCodepoint when… |
| 2026-09-26 01:17:00 | [CVE-2026-100520](https://nvd.nist.gov/vuln/detail/CVE-2026-100520) | High | 8.7 | Laranode versions before 1.2.1 contain a path traversal vulnerability in the POST /filemanager/upload-file endpoint tha… |
| 2026-09-26 01:17:00 | [CVE-2026-100521](https://nvd.nist.gov/vuln/detail/CVE-2026-100521) | Medium | 5.1 | Cotonti through 1.0.0 contains a reflected cross-site scripting vulnerability in the search plugin highlight parameter… |
| 2026-09-26 01:17:00 | [CVE-2026-100522](https://nvd.nist.gov/vuln/detail/CVE-2026-100522) | Medium | 5.1 | Cotonti through 1.0.0 contains a reflected cross-site scripting vulnerability in message.php where the lng parameter is… |
| 2026-09-26 01:17:00 | [CVE-2026-100523](https://nvd.nist.gov/vuln/detail/CVE-2026-100523) | Medium | 5.1 | Cotonti through 1.0.0 contains an open redirect vulnerability in message.php that base64-decodes the redirect parameter… |
| 2026-09-26 01:17:01 | [CVE-2026-100524](https://nvd.nist.gov/vuln/detail/CVE-2026-100524) | Medium | 5.3 | Cotonti through 1.0.0 contains a cross-site request forgery vulnerability in the extensions manager that allows attacke… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
