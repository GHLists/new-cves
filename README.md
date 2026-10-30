# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-30 14:23 UTC

New CVEs published between 2026-10-30 13:18 UTC and 2026-10-30 14:23 UTC.

[Full CSV](data/new-cves-2026-10-30T14-23-28-840049Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-10-30 13:19:38 | [CVE-2026-64860](https://nvd.nist.gov/vuln/detail/CVE-2026-64860) |  |  | Rejected reason: Further research determined the issue is not a vulnerability. |
| 2026-10-30 13:20:06 | [CVE-2026-75882](https://nvd.nist.gov/vuln/detail/CVE-2026-75882) | High | 8.5 | An improper access control vulnerability in ESET Endpoint Encryption and ESET Full Disk Encryption allow attacker with… |
| 2026-10-30 13:20:15 | [CVE-2026-87768](https://nvd.nist.gov/vuln/detail/CVE-2026-87768) |  |  | DateTime::Lite versions before 0.8.1 for Perl allow CPU exhaustion via a per-day loop when adding seconds. _normalize_l… |
| 2026-10-30 13:20:53 | [CVE-2026-91917](https://nvd.nist.gov/vuln/detail/CVE-2026-91917) | High | 8.0 | Dell OpenManage Enterprise, versions prior to 4.8.0, contains an Improper Input Validation vulnerability. A low privile… |
| 2026-10-30 14:16:35 | [CVE-2026-100355](https://nvd.nist.gov/vuln/detail/CVE-2026-100355) | Low | 3.1 | Campfire is a web-based chat application. In version 1.4.4 and earlier, when a Campfire message contains a link, the se… |
| 2026-10-30 14:16:37 | [CVE-2026-111498](https://nvd.nist.gov/vuln/detail/CVE-2026-111498) | Medium | 4.7 | OpenManage Enterprise, versions prior to 4.8.0, contains an Improper Resource Locking vulnerability. A high privileged… |
| 2026-10-30 14:16:37 | [CVE-2026-111499](https://nvd.nist.gov/vuln/detail/CVE-2026-111499) | Medium | 5.5 | Dell OpenManage Enterprise, versions prior to 4.8.0, contains an Incorrect Permission Assignment for Critical Resource… |
| 2026-10-30 14:16:37 | [CVE-2026-111500](https://nvd.nist.gov/vuln/detail/CVE-2026-111500) | Medium | 5.4 | Dell OpenManage Enterprise, versions prior to 4.8.0, contains a Missing Authentication for Critical Function vulnerabil… |
| 2026-10-30 14:16:37 | [CVE-2026-112347](https://nvd.nist.gov/vuln/detail/CVE-2026-112347) | High | 7.2 | Kirki plugin for WordPress before 6.4.1 contains a broken object-level access control vulnerability in its page REST AP… |
| 2026-10-30 14:16:38 | [CVE-2026-112348](https://nvd.nist.gov/vuln/detail/CVE-2026-112348) | Medium | 6.9 | Kirki plugin for WordPress before 6.2.5 contains a reCAPTCHA bypass vulnerability that allows unauthenticated attackers… |
| 2026-10-30 14:16:39 | [CVE-2026-115683](https://nvd.nist.gov/vuln/detail/CVE-2026-115683) | Medium | 6.8 | A race condition in Epiphany allows a malicious website to bypass the TLS/SSL certificate warning page. Epiphany regist… |
| 2026-10-30 14:16:39 | [CVE-2026-117028](https://nvd.nist.gov/vuln/detail/CVE-2026-117028) |  |  | Skuul School Management System through version 2.6.5 is vulnerable to incorrect access control in the ResultChecker::ch… |
| 2026-10-30 14:16:39 | [CVE-2026-117350](https://nvd.nist.gov/vuln/detail/CVE-2026-117350) |  |  | Bitcoin Core prior to 29.5, 30.4, 31.2 and 32.1 is vulnerable to an OOM issue. |
| 2026-10-30 14:16:41 | [CVE-2026-118986](https://nvd.nist.gov/vuln/detail/CVE-2026-118986) |  |  | CallBackery versions before 0.62.0 for Perl allow session cookie forgery via a signing secret generated with rand(). Th… |
| 2026-10-30 14:16:41 | [CVE-2026-118987](https://nvd.nist.gov/vuln/detail/CVE-2026-118987) |  |  | CallBackery versions before 0.62.0 for Perl accept session cookies of any age sent in the X-Session-Cookie header. cook… |
| 2026-10-30 14:16:45 | [CVE-2026-119528](https://nvd.nist.gov/vuln/detail/CVE-2026-119528) | High | 7.8 | A flaw was found in GIMP. The PSD plug-in’s image resource header loader uses an incorrect destination size when copyin… |
| 2026-10-30 14:16:45 | [CVE-2026-119542](https://nvd.nist.gov/vuln/detail/CVE-2026-119542) | Medium | 4.3 | A flaw was found in the Ickle query parser in Infinispan. A query containing deeply nested predicates can cause recursi… |
| 2026-10-30 14:16:45 | [CVE-2026-119569](https://nvd.nist.gov/vuln/detail/CVE-2026-119569) | Medium | 6.0 | Parse Server before 8.6.108 and 9.0.0 before 9.10.5-alpha.9 contains a prototype pollution vulnerability because user-c… |
| 2026-10-30 14:16:45 | [CVE-2026-119570](https://nvd.nist.gov/vuln/detail/CVE-2026-119570) | Low | 2.3 | Parse Server from 9.7.0 before 9.10.5-alpha.7 contains an information disclosure vulnerability that allows clients to r… |
| 2026-10-30 14:16:45 | [CVE-2026-119571](https://nvd.nist.gov/vuln/detail/CVE-2026-119571) | Medium | 6.3 | Parse Server from 9.7.0 before 9.10.5-alpha.10 contains an authorization flaw that applies _Installation updates addres… |
| 2026-10-30 14:16:46 | [CVE-2026-119572](https://nvd.nist.gov/vuln/detail/CVE-2026-119572) | High | 7.0 | Traefik from 3.7.0-ea.1 before 3.7.15 contains an authentication bypass vulnerability in the Kubernetes Ingress NGINX p… |
| 2026-10-30 14:16:46 | [CVE-2026-119573](https://nvd.nist.gov/vuln/detail/CVE-2026-119573) | Low | 2.1 | Traefik 3.7.11 before 3.7.15 contains an authorization bypass in the Kubernetes Ingress NGINX provider that skips the c… |
| 2026-10-30 14:16:46 | [CVE-2026-119574](https://nvd.nist.gov/vuln/detail/CVE-2026-119574) | High | 8.2 | Traefik from 3.2.0 before 3.7.15 contains a data race in the experimental FastProxy that allows unauthenticated attacke… |
| 2026-10-30 14:16:46 | [CVE-2026-119575](https://nvd.nist.gov/vuln/detail/CVE-2026-119575) | High | 7.1 | ArcadeDB from 26.8.1 before 26.10.2 contains a server-side request forgery vulnerability that allows authenticated user… |
| 2026-10-30 14:16:46 | [CVE-2026-119576](https://nvd.nist.gov/vuln/detail/CVE-2026-119576) | Medium | 5.3 | ArcadeDB from 21.12.1 before 26.10.2 contains an authorization bypass vulnerability that allows users with only readRec… |
| 2026-10-30 14:16:47 | [CVE-2026-119577](https://nvd.nist.gov/vuln/detail/CVE-2026-119577) | High | 7.6 | ArcadeDB before 26.10.2 contains an improper authorization vulnerability that allows revoked users to retain access thr… |
| 2026-10-30 14:16:47 | [CVE-2026-119578](https://nvd.nist.gov/vuln/detail/CVE-2026-119578) | High | 8.5 | MONAI from 1.6.0 before 1.6.1 contains a remote code execution vulnerability in Auto3DSeg algo_from_json() that allows… |
| 2026-10-30 14:16:47 | [CVE-2026-119596](https://nvd.nist.gov/vuln/detail/CVE-2026-119596) | Medium | 5.3 | UNIT3D through 9.2.0 contains a missing authorization vulnerability in PlaylistZipController::show that allows authenti… |
| 2026-10-30 14:16:47 | [CVE-2026-119597](https://nvd.nist.gov/vuln/detail/CVE-2026-119597) | Critical | 9.3 | OpenDeepWiki through 2.0.6 contains a hard-coded JWT signing key vulnerability that allows unauthenticated attackers to… |
| 2026-10-30 14:16:47 | [CVE-2026-119598](https://nvd.nist.gov/vuln/detail/CVE-2026-119598) | Medium | 5.3 | Miaomiaowu before 0.9.3 contains an insecure direct object reference vulnerability in /api/user/proxy-provider-configs… |
| 2026-10-30 14:16:48 | [CVE-2026-119599](https://nvd.nist.gov/vuln/detail/CVE-2026-119599) | Medium | 5.3 | AxonHub through 1.0.0-beta11 contains a privilege escalation vulnerability that allows project users to assign system-l… |
| 2026-10-30 14:16:48 | [CVE-2026-119600](https://nvd.nist.gov/vuln/detail/CVE-2026-119600) | Medium | 6.3 | tcpflow through 1.6.1 contains an out-of-bounds read vulnerability that allows unauthenticated attackers to read proces… |
| 2026-10-30 14:16:48 | [CVE-2026-119601](https://nvd.nist.gov/vuln/detail/CVE-2026-119601) | Medium | 6.9 | AFFLIB through 3.7.22 contains a heap out-of-bounds write vulnerability in af_get_page() that allows attackers to corru… |
| 2026-10-30 14:16:48 | [CVE-2026-119602](https://nvd.nist.gov/vuln/detail/CVE-2026-119602) | Medium | 6.3 | libmspack through 0.11alpha contains an uninitialized memory disclosure vulnerability in the MS-ZIP decompressor that a… |
| 2026-10-30 14:17:05 | [CVE-2026-49115](https://nvd.nist.gov/vuln/detail/CVE-2026-49115) |  |  | Rejected reason: This CVE ID has been rejected or withdrawn by its CVE Numbering Authority. |
| 2026-10-30 14:17:05 | [CVE-2026-49116](https://nvd.nist.gov/vuln/detail/CVE-2026-49116) |  |  | Rejected reason: This CVE ID has been rejected or withdrawn by its CVE Numbering Authority. |
| 2026-10-30 14:17:10 | [CVE-2026-86715](https://nvd.nist.gov/vuln/detail/CVE-2026-86715) | High | 7.1 | Plaintext storage of a password vulnerability in Crypttech Crypto and Informatics Technologies Industry and Trade Inc.… |
| 2026-10-30 14:17:10 | [CVE-2026-91912](https://nvd.nist.gov/vuln/detail/CVE-2026-91912) | High | 7.3 | Dell OpenManage Enterprise, versions prior to 4.8.0, contains an Use of Hard-coded Cryptographic Key vulnerability. A l… |
| 2026-10-30 14:17:10 | [CVE-2026-91913](https://nvd.nist.gov/vuln/detail/CVE-2026-91913) | High | 8.8 | Dell OpenManage Enterprise, versions prior to 4.8.0, contains an Improper Neutralization of Special Elements used in an… |
| 2026-10-30 14:17:10 | [CVE-2026-91914](https://nvd.nist.gov/vuln/detail/CVE-2026-91914) | High | 7.1 | Dell OpenManage Enterprise, versions prior to 4.8.0, contains an Authentication Bypass by Spoofing vulnerability. An un… |
| 2026-10-30 14:17:11 | [CVE-2026-91915](https://nvd.nist.gov/vuln/detail/CVE-2026-91915) | Medium | 6.8 | Dell OpenManage Enterprise, versions prior to 4.8.0, contains an Improper Neutralization of Special Elements in Output… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
