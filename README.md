# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-16 19:19 UTC

New CVEs published between 2026-10-16 18:18 UTC and 2026-10-16 19:19 UTC.

[Full CSV](data/new-cves-2026-10-16T19-19-52-645438Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-10-16 18:18:37 | [CVE-2026-80092](https://nvd.nist.gov/vuln/detail/CVE-2026-80092) | Medium | 5.3 | Authentication bypass by assumed-immutable data in Microsoft Identity Web allows an authorized attacker to elevate priv… |
| 2026-10-16 18:18:37 | [CVE-2026-81452](https://nvd.nist.gov/vuln/detail/CVE-2026-81452) | High | 7.0 | Dell Alienware Command Center (AWCC), versions prior to 6.14.54.0, contain a Least Privilege Violation vulnerability. A… |
| 2026-10-16 18:19:42 | [CVE-2026-89098](https://nvd.nist.gov/vuln/detail/CVE-2026-89098) | Medium | 5.5 | A flaw was found in nfs-utils. The fsidd daemon improperly handles input received over its local domain socket by relyi… |
| 2026-10-16 19:16:56 | [CVE-2025-55640](https://nvd.nist.gov/vuln/detail/CVE-2025-55640) |  |  | A heap buffer overflow in the stbl_AddSize function (isomedia/stbl_write.c) of GPAC MP4Box v2.4 allows attackers to cau… |
| 2026-10-16 19:16:57 | [CVE-2025-55653](https://nvd.nist.gov/vuln/detail/CVE-2025-55653) |  |  | GPAC MP4Box v2.4 was discovered to contain a floating point exception in the gf_parse_lfrac function (utils/error.c). P… |
| 2026-10-16 19:16:57 | [CVE-2025-66969](https://nvd.nist.gov/vuln/detail/CVE-2025-66969) |  |  | Integer overflow in OpenModSim (<=1.11.0), leading to denial of service |
| 2026-10-16 19:17:01 | [CVE-2026-102917](https://nvd.nist.gov/vuln/detail/CVE-2026-102917) | High | 7.8 | IBM i 7.3, 7.4, 7.5, and 7.6 is vulnerable to an authenticated attacker elevating their privilege. A bad actor could ex… |
| 2026-10-16 19:17:02 | [CVE-2026-107674](https://nvd.nist.gov/vuln/detail/CVE-2026-107674) | Medium | 5.1 | IBM i 7.3, 7.4, 7.5, and 7.6 is vulnerable to a denial of service to Digital Certificate Manager (DCM) for System TLS u… |
| 2026-10-16 19:17:05 | [CVE-2026-111793](https://nvd.nist.gov/vuln/detail/CVE-2026-111793) | Medium | 4.3 | Openwave Webtop Media Transcoder does not enforce administrator-defined file type restrictions to restrict the file-typ… |
| 2026-10-16 19:17:06 | [CVE-2026-17068](https://nvd.nist.gov/vuln/detail/CVE-2026-17068) | Medium | 5.4 | IBM i 7.3, 7.4, 7.5, and 7.6 could allow a local attacker to bypass NFS version restrictions due to improper enforcemen… |
| 2026-10-16 19:17:06 | [CVE-2026-17073](https://nvd.nist.gov/vuln/detail/CVE-2026-17073) | Medium | 5.4 | IBM i 7.3, 7.4, 7.5, and 7.6 could allow a local attacker to obtain sensitive information due to missing subtree checks… |
| 2026-10-16 19:17:06 | [CVE-2026-17275](https://nvd.nist.gov/vuln/detail/CVE-2026-17275) | Low | 3.7 | IBM i 7.3, 7.4, 7.5, and 7.6 could allow a remote attacker to perform unauthorized manipulation of distributed transact… |
| 2026-10-16 19:17:06 | [CVE-2026-17488](https://nvd.nist.gov/vuln/detail/CVE-2026-17488) | Medium | 4.3 | IBM i 7.3, 7.4, 7.5, and 7.6 could allow a remote authenticated attacker to bypass security restrictions due to imprope… |
| 2026-10-16 19:17:06 | [CVE-2026-17491](https://nvd.nist.gov/vuln/detail/CVE-2026-17491) | Medium | 5.4 | IBM i 7.3, 7.4, 7.5, and 7.6 is could allow a remote authenticated attacker to bypass security restrictions due to impr… |
| 2026-10-16 19:17:44 | [CVE-2026-85231](https://nvd.nist.gov/vuln/detail/CVE-2026-85231) | Medium | 6.5 | A flaw was found in libtirpc. An authenticated remote attacker could exploit this vulnerability by sending oversized wr… |
| 2026-10-16 19:17:44 | [CVE-2026-85977](https://nvd.nist.gov/vuln/detail/CVE-2026-85977) | Medium | 5.3 | A flaw was found in libtirpc. A remote attacker can exploit this vulnerability by sending specially crafted PMAPPROC_DU… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
