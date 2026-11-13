# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-11-13 14:18 UTC

New CVEs published between 2026-11-13 13:18 UTC and 2026-11-13 14:18 UTC.

[Full CSV](data/new-cves-2026-11-13T14-18-38-476825Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-11-13 14:17:47 | [CVE-2026-109095](https://nvd.nist.gov/vuln/detail/CVE-2026-109095) | Medium | 6.9 | A integer overflow in glamor Xv Image Size handling in X.Org xwayland before 24.1.15 and X server before 21.1.26 could… |
| 2026-11-13 14:17:47 | [CVE-2026-109096](https://nvd.nist.gov/vuln/detail/CVE-2026-109096) | Medium | 5.5 | Incorrect handling of negative returns from ddQueryImageAttributes() when processing XvPutImage requests in X.Org xwayl… |
| 2026-11-13 14:17:48 | [CVE-2026-116411](https://nvd.nist.gov/vuln/detail/CVE-2026-116411) | High | 8.8 | Dell PowerStore contains a Server-Side Request Forgery (SSRF) vulnerability. An authenticated user with limited privile… |
| 2026-11-13 14:17:48 | [CVE-2026-116412](https://nvd.nist.gov/vuln/detail/CVE-2026-116412) | Medium | 5.5 | Dell PowerStore contains an insecure-file-permissions vulnerability. A local low-privileged attacker could exploit this… |
| 2026-11-13 14:17:48 | [CVE-2026-116413](https://nvd.nist.gov/vuln/detail/CVE-2026-116413) | High | 7.1 | Dell PowerStore contains a use-of-broken-cryptography vulnerability. A low-privileged attacker could exploit it to impe… |
| 2026-11-13 14:17:50 | [CVE-2026-124758](https://nvd.nist.gov/vuln/detail/CVE-2026-124758) | Low | 2.3 | P-Net before 1.0.4 does not check the record data length of an IODWrite request to a non-user record index against the… |
| 2026-11-13 14:17:50 | [CVE-2026-124759](https://nvd.nist.gov/vuln/detail/CVE-2026-124759) | High | 7.1 | P-Net before 1.0.4 routes a received RTA alarm frame to an Application Relationship using only the destination alarm re… |
| 2026-11-13 14:17:50 | [CVE-2026-124760](https://nvd.nist.gov/vuln/detail/CVE-2026-124760) | Low | 2.3 | P-Net before 1.0.4 sets the alarm receiver state to waiting for confirmation before the data of a received alarm notifi… |
| 2026-11-13 14:17:50 | [CVE-2026-124761](https://nvd.nist.gov/vuln/detail/CVE-2026-124761) | High | 7.1 | P-Net before 1.0.4 copies the IP suite of a DCP Set request to the current and the non-volatile configuration, and star… |
| 2026-11-13 14:17:50 | [CVE-2026-124762](https://nvd.nist.gov/vuln/detail/CVE-2026-124762) | Medium | 6.0 | P-Net before 1.0.4 finds the RPC session of a received PDU by its activity UUID only, and a reject, fault or cancel PDU… |
| 2026-11-13 14:17:53 | [CVE-2026-125800](https://nvd.nist.gov/vuln/detail/CVE-2026-125800) | Medium | 6.5 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in Brainstorm Force… |
| 2026-11-13 14:17:54 | [CVE-2026-127122](https://nvd.nist.gov/vuln/detail/CVE-2026-127122) | High | 7.2 | P-Net before 1.0.4 does not check the number of MCR request blocks in a Connect request against the number of multicast… |
| 2026-11-13 14:17:54 | [CVE-2026-127123](https://nvd.nist.gov/vuln/detail/CVE-2026-127123) | Medium | 6.0 | P-Net before 1.0.4 releases the Application Relationship of an RPC session, without the abort procedure, when a fragmen… |
| 2026-11-13 14:17:54 | [CVE-2026-127124](https://nvd.nist.gov/vuln/detail/CVE-2026-127124) | High | 7.1 | P-Net before 1.0.4 keeps the RPC session that is allocated for a fragment of a request with an unknown activity UUID, w… |
| 2026-11-13 14:17:55 | [CVE-2026-127125](https://nvd.nist.gov/vuln/detail/CVE-2026-127125) | Medium | 6.0 | P-Net before 1.0.4 aborts the Application Relationship of an RPC session when a fragment of a response has been resent… |
| 2026-11-13 14:17:55 | [CVE-2026-128790](https://nvd.nist.gov/vuln/detail/CVE-2026-128790) | High | 7.1 | In Eclipse BaSyx Go Components versions up to and including 1.1.2, ABAC-enabled deployments of the Submodel Repository… |
| 2026-11-13 14:18:00 | [CVE-2026-77706](https://nvd.nist.gov/vuln/detail/CVE-2026-77706) | Medium | 6.5 | Improper handling of highly compressed data (data amplification) vulnerability in Fileorbis Bilişim Hizmetleri Ticaret… |
| 2026-11-13 14:18:00 | [CVE-2026-82177](https://nvd.nist.gov/vuln/detail/CVE-2026-82177) | High | 7.2 | Dell PowerStore contains an OS Command Injection vulnerability. A high-privileged attacker could exploit this vulnerabi… |
| 2026-11-13 14:18:00 | [CVE-2026-82179](https://nvd.nist.gov/vuln/detail/CVE-2026-82179) | Medium | 4.9 | Dell PowerStore contains an authorization bypass vulnerability. An authenticated administrator could exploit this vulne… |
| 2026-11-13 14:18:00 | [CVE-2026-86353](https://nvd.nist.gov/vuln/detail/CVE-2026-86353) | Medium | 5.0 | Dell PowerStore contains a use of a weak cryptographic algorithm vulnerability that could allow an attacker with existi… |
| 2026-11-13 14:18:01 | [CVE-2026-91094](https://nvd.nist.gov/vuln/detail/CVE-2026-91094) |  |  | A directory traversal bug was discovered when unpacking 3.0 (quilt) source packages, where the packaging tarball could… |
| 2026-11-13 14:18:01 | [CVE-2026-92241](https://nvd.nist.gov/vuln/detail/CVE-2026-92241) | Medium | 5.7 | The AVRCP browsing channel's L2CAP receive-buffer callback, browsing_avrcp_l2cap_alloc_buf() in subsys/bluetooth/host/c… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
