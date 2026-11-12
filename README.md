# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-11-12 08:18 UTC

New CVEs published between 2026-11-12 07:21 UTC and 2026-11-12 08:18 UTC.

[Full CSV](data/new-cves-2026-11-12T08-18-52-716055Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-11-12 08:16:39 | [CVE-2026-118855](https://nvd.nist.gov/vuln/detail/CVE-2026-118855) | High | 7.0 | Akaunting 3.3.0 contains a stored cross-site scripting vulnerability through invoice import. An authenticated user with… |
| 2026-11-12 08:16:41 | [CVE-2026-123133](https://nvd.nist.gov/vuln/detail/CVE-2026-123133) |  |  | Rejected reason: This CVE ID is a duplicate of CVE-2026-116518 and was never published. Both IDs were assigned to the s… |
| 2026-11-12 08:16:41 | [CVE-2026-125836](https://nvd.nist.gov/vuln/detail/CVE-2026-125836) | High | 8.8 | Cross-Site Request Forgery (CSRF) vulnerability in Nicu Micle Simple JWT Login simple-jwt-login allows Cross Site Reque… |
| 2026-11-12 08:16:41 | [CVE-2026-126991](https://nvd.nist.gov/vuln/detail/CVE-2026-126991) | Medium | 5.3 | The Wikidata Lookup expansion module (wiki.py) in MISP misp-modules contained a SPARQL injection vulnerability. The han… |
| 2026-11-12 08:16:41 | [CVE-2026-40820](https://nvd.nist.gov/vuln/detail/CVE-2026-40820) | Medium | 6.9 | A high privileged remote attacker can exploit an unauthenticated SQL Injection vulnerability in the getVpnData function… |
| 2026-11-12 08:16:41 | [CVE-2026-47832](https://nvd.nist.gov/vuln/detail/CVE-2026-47832) | High | 7.3 | The vulnerability lies in the way application credentials are handled within the BOSH deployment. bosh-openstack-cpi-re… |
| 2026-11-12 08:16:42 | [CVE-2026-82292](https://nvd.nist.gov/vuln/detail/CVE-2026-82292) | Low | 1.9 | A NULL pointer dereference vulnerability in the Qt Framework QDomDocument::setContent() XML parsing path of the Qt XML… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
