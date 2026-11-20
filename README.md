# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-11-20 13:21 UTC

New CVEs published between 2026-11-20 12:18 UTC and 2026-11-20 13:21 UTC.

[Full CSV](data/new-cves-2026-11-20T13-21-52-231323Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-11-20 13:18:34 | [CVE-2026-101340](https://nvd.nist.gov/vuln/detail/CVE-2026-101340) | Critical | 9.1 | Net::DNS uses a 16-bit query ID to match responses to the corresponding requests. In versions up to and including 1.57,… |
| 2026-11-20 13:18:35 | [CVE-2026-109878](https://nvd.nist.gov/vuln/detail/CVE-2026-109878) | High | 7.1 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in Elementor Element… |
| 2026-11-20 13:18:36 | [CVE-2026-128997](https://nvd.nist.gov/vuln/detail/CVE-2026-128997) | High | 7.5 | Missing Authorization vulnerability in RomanCode MapSVG mapsvg-lite-interactive-vector-maps allows Exploiting Incorrect… |
| 2026-11-20 13:18:37 | [CVE-2026-129073](https://nvd.nist.gov/vuln/detail/CVE-2026-129073) | Critical | 9.8 | Authentication Bypass Using an Alternate Path or Channel vulnerability in miniOrange miniorange otp verification minior… |
| 2026-11-20 13:18:41 | [CVE-2026-129420](https://nvd.nist.gov/vuln/detail/CVE-2026-129420) | Medium | 6.9 | Joomla Extension - joomlatools.com - Local file read through remote document links in DOCman extension < 6.2.2 - Remote… |
| 2026-11-20 13:18:41 | [CVE-2026-129421](https://nvd.nist.gov/vuln/detail/CVE-2026-129421) | Medium | 5.1 | Joomla Extension - joomlatools.com - Server-side request forgery in URL uploads in DOCman extension < 6.2.2 - The URL p… |
| 2026-11-20 13:18:42 | [CVE-2026-129423](https://nvd.nist.gov/vuln/detail/CVE-2026-129423) | High | 7.5 | Joomla Extension - phoca.cz - Stored XSS through author website in frontend upload in Phoca Download extension 3.0.6-6.… |
| 2026-11-20 13:18:42 | [CVE-2026-129424](https://nvd.nist.gov/vuln/detail/CVE-2026-129424) | High | 8.7 | Joomla Extension - solidres.com - Unauthenticated stored XSS through guest reservation details in Solidres extension 1.… |
| 2026-11-20 13:18:42 | [CVE-2026-131171](https://nvd.nist.gov/vuln/detail/CVE-2026-131171) | Medium | 5.3 | A bug caused room permissions to leak into the world permissions of the acting user during certain actions. |
| 2026-11-20 13:18:44 | [CVE-2026-133606](https://nvd.nist.gov/vuln/detail/CVE-2026-133606) | Medium | 6.9 | A weakness has been identified in PowerJob up to 5.1.7. This affects the function CustomHttpServletRequestWrapper of th… |
| 2026-11-20 13:18:45 | [CVE-2026-133607](https://nvd.nist.gov/vuln/detail/CVE-2026-133607) | Medium | 6.9 | A vulnerability was determined in tianshiyeben wgcloud up to 4.0.1. This vulnerability affects unknown code of the file… |
| 2026-11-20 13:18:45 | [CVE-2026-133608](https://nvd.nist.gov/vuln/detail/CVE-2026-133608) | Medium | 6.9 | A vulnerability was identified in OpenZipkin Zipkin 3.6.1. This affects the function UnzippingBytesRequestConverter.con… |
| 2026-11-20 13:18:45 | [CVE-2026-133699](https://nvd.nist.gov/vuln/detail/CVE-2026-133699) | Low | 2.3 | free5GC SMF through 1.4.6 contains a resource exhaustion vulnerability because sendPDUSessionEstablishmentAccept return… |
| 2026-11-20 13:18:45 | [CVE-2026-133700](https://nvd.nist.gov/vuln/detail/CVE-2026-133700) | Low | 2.3 | free5GC SMF through 1.4.6 contains a resource leak vulnerability in HandlePDUSessionSMContextCreate that leaves SM cont… |
| 2026-11-20 13:18:45 | [CVE-2026-133701](https://nvd.nist.gov/vuln/detail/CVE-2026-133701) | Low | 2.3 | free5GC SMF through 1.4.6 contains a resource exhaustion vulnerability in HandlePDUSessionSMContextLocalRelease that or… |
| 2026-11-20 13:18:46 | [CVE-2026-133702](https://nvd.nist.gov/vuln/detail/CVE-2026-133702) | Medium | 5.3 | free5GC PCF through 1.4.6 contains a resource leak in postAppSessCtxProcedure that leaves PCC rules and QoS data in the… |
| 2026-11-20 13:18:46 | [CVE-2026-133703](https://nvd.nist.gov/vuln/detail/CVE-2026-133703) | Medium | 5.3 | Open5GS AMF through 2.8.0 contains a resource leak vulnerability that allows authenticated UEs to exhaust the session p… |
| 2026-11-20 13:18:46 | [CVE-2026-133704](https://nvd.nist.gov/vuln/detail/CVE-2026-133704) | Medium | 5.1 | Penpot 2.18.0 before 2.18.2 contains a stored cross-site scripting vulnerability that allows authenticated users with e… |
| 2026-11-20 13:18:46 | [CVE-2026-133705](https://nvd.nist.gov/vuln/detail/CVE-2026-133705) | High | 7.6 | Hanko before 3.2.0 contains an open redirect vulnerability in Saml.IsAllowedRedirect that allows unauthenticated attack… |
| 2026-11-20 13:18:46 | [CVE-2026-133706](https://nvd.nist.gov/vuln/detail/CVE-2026-133706) | Medium | 6.3 | request-filtering-agent before 3.2.2 contains a server-side request forgery filter bypass because address validation in… |
| 2026-11-20 13:18:46 | [CVE-2026-133707](https://nvd.nist.gov/vuln/detail/CVE-2026-133707) | High | 8.5 | The targets R package before 1.12.1 contains a code execution vulnerability that allows attackers to run arbitrary R co… |
| 2026-11-20 13:18:47 | [CVE-2026-133708](https://nvd.nist.gov/vuln/detail/CVE-2026-133708) | High | 8.5 | diffpy.structure before 3.5.1 contains a code execution vulnerability that allows attackers to run Python code by suppl… |
| 2026-11-20 13:18:47 | [CVE-2026-133709](https://nvd.nist.gov/vuln/detail/CVE-2026-133709) | Medium | 6.9 | C-Blosc2 before 3.4.1 contains a heap-based out-of-bounds read vulnerability in frame_decompress_chunk() because sparse… |
| 2026-11-20 13:18:47 | [CVE-2026-133710](https://nvd.nist.gov/vuln/detail/CVE-2026-133710) | High | 8.5 | llama.cpp b11003 before b12556 contains an integer overflow in the hrm_text loader load_arch_hparams() that allows atta… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
