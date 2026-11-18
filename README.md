# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-11-18 21:22 UTC

New CVEs published between 2026-11-18 20:22 UTC and 2026-11-18 21:22 UTC.

[Full CSV](data/new-cves-2026-11-18T21-22-17-878824Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-11-18 21:17:44 | [CVE-2025-36441](https://nvd.nist.gov/vuln/detail/CVE-2025-36441) | Medium | 6.2 | IBM Financial Transaction Manager (FTM) 3.2.13.0 through 3.2.13.0 Interim Fix 006 stores potentially sensitive informat… |
| 2026-11-18 21:17:44 | [CVE-2026-102434](https://nvd.nist.gov/vuln/detail/CVE-2026-102434) | Medium | 5.3 | IBM Engineering AI Hub 1.0.0 through 1.4.0 could allow a remote attacker to obtain sensitive information due to a Cross… |
| 2026-11-18 21:17:45 | [CVE-2026-110521](https://nvd.nist.gov/vuln/detail/CVE-2026-110521) | Medium | 6.1 | IBM Engineering AI Hub 1.0.0 through 1.4.0 is vulnerable to cross-site scripting. This vulnerability allows an unauthen… |
| 2026-11-18 21:17:46 | [CVE-2026-111513](https://nvd.nist.gov/vuln/detail/CVE-2026-111513) | High | 7.3 | Dell Alienware Command Center (AWCC), versions prior to 6.14.105.0, contain an Improper Verification of Cryptographic S… |
| 2026-11-18 21:17:46 | [CVE-2026-111514](https://nvd.nist.gov/vuln/detail/CVE-2026-111514) | High | 7.3 | Dell Alienware Command Center (AWCC), versions prior to 6.14.105.0, contain an Incorrect Default Permissions vulnerabil… |
| 2026-11-18 21:17:46 | [CVE-2026-111515](https://nvd.nist.gov/vuln/detail/CVE-2026-111515) | High | 7.1 | Dell Alienware Command Center (AWCC), versions prior to 6.14.105.0, contain an Improper Authorization in Handler for Cu… |
| 2026-11-18 21:17:46 | [CVE-2026-111516](https://nvd.nist.gov/vuln/detail/CVE-2026-111516) | Medium | 6.6 | Dell Alienware Command Center (AWCC), versions prior to 6.14.105.0, contain a Least Privilege Violation vulnerability.… |
| 2026-11-18 21:17:46 | [CVE-2026-111517](https://nvd.nist.gov/vuln/detail/CVE-2026-111517) | Medium | 4.4 | Dell Alienware Command Center (AWCC), versions prior to 6.14.105.0, contain a Deserialization of Untrusted Data vulnera… |
| 2026-11-18 21:17:46 | [CVE-2026-111518](https://nvd.nist.gov/vuln/detail/CVE-2026-111518) | Low | 3.1 | Dell Alienware Command Center (AWCC), versions prior to 6.14.105.0, contain an Improper Restriction of Rendered UI Laye… |
| 2026-11-18 21:17:46 | [CVE-2026-111519](https://nvd.nist.gov/vuln/detail/CVE-2026-111519) | Low | 2.0 | Dell Alienware Command Center (AWCC), versions prior to 6.14.105.0, contain an Improper Authorization in Handler for Cu… |
| 2026-11-18 21:17:46 | [CVE-2026-111520](https://nvd.nist.gov/vuln/detail/CVE-2026-111520) | High | 7.3 | Dell Alienware Command Center (AWCC), versions prior to 6.14.105.0, contain a Time-of-check Time-of-use (TOCTOU) Race C… |
| 2026-11-18 21:17:47 | [CVE-2026-114585](https://nvd.nist.gov/vuln/detail/CVE-2026-114585) | High | 7.6 | IBM Engineering AI Hub 1.0.0 through 1.4.0 could allow a remote authenticated attacker to obtain sensitive information… |
| 2026-11-18 21:17:47 | [CVE-2026-122119](https://nvd.nist.gov/vuln/detail/CVE-2026-122119) |  |  | Rejected reason: ** REJECT ** DO NOT USE THIS CANDIDATE NUMBER. ConsultIDs: CVE-2026-122227. Reason: This candidate is… |
| 2026-11-18 21:17:48 | [CVE-2026-127222](https://nvd.nist.gov/vuln/detail/CVE-2026-127222) | High | 8.7 | SGLang through 0.5.23, fixed in commit 7b5fb39, contains a missing authorization vulnerability in the POST /load_lora_a… |
| 2026-11-18 21:17:48 | [CVE-2026-128974](https://nvd.nist.gov/vuln/detail/CVE-2026-128974) | Medium | 5.4 | Cleartext storage of the WhatsApp Noise static private key in the shared application container (cck.dat) in WhatsApp Me… |
| 2026-11-18 21:17:48 | [CVE-2026-130089](https://nvd.nist.gov/vuln/detail/CVE-2026-130089) | High | 7.3 | A caller who can send requests to the temporal-proxy gRPC listener can obtain the static API key of an upstream whose a… |
| 2026-11-18 21:17:49 | [CVE-2026-130090](https://nvd.nist.gov/vuln/detail/CVE-2026-130090) | Low | 2.3 | When two templated upstreams in temporal-proxy render the same address, a request routed to one upstream can be sent un… |
| 2026-11-18 21:17:49 | [CVE-2026-130091](https://nvd.nist.gov/vuln/detail/CVE-2026-130091) | High | 7.1 | A caller with write permission in a namespace can terminate temporal-proxy through memory exhaustion by storing highly… |
| 2026-11-18 21:17:49 | [CVE-2026-130092](https://nvd.nist.gov/vuln/detail/CVE-2026-130092) | High | 8.7 | A caller who can reach the temporal-proxy gRPC listener, with or without a valid credential, can grow the proxy's memor… |
| 2026-11-18 21:17:55 | [CVE-2026-132137](https://nvd.nist.gov/vuln/detail/CVE-2026-132137) | Low | 2.1 | A vulnerability was identified in Relaticle up to 3.10.0. This affects the function mapToField of the file packages/Imp… |
| 2026-11-18 21:17:55 | [CVE-2026-132139](https://nvd.nist.gov/vuln/detail/CVE-2026-132139) | High | 8.6 | A weakness has been identified in DrayTek Vigor2960 up to 1.5.1.6. Affected is the function setSWMProfile of the file /… |
| 2026-11-18 21:17:56 | [CVE-2026-132140](https://nvd.nist.gov/vuln/detail/CVE-2026-132140) | High | 7.7 | A security vulnerability has been detected in DrayTek Vigor2960 up to 1.5.1.6. Affected by this vulnerability is an unk… |
| 2026-11-18 21:17:56 | [CVE-2026-132144](https://nvd.nist.gov/vuln/detail/CVE-2026-132144) | High | 8.3 | MISP contains an authorization flaw in the user login-email change logic. When an external authentication backend is co… |
| 2026-11-18 21:17:57 | [CVE-2026-132559](https://nvd.nist.gov/vuln/detail/CVE-2026-132559) | Low | 2.3 | When payload encryption is enabled, failure messages and stack traces that temporal-proxy is configured to keep from th… |
| 2026-11-18 21:17:57 | [CVE-2026-132636](https://nvd.nist.gov/vuln/detail/CVE-2026-132636) | Medium | 5.3 | MISP contains an authorization bypass in its event search and filter functionality. When a user performed searches thro… |
| 2026-11-18 21:17:57 | [CVE-2026-132637](https://nvd.nist.gov/vuln/detail/CVE-2026-132637) | Medium | 5.3 | MISP contains an authorization bypass in the correlations/eventCorrelations endpoint and the underlying correlation eng… |
| 2026-11-18 21:17:58 | [CVE-2026-132641](https://nvd.nist.gov/vuln/detail/CVE-2026-132641) | Medium | 5.3 | MISP's EventDelegationsController delegateEvent method accepted a user-supplied sharing_group_id parameter without veri… |
| 2026-11-18 21:17:58 | [CVE-2026-132642](https://nvd.nist.gov/vuln/detail/CVE-2026-132642) | Medium | 5.3 | MISP contains an access control flaw in its tag management endpoints: events/addTag (single and bulk), events/removeTag… |
| 2026-11-18 21:17:58 | [CVE-2026-132643](https://nvd.nist.gov/vuln/detail/CVE-2026-132643) | Medium | 5.3 | MISP contains an information disclosure vulnerability in the Sighting model when the Sightings_anonymise setting is ena… |
| 2026-11-18 21:17:59 | [CVE-2026-55169](https://nvd.nist.gov/vuln/detail/CVE-2026-55169) | High | 8.4 | Open OnDemand is an open-source high-performance computing portal. Prior to 4.1.6 and 4.2.3, the Open OnDemand dashboar… |
| 2026-11-18 21:17:59 | [CVE-2026-55171](https://nvd.nist.gov/vuln/detail/CVE-2026-55171) | Critical | 9.1 | Open OnDemand is an open-source high-performance computing portal. Prior to Open OnDemand 4.1.6 and 4.2.3, and prior to… |
| 2026-11-18 21:17:59 | [CVE-2026-55172](https://nvd.nist.gov/vuln/detail/CVE-2026-55172) | Medium | 5.4 | Open OnDemand is an open-source high-performance computing portal. Prior to 4.1.6 and 4.2.3, apps/dashboard/config/init… |
| 2026-11-18 21:17:59 | [CVE-2026-55505](https://nvd.nist.gov/vuln/detail/CVE-2026-55505) | Medium | 4.9 | Wavelog is web-based amateur radio logging software. Prior to 3.2.4, the application/controllers/Lotw.php import() work… |
| 2026-11-18 21:17:59 | [CVE-2026-55506](https://nvd.nist.gov/vuln/detail/CVE-2026-55506) | Critical | 9.6 | Wavelog is web-based amateur radio logging software. Prior to 2.5, the filename parameter accepted by POST /qsl/addQsoT… |
| 2026-11-18 21:17:59 | [CVE-2026-55507](https://nvd.nist.gov/vuln/detail/CVE-2026-55507) | Medium | 6.0 | Wavelog is web-based amateur radio logging software. In 3.2.5 and earlier, the Hams of Note feature stores the administ… |
| 2026-11-18 21:18:00 | [CVE-2026-55508](https://nvd.nist.gov/vuln/detail/CVE-2026-55508) | Critical | 9.4 | Wavelog is web-based amateur radio logging software. Prior to 2.5, the callsign parameter accepted by POST /oqrs/search… |
| 2026-11-18 21:18:00 | [CVE-2026-59964](https://nvd.nist.gov/vuln/detail/CVE-2026-59964) | Medium | 5.9 | uftpd is a UNIX FTP and TFTP server. Prior to 2.16, uftpd's compose_path function in src/common.c can overflow the fixe… |
| 2026-11-18 21:18:00 | [CVE-2026-59975](https://nvd.nist.gov/vuln/detail/CVE-2026-59975) | High | 7.5 | SharpIppNext is a .NET Standard library for building Internet Printing Protocol clients and servers. Prior to 4.1.0, se… |
| 2026-11-18 21:18:01 | [CVE-2026-69131](https://nvd.nist.gov/vuln/detail/CVE-2026-69131) | Medium | 4.3 | django-filer is a file and image management application for Django. Prior to 3.5.0, the delete_files_or_folders action… |
| 2026-11-18 21:18:01 | [CVE-2026-69138](https://nvd.nist.gov/vuln/detail/CVE-2026-69138) | Medium | 6.5 | djangocms-versioning is a general-purpose versioning package for django CMS 4 and later. Prior to 2.6.1, the check_disc… |
| 2026-11-18 21:18:01 | [CVE-2026-71427](https://nvd.nist.gov/vuln/detail/CVE-2026-71427) | Medium | 5.3 | WPGraphQL Content Blocks is a WordPress plugin that extends WPGraphQL to support querying Gutenberg blocks as data. Pri… |
| 2026-11-18 21:18:01 | [CVE-2026-73967](https://nvd.nist.gov/vuln/detail/CVE-2026-73967) | High | 8.7 | AnsibleForms is a self-hosted web application that turns automation into self-service forms. Prior to 6.2.1, AnsibleFor… |
| 2026-11-18 21:18:01 | [CVE-2026-73968](https://nvd.nist.gov/vuln/detail/CVE-2026-73968) | High | 7.2 | AnsibleForms is a self-hosted web application that turns automation into self-service forms. Prior to 6.2.1, AnsibleFor… |
| 2026-11-18 21:18:02 | [CVE-2026-73969](https://nvd.nist.gov/vuln/detail/CVE-2026-73969) | Critical | 9.8 | AnsibleForms is a self-hosted web application that turns automation into self-service forms. Prior to 6.2.1, AnsibleFor… |
| 2026-11-18 21:18:02 | [CVE-2026-75506](https://nvd.nist.gov/vuln/detail/CVE-2026-75506) | Medium | 6.6 | OliveTin gives safe and simple access to predefined shell commands from a web interface. From 3000.0.0 until 3000.18.1,… |
| 2026-11-18 21:18:02 | [CVE-2026-75522](https://nvd.nist.gov/vuln/detail/CVE-2026-75522) | High | 7.5 | OpenID4VP is an open-source credential parsing library for SD-JWT VC and mDOC/mDL formats. Prior to 0.8.1, src/trust/Ch… |
| 2026-11-18 21:18:02 | [CVE-2026-76007](https://nvd.nist.gov/vuln/detail/CVE-2026-76007) | High | 8.1 | IBM Engineering AI Hub 1.0.0 through 1.4.0 could allow a remote attacker to obtain sensitive information and perform un… |
| 2026-11-18 21:18:02 | [CVE-2026-76088](https://nvd.nist.gov/vuln/detail/CVE-2026-76088) | High | 7.5 | PGPainless is a simple-to-use OpenPGP API based on Bouncy Castle. Prior to 1.7.8 and from 2.0.0 until 2.0.4, pgpainless… |
| 2026-11-18 21:18:02 | [CVE-2026-76100](https://nvd.nist.gov/vuln/detail/CVE-2026-76100) | High | 8.2 | OwnPay is a self-hosted open-source payment gateway automation platform. In 0.2.0 and earlier, modules/gateways/alipay/… |
| 2026-11-18 21:18:03 | [CVE-2026-76913](https://nvd.nist.gov/vuln/detail/CVE-2026-76913) | High | 8.8 | NotrinosERP is an open-source web-based enterprise resource planning system written in PHP and MySQL. From 1.0.0 until… |
| 2026-11-18 21:18:03 | [CVE-2026-77295](https://nvd.nist.gov/vuln/detail/CVE-2026-77295) | High | 8.7 | MyMangaDB is a self-hosted manga collection manager with automatic metadata, MyAnimeList import, Docker support, and co… |
| 2026-11-18 21:18:03 | [CVE-2026-77296](https://nvd.nist.gov/vuln/detail/CVE-2026-77296) | Critical | 9.3 | MyMangaDB is a self-hosted manga collection manager with automatic metadata, MyAnimeList import, Docker support, and co… |
| 2026-11-18 21:18:03 | [CVE-2026-77297](https://nvd.nist.gov/vuln/detail/CVE-2026-77297) | Critical | 9.3 | MyMangaDB is a self-hosted manga collection manager with automatic metadata, MyAnimeList import, Docker support, and co… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
