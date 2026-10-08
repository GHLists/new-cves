# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-08 18:18 UTC

New CVEs published between 2026-10-08 17:19 UTC and 2026-10-08 18:18 UTC.

[Full CSV](data/new-cves-2026-10-08T18-18-34-296928Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-10-08 18:17:19 | [CVE-2026-107302](https://nvd.nist.gov/vuln/detail/CVE-2026-107302) | High | 7.5 | msgpack5 is a msgpack v5 implementation for node.js and the browser. Prior to 6.1.0, the decoder reads the four-byte le… |
| 2026-10-08 18:17:19 | [CVE-2026-107303](https://nvd.nist.gov/vuln/detail/CVE-2026-107303) | High | 7.6 | JHipster is a development platform to quickly generate, develop, and deploy modern web applications and microservice ar… |
| 2026-10-08 18:17:19 | [CVE-2026-107332](https://nvd.nist.gov/vuln/detail/CVE-2026-107332) | Medium | 6.8 | Insecure file permissions in the CodeCatalyst connection handler in AWS Toolkit for VS Code before 4.10.0 allowed local… |
| 2026-10-08 18:17:19 | [CVE-2026-107333](https://nvd.nist.gov/vuln/detail/CVE-2026-107333) | High | 8.1 | Malcolm's nginx based reverse proxy contains a URL path normalization inconsistency between its Lua based role-based ac… |
| 2026-10-08 18:17:19 | [CVE-2026-107334](https://nvd.nist.gov/vuln/detail/CVE-2026-107334) | Medium | 5.4 | Malcolm's nginx Lua role-based access control (RBAC) layer decides whether an authenticated user may reach a role-restr… |
| 2026-10-08 18:17:19 | [CVE-2026-107335](https://nvd.nist.gov/vuln/detail/CVE-2026-107335) | Medium | 6.5 | Malcolm's upload-processing pipeline (scripts/safe-extract.py) enforces entry-count, nesting-depth, and total-uncompres… |
| 2026-10-08 18:17:20 | [CVE-2026-107336](https://nvd.nist.gov/vuln/detail/CVE-2026-107336) | Medium | 6.5 | Malcolm's front nginx reverse proxy defines a "Dashboards → Arkime shortcut" location using a case-insensitive regex ma… |
| 2026-10-08 18:17:20 | [CVE-2026-107337](https://nvd.nist.gov/vuln/detail/CVE-2026-107337) | High | 7.1 | The Malcolm kiosk Flask application exposes a POST /script_call/<script> endpoint with zero authentication and wildcard… |
| 2026-10-08 18:17:21 | [CVE-2026-107361](https://nvd.nist.gov/vuln/detail/CVE-2026-107361) | Medium | 4.2 | The Arkime live capture service (arkime-live) in Malcolm runs with network_mode: host, exposing port 8005 on all networ… |
| 2026-10-08 18:17:21 | [CVE-2026-107362](https://nvd.nist.gov/vuln/detail/CVE-2026-107362) | High | 7.1 | Malcolm file-upload component ships the upstream FilePond PHP server (pqina/filepond-server-php) largely unmodified: Do… |
| 2026-10-08 18:17:21 | [CVE-2026-107375](https://nvd.nist.gov/vuln/detail/CVE-2026-107375) | High | 8.8 | JHipster is a development platform to quickly generate, develop, and deploy modern web applications and microservice ar… |
| 2026-10-08 18:17:22 | [CVE-2026-107376](https://nvd.nist.gov/vuln/detail/CVE-2026-107376) | High | 8.2 | webonyx graphql-php is a PHP implementation of the GraphQL specification. Prior to 15.32.3, GraphQL\Language\Parser per… |
| 2026-10-08 18:17:22 | [CVE-2026-107377](https://nvd.nist.gov/vuln/detail/CVE-2026-107377) | High | 7.5 | datamodel-code-generator generates Python data models from schema definitions. From 0.59.0 until 0.81.0, an attacker-co… |
| 2026-10-08 18:17:23 | [CVE-2026-107378](https://nvd.nist.gov/vuln/detail/CVE-2026-107378) | High | 8.7 | CairoSVG is an SVG converter based on Cairo, a 2D graphics library. Prior to 2.9.1, rendering an attacker-controlled SV… |
| 2026-10-08 18:17:23 | [CVE-2026-107379](https://nvd.nist.gov/vuln/detail/CVE-2026-107379) | Medium | 6.5 | savg-sanitizer is a PHP SVG/XML sanitizer. Prior to 1.0.0, svg-sanitizer allows a crafted SVG DTD with a #FIXED attribu… |
| 2026-10-08 18:17:23 | [CVE-2026-107380](https://nvd.nist.gov/vuln/detail/CVE-2026-107380) | Medium | 5.4 | savg-sanitizer is a PHP SVG/XML sanitizer. Prior to 1.0.0, svg-sanitizer's isHrefSafeValue() validates an SVG href afte… |
| 2026-10-08 18:17:25 | [CVE-2026-107695](https://nvd.nist.gov/vuln/detail/CVE-2026-107695) | High | 7.1 | FFmpeg before 8.1.3 contains an infinite loop vulnerability in the HLS demuxer that allows remote attackers to cause de… |
| 2026-10-08 18:17:26 | [CVE-2026-107696](https://nvd.nist.gov/vuln/detail/CVE-2026-107696) | High | 7.1 | FFmpeg through 9.0.2 contains an infinite loop vulnerability in ff_rtsp_connect() in libavformat/rtsp.c that follows RT… |
| 2026-10-08 18:17:26 | [CVE-2026-107697](https://nvd.nist.gov/vuln/detail/CVE-2026-107697) | Medium | 5.3 | FFmpeg before 8.1.3 contains a protection mechanism failure in the HLS demuxer that allows attackers to bypass protocol… |
| 2026-10-08 18:17:26 | [CVE-2026-107698](https://nvd.nist.gov/vuln/detail/CVE-2026-107698) | Medium | 5.3 | FFmpeg before 7.1.4 and 8.0.x before 8.0.2 contains a server-side request forgery vulnerability in ff_rtsp_connect() in… |
| 2026-10-08 18:17:26 | [CVE-2026-107702](https://nvd.nist.gov/vuln/detail/CVE-2026-107702) | Medium | 5.3 | QloApps through 1.7.0 contains an authorization bypass vulnerability in AdminHotelRoomsBookingController::postProcess()… |
| 2026-10-08 18:17:48 | [CVE-2026-62170](https://nvd.nist.gov/vuln/detail/CVE-2026-62170) |  |  | Rejected reason: This CVE is a duplicate of another CVE. |
| 2026-10-08 18:17:48 | [CVE-2026-62171](https://nvd.nist.gov/vuln/detail/CVE-2026-62171) |  |  | Rejected reason: This CVE is a duplicate of another CVE. |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
