# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-07 20:19 UTC

New CVEs published between 2026-10-07 19:20 UTC and 2026-10-07 20:19 UTC.

[Full CSV](data/new-cves-2026-10-07T20-19-27-543085Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-10-07 20:17:10 | [CVE-2026-107161](https://nvd.nist.gov/vuln/detail/CVE-2026-107161) | High | 7.5 | A heap-based buffer overflow flaw was found in Cyrus SASL. The add_to_challenge() function in the DIGEST-MD5 plugin com… |
| 2026-10-07 20:17:11 | [CVE-2026-107176](https://nvd.nist.gov/vuln/detail/CVE-2026-107176) | Medium | 6.8 | A flaw was found in the cluster-samples-operator. The RBAC Role coreos-pull-secret-reader in namespace openshift-config… |
| 2026-10-07 20:17:11 | [CVE-2026-107353](https://nvd.nist.gov/vuln/detail/CVE-2026-107353) | Medium | 6.9 | traverse (npm) versions 0.3.6 through 0.3.9, 0.4.0 through 0.4.6, 0.5.0 through 0.5.2, and 0.6.0 through 0.6.11 allow p… |
| 2026-10-07 20:17:12 | [CVE-2026-107354](https://nvd.nist.gov/vuln/detail/CVE-2026-107354) |  |  | Rejected reason: ** This candidate has been removed by an organization. |
| 2026-10-07 20:17:12 | [CVE-2026-107355](https://nvd.nist.gov/vuln/detail/CVE-2026-107355) |  |  | Rejected reason: ** This candidate has been removed by an organization. |
| 2026-10-07 20:17:12 | [CVE-2026-34499](https://nvd.nist.gov/vuln/detail/CVE-2026-34499) | High | 8.5 | Use of hard-coded cryptographic key vulnerability in Johnson Controls ADVMS allows Read Sensitive Constants Within an E… |
| 2026-10-07 20:17:15 | [CVE-2026-97714](https://nvd.nist.gov/vuln/detail/CVE-2026-97714) | High | 8.2 | CVE-2026-97714 is a is a vulnerability in the authentication sub-system of Secure Access servers prior to version 14.60… |
| 2026-10-07 20:17:16 | [CVE-2026-97715](https://nvd.nist.gov/vuln/detail/CVE-2026-97715) | High | 7.1 | CVE-2026-97715 is a vulnerability in the client registration process of Secure Access servers prior to version 14.60. A… |
| 2026-10-07 20:17:16 | [CVE-2026-97716](https://nvd.nist.gov/vuln/detail/CVE-2026-97716) | High | 8.7 | CVE-2026-97716 is a vulnerability in the connection set up sub-system of Secure Access servers prior to version 14.60.… |
| 2026-10-07 20:17:16 | [CVE-2026-97717](https://nvd.nist.gov/vuln/detail/CVE-2026-97717) | Medium | 6.0 | CVE-2026-97717 is a vulnerability in the proxy sub-system of Secure Access servers prior to 14.60. Authenticated attack… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
