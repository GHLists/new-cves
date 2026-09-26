# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-09-26 14:18 UTC

New CVEs published between 2026-09-26 13:19 UTC and 2026-09-26 14:18 UTC.

[Full CSV](data/new-cves-2026-09-26T14-18-52-605052Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-09-26 14:16:39 | [CVE-2026-100600](https://nvd.nist.gov/vuln/detail/CVE-2026-100600) | Medium | 6.9 | ClawHub (the openclaw/clawhub application/backend) does not bind anonymous HTTP API requests to a trusted caller identi… |
| 2026-09-26 14:16:40 | [CVE-2026-100601](https://nvd.nist.gov/vuln/detail/CVE-2026-100601) | Medium | 6.9 | ClawHub (openclaw/clawhub) application/backend contains a server-side request forgery vulnerability in the public profi… |
| 2026-09-26 14:16:40 | [CVE-2026-100602](https://nvd.nist.gov/vuln/detail/CVE-2026-100602) | High | 7.1 | ClawHub (openclaw/clawhub application/backend) contains a missing authorization check in the changelog preview feature.… |
| 2026-09-26 14:16:40 | [CVE-2026-100603](https://nvd.nist.gov/vuln/detail/CVE-2026-100603) | High | 8.7 | ClawHub (openclaw/clawhub) application/backend contains a flaw in the skill report moderation flow: four distinct ordin… |
| 2026-09-26 14:16:40 | [CVE-2026-100604](https://nvd.nist.gov/vuln/detail/CVE-2026-100604) | Medium | 5.3 | ClawHub (openclaw/clawhub) contains an incorrect authorization vulnerability in the ClawHub application/backend: an org… |
| 2026-09-26 14:16:40 | [CVE-2026-100605](https://nvd.nist.gov/vuln/detail/CVE-2026-100605) | High | 7.5 | Flowise through 3.1.4 contains missing route-level RBAC checks on chat message endpoints that allow low-privileged API… |
| 2026-09-26 14:16:40 | [CVE-2026-100606](https://nvd.nist.gov/vuln/detail/CVE-2026-100606) | Critical | 9.2 | Flowise through 3.1.4 (Enterprise/platform mode with SSO enabled) contains an authentication bypass in the SSO login pa… |
| 2026-09-26 14:16:40 | [CVE-2026-100607](https://nvd.nist.gov/vuln/detail/CVE-2026-100607) | Critical | 9.2 | Flowise through 3.1.4 resolves SSO and local-password users solely by email without storing provider or subject identif… |
| 2026-09-26 14:16:41 | [CVE-2026-100608](https://nvd.nist.gov/vuln/detail/CVE-2026-100608) | High | 8.7 | Flowise through 3.1.4 does not enforce authorization on the BullMQ admin dashboard. When the server runs in queue mode… |
| 2026-09-26 14:16:41 | [CVE-2026-100609](https://nvd.nist.gov/vuln/detail/CVE-2026-100609) | High | 7.6 | Flowise (npm packages `flowise` and `flowise-components`) through 3.1.4 looks up credentials by ID without filtering on… |
| 2026-09-26 14:16:41 | [CVE-2026-100610](https://nvd.nist.gov/vuln/detail/CVE-2026-100610) | High | 7.7 | Flowise through 3.1.4 exposes GET /api/v1/upsert-history/:id and PATCH /api/v1/upsert-history without route-level permi… |
| 2026-09-26 14:16:41 | [CVE-2026-100611](https://nvd.nist.gov/vuln/detail/CVE-2026-100611) | High | 7.1 | Capgo (capgo.app backend, versions ≤ 12.261.0) improperly restricts which roles the apikey_manager organization role ma… |
| 2026-09-26 14:16:41 | [CVE-2026-100612](https://nvd.nist.gov/vuln/detail/CVE-2026-100612) | High | 8.6 | Capgo (capgo.app) through version 12.261.0 contains an incomplete access-control fix for the public.sso_providers table… |
| 2026-09-26 14:16:41 | [CVE-2026-100613](https://nvd.nist.gov/vuln/detail/CVE-2026-100613) | Medium | 6.0 | capgo.app is an over-the-air (OTA) update platform for Capacitor apps. In all versions up to and including the current… |
| 2026-09-26 14:16:42 | [CVE-2026-100614](https://nvd.nist.gov/vuln/detail/CVE-2026-100614) | High | 8.7 | Capgo before 12.244.1 contains a cross-tenant integrity vulnerability in the metadata-cleaning worker that trusts image… |
| 2026-09-26 14:16:42 | [CVE-2026-100615](https://nvd.nist.gov/vuln/detail/CVE-2026-100615) | High | 8.7 | Cap-go capgo.app before 12.267.1 fails to validate target API key privilege during rotation, allowing an apikey_manager… |
| 2026-09-26 14:16:42 | [CVE-2026-100616](https://nvd.nist.gov/vuln/detail/CVE-2026-100616) | High | 7.0 | capgo.app is an over-the-air update platform for Capacitor apps. In all versions prior to a fix, the row-level security… |
| 2026-09-26 14:16:42 | [CVE-2026-100617](https://nvd.nist.gov/vuln/detail/CVE-2026-100617) | High | 8.7 | Cap-go capgo.app fails to validate that principals in channel_permission_overrides belong to the organization, allowing… |
| 2026-09-26 14:16:42 | [CVE-2026-100618](https://nvd.nist.gov/vuln/detail/CVE-2026-100618) | High | 8.7 | Capgo (capgo.app) is affected by an authorization flaw in the app icon update path. The PUT /app/:id endpoint accepts a… |
| 2026-09-26 14:16:42 | [CVE-2026-100619](https://nvd.nist.gov/vuln/detail/CVE-2026-100619) | High | 8.7 | Capgo (capgo.app) blocks direct user inserts into the public.manifest table with a RESTRICTIVE row-level security polic… |
| 2026-09-26 14:16:42 | [CVE-2026-100620](https://nvd.nist.gov/vuln/detail/CVE-2026-100620) | Medium | 5.1 | Capgo CLI (npm package @capgo/cli) through 7.98.2 is affected by an over-permissioned service account in its Android on… |
| 2026-09-26 14:16:43 | [CVE-2026-100621](https://nvd.nist.gov/vuln/detail/CVE-2026-100621) | Medium | 5.3 | Capgo (capgo.app) contains an incomplete access-control/content-lock enforcement issue affecting all versions; no patch… |
| 2026-09-26 14:16:43 | [CVE-2026-100622](https://nvd.nist.gov/vuln/detail/CVE-2026-100622) | High | 8.7 | capgo.app through 12.129.0 fails to verify deletion status when serving cached bundle artifacts from the public file re… |
| 2026-09-26 14:16:43 | [CVE-2026-100623](https://nvd.nist.gov/vuln/detail/CVE-2026-100623) | High | 8.7 | Capgo (capgo.app) exposes the legacy membership table public.org_users directly through Supabase PostgREST. The table's… |
| 2026-09-26 14:16:43 | [CVE-2026-100624](https://nvd.nist.gov/vuln/detail/CVE-2026-100624) | Medium | 5.3 | Capgo.app before 12.264.5 does not enforce upload expiry or build lifecycle state in the /build/upload/:jobId TUS proxy… |
| 2026-09-26 14:16:43 | [CVE-2026-100625](https://nvd.nist.gov/vuln/detail/CVE-2026-100625) | High | 8.7 | Capgo (capgo.app) exposes a native build TUS upload proxy (supabase/functions/_backend/public/build/upload.ts) that aut… |
| 2026-09-26 14:16:43 | [CVE-2026-100626](https://nvd.nist.gov/vuln/detail/CVE-2026-100626) | Medium | 5.3 | capgo through 12.128.2 contains an insecure direct object reference vulnerability in the PUT /app/:appId endpoint that… |
| 2026-09-26 14:16:43 | [CVE-2026-100627](https://nvd.nist.gov/vuln/detail/CVE-2026-100627) | High | 7.2 | Capgo (Cap-go/capgo.app) server backend Supabase functions contain an incorrect authorization flaw in the API-key bundl… |
| 2026-09-26 14:16:43 | [CVE-2026-100628](https://nvd.nist.gov/vuln/detail/CVE-2026-100628) | High | 8.7 | capgo.app before 12.128.12 fails to enforce an organization's API key expiration policy when creating app-scoped API ke… |
| 2026-09-26 14:16:44 | [CVE-2026-100629](https://nvd.nist.gov/vuln/detail/CVE-2026-100629) | High | 7.0 | Capgo (capgo.app backend) before 12.127.5 contains an authorization flaw in the PATCH /private/role_bindings/:binding_i… |
| 2026-09-26 14:16:44 | [CVE-2026-100630](https://nvd.nist.gov/vuln/detail/CVE-2026-100630) | Medium | 5.1 | AVideo contains a stored cross-site scripting vulnerability in the video trailer1 field rendered unsanitized within an… |
| 2026-09-26 14:16:44 | [CVE-2026-100631](https://nvd.nist.gov/vuln/detail/CVE-2026-100631) | High | 8.7 | Parse Server is an open source backend server. In versions prior to 8.6.90 and in versions from 9.0.0 prior to 9.10.1-a… |
| 2026-09-26 14:16:44 | [CVE-2026-100632](https://nvd.nist.gov/vuln/detail/CVE-2026-100632) | High | 7.1 | Parse Server is an open-source backend server. In versions >= 9.0.0 and < 9.10.1-alpha.8, and in versions < 8.6.89, Liv… |
| 2026-09-26 14:16:44 | [CVE-2026-100633](https://nvd.nist.gov/vuln/detail/CVE-2026-100633) | High | 8.5 | SiYuan is a self-hosted personal knowledge management system. In versions 3.8.0 through 3.8.3, the MCP file tool's sens… |
| 2026-09-26 14:16:44 | [CVE-2026-100634](https://nvd.nist.gov/vuln/detail/CVE-2026-100634) | Medium | 5.3 | SiYuan before v3.8.4 does not validate the sender or restrict recipients in the 'siyuan-send-windows' IPC handler of th… |
| 2026-09-26 14:16:45 | [CVE-2026-100635](https://nvd.nist.gov/vuln/detail/CVE-2026-100635) | High | 8.2 | SiYuan before v3.8.4 contains an authentication bypass vulnerability in the publish service where session cookies are i… |
| 2026-09-26 14:16:45 | [CVE-2026-100636](https://nvd.nist.gov/vuln/detail/CVE-2026-100636) | High | 8.3 | SiYuan versions before v3.8.4 contain a path traversal vulnerability in the exportBrowserHTML endpoint that allows auth… |
| 2026-09-26 14:16:45 | [CVE-2026-100637](https://nvd.nist.gov/vuln/detail/CVE-2026-100637) | High | 8.3 | SiYuan versions before v3.8.4 contain a path traversal vulnerability in the checkoutRepo endpoint that allows authentic… |
| 2026-09-26 14:16:45 | [CVE-2026-100638](https://nvd.nist.gov/vuln/detail/CVE-2026-100638) | High | 8.3 | SiYuan versions before v3.8.4 contain a path traversal vulnerability in the setNotebookIcon endpoint that allows authen… |
| 2026-09-26 14:16:45 | [CVE-2026-100639](https://nvd.nist.gov/vuln/detail/CVE-2026-100639) | High | 8.6 | SiYuan v3.8.3 fails to HTML-escape the data-subtype attribute when generating gutter-button markup (app/src/protyle/gut… |
| 2026-09-26 14:16:45 | [CVE-2026-100640](https://nvd.nist.gov/vuln/detail/CVE-2026-100640) | High | 8.6 | SiYuan before v3.8.4 contains an authorization omission in the siyuan-get IPC handler that allows remote-kernel rendere… |
| 2026-09-26 14:16:46 | [CVE-2026-100641](https://nvd.nist.gov/vuln/detail/CVE-2026-100641) | High | 8.6 | SiYuan before v3.8.4 does not HTML-escape stored flashcard block content before interpolating it into the card-manager… |
| 2026-09-26 14:16:46 | [CVE-2026-100642](https://nvd.nist.gov/vuln/detail/CVE-2026-100642) | High | 7.2 | SiYuan versions from v2.1.0 before v3.8.4 contain a cross-site request forgery vulnerability in the CheckAuth lock-scre… |
| 2026-09-26 14:16:46 | [CVE-2026-100643](https://nvd.nist.gov/vuln/detail/CVE-2026-100643) | High | 8.5 | SiYuan versions before v3.8.4 fail to properly escape four stored Attribute View values in textarea elements, allowing… |
| 2026-09-26 14:16:46 | [CVE-2026-100644](https://nvd.nist.gov/vuln/detail/CVE-2026-100644) | High | 8.7 | SiYuan before v3.8.4 contains a SQL injection vulnerability in the graph query endpoint where the dailyNoteSavePath par… |
| 2026-09-26 14:16:46 | [CVE-2026-100645](https://nvd.nist.gov/vuln/detail/CVE-2026-100645) | High | 8.6 | SiYuan versions 3.7.0 before 3.8.4 contain a stored cross-site scripting vulnerability in gallery and kanban database r… |
| 2026-09-26 14:16:46 | [CVE-2026-100646](https://nvd.nist.gov/vuln/detail/CVE-2026-100646) | High | 8.6 | SiYuan is a self-hosted personal knowledge management system. In versions up to and including 3.8.3, the kernel's authe… |
| 2026-09-26 14:16:47 | [CVE-2026-100647](https://nvd.nist.gov/vuln/detail/CVE-2026-100647) | Medium | 6.9 | vLLM versions before 0.29.0 contain a denial-of-service vulnerability in the cache_salt parameter accepted on OpenAI-co… |
| 2026-09-26 14:16:47 | [CVE-2026-100648](https://nvd.nist.gov/vuln/detail/CVE-2026-100648) | Medium | 6.9 | vllm before 0.29.0 fails to enforce VLLM_MAX_AUDIO_CLIP_FILESIZE_MB limit in multimodal chat audio decoding, allowing u… |
| 2026-09-26 14:16:47 | [CVE-2026-100649](https://nvd.nist.gov/vuln/detail/CVE-2026-100649) | Medium | 6.3 | vLLM before 0.29.0 contains a resource-limit bypass vulnerability in PyNvVideoCodec decoder allocation where sampler su… |
| 2026-09-26 14:16:47 | [CVE-2026-100650](https://nvd.nist.gov/vuln/detail/CVE-2026-100650) | High | 7.1 | vLLM through 0.29.0 fetches and fully materializes remote or inline media before enforcing its documented media control… |
| 2026-09-26 14:16:47 | [CVE-2026-100651](https://nvd.nist.gov/vuln/detail/CVE-2026-100651) | High | 7.1 | vLLM before 0.29.0 fails to enforce decoder prompt-length validation on the disaggregated serving endpoint /inference/v… |
| 2026-09-26 14:16:47 | [CVE-2026-100652](https://nvd.nist.gov/vuln/detail/CVE-2026-100652) | High | 8.2 | vLLM versions 0.22.0 through 0.23.0 fail to validate stop_token_ids against vocabulary bounds in Rust HTTP and gRPC fro… |
| 2026-09-26 14:16:47 | [CVE-2026-100653](https://nvd.nist.gov/vuln/detail/CVE-2026-100653) | High | 8.3 | vLLM is an inference and serving engine for large language models. In versions from 0.22.1 through 0.28.0, the operator… |
| 2026-09-26 14:16:48 | [CVE-2026-100654](https://nvd.nist.gov/vuln/detail/CVE-2026-100654) | High | 7.1 | vLLM before 0.29.0 accepts user-controlled stop_token_ids on the OpenAI-compatible POST /v1/completions and POST /v1/ch… |
| 2026-09-26 14:16:48 | [CVE-2026-100655](https://nvd.nist.gov/vuln/detail/CVE-2026-100655) | Medium | 6.9 | Netty (io.netty:netty-codec-http) versions up to and including 4.1.137.Final and from 4.2.0.Final through 4.2.17.Final… |
| 2026-09-26 14:16:48 | [CVE-2026-100656](https://nvd.nist.gov/vuln/detail/CVE-2026-100656) | High | 8.7 | Netty (io.netty:netty-codec-http) contains an unbounded per-connection queue growth flaw in HttpServerCodec. The codec… |
| 2026-09-26 14:16:48 | [CVE-2026-100657](https://nvd.nist.gov/vuln/detail/CVE-2026-100657) | High | 8.7 | Netty's STOMP codec (io.netty:netty-codec-stomp) contains a ByteBuf leak in StompSubframeDecoder. Once a frame's declar… |
| 2026-09-26 14:16:48 | [CVE-2026-100658](https://nvd.nist.gov/vuln/detail/CVE-2026-100658) | Medium | 6.9 | Netty (io.netty:netty-codec-http) contains an unbounded per-connection queue in WebSocketServerExtensionHandler. The ha… |
| 2026-09-26 14:16:48 | [CVE-2026-100659](https://nvd.nist.gov/vuln/detail/CVE-2026-100659) | Medium | 6.9 | Netty's HTTP/3 codec (io.netty:netty-codec-http3) in versions 4.2.0.Final through 4.2.17.Final does not enforce the RFC… |
| 2026-09-26 14:16:48 | [CVE-2026-100660](https://nvd.nist.gov/vuln/detail/CVE-2026-100660) | High | 8.7 | Netty's HTTP/3 codec (io.netty:netty-codec-http3) from 4.2.0.Final through 4.2.17.Final retains unbounded per-stream QP… |
| 2026-09-26 14:16:49 | [CVE-2026-100661](https://nvd.nist.gov/vuln/detail/CVE-2026-100661) | High | 8.7 | Netty's HTTP/3 codec (io.netty:netty-codec-http3) versions 4.2.0.Final through 4.2.17.Final contain a denial-of-service… |
| 2026-09-26 14:16:49 | [CVE-2026-100662](https://nvd.nist.gov/vuln/detail/CVE-2026-100662) | High | 8.7 | Netty's HTTP/3 codec (io.netty:netty-codec-http3) versions 4.2.0.Final through 4.2.17.Final contain an uncontrolled res… |
| 2026-09-26 14:16:49 | [CVE-2026-100663](https://nvd.nist.gov/vuln/detail/CVE-2026-100663) | High | 8.7 | Netty's HTTP/3 codec (io.netty:netty-codec-http3) from 4.2.2.Final through 4.2.17.Final does not special-case HTTP/1 CO… |
| 2026-09-26 14:16:49 | [CVE-2026-100664](https://nvd.nist.gov/vuln/detail/CVE-2026-100664) | High | 8.7 | Netty's HTTP/3 codec (io.netty:netty-codec-http3) versions 4.2.2.Final through 4.2.17.Final builds the HTTP/3 :authorit… |
| 2026-09-26 14:16:49 | [CVE-2026-100665](https://nvd.nist.gov/vuln/detail/CVE-2026-100665) | High | 8.7 | Netty versions from 4.2.11.Final before 4.2.18.Final contain an incomplete hostname verification fix in the QUIC certif… |
| 2026-09-26 14:16:49 | [CVE-2026-100666](https://nvd.nist.gov/vuln/detail/CVE-2026-100666) | Medium | 6.9 | Netty's HttpServerCodec (io.netty:netty-codec-http) in versions 4.2.0.Final through 4.2.16.Final and in versions up to… |
| 2026-09-26 14:16:50 | [CVE-2026-100667](https://nvd.nist.gov/vuln/detail/CVE-2026-100667) | Medium | 6.9 | grav-plugin-login (the Grav CMS Login plugin) versions >= 3.8.7 and < 3.9.7 allow the two-factor authentication challen… |
| 2026-09-26 14:16:50 | [CVE-2026-100668](https://nvd.nist.gov/vuln/detail/CVE-2026-100668) | High | 7.1 | Grav 2.0.0 through 2.0.24 contain a Twig content sandbox escape. The `array` filter (and its identical function form) i… |
| 2026-09-26 14:16:50 | [CVE-2026-100669](https://nvd.nist.gov/vuln/detail/CVE-2026-100669) | High | 8.7 | Grav before 2.0.25 ships web server configuration samples whose access-control deny rules are matched case-sensitively.… |
| 2026-09-26 14:16:50 | [CVE-2026-100670](https://nvd.nist.gov/vuln/detail/CVE-2026-100670) | High | 8.7 | Grav CMS 2.0.14 through 2.0.24 contains a privilege escalation vulnerability in the group and account blueprints. The a… |
| 2026-09-26 14:16:50 | [CVE-2026-100671](https://nvd.nist.gov/vuln/detail/CVE-2026-100671) | High | 8.6 | Grav is a flat-file CMS. In versions 2.0.19 through 2.0.24 — and in 2.0.0 through 2.0.18 and 1.7.x only where content T… |
| 2026-09-26 14:16:50 | [CVE-2026-100672](https://nvd.nist.gov/vuln/detail/CVE-2026-100672) | High | 8.7 | The Comments plugin (getgrav/grav-plugin-comments) for Grav CMS through version 1.2.10 registers an admin handler that… |
| 2026-09-26 14:16:51 | [CVE-2026-100673](https://nvd.nist.gov/vuln/detail/CVE-2026-100673) | High | 8.4 | The Grav Data Manager plugin (getgrav/grav-plugin-datamanager) versions 1.0.1 through 1.4.4 render stored data entries… |
| 2026-09-26 14:16:51 | [CVE-2026-100674](https://nvd.nist.gov/vuln/detail/CVE-2026-100674) | Medium | 5.3 | stoatchat before 0.15.5 fails to revalidate usernames after Unicode sanitization, allowing attackers to create username… |
| 2026-09-26 14:16:51 | [CVE-2026-100675](https://nvd.nist.gov/vuln/detail/CVE-2026-100675) | High | 7.1 | stoatchat versions before 0.15.5 contain a denial of service vulnerability in the acknowledgement worker that processes… |
| 2026-09-26 14:16:51 | [CVE-2026-100676](https://nvd.nist.gov/vuln/detail/CVE-2026-100676) | High | 8.8 | January, the media proxy/embed service of stoatchat (stoatchat/stoatchat), before version 0.15.5 improperly resolves SV… |
| 2026-09-26 14:16:51 | [CVE-2026-100677](https://nvd.nist.gov/vuln/detail/CVE-2026-100677) | Medium | 6.9 | stoatchat before 0.15.5 contains an account enumeration vulnerability in the login endpoint that exposes source file lo… |
| 2026-09-26 14:16:51 | [CVE-2026-100678](https://nvd.nist.gov/vuln/detail/CVE-2026-100678) | High | 8.3 | stoatchat before 0.15.5 fails to enforce account-level attempt limits on MFA login challenges, allowing attackers who k… |
| 2026-09-26 14:16:51 | [CVE-2026-100679](https://nvd.nist.gov/vuln/detail/CVE-2026-100679) | High | 7.1 | stoatchat before 0.15.5 fails to validate that MFA tickets belong to the authenticated user, allowing attackers to bypa… |
| 2026-09-26 14:16:52 | [CVE-2026-100680](https://nvd.nist.gov/vuln/detail/CVE-2026-100680) | High | 8.6 | Budibase versions before 3.45.0 fail to disable external JSON reference resolution in the OpenAPI/Swagger import valida… |
| 2026-09-26 14:16:52 | [CVE-2026-100681](https://nvd.nist.gov/vuln/detail/CVE-2026-100681) | Medium | 6.3 | Budibase before 3.45.0 contains an unauthenticated server-side request forgery and credential exfiltration vulnerabilit… |
| 2026-09-26 14:16:52 | [CVE-2026-100682](https://nvd.nist.gov/vuln/detail/CVE-2026-100682) | High | 8.7 | Budibase Server before 3.45.0 contains an arbitrary file write vulnerability in the PWA icon upload endpoint that extra… |
| 2026-09-26 14:16:52 | [CVE-2026-100683](https://nvd.nist.gov/vuln/detail/CVE-2026-100683) | High | 8.9 | Budibase (@budibase/server) before 3.45.0 builds MySQL and MSSQL column-rename DDL in packages/backend-core/src/sql/sql… |
| 2026-09-26 14:16:52 | [CVE-2026-100684](https://nvd.nist.gov/vuln/detail/CVE-2026-100684) | Critical | 9.2 | Budibase versions 3.41.0 before 3.45.0 contain an authentication bypass in the OIDC/SSO login path of @budibase/server.… |
| 2026-09-26 14:16:52 | [CVE-2026-100685](https://nvd.nist.gov/vuln/detail/CVE-2026-100685) | High | 8.3 | Budibase before 3.45.0 fails to properly scope the GET /api/chat-links endpoint by workspace, allowing builders to enum… |
| 2026-09-26 14:16:53 | [CVE-2026-100687](https://nvd.nist.gov/vuln/detail/CVE-2026-100687) | High | 7.0 | Budibase Server before 3.45.0 fails to redact plaintext datasource credentials before broadcasting external table updat… |
| 2026-09-26 14:16:53 | [CVE-2026-100688](https://nvd.nist.gov/vuln/detail/CVE-2026-100688) | High | 7.1 | Budibase server before 3.45.0 contains a cross-tenant information disclosure vulnerability in the GET /api/applications… |
| 2026-09-26 14:16:53 | [CVE-2026-100689](https://nvd.nist.gov/vuln/detail/CVE-2026-100689) | High | 8.7 | GitPython before 3.1.62 does not validate the `path` field read from an untrusted .gitmodules file when updating submod… |
| 2026-09-26 14:16:53 | [CVE-2026-100690](https://nvd.nist.gov/vuln/detail/CVE-2026-100690) | High | 8.7 | Hugo versions from v0.161.0 through v0.165.0 run Node.js tools (css.PostCSS, css.TailwindCSS, js.Babel) under the Node.… |
| 2026-09-26 14:16:53 | [CVE-2026-100691](https://nvd.nist.gov/vuln/detail/CVE-2026-100691) | Medium | 5.1 | Hugo versions 0.75.0 through 0.165.x contain a stored cross-site scripting vulnerability: the syntax highlighter does n… |
| 2026-09-26 14:16:53 | [CVE-2026-100692](https://nvd.nist.gov/vuln/detail/CVE-2026-100692) | High | 8.7 | Hugo is a static site generator. In versions after v0.123.0 and before v0.166.0, Hugo's symlink confinement checks stop… |
| 2026-09-26 14:16:53 | [CVE-2026-100686](https://nvd.nist.gov/vuln/detail/CVE-2026-100686) | High | 8.6 | Budibase versions before 3.45.0 fail to validate per-app authorization in the POST /api/global/groups/:groupId/apps end… |
| 2026-09-26 14:16:54 | [CVE-2026-100693](https://nvd.nist.gov/vuln/detail/CVE-2026-100693) | High | 8.6 | Hugo versions from v0.162.0 before v0.166.0 contain a case-sensitive validation flaw in the security.http.urls IP-liter… |
| 2026-09-26 14:16:54 | [CVE-2026-100694](https://nvd.nist.gov/vuln/detail/CVE-2026-100694) | Medium | 5.1 | Hugo is a static site generator. In versions from v0.56.0 through v0.165.x, content files mapped to the text/org media… |
| 2026-09-26 14:16:54 | [CVE-2026-100695](https://nvd.nist.gov/vuln/detail/CVE-2026-100695) | Medium | 5.3 | Adminer before 6.0.2 contains a cross-site scripting vulnerability where the CONNECTION_ID() database result is interpo… |
| 2026-09-26 14:16:54 | [CVE-2026-100696](https://nvd.nist.gov/vuln/detail/CVE-2026-100696) | Medium | 6.9 | Adminer 4.16.0 through 6.0.1 contain a pre-authentication Server-Side Request Forgery (SSRF) vulnerability in the optio… |
| 2026-09-26 14:16:54 | [CVE-2026-100697](https://nvd.nist.gov/vuln/detail/CVE-2026-100697) | Medium | 5.3 | Adminer 6.0.0 through 6.0.1, when the official ClickHouse driver plugin (plugins/drivers/clickhouse.php, rewritten in 6… |
| 2026-09-26 14:16:54 | [CVE-2026-100698](https://nvd.nist.gov/vuln/detail/CVE-2026-100698) | Medium | 6.9 | Adminer 5.5.1 through 6.0.1 improperly parses the login 'server' string in the host_port() function in adminer/include/… |
| 2026-09-26 14:16:54 | [CVE-2026-100699](https://nvd.nist.gov/vuln/detail/CVE-2026-100699) | Medium | 6.9 | Nodemailer is a Node.js email-sending library. In versions >= 9.1.0 and < 10.0.9, the address parser (src/addressparser… |
| 2026-09-26 14:16:55 | [CVE-2026-100700](https://nvd.nist.gov/vuln/detail/CVE-2026-100700) | High | 8.7 | nodemailer before 10.0.6 contains a denial of service vulnerability in the addressparser free-text fallback regex patte… |
| 2026-09-26 14:16:55 | [CVE-2026-100701](https://nvd.nist.gov/vuln/detail/CVE-2026-100701) | Medium | 6.0 | Nodemailer versions 5.0.0 through 10.0.1 use a process-global DNS cache that is keyed only by the DNS host, while each… |
| 2026-09-26 14:16:55 | [CVE-2026-100702](https://nvd.nist.gov/vuln/detail/CVE-2026-100702) | High | 8.2 | Nodemailer before 10.0.2 fails to properly flatten deeply nested arrays in recipient fields such as to, cc, and bcc, al… |
| 2026-09-26 14:16:55 | [CVE-2026-100703](https://nvd.nist.gov/vuln/detail/CVE-2026-100703) | High | 8.3 | Kyverno 1.16.0 through 1.19.0 registers the globalcontext.Lib CEL library in its policy environment without confining i… |
| 2026-09-26 14:16:55 | [CVE-2026-100704](https://nvd.nist.gov/vuln/detail/CVE-2026-100704) | High | 8.3 | Kyverno is a policy engine for Kubernetes. In versions 1.14.0 through 1.19.0, the ImageValidatingPolicy (policies.kyver… |
| 2026-09-26 14:16:55 | [CVE-2026-100705](https://nvd.nist.gov/vuln/detail/CVE-2026-100705) | High | 8.3 | Kyverno before 1.19.1 is vulnerable to server-side request forgery. The default egress blocklist (169.254.169.254, 169.… |
| 2026-09-26 14:16:55 | [CVE-2026-100706](https://nvd.nist.gov/vuln/detail/CVE-2026-100706) | Critical | 9.4 | kyverno before 1.19.1 fails to properly validate URL-encoded path segments in Policy apiCall urlPath, allowing namespac… |
| 2026-09-26 14:16:55 | [CVE-2026-100707](https://nvd.nist.gov/vuln/detail/CVE-2026-100707) | High | 8.3 | Kyverno before 1.19.1 contains a namespace isolation bypass in the apiCall context entry of namespaced Policy resources… |
| 2026-09-26 14:16:56 | [CVE-2026-100708](https://nvd.nist.gov/vuln/detail/CVE-2026-100708) | High | 7.1 | Froxlor before 2.3.13 returns the ssl_key_file column — which stores the raw PEM TLS private-key content — verbatim in… |
| 2026-09-26 14:16:56 | [CVE-2026-100709](https://nvd.nist.gov/vuln/detail/CVE-2026-100709) | High | 7.7 | Froxlor through 2.3.10 stores only a numeric user ID in remembered-2FA tokens (panel_2fa_tokens) without recording the… |
| 2026-09-26 14:16:56 | [CVE-2026-100710](https://nvd.nist.gov/vuln/detail/CVE-2026-100710) | Medium | 6.9 | Froxlor through 2.3.10 does not filter sensitive columns from API responses: Domains::get(), Domains::listing(), SubDom… |
| 2026-09-26 14:16:56 | [CVE-2026-100711](https://nvd.nist.gov/vuln/detail/CVE-2026-100711) | High | 8.7 | froxlor versions before 2.3.12 fail to invalidate existing panel sessions, API keys, and 2FA trust cookies when a user… |
| 2026-09-26 14:16:56 | [CVE-2026-100712](https://nvd.nist.gov/vuln/detail/CVE-2026-100712) | High | 7.1 | froxlor through 2.3.10 disables a user's two-factor authentication immediately upon an unauthenticated-triggerable GET… |
| 2026-09-26 14:16:57 | [CVE-2026-100713](https://nvd.nist.gov/vuln/detail/CVE-2026-100713) | High | 7.1 | Froxlor 2.3.10 and earlier contain a time-of-check time-of-use (TOCTOU) race condition in the SSH key synchronization c… |
| 2026-09-26 14:16:57 | [CVE-2026-100714](https://nvd.nist.gov/vuln/detail/CVE-2026-100714) | Critical | 9.4 | Froxlor before 2.3.12 does not restrict or escape the system.letsencryptchallengepath setting: unlike sibling settings… |
| 2026-09-26 14:16:57 | [CVE-2026-100715](https://nvd.nist.gov/vuln/detail/CVE-2026-100715) | High | 8.5 | Froxlor through 2.3.10 is vulnerable to arbitrary file deletion via symlink following in the FTP data deletion cron tas… |
| 2026-09-26 14:16:57 | [CVE-2026-100716](https://nvd.nist.gov/vuln/detail/CVE-2026-100716) | Critical | 9.4 | Froxlor is a server administration panel. In versions 2.3.10 and earlier, the customer data-export (DataDump) cron fail… |
| 2026-09-26 14:16:57 | [CVE-2026-100717](https://nvd.nist.gov/vuln/detail/CVE-2026-100717) | High | 8.5 | froxlor is a server administration panel. In versions 2.3.10 and earlier, Validate::validateUrl rejects carriage return… |
| 2026-09-26 14:16:57 | [CVE-2026-100718](https://nvd.nist.gov/vuln/detail/CVE-2026-100718) | High | 7.1 | Froxlor through 2.3.10 does not enforce the mail.allow_external_domains policy in the EmailSender.add API command. When… |
| 2026-09-26 14:16:58 | [CVE-2026-100719](https://nvd.nist.gov/vuln/detail/CVE-2026-100719) | High | 7.1 | Froxlor versions before 2.3.12 contain a credential disclosure vulnerability in the DirProtections.listing API command… |
| 2026-09-26 14:16:58 | [CVE-2026-100720](https://nvd.nist.gov/vuln/detail/CVE-2026-100720) | Critical | 9.3 | Froxlor 2.0.0 through 2.3.10 is vulnerable to stored cross-site scripting. When a customer (the lowest-privileged authe… |
| 2026-09-26 14:17:00 | [CVE-2026-94130](https://nvd.nist.gov/vuln/detail/CVE-2026-94130) | Critical | 9.3 | Joomla Extension - joomlaboat.com - Unauthenticated SQL injection in YouTube Gallery extension < 5.7.3 - An SQL injecti… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
