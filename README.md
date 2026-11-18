# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-11-18 13:19 UTC

New CVEs published between 2026-11-18 12:21 UTC and 2026-11-18 13:19 UTC.

[Full CSV](data/new-cves-2026-11-18T13-19-16-408761Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-11-18 13:17:23 | [CVE-2026-107517](https://nvd.nist.gov/vuln/detail/CVE-2026-107517) | Medium | 5.4 | Dell PowerStore contains a stored cross-site scripting (XSS) vulnerability. A low-privileged authenticated attacker cou… |
| 2026-11-18 13:17:23 | [CVE-2026-107518](https://nvd.nist.gov/vuln/detail/CVE-2026-107518) | High | 8.7 | Dell PowerStore contains a Server-Side Request Forgery (SSRF) vulnerability. An authenticated user with limited privile… |
| 2026-11-18 13:17:23 | [CVE-2026-107519](https://nvd.nist.gov/vuln/detail/CVE-2026-107519) | High | 8.1 | Dell PowerStore contains an integer underflow vulnerability. An attacker could exploit this vulnerability, potentially… |
| 2026-11-18 13:17:23 | [CVE-2026-109857](https://nvd.nist.gov/vuln/detail/CVE-2026-109857) | Critical | 9.2 | CAST Imaging is vulnerable to authentication bypass in the TenantFilter class. The TenantFilter processes the X-ISSUER-… |
| 2026-11-18 13:17:23 | [CVE-2026-109858](https://nvd.nist.gov/vuln/detail/CVE-2026-109858) | High | 8.3 | CAST Imaging has multiple path traversal vulnerabilities in various endpoints. The application does not properly valida… |
| 2026-11-18 13:17:23 | [CVE-2026-109859](https://nvd.nist.gov/vuln/detail/CVE-2026-109859) | Medium | 6.9 | CAST Imaging has a missing authentication vulnerability in the "/api/auth/keycloak/users/{username}" endpoint. An unaut… |
| 2026-11-18 13:17:24 | [CVE-2026-109860](https://nvd.nist.gov/vuln/detail/CVE-2026-109860) | High | 8.3 | CAST Imaging is vulnerable to Path Traversal vulnerability in "/api/server-folders" and "/api/server-folders/download"… |
| 2026-11-18 13:17:24 | [CVE-2026-109861](https://nvd.nist.gov/vuln/detail/CVE-2026-109861) | High | 8.7 | CAST Imaging contains a hardcoded authentication token in the "KeyCloakController" class of auth-service.jar. An attack… |
| 2026-11-18 13:17:24 | [CVE-2026-109862](https://nvd.nist.gov/vuln/detail/CVE-2026-109862) | Medium | 5.3 | CAST Imaging does not properly check whether a user is authorized to modify another user's notification settings in the… |
| 2026-11-18 13:17:24 | [CVE-2026-109863](https://nvd.nist.gov/vuln/detail/CVE-2026-109863) | Medium | 5.3 | CAST Imaging allows authenticated, low-privileged users to access parts of the administrator panel. When a user navigat… |
| 2026-11-18 13:17:24 | [CVE-2026-109864](https://nvd.nist.gov/vuln/detail/CVE-2026-109864) | Low | 2.3 | CAST Imaging has an access control flaw in the "/api/jobs/<uuid>/logs/download" endpoint. An authenticated low-privileg… |
| 2026-11-18 13:17:24 | [CVE-2026-113699](https://nvd.nist.gov/vuln/detail/CVE-2026-113699) | High | 7.2 | Improper neutralization of special elements used in an OS command ('OS command injection') vulnerability in Aidata Bili… |
| 2026-11-18 13:17:24 | [CVE-2026-125033](https://nvd.nist.gov/vuln/detail/CVE-2026-125033) | High | 7.2 | The Smash Balloon Social Post Feed – Simple Social Feeds for WordPress plugin for WordPress is vulnerable to Stored Cro… |
| 2026-11-18 13:17:25 | [CVE-2026-127142](https://nvd.nist.gov/vuln/detail/CVE-2026-127142) | High | 8.7 | LMS (Lan Management System) is vulnerable to Remote Code Execution via unrestricted upload of dangerous file types in t… |
| 2026-11-18 13:17:25 | [CVE-2026-127143](https://nvd.nist.gov/vuln/detail/CVE-2026-127143) | Critical | 9.4 | LMS (Lan Management System) is vulnerable to privilege escalation in the lmsd daemon. The daemon loads the libraries li… |
| 2026-11-18 13:17:26 | [CVE-2026-129961](https://nvd.nist.gov/vuln/detail/CVE-2026-129961) | Critical | 9.5 | LMS (Lan Management System) is vulnerable to Remote Code Execution in its e-mail-based Helpdesk ticket intake. The mail… |
| 2026-11-18 13:17:27 | [CVE-2026-130333](https://nvd.nist.gov/vuln/detail/CVE-2026-130333) | High | 7.2 | The SNORDIAN's H5PxAPIkatchu plugin for WordPress is vulnerable to Stored Cross-Site Scripting via the 'xapi' parameter… |
| 2026-11-18 13:17:27 | [CVE-2026-132121](https://nvd.nist.gov/vuln/detail/CVE-2026-132121) | High | 8.6 | Supergateway 2.4.0 through 4.2.2 contains a cross-site WebSocket hijacking vulnerability in stdio-to-WebSocket mode tha… |
| 2026-11-18 13:17:27 | [CVE-2026-132122](https://nvd.nist.gov/vuln/detail/CVE-2026-132122) | Medium | 5.7 | agentic-radar 0.7.0 before 0.14.2 contains an untrusted configuration loading vulnerability that allows malicious repos… |
| 2026-11-18 13:17:27 | [CVE-2026-132123](https://nvd.nist.gov/vuln/detail/CVE-2026-132123) | Medium | 4.8 | modified eCommerce Shopsoftware through 3.3.0 contains a stored cross-site scripting vulnerability that allows authenti… |
| 2026-11-18 13:17:27 | [CVE-2026-132124](https://nvd.nist.gov/vuln/detail/CVE-2026-132124) | Medium | 4.8 | modified eCommerce Shopsoftware through 3.3.0 contains a stored cross-site scripting vulnerability that allows authenti… |
| 2026-11-18 13:17:27 | [CVE-2026-132125](https://nvd.nist.gov/vuln/detail/CVE-2026-132125) | Low | 2.1 | Weblate 5.0 through 2026.11.2 contains a privilege escalation vulnerability where deleting a component list leaves stal… |
| 2026-11-18 13:17:28 | [CVE-2026-132126](https://nvd.nist.gov/vuln/detail/CVE-2026-132126) | Medium | 5.3 | Weblate 2026.6 through 2026.11.2 contains an information disclosure vulnerability that allows authenticated users to en… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
