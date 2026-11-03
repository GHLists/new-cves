# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-11-03 16:19 UTC

New CVEs published between 2026-11-03 15:19 UTC and 2026-11-03 16:19 UTC.

[Full CSV](data/new-cves-2026-11-03T16-19-51-145392Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-11-03 16:17:18 | [CVE-2026-108147](https://nvd.nist.gov/vuln/detail/CVE-2026-108147) | Medium | 6.9 | An issue was discovered in Django 6.1 before 6.1.3, 6.0.4 before 6.0.10, and 5.2.13 before 5.2.19. `django.http.multipa… |
| 2026-11-03 16:17:18 | [CVE-2026-111211](https://nvd.nist.gov/vuln/detail/CVE-2026-111211) | Medium | 6.9 | An issue was discovered in Django 6.1 before 6.1.3, 6.0 before 6.0.10, and 5.2 before 5.2.19. `django.contrib.gis.forms… |
| 2026-11-03 16:17:18 | [CVE-2026-111362](https://nvd.nist.gov/vuln/detail/CVE-2026-111362) | Medium | 6.9 | An issue was discovered in Django 6.1 before 6.1.3, 6.0 before 6.0.10, and 5.2 before 5.2.19. `django.contrib.gis.gdal.… |
| 2026-11-03 16:17:19 | [CVE-2026-113593](https://nvd.nist.gov/vuln/detail/CVE-2026-113593) | Low | 2.3 | An issue was discovered in Django 6.1 before 6.1.3, 6.0 before 6.0.10, and 5.2 before 5.2.19. The `django.middleware.ca… |
| 2026-11-03 16:17:19 | [CVE-2026-113733](https://nvd.nist.gov/vuln/detail/CVE-2026-113733) | Low | 2.1 | An issue was discovered in Django 6.1 before 6.1.3 and 6.0 before 6.0.10. The `django.contrib.admin.utils.display_for_f… |
| 2026-11-03 16:17:19 | [CVE-2026-114582](https://nvd.nist.gov/vuln/detail/CVE-2026-114582) | Medium | 6.9 | An issue was discovered in Django 6.1 before 6.1.3, 6.0 before 6.0.10, and 5.2 before 5.2.19. `django.contrib.gis.gdal.… |
| 2026-11-03 16:17:19 | [CVE-2026-118487](https://nvd.nist.gov/vuln/detail/CVE-2026-118487) | High | 7.5 | In Eclipse Vert.x versions [4.0.0, 4.5.35] or [5.0.0, 5.2.2], the `FrameParser` in vertx-stomp creates a `RecordParser`… |
| 2026-11-03 16:17:20 | [CVE-2026-118505](https://nvd.nist.gov/vuln/detail/CVE-2026-118505) | Medium | 6.3 | Improper Restriction of Excessive Authentication Attempts vulnerability in team-alembic ash_authentication allows an un… |
| 2026-11-03 16:17:21 | [CVE-2026-119215](https://nvd.nist.gov/vuln/detail/CVE-2026-119215) | High | 7.6 | Authorization Bypass Through User-Controlled Key vulnerability in team-alembic ash_authentication allows a user with an… |
| 2026-11-03 16:17:21 | [CVE-2026-119741](https://nvd.nist.gov/vuln/detail/CVE-2026-119741) | High | 8.7 | rsync through 3.5.1 contains a denial of service vulnerability in the delta-transfer sender's hash_search() in match.c… |
| 2026-11-03 16:17:22 | [CVE-2026-120754](https://nvd.nist.gov/vuln/detail/CVE-2026-120754) | Low | 1.9 | HDF5 through 2.2.0 contains an uninitialized memory read vulnerability in H5Z__filter_scaleoffset() in src/H5Zscaleoffs… |
| 2026-11-03 16:17:22 | [CVE-2026-120755](https://nvd.nist.gov/vuln/detail/CVE-2026-120755) | Medium | 4.7 | HDF5 through 2.2.0 contains an out-of-bounds read vulnerability in H5Z__filter_szip() in src/H5Zszip.c. When decoding a… |
| 2026-11-03 16:17:22 | [CVE-2026-120756](https://nvd.nist.gov/vuln/detail/CVE-2026-120756) | Low | 1.9 | HDF5 through 2.2.0 contains a heap buffer over-read vulnerability in H5O__chunk_deserialize() in src/H5Ocache.c. When d… |
| 2026-11-03 16:17:23 | [CVE-2026-120757](https://nvd.nist.gov/vuln/detail/CVE-2026-120757) | Medium | 6.9 | HDF5 through 2.2.0 contains a heap buffer over-read vulnerability in H5L__extern_traverse() in src/H5Lexternal.c, the d… |
| 2026-11-03 16:17:23 | [CVE-2026-120758](https://nvd.nist.gov/vuln/detail/CVE-2026-120758) | Medium | 5.4 | HDF5 through 2.2.0 contains a NULL pointer dereference vulnerability in H5HL_unprotect() in src/H5HL.c. H5HL_protect()… |
| 2026-11-03 16:17:23 | [CVE-2026-121260](https://nvd.nist.gov/vuln/detail/CVE-2026-121260) | High | 8.5 | A flaw has been found in Ziroom ZHOME A0101 1.0.1.0 Build 202004151405. This issue affects the function loadstring of t… |
| 2026-11-03 16:17:23 | [CVE-2026-121450](https://nvd.nist.gov/vuln/detail/CVE-2026-121450) | High | 7.7 | CFNext before 3.1.0 contains a weak cryptographic derivation vulnerability that allows subscription link holders to rec… |
| 2026-11-03 16:17:23 | [CVE-2026-121451](https://nvd.nist.gov/vuln/detail/CVE-2026-121451) | High | 8.7 | AB Download Manager before 1.11.2 contains a cross-site request forgery vulnerability in its unauthenticated browser-in… |
| 2026-11-03 16:17:24 | [CVE-2026-121452](https://nvd.nist.gov/vuln/detail/CVE-2026-121452) | High | 8.3 | bbs-go through 4.4.6 contains an improper certificate validation vulnerability that allows network-positioned attackers… |
| 2026-11-03 16:17:24 | [CVE-2026-121453](https://nvd.nist.gov/vuln/detail/CVE-2026-121453) | Medium | 5.1 | SQLBot through 1.10.3 contains a path traversal vulnerability in the importToDb endpoint that allows authenticated work… |
| 2026-11-03 16:17:24 | [CVE-2026-121454](https://nvd.nist.gov/vuln/detail/CVE-2026-121454) | Medium | 6.3 | Padloc through 4.3.0 contains a missing authentication vulnerability in ScimServer._handleScimGet() that allows unauthe… |
| 2026-11-03 16:17:24 | [CVE-2026-121455](https://nvd.nist.gov/vuln/detail/CVE-2026-121455) | Medium | 5.3 | DbGate before 7.3.3 contains a missing authorization vulnerability that allows connection-restricted authenticated user… |
| 2026-11-03 16:17:25 | [CVE-2026-121543](https://nvd.nist.gov/vuln/detail/CVE-2026-121543) | High | 8.7 | smart-sso through 2.0.1 contains an incorrect authorization vulnerability in PermissionFilter that allows any authentic… |
| 2026-11-03 16:17:25 | [CVE-2026-121544](https://nvd.nist.gov/vuln/detail/CVE-2026-121544) | Medium | 6.9 | Koodo Reader through 2.4.6 contains a path traversal vulnerability in the self-hosted HTTP server's OPDS handlers that… |
| 2026-11-03 16:17:26 | [CVE-2026-121545](https://nvd.nist.gov/vuln/detail/CVE-2026-121545) | Medium | 6.9 | Dreeve before 5.8.0 contains a missing authentication vulnerability in StravaWebhookRequestHandler::handleEvent that al… |
| 2026-11-03 16:17:26 | [CVE-2026-121546](https://nvd.nist.gov/vuln/detail/CVE-2026-121546) | Medium | 6.0 | ruTorrent before 5.3.20 contains a path traversal vulnerability in the datadir plugin that allows authenticated users t… |
| 2026-11-03 16:17:26 | [CVE-2026-121547](https://nvd.nist.gov/vuln/detail/CVE-2026-121547) | Low | 1.0 | Canop dysk before 3.8.2 contains a terminal escape sequence injection vulnerability that allows local users to inject c… |
| 2026-11-03 16:17:26 | [CVE-2026-121548](https://nvd.nist.gov/vuln/detail/CVE-2026-121548) | High | 8.4 | Jarun nnn through 5.3 contains an OS command injection vulnerability in plugins/togglex that allows attackers to execut… |
| 2026-11-03 16:17:26 | [CVE-2026-121549](https://nvd.nist.gov/vuln/detail/CVE-2026-121549) | Medium | 4.1 | nnn through 5.3 contains an insecure temporary file vulnerability in the pdfread and nuke plugins that allows local att… |
| 2026-11-03 16:17:26 | [CVE-2026-121550](https://nvd.nist.gov/vuln/detail/CVE-2026-121550) | Low | 1.0 | nnn through 5.3 contains an insecure file handling vulnerability that allows local attackers to redirect writes because… |
| 2026-11-03 16:17:27 | [CVE-2026-121551](https://nvd.nist.gov/vuln/detail/CVE-2026-121551) | Medium | 5.1 | PostfixAdmin through 4.0.5 contains a stored cross-site scripting vulnerability that allows authenticated mailbox users… |
| 2026-11-03 16:17:27 | [CVE-2026-121552](https://nvd.nist.gov/vuln/detail/CVE-2026-121552) | Medium | 5.3 | Dromara domain-admin before 1.6.79 contains a missing authorization vulnerability in the POST /api/getGroupUserList han… |
| 2026-11-03 16:17:27 | [CVE-2026-121553](https://nvd.nist.gov/vuln/detail/CVE-2026-121553) | Medium | 6.3 | Cotonti through 1.0.0 generates registration and email-change validation tokens with md5(microtime()), allowing attacke… |
| 2026-11-03 16:17:27 | [CVE-2026-121554](https://nvd.nist.gov/vuln/detail/CVE-2026-121554) | High | 8.2 | cordova-plugin-advanced-http 1.5.0 through 3.3.1 contains an information disclosure vulnerability that leaks cookies to… |
| 2026-11-03 16:17:27 | [CVE-2026-121555](https://nvd.nist.gov/vuln/detail/CVE-2026-121555) | High | 8.7 | Foxel through 2.4.0 contains a missing authentication vulnerability that allows unauthenticated attackers to read files… |
| 2026-11-03 16:17:27 | [CVE-2026-121556](https://nvd.nist.gov/vuln/detail/CVE-2026-121556) | High | 8.7 | FastBee through 2.1.0 contains an insecure direct object reference vulnerability in ProductController that allows authe… |
| 2026-11-03 16:17:28 | [CVE-2026-121557](https://nvd.nist.gov/vuln/detail/CVE-2026-121557) | High | 8.2 | WPPConnect Server through 2.10.74 contains a missing authentication vulnerability that allows unauthenticated attackers… |
| 2026-11-03 16:17:28 | [CVE-2026-121558](https://nvd.nist.gov/vuln/detail/CVE-2026-121558) | Low | 2.3 | AuditPilot before commit 4669c93 contains an authorization bypass vulnerability in _metadata_allowed in rag/agentic_rag… |
| 2026-11-03 16:17:28 | [CVE-2026-121559](https://nvd.nist.gov/vuln/detail/CVE-2026-121559) | High | 8.6 | GLPI 10.0.0 before 10.0.28 and 11.0.0 before 11.0.10 contains a privilege escalation vulnerability that allows authenti… |
| 2026-11-03 16:17:28 | [CVE-2026-121560](https://nvd.nist.gov/vuln/detail/CVE-2026-121560) | High | 7.1 | LogChimp 0.9.0-alpha.1 before 0.9.3 contains an authorization bypass vulnerability that allows authenticated post autho… |
| 2026-11-03 16:17:28 | [CVE-2026-121561](https://nvd.nist.gov/vuln/detail/CVE-2026-121561) | Medium | 6.3 | Label Studio before 1.23.2 (label-studio-sdk before 2.1.2) contains a server-side request forgery vulnerability that al… |
| 2026-11-03 16:17:29 | [CVE-2026-121562](https://nvd.nist.gov/vuln/detail/CVE-2026-121562) | Medium | 6.9 | CTFd 3.1.0 before 3.8.7 contains an information disclosure vulnerability in the /api/v1/teams list endpoint that expose… |
| 2026-11-03 16:17:29 | [CVE-2026-121564](https://nvd.nist.gov/vuln/detail/CVE-2026-121564) | Low | 1.8 | Incomplete Comparison with Missing Factors (CWE-1023) in merge_chats() (whatstk/utils/chat_merge.py), reached from Base… |
| 2026-11-03 16:17:29 | [CVE-2026-121578](https://nvd.nist.gov/vuln/detail/CVE-2026-121578) |  |  | Tactical RMM contains a stored XSS vulnerability caused by improperly validated input or encode output for various fiel… |
| 2026-11-03 16:17:35 | [CVE-2026-65107](https://nvd.nist.gov/vuln/detail/CVE-2026-65107) | Medium | 6.3 | NVIDIA Slurm contains a vulnerability where a user could alter the supplemental group list as part of an sbcast file tr… |
| 2026-11-03 16:17:35 | [CVE-2026-65108](https://nvd.nist.gov/vuln/detail/CVE-2026-65108) | Medium | 6.3 | NVIDIA Slurm contains an attacker-controlled heap-based buffer overflow in the slurmstepd process while the slurmstepd… |
| 2026-11-03 16:17:35 | [CVE-2026-65109](https://nvd.nist.gov/vuln/detail/CVE-2026-65109) | Medium | 4.7 | NVIDIA Slurm is subject to a symlink resolution issue in the container cleanup code that could allow an attacker to rem… |
| 2026-11-03 16:17:35 | [CVE-2026-65138](https://nvd.nist.gov/vuln/detail/CVE-2026-65138) | Medium | 6.3 | NVIDIA Slurm contains an attacker-controlled arbitrary-memory read in the slurmstepd socket API that could be used to e… |
| 2026-11-03 16:17:35 | [CVE-2026-65139](https://nvd.nist.gov/vuln/detail/CVE-2026-65139) | Medium | 6.3 | NVIDIA Slurm contains an attacker-controlled SQL injection attack in certain SlurmDBD RPCs that can lead to arbitrary c… |
| 2026-11-03 16:17:35 | [CVE-2026-65140](https://nvd.nist.gov/vuln/detail/CVE-2026-65140) | Medium | 5.7 | NVIDIA Slurm contains some inconsistent authorization checks against the Operator permission level in the SlurmDBD that… |
| 2026-11-03 16:17:36 | [CVE-2026-65165](https://nvd.nist.gov/vuln/detail/CVE-2026-65165) | Medium | 5.3 | NVIDIA Slurm contains a vulnerability where a user could deliberately alter the provided nodelist alongside the --distr… |
| 2026-11-03 16:17:36 | [CVE-2026-65168](https://nvd.nist.gov/vuln/detail/CVE-2026-65168) | High | 7.0 | NVIDIA Slurm contains an attacker-controlled heap-based buffer overflow in the slurmstepd socket handling code. |
| 2026-11-03 16:17:36 | [CVE-2026-73328](https://nvd.nist.gov/vuln/detail/CVE-2026-73328) | High | 8.6 | Volmarg Personal Management System through 2.1.0 contains an unrestricted file upload vulnerability that allows authent… |
| 2026-11-03 16:17:38 | [CVE-2026-97350](https://nvd.nist.gov/vuln/detail/CVE-2026-97350) | Medium | 6.9 | Securepoint SSL VPN Client v2 on Windows contains vulnerabilities in the handling of OpenVPN configurations and proxy s… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
