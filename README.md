# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-11-09 08:18 UTC

New CVEs published between 2026-11-09 07:18 UTC and 2026-11-09 08:18 UTC.

[Full CSV](data/new-cves-2026-11-09T08-18-31-274499Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-11-09 08:17:00 | [CVE-2026-109582](https://nvd.nist.gov/vuln/detail/CVE-2026-109582) | Medium | 5.1 | Insecure storage of sensitive information issue exists in SS1 provided by DOS Co., Ltd. Sensitive information used by t… |
| 2026-11-09 08:17:02 | [CVE-2026-113437](https://nvd.nist.gov/vuln/detail/CVE-2026-113437) | Medium | 6.9 | Path Traversal vulnerability exists in SS1/ SS1 Cloud provided by DOS Co., Ltd. and the ODM product rocoeyes provided b… |
| 2026-11-09 08:17:02 | [CVE-2026-120386](https://nvd.nist.gov/vuln/detail/CVE-2026-120386) | Medium | 5.1 | Effekseer improperly validates "effect" files. When a crafted effect file is loaded to the affected runtime, the host p… |
| 2026-11-09 08:17:02 | [CVE-2026-124577](https://nvd.nist.gov/vuln/detail/CVE-2026-124577) | High | 8.9 | A weakness has been identified in Intelbras SG 2404 PoE L2+ 1.00.70/1.00.72. The affected element is an unknown functio… |
| 2026-11-09 08:17:02 | [CVE-2026-124578](https://nvd.nist.gov/vuln/detail/CVE-2026-124578) | Medium | 6.9 | A security vulnerability has been detected in Pantum BP5100DW 3.A.4.7. The impacted element is an unknown function of t… |
| 2026-11-09 08:17:02 | [CVE-2026-124579](https://nvd.nist.gov/vuln/detail/CVE-2026-124579) | Low | 2.1 | A vulnerability was determined in aaPanel BillionMail up to 4.9. Affected by this issue is some unknown functionality o… |
| 2026-11-09 08:17:02 | [CVE-2026-124580](https://nvd.nist.gov/vuln/detail/CVE-2026-124580) | Critical | 9.3 | A vulnerability was found in Chengdu Feiyuxing Technology VW2100 and VEC10GP 1.0 B-MB3W202-210825-r11775. This impacts… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
