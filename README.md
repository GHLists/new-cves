# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-19 09:19 UTC

New CVEs published between 2026-10-19 08:19 UTC and 2026-10-19 09:19 UTC.

[Full CSV](data/new-cves-2026-10-19T09-19-15-405485Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-10-19 09:17:06 | [CVE-2026-104679](https://nvd.nist.gov/vuln/detail/CVE-2026-104679) | Medium | 6.9 | VOCALOID6 Editor provided by Yamaha Corporation improperly restricts XML external entity references. Loading a speciall… |
| 2026-10-19 09:17:07 | [CVE-2026-111438](https://nvd.nist.gov/vuln/detail/CVE-2026-111438) | Medium | 6.5 | 在 openGauss-server 的 src/common/backend/libpq/hba.cpp 中，复制连接认证存在访问控制绕过。hba_getauthmethod() 在处理 HADR/SW 复制发送方时，不要求 is_no… |
| 2026-10-19 09:17:07 | [CVE-2026-112095](https://nvd.nist.gov/vuln/detail/CVE-2026-112095) | Low | 2.0 | A flaw has been found in SourceCodester Inventory System 1.0. This affects an unknown part of the file /api/products_ha… |
| 2026-10-19 09:17:07 | [CVE-2026-112096](https://nvd.nist.gov/vuln/detail/CVE-2026-112096) | Low | 2.0 | A vulnerability has been found in SourceCodester Inventory System 1.0. This vulnerability affects unknown code of the f… |
| 2026-10-19 09:17:07 | [CVE-2026-112097](https://nvd.nist.gov/vuln/detail/CVE-2026-112097) | Medium | 5.1 | A vulnerability was found in SourceCodester Inventory System 1.0. This issue affects some unknown processing of the fil… |
| 2026-10-19 09:17:07 | [CVE-2026-112098](https://nvd.nist.gov/vuln/detail/CVE-2026-112098) | Low | 2.1 | A security flaw has been discovered in DeepPavlov up to 1.7.0. Impacted is the function resolve of the file deeppavlov/… |
| 2026-10-19 09:17:08 | [CVE-2026-112161](https://nvd.nist.gov/vuln/detail/CVE-2026-112161) | High | 8.5 | MobaXterm Personal Edition (Portable) 26.4 GA extracts the CygUtils64.plugin file without first verifying its integrity… |
| 2026-10-19 09:17:08 | [CVE-2026-112178](https://nvd.nist.gov/vuln/detail/CVE-2026-112178) | High | 7.1 | MISP contains an access control flaw in the proposal (shadow attribute) visibility logic. The authorization check accep… |
| 2026-10-19 09:17:08 | [CVE-2026-112179](https://nvd.nist.gov/vuln/detail/CVE-2026-112179) | Medium | 5.3 | In MISP, the event synchronization process contained a logic error in the preparation of event reports for remote push.… |
| 2026-10-19 09:17:08 | [CVE-2026-112180](https://nvd.nist.gov/vuln/detail/CVE-2026-112180) | Medium | 5.1 | MISP contains a data integrity flaw in its event deletion logic. When a user deletes an event, several associated recor… |
| 2026-10-19 09:17:08 | [CVE-2026-13695](https://nvd.nist.gov/vuln/detail/CVE-2026-13695) | High | 8.8 | SQL injection (SQLi) vulnerability—specifically a UNION-based vulnerability—in the Integratec application that affects… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
