# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-11-28 12:20 UTC

New CVEs published between 2026-11-28 11:20 UTC and 2026-11-28 12:20 UTC.

[Full CSV](data/new-cves-2026-11-28T12-20-30-812254Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-11-28 12:17:41 | [CVE-2026-138037](https://nvd.nist.gov/vuln/detail/CVE-2026-138037) | Medium | 5.5 | A flaw has been found in Open5GS up to 2.8.0. This affects the function ogs_pfcp_handle_create_urr of the file lib/pfcp… |
| 2026-11-28 12:17:41 | [CVE-2026-138038](https://nvd.nist.gov/vuln/detail/CVE-2026-138038) | Medium | 5.5 | A vulnerability has been found in Open5GS 2.8.0. This impacts the function nrf_nnrf_handle_nf_discover of the file src/… |
| 2026-11-28 12:17:42 | [CVE-2026-5771](https://nvd.nist.gov/vuln/detail/CVE-2026-5771) | Medium | 4.3 | The Loco Translate plugin for WordPress is vulnerable to Arbitrary File Write/Overwrite via Path Traversal in all versi… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
