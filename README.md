# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-11-18 03:21 UTC

New CVEs published between 2026-11-18 02:19 UTC and 2026-11-18 03:21 UTC.

[Full CSV](data/new-cves-2026-11-18T03-21-31-49247Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-11-18 03:17:39 | [CVE-2026-107949](https://nvd.nist.gov/vuln/detail/CVE-2026-107949) | Medium | 6.5 | A SQL injection vulnerability affects an administrative API in HCL Commerce versions 8, 9.0.1 and 9.1.0 - 9.1.21. A rem… |
| 2026-11-18 03:17:40 | [CVE-2026-107950](https://nvd.nist.gov/vuln/detail/CVE-2026-107950) | High | 8.2 | An XML External Entity (XXE) vulnerability affects a Storefront REST API in HCL Commerce versions 8, 9.0.1 and 9.1.x. A… |
| 2026-11-18 03:17:40 | [CVE-2026-117634](https://nvd.nist.gov/vuln/detail/CVE-2026-117634) | Medium | 6.9 | Pleasanter contains an incorrect authorization vulnerability in Publishing feature. If this vulnerability is exploited,… |
| 2026-11-18 03:17:40 | [CVE-2026-120472](https://nvd.nist.gov/vuln/detail/CVE-2026-120472) | Medium | 5.9 | A flaw was found in OpenShift Hive. The ClusterClaim controller assigns hive-claim-owner RBAC based on a user-controlle… |
| 2026-11-18 03:17:40 | [CVE-2026-121811](https://nvd.nist.gov/vuln/detail/CVE-2026-121811) | Medium | 5.3 | Pleasanter contains an issue with improper limitation of a pathname to a restricted directory ('Path Traversal') in the… |
| 2026-11-18 03:17:40 | [CVE-2026-125276](https://nvd.nist.gov/vuln/detail/CVE-2026-125276) | High | 7.1 | Pleasanter contains an issue with insertion of sensitive information into sent data in the API. If the affected product… |
| 2026-11-18 03:17:41 | [CVE-2026-125411](https://nvd.nist.gov/vuln/detail/CVE-2026-125411) | Medium | 5.3 | Pleasanter contains an incorrect authorization vulnerability in the access control of Items. If this vulnerability is e… |
| 2026-11-18 03:17:41 | [CVE-2026-131800](https://nvd.nist.gov/vuln/detail/CVE-2026-131800) | High | 8.3 | A stored cross-site scripting vulnerability was identified in GitHub Enterprise Server that allowed an organization mem… |
| 2026-11-18 03:17:41 | [CVE-2026-131871](https://nvd.nist.gov/vuln/detail/CVE-2026-131871) | High | 8.5 | WLA DX 9.7 through 10.7 contains a stack-based buffer overflow vulnerability in parse_data_blocks() in wlalink/analyze.… |
| 2026-11-18 03:17:41 | [CVE-2026-131872](https://nvd.nist.gov/vuln/detail/CVE-2026-131872) | Medium | 6.8 | SOIL2 before 1.4.2 contains a NULL pointer dereference vulnerability in its DDS, PVR and PKM image loaders that write r… |
| 2026-11-18 03:17:41 | [CVE-2026-131873](https://nvd.nist.gov/vuln/detail/CVE-2026-131873) | Medium | 6.9 | Gargoyle 2023.1 through 2026.1.1 contains a stack-based buffer overflow vulnerability in the bundled Plus interpreter's… |
| 2026-11-18 03:17:42 | [CVE-2026-131874](https://nvd.nist.gov/vuln/detail/CVE-2026-131874) | Medium | 6.8 | Gargoyle 2023.1 through 2026.1.1 contains an infinite loop vulnerability in the bundled Plus interpreter's ReadString()… |
| 2026-11-18 03:17:42 | [CVE-2026-131875](https://nvd.nist.gov/vuln/detail/CVE-2026-131875) | High | 8.7 | fqterm before 0.9.11 contains a heap out-of-bounds write vulnerability in FQTermDecode that allows malicious servers to… |
| 2026-11-18 03:17:42 | [CVE-2026-131876](https://nvd.nist.gov/vuln/detail/CVE-2026-131876) | High | 7.1 | fqterm 0.9.9 before 0.9.11 contains an out-of-bounds memory access vulnerability in its SSH client that trusts unchecke… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
