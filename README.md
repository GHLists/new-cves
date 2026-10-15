# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-15 23:20 UTC

New CVEs published between 2026-10-15 22:19 UTC and 2026-10-15 23:20 UTC.

[Full CSV](data/new-cves-2026-10-15T23-20-14-88899Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-10-15 22:19:26 | [CVE-2026-110913](https://nvd.nist.gov/vuln/detail/CVE-2026-110913) |  |  | Memory corruption in DOM in Google Chrome prior to 155.0.8059.84 allowed a remote attacker to execute arbitrary code in… |
| 2026-10-15 22:19:26 | [CVE-2026-110914](https://nvd.nist.gov/vuln/detail/CVE-2026-110914) |  |  | Memory corruption in Workers in Google Chrome prior to 155.0.8059.84 allowed a remote attacker to potentially execute a… |
| 2026-10-15 22:19:26 | [CVE-2026-110915](https://nvd.nist.gov/vuln/detail/CVE-2026-110915) |  |  | Use after free in Compositing in Google Chrome prior to 155.0.8059.84 allowed a remote attacker to execute arbitrary co… |
| 2026-10-15 22:19:26 | [CVE-2026-110916](https://nvd.nist.gov/vuln/detail/CVE-2026-110916) |  |  | Improper input validation in Desktop in Google Chrome prior to 155.0.8059.84 allowed a remote attacker to potentially e… |
| 2026-10-15 22:19:27 | [CVE-2026-110917](https://nvd.nist.gov/vuln/detail/CVE-2026-110917) |  |  | Memory corruption in SVG in Google Chrome prior to 155.0.8059.84 allowed a remote attacker to read memory via a crafted… |
| 2026-10-15 22:19:27 | [CVE-2026-110918](https://nvd.nist.gov/vuln/detail/CVE-2026-110918) |  |  | Memory corruption in Core in Google Chrome prior to 155.0.8059.84 allowed a remote attacker to read memory via a crafte… |
| 2026-10-15 22:19:27 | [CVE-2026-110919](https://nvd.nist.gov/vuln/detail/CVE-2026-110919) |  |  | Use after free in V8 in Google Chrome prior to 155.0.8059.84 allowed a remote attacker to execute arbitrary code inside… |
| 2026-10-15 22:19:27 | [CVE-2026-110920](https://nvd.nist.gov/vuln/detail/CVE-2026-110920) |  |  | Memory corruption in V8 in Google Chrome prior to 155.0.8059.84 allowed a remote attacker to execute arbitrary code ins… |
| 2026-10-15 22:19:27 | [CVE-2026-110921](https://nvd.nist.gov/vuln/detail/CVE-2026-110921) |  |  | Use after free in V8 in Google Chrome prior to 155.0.8059.84 allowed a remote attacker to execute arbitrary code inside… |
| 2026-10-15 22:19:27 | [CVE-2026-110922](https://nvd.nist.gov/vuln/detail/CVE-2026-110922) |  |  | Use after free in Prerender in Google Chrome prior to 155.0.8059.84 allowed a remote attacker to execute arbitrary code… |
| 2026-10-15 22:19:27 | [CVE-2026-111269](https://nvd.nist.gov/vuln/detail/CVE-2026-111269) | Medium | 6.9 | libical through 4.0.6 contains a heap-based out-of-bounds read in icalvalue_decode_ical_string() in src/libical/icalval… |
| 2026-10-15 22:19:27 | [CVE-2026-111270](https://nvd.nist.gov/vuln/detail/CVE-2026-111270) | Medium | 6.9 | libmodplug through 0.8.9.1 contains a heap-based out-of-bounds write in CSoundFile::ReadDSM() in src/load_dsm.cpp becau… |
| 2026-10-15 22:19:27 | [CVE-2026-111271](https://nvd.nist.gov/vuln/detail/CVE-2026-111271) | Medium | 6.8 | libmodplug through 0.8.9.1 contains a heap-based out-of-bounds read vulnerability in CSoundFile::ReadAMS2() in src/load… |
| 2026-10-15 22:19:28 | [CVE-2026-111272](https://nvd.nist.gov/vuln/detail/CVE-2026-111272) | Medium | 6.8 | LibRaw through 0.22.2 contains a heap-based out-of-bounds read in LibRaw::parseNikonMakernote() that allows attackers t… |
| 2026-10-15 22:19:28 | [CVE-2026-111273](https://nvd.nist.gov/vuln/detail/CVE-2026-111273) | Medium | 6.9 | unarr through 1.1.1 contains an off-by-one heap-based buffer overflow in tar_get_name() in tar/parse-tar.c, reachable t… |
| 2026-10-15 22:19:28 | [CVE-2026-111274](https://nvd.nist.gov/vuln/detail/CVE-2026-111274) | Medium | 6.8 | unarr through 1.1.1 contains a heap-based out-of-bounds read in zip_parse_extra_fields() in zip/parse-zip.c due to an i… |
| 2026-10-15 22:19:28 | [CVE-2026-111275](https://nvd.nist.gov/vuln/detail/CVE-2026-111275) | Medium | 6.9 | nifti_clib through 3.0.1 contains a stack-based out-of-bounds read and write vulnerability in nifti_convert_n2hdr2nim()… |
| 2026-10-15 22:19:28 | [CVE-2026-111277](https://nvd.nist.gov/vuln/detail/CVE-2026-111277) | High | 8.7 | NivoCart through 2.5.1 contains a missing authorization vulnerability in the download() action of account/order that al… |
| 2026-10-15 22:19:28 | [CVE-2026-111278](https://nvd.nist.gov/vuln/detail/CVE-2026-111278) | Medium | 6.9 | NivoCart through 2.5.1 contains a CAPTCHA bypass vulnerability that allows unauthenticated attackers to defeat form pro… |
| 2026-10-15 22:19:29 | [CVE-2026-111279](https://nvd.nist.gov/vuln/detail/CVE-2026-111279) | High | 8.7 | Dragonfly through 2.0.2 contains an unbounded memory allocation vulnerability that allows unauthenticated clients to ex… |
| 2026-10-15 22:19:29 | [CVE-2026-111280](https://nvd.nist.gov/vuln/detail/CVE-2026-111280) | High | 8.3 | snap7 through 1.4.3 contains an out-of-bounds write vulnerability in TSnap7MicroClient::opReadArea() that allows malici… |
| 2026-10-15 22:19:29 | [CVE-2026-111281](https://nvd.nist.gov/vuln/detail/CVE-2026-111281) | Critical | 9.3 | Jooan JA-A12 IP cameras with firmware 009_20171107 and 05.02.31.105 contain a remote code execution vulnerability that… |
| 2026-10-15 22:19:29 | [CVE-2026-111282](https://nvd.nist.gov/vuln/detail/CVE-2026-111282) | High | 8.8 | Driftregion iso14229 before 0.10.1 contains an integer wraparound in Handle_0x38_RequestFileTransfer that lets unauthen… |
| 2026-10-15 22:19:29 | [CVE-2026-111283](https://nvd.nist.gov/vuln/detail/CVE-2026-111283) | Critical | 9.5 | BMC Helix Network Management on-prem before 26.3.01 contains an authentication bypass vulnerability that allows unauthe… |
| 2026-10-15 22:19:29 | [CVE-2026-111284](https://nvd.nist.gov/vuln/detail/CVE-2026-111284) | Medium | 5.1 | Aureus ERP through 1.6.0 contains a stored cross-site scripting vulnerability in HolidayAction.php that allows authenti… |
| 2026-10-15 22:19:30 | [CVE-2026-111312](https://nvd.nist.gov/vuln/detail/CVE-2026-111312) | Critical | 9.2 | OpenHealth through 0.2.0 contains a missing authentication and authorization vulnerability in the /api/health-data/[id]… |
| 2026-10-15 22:19:30 | [CVE-2026-111313](https://nvd.nist.gov/vuln/detail/CVE-2026-111313) | High | 7.1 | JobOps through 0.13.1 contains a server-side request forgery vulnerability in the POST /api/manual-jobs/fetch handler t… |
| 2026-10-15 22:19:30 | [CVE-2026-111320](https://nvd.nist.gov/vuln/detail/CVE-2026-111320) | Medium | 6.9 | ValueCell through 0.1.20 contains an unauthenticated server-side request forgery vulnerability that allows remote attac… |
| 2026-10-15 22:19:30 | [CVE-2026-111321](https://nvd.nist.gov/vuln/detail/CVE-2026-111321) | Medium | 5.3 | TaskingAI through 0.3.0 contains a server-side request forgery vulnerability that allows authenticated attackers to mak… |
| 2026-10-15 22:19:30 | [CVE-2026-111322](https://nvd.nist.gov/vuln/detail/CVE-2026-111322) | Critical | 9.3 | Archon 0.2.13 through 0.11.1 contains a missing authentication vulnerability that allows unauthenticated attackers to a… |
| 2026-10-15 22:19:30 | [CVE-2026-111323](https://nvd.nist.gov/vuln/detail/CVE-2026-111323) | Medium | 6.9 | RedAmon through 7.0.1 contains an unauthenticated server-side request forgery vulnerability in the agent POST /tradecra… |
| 2026-10-15 22:19:30 | [CVE-2026-111324](https://nvd.nist.gov/vuln/detail/CVE-2026-111324) | Medium | 6.9 | rustdesk-api through 2.7 contains an authorization bypass vulnerability that allows unauthenticated attackers to overwr… |
| 2026-10-15 22:19:31 | [CVE-2026-111329](https://nvd.nist.gov/vuln/detail/CVE-2026-111329) | Critical | 9.3 | JuggleIM im-server through 1.8.16 ships default administrator credentials admin/123456 that allow unauthenticated remot… |
| 2026-10-15 22:19:31 | [CVE-2026-111330](https://nvd.nist.gov/vuln/detail/CVE-2026-111330) | High | 8.2 | JuggleIM im-server through 1.8.16 contains a weak password hashing vulnerability that stores admin console passwords as… |
| 2026-10-15 22:19:31 | [CVE-2026-111331](https://nvd.nist.gov/vuln/detail/CVE-2026-111331) | Medium | 5.3 | Dokploy through 0.30.8 contains a cross-organization authorization bypass in the port tRPC router that allows authentic… |
| 2026-10-15 22:19:31 | [CVE-2026-111332](https://nvd.nist.gov/vuln/detail/CVE-2026-111332) | Medium | 6.3 | OxiCloud 0.9.1 through 0.9.3 contains an incorrect authorization vulnerability that allows anonymous visitors to keep s… |
| 2026-10-15 22:19:31 | [CVE-2026-111343](https://nvd.nist.gov/vuln/detail/CVE-2026-111343) | Medium | 5.3 | pig through 4.1.1 contains a missing authorization vulnerability in SysUserController.user that allows any authenticate… |
| 2026-10-15 22:19:31 | [CVE-2026-111344](https://nvd.nist.gov/vuln/detail/CVE-2026-111344) | Medium | 5.3 | APITable through 1.14.0-beta contains an authorization bypass vulnerability that allows authenticated users to read nod… |
| 2026-10-15 22:19:31 | [CVE-2026-111345](https://nvd.nist.gov/vuln/detail/CVE-2026-111345) | Medium | 5.3 | Trudesk through 1.2.11 contains an authorization bypass vulnerability that allows any authenticated user to read privat… |
| 2026-10-15 22:19:32 | [CVE-2026-111346](https://nvd.nist.gov/vuln/detail/CVE-2026-111346) | Medium | 5.3 | ZenTao PMS through 22.6 contains an authorization bypass vulnerability in action::editComment that allows authenticated… |
| 2026-10-15 22:19:32 | [CVE-2026-111347](https://nvd.nist.gov/vuln/detail/CVE-2026-111347) | High | 8.2 | go-ldap-admin through 0.6.2 embeds a hard-coded RSA private key, published in the public repository, that protects encr… |
| 2026-10-15 22:19:32 | [CVE-2026-111348](https://nvd.nist.gov/vuln/detail/CVE-2026-111348) | Medium | 5.3 | Likeshop through 3.5.1 contains an insecure direct object reference vulnerability in AfterSale.php and AfterSaleLogic.p… |
| 2026-10-15 22:19:32 | [CVE-2026-111349](https://nvd.nist.gov/vuln/detail/CVE-2026-111349) | Medium | 6.9 | Craftplan through 0.7.5 contains a missing authorization vulnerability in the CRM Customer resource that allows unauthe… |
| 2026-10-15 22:19:32 | [CVE-2026-111350](https://nvd.nist.gov/vuln/detail/CVE-2026-111350) | Low | 2.3 | Papermark through 0.22.0 contains a missing authorization vulnerability in the data room viewer group API that allows a… |
| 2026-10-15 22:19:32 | [CVE-2026-111351](https://nvd.nist.gov/vuln/detail/CVE-2026-111351) | Low | 2.3 | metasfresh through 5.175 contains a missing record-level authorization vulnerability in BoardRestController that allows… |
| 2026-10-15 22:19:33 | [CVE-2026-111352](https://nvd.nist.gov/vuln/detail/CVE-2026-111352) | High | 8.7 | ThinkCMF through 8.0.1 contains an incorrect authorization vulnerability in RestAdminBaseController that allows restric… |
| 2026-10-15 22:19:33 | [CVE-2026-111353](https://nvd.nist.gov/vuln/detail/CVE-2026-111353) | Medium | 5.3 | Peppermint through 0.5.5 contains a missing authorization vulnerability that allows any authenticated user to create ti… |
| 2026-10-15 22:19:33 | [CVE-2026-111354](https://nvd.nist.gov/vuln/detail/CVE-2026-111354) | Low | 2.3 | crmeb_java through 3.1 contains an authorization bypass vulnerability that allows authenticated members to read other m… |
| 2026-10-15 22:19:33 | [CVE-2026-111355](https://nvd.nist.gov/vuln/detail/CVE-2026-111355) | Medium | 5.3 | zhontai Admin.Core through 10.1.0 contains an authorization bypass vulnerability that allows authenticated users to ign… |
| 2026-10-15 22:19:33 | [CVE-2026-111356](https://nvd.nist.gov/vuln/detail/CVE-2026-111356) | Critical | 9.1 | MacCMS v10 through 2026.1000.4056 does not limit attempts on the six-digit password recovery code, allowing unauthentic… |
| 2026-10-15 22:19:33 | [CVE-2026-111358](https://nvd.nist.gov/vuln/detail/CVE-2026-111358) | Medium | 5.3 | SendPortal sendportal-core through 4.0.1 contains an authorization bypass vulnerability that allows authenticated works… |
| 2026-10-15 22:19:33 | [CVE-2026-111359](https://nvd.nist.gov/vuln/detail/CVE-2026-111359) | High | 7.1 | CRMEB 5.6.1 through 6.0.0 contains an insecure direct object reference vulnerability that allows authenticated storefro… |
| 2026-10-15 22:19:34 | [CVE-2026-111363](https://nvd.nist.gov/vuln/detail/CVE-2026-111363) | High | 7.1 | BISHENG through 3.0.0-beta4 contains an insecure direct object reference vulnerability that allows authenticated low-pr… |
| 2026-10-15 22:19:34 | [CVE-2026-111364](https://nvd.nist.gov/vuln/detail/CVE-2026-111364) | High | 7.1 | MinDoc through 2.2-beta.2 contains an insecure direct object reference vulnerability in DocumentController.Content that… |
| 2026-10-15 22:19:34 | [CVE-2026-111365](https://nvd.nist.gov/vuln/detail/CVE-2026-111365) | High | 7.0 | cool-admin-midway through 8.0.0 contains an authorization bypass vulnerability that allows non-superadmin admins to rea… |
| 2026-10-15 22:19:34 | [CVE-2026-111366](https://nvd.nist.gov/vuln/detail/CVE-2026-111366) | High | 8.6 | cool-admin-midway through 8.0.0 contains an authorization bypass vulnerability that allows department-limited admins to… |
| 2026-10-15 22:19:34 | [CVE-2026-111367](https://nvd.nist.gov/vuln/detail/CVE-2026-111367) | Medium | 6.9 | BillionMail through 4.9 contains a hard-coded cryptographic key vulnerability that allows unauthenticated attackers to… |
| 2026-10-15 22:19:34 | [CVE-2026-111368](https://nvd.nist.gov/vuln/detail/CVE-2026-111368) | Medium | 6.1 | ClassroomIO through 1.0.0 contains an insecure direct object reference vulnerability in the Hono API course submission… |
| 2026-10-15 22:19:35 | [CVE-2026-111369](https://nvd.nist.gov/vuln/detail/CVE-2026-111369) | High | 7.1 | ClassroomIO through 1.0.0 contains an incorrect authorization vulnerability in the PUT and DELETE /:lessonId lesson rou… |
| 2026-10-15 22:21:11 | [CVE-2026-92228](https://nvd.nist.gov/vuln/detail/CVE-2026-92228) |  |  | The Apache Airflow Keycloak provider's multi-team provisioning (`_attach_team_permissions`) granted every team role glo… |
| 2026-10-15 22:21:12 | [CVE-2026-94134](https://nvd.nist.gov/vuln/detail/CVE-2026-94134) |  |  | The Apache Airflow SSH provider hook disables SSH host-key verification by default: unless `host_key` is configured or… |
| 2026-10-15 22:21:12 | [CVE-2026-94135](https://nvd.nist.gov/vuln/detail/CVE-2026-94135) |  |  | The Apache Airflow SFTP provider's deferrable code paths (`SFTPTrigger`, `SFTPHookAsync`, `SFTPClientPool`) disable SSH… |
| 2026-10-15 22:21:19 | [CVE-2026-96806](https://nvd.nist.gov/vuln/detail/CVE-2026-96806) |  |  | The Apache Airflow Keycloak auth manager did not end the session on logout: the logout route revoked the presented toke… |
| 2026-10-15 23:17:12 | [CVE-2025-3778](https://nvd.nist.gov/vuln/detail/CVE-2025-3778) |  |  | Rejected reason: This CVE ID has been rejected or withdrawn by its CVE Numbering Authority. |
| 2026-10-15 23:17:24 | [CVE-2026-107172](https://nvd.nist.gov/vuln/detail/CVE-2026-107172) |  |  | Rejected reason: This CVE ID has been rejected or withdrawn by its CVE Numbering Authority. |
| 2026-10-15 23:17:25 | [CVE-2026-107316](https://nvd.nist.gov/vuln/detail/CVE-2026-107316) |  |  | Rejected reason: This CVE ID has been rejected or withdrawn by its CVE Numbering Authority. |
| 2026-10-15 23:17:36 | [CVE-2026-2937](https://nvd.nist.gov/vuln/detail/CVE-2026-2937) |  |  | Rejected reason: This CVE ID has been rejected or withdrawn by its CVE Numbering Authority. |
| 2026-10-15 23:17:38 | [CVE-2026-5819](https://nvd.nist.gov/vuln/detail/CVE-2026-5819) |  |  | Rejected reason: This CVE ID has been rejected or withdrawn by its CVE Numbering Authority. |
| 2026-10-15 23:19:15 | [CVE-2026-8311](https://nvd.nist.gov/vuln/detail/CVE-2026-8311) |  |  | Rejected reason: This CVE ID has been rejected or withdrawn by its CVE Numbering Authority. |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
