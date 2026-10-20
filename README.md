# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-20 11:20 UTC

New CVEs published between 2026-10-20 10:20 UTC and 2026-10-20 11:20 UTC.

[Full CSV](data/new-cves-2026-10-20T11-20-16-364347Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-10-20 11:17:15 | [CVE-2026-107597](https://nvd.nist.gov/vuln/detail/CVE-2026-107597) | Medium | 5.1 | PIA's token verification (`verify_token` in `pia/oidc.py`) fetches the OIDC discovery document of an allowlisted issuer… |
| 2026-10-20 11:17:16 | [CVE-2026-108062](https://nvd.nist.gov/vuln/detail/CVE-2026-108062) | Medium | 6.9 | Pre-authentication OIDC discovery and JWKS fetches run synchronously on the asyncio event loop, so one unauthenticated… |
| 2026-10-20 11:17:16 | [CVE-2026-108086](https://nvd.nist.gov/vuln/detail/CVE-2026-108086) |  |  | ** UNSUPPORTED WHEN ASSIGNED ** Improper restriction of recursive entity references in DTDs ('XML entity expansion') vu… |
| 2026-10-20 11:17:16 | [CVE-2026-108087](https://nvd.nist.gov/vuln/detail/CVE-2026-108087) |  |  | ** UNSUPPORTED WHEN ASSIGNED ** Improper neutralization of special elements used in an SQL command ('SQL injection') vu… |
| 2026-10-20 11:17:16 | [CVE-2026-108088](https://nvd.nist.gov/vuln/detail/CVE-2026-108088) |  |  | ** UNSUPPORTED WHEN ASSIGNED ** Use of cache containing sensitive information vulnerability in Apache Cocoon. When usin… |
| 2026-10-20 11:17:17 | [CVE-2026-108089](https://nvd.nist.gov/vuln/detail/CVE-2026-108089) |  |  | ** UNSUPPORTED WHEN ASSIGNED ** Exposure of sensitive system information to an unauthorized control sphere vulnerabilit… |
| 2026-10-20 11:17:18 | [CVE-2026-112783](https://nvd.nist.gov/vuln/detail/CVE-2026-112783) | Medium | 5.3 | OpenCATS before 0.10.0 contains a missing authorization vulnerability in ajax/deleteActivity.php and ajax/editActivity.… |
| 2026-10-20 11:17:18 | [CVE-2026-112784](https://nvd.nist.gov/vuln/detail/CVE-2026-112784) | Medium | 5.3 | OpenCATS before 0.10.0 contains a missing authorization vulnerability in ajax/testEmailSettings.php that allows any aut… |
| 2026-10-20 11:17:18 | [CVE-2026-112785](https://nvd.nist.gov/vuln/detail/CVE-2026-112785) | Medium | 5.3 | OpenCATS before 0.10.0 contains a missing authorization vulnerability that allows READ-level users to create, rename, d… |
| 2026-10-20 11:17:18 | [CVE-2026-112786](https://nvd.nist.gov/vuln/detail/CVE-2026-112786) | Medium | 5.3 | OpenCATS before 0.10.0 contains a missing authorization vulnerability in ImportUI::handleRequest() that allows low-priv… |
| 2026-10-20 11:17:18 | [CVE-2026-112787](https://nvd.nist.gov/vuln/detail/CVE-2026-112787) | Medium | 5.3 | OpenCATS before 0.10.0 contains a missing authorization vulnerability in ReportsUI::handleRequest() that allows authent… |
| 2026-10-20 11:17:19 | [CVE-2026-113349](https://nvd.nist.gov/vuln/detail/CVE-2026-113349) | Medium | 5.3 | OpenCATS before 0.10.0 contains a missing authorization vulnerability in CalendarUI::onEditEvent() and onDeleteEvent()… |
| 2026-10-20 11:17:19 | [CVE-2026-113350](https://nvd.nist.gov/vuln/detail/CVE-2026-113350) | Medium | 5.1 | react-admin before 5.15.5 contains a stored cross-site scripting vulnerability that allows attackers to inject scripts… |
| 2026-10-20 11:17:19 | [CVE-2026-113351](https://nvd.nist.gov/vuln/detail/CVE-2026-113351) | High | 8.2 | libexpat 2.7.2 through 2.9.0 contains a denial of service vulnerability because XML_ParserReset zeroes the direct byte… |
| 2026-10-20 11:17:19 | [CVE-2026-113352](https://nvd.nist.gov/vuln/detail/CVE-2026-113352) | High | 7.7 | uTox through 0.18.1 contains a path traversal vulnerability that allows Tox friends to write arbitrary files by sending… |
| 2026-10-20 11:17:19 | [CVE-2026-113353](https://nvd.nist.gov/vuln/detail/CVE-2026-113353) | Medium | 5.3 | LearnPress before 4.4.10 contains a missing authorization vulnerability in the admin_course_editor, admin_quiz_editor a… |
| 2026-10-20 11:17:19 | [CVE-2026-113354](https://nvd.nist.gov/vuln/detail/CVE-2026-113354) | High | 7.1 | Dockhand before 1.0.46 contains an arbitrary file read vulnerability that allows non-admin users with stacks:edit permi… |
| 2026-10-20 11:17:19 | [CVE-2026-113355](https://nvd.nist.gov/vuln/detail/CVE-2026-113355) | Medium | 4.8 | Chatwoot before 4.14.0 contains a stored cross-site scripting vulnerability that allows account administrators to injec… |
| 2026-10-20 11:17:20 | [CVE-2026-113356](https://nvd.nist.gov/vuln/detail/CVE-2026-113356) | High | 7.7 | DokuWiki before 2026-07-14c contains a PHP object injection vulnerability in Draft::getDraftText() that passes draft fi… |
| 2026-10-20 11:17:20 | [CVE-2026-113357](https://nvd.nist.gov/vuln/detail/CVE-2026-113357) | Medium | 5.1 | @e2e-dev/github before 0.4.1 contains an improper authorization vulnerability that allows pull request commenters to hi… |
| 2026-10-20 11:17:20 | [CVE-2026-113358](https://nvd.nist.gov/vuln/detail/CVE-2026-113358) | High | 8.7 | LavaLite CMS through 10.1.2 contains a missing authentication vulnerability in the Filer module that allows unauthentic… |
| 2026-10-20 11:17:20 | [CVE-2026-113382](https://nvd.nist.gov/vuln/detail/CVE-2026-113382) | Low | 2.1 | A security vulnerability has been detected in arizu-id fast-tunnel 1.0.0. Affected by this issue is the function ZipArc… |
| 2026-10-20 11:17:20 | [CVE-2026-113383](https://nvd.nist.gov/vuln/detail/CVE-2026-113383) | Low | 2.1 | A vulnerability was detected in Optimal IdM OptimalCloud 5.0. This affects an unknown part of the file /v5.0/webapps/pa… |
| 2026-10-20 11:17:20 | [CVE-2026-113384](https://nvd.nist.gov/vuln/detail/CVE-2026-113384) | Low | 2.1 | A flaw has been found in Optimal IdM OptimalCloud 5.0. This vulnerability affects unknown code of the file /v5.0/social… |
| 2026-10-20 11:17:35 | [CVE-2026-9589](https://nvd.nist.gov/vuln/detail/CVE-2026-9589) | Critical | 9.3 | Missing authorization in the configuration cascade operations of the Collaboration Server in Unblu inc. Unblu Spark 7.0… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
