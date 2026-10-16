# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-16 18:18 UTC

New CVEs published between 2026-10-16 17:19 UTC and 2026-10-16 18:18 UTC.

[Full CSV](data/new-cves-2026-10-16T18-18-31-210912Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-10-16 18:17:14 | [CVE-2026-102551](https://nvd.nist.gov/vuln/detail/CVE-2026-102551) | Critical | 9.2 | Improper verification of the source of a communication channel in the IPv6 Router Advertisement handler in Amazon FreeR… |
| 2026-10-16 18:17:14 | [CVE-2026-102552](https://nvd.nist.gov/vuln/detail/CVE-2026-102552) | High | 8.2 | Improper verification of the source of a communication channel in the DNS resolver in Amazon FreeRTOS-Plus-TCP before V… |
| 2026-10-16 18:17:31 | [CVE-2026-109461](https://nvd.nist.gov/vuln/detail/CVE-2026-109461) | Medium | 5.9 | Origin validation error in Microsoft Authentication Library (MSAL) for Node.js allows an unauthorized attacker to discl… |
| 2026-10-16 18:17:31 | [CVE-2026-109587](https://nvd.nist.gov/vuln/detail/CVE-2026-109587) | Critical | 9.3 | Incorrect authorization in the Arm Cortex-R82 (Armv8-R AArch64) MPU port in FreeRTOS-Kernel V11.3.0 and V11.3.1 might a… |
| 2026-10-16 18:17:31 | [CVE-2026-109588](https://nvd.nist.gov/vuln/detail/CVE-2026-109588) | Critical | 9.3 | Numeric truncation of the buffer length in the MPU buffer authorization check in FreeRTOS-Kernel V11.3.0 and V11.3.1 on… |
| 2026-10-16 18:17:31 | [CVE-2026-109838](https://nvd.nist.gov/vuln/detail/CVE-2026-109838) | Medium | 5.1 | IBM Db2 Genius Hub 1.0 could allow a local attacker to obtain sensitive information due to improper verification of cry… |
| 2026-10-16 18:17:31 | [CVE-2026-109839](https://nvd.nist.gov/vuln/detail/CVE-2026-109839) | Low | 3.1 | IBM Db2 Genius Hub 1.0 could allow a remote authenticated attacker to bypass security restrictions due to a missing ini… |
| 2026-10-16 18:17:38 | [CVE-2026-111392](https://nvd.nist.gov/vuln/detail/CVE-2026-111392) | Medium | 6.3 | SGLang through 0.5.21 trusts caller-supplied mm_hashes values as the multimodal prefix-cache key, allowing remote attac… |
| 2026-10-16 18:17:39 | [CVE-2026-111603](https://nvd.nist.gov/vuln/detail/CVE-2026-111603) | Medium | 5.3 | PlayEdu through 2.3 contains a missing authorization vulnerability in the CourseController that allows authenticated st… |
| 2026-10-16 18:17:39 | [CVE-2026-111604](https://nvd.nist.gov/vuln/detail/CVE-2026-111604) | Medium | 5.1 | eladmin through 2.7 contains an authorization bypass vulnerability that allows department-scoped user managers to modif… |
| 2026-10-16 18:17:39 | [CVE-2026-111605](https://nvd.nist.gov/vuln/detail/CVE-2026-111605) | High | 8.6 | Jpom through 2.11.12 contains an authorization bypass vulnerability in SshFileController that allows authenticated work… |
| 2026-10-16 18:17:39 | [CVE-2026-111606](https://nvd.nist.gov/vuln/detail/CVE-2026-111606) | High | 8.6 | Huly Platform through 0.7.432 contains a missing authorization vulnerability that allows any authenticated user to merg… |
| 2026-10-16 18:17:39 | [CVE-2026-111607](https://nvd.nist.gov/vuln/detail/CVE-2026-111607) | High | 7.1 | Jeepay through 3.2.9 contains an insecure direct object reference vulnerability that allows authenticated merchant user… |
| 2026-10-16 18:17:39 | [CVE-2026-111608](https://nvd.nist.gov/vuln/detail/CVE-2026-111608) | Low | 2.3 | Jeepay through 3.2.9 contains an insecure direct object reference vulnerability that allows authenticated merchant user… |
| 2026-10-16 18:17:40 | [CVE-2026-111609](https://nvd.nist.gov/vuln/detail/CVE-2026-111609) | Medium | 5.1 | PKP Open Journal Systems through 3.5.0-5 contains an insecure direct object reference vulnerability that allows journal… |
| 2026-10-16 18:17:40 | [CVE-2026-111610](https://nvd.nist.gov/vuln/detail/CVE-2026-111610) | Medium | 5.3 | B3log Solo through 4.4.0 contains a missing authorization vulnerability in ArticleConsole that allows authenticated aut… |
| 2026-10-16 18:17:40 | [CVE-2026-111611](https://nvd.nist.gov/vuln/detail/CVE-2026-111611) | Medium | 5.3 | roncoo-education through 25.0.0-RELEASE contains an insecure direct object reference vulnerability that allows authenti… |
| 2026-10-16 18:17:40 | [CVE-2026-111612](https://nvd.nist.gov/vuln/detail/CVE-2026-111612) | High | 8.7 | netdisk-fast-download through 0.4.8 contains an information disclosure vulnerability that allows unauthenticated attack… |
| 2026-10-16 18:17:40 | [CVE-2026-111613](https://nvd.nist.gov/vuln/detail/CVE-2026-111613) | High | 8.7 | AllData through 0.7.1 contains an unauthenticated JDBC injection vulnerability that allows remote attackers to open arb… |
| 2026-10-16 18:17:40 | [CVE-2026-111614](https://nvd.nist.gov/vuln/detail/CVE-2026-111614) | High | 7.1 | DataCap through 2025.1.1 contains an insecure direct object reference vulnerability in BaseController.getInfoForPath th… |
| 2026-10-16 18:17:40 | [CVE-2026-111615](https://nvd.nist.gov/vuln/detail/CVE-2026-111615) | High | 7.1 | Mall4cloud through 4.0 contains an insecure direct object reference vulnerability that allows authenticated merchants t… |
| 2026-10-16 18:17:41 | [CVE-2026-111616](https://nvd.nist.gov/vuln/detail/CVE-2026-111616) | Medium | 6.9 | Oqtane Framework through 10.2.6 contains an authorization bypass vulnerability in SettingController that allows a site… |
| 2026-10-16 18:17:41 | [CVE-2026-111617](https://nvd.nist.gov/vuln/detail/CVE-2026-111617) | Medium | 6.9 | WHartTest through 2.8.1 contains a missing authentication vulnerability that allows unauthenticated attackers to connec… |
| 2026-10-16 18:17:41 | [CVE-2026-111618](https://nvd.nist.gov/vuln/detail/CVE-2026-111618) | Medium | 6.9 | CoAI (Chat Nio) through 4.0.0 contains an unauthenticated path traversal vulnerability in the generation and article ar… |
| 2026-10-16 18:17:41 | [CVE-2026-111619](https://nvd.nist.gov/vuln/detail/CVE-2026-111619) | High | 7.1 | FilePress through 3.0.1 contains an sql injection vulnerability that allows authenticated low-privilege users to inject… |
| 2026-10-16 18:17:41 | [CVE-2026-111620](https://nvd.nist.gov/vuln/detail/CVE-2026-111620) | Medium | 6.0 | O2OA through 10.0.2-ce contains an authorization bypass vulnerability in x_processplatform_assemble_surface that allows… |
| 2026-10-16 18:17:41 | [CVE-2026-111621](https://nvd.nist.gov/vuln/detail/CVE-2026-111621) | Medium | 5.3 | TDuck Survey Form through 5.3 contains a missing authorization vulnerability that allows any authenticated user to read… |
| 2026-10-16 18:17:41 | [CVE-2026-111622](https://nvd.nist.gov/vuln/detail/CVE-2026-111622) | High | 7.6 | smart-sso through 2.1.1 contains an open redirect vulnerability in the /login handler that allows unauthenticated attac… |
| 2026-10-16 18:17:42 | [CVE-2026-111623](https://nvd.nist.gov/vuln/detail/CVE-2026-111623) | Medium | 6.3 | Xiaozhi-esp32-server-java through 6.1.0 contains an authentication bypass vulnerability that allows unauthenticated att… |
| 2026-10-16 18:17:42 | [CVE-2026-111624](https://nvd.nist.gov/vuln/detail/CVE-2026-111624) | Medium | 6.3 | Umbraco CMS before 17.7.1 and 18.2.1 contains a missing authorization vulnerability that allows unauthenticated clients… |
| 2026-10-16 18:17:42 | [CVE-2026-111625](https://nvd.nist.gov/vuln/detail/CVE-2026-111625) | Medium | 5.3 | 10up Distributor before 2.3.2 contains a missing authorization vulnerability in ajax_push() that allows Contributor-lev… |
| 2026-10-16 18:17:42 | [CVE-2026-111626](https://nvd.nist.gov/vuln/detail/CVE-2026-111626) | Critical | 9.3 | Webreaper Damselfly through 4.5.3 contains an authentication bypass vulnerability that allows unauthenticated attackers… |
| 2026-10-16 18:17:42 | [CVE-2026-111627](https://nvd.nist.gov/vuln/detail/CVE-2026-111627) | High | 8.6 | HestiaCP before 1.10.5 contains an authorization bypass vulnerability that allows non-ROOT_USER administrators to perfo… |
| 2026-10-16 18:17:42 | [CVE-2026-111628](https://nvd.nist.gov/vuln/detail/CVE-2026-111628) | Low | 2.3 | 10up Distributor before 2.3.2 contains a PHP object injection vulnerability that allows Contributor-level users to inst… |
| 2026-10-16 18:17:43 | [CVE-2026-111629](https://nvd.nist.gov/vuln/detail/CVE-2026-111629) | Medium | 5.3 | IoTSharp through 3.6.1 contains an insecure direct object reference vulnerability that allows any authenticated user to… |
| 2026-10-16 18:17:43 | [CVE-2026-111630](https://nvd.nist.gov/vuln/detail/CVE-2026-111630) | Medium | 5.3 | abp-next-admin 10.2.0 through 10.6.0 contains an insecure direct object reference vulnerability in the LINGYUN.Abp.AIMa… |
| 2026-10-16 18:17:43 | [CVE-2026-111631](https://nvd.nist.gov/vuln/detail/CVE-2026-111631) | Medium | 5.3 | Distributor before 2.3.2 contains a missing authorization vulnerability that allows Contributor-level users to invoke e… |
| 2026-10-16 18:17:43 | [CVE-2026-111632](https://nvd.nist.gov/vuln/detail/CVE-2026-111632) | Medium | 5.3 | Aureus ERP through 1.6.0 contains an authorization bypass vulnerability that allows authenticated API users to create o… |
| 2026-10-16 18:17:43 | [CVE-2026-111633](https://nvd.nist.gov/vuln/detail/CVE-2026-111633) | High | 8.8 | ZKEACMS through 4.4 contains an authentication bypass vulnerability that allows unauthenticated attackers to forge REST… |
| 2026-10-16 18:17:43 | [CVE-2026-111634](https://nvd.nist.gov/vuln/detail/CVE-2026-111634) | High | 8.6 | Helical Insight through 7.0.0 contains an sql injection vulnerability that allows authenticated viewers to inject SQL t… |
| 2026-10-16 18:17:43 | [CVE-2026-111635](https://nvd.nist.gov/vuln/detail/CVE-2026-111635) | Medium | 5.3 | Helical Insight through 7.0.0 contains a path traversal vulnerability that allows authenticated viewers to read files o… |
| 2026-10-16 18:17:44 | [CVE-2026-111636](https://nvd.nist.gov/vuln/detail/CVE-2026-111636) | Critical | 9.2 | OpenBMB StaffDeck through 0.5.6 contains an authentication bypass vulnerability that allows unauthenticated attackers t… |
| 2026-10-16 18:17:44 | [CVE-2026-111637](https://nvd.nist.gov/vuln/detail/CVE-2026-111637) | Medium | 6.9 | NexoPOS through 6.2.4 contains a missing authentication vulnerability that allows unauthenticated attackers to read acc… |
| 2026-10-16 18:17:44 | [CVE-2026-111638](https://nvd.nist.gov/vuln/detail/CVE-2026-111638) | High | 8.3 | sshportal through 1.19.5 contains a missing authorization vulnerability in the management shell 'key show' command that… |
| 2026-10-16 18:17:44 | [CVE-2026-111639](https://nvd.nist.gov/vuln/detail/CVE-2026-111639) | High | 8.6 | bbs-go through 4.4.6 contains an authentication bypass vulnerability in the /api/login/google_one_tap endpoint that all… |
| 2026-10-16 18:17:44 | [CVE-2026-111640](https://nvd.nist.gov/vuln/detail/CVE-2026-111640) | Medium | 5.3 | DooTask through 1.9.66 contains a missing authorization vulnerability in WebSocketDialog::checkDialog() that skips the… |
| 2026-10-16 18:17:44 | [CVE-2026-111641](https://nvd.nist.gov/vuln/detail/CVE-2026-111641) | Critical | 9.3 | FastapiAdmin through 3.0 contains an authentication bypass vulnerability that allows unauthenticated attackers to obtai… |
| 2026-10-16 18:17:44 | [CVE-2026-111642](https://nvd.nist.gov/vuln/detail/CVE-2026-111642) | High | 8.7 | FastapiAdmin through 3.0 contains a hard-coded JWT signing secret in backend/app/config/setting.py that allows low-priv… |
| 2026-10-16 18:17:45 | [CVE-2026-111643](https://nvd.nist.gov/vuln/detail/CVE-2026-111643) | Critical | 9.3 | Misaka Danmu Server through 2.8.9 contains an authentication bypass vulnerability that allows unauthenticated attackers… |
| 2026-10-16 18:17:45 | [CVE-2026-111644](https://nvd.nist.gov/vuln/detail/CVE-2026-111644) | Medium | 6.9 | Misaka Danmu Server through 2.8.9 contains a missing authentication vulnerability that allows unauthenticated attackers… |
| 2026-10-16 18:17:45 | [CVE-2026-111645](https://nvd.nist.gov/vuln/detail/CVE-2026-111645) | Medium | 5.3 | MrDoc through 1.1.1 contains a missing object-level authorization vulnerability in the ImportLocalDoc API that allows a… |
| 2026-10-16 18:17:45 | [CVE-2026-111646](https://nvd.nist.gov/vuln/detail/CVE-2026-111646) | High | 8.2 | SurveyKing before 1.13.0 contains a missing authorization vulnerability that allows unauthenticated attackers to downlo… |
| 2026-10-16 18:17:45 | [CVE-2026-111647](https://nvd.nist.gov/vuln/detail/CVE-2026-111647) | Medium | 5.3 | PickMall lilishop through 5.0.0 contains an insecure direct object reference vulnerability that allows authenticated bu… |
| 2026-10-16 18:17:45 | [CVE-2026-111648](https://nvd.nist.gov/vuln/detail/CVE-2026-111648) | Medium | 5.1 | BuildAdmin through 2.3.9 contains an insecure direct object reference vulnerability that allows authenticated backend a… |
| 2026-10-16 18:17:45 | [CVE-2026-111649](https://nvd.nist.gov/vuln/detail/CVE-2026-111649) | High | 7.1 | Rocboss paopao-ce through 0.6.0-alpha.3 contains an insecure direct object reference vulnerability in DownloadAttachmen… |
| 2026-10-16 18:17:46 | [CVE-2026-111650](https://nvd.nist.gov/vuln/detail/CVE-2026-111650) | High | 8.8 | ChronoFrame through 1.0.0 contains a missing authentication vulnerability in the server/api/wizard/ handlers that allow… |
| 2026-10-16 18:17:46 | [CVE-2026-111651](https://nvd.nist.gov/vuln/detail/CVE-2026-111651) | High | 7.1 | Risesoft Digital-Infrastructure through 9.6.11 contains a missing authorization vulnerability in the log module Downloa… |
| 2026-10-16 18:17:46 | [CVE-2026-111652](https://nvd.nist.gov/vuln/detail/CVE-2026-111652) | Medium | 6.9 | Engineercms through 2.0.5 contains a missing authorization vulnerability in AttachController.Attachment that allows una… |
| 2026-10-16 18:17:46 | [CVE-2026-111653](https://nvd.nist.gov/vuln/detail/CVE-2026-111653) | Medium | 6.9 | 53AIHub through 0.5.3 contains a missing authentication vulnerability that allows unauthenticated attackers to overwrit… |
| 2026-10-16 18:17:46 | [CVE-2026-111654](https://nvd.nist.gov/vuln/detail/CVE-2026-111654) | Medium | 5.3 | FastBee through 2.1.0 contains an insecure direct object reference vulnerability that allows authenticated low-privileg… |
| 2026-10-16 18:17:46 | [CVE-2026-111655](https://nvd.nist.gov/vuln/detail/CVE-2026-111655) | Medium | 5.1 | ThinkAdmin think-plugs-admin through 1.0.81 contains an insecure direct object reference vulnerability that allows non-… |
| 2026-10-16 18:17:46 | [CVE-2026-111656](https://nvd.nist.gov/vuln/detail/CVE-2026-111656) | Medium | 5.3 | ChatWiki through 2.9.6 contains an insecure direct object reference vulnerability that allows authenticated users to ac… |
| 2026-10-16 18:17:47 | [CVE-2026-111657](https://nvd.nist.gov/vuln/detail/CVE-2026-111657) | Medium | 5.3 | BeikeShop through 2.0.0.31 contains an insecure direct object reference vulnerability in the markAsShipped handler of R… |
| 2026-10-16 18:17:47 | [CVE-2026-111658](https://nvd.nist.gov/vuln/detail/CVE-2026-111658) | Medium | 5.1 | SiteServer SSCMS through 7.4.0 contains an authorization bypass vulnerability in ChannelsController that allows site-sc… |
| 2026-10-16 18:17:47 | [CVE-2026-111659](https://nvd.nist.gov/vuln/detail/CVE-2026-111659) | Medium | 6.9 | Waynboot-mall through 2.0.0 contains a missing authentication vulnerability that allows unauthenticated attackers to fo… |
| 2026-10-16 18:17:47 | [CVE-2026-111660](https://nvd.nist.gov/vuln/detail/CVE-2026-111660) | Medium | 6.9 | waynboot-mall through 2.0.0 contains a missing authentication vulnerability that allows unauthenticated attackers to ca… |
| 2026-10-16 18:17:47 | [CVE-2026-111661](https://nvd.nist.gov/vuln/detail/CVE-2026-111661) | Medium | 6.9 | waynboot-mall through 2.0.0 contains a missing authentication vulnerability that allows unauthenticated attackers to se… |
| 2026-10-16 18:17:47 | [CVE-2026-111662](https://nvd.nist.gov/vuln/detail/CVE-2026-111662) | Medium | 6.9 | Chaskiq through 2.0.3 contains a server-side request forgery vulnerability that allows unauthenticated attackers to mak… |
| 2026-10-16 18:17:48 | [CVE-2026-111663](https://nvd.nist.gov/vuln/detail/CVE-2026-111663) | Critical | 9.2 | Chaskiq through 2.0.3 contains a server-side request forgery vulnerability that allows unauthenticated attackers to fet… |
| 2026-10-16 18:17:48 | [CVE-2026-111664](https://nvd.nist.gov/vuln/detail/CVE-2026-111664) | Medium | 4.8 | Safing Portmaster before 2.2.5 contains a missing authorization vulnerability that allows unprivileged local processes… |
| 2026-10-16 18:17:48 | [CVE-2026-111665](https://nvd.nist.gov/vuln/detail/CVE-2026-111665) | Medium | 5.3 | Piranha CMS through 12.2 contains a missing authorization vulnerability in the Piranha.Manager LanguageApiController th… |
| 2026-10-16 18:17:48 | [CVE-2026-111666](https://nvd.nist.gov/vuln/detail/CVE-2026-111666) | Medium | 5.3 | Steedos Platform through 3.0.15-beta.51 contains an authorization bypass vulnerability that allows authenticated users… |
| 2026-10-16 18:17:48 | [CVE-2026-111667](https://nvd.nist.gov/vuln/detail/CVE-2026-111667) | Medium | 5.3 | REBUILD through 4.5.0 contains a missing authorization vulnerability in TaskCommentController.commentList that allows a… |
| 2026-10-16 18:17:48 | [CVE-2026-111668](https://nvd.nist.gov/vuln/detail/CVE-2026-111668) | Medium | 5.3 | AIHelms through 0.1.25 contains a missing authorization vulnerability in apps/api/v1/efficiency.py that allows authenti… |
| 2026-10-16 18:17:49 | [CVE-2026-111669](https://nvd.nist.gov/vuln/detail/CVE-2026-111669) | High | 7.1 | ZR.Admin.NET through 3.8.2 contains an sql injection vulnerability that allows authenticated attackers to manipulate th… |
| 2026-10-16 18:17:49 | [CVE-2026-111670](https://nvd.nist.gov/vuln/detail/CVE-2026-111670) | Medium | 5.3 | ClickVisual through 1.1.2 contains a missing authorization vulnerability in the /api/v2/reports handlers that allows au… |
| 2026-10-16 18:17:49 | [CVE-2026-111671](https://nvd.nist.gov/vuln/detail/CVE-2026-111671) | High | 7.1 | Cube-studio through 2026.09.01 contains an insecure direct object reference vulnerability that allows authenticated use… |
| 2026-10-16 18:17:49 | [CVE-2026-111672](https://nvd.nist.gov/vuln/detail/CVE-2026-111672) | Medium | 5.3 | Cube-studio through 2026.09.01 contains a missing authorization vulnerability in myapp/views/view_pipeline.py that allo… |
| 2026-10-16 18:17:49 | [CVE-2026-111673](https://nvd.nist.gov/vuln/detail/CVE-2026-111673) | Critical | 9.3 | IceCMS through 4.1.5 contains a missing authentication vulnerability that allows unauthenticated attackers to modify, d… |
| 2026-10-16 18:17:50 | [CVE-2026-111674](https://nvd.nist.gov/vuln/detail/CVE-2026-111674) | Medium | 5.3 | Tbed through 20240319 contains a missing authorization vulnerability that allows any authenticated user to rename other… |
| 2026-10-16 18:17:50 | [CVE-2026-111675](https://nvd.nist.gov/vuln/detail/CVE-2026-111675) | Critical | 9.1 | Course-tencent-cloud through 2.0.1 contains an improper restriction of authentication attempts vulnerability that allow… |
| 2026-10-16 18:17:50 | [CVE-2026-111676](https://nvd.nist.gov/vuln/detail/CVE-2026-111676) | Medium | 5.3 | Faveo Helpdesk through 2.0.3 contains a broken access control vulnerability that allows authenticated agents to read ti… |
| 2026-10-16 18:17:50 | [CVE-2026-111677](https://nvd.nist.gov/vuln/detail/CVE-2026-111677) | Medium | 6.8 | Antiword through 0.37 contains a heap out-of-bounds read vulnerability in vGet8LstInfo in prop8.c caused by an inverted… |
| 2026-10-16 18:17:50 | [CVE-2026-111678](https://nvd.nist.gov/vuln/detail/CVE-2026-111678) | Medium | 4.8 | Antiword through 0.37 contains a stack out-of-bounds read vulnerability in vGet8PapInfo and vGet8ChrInfo in prop8.c bec… |
| 2026-10-16 18:17:50 | [CVE-2026-111679](https://nvd.nist.gov/vuln/detail/CVE-2026-111679) | Medium | 5.3 | Ekko Studio through 0.7.36 contains a missing authorization vulnerability that allows any authenticated non-super_admin… |
| 2026-10-16 18:17:50 | [CVE-2026-111680](https://nvd.nist.gov/vuln/detail/CVE-2026-111680) | High | 7.2 | APIPark through 1.9.7-beta contains an authorization bypass vulnerability that allows authenticated team managers to ac… |
| 2026-10-16 18:17:51 | [CVE-2026-111681](https://nvd.nist.gov/vuln/detail/CVE-2026-111681) | High | 8.7 | EFAK through 5.1.0 contains a missing authorization vulnerability that allows authenticated low-privilege users to mana… |
| 2026-10-16 18:17:51 | [CVE-2026-111682](https://nvd.nist.gov/vuln/detail/CVE-2026-111682) | High | 7.1 | EFAK 5.0.0 through 5.1.0 contains a missing authorization vulnerability that allows authenticated low-privilege users t… |
| 2026-10-16 18:17:51 | [CVE-2026-111683](https://nvd.nist.gov/vuln/detail/CVE-2026-111683) | Medium | 5.3 | Allegro Ralph through 20260902.1 contains a missing authorization vulnerability that allows authenticated staff users t… |
| 2026-10-16 18:17:51 | [CVE-2026-111684](https://nvd.nist.gov/vuln/detail/CVE-2026-111684) | High | 7.2 | Magistrala through 1.0.0 contains an authorization bypass vulnerability that allows authenticated workspace members to… |
| 2026-10-16 18:17:51 | [CVE-2026-111685](https://nvd.nist.gov/vuln/detail/CVE-2026-111685) | High | 8.7 | IceCMS through 4.1.5 contains an unauthenticated sql injection vulnerability that allows remote attackers to inject SQL… |
| 2026-10-16 18:17:51 | [CVE-2026-111686](https://nvd.nist.gov/vuln/detail/CVE-2026-111686) | High | 8.7 | IceCMS through 4.1.5 contains an unauthenticated sql injection vulnerability that allows remote attackers to inject SQL… |
| 2026-10-16 18:17:51 | [CVE-2026-111687](https://nvd.nist.gov/vuln/detail/CVE-2026-111687) | Critical | 9.3 | WeRSS (we-mp-rss) through 1.5.3 contains a remote code execution vulnerability that allows unauthenticated attackers to… |
| 2026-10-16 18:17:52 | [CVE-2026-111688](https://nvd.nist.gov/vuln/detail/CVE-2026-111688) | Medium | 5.3 | Exrick XBoot through 3.3.4 contains an authorization bypass vulnerability that allows authenticated users to evade role… |
| 2026-10-16 18:17:52 | [CVE-2026-111689](https://nvd.nist.gov/vuln/detail/CVE-2026-111689) | Medium | 5.3 | Exrick XBoot through 3.3.4 contains an authorization bypass vulnerability that allows authenticated users to read user… |
| 2026-10-16 18:17:52 | [CVE-2026-111690](https://nvd.nist.gov/vuln/detail/CVE-2026-111690) | Critical | 9.3 | Simple Admin Core through 1.8.7 contains an authentication bypass vulnerability that allows unauthenticated attackers t… |
| 2026-10-16 18:17:52 | [CVE-2026-111691](https://nvd.nist.gov/vuln/detail/CVE-2026-111691) | Critical | 9.1 | WIMOOR through commit ec86736 contains an authentication bypass vulnerability that allows attackers to impersonate any… |
| 2026-10-16 18:17:52 | [CVE-2026-111692](https://nvd.nist.gov/vuln/detail/CVE-2026-111692) | Critical | 9.3 | DataBuff ai-apm-web through 0.1.10 contains an authentication bypass vulnerability that allows unauthenticated attacker… |
| 2026-10-16 18:17:52 | [CVE-2026-111693](https://nvd.nist.gov/vuln/detail/CVE-2026-111693) | Critical | 9.3 | DataBuff ai-apm-web through 0.1.10 contains a hard-coded default credentials vulnerability that allows unauthenticated… |
| 2026-10-16 18:17:52 | [CVE-2026-111694](https://nvd.nist.gov/vuln/detail/CVE-2026-111694) | Medium | 6.9 | qKnow through 2.4.3 contains a missing authentication vulnerability that allows unauthenticated remote attackers to acc… |
| 2026-10-16 18:17:53 | [CVE-2026-111695](https://nvd.nist.gov/vuln/detail/CVE-2026-111695) | High | 7.1 | Shaiwz data-platform-open through commit efeacd3 contains an insecure direct object reference vulnerability that allows… |
| 2026-10-16 18:17:53 | [CVE-2026-111696](https://nvd.nist.gov/vuln/detail/CVE-2026-111696) | High | 7.1 | data-platform-open through commit efeacd3 uses a hardcoded, publicly known default AES key in AesPasswordEncAndDecServi… |
| 2026-10-16 18:17:53 | [CVE-2026-111697](https://nvd.nist.gov/vuln/detail/CVE-2026-111697) | High | 7.1 | HUIZHI ChargeOS cloud through 3.0.9 contains an insecure direct object reference vulnerability in the hcp-mp MeControll… |
| 2026-10-16 18:17:53 | [CVE-2026-111698](https://nvd.nist.gov/vuln/detail/CVE-2026-111698) | High | 7.1 | HUIZHI ChargeOS cloud through 3.0.9 contains a missing authorization vulnerability in the hcp-mp PayController.xcxRecha… |
| 2026-10-16 18:17:53 | [CVE-2026-111699](https://nvd.nist.gov/vuln/detail/CVE-2026-111699) | Medium | 6.3 | Niefy wx-api through 0.8.2 contains an authentication bypass vulnerability that allows unauthenticated attackers to imp… |
| 2026-10-16 18:17:53 | [CVE-2026-111700](https://nvd.nist.gov/vuln/detail/CVE-2026-111700) | High | 7.1 | WebVella ERP through 1.8.8 contains an sql injection vulnerability that allows any authenticated user to inject SQL thr… |
| 2026-10-16 18:17:53 | [CVE-2026-111701](https://nvd.nist.gov/vuln/detail/CVE-2026-111701) | High | 8.3 | OtterMind Nubase through 0.1.4 contains a missing authentication vulnerability that allows unauthenticated attackers to… |
| 2026-10-16 18:17:54 | [CVE-2026-111702](https://nvd.nist.gov/vuln/detail/CVE-2026-111702) | High | 8.7 | ChatOllama through commit 96c3ce5 contains an insecure direct object reference vulnerability that allows remote attacke… |
| 2026-10-16 18:17:54 | [CVE-2026-111703](https://nvd.nist.gov/vuln/detail/CVE-2026-111703) | Medium | 5.3 | yshop-crm through 2.1.3 contains an insecure direct object reference vulnerability that allows authenticated sales user… |
| 2026-10-16 18:17:54 | [CVE-2026-111704](https://nvd.nist.gov/vuln/detail/CVE-2026-111704) | Critical | 9.3 | LangChat through commit 2a6285a contains a missing authentication vulnerability that allows unauthenticated remote atta… |
| 2026-10-16 18:17:54 | [CVE-2026-111705](https://nvd.nist.gov/vuln/detail/CVE-2026-111705) | Medium | 5.3 | Fuint through commit 57ec018 contains an insecure direct object reference vulnerability that allows authenticated membe… |
| 2026-10-16 18:17:54 | [CVE-2026-111706](https://nvd.nist.gov/vuln/detail/CVE-2026-111706) | High | 8.7 | 99AI through 4.3.0 contains a missing authentication vulnerability in the POST /api/chatLog/exportExcel route that allo… |
| 2026-10-16 18:17:54 | [CVE-2026-111707](https://nvd.nist.gov/vuln/detail/CVE-2026-111707) | Medium | 6.9 | 99AI through 4.3.0 contains an insecure direct object reference vulnerability that allows unauthenticated attackers to… |
| 2026-10-16 18:17:54 | [CVE-2026-111708](https://nvd.nist.gov/vuln/detail/CVE-2026-111708) | Critical | 9.3 | WhaTicket Community through commit cf04795 contains an authentication bypass vulnerability that allows unauthenticated… |
| 2026-10-16 18:17:55 | [CVE-2026-111709](https://nvd.nist.gov/vuln/detail/CVE-2026-111709) | Medium | 5.3 | WhaTicket Community through commit cf04795 contains an insecure direct object reference vulnerability that allows authe… |
| 2026-10-16 18:17:55 | [CVE-2026-111710](https://nvd.nist.gov/vuln/detail/CVE-2026-111710) | High | 8.7 | Netcore NR256CN through 1.5.140116 contains a NULL pointer dereference vulnerability in the Boa web server's user_auth(… |
| 2026-10-16 18:17:55 | [CVE-2026-111711](https://nvd.nist.gov/vuln/detail/CVE-2026-111711) | Critical | 9.3 | Netcore NR256CN through 1.5.140116 contains a pre-authentication stack overflow vulnerability in the Boa web server's u… |
| 2026-10-16 18:17:55 | [CVE-2026-111712](https://nvd.nist.gov/vuln/detail/CVE-2026-111712) | Medium | 6.9 | Netcore NR256CN through 1.5.140116 contains an authentication bypass vulnerability that allows unauthenticated attacker… |
| 2026-10-16 18:17:55 | [CVE-2026-111713](https://nvd.nist.gov/vuln/detail/CVE-2026-111713) | Medium | 5.1 | tarteaucitron.js before 1.37.0 contains a cross-site scripting vulnerability because getElemAttr resolves 'data-' prefi… |
| 2026-10-16 18:17:55 | [CVE-2026-111714](https://nvd.nist.gov/vuln/detail/CVE-2026-111714) | Low | 2.3 | tarteaucitron.js before 1.37.0 contains a regular expression denial of service vulnerability that allows attackers to b… |
| 2026-10-16 18:17:55 | [CVE-2026-111715](https://nvd.nist.gov/vuln/detail/CVE-2026-111715) | Medium | 5.3 | Arkon through 0.9.2 contains a missing authorization vulnerability in GET /api/wiki/graph that lets authenticated emplo… |
| 2026-10-16 18:17:55 | [CVE-2026-111716](https://nvd.nist.gov/vuln/detail/CVE-2026-111716) | Medium | 5.3 | Arkon through 0.9.2 contains a broken access control vulnerability that allows authenticated employees to read and modi… |
| 2026-10-16 18:17:56 | [CVE-2026-111717](https://nvd.nist.gov/vuln/detail/CVE-2026-111717) | Medium | 5.3 | Arkon through 0.9.2 contains a missing authorization vulnerability in list_skill_versions that allows authenticated emp… |
| 2026-10-16 18:17:56 | [CVE-2026-111718](https://nvd.nist.gov/vuln/detail/CVE-2026-111718) | High | 7.1 | AipexBase through commit 690adb9 contains a sql injection vulnerability that allows attackers to inject SQL through the… |
| 2026-10-16 18:17:56 | [CVE-2026-111719](https://nvd.nist.gov/vuln/detail/CVE-2026-111719) | High | 8.2 | Roncoo-pay through commit 9428382 contains a missing authorization vulnerability in F2FPayController.orderQuery that al… |
| 2026-10-16 18:17:56 | [CVE-2026-111720](https://nvd.nist.gov/vuln/detail/CVE-2026-111720) | Medium | 6.9 | fish-island-backend through commit 7c61b78 contains an unauthenticated server-side request forgery vulnerability that a… |
| 2026-10-16 18:17:56 | [CVE-2026-111721](https://nvd.nist.gov/vuln/detail/CVE-2026-111721) | Medium | 5.3 | Open WES through 1.0.0 contains an authorization bypass vulnerability that allows authenticated users to modify other w… |
| 2026-10-16 18:17:56 | [CVE-2026-111722](https://nvd.nist.gov/vuln/detail/CVE-2026-111722) | High | 8.6 | LingGuo-Drama through commit 8a6924a contains an insecure direct object reference vulnerability that allows registered… |
| 2026-10-16 18:17:56 | [CVE-2026-111723](https://nvd.nist.gov/vuln/detail/CVE-2026-111723) | High | 8.7 | LingGuo-Drama through commit 8a6924a contains a missing authorization vulnerability that allows any registered user to… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
