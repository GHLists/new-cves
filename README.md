# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-11-17 20:19 UTC

New CVEs published between 2026-11-17 19:19 UTC and 2026-11-17 20:19 UTC.

[Full CSV](data/new-cves-2026-11-17T20-19-07-080274Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-11-17 20:17:35 | [CVE-2026-100397](https://nvd.nist.gov/vuln/detail/CVE-2026-100397) | Critical | 10.0 | Rucio is a scientific data management framework. From 1.14.0 until 35.9.1, 38.6.1, 40.4.2, and 41.1.1, validate_auth_to… |
| 2026-11-17 20:17:35 | [CVE-2026-107853](https://nvd.nist.gov/vuln/detail/CVE-2026-107853) | Medium | 6.3 | tiny-secp256k1 is a tiny secp256k1 native/JS wrapper. From 2.1.0 until 2.2.5 for tiny-secp256k1 and from 2.2.2 until 2.… |
| 2026-11-17 20:17:35 | [CVE-2026-110789](https://nvd.nist.gov/vuln/detail/CVE-2026-110789) | High | 7.5 | libp2p is a JavaScript implementation of the libp2p networking stack. Prior to 5.1.22, the @libp2p/crypto code reached… |
| 2026-11-17 20:17:36 | [CVE-2026-119192](https://nvd.nist.gov/vuln/detail/CVE-2026-119192) | High | 7.5 | Forge, also called node-forge, is a native implementation of Transport Layer Security in JavaScript. Prior to 1.4.1, pu… |
| 2026-11-17 20:17:36 | [CVE-2026-119292](https://nvd.nist.gov/vuln/detail/CVE-2026-119292) | High | 8.7 | FreeSWITCH is a Software Defined Telecom Stack enabling the digital transformation from proprietary telecom switches to… |
| 2026-11-17 20:17:36 | [CVE-2026-119293](https://nvd.nist.gov/vuln/detail/CVE-2026-119293) | Critical | 9.3 | FreeSWITCH is a Software Defined Telecom Stack enabling the digital transformation from proprietary telecom switches to… |
| 2026-11-17 20:17:36 | [CVE-2026-121707](https://nvd.nist.gov/vuln/detail/CVE-2026-121707) | High | 8.7 | Effect is a TypeScript framework that consists of several packages that work together to help build TypeScript applicat… |
| 2026-11-17 20:17:36 | [CVE-2026-121716](https://nvd.nist.gov/vuln/detail/CVE-2026-121716) | High | 7.0 | fzf is a command-line fuzzy finder. Prior to 0.74.5, bin/fzf-tmux validates separately supplied layout sizes but does n… |
| 2026-11-17 20:17:36 | [CVE-2026-121717](https://nvd.nist.gov/vuln/detail/CVE-2026-121717) | Medium | 5.0 | fzf is a command-line fuzzy finder. Prior to 0.74.5, trigger-driven zsh completion in shell/completion.zsh uses _fzf_fe… |
| 2026-11-17 20:17:38 | [CVE-2026-123351](https://nvd.nist.gov/vuln/detail/CVE-2026-123351) | Medium | 4.7 | HomeBox is a home inventory and organization system. Prior to 0.27.0, the unauthenticated GET /swagger/doc.json endpoin… |
| 2026-11-17 20:17:38 | [CVE-2026-123352](https://nvd.nist.gov/vuln/detail/CVE-2026-123352) | Medium | 6.5 | HomeBox is a home inventory and organization system. Prior to 0.27.0, a HomeBox password change revokes the user's othe… |
| 2026-11-17 20:17:40 | [CVE-2026-127220](https://nvd.nist.gov/vuln/detail/CVE-2026-127220) | Medium | 6.9 | Kadence Security plugin for WordPress (better-wp-security) before 10.0.6.1 contains a brute-force protection bypass vul… |
| 2026-11-17 20:17:40 | [CVE-2026-127221](https://nvd.nist.gov/vuln/detail/CVE-2026-127221) | Medium | 6.9 | WPS Limit Login (wps-limit-login) before 1.5.9.5 contains an improper access control vulnerability that allows unauthen… |
| 2026-11-17 20:17:42 | [CVE-2026-128073](https://nvd.nist.gov/vuln/detail/CVE-2026-128073) | High | 7.5 | gosaml2 is a Pure Go implementation of SAML 2.0. Prior to 0.12.0, ValidateEncodedResponse() calls decryptAssertions() o… |
| 2026-11-17 20:17:44 | [CVE-2026-130622](https://nvd.nist.gov/vuln/detail/CVE-2026-130622) | Medium | 5.1 | Incorrect authorization in the credential loading logic in AWS Private CA Connector for Kubernetes (aws-privateca-issue… |
| 2026-11-17 20:17:44 | [CVE-2026-130623](https://nvd.nist.gov/vuln/detail/CVE-2026-130623) | Medium | 5.1 | Incorrect authorization in the credential handling for namespace-scoped issuers in AWS Private CA Connector for Kuberne… |
| 2026-11-17 20:17:44 | [CVE-2026-130792](https://nvd.nist.gov/vuln/detail/CVE-2026-130792) | Medium | 6.9 | GPAC before 26.07.0 contains an integer underflow in gf_xml_sax_parse_intern() in src/utils/xml_parser.c that causes a… |
| 2026-11-17 20:17:45 | [CVE-2026-130793](https://nvd.nist.gov/vuln/detail/CVE-2026-130793) | Medium | 6.9 | GPAC before 26.07.0 contains a stack-based buffer overflow vulnerability in gf_filter_pid_resolve_file_template_ex() in… |
| 2026-11-17 20:17:45 | [CVE-2026-130794](https://nvd.nist.gov/vuln/detail/CVE-2026-130794) | Medium | 5.3 | Frappe HR (hrms) before 16.9.0 contains a missing authorization vulnerability in the hrms.api.roster.get_events method… |
| 2026-11-17 20:17:45 | [CVE-2026-130795](https://nvd.nist.gov/vuln/detail/CVE-2026-130795) | Medium | 6.9 | GPAC before 26.07.0 contains a type confusion vulnerability in the XMT scene loader that allows local attackers to corr… |
| 2026-11-17 20:17:45 | [CVE-2026-130796](https://nvd.nist.gov/vuln/detail/CVE-2026-130796) | High | 8.8 | Flowise 3.1.3 through 3.1.4 contains an information disclosure vulnerability that allows unauthenticated attackers to r… |
| 2026-11-17 20:17:45 | [CVE-2026-130797](https://nvd.nist.gov/vuln/detail/CVE-2026-130797) | Medium | 6.9 | GPAC through 26.07.0 contains a use of uninitialized variable vulnerability in xmt_parse_element() that allows local at… |
| 2026-11-17 20:17:45 | [CVE-2026-130798](https://nvd.nist.gov/vuln/detail/CVE-2026-130798) | Medium | 6.9 | GPAC before 26.07.0 contains a use-after-free vulnerability in the XMT scene loader that leaves dangling MFURL pointers… |
| 2026-11-17 20:17:46 | [CVE-2026-130799](https://nvd.nist.gov/vuln/detail/CVE-2026-130799) | Medium | 6.9 | GPAC before 26.07.0 contains a use-after-free vulnerability in xmt_parse_element() in src/scene_manager/loader_xmt.c th… |
| 2026-11-17 20:17:46 | [CVE-2026-130829](https://nvd.nist.gov/vuln/detail/CVE-2026-130829) | Medium | 6.8 | GPAC before 26.07.0 contains a NULL pointer dereference vulnerability in xmt_new_od_link_from_node() in src/scene_manag… |
| 2026-11-17 20:17:47 | [CVE-2026-130830](https://nvd.nist.gov/vuln/detail/CVE-2026-130830) | Medium | 6.9 | GPAC before 26.07.0 contains a use-after-free vulnerability in load_xmt_done() in src/scene_manager/loader_xmt.c that r… |
| 2026-11-17 20:17:47 | [CVE-2026-130831](https://nvd.nist.gov/vuln/detail/CVE-2026-130831) | Medium | 6.9 | GPAC before 26.07.0 contains a use-after-free vulnerability in xmt_parse_element() that allows attackers to corrupt mem… |
| 2026-11-17 20:17:47 | [CVE-2026-130832](https://nvd.nist.gov/vuln/detail/CVE-2026-130832) | Medium | 6.8 | GPAC before 26.07.0 contains a NULL pointer dereference vulnerability in xmt_parse_element() in src/scene_manager/loade… |
| 2026-11-17 20:17:47 | [CVE-2026-130833](https://nvd.nist.gov/vuln/detail/CVE-2026-130833) | Medium | 6.8 | Phoboslab pl_mpeg through commit c871f2b contains an integer underflow in plm_demux_seek() that allows attackers to tri… |
| 2026-11-17 20:17:47 | [CVE-2026-130834](https://nvd.nist.gov/vuln/detail/CVE-2026-130834) | Medium | 6.9 | GPAC before 26.07.0 contains a use-after-free vulnerability in xmt_parse_command() in loader_xmt.c that allows attacker… |
| 2026-11-17 20:17:47 | [CVE-2026-130835](https://nvd.nist.gov/vuln/detail/CVE-2026-130835) | High | 7.0 | Storyden before 1.26.17 contains a missing authorization vulnerability in the AccountRemoveRole handler that allows non… |
| 2026-11-17 20:17:48 | [CVE-2026-130836](https://nvd.nist.gov/vuln/detail/CVE-2026-130836) | Medium | 6.9 | GPAC before 26.07.0 contains an invalid pointer free vulnerability in gf_sg_command_del() in src/scenegraph/commands.c… |
| 2026-11-17 20:17:48 | [CVE-2026-130837](https://nvd.nist.gov/vuln/detail/CVE-2026-130837) | Medium | 6.9 | GPAC before 26.07.0 contains a heap-based out-of-bounds read vulnerability in xmt_parse_mf_field() in loader_xmt.c caus… |
| 2026-11-17 20:17:48 | [CVE-2026-130838](https://nvd.nist.gov/vuln/detail/CVE-2026-130838) | Critical | 9.1 | Radicale 3.3.0 before 3.8.3 contains an authorization bypass vulnerability that allows unauthenticated attackers to inh… |
| 2026-11-17 20:17:48 | [CVE-2026-130839](https://nvd.nist.gov/vuln/detail/CVE-2026-130839) | High | 8.5 | ModelScope 1.11.0 to before 1.40.1 contains an unsafe reflection vulnerability in the image-to-3D SyncDreamer pipeline… |
| 2026-11-17 20:17:48 | [CVE-2026-130840](https://nvd.nist.gov/vuln/detail/CVE-2026-130840) | Critical | 9.3 | BISHENG before 3.0.0 contains an authentication bypass vulnerability that allows unauthenticated remote attackers to im… |
| 2026-11-17 20:17:48 | [CVE-2026-130841](https://nvd.nist.gov/vuln/detail/CVE-2026-130841) | High | 8.7 | ioBroker.lovelace before 7.0.0 contains a path traversal vulnerability in the onCards() request handler that allows una… |
| 2026-11-17 20:17:49 | [CVE-2026-130842](https://nvd.nist.gov/vuln/detail/CVE-2026-130842) | Low | 2.3 | HyperFrames before 0.8.73 contains a path traversal vulnerability in the Studio server waveform and thumbnail routes th… |
| 2026-11-17 20:17:49 | [CVE-2026-130843](https://nvd.nist.gov/vuln/detail/CVE-2026-130843) | High | 8.7 | HyperFrames before 0.9.30 contains a missing Origin and Host validation vulnerability in the unauthenticated Studio API… |
| 2026-11-17 20:17:49 | [CVE-2026-130844](https://nvd.nist.gov/vuln/detail/CVE-2026-130844) | Low | 2.3 | HyperFrames before 0.8.216 contains a server-side request forgery vulnerability in the engine URL downloader because is… |
| 2026-11-17 20:17:49 | [CVE-2026-130845](https://nvd.nist.gov/vuln/detail/CVE-2026-130845) | Medium | 5.3 | CodeIgniter4 before 4.7.5 contains a cross-site scripting vulnerability in the View Parser (system/View/Parser.php) tha… |
| 2026-11-17 20:17:49 | [CVE-2026-130846](https://nvd.nist.gov/vuln/detail/CVE-2026-130846) | Medium | 5.1 | AppFlowy-Web before 0.20.0 contains a stored cross-site scripting vulnerability in the TextareaAutosize component that… |
| 2026-11-17 20:17:49 | [CVE-2026-130847](https://nvd.nist.gov/vuln/detail/CVE-2026-130847) | High | 8.6 | Dolibarr ERP CRM before 24.0.2 contains an improper authorization vulnerability in the Users REST API put() method that… |
| 2026-11-17 20:17:49 | [CVE-2026-130848](https://nvd.nist.gov/vuln/detail/CVE-2026-130848) | High | 8.7 | Dolibarr ERP CRM through 24.0.3 contains a code injection vulnerability in Website::importWebSite() that allows website… |
| 2026-11-17 20:17:50 | [CVE-2026-130849](https://nvd.nist.gov/vuln/detail/CVE-2026-130849) | Critical | 9.3 | BZFlag bzfs before 2.4.32 contains a heap out-of-bounds write vulnerability in NetHandler::tcpReceive() that allows rem… |
| 2026-11-17 20:17:50 | [CVE-2026-130850](https://nvd.nist.gov/vuln/detail/CVE-2026-130850) | Medium | 5.1 | LaraCollab through 0.18.2 contains a stored cross-site scripting vulnerability that allows authenticated client-role us… |
| 2026-11-17 20:17:50 | [CVE-2026-130851](https://nvd.nist.gov/vuln/detail/CVE-2026-130851) | High | 7.1 | wishthis through 1.2.3 contains an authorization bypass vulnerability in User::ownsWishlist() that allows authenticated… |
| 2026-11-17 20:17:50 | [CVE-2026-130852](https://nvd.nist.gov/vuln/detail/CVE-2026-130852) | Medium | 6.9 | wishthis through 1.2.3 contains a missing authentication vulnerability in the PUT branch of src/api/wishes.php that all… |
| 2026-11-17 20:17:50 | [CVE-2026-130853](https://nvd.nist.gov/vuln/detail/CVE-2026-130853) | High | 8.6 | Nexterm through 1.2.2-BETA contains a privilege escalation vulnerability that allows users with permissions.manage to g… |
| 2026-11-17 20:17:50 | [CVE-2026-130854](https://nvd.nist.gov/vuln/detail/CVE-2026-130854) | Medium | 5.1 | AudioBookRequest 1.9.0 through 2.0.1 contains a stored cross-site scripting vulnerability that allows low-privileged au… |
| 2026-11-17 20:17:51 | [CVE-2026-130855](https://nvd.nist.gov/vuln/detail/CVE-2026-130855) | High | 8.7 | Bonsai through 6.0 contains an incorrect authorization vulnerability that allows authenticated Editor users to access a… |
| 2026-11-17 20:17:51 | [CVE-2026-130856](https://nvd.nist.gov/vuln/detail/CVE-2026-130856) | Critical | 9.3 | 53AIHub before 0.5.5 contains a missing authentication vulnerability that allows remote unauthenticated attackers to re… |
| 2026-11-17 20:17:51 | [CVE-2026-130857](https://nvd.nist.gov/vuln/detail/CVE-2026-130857) | High | 8.7 | EveryDocs Core before 1.6.1 contains an authorization bypass vulnerability that allows authenticated users to access ot… |
| 2026-11-17 20:17:51 | [CVE-2026-130858](https://nvd.nist.gov/vuln/detail/CVE-2026-130858) | Medium | 5.3 | FS PBX through 2.2.5 contains a missing authorization vulnerability in FaxesController, PaymentGatewayController and Vi… |
| 2026-11-17 20:17:51 | [CVE-2026-130859](https://nvd.nist.gov/vuln/detail/CVE-2026-130859) | Medium | 5.3 | Habitat through 1.7.1 contains an insecure direct object reference vulnerability in CreatePostController::addAttachment… |
| 2026-11-17 20:17:51 | [CVE-2026-130860](https://nvd.nist.gov/vuln/detail/CVE-2026-130860) | High | 8.8 | Flagr before 1.2.5 contains an authentication bypass vulnerability that allows unauthenticated remote attackers to acce… |
| 2026-11-17 20:17:52 | [CVE-2026-130861](https://nvd.nist.gov/vuln/detail/CVE-2026-130861) | High | 8.7 | UrlHub before 1.20.1 contains a missing authorization vulnerability that allows any authenticated user to create accoun… |
| 2026-11-17 20:17:52 | [CVE-2026-130862](https://nvd.nist.gov/vuln/detail/CVE-2026-130862) | Medium | 5.1 | BeikeShop through 2.0.0.32 contains a stored cross-site scripting vulnerability that allows registered customers to inj… |
| 2026-11-17 20:17:52 | [CVE-2026-130863](https://nvd.nist.gov/vuln/detail/CVE-2026-130863) | High | 8.7 | ArtisanCloud PowerX through 1.0.2 contains a missing authorization vulnerability in the IAM role management API that al… |
| 2026-11-17 20:17:52 | [CVE-2026-130864](https://nvd.nist.gov/vuln/detail/CVE-2026-130864) | Medium | 5.3 | Coyote before commit d6e8fb9 contains a missing authorization vulnerability in Wiki\CommentController::save that allows… |
| 2026-11-17 20:17:52 | [CVE-2026-130865](https://nvd.nist.gov/vuln/detail/CVE-2026-130865) | Medium | 5.3 | wireguard_webadmin before 0.9981 contains a missing authorization vulnerability in scheduler/views.py that allows low-p… |
| 2026-11-17 20:17:52 | [CVE-2026-130866](https://nvd.nist.gov/vuln/detail/CVE-2026-130866) | Medium | 5.3 | Pastefy 7.2.1 before 7.2.7 contains a stored cross-site scripting vulnerability in MermaidViewer.vue that passes attack… |
| 2026-11-17 20:17:52 | [CVE-2026-130867](https://nvd.nist.gov/vuln/detail/CVE-2026-130867) | High | 8.7 | GreaterWMS through 2.1.54 contains an unauthenticated path traversal vulnerability in the css, js, statics and fonts ro… |
| 2026-11-17 20:17:53 | [CVE-2026-130868](https://nvd.nist.gov/vuln/detail/CVE-2026-130868) | Critical | 9.1 | GreaterWMS through 2.1.54 contains a predictable authentication token vulnerability that allows unauthenticated attacke… |
| 2026-11-17 20:17:53 | [CVE-2026-130869](https://nvd.nist.gov/vuln/detail/CVE-2026-130869) | Medium | 5.3 | Ruby Central cfp-app through 2.0 contains a missing authorization vulnerability in CommentsController#create that allow… |
| 2026-11-17 20:17:53 | [CVE-2026-130870](https://nvd.nist.gov/vuln/detail/CVE-2026-130870) | Critical | 9.1 | ClearFlask before 2.7.3 contains an improper authorization vulnerability that allows any account holding an invitation… |
| 2026-11-17 20:17:53 | [CVE-2026-130871](https://nvd.nist.gov/vuln/detail/CVE-2026-130871) | Medium | 5.3 | linkdotnet Blog through 17.1 contains an open redirect vulnerability that allows unauthenticated attackers to redirect… |
| 2026-11-17 20:17:53 | [CVE-2026-130872](https://nvd.nist.gov/vuln/detail/CVE-2026-130872) | High | 7.1 | Pytition before 2.10 contains an insecure direct object reference vulnerability in the show_signatures view that allows… |
| 2026-11-17 20:17:53 | [CVE-2026-130873](https://nvd.nist.gov/vuln/detail/CVE-2026-130873) | Medium | 5.1 | ep3-bs through 1.9.1b contains an improper authorization vulnerability that allows staff users with only user managemen… |
| 2026-11-17 20:17:54 | [CVE-2026-130874](https://nvd.nist.gov/vuln/detail/CVE-2026-130874) | High | 8.7 | Seerr before 3.5.2 contains an uncontrolled resource consumption vulnerability that allows unauthenticated attackers to… |
| 2026-11-17 20:17:54 | [CVE-2026-130875](https://nvd.nist.gov/vuln/detail/CVE-2026-130875) | High | 7.7 | tac_plus-ng before commit d8493e0 contains a stack-based buffer overflow vulnerability that allows clients holding the… |
| 2026-11-17 20:17:55 | [CVE-2026-77433](https://nvd.nist.gov/vuln/detail/CVE-2026-77433) | Medium | 6.1 | Kiwi TCMS is an open source test management system. From 16.1 until 16.2, the account confirmation page’s incomplete va… |
| 2026-11-17 20:17:56 | [CVE-2026-82037](https://nvd.nist.gov/vuln/detail/CVE-2026-82037) | Medium | 5.3 | Bludit through 3.22.0 contains a missing authorization vulnerability that allows authenticated low-privileged users to… |
| 2026-11-17 20:17:56 | [CVE-2026-82038](https://nvd.nist.gov/vuln/detail/CVE-2026-82038) | High | 7.4 | Bludit through 3.22.0 contains an improper session invalidation vulnerability that allows demoted users to retain revok… |
| 2026-11-17 20:17:56 | [CVE-2026-82136](https://nvd.nist.gov/vuln/detail/CVE-2026-82136) | Medium | 6.7 | Dell SupportAssist OS Recovery, versions prior to 5.5.16.3, contain a Download of Code Without Integrity Check vulnerab… |
| 2026-11-17 20:17:56 | [CVE-2026-82138](https://nvd.nist.gov/vuln/detail/CVE-2026-82138) | High | 7.4 | Dell SupportAssist OS Recovery, versions prior to 5.5.16.3 contain a Download of Code Without Integrity Check vulnerabi… |
| 2026-11-17 20:17:56 | [CVE-2026-82139](https://nvd.nist.gov/vuln/detail/CVE-2026-82139) | High | 7.4 | Dell SupportAssist OS Recovery, versions prior to 5.5.16.3, contain an Improper Certificate Validation vulnerability. A… |
| 2026-11-17 20:17:56 | [CVE-2026-82140](https://nvd.nist.gov/vuln/detail/CVE-2026-82140) | Medium | 4.3 | Dell SupportAssist OS Recovery, versions prior to 5.5.16.3, contain an Acceptance of Extraneous Untrusted Data With Tru… |
| 2026-11-17 20:17:57 | [CVE-2026-82142](https://nvd.nist.gov/vuln/detail/CVE-2026-82142) | High | 7.1 | Dell SupportAssist OS Recovery, versions prior to 5.5.16.3, contain a Missing Authorization vulnerability. A low privil… |
| 2026-11-17 20:17:57 | [CVE-2026-82143](https://nvd.nist.gov/vuln/detail/CVE-2026-82143) | High | 7.8 | Dell SupportAssist OS Recovery, versions prior to 5.5.16.3 contain an Improper Authorization vulnerability. A low privi… |
| 2026-11-17 20:17:57 | [CVE-2026-82145](https://nvd.nist.gov/vuln/detail/CVE-2026-82145) | Medium | 6.1 | Dell SupportAssist OS Recovery, versions prior to 5.5.16.3, contain an Insecure Inherited Permissions vulnerability. A… |
| 2026-11-17 20:17:57 | [CVE-2026-82146](https://nvd.nist.gov/vuln/detail/CVE-2026-82146) | High | 7.8 | Dell SupportAssist OS Recovery, versions prior to 5.5.16.3, contain an Untrusted Search Path vulnerability. A low privi… |
| 2026-11-17 20:17:57 | [CVE-2026-82149](https://nvd.nist.gov/vuln/detail/CVE-2026-82149) | Medium | 5.9 | Dell SupportAssist OS Recovery, versions prior to 5.5.16.3, contain an External Control of System or Configuration Sett… |
| 2026-11-17 20:17:57 | [CVE-2026-82150](https://nvd.nist.gov/vuln/detail/CVE-2026-82150) | High | 8.0 | Dell SupportAssist OS Recovery, versions prior to 5.5.16.3, contain an Insufficient Verification of Data Authenticity v… |
| 2026-11-17 20:17:59 | [CVE-2026-95822](https://nvd.nist.gov/vuln/detail/CVE-2026-95822) | Low | 3.3 | The SOCKS5 client in subsys/net/lib/socks/socks.c built the CONNECT request in socks5_tcp_connect() by choosing the SOC… |
| 2026-11-17 20:18:00 | [CVE-2026-97698](https://nvd.nist.gov/vuln/detail/CVE-2026-97698) | High | 7.5 | Mistune is a Python Markdown parser with renderers and plugins. Prior to 3.3.4, parse_link_href performs an unbounded p… |
| 2026-11-17 20:18:00 | [CVE-2026-97699](https://nvd.nist.gov/vuln/detail/CVE-2026-97699) | High | 7.5 | Mistune is a Python Markdown parser with renderers and plugins. Prior to 3.3.4, inline image parsing sends nested ![ op… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
