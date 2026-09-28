# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-09-28 23:20 UTC

New CVEs published between 2026-09-28 22:22 UTC and 2026-09-28 23:20 UTC.

[Full CSV](data/new-cves-2026-09-28T23-20-30-506845Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-09-28 23:17:00 | [CVE-2026-101260](https://nvd.nist.gov/vuln/detail/CVE-2026-101260) | High | 8.5 | A vulnerability was detected in Ziroom ZHOME A0101 1.0.1.0. Affected by this issue is some unknown functionality of the… |
| 2026-09-28 23:17:01 | [CVE-2026-101261](https://nvd.nist.gov/vuln/detail/CVE-2026-101261) | High | 8.5 | A flaw has been found in Ziroom ZHOME A0101 1.0.1.0. This affects an unknown part of the file /api/ZRnetwork/firstSetup… |
| 2026-09-28 23:17:01 | [CVE-2026-101262](https://nvd.nist.gov/vuln/detail/CVE-2026-101262) | High | 8.5 | A vulnerability has been found in Ziroom ZHOME A0101 1.0.1.0. This vulnerability affects unknown code of the file /api/… |
| 2026-09-28 23:17:01 | [CVE-2026-102332](https://nvd.nist.gov/vuln/detail/CVE-2026-102332) | Medium | 4.6 | Dozzle versions before 11.1.2 fail to sanitize container display names when building ZIP archive entry names in the log… |
| 2026-09-28 23:17:01 | [CVE-2026-102333](https://nvd.nist.gov/vuln/detail/CVE-2026-102333) | Medium | 5.3 | httpdbg before 2.2.1 fails to validate URL schemes in recorded HTTP request URLs rendered as clickable links in the web… |
| 2026-09-28 23:17:01 | [CVE-2026-102334](https://nvd.nist.gov/vuln/detail/CVE-2026-102334) | Critical | 9.1 | Nginx Proxy Manager through 2.16.0 lacks rate-limiting on authentication endpoints, allowing unauthenticated attackers… |
| 2026-09-28 23:17:02 | [CVE-2026-102335](https://nvd.nist.gov/vuln/detail/CVE-2026-102335) | High | 7.1 | Nginx Proxy Manager through 2.16.0 fails to restrict the advanced_config field to administrators, allowing non-admin us… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
