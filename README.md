# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-11-24 16:19 UTC

New CVEs published between 2026-11-24 15:20 UTC and 2026-11-24 16:19 UTC.

[Full CSV](data/new-cves-2026-11-24T16-19-56-812932Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-11-24 16:17:53 | [CVE-2026-115747](https://nvd.nist.gov/vuln/detail/CVE-2026-115747) | Medium | 5.9 | Improper Restriction of Operations within the Bounds of a Memory Buffer vulnerability in the AArch64 JIT in Erlang OTP… |
| 2026-11-24 16:17:53 | [CVE-2026-125658](https://nvd.nist.gov/vuln/detail/CVE-2026-125658) | Medium | 5.7 | Use After Free vulnerability in Erlang/OTP erts allows an attacker who can create a file system entry with a chosen nam… |
| 2026-11-24 16:17:54 | [CVE-2026-132157](https://nvd.nist.gov/vuln/detail/CVE-2026-132157) | High | 8.7 | The OSI Presentation Protocol analyzer in DINA-community's icsnpp-pres 1.0.0 plugin for Zeek uses an incompatible ASN.1… |
| 2026-11-24 16:17:55 | [CVE-2026-132887](https://nvd.nist.gov/vuln/detail/CVE-2026-132887) | High | 8.7 | The DINA-community icsnpp-acse 1.0.0 plugin for Zeek does not release partially decoded ACSE protocol data units when A… |
| 2026-11-24 16:17:55 | [CVE-2026-133002](https://nvd.nist.gov/vuln/detail/CVE-2026-133002) | High | 8.7 | The DINA-community icsnpp-mms 1.0.0 plugin for Zeek does not release partially decoded Manufacturing Message Specificat… |
| 2026-11-24 16:17:59 | [CVE-2026-135479](https://nvd.nist.gov/vuln/detail/CVE-2026-135479) | Medium | 6.9 | Merchant for WooCommerce before 2.3.3 contains a missing authorization vulnerability in the Quick View module that allo… |
| 2026-11-24 16:18:16 | [CVE-2026-135786](https://nvd.nist.gov/vuln/detail/CVE-2026-135786) | Low | 2.1 | A vulnerability was identified in zhayujie CowAgent up to 2.2.1. This impacts the function _create_task of the file age… |
| 2026-11-24 16:18:16 | [CVE-2026-135787](https://nvd.nist.gov/vuln/detail/CVE-2026-135787) | Medium | 5.5 | A security flaw has been discovered in hrshadhin CloudSchool up to 3.0.1. Affected is the function ReportController::ma… |
| 2026-11-24 16:18:17 | [CVE-2026-136214](https://nvd.nist.gov/vuln/detail/CVE-2026-136214) | Medium | 4.8 | Astra WordPress theme before 4.14.0 contains an improper input neutralization vulnerability that allows authenticated a… |
| 2026-11-24 16:18:17 | [CVE-2026-136226](https://nvd.nist.gov/vuln/detail/CVE-2026-136226) |  |  | By adding a From header with lowercase name before the actual From header, an attacker could make Thunderbird display a… |
| 2026-11-24 16:18:17 | [CVE-2026-136227](https://nvd.nist.gov/vuln/detail/CVE-2026-136227) |  |  | By combining several weaknesses, a crafted email could, when opened, inject commands into the authenticated IMAP connec… |
| 2026-11-24 16:18:17 | [CVE-2026-136228](https://nvd.nist.gov/vuln/detail/CVE-2026-136228) |  |  | Thunderbird did not compare the signature creation time with the message date for messages that were both signed and en… |
| 2026-11-24 16:18:17 | [CVE-2026-136229](https://nvd.nist.gov/vuln/detail/CVE-2026-136229) |  |  | When a signed OpenPGP/MIME message had no Date header, or one that could not be parsed, Thunderbird did not compare the… |
| 2026-11-24 16:18:18 | [CVE-2026-136230](https://nvd.nist.gov/vuln/detail/CVE-2026-136230) |  |  | When a CardDAV address book was accessed through an HTTP proxy that requested authentication, Thunderbird could answer… |
| 2026-11-24 16:18:18 | [CVE-2026-136231](https://nvd.nist.gov/vuln/detail/CVE-2026-136231) |  |  | A received message could include an attachment that referred to an arbitrary local file under a misleading name. If the… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
