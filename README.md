# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-10 13:19 UTC

New CVEs published between 2026-10-10 12:18 UTC and 2026-10-10 13:19 UTC.

[Full CSV](data/new-cves-2026-10-10T13-19-32-008334Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-10-10 13:17:30 | [CVE-2013-10076](https://nvd.nist.gov/vuln/detail/CVE-2013-10076) |  |  | ExtUtils::Typemaps::STL::Vector versions before 1.05 for Perl allocate a 32 GiB array on an empty list. The OUTPUT type… |
| 2026-10-10 13:17:31 | [CVE-2026-107373](https://nvd.nist.gov/vuln/detail/CVE-2026-107373) |  |  | ExtUtils::Typemaps::STL::String versions before 1.06 for Perl T_STD_STRING typemap may read the SV length before string… |
| 2026-10-10 13:17:31 | [CVE-2026-107794](https://nvd.nist.gov/vuln/detail/CVE-2026-107794) |  |  | ExtUtils::Typemaps::STL::List versions before 1.07 for Perl allocate a 32 GiB array on an empty list. The OUTPUT typema… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
