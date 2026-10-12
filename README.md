# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-12 06:20 UTC

New CVEs published between 2026-10-12 05:18 UTC and 2026-10-12 06:20 UTC.

[Full CSV](data/new-cves-2026-10-12T06-20-12-831294Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-10-12 06:16:58 | [CVE-2025-15703](https://nvd.nist.gov/vuln/detail/CVE-2025-15703) |  |  | The HireZoot WordPress plugin before 4.0.0 does not sanitise and escape one of its job specification settings before it… |
| 2026-10-12 06:16:58 | [CVE-2026-107193](https://nvd.nist.gov/vuln/detail/CVE-2026-107193) | Medium | 6.5 | A flaw has been found in **permission filters** in the **foreman** package. The API loads a filter by its identifier an… |
| 2026-10-12 06:16:58 | [CVE-2026-107203](https://nvd.nist.gov/vuln/detail/CVE-2026-107203) | Medium | 5.4 | An **incorrect authorization** flaw has been found in **network interface handling** in the **Foreman** package. The do… |
| 2026-10-12 06:16:58 | [CVE-2026-107791](https://nvd.nist.gov/vuln/detail/CVE-2026-107791) |  |  | The WP Comment Cleaner WordPress plugin before 7.2 does not perform a capability check or validate a nonce on one of it… |
| 2026-10-12 06:16:58 | [CVE-2026-108802](https://nvd.nist.gov/vuln/detail/CVE-2026-108802) | Low | 2.0 | A weakness has been identified in y_project RuoYi up to 4.8.3. This affects the function renderDrawer of the file /syst… |
| 2026-10-12 06:16:59 | [CVE-2026-108803](https://nvd.nist.gov/vuln/detail/CVE-2026-108803) | Medium | 5.3 | A security vulnerability has been detected in y_project RuoYi up to 4.8.3. This impacts the function changeStatus of th… |
| 2026-10-12 06:16:59 | [CVE-2026-108804](https://nvd.nist.gov/vuln/detail/CVE-2026-108804) | Critical | 9.3 | A vulnerability was detected in TRENDnet TEW-751DR, TEW-752DRU and TEW733GR 1.03B01/1.03B03. Affected is the function f… |
| 2026-10-12 06:16:59 | [CVE-2026-108805](https://nvd.nist.gov/vuln/detail/CVE-2026-108805) | Medium | 5.5 | A flaw has been found in krupalshah EmployeeRecruitmentSystem up to 922ff6d208278282e7c8e36d70d9ae356adec9fe. Affected… |
| 2026-10-12 06:16:59 | [CVE-2026-108806](https://nvd.nist.gov/vuln/detail/CVE-2026-108806) | Medium | 5.5 | A vulnerability has been found in krupalshah EmployeeRecruitmentSystem up to 922ff6d208278282e7c8e36d70d9ae356adec9fe.… |
| 2026-10-12 06:17:00 | [CVE-2026-109080](https://nvd.nist.gov/vuln/detail/CVE-2026-109080) | High | 7.1 | SQL injection in the bulk license plate search of the Flock Night Shift hosted service allowed an authenticated user to… |
| 2026-10-12 06:17:00 | [CVE-2026-84166](https://nvd.nist.gov/vuln/detail/CVE-2026-84166) |  |  | The Hotel Booking WordPress plugin through 3.8 does not implement CSRF protection on its administrative booking order m… |
| 2026-10-12 06:17:00 | [CVE-2026-84167](https://nvd.nist.gov/vuln/detail/CVE-2026-84167) |  |  | The Hotel Booking WordPress plugin through 3.8 does not verify that a booking record belongs to the user requesting it,… |
| 2026-10-12 06:17:00 | [CVE-2026-98385](https://nvd.nist.gov/vuln/detail/CVE-2026-98385) |  |  | In the Linux kernel, the following vulnerability has been resolved: sched/cache: Decouple sched_cache_group from mm to… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
