# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-09-25 05:20 UTC

New CVEs published between 2026-09-25 04:19 UTC and 2026-09-25 05:20 UTC.

[Full CSV](data/new-cves-2026-09-25T05-20-12-634395Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-09-25 05:17:07 | [CVE-2026-97737](https://nvd.nist.gov/vuln/detail/CVE-2026-97737) | High | 7.4 | In Wakapi before 2.17.6, the user caching service allows a lookup to be resolved in an unintended lookup context, leadi… |
| 2026-09-25 05:17:07 | [CVE-2026-97764](https://nvd.nist.gov/vuln/detail/CVE-2026-97764) | Low | 3.7 | django-allauth before 65.19.4 does not have the expected limits on failed login attempts because, in some common config… |
| 2026-09-25 05:17:08 | [CVE-2026-97818](https://nvd.nist.gov/vuln/detail/CVE-2026-97818) | High | 8.6 | phpIPAM through 1.8.3 has incorrect authorization for id=="admins" and id=="all" in api/controllers/User.php. |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
