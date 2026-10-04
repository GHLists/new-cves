# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-04 07:19 UTC

New CVEs published between 2026-10-04 06:18 UTC and 2026-10-04 07:19 UTC.

[Full CSV](data/new-cves-2026-10-04T07-19-05-018982Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-10-04 07:16:31 | [CVE-2026-104118](https://nvd.nist.gov/vuln/detail/CVE-2026-104118) |  |  | The Razorpay for WooCommerce WordPress plugin before 4.8.8 does not perform ownership or authorization checks on a REST… |
| 2026-10-04 07:16:32 | [CVE-2026-104119](https://nvd.nist.gov/vuln/detail/CVE-2026-104119) |  |  | The Simple Shopping Cart WordPress plugin before 5.2.6 does not escape some of its settings field values before outputt… |
| 2026-10-04 07:16:33 | [CVE-2026-105133](https://nvd.nist.gov/vuln/detail/CVE-2026-105133) | Medium | 5.5 | A vulnerability was detected in Ahsay AhsayCBS up to 10.3.2. This affects the function checkSysPwd of the file com/ahsa… |
| 2026-10-04 07:16:33 | [CVE-2026-105134](https://nvd.nist.gov/vuln/detail/CVE-2026-105134) | Critical | 9.3 | A flaw has been found in Ahsay AhsayCBS up to 10.3.2. This vulnerability affects unknown code of the file /rps/api/json… |
| 2026-10-04 07:16:33 | [CVE-2026-105135](https://nvd.nist.gov/vuln/detail/CVE-2026-105135) | Critical | 9.3 | A vulnerability has been found in InternLM MindSearch 0.1.0. This issue affects the function ExecutionAction.run of the… |
| 2026-10-04 07:16:33 | [CVE-2026-17005](https://nvd.nist.gov/vuln/detail/CVE-2026-17005) |  |  | The Horizontal scrolling announcements WordPress plugin through 2.6 does not sanitise and escape one of its announcemen… |
| 2026-10-04 07:16:34 | [CVE-2026-86817](https://nvd.nist.gov/vuln/detail/CVE-2026-86817) |  |  | The Five Star Business Profile and Schema WordPress plugin before 2.4.0 does not properly restrict the callbacks used t… |
| 2026-10-04 07:16:34 | [CVE-2026-93549](https://nvd.nist.gov/vuln/detail/CVE-2026-93549) |  |  | The CoCart WordPress plugin before 4.9.7 does not scope its REST API authentication filter to its own endpoints, which… |
| 2026-10-04 07:16:34 | [CVE-2026-97332](https://nvd.nist.gov/vuln/detail/CVE-2026-97332) |  |  | The User Private Files WordPress plugin before 2.2.0 does not properly protect its stored private files on multisite in… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
