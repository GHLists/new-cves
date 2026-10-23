# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-23 01:18 UTC

New CVEs published between 2026-10-23 00:21 UTC and 2026-10-23 01:18 UTC.

[Full CSV](data/new-cves-2026-10-23T01-18-48-441538Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-10-23 01:16:53 | [CVE-2026-115484](https://nvd.nist.gov/vuln/detail/CVE-2026-115484) | High | 7.6 | A flaw was found in the iscsiuio component of open-iscsi. The DHCPv4 option parser incorrectly calculates the length of… |
| 2026-10-23 01:16:53 | [CVE-2026-115485](https://nvd.nist.gov/vuln/detail/CVE-2026-115485) | Medium | 6.3 | A flaw was found in the iscsiuio component of open-iscsi. The DHCPv6 option parser calls strlen() on raw network data w… |
| 2026-10-23 01:16:53 | [CVE-2026-115486](https://nvd.nist.gov/vuln/detail/CVE-2026-115486) | High | 7.1 | A flaw was found in the iscsiuio component of open-iscsi. The IPv6 Neighbor Discovery handler accesses link-layer addre… |
| 2026-10-23 01:16:54 | [CVE-2026-115535](https://nvd.nist.gov/vuln/detail/CVE-2026-115535) | Low | 1.9 | A vulnerability was identified in gedelumbung HospitalManagement up to c2d45543789a3887067d3915f69d44cfc2cf76a8. The af… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
