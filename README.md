# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-11-12 19:21 UTC

New CVEs published between 2026-11-12 18:20 UTC and 2026-11-12 19:21 UTC.

[Full CSV](data/new-cves-2026-11-12T19-21-07-554583Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-11-12 19:16:44 | [CVE-2024-21954](https://nvd.nist.gov/vuln/detail/CVE-2024-21954) | High | 7.0 | Improper exception handling in IOMMU could allow an invalidate command to be sent to PCIe devices that do not support A… |
| 2026-11-12 19:16:45 | [CVE-2025-54501](https://nvd.nist.gov/vuln/detail/CVE-2025-54501) | Medium | 5.9 | Improper access control on an internal debug interface could allow a high privileged attacker to bypass memory access c… |
| 2026-11-12 19:16:45 | [CVE-2026-0004](https://nvd.nist.gov/vuln/detail/CVE-2026-0004) | Medium | 5.7 | A transient execution vulnerability in some AMD processors may allow an attacker with the ability to execute code on th… |
| 2026-11-12 19:16:45 | [CVE-2026-0101](https://nvd.nist.gov/vuln/detail/CVE-2026-0101) | Medium | 6.8 | Improper validation of specified quantities in input within AMD Power Management Firmware (PMFW) could allow a local at… |
| 2026-11-12 19:16:45 | [CVE-2026-0436](https://nvd.nist.gov/vuln/detail/CVE-2026-0436) | Medium | 6.9 | Insufficient parameter sanitization in the AMD Secure Processor (ASP) trusted execution environment (TEE) SPDM driver c… |
| 2026-11-12 19:16:47 | [CVE-2026-117542](https://nvd.nist.gov/vuln/detail/CVE-2026-117542) | Medium | 5.1 | Joomla Extension - jdownloads.com - Authenticated path traversal in jDownloads < 4.1.8 - A manipulated `update_file` fo… |
| 2026-11-12 19:16:47 | [CVE-2026-117544](https://nvd.nist.gov/vuln/detail/CVE-2026-117544) | High | 8.2 | Joomla Extension - jdownloads.com - IDOR allowing restricted file downloads in jDownloads < 4.1.8 - The `other_file_id`… |
| 2026-11-12 19:16:48 | [CVE-2026-120033](https://nvd.nist.gov/vuln/detail/CVE-2026-120033) | Medium | 6.0 | In FRRouting 10.1 and later, bgpd does not correctly close a BGP session when the Send Hold Timer (RFC 9687) expires, i… |
| 2026-11-12 19:16:48 | [CVE-2026-120467](https://nvd.nist.gov/vuln/detail/CVE-2026-120467) | High | 7.1 | Joomla / WordPress Extension - acymailing.com - Subscriber identity not bound to the record acted upon in AcyMailing 1.… |
| 2026-11-12 19:16:48 | [CVE-2026-121619](https://nvd.nist.gov/vuln/detail/CVE-2026-121619) | Medium | 6.3 | The Symfony FrameworkBundle framework.trusted_proxies option and the HttpFoundation Request::setTrustedProxies() method… |
| 2026-11-12 19:16:56 | [CVE-2026-126203](https://nvd.nist.gov/vuln/detail/CVE-2026-126203) | Medium | 6.1 | Loofah is a general library for manipulating and transforming HTML/XML documents and fragments, built on top of Nokogir… |
| 2026-11-12 19:16:56 | [CVE-2026-126204](https://nvd.nist.gov/vuln/detail/CVE-2026-126204) | Low | 3.7 | express-rate-limit is a basic rate-limiting middleware for Express. From 8.6.0 until 8.7.2, the built-in MemoryStore re… |
| 2026-11-12 19:17:01 | [CVE-2026-126838](https://nvd.nist.gov/vuln/detail/CVE-2026-126838) | Medium | 5.7 | A MongoDB Rust Driver component that holds client-side field level encryption settings includes key management service… |
| 2026-11-12 19:17:03 | [CVE-2026-127119](https://nvd.nist.gov/vuln/detail/CVE-2026-127119) | Medium | 5.9 | Unverified ownership of the default cluster log location in the EMR module in AWS SDK for pandas (awswrangler) from 1.1… |
| 2026-11-12 19:17:03 | [CVE-2026-127235](https://nvd.nist.gov/vuln/detail/CVE-2026-127235) | Medium | 6.1 | A reflected cross-site scripting vulnerability exists in the web user interface of multiple versions of OpenNMS Meridia… |
| 2026-11-12 19:17:03 | [CVE-2026-127236](https://nvd.nist.gov/vuln/detail/CVE-2026-127236) | Medium | 5.4 | An argument injection vulnerability exists in the ad-hoc RRD graph feature of multiple versions of OpenNMS Meridian and… |
| 2026-11-12 19:17:04 | [CVE-2026-18379](https://nvd.nist.gov/vuln/detail/CVE-2026-18379) | High | 8.8 | A flaw was found in yggdrasil-worker-package-manager. An authenticated attacker can exploit this issue to achieve arbit… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
