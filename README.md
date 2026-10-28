# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-28 19:18 UTC

New CVEs published between 2026-10-28 18:20 UTC and 2026-10-28 19:18 UTC.

[Full CSV](data/new-cves-2026-10-28T19-18-53-358408Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-10-28 19:17:21 | [CVE-2026-106484](https://nvd.nist.gov/vuln/detail/CVE-2026-106484) |  |  | Insufficient policy enforcement in chrome-devtools-mcp in Google Chrome on Linux prior to 1.5.0 allowed a local attacke… |
| 2026-10-28 19:17:29 | [CVE-2026-118251](https://nvd.nist.gov/vuln/detail/CVE-2026-118251) | High | 8.4 | Highcharts JS is a JavaScript charting library based on SVG. Prior to 11.4.9, 12.6.1, and 13.1.0, Highcharts assigns cr… |
| 2026-10-28 19:17:29 | [CVE-2026-118252](https://nvd.nist.gov/vuln/detail/CVE-2026-118252) | High | 8.4 | Highcharts JS is a JavaScript charting library based on SVG. From 1.0.0 until 4.2.3, Highcharts Dashboards edit-mode si… |
| 2026-10-28 19:17:29 | [CVE-2026-118253](https://nvd.nist.gov/vuln/detail/CVE-2026-118253) | High | 8.4 | Highcharts JS is a JavaScript charting library based on SVG. From 1.0.0 until 4.2.3, Highcharts Dashboards edit mode pa… |
| 2026-10-28 19:17:29 | [CVE-2026-118254](https://nvd.nist.gov/vuln/detail/CVE-2026-118254) | High | 8.6 | Highcharts JS is a JavaScript charting library based on SVG. From 2.0.0 until 3.2.0, Highcharts Grid writes pagination… |
| 2026-10-28 19:17:29 | [CVE-2026-118255](https://nvd.nist.gov/vuln/detail/CVE-2026-118255) | High | 8.4 | Highcharts JS is a JavaScript charting library based on SVG. From 2.0.0 until 3.2.0, Highcharts Grid applies credits.hr… |
| 2026-10-28 19:17:30 | [CVE-2026-118256](https://nvd.nist.gov/vuln/detail/CVE-2026-118256) | Low | 2.1 | Vue I18n is the internationalization plugin for Vue.js. From 9.0.0-beta.5 until 11.4.14 and 12.0.0-alpha.5, enabling es… |
| 2026-10-28 19:17:30 | [CVE-2026-118257](https://nvd.nist.gov/vuln/detail/CVE-2026-118257) | High | 7.2 | Vue I18n is the internationalization plugin for Vue.js. From 11.1.10 until 11.4.14 and from 12.0.0-alpha.4 until 12.0.0… |
| 2026-10-28 19:17:30 | [CVE-2026-118258](https://nvd.nist.gov/vuln/detail/CVE-2026-118258) | Low | 3.7 | i18next-http-backend is a backend layer for i18next that loads translation resources in Node.js, browsers, and Deno. Pr… |
| 2026-10-28 19:17:30 | [CVE-2026-118259](https://nvd.nist.gov/vuln/detail/CVE-2026-118259) | Medium | 5.3 | opentelemetry-java is the Java implementation of the OpenTelemetry API for recording telemetry, and SDK for managing te… |
| 2026-10-28 19:17:30 | [CVE-2026-118260](https://nvd.nist.gov/vuln/detail/CVE-2026-118260) | High | 8.2 | Echo is a Go web framework. From 4.0.0 until 4.16.1, Echo v4's opt-in BodyDump middleware reads complete request bodies… |
| 2026-10-28 19:17:30 | [CVE-2026-118261](https://nvd.nist.gov/vuln/detail/CVE-2026-118261) | High | 8.2 | Echo is a Go web framework. From 4.0.0 until 4.16.1, Echo v4's opt-in Decompress middleware exposes a gzip-decoded requ… |
| 2026-10-28 19:17:30 | [CVE-2026-118262](https://nvd.nist.gov/vuln/detail/CVE-2026-118262) | High | 8.2 | Echo is a Go web framework. From 4.15.0 until 4.16.1 and 5.4.1, Echo's Proxy middleware can retain a handler, copy goro… |
| 2026-10-28 19:17:31 | [CVE-2026-118263](https://nvd.nist.gov/vuln/detail/CVE-2026-118263) | Medium | 6.3 | Echo is a Go web framework. From 5.0.0 until 5.4.1, Echo v5's BodyDump middleware can discard a BodyLimit overflow erro… |
| 2026-10-28 19:17:31 | [CVE-2026-118264](https://nvd.nist.gov/vuln/detail/CVE-2026-118264) | Critical | 9.1 | Echo is a Go web framework. From 4.0.0 until 4.16.1 and 5.4.1, Echo's Proxy middleware selects a raw tunnel from a clie… |
| 2026-10-28 19:17:31 | [CVE-2026-118265](https://nvd.nist.gov/vuln/detail/CVE-2026-118265) | Medium | 5.3 | Echo is a Go web framework. From 5.0.0 until 5.4.1, Echo v5's ExtractIPFromRealIPHeader validates whether the client-su… |
| 2026-10-28 19:17:31 | [CVE-2026-118633](https://nvd.nist.gov/vuln/detail/CVE-2026-118633) | Critical | 9.2 | A path traversal vulnerability allows a remote unauthenticated attacker to execute arbitrary code as root in Sophos UTM… |
| 2026-10-28 19:17:31 | [CVE-2026-118640](https://nvd.nist.gov/vuln/detail/CVE-2026-118640) | Medium | 5.3 | n8n before 1.123.85, 2.43.5, and 2.44.1 contains an authorization bypass vulnerability in Chat Hub that allows chat-onl… |
| 2026-10-28 19:17:31 | [CVE-2026-118641](https://nvd.nist.gov/vuln/detail/CVE-2026-118641) | Medium | 6.9 | n8n before 1.123.85, 2.x before 2.43.5, and 2.44.x before 2.44.1 contains an OData $filter injection vulnerability in t… |
| 2026-10-28 19:17:32 | [CVE-2026-118642](https://nvd.nist.gov/vuln/detail/CVE-2026-118642) | Medium | 5.1 | n8n before 1.123.85, 2.43.5, and 2.44.1 contains an authorization bypass vulnerability that allows authenticated member… |
| 2026-10-28 19:17:32 | [CVE-2026-118643](https://nvd.nist.gov/vuln/detail/CVE-2026-118643) | Medium | 5.3 | n8n before 1.123.85, 2.x before 2.43.5, and 2.44.x before 2.44.1 stores credential secrets in execution error data when… |
| 2026-10-28 19:17:32 | [CVE-2026-118644](https://nvd.nist.gov/vuln/detail/CVE-2026-118644) | Medium | 5.1 | n8n before 2.41.5 and 2.42.x before 2.42.2 passes a failed workflow's full execution context, including the identity of… |
| 2026-10-28 19:17:32 | [CVE-2026-118645](https://nvd.nist.gov/vuln/detail/CVE-2026-118645) | High | 7.0 | n8n before 1.123.85, 2.x before 2.43.5, and 2.44.x before 2.44.1 contains a filter injection vulnerability in the Quick… |
| 2026-10-28 19:17:32 | [CVE-2026-118646](https://nvd.nist.gov/vuln/detail/CVE-2026-118646) | High | 7.1 | n8n before 1.123.85, 2.43.5, and 2.44.1 contains a regular expression denial of service vulnerability that allows authe… |
| 2026-10-28 19:17:32 | [CVE-2026-118647](https://nvd.nist.gov/vuln/detail/CVE-2026-118647) | Medium | 5.3 | n8n before 1.123.85, 2.x before 2.43.5, and 2.44.x before 2.44.1 saves the SeaTable Trigger node's API token in error e… |
| 2026-10-28 19:17:33 | [CVE-2026-118648](https://nvd.nist.gov/vuln/detail/CVE-2026-118648) | High | 8.4 | n8n before 1.123.85, 2.x before 2.43.5, and 2.44.x before 2.44.1 contains a stored cross-site scripting vulnerability b… |
| 2026-10-28 19:17:33 | [CVE-2026-118649](https://nvd.nist.gov/vuln/detail/CVE-2026-118649) | High | 8.7 | n8n before 2.43.5 and 2.44.x before 2.44.1 accepts a client-supplied workflow ID and caches each workflow's owner proje… |
| 2026-10-28 19:17:33 | [CVE-2026-118675](https://nvd.nist.gov/vuln/detail/CVE-2026-118675) | Medium | 5.1 | n8n before 1.123.85, 2.43.5, and 2.44.1 contains a credential guard bypass vulnerability that allows editors of shared… |
| 2026-10-28 19:17:33 | [CVE-2026-118676](https://nvd.nist.gov/vuln/detail/CVE-2026-118676) | Medium | 5.1 | n8n before 1.123.85, 2.43.5, and 2.44.1 contains an authorization bypass vulnerability that allows member users to use… |
| 2026-10-28 19:17:33 | [CVE-2026-118677](https://nvd.nist.gov/vuln/detail/CVE-2026-118677) | Medium | 5.9 | n8n before 2.41.4 and 2.42.x before 2.42.1 contains a missing confirmation vulnerability in the Local Gateway desktop a… |
| 2026-10-28 19:17:33 | [CVE-2026-118678](https://nvd.nist.gov/vuln/detail/CVE-2026-118678) | High | 7.1 | n8n before 2.41.4 and 2.42.x before 2.42.1 contains a prototype pollution vulnerability that allows low-privileged user… |
| 2026-10-28 19:17:34 | [CVE-2026-118679](https://nvd.nist.gov/vuln/detail/CVE-2026-118679) | Medium | 6.9 | n8n before 1.123.83, 2.41.4, and 2.42.1 contains a server-side request forgery vulnerability in the Slack Trigger webho… |
| 2026-10-28 19:17:34 | [CVE-2026-118680](https://nvd.nist.gov/vuln/detail/CVE-2026-118680) | Medium | 5.9 | SiYuan 3.8.7 through 3.8.8 fails to normalize Windows GLOBALROOT device-namespace aliases, bypassing the IsSensitivePat… |
| 2026-10-28 19:17:34 | [CVE-2026-118681](https://nvd.nist.gov/vuln/detail/CVE-2026-118681) | Medium | 6.3 | go-chi chi before 5.5.0 contains an authentication bypass in middleware.SupressNotFound, which calls Match with the liv… |
| 2026-10-28 19:17:35 | [CVE-2026-118683](https://nvd.nist.gov/vuln/detail/CVE-2026-118683) | High | 8.6 | MONAI from 1.2.0 before 1.6.1 contains a remote code execution vulnerability in ConfigWorkflow.__init__, which passes a… |
| 2026-10-28 19:17:35 | [CVE-2026-118684](https://nvd.nist.gov/vuln/detail/CVE-2026-118684) | High | 8.2 | MONAI before 1.6.1 contains an insufficient integrity verification vulnerability in check_hash() that silently returns… |
| 2026-10-28 19:17:35 | [CVE-2026-118685](https://nvd.nist.gov/vuln/detail/CVE-2026-118685) | Medium | 6.9 | ToolJet from 3.20.2-lts before 3.20.242-lts contains an authorization bypass in SignupDisableGuard, which treats the st… |
| 2026-10-28 19:17:35 | [CVE-2026-118686](https://nvd.nist.gov/vuln/detail/CVE-2026-118686) | High | 8.7 | EspoCRM before 9.3.11 and 10.x before 10.0.8 contains a denial of service vulnerability in which the password-redaction… |
| 2026-10-28 19:17:35 | [CVE-2026-118687](https://nvd.nist.gov/vuln/detail/CVE-2026-118687) | High | 8.3 | Coder before 2.29.21, 2.30.0 before 2.34.12, 2.35.0 before 2.35.9, 2.36.0 before 2.36.7, and 2.37.0 before 2.37.4 does… |
| 2026-10-28 19:17:35 | [CVE-2026-118688](https://nvd.nist.gov/vuln/detail/CVE-2026-118688) | High | 8.8 | wasmtime-wasi in Wasmtime before 36.0.18, 37.0.0 before 48.0.6, and 49.0.0 before 49.0.3 re-appends a trailing slash to… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
