# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-01 12:20 UTC

New CVEs published between 2026-10-01 11:19 UTC and 2026-10-01 12:20 UTC.

[Full CSV](data/new-cves-2026-10-01T12-20-16-081335Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-10-01 12:17:14 | [CVE-2026-103336](https://nvd.nist.gov/vuln/detail/CVE-2026-103336) | Medium | 5.3 | Insertion of Sensitive Information Into Sent Data vulnerability in Smackcoders Inc. WP Ultimate CSV Importer wp-ultimat… |
| 2026-10-01 12:17:15 | [CVE-2026-103678](https://nvd.nist.gov/vuln/detail/CVE-2026-103678) | Medium | 5.4 | A flaw was found in tnef. An attacker can exploit this vulnerability by providing a specially crafted file containing u… |
| 2026-10-01 12:17:15 | [CVE-2026-103679](https://nvd.nist.gov/vuln/detail/CVE-2026-103679) | Medium | 6.5 | A flaw was found in tnef. A remote attacker could exploit this vulnerability by providing a specially crafted Transport… |
| 2026-10-01 12:17:15 | [CVE-2026-103680](https://nvd.nist.gov/vuln/detail/CVE-2026-103680) | Low | 3.1 | A flaw was found in tnef. A heap-based buffer overflow can occur in the find_free_number() function when generating num… |
| 2026-10-01 12:17:15 | [CVE-2026-103754](https://nvd.nist.gov/vuln/detail/CVE-2026-103754) | Medium | 5.9 | A flaw was found in ansible-runner. The unstream_dir() function, which receives and extracts a streamed zip archive on… |
| 2026-10-01 12:17:16 | [CVE-2026-103858](https://nvd.nist.gov/vuln/detail/CVE-2026-103858) | Medium | 5.3 | MISP contains an incomplete authorization check in the discussion posting functionality. When a user submits a post to… |
| 2026-10-01 12:17:16 | [CVE-2026-94212](https://nvd.nist.gov/vuln/detail/CVE-2026-94212) | Medium | 6.4 | Improper verification of cryptographic signature vulnerability in Apache APISIX. Any unauthenticated attacker could imp… |
| 2026-10-01 12:17:16 | [CVE-2026-94220](https://nvd.nist.gov/vuln/detail/CVE-2026-94220) | Low | 2.1 | Cross-Site request forgery (CSRF) vulnerability in feishu-auth and dingtalk-auth plugins in Apache APISIX. An attacker… |
| 2026-10-01 12:17:17 | [CVE-2026-94250](https://nvd.nist.gov/vuln/detail/CVE-2026-94250) | High | 8.2 | Allocation of resources without limits or throttling vulnerability in batch-requests plugin in Apache APISIX. An unauth… |
| 2026-10-01 12:17:17 | [CVE-2026-94269](https://nvd.nist.gov/vuln/detail/CVE-2026-94269) | Medium | 6.3 | Use of Non-Canonical URL paths for authorization decisions vulnerability in Apache APISIX. In some configurations where… |
| 2026-10-01 12:17:17 | [CVE-2026-94276](https://nvd.nist.gov/vuln/detail/CVE-2026-94276) | Medium | 5.1 | Improper Authentication vulnerability in Apache APISIX. On a route using openid-connect plugin with remote introspectio… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
