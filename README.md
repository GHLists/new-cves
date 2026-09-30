# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-09-30 11:18 UTC

New CVEs published between 2026-09-30 10:18 UTC and 2026-09-30 11:18 UTC.

[Full CSV](data/new-cves-2026-09-30T11-18-40-672374Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-09-30 11:16:43 | [CVE-2026-103113](https://nvd.nist.gov/vuln/detail/CVE-2026-103113) | Low | 2.0 | A vulnerability was determined in OS4ED openSIS-Classic up to 9.3. The affected element is the function save action of… |
| 2026-09-30 11:16:43 | [CVE-2026-103239](https://nvd.nist.gov/vuln/detail/CVE-2026-103239) | High | 8.6 | MISP contains a privilege escalation vulnerability in the tag collection creation and editing functionality. The affect… |
| 2026-09-30 11:16:43 | [CVE-2026-13719](https://nvd.nist.gov/vuln/detail/CVE-2026-13719) | Medium | 4.3 | An authenticated user can list alert rules stored in folders they are not allowed to read through the alert rules API l… |
| 2026-09-30 11:16:43 | [CVE-2026-13720](https://nvd.nist.gov/vuln/detail/CVE-2026-13720) | Medium | 5.4 | An Editor can set file-provisioning metadata (the grafana.app/managedBy, grafana.app/managerId and grafana.app/sourcePa… |
| 2026-09-30 11:16:47 | [CVE-2026-76992](https://nvd.nist.gov/vuln/detail/CVE-2026-76992) | High | 8.7 | The CODESYS Gateway Client allocates memory based on a size field in a gateway response without enforcing an appropriat… |
| 2026-09-30 11:16:48 | [CVE-2026-96342](https://nvd.nist.gov/vuln/detail/CVE-2026-96342) | Medium | 6.9 | Missing Authorization vulnerability in Amauri.IO WPMobile.App wpappninja allows Retrieve Embedded Sensitive Data.This i… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
