# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-27 22:18 UTC

New CVEs published between 2026-10-27 21:18 UTC and 2026-10-27 22:18 UTC.

[Full CSV](data/new-cves-2026-10-27T22-18-40-298442Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-10-27 21:19:08 | [CVE-2026-83831](https://nvd.nist.gov/vuln/detail/CVE-2026-83831) | High | 8.8 | Double free in Microsoft Edge (Chromium-based) allows an unauthorized attacker to execute code over a network. |
| 2026-10-27 21:19:34 | [CVE-2026-85898](https://nvd.nist.gov/vuln/detail/CVE-2026-85898) | High | 8.8 | Access of resource using incompatible type ('type confusion') in Microsoft Edge (Chromium-based) allows an unauthorized… |
| 2026-10-27 22:17:26 | [CVE-2026-57186](https://nvd.nist.gov/vuln/detail/CVE-2026-57186) | High | 7.5 | Asterisk is an open source private branch exchange and telephony toolkit. From 21.0.0-pre1 until Asterisk 21.12.3, 22.1… |
| 2026-10-27 22:17:27 | [CVE-2026-57190](https://nvd.nist.gov/vuln/detail/CVE-2026-57190) | High | 7.0 | Asterisk is an open source private branch exchange and telephony toolkit. Prior to Asterisk 20.20.1, 21.12.3, 22.10.1,… |
| 2026-10-27 22:17:27 | [CVE-2026-57191](https://nvd.nist.gov/vuln/detail/CVE-2026-57191) | High | 8.2 | Asterisk is an open source private branch exchange and telephony toolkit. Prior to Asterisk 20.20.1, 21.12.3, 22.10.1,… |
| 2026-10-27 22:17:27 | [CVE-2026-57192](https://nvd.nist.gov/vuln/detail/CVE-2026-57192) | Medium | 6.0 | Asterisk is an open source private branch exchange and telephony toolkit. Prior to Asterisk 20.20.1, 21.12.3, 22.10.1,… |
| 2026-10-27 22:17:27 | [CVE-2026-57199](https://nvd.nist.gov/vuln/detail/CVE-2026-57199) | Low | 2.3 | Asterisk is an open source private branch exchange and telephony toolkit. Prior to Asterisk 20.20.1, 21.12.3, 22.10.1,… |
| 2026-10-27 22:17:27 | [CVE-2026-57203](https://nvd.nist.gov/vuln/detail/CVE-2026-57203) | Medium | 6.9 | Asterisk is an open source private branch exchange and telephony toolkit. Prior to Asterisk 20.20.1, 21.12.3, 22.10.1,… |
| 2026-10-27 22:17:29 | [CVE-2026-62765](https://nvd.nist.gov/vuln/detail/CVE-2026-62765) | High | 7.5 | Access of resource using incompatible type ('type confusion') in Microsoft Edge (Chromium-based) allows an unauthorized… |
| 2026-10-27 22:18:05 | [CVE-2026-78661](https://nvd.nist.gov/vuln/detail/CVE-2026-78661) |  |  | When coalescing adjacent text nodes in addText and fosterParent, appending to an existing TextNode's Data via string co… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
