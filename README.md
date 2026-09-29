# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-09-29 00:19 UTC

New CVEs published between 2026-09-28 23:20 UTC and 2026-09-29 00:19 UTC.

[Full CSV](data/new-cves-2026-09-29T00-19-33-725659Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-09-29 00:17:01 | [CVE-2026-101263](https://nvd.nist.gov/vuln/detail/CVE-2026-101263) | High | 8.5 | A vulnerability was found in Ziroom ZHOME A0101 1.0.1.0. This issue affects some unknown processing of the file /api/ZR… |
| 2026-09-29 00:17:02 | [CVE-2026-101264](https://nvd.nist.gov/vuln/detail/CVE-2026-101264) | High | 8.5 | A vulnerability was determined in Ziroom ZHOME A0101 1.0.1.0. Impacted is an unknown function of the file /api/ZRnetwor… |
| 2026-09-29 00:17:02 | [CVE-2026-101265](https://nvd.nist.gov/vuln/detail/CVE-2026-101265) | Low | 1.3 | A vulnerability was identified in Intelbras TIP 125i 4.3.35/4.3.41. The affected element is an unknown function of the… |
| 2026-09-29 00:17:03 | [CVE-2026-101277](https://nvd.nist.gov/vuln/detail/CVE-2026-101277) | Medium | 5.5 | A security flaw has been discovered in Trusted Domain Project OpenDKIM up to 2.11.0. The impacted element is the functi… |
| 2026-09-29 00:17:03 | [CVE-2026-102361](https://nvd.nist.gov/vuln/detail/CVE-2026-102361) | Critical | 9.3 | mall4j through 4.0 contains a missing authentication vulnerability in the PUT /user/updatePwd endpoint that allows unau… |
| 2026-09-29 00:17:03 | [CVE-2026-102362](https://nvd.nist.gov/vuln/detail/CVE-2026-102362) | Medium | 6.9 | mall4j through 4.0 fails to implement authentication controls on the DELETE /prodComm endpoint in ProdCommController. U… |
| 2026-09-29 00:17:03 | [CVE-2026-102363](https://nvd.nist.gov/vuln/detail/CVE-2026-102363) | Medium | 6.3 | mall4j through 4.0 contains a missing authentication vulnerability in the DeliveryController checkDelivery endpoint tha… |
| 2026-09-29 00:17:03 | [CVE-2026-102364](https://nvd.nist.gov/vuln/detail/CVE-2026-102364) | Medium | 5.3 | mall4j through 4.0 fails to validate the sysType field in sa-token sessions, allowing storefront customers to authentic… |
| 2026-09-29 00:17:03 | [CVE-2026-102365](https://nvd.nist.gov/vuln/detail/CVE-2026-102365) | High | 7.1 | mall4j through 4.0 fails to enforce authorization checks on GET endpoints in UserAddrController that retrieve customer… |
| 2026-09-29 00:17:03 | [CVE-2026-102366](https://nvd.nist.gov/vuln/detail/CVE-2026-102366) | Low | 2.1 | mall4j through 4.0 contains an unrestricted file upload vulnerability in FileController endpoints that lack authorizati… |
| 2026-09-29 00:17:04 | [CVE-2026-102367](https://nvd.nist.gov/vuln/detail/CVE-2026-102367) | Medium | 5.3 | mall4j through 4.0 contains an insufficient session expiration vulnerability in the token refresh endpoint that fails t… |
| 2026-09-29 00:17:04 | [CVE-2026-18417](https://nvd.nist.gov/vuln/detail/CVE-2026-18417) | Medium | 6.5 | The native BSD-socket layer recorded a pending asynchronous socket error by type-punning it into struct net_context's v… |
| 2026-09-29 00:17:04 | [CVE-2026-18746](https://nvd.nist.gov/vuln/detail/CVE-2026-18746) | Medium | 5.9 | parse_write_op() in subsys/net/lib/lwm2m/lwm2m_message_handling.c handles inbound CoAP WRITE/CREATE requests that carry… |
| 2026-09-29 00:17:04 | [CVE-2026-18747](https://nvd.nist.gov/vuln/detail/CVE-2026-18747) | Medium | 6.8 | The MCUmgr SMP-over-console transport decodes a base64 frame, reads a 16-bit packet length from it, verifies a CRC and… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
