# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-10 10:18 UTC

New CVEs published between 2026-10-10 09:19 UTC and 2026-10-10 10:18 UTC.

[Full CSV](data/new-cves-2026-10-10T10-18-36-113187Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-10-10 10:16:42 | [CVE-2026-106138](https://nvd.nist.gov/vuln/detail/CVE-2026-106138) | Medium | 5.4 | In Progress® KendoReact (@progress/kendo-react-charts) starting with version 1.1.0 and prior to 16.2.0, the default Cha… |
| 2026-10-10 10:16:43 | [CVE-2026-106139](https://nvd.nist.gov/vuln/detail/CVE-2026-106139) | Medium | 5.4 | In Progress® Kendo UI for Vue (@progress/kendo-vue-charts) starting with version 2.5.0 and prior to 16.2.0, the default… |
| 2026-10-10 10:16:44 | [CVE-2026-108506](https://nvd.nist.gov/vuln/detail/CVE-2026-108506) | Medium | 5.5 | ZTE Z80 Ultra's system interfaces do not have robust invocation authentication, with inadequate access control. Third-p… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
