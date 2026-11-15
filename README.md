# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-11-15 07:19 UTC

New CVEs published between 2026-11-15 06:21 UTC and 2026-11-15 07:19 UTC.

[Full CSV](data/new-cves-2026-11-15T07-19-11-813117Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-11-15 07:16:49 | [CVE-2026-103361](https://nvd.nist.gov/vuln/detail/CVE-2026-103361) |  |  | The Payment Gateway via Valitor for WooCommerce WordPress plugin before 1.9.41 does not properly validate the authentic… |
| 2026-11-15 07:16:53 | [CVE-2026-110960](https://nvd.nist.gov/vuln/detail/CVE-2026-110960) |  |  | The Auth Armor WordPress plugin through 1.0.3 does not require authentication on several handlers available to logged-o… |
| 2026-11-15 07:16:53 | [CVE-2026-110984](https://nvd.nist.gov/vuln/detail/CVE-2026-110984) |  |  | The RegistrationMagic WordPress plugin before 6.1.0.4 does not sanitise and escape a parameter before using it in a SQL… |
| 2026-11-15 07:16:53 | [CVE-2026-110987](https://nvd.nist.gov/vuln/detail/CVE-2026-110987) |  |  | The RegistrationMagic WordPress plugin before 6.1.0.4 does not properly escape a user-supplied value before printing it… |
| 2026-11-15 07:16:53 | [CVE-2026-110989](https://nvd.nist.gov/vuln/detail/CVE-2026-110989) |  |  | The RegistrationMagic WordPress plugin before 6.1.0.4 does not verify ownership of the submitted email address before u… |
| 2026-11-15 07:16:53 | [CVE-2026-114451](https://nvd.nist.gov/vuln/detail/CVE-2026-114451) |  |  | The Membership Plugin WordPress plugin before 4.0.6 does not perform any authorization or CSRF check before running a s… |
| 2026-11-15 07:16:54 | [CVE-2026-114452](https://nvd.nist.gov/vuln/detail/CVE-2026-114452) |  |  | The Membership Plugin WordPress plugin before 4.0.6 does not verify that the membership referenced in a saved-card paym… |
| 2026-11-15 07:16:54 | [CVE-2026-116559](https://nvd.nist.gov/vuln/detail/CVE-2026-116559) |  |  | The A2Reviews WordPress plugin through 1.2.3 does not properly verify authorization on several of its API command handl… |
| 2026-11-15 07:16:54 | [CVE-2026-123707](https://nvd.nist.gov/vuln/detail/CVE-2026-123707) |  |  | The WPGraphQL WordPress plugin before 2.27.1 does not restrict access to posts in custom non-public post statuses, allo… |
| 2026-11-15 07:16:54 | [CVE-2026-124671](https://nvd.nist.gov/vuln/detail/CVE-2026-124671) |  |  | The Burst Statistics WordPress plugin before 3.7.5 does not enforce a shared report's date range on the analytics it se… |
| 2026-11-15 07:16:54 | [CVE-2026-124673](https://nvd.nist.gov/vuln/detail/CVE-2026-124673) |  |  | The Burst Statistics WordPress plugin before 3.7.5 does not check that a reported page view belongs to published conten… |
| 2026-11-15 07:16:54 | [CVE-2026-127048](https://nvd.nist.gov/vuln/detail/CVE-2026-127048) |  |  | The Custom Block Builder WordPress plugin before 3.0.0 does not properly deny unauthorised requests to its REST routes,… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
