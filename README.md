# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-11-05 02:20 UTC

New CVEs published between 2026-11-05 01:18 UTC and 2026-11-05 02:20 UTC.

[Full CSV](data/new-cves-2026-11-05T02-20-09-553792Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-11-05 02:16:57 | [CVE-2025-66364](https://nvd.nist.gov/vuln/detail/CVE-2025-66364) |  |  | Continuously sending control‑plane messages causes the baseband to crashes. |
| 2026-11-05 02:16:57 | [CVE-2026-122154](https://nvd.nist.gov/vuln/detail/CVE-2026-122154) | Medium | 5.5 | A vulnerability was found in purocean Yank Note 3.93.0. This impacts the function config.getAll of the file src/main/se… |
| 2026-11-05 02:16:58 | [CVE-2026-122157](https://nvd.nist.gov/vuln/detail/CVE-2026-122157) | Low | 2.1 | A vulnerability was identified in Purocean Yank Note 3.93.0. Affected by this vulnerability is the function checkPermis… |
| 2026-11-05 02:16:58 | [CVE-2026-122158](https://nvd.nist.gov/vuln/detail/CVE-2026-122158) | Low | 2.0 | A security flaw has been discovered in InvoiceShelf up to 2.4.3/3.0.0-alpha.3. Affected by this issue is the function M… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
