# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-14 15:19 UTC

New CVEs published between 2026-10-14 14:19 UTC and 2026-10-14 15:19 UTC.

[Full CSV](data/new-cves-2026-10-14T15-19-44-421968Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-10-14 15:16:58 | [CVE-2016-20099](https://nvd.nist.gov/vuln/detail/CVE-2016-20099) | Medium | 6.8 | L-SMASH through 2.14.5 contains an infinite loop vulnerability in vc1_importer_probe() in importer/vc1_imp.c that allow… |
| 2026-10-14 15:16:59 | [CVE-2017-20286](https://nvd.nist.gov/vuln/detail/CVE-2017-20286) | High | 8.5 | DevIL through 1.8.0 contains a heap-based buffer overflow in iGetPalette() in il_gif.cpp that allows attackers to write… |
| 2026-10-14 15:16:59 | [CVE-2020-37281](https://nvd.nist.gov/vuln/detail/CVE-2020-37281) | Critical | 9.2 | Gravitee API Management through 4.12.22 contains an authentication bypass vulnerability that allows unauthenticated rem… |
| 2026-10-14 15:16:59 | [CVE-2020-37282](https://nvd.nist.gov/vuln/detail/CVE-2020-37282) | Critical | 9.3 | office-converter through 1.0.2 contains an OS command injection vulnerability that allows attackers to execute commands… |
| 2026-10-14 15:17:00 | [CVE-2024-58392](https://nvd.nist.gov/vuln/detail/CVE-2024-58392) | Medium | 4.8 | PhysicsFS through 3.2.0 contains an out-of-bounds read vulnerability in __PHYSFS_utf8codepoint() that allows attackers… |
| 2026-10-14 15:17:00 | [CVE-2025-71433](https://nvd.nist.gov/vuln/detail/CVE-2025-71433) | High | 7.7 | Kaneo before 2.1.6 contains a missing authorization vulnerability that allows authenticated users to access other works… |
| 2026-10-14 15:17:01 | [CVE-2026-101019](https://nvd.nist.gov/vuln/detail/CVE-2026-101019) | High | 8.3 | Description NGINX JavaScript (njs) has a vulnerability where the njs XML module exposes entity-backed XML attributes in… |
| 2026-10-14 15:17:01 | [CVE-2026-101025](https://nvd.nist.gov/vuln/detail/CVE-2026-101025) | Medium | 6.9 | Description NGINX JavaScript (njs) has a vulnerability where the built-in njs engine leaks a libxml2 parser context whe… |
| 2026-10-14 15:17:03 | [CVE-2026-101895](https://nvd.nist.gov/vuln/detail/CVE-2026-101895) | High | 8.7 | Angular is a development platform for building mobile and desktop web applications using TypeScript/JavaScript and othe… |
| 2026-10-14 15:17:05 | [CVE-2026-104939](https://nvd.nist.gov/vuln/detail/CVE-2026-104939) | High | 8.7 | Description NGINX Ingress Controller has a vulnerability when implementing an externalAuth policy for ingress. NGINX In… |
| 2026-10-14 15:17:06 | [CVE-2026-107381](https://nvd.nist.gov/vuln/detail/CVE-2026-107381) | Medium | 6.5 | svg-sanitizer is a PHP SVG/XML sanitizer. Prior to 1.0.0, Resolver::processReferences() in src/ElementReference/Resolve… |
| 2026-10-14 15:17:07 | [CVE-2026-110257](https://nvd.nist.gov/vuln/detail/CVE-2026-110257) | Medium | 6.8 | OW2 ASM 5.0 before 9.11 contains an excessive memory allocation vulnerability in ClassReader.readBootstrapMethodsAttrib… |
| 2026-10-14 15:17:07 | [CVE-2026-110258](https://nvd.nist.gov/vuln/detail/CVE-2026-110258) | Medium | 6.8 | OW2 ASM 3.0 before 9.11 contains an excessive memory allocation vulnerability in Label.addSubroutineRetSuccessors() tha… |
| 2026-10-14 15:17:07 | [CVE-2026-110259](https://nvd.nist.gov/vuln/detail/CVE-2026-110259) | Medium | 6.8 | OW2 ASM 3.0 before 9.11 contains an uncontrolled recursion vulnerability in ClassWriter.replaceAsmInstructions() that a… |
| 2026-10-14 15:17:07 | [CVE-2026-110260](https://nvd.nist.gov/vuln/detail/CVE-2026-110260) | Medium | 6.8 | OW2 ASM 3.0 before 9.11 contains a quadratic memory allocation vulnerability in MethodWriter.computeMaxStackAndLocal()… |
| 2026-10-14 15:17:07 | [CVE-2026-110261](https://nvd.nist.gov/vuln/detail/CVE-2026-110261) | Medium | 6.8 | OW2 ASM 3.0 before 9.11 contains a denial of service vulnerability that allows attackers to exhaust CPU by supplying cr… |
| 2026-10-14 15:17:08 | [CVE-2026-110262](https://nvd.nist.gov/vuln/detail/CVE-2026-110262) | Medium | 4.8 | OW2 ASM 3.1 before 9.11 contains an excessive memory allocation vulnerability in the asm-commons AdviceAdapter that all… |
| 2026-10-14 15:17:08 | [CVE-2026-110263](https://nvd.nist.gov/vuln/detail/CVE-2026-110263) | Medium | 6.8 | OW2 ASM 3.0 before 9.11 contains an uncontrolled recursion vulnerability in SignatureReader.parseType() that allows att… |
| 2026-10-14 15:17:08 | [CVE-2026-110270](https://nvd.nist.gov/vuln/detail/CVE-2026-110270) | Medium | 6.8 | OW2 ASM 3.0 before 9.11 contains an uncontrolled memory allocation vulnerability in the asm-commons JSRInlinerAdapter t… |
| 2026-10-14 15:17:09 | [CVE-2026-110591](https://nvd.nist.gov/vuln/detail/CVE-2026-110591) | Medium | 6.8 | OW2 ASM 1.4.3 before 9.11 contains an excessive resource consumption vulnerability in Analyzer.analyze() that allows at… |
| 2026-10-14 15:17:10 | [CVE-2026-110592](https://nvd.nist.gov/vuln/detail/CVE-2026-110592) | Medium | 5.1 | BottleCRM 0.30 through 1.14.5 contains an HTML injection vulnerability in render_invoice_template() that allows authent… |
| 2026-10-14 15:17:10 | [CVE-2026-110593](https://nvd.nist.gov/vuln/detail/CVE-2026-110593) | Medium | 5.3 | BottleCRM through 1.14.5 contains a server-side template injection vulnerability in the send_email Celery task, which c… |
| 2026-10-14 15:17:10 | [CVE-2026-110594](https://nvd.nist.gov/vuln/detail/CVE-2026-110594) | Medium | 6.9 | BottleCRM 0.43 through 1.14.5 contains a regular expression denial of service vulnerability that allows authenticated o… |
| 2026-10-14 15:17:10 | [CVE-2026-110595](https://nvd.nist.gov/vuln/detail/CVE-2026-110595) | Medium | 5.3 | BottleCRM 0.45 through 1.14.5 contains an uncontrolled memory allocation vulnerability in _read_upload() that reads ent… |
| 2026-10-14 15:17:10 | [CVE-2026-110596](https://nvd.nist.gov/vuln/detail/CVE-2026-110596) | Medium | 6.8 | quirc through 1.2 contains an excessive-iteration vulnerability in find_alignment_pattern() in lib/identify.c that allo… |
| 2026-10-14 15:17:10 | [CVE-2026-110597](https://nvd.nist.gov/vuln/detail/CVE-2026-110597) | Medium | 6.9 | Tinyexr through 3.2.0 contains a heap out-of-bounds read vulnerability in ParseEXRMultipartHeaderFromMemory() that allo… |
| 2026-10-14 15:17:11 | [CVE-2026-110598](https://nvd.nist.gov/vuln/detail/CVE-2026-110598) | Medium | 6.9 | Libyal libpff through 20260926 contains an integer underflow in libpff_record_entry_get_multi_value() that allows attac… |
| 2026-10-14 15:17:11 | [CVE-2026-110599](https://nvd.nist.gov/vuln/detail/CVE-2026-110599) | Medium | 6.9 | L-SMASH through 2.14.5 contains a double free vulnerability in hevc_setup_first_summary() and h264_setup_first_summary(… |
| 2026-10-14 15:17:11 | [CVE-2026-110600](https://nvd.nist.gov/vuln/detail/CVE-2026-110600) | Medium | 6.8 | xlsxio through 0.2.37 contains a NULL pointer dereference vulnerability in main_sheet_get_sheetfile_expat_callback_elem… |
| 2026-10-14 15:17:11 | [CVE-2026-110601](https://nvd.nist.gov/vuln/detail/CVE-2026-110601) | Medium | 5.8 | libsixel before 1.8.7-r1 and 1.9.0 through 1.10.5 contains a heap out-of-bounds write vulnerability in gif_init_frame()… |
| 2026-10-14 15:17:11 | [CVE-2026-110602](https://nvd.nist.gov/vuln/detail/CVE-2026-110602) | Medium | 5.8 | libmspack through 0.11alpha contains an uninitialized pointer free vulnerability in kwajd_open() in mspack/kwajd.c that… |
| 2026-10-14 15:17:11 | [CVE-2026-110603](https://nvd.nist.gov/vuln/detail/CVE-2026-110603) | Medium | 5.8 | LASzip through 3.5.0 contains an invalid free vulnerability in laszip_read_header() that allows attackers to free unini… |
| 2026-10-14 15:17:11 | [CVE-2026-110604](https://nvd.nist.gov/vuln/detail/CVE-2026-110604) | Low | 2.0 | Mini-XML 4.0.0 through 4.0.6 contains an off-by-one stack out-of-bounds write in mxml_strtod() when the locale decimal… |
| 2026-10-14 15:17:12 | [CVE-2026-110605](https://nvd.nist.gov/vuln/detail/CVE-2026-110605) | Medium | 6.8 | libschrift through 0.10.2 contains a divide by zero vulnerability that allows attackers to crash applications by supply… |
| 2026-10-14 15:17:12 | [CVE-2026-110606](https://nvd.nist.gov/vuln/detail/CVE-2026-110606) | Medium | 4.8 | LibreCAD libdxfrw through LC2.2.0 (LibreCAD through 2.2.1.5) contains a stack-based out-of-bounds read vulnerability in… |
| 2026-10-14 15:17:12 | [CVE-2026-110607](https://nvd.nist.gov/vuln/detail/CVE-2026-110607) | High | 7.1 | BizSpring Shop through commit cf22d39daaf1 contains a payment verification bypass vulnerability that allows authenticat… |
| 2026-10-14 15:17:12 | [CVE-2026-110608](https://nvd.nist.gov/vuln/detail/CVE-2026-110608) | Medium | 5.3 | BizSpring Shop through commit cf22d39daaf1 contains an insecure direct object reference vulnerability in the OrderContr… |
| 2026-10-14 15:17:12 | [CVE-2026-110609](https://nvd.nist.gov/vuln/detail/CVE-2026-110609) | High | 7.1 | Dromara Skyeye through commit 65d3ddcede70 contains an sql injection vulnerability that allows authenticated low-privil… |
| 2026-10-14 15:17:12 | [CVE-2026-110610](https://nvd.nist.gov/vuln/detail/CVE-2026-110610) | Medium | 5.3 | ruoyi-vue-pro through 2026.09 contains a server-side request forgery vulnerability in the yudao-module-ai image service… |
| 2026-10-14 15:17:13 | [CVE-2026-110611](https://nvd.nist.gov/vuln/detail/CVE-2026-110611) | Medium | 6.0 | REBUILD through 4.5.0 contains an authorization bypass vulnerability in AiBot2Controller /aibot2 endpoints that act on… |
| 2026-10-14 15:17:13 | [CVE-2026-110612](https://nvd.nist.gov/vuln/detail/CVE-2026-110612) | Critical | 9.3 | vlife through 2.0.1 contains an authentication bypass vulnerability that allows unauthenticated attackers to forge JWTs… |
| 2026-10-14 15:17:13 | [CVE-2026-110613](https://nvd.nist.gov/vuln/detail/CVE-2026-110613) | High | 7.1 | youlai-mall through commit 9f62de8 contains a missing authorization vulnerability that allows authenticated members to… |
| 2026-10-14 15:17:13 | [CVE-2026-110614](https://nvd.nist.gov/vuln/detail/CVE-2026-110614) | High | 7.1 | Yiuman citrus through 0.15.0 contains an ORDER BY sql injection vulnerability in the citrus-support generic query frame… |
| 2026-10-14 15:17:13 | [CVE-2026-110615](https://nvd.nist.gov/vuln/detail/CVE-2026-110615) | High | 7.1 | jshERP through 3.6 contains a missing authorization vulnerability in the POST /user/batchSetStatus endpoint that allows… |
| 2026-10-14 15:17:13 | [CVE-2026-110616](https://nvd.nist.gov/vuln/detail/CVE-2026-110616) | Critical | 9.2 | NullHub through 2026.5.29 contains a missing authentication vulnerability that allows unauthenticated attackers to acce… |
| 2026-10-14 15:17:13 | [CVE-2026-110617](https://nvd.nist.gov/vuln/detail/CVE-2026-110617) | Medium | 6.3 | we-mp-rss through 1.5.3 contains a missing authorization vulnerability in the /api/v1/wx/tools/export/download endpoint… |
| 2026-10-14 15:17:14 | [CVE-2026-110618](https://nvd.nist.gov/vuln/detail/CVE-2026-110618) | High | 8.6 | SmsForwarder through 3.5.0 contains a missing authentication vulnerability in its AndServer HTTP server that allows una… |
| 2026-10-14 15:17:14 | [CVE-2026-110619](https://nvd.nist.gov/vuln/detail/CVE-2026-110619) | Medium | 6.3 | frp 0.41.0 through 0.71.1 contains a missing authentication vulnerability that allows unauthenticated remote attackers… |
| 2026-10-14 15:17:14 | [CVE-2026-110620](https://nvd.nist.gov/vuln/detail/CVE-2026-110620) | Medium | 6.1 | Formbricks before 4.9.0 contains an authorization bypass vulnerability in server actions like resetSurveyAction and upd… |
| 2026-10-14 15:17:14 | [CVE-2026-110621](https://nvd.nist.gov/vuln/detail/CVE-2026-110621) | High | 8.7 | Swetrix Cloud before 5.1.0 contains a missing authorization vulnerability in ProjectController.addProject that allows a… |
| 2026-10-14 15:17:14 | [CVE-2026-110622](https://nvd.nist.gov/vuln/detail/CVE-2026-110622) | High | 7.7 | Papermerge Core through 3.5.3 contains a missing authorization vulnerability that allows authenticated users to manipul… |
| 2026-10-14 15:17:14 | [CVE-2026-110623](https://nvd.nist.gov/vuln/detail/CVE-2026-110623) | High | 7.7 | Papermerge Core through 3.5.3 contains a missing authorization vulnerability in the shared nodes API that allows authen… |
| 2026-10-14 15:17:14 | [CVE-2026-110624](https://nvd.nist.gov/vuln/detail/CVE-2026-110624) | Low | 2.3 | Papermerge Core through 3.5.3 contains a missing authorization vulnerability that allows authenticated users to list ot… |
| 2026-10-14 15:17:15 | [CVE-2026-110625](https://nvd.nist.gov/vuln/detail/CVE-2026-110625) | Medium | 5.1 | ClipBucket v5 through 5.5.3-#206 contains a reflected cross-site scripting vulnerability in admin_area/flagged_item.php… |
| 2026-10-14 15:17:15 | [CVE-2026-110626](https://nvd.nist.gov/vuln/detail/CVE-2026-110626) | Medium | 5.1 | ClipBucket v5 through 5.5.3-#206 contains a reflected cross-site scripting vulnerability in admin_area/language_setting… |
| 2026-10-14 15:17:15 | [CVE-2026-110627](https://nvd.nist.gov/vuln/detail/CVE-2026-110627) | Low | 2.1 | ClipBucket v5 through 5.5.3-#206 contains a reflected cross-site scripting vulnerability in admin_area/index.php that a… |
| 2026-10-14 15:17:15 | [CVE-2026-110628](https://nvd.nist.gov/vuln/detail/CVE-2026-110628) | Critical | 9.2 | Kan 0.5.5 through 0.6.0 contains an unauthenticated server-side request forgery vulnerability in the /api/download/atta… |
| 2026-10-14 15:17:15 | [CVE-2026-110629](https://nvd.nist.gov/vuln/detail/CVE-2026-110629) | High | 7.1 | VentureDrake Laravel CRM before 2.4.0 contains a missing authorization vulnerability that allows authenticated users to… |
| 2026-10-14 15:17:15 | [CVE-2026-110630](https://nvd.nist.gov/vuln/detail/CVE-2026-110630) | High | 7.0 | VentureDrake Laravel CRM before 2.4.0 contains an incorrect authorization vulnerability in user management that allows… |
| 2026-10-14 15:17:15 | [CVE-2026-110631](https://nvd.nist.gov/vuln/detail/CVE-2026-110631) | Critical | 9.3 | Komodo through 2.3.3 contains an authentication bypass vulnerability in the Periphery agent that allows unauthenticated… |
| 2026-10-14 15:17:16 | [CVE-2026-110632](https://nvd.nist.gov/vuln/detail/CVE-2026-110632) | Critical | 9.2 | Report One MyReport Updater through 2.1.1 exposes an unauthenticated gRPC service on TCP port 9095 that allows remote a… |
| 2026-10-14 15:17:16 | [CVE-2026-110633](https://nvd.nist.gov/vuln/detail/CVE-2026-110633) | High | 8.5 | MyReport Updater through 2.1.1 contains a local privilege escalation vulnerability that allows low-privileged users to… |
| 2026-10-14 15:17:16 | [CVE-2026-110634](https://nvd.nist.gov/vuln/detail/CVE-2026-110634) | Critical | 9.3 | git-diff before 2.0.7 contains an OS command injection vulnerability that allows attackers to execute shell commands by… |
| 2026-10-14 15:17:16 | [CVE-2026-110635](https://nvd.nist.gov/vuln/detail/CVE-2026-110635) | Critical | 9.3 | webp-converter before 3.0.0 contains an OS command injection vulnerability in src/webpconverter.js helpers that run lib… |
| 2026-10-14 15:17:16 | [CVE-2026-110636](https://nvd.nist.gov/vuln/detail/CVE-2026-110636) | Critical | 9.3 | pypdftk through 0.5 contains an OS command injection vulnerability in fill_form(), dump_data_fields(), and pdftk_cmd_ut… |
| 2026-10-14 15:17:16 | [CVE-2026-110637](https://nvd.nist.gov/vuln/detail/CVE-2026-110637) | High | 8.5 | buildebooks before 0.2.2 contains an OS command injection vulnerability in lib/kindle.js that allows attackers to execu… |
| 2026-10-14 15:17:16 | [CVE-2026-110638](https://nvd.nist.gov/vuln/detail/CVE-2026-110638) | Critical | 9.3 | doc-recog through 1.1.6 contains an OS command injection vulnerability that allows attackers to execute commands by sup… |
| 2026-10-14 15:17:17 | [CVE-2026-110639](https://nvd.nist.gov/vuln/detail/CVE-2026-110639) | Critical | 9.3 | @mborne/extract before 0.2.1 contains an OS command injection vulnerability that allows attackers to execute commands b… |
| 2026-10-14 15:17:17 | [CVE-2026-110640](https://nvd.nist.gov/vuln/detail/CVE-2026-110640) | Critical | 9.3 | Whisper-node through 1.1.1 contains an OS command injection vulnerability that allows attackers to execute commands by… |
| 2026-10-14 15:17:17 | [CVE-2026-110641](https://nvd.nist.gov/vuln/detail/CVE-2026-110641) | High | 8.7 | @runnerty/executor-decompress through 3.1.1 contains an OS command injection vulnerability that allows attackers to exe… |
| 2026-10-14 15:17:17 | [CVE-2026-110642](https://nvd.nist.gov/vuln/detail/CVE-2026-110642) | High | 8.5 | xhtml2pdf before 0.2.19 contains an OS command injection vulnerability in pisa.startViewer() that allows attackers to e… |
| 2026-10-14 15:17:17 | [CVE-2026-110643](https://nvd.nist.gov/vuln/detail/CVE-2026-110643) | Critical | 9.3 | transcribe2texts through 1.0.6 contains an OS command injection vulnerability that allows attackers to execute commands… |
| 2026-10-14 15:17:17 | [CVE-2026-110644](https://nvd.nist.gov/vuln/detail/CVE-2026-110644) | Critical | 9.3 | nodejs-whisper through 0.3.1 contains an OS command injection vulnerability in convertToWavType() that allows attackers… |
| 2026-10-14 15:17:18 | [CVE-2026-110645](https://nvd.nist.gov/vuln/detail/CVE-2026-110645) | Critical | 9.3 | Video-stitch before 2.0.0-beta.1 contains an OS command injection vulnerability that allows attackers to execute comman… |
| 2026-10-14 15:17:18 | [CVE-2026-110646](https://nvd.nist.gov/vuln/detail/CVE-2026-110646) | Critical | 9.2 | Beganovich snappdf from 1.1.0 before 6.1.0 contains an OS command injection vulnerability on Windows that allows attack… |
| 2026-10-14 15:17:18 | [CVE-2026-110647](https://nvd.nist.gov/vuln/detail/CVE-2026-110647) | High | 8.5 | Turnpress through 0.4.2 contains an OS command injection vulnerability that allows attackers to execute shell commands… |
| 2026-10-14 15:17:18 | [CVE-2026-110648](https://nvd.nist.gov/vuln/detail/CVE-2026-110648) | High | 8.5 | @offactory/compress-fonts before 1.1.1 contains an OS command injection vulnerability that allows attackers to execute… |
| 2026-10-14 15:17:18 | [CVE-2026-110649](https://nvd.nist.gov/vuln/detail/CVE-2026-110649) | Critical | 9.3 | Stills before 25.24.2 contains an OS command injection vulnerability that allows attackers to execute shell commands by… |
| 2026-10-14 15:17:18 | [CVE-2026-110650](https://nvd.nist.gov/vuln/detail/CVE-2026-110650) | Critical | 9.3 | The thumbnail Python package through 1.5 contains an OS command injection vulnerability in generate_thumbnail() that al… |
| 2026-10-14 15:17:19 | [CVE-2026-15176](https://nvd.nist.gov/vuln/detail/CVE-2026-15176) | Critical | 9.2 | A vulnerability exists in NGINX Plus and NGINX Open Source when a location is configured that uses the alias directive… |
| 2026-10-14 15:17:19 | [CVE-2026-25946](https://nvd.nist.gov/vuln/detail/CVE-2026-25946) |  |  | When OpenID sign-in is enabled, Gitea accepts a user-supplied OpenID URL and performs discovery requests without valida… |
| 2026-10-14 15:17:20 | [CVE-2026-53612](https://nvd.nist.gov/vuln/detail/CVE-2026-53612) | High | 7.0 | util-linux is a random collection of Linux utilities. In util-linux 2.39 through 2.41.4 and 2.42 through 2.42.1, the SU… |
| 2026-10-14 15:17:20 | [CVE-2026-53613](https://nvd.nist.gov/vuln/detail/CVE-2026-53613) | High | 7.0 | util-linux is a random collection of Linux utilities. In util-linux 2.17 through 2.41.6 and 2.42 through 2.42.3, and in… |
| 2026-10-14 15:17:20 | [CVE-2026-59766](https://nvd.nist.gov/vuln/detail/CVE-2026-59766) |  |  | Gitea's starred-repository and tracked-time API endpoints do not re-check current repository permissions before returni… |
| 2026-10-14 15:17:20 | [CVE-2026-59774](https://nvd.nist.gov/vuln/detail/CVE-2026-59774) |  |  | Gitea's Org-mode markup renderer processes INCLUDE directives supplied to the repository markup endpoint without preven… |
| 2026-10-14 15:17:20 | [CVE-2026-60008](https://nvd.nist.gov/vuln/detail/CVE-2026-60008) |  |  | Gitea's Jupyter notebook renderer inserts the notebook's language_info.name metadata into a CSS class attribute while d… |
| 2026-10-14 15:17:20 | [CVE-2026-60010](https://nvd.nist.gov/vuln/detail/CVE-2026-60010) |  |  | Gitea's repository-side team-link API allows a repository administrator who is not an organization owner to attach orga… |
| 2026-10-14 15:17:21 | [CVE-2026-60018](https://nvd.nist.gov/vuln/detail/CVE-2026-60018) |  |  | Gitea's OneDev migration downloader reads the entire remote version response into memory without a size limit and uses… |
| 2026-10-14 15:17:21 | [CVE-2026-60021](https://nvd.nist.gov/vuln/detail/CVE-2026-60021) |  |  | Gitea's initial GitLab migration version probe uses an HTTP client without a timeout and does not attach the migration… |
| 2026-10-14 15:17:21 | [CVE-2026-62925](https://nvd.nist.gov/vuln/detail/CVE-2026-62925) |  |  | Gitea parses Alpine package uploads before enforcing package-size quotas and does not bound the decompressed .PKGINFO d… |
| 2026-10-14 15:17:21 | [CVE-2026-63021](https://nvd.nist.gov/vuln/detail/CVE-2026-63021) |  |  | Gitea's Swift package parser limits each manifest to 128 KiB but does not limit the number of manifests or their aggreg… |
| 2026-10-14 15:17:21 | [CVE-2026-63792](https://nvd.nist.gov/vuln/detail/CVE-2026-63792) |  |  | Gitea's collaborative-owner authorization path for reading cross-repository reusable workflows does not exclude fork pu… |
| 2026-10-14 15:17:21 | [CVE-2026-66849](https://nvd.nist.gov/vuln/detail/CVE-2026-66849) |  |  | Gitea's package registry grants authenticated users read access to packages owned by Limited-visibility users without e… |
| 2026-10-14 15:17:21 | [CVE-2026-66853](https://nvd.nist.gov/vuln/detail/CVE-2026-66853) |  |  | Gitea's user organization-list API includes Limited-visibility organizations for authenticated restricted accounts with… |
| 2026-10-14 15:17:21 | [CVE-2026-66874](https://nvd.nist.gov/vuln/detail/CVE-2026-66874) |  |  | For pull request events, Gitea reads workflow definitions from the pull request head and posts a synthetic skipped stat… |
| 2026-10-14 15:17:21 | [CVE-2026-66877](https://nvd.nist.gov/vuln/detail/CVE-2026-66877) |  |  | Gitea enforces first-time fork contributor approval by blocking jobs, but some job transition and dispatch paths do not… |
| 2026-10-14 15:17:21 | [CVE-2026-67577](https://nvd.nist.gov/vuln/detail/CVE-2026-67577) |  |  | Gitea's activity-feed and contribution-heatmap API handlers do not apply the profile visibility check for restricted ac… |
| 2026-10-14 15:17:22 | [CVE-2026-68957](https://nvd.nist.gov/vuln/detail/CVE-2026-68957) |  |  | Gitea's API and web issue-search paths do not treat restricted accounts as anonymous viewers when evaluating Limited-vi… |
| 2026-10-14 15:17:22 | [CVE-2026-68964](https://nvd.nist.gov/vuln/detail/CVE-2026-68964) |  |  | Gitea's user SSH and GPG key-list API endpoints omit the profile visibility check applied by their web equivalents. A r… |
| 2026-10-14 15:17:22 | [CVE-2026-70396](https://nvd.nist.gov/vuln/detail/CVE-2026-70396) |  |  | Gitea's organization repository-creation API requires write:organization but omits the write:repository token scope enf… |
| 2026-10-14 15:17:22 | [CVE-2026-70400](https://nvd.nist.gov/vuln/detail/CVE-2026-70400) |  |  | Gitea's repository migration API accepts a public-only token when the request specifies creation of a private repositor… |
| 2026-10-14 15:17:22 | [CVE-2026-70402](https://nvd.nist.gov/vuln/detail/CVE-2026-70402) |  |  | Gitea creates server-side Git hook directories and scripts with mode 0777 and relies on the process umask to restrict a… |
| 2026-10-14 15:17:22 | [CVE-2026-70406](https://nvd.nist.gov/vuln/detail/CVE-2026-70406) |  |  | Gitea's shared comparison helper omits the token repository-access check used when updating pull requests. A public-onl… |
| 2026-10-14 15:17:22 | [CVE-2026-70407](https://nvd.nist.gov/vuln/detail/CVE-2026-70407) |  |  | Gitea's organization-list API does not enforce the read:organization token scope. A token limited to another category,… |
| 2026-10-14 15:17:22 | [CVE-2026-71184](https://nvd.nist.gov/vuln/detail/CVE-2026-71184) |  |  | Gitea's pull request review notifier does not attach the pull request to the Actions notification, so the fork workflow… |
| 2026-10-14 15:17:22 | [CVE-2026-71301](https://nvd.nist.gov/vuln/detail/CVE-2026-71301) |  |  | Gitea's repository markup endpoint resolves same-repository pull request references without enforcing the viewer's Pull… |
| 2026-10-14 15:17:23 | [CVE-2026-73126](https://nvd.nist.gov/vuln/detail/CVE-2026-73126) |  |  | Gitea's Actions workflow status badge endpoint does not enforce repository-read scope or the public-only restriction on… |
| 2026-10-14 15:17:23 | [CVE-2026-73130](https://nvd.nist.gov/vuln/detail/CVE-2026-73130) |  |  | Gitea does not limit the length of the gitignores field accepted by repository-creation forms and the API. Repository i… |
| 2026-10-14 15:17:23 | [CVE-2026-73135](https://nvd.nist.gov/vuln/detail/CVE-2026-73135) |  |  | Gitea uses inconsistent repository visibility predicates, and the condition used by some repository-listing endpoints a… |
| 2026-10-14 15:17:23 | [CVE-2026-73273](https://nvd.nist.gov/vuln/detail/CVE-2026-73273) |  |  | Gitea's Maven upload handler reads checksum uploads entirely into memory and returns before enforcing package-size quot… |
| 2026-10-14 15:17:23 | [CVE-2026-73535](https://nvd.nist.gov/vuln/detail/CVE-2026-73535) |  |  | Gitea's OpenID connect handler accepts a user's password without enforcing enrolled TOTP or WebAuthn verification befor… |
| 2026-10-14 15:17:23 | [CVE-2026-73539](https://nvd.nist.gov/vuln/detail/CVE-2026-73539) |  |  | Gitea substitutes a URL derived from the markup Context field into external renderer command templates without escaping… |
| 2026-10-14 15:17:24 | [CVE-2026-73800](https://nvd.nist.gov/vuln/detail/CVE-2026-73800) |  |  | Gitea resolves local reusable workflow files from a fork's head commit when a trusted base-branch workflow runs for a p… |
| 2026-10-14 15:17:24 | [CVE-2026-73802](https://nvd.nist.gov/vuln/detail/CVE-2026-73802) |  |  | Gitea Runner passes workflow-controlled container options into Docker job container configuration while privileged mode… |
| 2026-10-14 15:17:24 | [CVE-2026-73804](https://nvd.nist.gov/vuln/detail/CVE-2026-73804) |  |  | Gitea allows a token with write:user scope to register an attacker-controlled SSH public key on the token owner's accou… |
| 2026-10-14 15:17:24 | [CVE-2026-73814](https://nvd.nist.gov/vuln/detail/CVE-2026-73814) |  |  | Gitea's collaboration access-mode endpoint accepts the Owner access mode from an authenticated repository collaborator… |
| 2026-10-14 15:17:25 | [CVE-2026-78231](https://nvd.nist.gov/vuln/detail/CVE-2026-78231) |  |  | When OpenID sign-in is enabled, Gitea processes unauthenticated assertion parameters and sends an HTTP POST request to… |
| 2026-10-14 15:17:25 | [CVE-2026-78433](https://nvd.nist.gov/vuln/detail/CVE-2026-78433) |  |  | Gitea's web attachment handler skips its cross-repository ownership check for attachments created before 16 January 202… |
| 2026-10-14 15:17:26 | [CVE-2026-84471](https://nvd.nist.gov/vuln/detail/CVE-2026-84471) | High | 7.2 | The fix for CVE-2026-12996 was incomplete. A use-after-free in OpenVPN 2.6.0 through 2.6.22 and 2.7_alpha1 through 2.7.… |
| 2026-10-14 15:17:26 | [CVE-2026-91184](https://nvd.nist.gov/vuln/detail/CVE-2026-91184) | High | 8.7 | Description NGINX Gateway Fabric has a vulnerability when it renders the spec.basic.realm (and spec.jwt.realm) field of… |
| 2026-10-14 15:17:26 | [CVE-2026-93479](https://nvd.nist.gov/vuln/detail/CVE-2026-93479) | Critical | 9.2 | A vulnerability exists in NGINX Plus and NGINX Open Source when a map directive uses regex matching and the root direct… |
| 2026-10-14 15:17:26 | [CVE-2026-94197](https://nvd.nist.gov/vuln/detail/CVE-2026-94197) | High | 8.7 | An authentication and authorization bypass vulnerability exists in F5 NGINX Kubernetes Ingress Controller (NIC) when co… |
| 2026-10-14 15:17:27 | [CVE-2026-95101](https://nvd.nist.gov/vuln/detail/CVE-2026-95101) | Medium | 6.9 | Description NGINX Plus and NGINX Open Source have a vulnerability in the ngx_http_v3_module module. When using HTTP/3 w… |
| 2026-10-14 15:17:28 | [CVE-2026-96615](https://nvd.nist.gov/vuln/detail/CVE-2026-96615) | High | 7.1 | Description NGINX Gateway Fabric has a vulnerability when it is configured with Gateway Custom Resource Definition (CRD… |
| 2026-10-14 15:17:28 | [CVE-2026-97205](https://nvd.nist.gov/vuln/detail/CVE-2026-97205) | Critical | 9.2 | NGINX Plus and NGINX Open Source have a vulnerability in the ngx_http_core_module module. When asynchronous file I/O (A… |
| 2026-10-14 15:17:28 | [CVE-2026-97629](https://nvd.nist.gov/vuln/detail/CVE-2026-97629) | High | 8.3 | Description When NGINX Plus or NGINX Open Source is configured with ssl_session_cache shared:name:size without an expli… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
