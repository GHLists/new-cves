# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-11-25 10:18 UTC

New CVEs published between 2026-11-25 09:22 UTC and 2026-11-25 10:18 UTC.

[Full CSV](data/new-cves-2026-11-25T10-18-44-007073Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-11-25 10:17:09 | [CVE-2026-122121](https://nvd.nist.gov/vuln/detail/CVE-2026-122121) |  |  | Cross Site Scripting (XSS) in 2.10 Legacy Theming in Apache JSPWIKI version 2.10.0 through 3.0.0 on all platforms allow… |
| 2026-11-25 10:17:10 | [CVE-2026-125949](https://nvd.nist.gov/vuln/detail/CVE-2026-125949) |  |  | Cross Site Scripting (XSS) in the Markdown renderer of Apache JSPWiki 2.11.0 through 3.0.0 on all platforms, when the M… |
| 2026-11-25 10:17:11 | [CVE-2026-133743](https://nvd.nist.gov/vuln/detail/CVE-2026-133743) | High | 7.0 | The fix for CVE-2026-123339 (GHSA-wg5q-m2ww-f3c9) restores the router context of the main request after an inline fragm… |
| 2026-11-25 10:17:11 | [CVE-2026-133744](https://nvd.nist.gov/vuln/detail/CVE-2026-133744) | Medium | 6.3 | The fixes for CVE-2026-135804 (GHSA-cpww-5vpx-72x7) bound the regex work of a JsonCrawler::find() call, and evaluate fi… |
| 2026-11-25 10:17:11 | [CVE-2026-133745](https://nvd.nist.gov/vuln/detail/CVE-2026-133745) | Medium | 5.3 | The router redirects a request to the same URL with or without its trailing slash, or with the scheme that a route requ… |
| 2026-11-25 10:17:11 | [CVE-2026-133746](https://nvd.nist.gov/vuln/detail/CVE-2026-133746) | Medium | 5.3 | The fix for CVE-2026-45065 (GHSA-72xp-p242-47p9) anchored the requirements that UrlGenerator checks parameter values ag… |
| 2026-11-25 10:17:11 | [CVE-2026-133747](https://nvd.nist.gov/vuln/detail/CVE-2026-133747) | Medium | 6.3 | Since Symfony 7.4, framework.http_client.scoped_clients can enable caching on a scoped client. FrameworkBundle then put… |
| 2026-11-25 10:17:12 | [CVE-2026-133748](https://nvd.nist.gov/vuln/detail/CVE-2026-133748) | Medium | 6.3 | NoPrivateNetworkHttpClient accepts a list of subnets to block instead of its default one. When that list contains an IP… |
| 2026-11-25 10:17:12 | [CVE-2026-133749](https://nvd.nist.gov/vuln/detail/CVE-2026-133749) | Low | 2.3 | GuardAuthenticatorHandler::authenticateUserAndHandleSuccess() logs a user in programmatically with a Guard authenticato… |
| 2026-11-25 10:17:12 | [CVE-2026-133750](https://nvd.nist.gov/vuln/detail/CVE-2026-133750) | Medium | 6.3 | Since Symfony 7.4, CachingHttpClient can cache the responses of HTTP clients, for example when caching is enabled in fr… |
| 2026-11-25 10:17:12 | [CVE-2026-133751](https://nvd.nist.gov/vuln/detail/CVE-2026-133751) | Medium | 6.3 | Since Symfony 7.3, the require_tls option of EsmtpTransport refuses to send a message over a connection that isn't encr… |
| 2026-11-25 10:17:12 | [CVE-2026-133752](https://nvd.nist.gov/vuln/detail/CVE-2026-133752) | Medium | 6.3 | When it denormalizes data into a class, the Serializer computes which attributes it may write from the #[Ignore] and #[… |
| 2026-11-25 10:17:12 | [CVE-2026-133753](https://nvd.nist.gov/vuln/detail/CVE-2026-133753) | Medium | 5.3 | With the unanimous access decision strategy, an access_control rule that lists several roles requires all of them. That… |
| 2026-11-25 10:17:12 | [CVE-2026-133754](https://nvd.nist.gov/vuln/detail/CVE-2026-133754) | Medium | 5.3 | UrlGenerator puts the values of host placeholders into the generated URL without encoding them. Their default requireme… |
| 2026-11-25 10:17:13 | [CVE-2026-133755](https://nvd.nist.gov/vuln/detail/CVE-2026-133755) | Medium | 6.3 | Since Symfony 7.3, the require_tls option of EsmtpTransport refuses to send a message over a connection that isn't encr… |
| 2026-11-25 10:17:13 | [CVE-2026-133756](https://nvd.nist.gov/vuln/detail/CVE-2026-133756) | Medium | 5.3 | MetaRefreshAttributeSanitizer checks the URL of a <meta http-equiv="refresh"> directive only when its content starts wi… |
| 2026-11-25 10:17:13 | [CVE-2026-133757](https://nvd.nist.gov/vuln/detail/CVE-2026-133757) | High | 8.2 | Since Symfony 5.4.48, 6.4.16, 7.1.9 and 7.2.0, NoPrivateNetworkHttpClient follows redirects itself, and sends each hop… |
| 2026-11-25 10:17:13 | [CVE-2026-133758](https://nvd.nist.gov/vuln/detail/CVE-2026-133758) | Medium | 6.3 | Since Symfony 5.4.48, 6.4.16, 7.1.9 and 7.2.0, NoPrivateNetworkHttpClient prepares each request with the default option… |
| 2026-11-25 10:17:13 | [CVE-2026-133759](https://nvd.nist.gov/vuln/detail/CVE-2026-133759) | Medium | 6.3 | DoctrineTokenProvider keeps a copy of the previous token of a remember-me cookie. This way, concurrent requests sent wi… |
| 2026-11-25 10:17:13 | [CVE-2026-133760](https://nvd.nist.gov/vuln/detail/CVE-2026-133760) | High | 8.7 | The fix for CVE-2026-109449 made the expression parser check the nesting level of long expressions. This check exists s… |
| 2026-11-25 10:17:14 | [CVE-2026-133761](https://nvd.nist.gov/vuln/detail/CVE-2026-133761) | High | 8.7 | CsvEncoder::decode() splits each header cell on the key separator, . by default, and nests the decoded rows one level p… |
| 2026-11-25 10:17:14 | [CVE-2026-133762](https://nvd.nist.gov/vuln/detail/CVE-2026-133762) | Medium | 6.0 | Since Symfony 7.4.0, FrameworkBundle chooses the error renderer from the runtime mode of the application, which comes f… |
| 2026-11-25 10:17:14 | [CVE-2026-134790](https://nvd.nist.gov/vuln/detail/CVE-2026-134790) | Medium | 5.3 | The fix for CVE-2017-16652 restricts the redirects of HttpUtils::createRedirectResponse() to the host of the request. W… |
| 2026-11-25 10:17:14 | [CVE-2026-134791](https://nvd.nist.gov/vuln/detail/CVE-2026-134791) | High | 8.7 | Since Symfony 7.2, expressions can contain comments. The lexer used a regular expression to find the end of a comment.… |
| 2026-11-25 10:17:14 | [CVE-2026-134792](https://nvd.nist.gov/vuln/detail/CVE-2026-134792) | High | 8.3 | When the proxy option isn't set, HttpClient takes the proxy from environment variables like http_proxy or HTTP_PROXY. O… |
| 2026-11-25 10:17:14 | [CVE-2026-136641](https://nvd.nist.gov/vuln/detail/CVE-2026-136641) | Medium | 6.8 | Pydantic AI Harness's PlaywrightBrowser enforces its egress policy on HTTP requests and page WebSockets, but not on Web… |
| 2026-11-25 10:17:15 | [CVE-2026-136706](https://nvd.nist.gov/vuln/detail/CVE-2026-136706) | Critical | 9.3 | This vulnerability exists in the DIGIT Platform due to improper neutralization of user supplied input while constructin… |
| 2026-11-25 10:17:15 | [CVE-2026-78105](https://nvd.nist.gov/vuln/detail/CVE-2026-78105) |  |  | Cross Site Scripting/injection in WYSIWYG editor in Apache JSPWIKI from 2.10 through 3.0.0 on all platforms allows atta… |
| 2026-11-25 10:17:15 | [CVE-2026-78108](https://nvd.nist.gov/vuln/detail/CVE-2026-78108) |  |  | Resource Exhaustion in Tika Search provider in Apache JSPWIKI versions 2.11.0.M7 through 3.0.0 on all platforms allows… |
| 2026-11-25 10:17:15 | [CVE-2026-78110](https://nvd.nist.gov/vuln/detail/CVE-2026-78110) |  |  | Cascading Style Sheet injection in Image plugin in Apache JSPWIKI versions 2.1.4 through 3.0.0 on all platforms allows… |
| 2026-11-25 10:17:15 | [CVE-2026-80267](https://nvd.nist.gov/vuln/detail/CVE-2026-80267) | High | 7.8 | Dell Secure Connect Gateway (SCG) Virtual Edition, versions prior to 5.36.00.16, contains a Use of Hard-coded Credentia… |
| 2026-11-25 10:17:15 | [CVE-2026-80269](https://nvd.nist.gov/vuln/detail/CVE-2026-80269) | High | 7.3 | Dell Secure Connect Gateway (SCG) Virtual Edition, versions prior to 5.36.00.16, contains an Insecure Temporary File vu… |
| 2026-11-25 10:17:15 | [CVE-2026-80270](https://nvd.nist.gov/vuln/detail/CVE-2026-80270) | Medium | 5.1 | Dell Secure Connect Gateway (SCG) Virtual Edition, versions prior to 5.36.00.16, contains an XML Injection vulnerabilit… |
| 2026-11-25 10:17:16 | [CVE-2026-80271](https://nvd.nist.gov/vuln/detail/CVE-2026-80271) | High | 7.8 | Dell Secure Connect Gateway (SCG) Virtual Edition, versions prior to 5.36.00.16, contains a Use of Hard-coded Cryptogra… |
| 2026-11-25 10:17:16 | [CVE-2026-80272](https://nvd.nist.gov/vuln/detail/CVE-2026-80272) | Medium | 5.1 | Dell Secure Connect Gateway (SCG) Virtual Edition, versions prior to 5.36.00.16, contains a Missing Authorization vulne… |
| 2026-11-25 10:17:16 | [CVE-2026-80273](https://nvd.nist.gov/vuln/detail/CVE-2026-80273) | High | 8.4 | Dell Secure Connect Gateway (SCG) Virtual Edition, versions prior to 5.36.00.16, contains an Improper Neutralization of… |
| 2026-11-25 10:17:16 | [CVE-2026-80283](https://nvd.nist.gov/vuln/detail/CVE-2026-80283) | High | 8.4 | Dell Secure Connect Gateway (SCG) Virtual Edition, versions prior to 5.36.00.16, contains a Missing Authentication for… |
| 2026-11-25 10:17:16 | [CVE-2026-80284](https://nvd.nist.gov/vuln/detail/CVE-2026-80284) | High | 7.7 | Dell Secure Connect Gateway (SCG) Virtual Edition, versions prior to 5.36.00.16, contains an Improper Authentication vu… |
| 2026-11-25 10:17:16 | [CVE-2026-80285](https://nvd.nist.gov/vuln/detail/CVE-2026-80285) | High | 7.8 | Dell Secure Connect Gateway (SCG) Virtual Edition, versions prior to 5.36.00.16, contains an Execution with Unnecessary… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
