# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-12 07:19 UTC

New CVEs published between 2026-10-12 06:20 UTC and 2026-10-12 07:19 UTC.

[Full CSV](data/new-cves-2026-10-12T07-19-38-862205Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-10-12 07:16:35 | [CVE-2026-108807](https://nvd.nist.gov/vuln/detail/CVE-2026-108807) | Medium | 5.5 | A vulnerability was found in krupalshah EmployeeRecruitmentSystem up to 922ff6d208278282e7c8e36d70d9ae356adec9fe. This… |
| 2026-10-12 07:16:35 | [CVE-2026-108808](https://nvd.nist.gov/vuln/detail/CVE-2026-108808) | Low | 1.2 | A vulnerability was determined in Eleveo Call Recording Software up to 10.3.0. This vulnerability affects unknown code… |
| 2026-10-12 07:16:36 | [CVE-2026-108809](https://nvd.nist.gov/vuln/detail/CVE-2026-108809) | Low | 2.0 | A vulnerability was identified in Eleveo Call Recording Software up to 10.3.0. This issue affects some unknown processi… |
| 2026-10-12 07:16:36 | [CVE-2026-109082](https://nvd.nist.gov/vuln/detail/CVE-2026-109082) | Medium | 6.8 | A flaw was found in the Client-Initiated Backchannel Authentication CIBA implementation within the keycloak-services co… |
| 2026-10-12 07:16:36 | [CVE-2026-48211](https://nvd.nist.gov/vuln/detail/CVE-2026-48211) | Medium | 5.4 | An authenticated administrator can be induced to delete administrative Import/Export templates through a Cross-Site Req… |
| 2026-10-12 07:16:36 | [CVE-2026-48212](https://nvd.nist.gov/vuln/detail/CVE-2026-48212) | Medium | 4.8 | An OTRS administrator can enter arbitrary JavaScript into the content of an OTRS Custom Page, which is stored by the ap… |
| 2026-10-12 07:16:36 | [CVE-2026-78355](https://nvd.nist.gov/vuln/detail/CVE-2026-78355) | High | 8.7 | A path traversal vulnerability in the OTRS SendSupportBundle functionality allows an authenticated administrator to ref… |
| 2026-10-12 07:16:36 | [CVE-2026-78356](https://nvd.nist.gov/vuln/detail/CVE-2026-78356) | Medium | 5.3 | The OTRS Agent Frontend configuration endpoint can be accessed without authentication. This allows unauthenticated remo… |
| 2026-10-12 07:16:37 | [CVE-2026-78357](https://nvd.nist.gov/vuln/detail/CVE-2026-78357) | Critical | 9.1 | Previously issued authentication tokens are not immediately invalidated when an OTRS agent or customer user account is… |
| 2026-10-12 07:16:37 | [CVE-2026-78358](https://nvd.nist.gov/vuln/detail/CVE-2026-78358) | Medium | 4.3 | Several administrative actions do not sufficiently validate whether a request was intentionally initiated by the authen… |
| 2026-10-12 07:16:37 | [CVE-2026-78359](https://nvd.nist.gov/vuln/detail/CVE-2026-78359) | Medium | 5.4 | OTRS does not sufficiently enforce the uniqueness of customer user identities across multiple configured CustomerUser b… |
| 2026-10-12 07:16:37 | [CVE-2026-93581](https://nvd.nist.gov/vuln/detail/CVE-2026-93581) | Medium | 6.1 | User-controlled values are not sufficiently neutralized when included in CSV exports. Values originating from user inpu… |
| 2026-10-12 07:16:37 | [CVE-2026-93582](https://nvd.nist.gov/vuln/detail/CVE-2026-93582) | Critical | 9.4 | The HTTP Basic Authentication modules in ((OTRS)) Community Edition 6 and prior accept the authenticated username from… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
