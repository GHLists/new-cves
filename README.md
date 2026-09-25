# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-09-25 23:19 UTC

New CVEs published between 2026-09-25 22:19 UTC and 2026-09-25 23:19 UTC.

[Full CSV](data/new-cves-2026-09-25T23-19-12-944137Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-09-25 23:16:53 | [CVE-2026-57449](https://nvd.nist.gov/vuln/detail/CVE-2026-57449) | High | 7.1 | Actual is a local-first personal finance tool. Prior to 26.7.0, Actual Sync Server's CORS proxy is intended to let auth… |
| 2026-09-25 23:16:54 | [CVE-2026-86066](https://nvd.nist.gov/vuln/detail/CVE-2026-86066) | Medium | 5.9 | Horilla is an HR and CRM software. Prior to 2.0.0, approve_validate_attendance_request at /attendance/approve-validate-… |
| 2026-09-25 23:16:55 | [CVE-2026-96795](https://nvd.nist.gov/vuln/detail/CVE-2026-96795) | High | 8.8 | Horilla is an HR and CRM software. Prior to 2.0.0, HorillaListView.export_data in horilla_views/generic/cbv/views.py ac… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
