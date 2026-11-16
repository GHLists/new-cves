# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-11-16 15:19 UTC

New CVEs published between 2026-11-16 14:18 UTC and 2026-11-16 15:19 UTC.

[Full CSV](data/new-cves-2026-11-16T15-19-19-334475Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-11-16 15:17:05 | [CVE-2024-58407](https://nvd.nist.gov/vuln/detail/CVE-2024-58407) | Medium | 6.9 | Microsoft jxrlib through 1.1 and the mircomir jxrlib fork before 1.3.1 contain a global buffer over-read vulnerability… |
| 2026-11-16 15:17:06 | [CVE-2024-58408](https://nvd.nist.gov/vuln/detail/CVE-2024-58408) | Medium | 6.9 | Microsoft jxrlib through 1.1 and the mircomir jxrlib fork before 1.3.1 contain a global buffer over-read vulnerability… |
| 2026-11-16 15:17:06 | [CVE-2025-5809](https://nvd.nist.gov/vuln/detail/CVE-2025-5809) | High | 7.1 | An improper privilege management vulnerability in an LDAP extension used with OpenText eDirectory could require a techn… |
| 2026-11-16 15:17:18 | [CVE-2026-127043](https://nvd.nist.gov/vuln/detail/CVE-2026-127043) | High | 7.1 | Insecure direct object reference (IDOR) in the myGESTIÓN Time Tracking module. The server skips the permission check wh… |
| 2026-11-16 15:17:19 | [CVE-2026-127044](https://nvd.nist.gov/vuln/detail/CVE-2026-127044) | High | 7.1 | Insecure direct object reference (IDOR) in the STEL Order Tempo module. The server retrieves data based on the `emplead… |
| 2026-11-16 15:17:22 | [CVE-2026-129851](https://nvd.nist.gov/vuln/detail/CVE-2026-129851) | Medium | 6.9 | SeaweedFS before 4.42 contains a server-side request forgery vulnerability in the VolumeServer.FetchAndWriteNeedle gRPC… |
| 2026-11-16 15:17:22 | [CVE-2026-129852](https://nvd.nist.gov/vuln/detail/CVE-2026-129852) | Medium | 6.9 | SeaweedFS before 4.42 contains an information disclosure vulnerability that allows unauthenticated attackers to probe l… |
| 2026-11-16 15:17:22 | [CVE-2026-129853](https://nvd.nist.gov/vuln/detail/CVE-2026-129853) | High | 8.2 | LimeSurvey before 6.17.16+260814 and 7.x before 7.0.10+260813 contains an unauthenticated SQL injection vulnerability i… |
| 2026-11-16 15:17:22 | [CVE-2026-129854](https://nvd.nist.gov/vuln/detail/CVE-2026-129854) | High | 8.7 | RedAmon 4.0.0 before 7.8.0 contains a missing object-level authorization vulnerability that allows authenticated users… |
| 2026-11-16 15:17:22 | [CVE-2026-129855](https://nvd.nist.gov/vuln/detail/CVE-2026-129855) | High | 8.7 | RedAmon before 7.8.0 contains a missing authentication vulnerability in the kali-sandbox terminal server that allows un… |
| 2026-11-16 15:17:22 | [CVE-2026-129856](https://nvd.nist.gov/vuln/detail/CVE-2026-129856) | Medium | 5.1 | wallabag 2.3.3 before 2.6.16 contains a stored cross-site scripting vulnerability that allows unauthenticated attackers… |
| 2026-11-16 15:17:23 | [CVE-2026-129857](https://nvd.nist.gov/vuln/detail/CVE-2026-129857) | High | 8.5 | Microsoft jxrlib through 1.1 and the mircomir jxrlib fork before 1.3.1 contain a heap buffer overflow in ReadBinaryData… |
| 2026-11-16 15:17:23 | [CVE-2026-129858](https://nvd.nist.gov/vuln/detail/CVE-2026-129858) | Medium | 6.8 | Microsoft jxrlib through 1.1 and the mircomir jxrlib fork before 1.3.6 contain a stack buffer over-read vulnerability i… |
| 2026-11-16 15:17:23 | [CVE-2026-129859](https://nvd.nist.gov/vuln/detail/CVE-2026-129859) | Medium | 6.8 | Microsoft jxrlib through 1.1 and the mircomir jxrlib fork before 1.3.1 contain a NULL pointer dereference vulnerability… |
| 2026-11-16 15:17:23 | [CVE-2026-129860](https://nvd.nist.gov/vuln/detail/CVE-2026-129860) | Medium | 6.8 | Microsoft jxrlib through 1.1 and the mircomir jxrlib fork before 1.3.7 contain a reachable assertion vulnerability in P… |
| 2026-11-16 15:17:23 | [CVE-2026-129861](https://nvd.nist.gov/vuln/detail/CVE-2026-129861) | Medium | 6.0 | @tinacms/graphql 2.2.2 through 4.1.0 contains a path traversal vulnerability that allows authenticated users to write f… |
| 2026-11-16 15:17:23 | [CVE-2026-129862](https://nvd.nist.gov/vuln/detail/CVE-2026-129862) | Medium | 6.9 | Koillection before 1.8.6 contains an information disclosure vulnerability that allows unauthenticated attackers to view… |
| 2026-11-16 15:17:24 | [CVE-2026-129863](https://nvd.nist.gov/vuln/detail/CVE-2026-129863) | High | 7.1 | GitBucket through 4.48.0 contains an incorrect authorization vulnerability that allows authenticated users to edit and… |
| 2026-11-16 15:17:24 | [CVE-2026-129864](https://nvd.nist.gov/vuln/detail/CVE-2026-129864) | High | 7.1 | Frappe CRM before 1.84.0 contains a missing authorization vulnerability in the get_deal_contacts method that allows aut… |
| 2026-11-16 15:17:24 | [CVE-2026-129865](https://nvd.nist.gov/vuln/detail/CVE-2026-129865) | High | 7.1 | Dinky through 1.2.5 contains a missing authorization vulnerability in DataSourceController.testConnect that allows any… |
| 2026-11-16 15:17:24 | [CVE-2026-129866](https://nvd.nist.gov/vuln/detail/CVE-2026-129866) | Medium | 5.3 | Dinky through 1.2.5 contains a missing authorization vulnerability in ClusterConfigurationController that allows authen… |
| 2026-11-16 15:17:24 | [CVE-2026-129867](https://nvd.nist.gov/vuln/detail/CVE-2026-129867) | Medium | 5.1 | Rocboss paopao-ce through 0.6.0-alpha.3 contains a stored cross-site scripting vulnerability that allows registered use… |
| 2026-11-16 15:17:24 | [CVE-2026-129868](https://nvd.nist.gov/vuln/detail/CVE-2026-129868) | High | 7.1 | Rocboss paopao-ce through 0.6.0-alpha.3 fails to validate the attachment_price field when creating posts, allowing auth… |
| 2026-11-16 15:17:25 | [CVE-2026-129869](https://nvd.nist.gov/vuln/detail/CVE-2026-129869) | Medium | 6.9 | SamWaf 1.0.128 through 1.3.25-beta.11 contains a request body inspection bypass vulnerability in WafEngine.ServeHTTP th… |
| 2026-11-16 15:17:25 | [CVE-2026-129870](https://nvd.nist.gov/vuln/detail/CVE-2026-129870) | High | 7.2 | Rocboss paopao-ce 0.2.0 through 0.6.0-alpha.3 contains a path traversal vulnerability in LocalOSS DeleteObject that all… |
| 2026-11-16 15:17:25 | [CVE-2026-129871](https://nvd.nist.gov/vuln/detail/CVE-2026-129871) | Medium | 6.9 | Rocboss paopao-ce through 0.6.0-alpha.3 contains a payment bypass vulnerability that allows unauthenticated attackers t… |
| 2026-11-16 15:17:25 | [CVE-2026-129872](https://nvd.nist.gov/vuln/detail/CVE-2026-129872) | High | 7.7 | REBUILD 2.7.0 through 4.5.4 contains an SQL injection vulnerability that allows low-privileged authenticated users to i… |
| 2026-11-16 15:17:25 | [CVE-2026-129873](https://nvd.nist.gov/vuln/detail/CVE-2026-129873) | High | 8.7 | REBUILD 4.3.0 through 4.5.4 contains a privilege escalation vulnerability that allows low-privileged authenticated user… |
| 2026-11-16 15:17:26 | [CVE-2026-129874](https://nvd.nist.gov/vuln/detail/CVE-2026-129874) | High | 8.7 | REBUILD 3.5.0 through 4.5.4 contains a privilege escalation vulnerability that allows low-privileged authenticated user… |
| 2026-11-16 15:17:26 | [CVE-2026-129875](https://nvd.nist.gov/vuln/detail/CVE-2026-129875) | High | 8.7 | REBUILD 4.5.0 through 4.5.4 contains an information disclosure vulnerability that allows low-privileged authenticated u… |
| 2026-11-16 15:17:26 | [CVE-2026-129876](https://nvd.nist.gov/vuln/detail/CVE-2026-129876) | Medium | 6.8 | OfficeCLI 1.0.56 through 1.0.161 contains a stored cross-site scripting vulnerability in the officecli watch preview th… |
| 2026-11-16 15:17:26 | [CVE-2026-129877](https://nvd.nist.gov/vuln/detail/CVE-2026-129877) | High | 8.7 | DeepAudit 2.0.0-beta.1 through 3.8.0 contains an information disclosure vulnerability that allows unauthenticated attac… |
| 2026-11-16 15:17:26 | [CVE-2026-129878](https://nvd.nist.gov/vuln/detail/CVE-2026-129878) | High | 7.1 | DeepAudit 2.0.0-beta.1 through 3.8.0 contains an HTML injection vulnerability in ReportGenerator.generate_task_report t… |
| 2026-11-16 15:17:26 | [CVE-2026-129879](https://nvd.nist.gov/vuln/detail/CVE-2026-129879) | High | 8.7 | DeepAudit 2.0.0-beta.1 through 3.8.0 contains a path traversal vulnerability that allows authenticated users to write a… |
| 2026-11-16 15:17:27 | [CVE-2026-129880](https://nvd.nist.gov/vuln/detail/CVE-2026-129880) | High | 8.3 | DeepAudit 2.0.0-beta.5 through 3.8.0 contains a server-side request forgery vulnerability that allows registered users… |
| 2026-11-16 15:17:27 | [CVE-2026-129881](https://nvd.nist.gov/vuln/detail/CVE-2026-129881) | Medium | 6.3 | Weblate 2026.6 through 2026.11.2 contains an information disclosure vulnerability in ChangeManager.last_changes() that… |
| 2026-11-16 15:17:27 | [CVE-2026-129882](https://nvd.nist.gov/vuln/detail/CVE-2026-129882) | Medium | 6.3 | Kiwi TCMS before 17.1 contains a hard-coded cryptographic key vulnerability that allows remote attackers to forge signe… |
| 2026-11-16 15:17:27 | [CVE-2026-129883](https://nvd.nist.gov/vuln/detail/CVE-2026-129883) | Medium | 5.1 | thirdweb Dashboard through commit 940b3745 contains an open redirect vulnerability that allows remote attackers to send… |
| 2026-11-16 15:17:27 | [CVE-2026-129884](https://nvd.nist.gov/vuln/detail/CVE-2026-129884) | Medium | 6.3 | thirdweb Dashboard through commit 940b3745 contains a missing authorization vulnerability in the fetchClientSecret Next… |
| 2026-11-16 15:17:27 | [CVE-2026-129885](https://nvd.nist.gov/vuln/detail/CVE-2026-129885) | Medium | 6.3 | Unrolled Secure before 1.18.0 contains an SSLRedirect bypass vulnerability in Secure.isSSL() that trusts the client-sup… |
| 2026-11-16 15:17:27 | [CVE-2026-129886](https://nvd.nist.gov/vuln/detail/CVE-2026-129886) | Medium | 6.9 | thirdweb Dashboard through commit 940b3745 contains a missing authorization vulnerability in revalidatePathAction and r… |
| 2026-11-16 15:17:28 | [CVE-2026-129887](https://nvd.nist.gov/vuln/detail/CVE-2026-129887) | Medium | 5.3 | thirdweb Dashboard through commit 940b3745 contains an information disclosure vulnerability that allows authenticated u… |
| 2026-11-16 15:17:28 | [CVE-2026-129888](https://nvd.nist.gov/vuln/detail/CVE-2026-129888) | High | 7.6 | Cetmix Tower through 17.0.3.0.0 and 18.0 before 18.0.4.0.1 contains an improper SSH host key verification vulnerability… |
| 2026-11-16 15:17:28 | [CVE-2026-129940](https://nvd.nist.gov/vuln/detail/CVE-2026-129940) | Medium | 5.3 | Prime CMS (@primecms/core) through 0.4.0-beta.0 contains an open redirect vulnerability in the unauthenticated GET /pri… |
| 2026-11-16 15:17:28 | [CVE-2026-129941](https://nvd.nist.gov/vuln/detail/CVE-2026-129941) | Critical | 9.3 | Prime CMS (@primecms/core) through 0.4.0-beta.0 contains an authentication bypass vulnerability that allows unauthentic… |
| 2026-11-16 15:17:28 | [CVE-2026-129942](https://nvd.nist.gov/vuln/detail/CVE-2026-129942) | Medium | 6.9 | Prime CMS (@primecms/core) through 0.4.0-beta.0 contains a missing authentication vulnerability that allows unauthentic… |
| 2026-11-16 15:17:29 | [CVE-2026-129943](https://nvd.nist.gov/vuln/detail/CVE-2026-129943) | High | 8.6 | Prime CMS (@primecms/core) through 0.4.0-beta.0 contains an OS command injection vulnerability in the updateSystem Grap… |
| 2026-11-16 15:17:29 | [CVE-2026-129944](https://nvd.nist.gov/vuln/detail/CVE-2026-129944) | Medium | 6.3 | Keystatic through 0.6.9 contains a path traversal vulnerability in the getIsPathValid function that allows unauthentica… |
| 2026-11-16 15:17:29 | [CVE-2026-129945](https://nvd.nist.gov/vuln/detail/CVE-2026-129945) | Medium | 5.3 | Keystatic through 0.6.9 contains a login cross-site request forgery vulnerability in the githubOauthCallback handler th… |
| 2026-11-16 15:17:29 | [CVE-2026-129946](https://nvd.nist.gov/vuln/detail/CVE-2026-129946) | Medium | 5.1 | Keystatic through 0.6.9 contains a stored cross-site scripting vulnerability in the DocumentRenderer component that all… |
| 2026-11-16 15:17:29 | [CVE-2026-129947](https://nvd.nist.gov/vuln/detail/CVE-2026-129947) | High | 8.6 | Contentlayer @contentlayer/core through 0.3.4 contains a code injection vulnerability that allows attackers to inject J… |
| 2026-11-16 15:17:29 | [CVE-2026-129948](https://nvd.nist.gov/vuln/detail/CVE-2026-129948) | High | 8.7 | Contentlayer @contentlayer/source-files through 0.3.4 contains a code injection vulnerability that allows attackers who… |
| 2026-11-16 15:17:30 | [CVE-2026-129949](https://nvd.nist.gov/vuln/detail/CVE-2026-129949) | Medium | 5.1 | Rowy through 3.0.0 contains a stored cross-site scripting vulnerability that allows authenticated users with table writ… |
| 2026-11-16 15:17:30 | [CVE-2026-129950](https://nvd.nist.gov/vuln/detail/CVE-2026-129950) | Medium | 5.3 | Rowy through 3.0.0 contains an incorrect permission assignment vulnerability in default Firebase Storage rules that gra… |
| 2026-11-16 15:17:30 | [CVE-2026-129951](https://nvd.nist.gov/vuln/detail/CVE-2026-129951) | Medium | 5.1 | Rowy through 3.0.0 contains a stored cross-site scripting vulnerability that allows authenticated users with table writ… |
| 2026-11-16 15:17:30 | [CVE-2026-129952](https://nvd.nist.gov/vuln/detail/CVE-2026-129952) | Critical | 9.3 | NodePress through 8.5.1 contains an authentication bypass vulnerability that allows unauthenticated remote attackers to… |
| 2026-11-16 15:17:30 | [CVE-2026-129953](https://nvd.nist.gov/vuln/detail/CVE-2026-129953) | Medium | 6.9 | NodePress through 8.5.1 contains a rate limit bypass vulnerability that allows unauthenticated attackers to evade throt… |
| 2026-11-16 15:17:30 | [CVE-2026-129954](https://nvd.nist.gov/vuln/detail/CVE-2026-129954) | Medium | 5.3 | NodePress through 8.5.1 contains an HTML injection vulnerability in linesToEmailContent() that allows unauthenticated a… |
| 2026-11-16 15:17:31 | [CVE-2026-129955](https://nvd.nist.gov/vuln/detail/CVE-2026-129955) | Critical | 9.3 | NodePress through 8.5.1 contains an authentication bypass vulnerability that allows unauthenticated attackers to gain a… |
| 2026-11-16 15:17:31 | [CVE-2026-129956](https://nvd.nist.gov/vuln/detail/CVE-2026-129956) | High | 8.5 | Sandboxie-Plus before 1.18.6 contains a local privilege escalation vulnerability in SbieSvc that allows standard users… |
| 2026-11-16 15:17:31 | [CVE-2026-129957](https://nvd.nist.gov/vuln/detail/CVE-2026-129957) | High | 8.6 | PrestaShop before 8.2.9 and 9.0.0 before 9.2.1 contains a path traversal vulnerability in back-office theme and module… |
| 2026-11-16 15:17:32 | [CVE-2026-3859](https://nvd.nist.gov/vuln/detail/CVE-2026-3859) | High | 7.4 | XSS vulnerability in Vibe Versions <= 4.0.8.7 could allow an attacker to inject malicious JavaScript through crafted se… |
| 2026-11-16 15:17:32 | [CVE-2026-3860](https://nvd.nist.gov/vuln/detail/CVE-2026-3860) | Low | 2.3 | CSRF vulnerability in OpenText Vibe versions <= 4.0.8.7 could expose the token over an insecure connection or make it a… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
