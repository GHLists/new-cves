# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-28 22:18 UTC

New CVEs published between 2026-10-28 21:19 UTC and 2026-10-28 22:18 UTC.

[Full CSV](data/new-cves-2026-10-28T22-18-19-171807Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-10-28 22:17:12 | [CVE-2026-116641](https://nvd.nist.gov/vuln/detail/CVE-2026-116641) | High | 7.6 | The DB Tools rely on the TLS implementation in Golang’s standard library, which generally uses the system CA store. How… |
| 2026-10-28 22:17:12 | [CVE-2026-118537](https://nvd.nist.gov/vuln/detail/CVE-2026-118537) | Medium | 5.3 | A vulnerability was found in a2ui up to 0.10.4. This vulnerability affects unknown code of the file src/v0_9/basic_cata… |
| 2026-10-28 22:17:12 | [CVE-2026-118538](https://nvd.nist.gov/vuln/detail/CVE-2026-118538) | Medium | 5.1 | A vulnerability was determined in a2ui-project a2ui up to 0.12.0. This issue affects the function Root.renderComponentT… |
| 2026-10-28 22:17:12 | [CVE-2026-118669](https://nvd.nist.gov/vuln/detail/CVE-2026-118669) | High | 8.4 | OAuthLib is an implementation of the OAuth request-signing logic for Python 3.6+. Prior to 4.0.0, the client_credential… |
| 2026-10-28 22:17:12 | [CVE-2026-118682](https://nvd.nist.gov/vuln/detail/CVE-2026-118682) | High | 7.7 | KaringX ClashMi through 1.0.32.1801 disables TLS certificate validation by default in the HttpUtils helper, allowing at… |
| 2026-10-28 22:17:12 | [CVE-2026-118689](https://nvd.nist.gov/vuln/detail/CVE-2026-118689) | High | 8.7 | OvenMediaEngine through 0.21.0 contains a denial of service vulnerability in OvtPacket::LoadHeader() that allows unauth… |
| 2026-10-28 22:17:13 | [CVE-2026-118690](https://nvd.nist.gov/vuln/detail/CVE-2026-118690) | Critical | 9.3 | Signal K Server before 2.33.0 contains a missing authentication vulnerability that allows unauthenticated remote attack… |
| 2026-10-28 22:17:13 | [CVE-2026-118691](https://nvd.nist.gov/vuln/detail/CVE-2026-118691) | Medium | 6.3 | xianyu-auto-reply-fix through 2.0.7 contains a missing authorization vulnerability in the POST /send-message endpoint t… |
| 2026-10-28 22:17:13 | [CVE-2026-118692](https://nvd.nist.gov/vuln/detail/CVE-2026-118692) | High | 7.1 | CherryTree through 1.7.2 contains an OS command injection vulnerability in CtActions::link_clicked that allows attacker… |
| 2026-10-28 22:17:13 | [CVE-2026-118693](https://nvd.nist.gov/vuln/detail/CVE-2026-118693) | Medium | 5.6 | CherryTree through 1.7.2 contains a path traversal vulnerability in CtStorageXmlHelper::_create_image_from_xml that tru… |
| 2026-10-28 22:17:13 | [CVE-2026-118694](https://nvd.nist.gov/vuln/detail/CVE-2026-118694) | High | 8.7 | python-markdown2 through 2.5.5 contains a denial of service vulnerability that allows remote users to exhaust CPU by su… |
| 2026-10-28 22:17:13 | [CVE-2026-118752](https://nvd.nist.gov/vuln/detail/CVE-2026-118752) | High | 8.5 | FreeImage (danoli3 fork) before 3.19.22 contains a heap buffer overflow vulnerability in the PBM RLE decoder of PluginI… |
| 2026-10-28 22:17:14 | [CVE-2026-118753](https://nvd.nist.gov/vuln/detail/CVE-2026-118753) | High | 8.5 | FreeImage (danoli3 fork) before 3.19.25 contains a heap buffer overflow vulnerability in PluginGIF.cpp that allows atta… |
| 2026-10-28 22:17:14 | [CVE-2026-118754](https://nvd.nist.gov/vuln/detail/CVE-2026-118754) | Medium | 6.9 | Dolibarr ERP CRM before 24.0.2 contains a missing authorization vulnerability in htdocs/public/recruitment/view.php tha… |
| 2026-10-28 22:17:14 | [CVE-2026-118755](https://nvd.nist.gov/vuln/detail/CVE-2026-118755) | High | 8.6 | Volmarg Personal Management System through 2.1.0 contains an OS command injection vulnerability that allows authenticat… |
| 2026-10-28 22:17:14 | [CVE-2026-118756](https://nvd.nist.gov/vuln/detail/CVE-2026-118756) | Medium | 6.7 | gopass before 1.17.0 contains a path traversal vulnerability in the filesystem storage backend that allows attackers to… |
| 2026-10-28 22:17:14 | [CVE-2026-118757](https://nvd.nist.gov/vuln/detail/CVE-2026-118757) | Medium | 6.9 | PiWeb Disable payment method / Partial payment for WooCommerce before 1.1.10.9 contains a missing authorization vulnera… |
| 2026-10-28 22:17:14 | [CVE-2026-118803](https://nvd.nist.gov/vuln/detail/CVE-2026-118803) | High | 7.5 | Bricks Theme 2.4.3 and before contains an unauthenticated dynamic-data tag injection vulnerability that allows anonymou… |
| 2026-10-28 22:17:14 | [CVE-2026-118804](https://nvd.nist.gov/vuln/detail/CVE-2026-118804) | High | 7.5 | Bricks Builder 2.4.3 and before contains a broken access control vulnerability that allows unauthenticated attackers to… |
| 2026-10-28 22:17:15 | [CVE-2026-54453](https://nvd.nist.gov/vuln/detail/CVE-2026-54453) | High | 7.2 | OpenCATS is an open-source applicant tracking system and recruitment CRM for staffing agencies and hiring teams. Prior… |
| 2026-10-28 22:17:15 | [CVE-2026-54455](https://nvd.nist.gov/vuln/detail/CVE-2026-54455) | High | 7.6 | OpenCATS is an open-source applicant tracking system and recruitment CRM for staffing agencies and hiring teams. Prior… |
| 2026-10-28 22:17:15 | [CVE-2026-57448](https://nvd.nist.gov/vuln/detail/CVE-2026-57448) | Medium | 6.2 | Blombooru is a self-hosted personal booru for organizing and tagging private image collections. Prior to 1.40.0, the ad… |
| 2026-10-28 22:17:15 | [CVE-2026-61546](https://nvd.nist.gov/vuln/detail/CVE-2026-61546) | High | 8.8 | AnkiMCP is an Anki addon that implements an MCP server, enabling AI assistants to interact with the Anki flashcard appl… |
| 2026-10-28 22:17:15 | [CVE-2026-61564](https://nvd.nist.gov/vuln/detail/CVE-2026-61564) | Critical | 10.0 | AVideo is a video-sharing Platform. Prior to 8.1.0, the unauthenticated installer endpoint `install/checkConfiguration.… |
| 2026-10-28 22:17:15 | [CVE-2026-61567](https://nvd.nist.gov/vuln/detail/CVE-2026-61567) | Critical | 10.0 | AVideo is a video-sharing Platform. Prior to 8.1.0, the live-streaming endpoint `view/videosListToLive.php` accepts an… |
| 2026-10-28 22:17:16 | [CVE-2026-61569](https://nvd.nist.gov/vuln/detail/CVE-2026-61569) | High | 7.5 | AVideo is a video-sharing Platform. Prior to 8.1.0, the unauthenticated streamer login at `objects/login.json.php` pass… |
| 2026-10-28 22:17:16 | [CVE-2026-61571](https://nvd.nist.gov/vuln/detail/CVE-2026-61571) | High | 7.3 | AVideo is a video-sharing Platform. Prior to 8.1.0, the encoder lacks a global authentication layer and exposes control… |
| 2026-10-28 22:17:16 | [CVE-2026-61572](https://nvd.nist.gov/vuln/detail/CVE-2026-61572) | High | 8.6 | AVideo is a video-sharing Platform. Before the initial remediation attempt in 8.1.0, `url_get_contents` in `objects/fun… |
| 2026-10-28 22:17:16 | [CVE-2026-61573](https://nvd.nist.gov/vuln/detail/CVE-2026-61573) | Medium | 6.1 | AVideo is a video-sharing Platform. Prior to 8.1.0, the anonymous login interface reflects request values into HTML and… |
| 2026-10-28 22:17:16 | [CVE-2026-61575](https://nvd.nist.gov/vuln/detail/CVE-2026-61575) | Medium | 4.7 | AVideo is a video-sharing Platform. Prior to 8.1.0, `view/queue.php` uses `pathinfo` on the caller-controlled `fileURI`… |
| 2026-10-28 22:17:17 | [CVE-2026-93851](https://nvd.nist.gov/vuln/detail/CVE-2026-93851) | High | 8.0 | Mattermost versions 11.9.x <= 11.9.1, 11.8.x <= 11.8.5, 11.7.x <= 11.7.10 fail to validate the target post ID in the Ag… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
