# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-09-28 05:19 UTC

New CVEs published between 2026-09-28 04:19 UTC and 2026-09-28 05:19 UTC.

[Full CSV](data/new-cves-2026-09-28T05-19-35-297482Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-09-28 05:16:28 | [CVE-2026-100907](https://nvd.nist.gov/vuln/detail/CVE-2026-100907) | Medium | 5.5 | A flaw has been found in Eyeplus 57.0.0.0308. The impacted element is an unknown function of the file /snapshot of the… |
| 2026-09-28 05:16:29 | [CVE-2026-100908](https://nvd.nist.gov/vuln/detail/CVE-2026-100908) | High | 7.7 | A vulnerability has been found in Eyeplus 57.0.0.0308. This affects an unknown function of the component p2pcam HTTP Pa… |
| 2026-09-28 05:16:30 | [CVE-2026-100909](https://nvd.nist.gov/vuln/detail/CVE-2026-100909) | Medium | 5.5 | A vulnerability was found in OctoberCMS up to 4.1.19/4.2.25/4.3.4. The impacted element is the function getSourcePathFo… |
| 2026-09-28 05:16:30 | [CVE-2026-101000](https://nvd.nist.gov/vuln/detail/CVE-2026-101000) | Critical | 9.3 | A vulnerability was determined in Netcore NBR100V2 1.3.240614.030928. This affects the function uci.apply of the file /… |
| 2026-09-28 05:16:30 | [CVE-2026-101001](https://nvd.nist.gov/vuln/detail/CVE-2026-101001) | Critical | 9.3 | A vulnerability was identified in Netcore NBR200V2 1.3.241127.071246. This impacts the function eval of the file /www/c… |
| 2026-09-28 05:16:30 | [CVE-2026-87723](https://nvd.nist.gov/vuln/detail/CVE-2026-87723) | Medium | 5.4 | In Google fuse-archive versions prior to 1.24, an attacker who can prepend a directory to PATH or write a malicious bin… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
