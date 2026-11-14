# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-11-14 12:18 UTC

New CVEs published between 2026-11-14 11:18 UTC and 2026-11-14 12:18 UTC.

[Full CSV](data/new-cves-2026-11-14T12-18-21-422328Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-11-14 12:17:42 | [CVE-2026-124536](https://nvd.nist.gov/vuln/detail/CVE-2026-124536) |  |  | JSON::XS versions before 4.05 for Perl allow memory exhaustion by buffering incremental input past max_size after a NUL… |
| 2026-11-14 12:17:43 | [CVE-2026-124539](https://nvd.nist.gov/vuln/detail/CVE-2026-124539) |  |  | JSON::XS versions before 4.05 for Perl leak the decoded key of an object rejected for a missing colon in decode_hv. Unl… |
| 2026-11-14 12:17:43 | [CVE-2026-124540](https://nvd.nist.gov/vuln/detail/CVE-2026-124540) |  |  | JSON::XS versions before 4.05 for Perl allow stack exhaustion via nested tagged values under allow_tags in decode_tag.… |
| 2026-11-14 12:17:43 | [CVE-2026-124541](https://nvd.nist.gov/vuln/detail/CVE-2026-124541) |  |  | JSON::XS versions before 4.05 for Perl leak the decoded part of a rejected long string in decode_str. A string is decod… |
| 2026-11-14 12:17:43 | [CVE-2026-129113](https://nvd.nist.gov/vuln/detail/CVE-2026-129113) |  |  | JSON::XS versions from 4.0_00 before 4.05 for Perl corrupt the incremental buffer length by chopping past its end in in… |
| 2026-11-14 12:17:44 | [CVE-2026-129114](https://nvd.nist.gov/vuln/detail/CVE-2026-129114) |  |  | JSON::XS versions from 3.04 before 4.05 for Perl write one byte past a heap buffer when appending a one-byte chunk in i… |
| 2026-11-14 12:17:44 | [CVE-2026-129115](https://nvd.nist.gov/vuln/detail/CVE-2026-129115) |  |  | JSON::XS versions from 3.0 before 4.05 for Perl read freed stack memory when a FREEZE result's serialisation grows the… |
| 2026-11-14 12:17:44 | [CVE-2026-129250](https://nvd.nist.gov/vuln/detail/CVE-2026-129250) | High | 8.6 | A security vulnerability has been detected in Edimax BR6478ACV2 1.23. The impacted element is the function formPPTPSetu… |
| 2026-11-14 12:17:44 | [CVE-2026-129251](https://nvd.nist.gov/vuln/detail/CVE-2026-129251) | Low | 1.9 | A vulnerability was detected in hrshadhin CloudSchool up to 3.0.1. This affects an unknown function of the file app/Htt… |
| 2026-11-14 12:17:44 | [CVE-2026-129427](https://nvd.nist.gov/vuln/detail/CVE-2026-129427) | High | 8.7 | Stored XSS via avatar upload chained with an authentication bypass in /Attachments leads to ATO in Cervantes version v1… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
