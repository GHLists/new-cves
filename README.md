# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-11-13 18:21 UTC

New CVEs published between 2026-11-13 17:21 UTC and 2026-11-13 18:21 UTC.

[Full CSV](data/new-cves-2026-11-13T18-21-41-560251Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-11-13 18:17:26 | [CVE-2026-107398](https://nvd.nist.gov/vuln/detail/CVE-2026-107398) | High | 7.1 | Indico is a feature-rich event management system. Prior to version 3.3.14, due to a path traversal vulnerability when b… |
| 2026-11-13 18:17:30 | [CVE-2026-123177](https://nvd.nist.gov/vuln/detail/CVE-2026-123177) | High | 8.4 | A flaw was found in dnf5daemon-server. Unauthenticated D-Bus methods pass caller-controlled URL or .rpm path patterns i… |
| 2026-11-13 18:17:30 | [CVE-2026-123965](https://nvd.nist.gov/vuln/detail/CVE-2026-123965) | Critical | 9.3 | A prompt injection vulnerability in all versions of Jet Admin Cloud Platform allows a remote attacker with a free accou… |
| 2026-11-13 18:17:31 | [CVE-2026-124041](https://nvd.nist.gov/vuln/detail/CVE-2026-124041) | Medium | 6.9 | Catalis/Patriot Properties WebPro 5.0 allows a remote unauthenticated attacker to execute arbitrary SQL queries against… |
| 2026-11-13 18:17:31 | [CVE-2026-124666](https://nvd.nist.gov/vuln/detail/CVE-2026-124666) | Medium | 6.4 | Authentication bypass by spoofing vulnerability in Apache APISIX. On a route where multi-auth falls back from wolf-rbac… |
| 2026-11-13 18:17:31 | [CVE-2026-124679](https://nvd.nist.gov/vuln/detail/CVE-2026-124679) | High | 7.8 | Authentication bypass by spoofing vulnerability in Apache APISIX. On routes using jwe-decrypt with strict: false and a… |
| 2026-11-13 18:17:31 | [CVE-2026-124680](https://nvd.nist.gov/vuln/detail/CVE-2026-124680) | High | 7.0 | Interpretation Conflict, resulting in (Incorrect Authorization) vulnerability in Apache APISIX. An unauthenticated clie… |
| 2026-11-13 18:17:31 | [CVE-2026-124716](https://nvd.nist.gov/vuln/detail/CVE-2026-124716) | Medium | 6.4 | Incorrect Authorization vulnerability in Apache APISIX. An authenticated user who holds any one of a route's required p… |
| 2026-11-13 18:17:31 | [CVE-2026-124719](https://nvd.nist.gov/vuln/detail/CVE-2026-124719) | Low | 2.3 | Authentication bypass by spoofing vulnerability in Apache APISIX. When a Route's configured headers carry a caller iden… |
| 2026-11-13 18:17:31 | [CVE-2026-124723](https://nvd.nist.gov/vuln/detail/CVE-2026-124723) | Medium | 6.3 | Interpretation Conflict, leading to Incorrect Authorization vulnerability in Apache APISIX. With match_uri_encoded_slas… |
| 2026-11-13 18:17:32 | [CVE-2026-124726](https://nvd.nist.gov/vuln/detail/CVE-2026-124726) | Medium | 6.9 | Relative Path Traversal, with Unintended Proxy vulnerability in Apache APISIX. A caller of the MCP endpoint can invoke… |
| 2026-11-13 18:17:32 | [CVE-2026-126091](https://nvd.nist.gov/vuln/detail/CVE-2026-126091) | High | 8.7 | Dental practice sites hosted with iDentalSoft send a JSON response to any user who loads certain pages containing sensi… |
| 2026-11-13 18:17:34 | [CVE-2026-128068](https://nvd.nist.gov/vuln/detail/CVE-2026-128068) | Medium | 5.3 | rails-html-sanitizer is responsible for sanitizing HTML fragments in Rails applications. From 1.0.3 through 1.7.1, Rail… |
| 2026-11-13 18:17:34 | [CVE-2026-128069](https://nvd.nist.gov/vuln/detail/CVE-2026-128069) | Medium | 4.7 | rails-html-sanitizer is responsible for sanitizing HTML fragments in Rails applications. Before 1.7.2, the HTML4 and HT… |
| 2026-11-13 18:17:34 | [CVE-2026-128070](https://nvd.nist.gov/vuln/detail/CVE-2026-128070) | Medium | 5.9 | Nuxt is an open-source web development framework for Vue.js. From 3.5.0 until 4.6.4, Nuxt can choose a parent directory… |
| 2026-11-13 18:17:35 | [CVE-2026-128071](https://nvd.nist.gov/vuln/detail/CVE-2026-128071) | Medium | 6.5 | Nuxt is an open-source web development framework for Vue.js. Nuxt from 3.0.0 until 4.6.4, @nuxt/nitro-server from 3.20.… |
| 2026-11-13 18:17:35 | [CVE-2026-128072](https://nvd.nist.gov/vuln/detail/CVE-2026-128072) | Low | 3.1 | Nuxt is an open-source web development framework for Vue.js. From @nuxt/webpack-builder 3.0.0 and @nuxt/rspack-builder… |
| 2026-11-13 18:17:36 | [CVE-2026-128074](https://nvd.nist.gov/vuln/detail/CVE-2026-128074) | Medium | 6.9 | Nuxt is an open-source web development framework for Vue.js. From 4.6.0 until 4.6.4, _payload.json URL generation and t… |
| 2026-11-13 18:17:36 | [CVE-2026-128075](https://nvd.nist.gov/vuln/detail/CVE-2026-128075) | Medium | 5.3 | Nuxt is an open-source web development framework for Vue.js. From 3.0.0 until 4.6.4, Nuxt wraps non-HTTP errors thrown… |
| 2026-11-13 18:17:37 | [CVE-2026-128076](https://nvd.nist.gov/vuln/detail/CVE-2026-128076) | Low | 3.1 | Nuxt is an open-source web development framework for Vue.js. From 3.21.6 to before 4.0.0 and from 4.4.6 until 4.6.4, th… |
| 2026-11-13 18:17:37 | [CVE-2026-128077](https://nvd.nist.gov/vuln/detail/CVE-2026-128077) | Medium | 6.5 | Nuxt is an open-source web development framework for Vue.js. From 4.6.0 until 4.6.4, Nuxt parses a request path beginni… |
| 2026-11-13 18:17:37 | [CVE-2026-128078](https://nvd.nist.gov/vuln/detail/CVE-2026-128078) | Medium | 5.3 | GLPI is a free asset and IT management software package. From 9.5.0 until 10.0.27 and 11.0.9, authenticated users could… |
| 2026-11-13 18:17:37 | [CVE-2026-128079](https://nvd.nist.gov/vuln/detail/CVE-2026-128079) | Medium | 6.8 | envd provides reproducible development environments for humans and agents. In versions starting with 0.3.38 and before… |
| 2026-11-13 18:17:38 | [CVE-2026-129139](https://nvd.nist.gov/vuln/detail/CVE-2026-129139) | High | 8.8 | paicoding from commit b8206b9 through commit 903adce uses predictable credentials for accounts created via ZSXQ login,… |
| 2026-11-13 18:17:38 | [CVE-2026-129140](https://nvd.nist.gov/vuln/detail/CVE-2026-129140) | Medium | 5.1 | paicoding 1.0.0 through 1.0.3 contains a stored cross-site scripting vulnerability in image upload because ImageService… |
| 2026-11-13 18:17:38 | [CVE-2026-129141](https://nvd.nist.gov/vuln/detail/CVE-2026-129141) | Medium | 5.1 | paicoding 1.0.0 through 1.0.3 contains a stored cross-site scripting vulnerability because SeoInjectService embeds user… |
| 2026-11-13 18:17:38 | [CVE-2026-129142](https://nvd.nist.gov/vuln/detail/CVE-2026-129142) | Medium | 5.1 | paicoding commit 766c48b through commit 903adce contains a stored cross-site scripting vulnerability in payment notific… |
| 2026-11-13 18:17:39 | [CVE-2026-129143](https://nvd.nist.gov/vuln/detail/CVE-2026-129143) | High | 8.7 | paicoding 1.0.3 contains a missing authorization vulnerability in the ArticleRestController article detail endpoint tha… |
| 2026-11-13 18:17:39 | [CVE-2026-129144](https://nvd.nist.gov/vuln/detail/CVE-2026-129144) | Medium | 5.3 | paicoding 1.0.3 contains a payment bypass vulnerability that allows authenticated attackers to unlock paid articles by… |
| 2026-11-13 18:17:39 | [CVE-2026-129151](https://nvd.nist.gov/vuln/detail/CVE-2026-129151) | High | 8.7 | SurveyKing 1.13.2 contains a missing authorization vulnerability in result lookup: the anonymous survey view leaks the… |
| 2026-11-13 18:17:39 | [CVE-2026-129152](https://nvd.nist.gov/vuln/detail/CVE-2026-129152) | Medium | 6.9 | SurveyKing 1.12.0 through 1.13.2 contains an authentication bypass vulnerability that allows unauthenticated attackers… |
| 2026-11-13 18:17:39 | [CVE-2026-129153](https://nvd.nist.gov/vuln/detail/CVE-2026-129153) | High | 7.1 | SurveyKing 1.12.0 through 1.13.2 contains an authorization bypass in the linked survey feature that fails to verify the… |
| 2026-11-13 18:17:39 | [CVE-2026-129154](https://nvd.nist.gov/vuln/detail/CVE-2026-129154) | Medium | 5.3 | SurveyKing 1.13.0 through 1.13.2 contains a stored cross-site scripting vulnerability because the server accepts a resp… |
| 2026-11-13 18:17:40 | [CVE-2026-129155](https://nvd.nist.gov/vuln/detail/CVE-2026-129155) | Medium | 5.1 | DjangoBlog 2.0.0.0 through 2.1.0.0 contains a stored cross-site scripting vulnerability because the class_filter commen… |
| 2026-11-13 18:17:40 | [CVE-2026-129156](https://nvd.nist.gov/vuln/detail/CVE-2026-129156) | Medium | 5.1 | DjangoBlog commit d186b1c through commit 6134ed6 contains a stored cross-site scripting vulnerability that allows authe… |
| 2026-11-13 18:17:40 | [CVE-2026-129157](https://nvd.nist.gov/vuln/detail/CVE-2026-129157) | Medium | 5.3 | ragent 1.0.0 through 1.1.0 contains a missing authorization vulnerability in RagTraceController that allows any logged-… |
| 2026-11-13 18:17:40 | [CVE-2026-129158](https://nvd.nist.gov/vuln/detail/CVE-2026-129158) | Medium | 5.1 | ragent 1.1.0 contains a stored cross-site scripting vulnerability that allows authenticated users to inject scripts by… |
| 2026-11-13 18:17:40 | [CVE-2026-129160](https://nvd.nist.gov/vuln/detail/CVE-2026-129160) | High | 7.1 | free-fs 2.0.1 through 2.3.1 contains an SQL injection vulnerability in FileShareServiceImpl.getPages, which passes the… |
| 2026-11-13 18:17:41 | [CVE-2026-129161](https://nvd.nist.gov/vuln/detail/CVE-2026-129161) | Critical | 9.1 | Dromara free-fs 2.0.1 through 2.3.1 contains an improper restriction of authentication attempts vulnerability that allo… |
| 2026-11-13 18:17:41 | [CVE-2026-129162](https://nvd.nist.gov/vuln/detail/CVE-2026-129162) | High | 8.2 | Dromara free-fs 2.0.1 through 2.3.1 contains a missing authentication vulnerability in FileStreamController.preview tha… |
| 2026-11-13 18:17:41 | [CVE-2026-129163](https://nvd.nist.gov/vuln/detail/CVE-2026-129163) | Medium | 5.1 | Dromara free-fs 2.0.1 through 2.3.1 contains a stored cross-site scripting vulnerability that allows registered users t… |
| 2026-11-13 18:17:41 | [CVE-2026-129164](https://nvd.nist.gov/vuln/detail/CVE-2026-129164) | High | 8.2 | Dromara free-fs 2.0.1 through 2.3.1 contains an authorization bypass vulnerability that allows attackers to access code… |
| 2026-11-13 18:17:41 | [CVE-2026-129165](https://nvd.nist.gov/vuln/detail/CVE-2026-129165) | Critical | 9.4 | Tactical RMM 0.17.0 through 1.6.1 contains an arbitrary file read in the /reporting/templates/preview/ endpoint because… |
| 2026-11-13 18:17:41 | [CVE-2026-129166](https://nvd.nist.gov/vuln/detail/CVE-2026-129166) | High | 7.1 | Keep 0.34.10 through 0.55.0 contains a blind SQL injection vulnerability in its CEL-to-SQL converter, which inserts bra… |
| 2026-11-13 18:17:41 | [CVE-2026-129167](https://nvd.nist.gov/vuln/detail/CVE-2026-129167) | Critical | 9.2 | Seafile SeaDoc converter 2.0.4 before 2.0.11 and 3.0.0 before 3.0.8 contains an absolute path traversal vulnerability t… |
| 2026-11-13 18:17:42 | [CVE-2026-129168](https://nvd.nist.gov/vuln/detail/CVE-2026-129168) | Medium | 5.3 | PMail 2.9.1 through 2.9.8 contains a stored cross-site scripting vulnerability because the /attachments/{id}/{cid} endp… |
| 2026-11-13 18:17:42 | [CVE-2026-129169](https://nvd.nist.gov/vuln/detail/CVE-2026-129169) | Medium | 5.1 | PMail 2.5.0 through 2.9.8 contains a stored cross-site scripting vulnerability that allows authenticated users to injec… |
| 2026-11-13 18:17:42 | [CVE-2026-129170](https://nvd.nist.gov/vuln/detail/CVE-2026-129170) | Medium | 5.3 | FileCodeBox 2.2.1 through 2.8.4 contains a stored cross-site scripting vulnerability in renderMarkdownPreview, which re… |
| 2026-11-13 18:17:42 | [CVE-2026-129171](https://nvd.nist.gov/vuln/detail/CVE-2026-129171) | Critical | 9.3 | NginxPulse 1.5.0 before 1.6.26 contains an unauthenticated sql injection vulnerability that allows remote attackers to… |
| 2026-11-13 18:17:42 | [CVE-2026-129172](https://nvd.nist.gov/vuln/detail/CVE-2026-129172) | Medium | 5.1 | EdgeEver 1.9.0 before 2.13.0 contains a stored cross-site scripting vulnerability in the backup restore endpoint PUT /a… |
| 2026-11-13 18:17:48 | [CVE-2026-63173](https://nvd.nist.gov/vuln/detail/CVE-2026-63173) | Medium | 5.3 | Omnispace Agora Project through 26.10.0 contains a broken access control vulnerability in which the isAutor() function… |
| 2026-11-13 18:17:49 | [CVE-2026-97357](https://nvd.nist.gov/vuln/detail/CVE-2026-97357) | Medium | 6.9 | An Out-Of-Bounds Write due to missing input validation is possible in the autoprogramming interface of SpaceCom and Spa… |
| 2026-11-13 18:17:50 | [CVE-2026-97358](https://nvd.nist.gov/vuln/detail/CVE-2026-97358) | High | 7.0 | An inclusion of web functionality from an untrusted source could allow remote code execution on SpaceCom |
| 2026-11-13 18:17:50 | [CVE-2026-97361](https://nvd.nist.gov/vuln/detail/CVE-2026-97361) | High | 8.5 | There exists an improper privilege management vulnerability that could cause privilege escalation at the SpaceCom and S… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
