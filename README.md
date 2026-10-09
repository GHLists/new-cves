# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-09 20:18 UTC

New CVEs published between 2026-10-09 19:18 UTC and 2026-10-09 20:18 UTC.

[Full CSV](data/new-cves-2026-10-09T20-18-53-830205Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-10-09 20:17:08 | [CVE-2025-8457](https://nvd.nist.gov/vuln/detail/CVE-2025-8457) |  |  | Rejected reason: This CVE ID has been rejected or withdrawn by its CVE Numbering Authority. |
| 2026-10-09 20:17:09 | [CVE-2026-104758](https://nvd.nist.gov/vuln/detail/CVE-2026-104758) |  |  | Rejected reason: ** REJECT ** DO NOT USE THIS CANDIDATE NUMBER. ConsultIDs: CVE-2026-73364. Reason: This candidate is a… |
| 2026-10-09 20:17:10 | [CVE-2026-107842](https://nvd.nist.gov/vuln/detail/CVE-2026-107842) | Medium | 5.3 | Contao is an Open Source CMS. From version 4.0.0 until 5.3.50 and 5.7.12, ModuleSearch can disclose protected page titl… |
| 2026-10-09 20:17:10 | [CVE-2026-107843](https://nvd.nist.gov/vuln/detail/CVE-2026-107843) | Medium | 5.3 | Contao is an Open Source CMS. From version 4.1.0 until 5.3.50 and 5.7.12, ModuleRegistration::compile() enters its foll… |
| 2026-10-09 20:17:10 | [CVE-2026-107844](https://nvd.nist.gov/vuln/detail/CVE-2026-107844) | Medium | 5.3 | Contao is an Open Source CMS. From version 5.0.0 until 5.3.50 and 5.7.12, ImagesController joins the user-controlled {p… |
| 2026-10-09 20:17:10 | [CVE-2026-107845](https://nvd.nist.gov/vuln/detail/CVE-2026-107845) | Critical | 9.3 | Contao is an Open Source CMS. From version 4.0.0 until 5.3.50 and 5.7.12, an unauthenticated visitor can submit a comme… |
| 2026-10-09 20:17:11 | [CVE-2026-78797](https://nvd.nist.gov/vuln/detail/CVE-2026-78797) |  |  | An issue in iStoreOS istoreos-24.10.7 and before allows a remote attacker to execute arbitrary code via the task_id in… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
