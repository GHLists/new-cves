# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-11-28 13:21 UTC

New CVEs published between 2026-11-28 12:20 UTC and 2026-11-28 13:21 UTC.

[Full CSV](data/new-cves-2026-11-28T13-21-21-831848Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-11-28 13:17:02 | [CVE-2026-138039](https://nvd.nist.gov/vuln/detail/CVE-2026-138039) | Medium | 5.5 | A vulnerability was found in Open5GS up to 2.8.0. Affected is the function smf_ue_find_by_imsi of the file src/smf/cont… |
| 2026-11-28 13:17:03 | [CVE-2026-138047](https://nvd.nist.gov/vuln/detail/CVE-2026-138047) | Low | 2.0 | A vulnerability was identified in dcatadmin Dcat-Admin 2.2.2-beta. Affected by this issue is the function getDatabaseCo… |
| 2026-11-28 13:17:03 | [CVE-2026-138049](https://nvd.nist.gov/vuln/detail/CVE-2026-138049) | Medium | 5.5 | A security flaw has been discovered in OpenAirInterface oai-cn5g-nrf up to 2.2.1. This affects the function notify_subs… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
