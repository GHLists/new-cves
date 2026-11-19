# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-11-19 22:21 UTC

New CVEs published between 2026-11-19 21:22 UTC and 2026-11-19 22:21 UTC.

[Full CSV](data/new-cves-2026-11-19T22-21-20-260613Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-11-19 22:17:49 | [CVE-2026-106012](https://nvd.nist.gov/vuln/detail/CVE-2026-106012) |  |  | Incorrect Authorization vulnerability in Apache Tomcat could occur during a request dispatch if the request depended on… |
| 2026-11-19 22:17:54 | [CVE-2026-114516](https://nvd.nist.gov/vuln/detail/CVE-2026-114516) | Critical | 9.8 | Etherpad is a real-time collaborative editor. From 1.8.14 until 3.3.3, the pre-authentication /static/* plugin asset ha… |
| 2026-11-19 22:17:58 | [CVE-2026-116561](https://nvd.nist.gov/vuln/detail/CVE-2026-116561) |  |  | Improper cleanup on thrown exception vulnerability in Apache Tomcat meant that an HTTP 200 response was sent rather tha… |
| 2026-11-19 22:17:58 | [CVE-2026-116600](https://nvd.nist.gov/vuln/detail/CVE-2026-116600) |  |  | Missing release of memory after effective lifetime vulnerability in Apache Tomcat via WebSocket. This issue affects Apa… |
| 2026-11-19 22:17:58 | [CVE-2026-116830](https://nvd.nist.gov/vuln/detail/CVE-2026-116830) |  |  | Missing release of resource after effective lifetime vulnerability in Apache Tomcat's HTTP/2 initial connection handlin… |
| 2026-11-19 22:17:58 | [CVE-2026-117517](https://nvd.nist.gov/vuln/detail/CVE-2026-117517) |  |  | The fix for CVE-2026-25854 was incomplete. This issue affects Apache Tomcat: from 11.0.19 through 11.0.27, from 10.1.53… |
| 2026-11-19 22:17:58 | [CVE-2026-118028](https://nvd.nist.gov/vuln/detail/CVE-2026-118028) |  |  | Execution After Redirect (EAR) vulnerability in Apache Tomcat in RedirectValve affecting flags [F], [G] and [R]. This i… |
| 2026-11-19 22:17:59 | [CVE-2026-118233](https://nvd.nist.gov/vuln/detail/CVE-2026-118233) |  |  | Allocation of resources without limits or throttling vulnerability in Apache Tomcat during HTTP upgrade in some circums… |
| 2026-11-19 22:17:59 | [CVE-2026-118436](https://nvd.nist.gov/vuln/detail/CVE-2026-118436) |  |  | Allocation of resources without limits or throttling vulnerability in Apache Tomcat in the CGI Servlet when handling PO… |
| 2026-11-19 22:17:59 | [CVE-2026-121649](https://nvd.nist.gov/vuln/detail/CVE-2026-121649) |  |  | Use of cache containing sensitive information vulnerability in Apache Tomcat's ExpiresFilter caused by the filter remov… |
| 2026-11-19 22:18:03 | [CVE-2026-133217](https://nvd.nist.gov/vuln/detail/CVE-2026-133217) | Medium | 4.8 | A weakness has been identified in OSGeo shapelib up to 1.6.3. This vulnerability affects the function DBFCloneEmpty of… |
| 2026-11-19 22:18:04 | [CVE-2026-133325](https://nvd.nist.gov/vuln/detail/CVE-2026-133325) |  |  | Key exchange without entity authentication vulnerability in Apache Tomcat allowed an unauthenticated node to join a clu… |
| 2026-11-19 22:18:04 | [CVE-2026-133430](https://nvd.nist.gov/vuln/detail/CVE-2026-133430) | Medium | 5.4 | A flaw was found in Keycloak. This vulnerability allows an authenticated remote attacker to cause a denial of service b… |
| 2026-11-19 22:18:04 | [CVE-2026-133476](https://nvd.nist.gov/vuln/detail/CVE-2026-133476) | High | 8.8 | In Dolibarr before 24.0.3, dolForgeSQLCriteriaCallback() in htdocs/core/lib/functions.lib.php allows account takeover b… |
| 2026-11-19 22:18:04 | [CVE-2026-133481](https://nvd.nist.gov/vuln/detail/CVE-2026-133481) | Medium | 4.3 | In Dolibarr before 24.0.3, /api/index.php/eventattendees discloses attendee and project data regardless of the caller's… |
| 2026-11-19 22:18:04 | [CVE-2026-133494](https://nvd.nist.gov/vuln/detail/CVE-2026-133494) | Medium | 4.3 | Greenbone gvmd before 26.43.0 does not restrict certificate creation. Even the Observer role, documented to be read-onl… |
| 2026-11-19 22:18:06 | [CVE-2026-61798](https://nvd.nist.gov/vuln/detail/CVE-2026-61798) | High | 8.1 | netty-incubator-codec-ohttp implements Oblivious HTTP (OHTTP) gateway and client functionality using Netty. Prior to 0.… |
| 2026-11-19 22:18:06 | [CVE-2026-61799](https://nvd.nist.gov/vuln/detail/CVE-2026-61799) | Medium | 5.3 | netty-incubator-codec-ohttp implements Oblivious HTTP (OHTTP) gateway and client functionality using Netty. Prior to 0.… |
| 2026-11-19 22:18:06 | [CVE-2026-61827](https://nvd.nist.gov/vuln/detail/CVE-2026-61827) | High | 8.7 | netty-incubator-codec-ohttp implements Oblivious HTTP (OHTTP) gateway and client functionality using Netty. Prior to 0.… |
| 2026-11-19 22:18:07 | [CVE-2026-63124](https://nvd.nist.gov/vuln/detail/CVE-2026-63124) | High | 7.5 | netty-incubator-codec-ohttp implements Oblivious HTTP (OHTTP) gateway and client functionality using Netty. Prior to 0.… |
| 2026-11-19 22:18:07 | [CVE-2026-63202](https://nvd.nist.gov/vuln/detail/CVE-2026-63202) | High | 7.5 | netty-incubator-codec-ohttp implements Oblivious HTTP (OHTTP) gateway and client functionality using Netty. Prior to 0.… |
| 2026-11-19 22:18:08 | [CVE-2026-69133](https://nvd.nist.gov/vuln/detail/CVE-2026-69133) | Medium | 5.3 | netty-incubator-codec-ohttp implements Oblivious HTTP (OHTTP) gateway and client functionality using Netty. From 0.0.20… |
| 2026-11-19 22:18:44 | [CVE-2026-77312](https://nvd.nist.gov/vuln/detail/CVE-2026-77312) | Critical | 10.0 | Flyto2 Core is an execution kernel for automation and AI-agent workflows. Prior to 2.26.8, the earlier CVE-2026-67429 r… |
| 2026-11-19 22:18:44 | [CVE-2026-77313](https://nvd.nist.gov/vuln/detail/CVE-2026-77313) | High | 7.1 | Flyto2 Core is an execution kernel for automation and AI-agent workflows. Prior to 2.26.8, validate_url_ssrf in src/cor… |
| 2026-11-19 22:18:44 | [CVE-2026-77314](https://nvd.nist.gov/vuln/detail/CVE-2026-77314) | Medium | 6.3 | Flyto2 Core is an execution kernel for automation and AI-agent workflows. Prior to 2.26.8, the MCP run_recipe tool in s… |
| 2026-11-19 22:18:44 | [CVE-2026-77315](https://nvd.nist.gov/vuln/detail/CVE-2026-77315) | High | 8.5 | Flyto2 Core is an execution kernel for automation and AI-agent workflows. Prior to 2.26.8, http.paginate in src/core/mo… |
| 2026-11-19 22:18:44 | [CVE-2026-77316](https://nvd.nist.gov/vuln/detail/CVE-2026-77316) | High | 7.1 | Flyto2 Core is an execution kernel for automation and AI-agent workflows. Prior to 2.26.8, validate_url_ssrf() in src/c… |
| 2026-11-19 22:19:56 | [CVE-2026-95517](https://nvd.nist.gov/vuln/detail/CVE-2026-95517) |  |  | Reliance on obfuscation or encryption of Security-Relevant inputs without integrity checking, Improper validation of in… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
