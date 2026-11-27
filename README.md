# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-11-27 14:18 UTC

New CVEs published between 2026-11-27 13:18 UTC and 2026-11-27 14:18 UTC.

[Full CSV](data/new-cves-2026-11-27T14-18-45-662415Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-11-27 14:17:01 | [CVE-2026-118968](https://nvd.nist.gov/vuln/detail/CVE-2026-118968) | Low | 1.0 | A denial-of-service vulnerability in the Qt WAV audio decoding of the Qt Multimedia module |
| 2026-11-27 14:17:01 | [CVE-2026-123757](https://nvd.nist.gov/vuln/detail/CVE-2026-123757) | High | 7.4 | An attacker can send a notify request that causes the root zone to be added as a secondary domain to be added to the bi… |
| 2026-11-27 14:17:01 | [CVE-2026-123758](https://nvd.nist.gov/vuln/detail/CVE-2026-123758) | Medium | 4.4 | A race condition in the handling of the forward notification requests queue can lead to a crash if too many UDP notify… |
| 2026-11-27 14:17:01 | [CVE-2026-123759](https://nvd.nist.gov/vuln/detail/CVE-2026-123759) | Medium | 4.8 | A catalog zone provider can add a root zone as member and cause PowerDNS to provision it from the given source. |
| 2026-11-27 14:17:01 | [CVE-2026-123760](https://nvd.nist.gov/vuln/detail/CVE-2026-123760) | Medium | 6.5 | When using the LMDB backend, performing zone rectification when the number of Empty Non-Terminal entries is larger than… |
| 2026-11-27 14:17:01 | [CVE-2026-123761](https://nvd.nist.gov/vuln/detail/CVE-2026-123761) | High | 8.2 | Various logic errors in view processing can cause incorrect cached results to be returned. |
| 2026-11-27 14:17:01 | [CVE-2026-123762](https://nvd.nist.gov/vuln/detail/CVE-2026-123762) | High | 7.6 | A catalog zone update introducing a new zone which already exists, but in a different backend than the one storing the… |
| 2026-11-27 14:17:01 | [CVE-2026-123764](https://nvd.nist.gov/vuln/detail/CVE-2026-123764) | High | 7.5 | Incorrect sanitization of received data during zone AXFR to Bind backend can cause wrong or invalid data to be serializ… |
| 2026-11-27 14:17:02 | [CVE-2026-124727](https://nvd.nist.gov/vuln/detail/CVE-2026-124727) | Medium | 6.5 | Incorrect handling of obsolete record types during zone AXFR to Bind backend will cause the zone to fail to load afterw… |
| 2026-11-27 14:17:02 | [CVE-2026-124728](https://nvd.nist.gov/vuln/detail/CVE-2026-124728) | High | 7.5 | Incomplete GSS negotiation, as well as TKEY context deletion while a pending operation will need to be signed with that… |
| 2026-11-27 14:17:02 | [CVE-2026-124981](https://nvd.nist.gov/vuln/detail/CVE-2026-124981) | Critical | 9.4 | A vulnerability has been identified in Mendix OIDC Provider (Mendix 10 compatible) (All versions < V6.0.0), Mendix OIDC… |
| 2026-11-27 14:17:02 | [CVE-2026-134708](https://nvd.nist.gov/vuln/detail/CVE-2026-134708) | High | 8.6 | Improper Limitation of a Pathname to a Restricted Directory ('Path Traversal') vulnerability in VideoWhisper.com Video… |
| 2026-11-27 14:17:02 | [CVE-2026-134956](https://nvd.nist.gov/vuln/detail/CVE-2026-134956) | Medium | 6.5 | Improper Neutralization of Script-Related HTML Tags in a Web Page (Basic XSS) vulnerability in Acato WP REST Cache wp-r… |
| 2026-11-27 14:17:02 | [CVE-2026-134982](https://nvd.nist.gov/vuln/detail/CVE-2026-134982) | High | 7.1 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in Amauri.IO WPMobil… |
| 2026-11-27 14:17:02 | [CVE-2026-134983](https://nvd.nist.gov/vuln/detail/CVE-2026-134983) | High | 7.1 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in Muralidharan Rama… |
| 2026-11-27 14:17:03 | [CVE-2026-134987](https://nvd.nist.gov/vuln/detail/CVE-2026-134987) | High | 8.6 | Improper Limitation of a Pathname to a Restricted Directory ('Path Traversal') vulnerability in Nickboss WordPress File… |
| 2026-11-27 14:17:03 | [CVE-2026-134993](https://nvd.nist.gov/vuln/detail/CVE-2026-134993) | High | 7.5 | Path Traversal: '.../...//' vulnerability in Seraphinite Solutions Seraphinite Accelerator seraphinite-accelerator allo… |
| 2026-11-27 14:17:03 | [CVE-2026-134994](https://nvd.nist.gov/vuln/detail/CVE-2026-134994) | Critical | 9.8 | Deserialization of Untrusted Data vulnerability in Nitramix Revertix &#8211; Backup, Migration, Staging &amp; Clone rev… |
| 2026-11-27 14:17:03 | [CVE-2026-135009](https://nvd.nist.gov/vuln/detail/CVE-2026-135009) | Critical | 9.3 | Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection') vulnerability in David Lingren Med… |
| 2026-11-27 14:17:03 | [CVE-2026-135032](https://nvd.nist.gov/vuln/detail/CVE-2026-135032) | High | 7.5 | Missing Authorization vulnerability in Everest Forms Everest Forms everest-forms allows Exploiting Incorrectly Configur… |
| 2026-11-27 14:17:03 | [CVE-2026-135048](https://nvd.nist.gov/vuln/detail/CVE-2026-135048) | High | 8.8 | Incorrect Privilege Assignment vulnerability in weDevs WP ERP erp allows Privilege Escalation.This issue affects WP ERP… |
| 2026-11-27 14:17:03 | [CVE-2026-135278](https://nvd.nist.gov/vuln/detail/CVE-2026-135278) | Medium | 5.3 | A vulnerability has been identified in Mendix Runtime V10 (All versions < V10.24.29), Mendix Runtime V11 (All versions… |
| 2026-11-27 14:17:04 | [CVE-2026-135923](https://nvd.nist.gov/vuln/detail/CVE-2026-135923) | High | 7.1 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in WPTasty AWP Class… |
| 2026-11-27 14:17:04 | [CVE-2026-135953](https://nvd.nist.gov/vuln/detail/CVE-2026-135953) | High | 7.1 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in WS Form WS Form L… |
| 2026-11-27 14:17:04 | [CVE-2026-137936](https://nvd.nist.gov/vuln/detail/CVE-2026-137936) | Medium | 6.0 | Payload 3.25.0 before 3.90.0 and 4.0.0-canary.0 before 4.0.0-canary.34 contains an authorization bypass through a user-… |
| 2026-11-27 14:17:04 | [CVE-2026-137937](https://nvd.nist.gov/vuln/detail/CVE-2026-137937) | Medium | 6.9 | PDFio before 1.6.5 contains an integer underflow in _pdfioCryptoAESDecrypt() in pdfio-aes.c, which strips PKCS#7 paddin… |
| 2026-11-27 14:17:04 | [CVE-2026-137938](https://nvd.nist.gov/vuln/detail/CVE-2026-137938) | High | 7.3 | Sparkle before 2.9.6 contains a time-of-check time-of-use race condition in the installer's SPUInstallationData handlin… |
| 2026-11-27 14:17:04 | [CVE-2026-137939](https://nvd.nist.gov/vuln/detail/CVE-2026-137939) | High | 7.3 | Sparkle 2.2.0 before 2.9.6 contains a link following vulnerability in -submitInstallerAtPath: in SUInstallerLauncher.m… |
| 2026-11-27 14:17:05 | [CVE-2026-137940](https://nvd.nist.gov/vuln/detail/CVE-2026-137940) | Medium | 5.7 | Pillow through 13.1.0 contains an integer overflow in the ImageMath integer divide and modulo operators (DIV_I and MOD_… |
| 2026-11-27 14:17:05 | [CVE-2026-137942](https://nvd.nist.gov/vuln/detail/CVE-2026-137942) | Medium | 5.3 | Roundcube Webmail before 1.6.19 and 1.7.x before 1.7.4 contains an authorization bypass in add_to_group() and remove_fr… |
| 2026-11-27 14:17:05 | [CVE-2026-137943](https://nvd.nist.gov/vuln/detail/CVE-2026-137943) | Medium | 5.1 | Roundcube Webmail before 1.6.19 and 1.7.x before 1.7.4 contains a cross-site scripting vulnerability in compose_part_bo… |
| 2026-11-27 14:17:05 | [CVE-2026-80480](https://nvd.nist.gov/vuln/detail/CVE-2026-80480) | Medium | 6.8 | Dell Secure Connect Gateway - Virtual Edition, versions prior to 5.36.00.16, contains an Improper Certificate Validatio… |
| 2026-11-27 14:17:05 | [CVE-2026-80481](https://nvd.nist.gov/vuln/detail/CVE-2026-80481) | Medium | 5.5 | Dell Secure Connect Gateway - Virtual Edition, versions prior to 5.36.00.16, contains an Insertion of Sensitive Informa… |
| 2026-11-27 14:17:05 | [CVE-2026-80482](https://nvd.nist.gov/vuln/detail/CVE-2026-80482) | Low | 3.3 | Dell Secure Connect Gateway - Virtual Edition, versions prior to 5.36.00.16, contains a J2EE Bad Practices: Use of Syst… |
| 2026-11-27 14:17:05 | [CVE-2026-80483](https://nvd.nist.gov/vuln/detail/CVE-2026-80483) | High | 7.3 | Dell Secure Connect Gateway - Virtual Edition, versions prior to 5.36.00.16, contains an Off-by-one Error vulnerability… |
| 2026-11-27 14:17:06 | [CVE-2026-80484](https://nvd.nist.gov/vuln/detail/CVE-2026-80484) | Medium | 5.5 | Dell Secure Connect Gateway - Virtual Edition, versions prior to 5.36.00.16, contains a Use of Hard-coded Cryptographic… |
| 2026-11-27 14:17:06 | [CVE-2026-80485](https://nvd.nist.gov/vuln/detail/CVE-2026-80485) | High | 8.4 | Dell Secure Connect Gateway - Virtual Edition, versions prior to 5.36.00.16, contains an Improper Neutralization of Spe… |
| 2026-11-27 14:17:06 | [CVE-2026-80498](https://nvd.nist.gov/vuln/detail/CVE-2026-80498) | High | 7.8 | Dell Secure Connect Gateway - Virtual Edition, versions prior to 5.36.00.16, contains a Use of Hard-coded Cryptographic… |
| 2026-11-27 14:17:06 | [CVE-2026-80499](https://nvd.nist.gov/vuln/detail/CVE-2026-80499) | Medium | 6.1 | Dell Secure Connect Gateway - Virtual Edition, versions prior to 5.36.00.16, contains an External Control of File Name… |
| 2026-11-27 14:17:06 | [CVE-2026-80500](https://nvd.nist.gov/vuln/detail/CVE-2026-80500) | High | 7.7 | Dell Secure Connect Gateway - Virtual Edition, versions prior to 5.36.00.16, contains an Improper Authentication vulner… |
| 2026-11-27 14:17:06 | [CVE-2026-80501](https://nvd.nist.gov/vuln/detail/CVE-2026-80501) | High | 7.8 | Dell Secure Connect Gateway - Virtual Edition, versions prior to 5.36.00.16, contains an Incorrect Permission Assignmen… |
| 2026-11-27 14:17:06 | [CVE-2026-80502](https://nvd.nist.gov/vuln/detail/CVE-2026-80502) | Medium | 6.8 | Dell Secure Connect Gateway - Virtual Edition, versions prior to 5.36.00.16, contains an Improper Certificate Validatio… |
| 2026-11-27 14:17:06 | [CVE-2026-80503](https://nvd.nist.gov/vuln/detail/CVE-2026-80503) | Medium | 6.1 | Dell Secure Connect Gateway - Virtual Edition, versions prior to 5.36.00.16, contains an Insertion of Sensitive Informa… |
| 2026-11-27 14:17:07 | [CVE-2026-80504](https://nvd.nist.gov/vuln/detail/CVE-2026-80504) | Medium | 5.3 | Dell Secure Connect Gateway - Virtual Edition, versions prior to 5.36.00.16, contains a Concurrent Execution using Shar… |
| 2026-11-27 14:17:07 | [CVE-2026-85258](https://nvd.nist.gov/vuln/detail/CVE-2026-85258) | Critical | 9.3 | A Missing Authorization vulnerability in the private console API in Google Cloud Vertex AI (Vertex AI Assistant) versio… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
