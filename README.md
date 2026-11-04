# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-11-04 03:20 UTC

New CVEs published between 2026-11-04 02:18 UTC and 2026-11-04 03:20 UTC.

[Full CSV](data/new-cves-2026-11-04T03-20-10-729701Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-11-04 03:17:14 | [CVE-2026-121615](https://nvd.nist.gov/vuln/detail/CVE-2026-121615) | Critical | 9.3 | A vulnerability was determined in Linksys E5600 1.1.0.26. Affected is an unknown function of the file /cgi-bin/mesh_log… |
| 2026-11-04 03:17:15 | [CVE-2026-121616](https://nvd.nist.gov/vuln/detail/CVE-2026-121616) | Medium | 5.5 | A vulnerability was identified in Linksys E5600 1.1.0.26. Affected by this vulnerability is the function strcpy of the… |
| 2026-11-04 03:17:15 | [CVE-2026-121617](https://nvd.nist.gov/vuln/detail/CVE-2026-121617) | High | 7.7 | A security flaw has been discovered in Linksys E5600 1.1.0.26. Affected by this issue is the function init_multipart of… |
| 2026-11-04 03:17:15 | [CVE-2026-121618](https://nvd.nist.gov/vuln/detail/CVE-2026-121618) | Medium | 5.5 | A weakness has been identified in Linksys E5600 1.1.0.26. This affects an unknown part of the file /cgi-bin/fqc.cgi of… |
| 2026-11-04 03:17:15 | [CVE-2026-121802](https://nvd.nist.gov/vuln/detail/CVE-2026-121802) | Critical | 9.1 | @better-auth/expo before 1.7.16 allows certain account-takeover outcomes (e.g., unauthenticated changes of any account'… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
