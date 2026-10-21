# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-21 10:19 UTC

New CVEs published between 2026-10-21 09:18 UTC and 2026-10-21 10:19 UTC.

[Full CSV](data/new-cves-2026-10-21T10-19-05-911975Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-10-21 10:16:54 | [CVE-2026-105923](https://nvd.nist.gov/vuln/detail/CVE-2026-105923) | Medium | 4.0 | A malicious SVG can trigger an integer overflow which in turn triggers a null-pointer dereference in VectorImage QML Ty… |
| 2026-10-21 10:16:55 | [CVE-2026-110369](https://nvd.nist.gov/vuln/detail/CVE-2026-110369) | High | 8.8 | Deserialization of Untrusted Data vulnerability in GS Plugins WordPress Team Members – GS Plugins gs-team-members allow… |
| 2026-10-21 10:16:55 | [CVE-2026-110370](https://nvd.nist.gov/vuln/detail/CVE-2026-110370) | High | 8.8 | Deserialization of Untrusted Data vulnerability in GS Plugins GS Pins for Pinterest gs-pinterest-portfolio allows Objec… |
| 2026-10-21 10:16:55 | [CVE-2026-110884](https://nvd.nist.gov/vuln/detail/CVE-2026-110884) | High | 7.1 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in geekontheroad Liv… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
