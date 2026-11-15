# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-11-15 13:21 UTC

New CVEs published between 2026-11-15 12:21 UTC and 2026-11-15 13:21 UTC.

[Full CSV](data/new-cves-2026-11-15T13-21-28-365941Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-11-15 13:16:58 | [CVE-2026-129451](https://nvd.nist.gov/vuln/detail/CVE-2026-129451) | High | 8.6 | A flaw has been found in DrayTek Vigor2960 up to 1.5.1.6. This affects the function app_guest_export of the file /cgi-b… |
| 2026-11-15 13:16:59 | [CVE-2026-129452](https://nvd.nist.gov/vuln/detail/CVE-2026-129452) | High | 8.5 | A vulnerability has been found in DrayTek Vigor2960 1.5.1.6. This vulnerability affects the function set_table of the f… |
| 2026-11-15 13:16:59 | [CVE-2026-129467](https://nvd.nist.gov/vuln/detail/CVE-2026-129467) | Medium | 5.3 | GeoPulse 1.5.0 through 2.3.0 contains an insecure direct object reference vulnerability in GET /api/v1/places/geocoding… |
| 2026-11-15 13:17:00 | [CVE-2026-129468](https://nvd.nist.gov/vuln/detail/CVE-2026-129468) | Medium | 5.3 | Netcccyun dnsmgr 2.18 before 2.22 contains a missing authorization vulnerability in POST /cloudflare/get_domain_default… |
| 2026-11-15 13:17:00 | [CVE-2026-129469](https://nvd.nist.gov/vuln/detail/CVE-2026-129469) | Medium | 6.9 | Course-tencent-cloud before 2.0.2 contains an insecure direct object reference vulnerability that allows unauthenticate… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
