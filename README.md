# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-11-05 14:19 UTC

New CVEs published between 2026-11-05 13:21 UTC and 2026-11-05 14:19 UTC.

[Full CSV](data/new-cves-2026-11-05T14-19-41-524964Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-11-05 14:16:58 | [CVE-2026-100168](https://nvd.nist.gov/vuln/detail/CVE-2026-100168) |  |  | Direct Request ('Forced Browsing') in the Content Manager component in Apache OFBiz 24.09.07 on all platforms allows an… |
| 2026-11-05 14:16:58 | [CVE-2026-100228](https://nvd.nist.gov/vuln/detail/CVE-2026-100228) |  |  | Improper Input Validation in Order Returns in Apache OFBiz 24.09.07 on all platforms allows an authenticated user witho… |
| 2026-11-05 14:16:59 | [CVE-2026-104720](https://nvd.nist.gov/vuln/detail/CVE-2026-104720) | High | 7.5 | Improper Limitation of a Pathname to a Restricted Directory ('Path Traversal') vulnerability in Kobikom Telecommunicati… |
| 2026-11-05 14:16:59 | [CVE-2026-105321](https://nvd.nist.gov/vuln/detail/CVE-2026-105321) | High | 7.5 | Improper neutralization of special elements used in an SQL command ('SQL injection') vulnerability in Kobikom Telecommu… |
| 2026-11-05 14:16:59 | [CVE-2026-105325](https://nvd.nist.gov/vuln/detail/CVE-2026-105325) |  |  | Missing check for ACCOUNTING_UPDATE / ACCOUNTING_CREATE in accounting in allows user with only ACCOUNTING_VIEW permissi… |
| 2026-11-05 14:16:59 | [CVE-2026-105330](https://nvd.nist.gov/vuln/detail/CVE-2026-105330) |  |  | Use of Hard-coded Cryptographic Key in JWT token authentication in Apache OFBiz 24.09.06 and 24.09.07 on all platforms… |
| 2026-11-05 14:16:59 | [CVE-2026-105461](https://nvd.nist.gov/vuln/detail/CVE-2026-105461) |  |  | Missing check for ORDERMGR_UPDATE in ordermgr allows user with only ORDERMGR_VIEW permission to update orders. Affected… |
| 2026-11-05 14:16:59 | [CVE-2026-107912](https://nvd.nist.gov/vuln/detail/CVE-2026-107912) | High | 7.7 | A flaw was found in the management interface of the Quarkus framework, specifically within the quarkus-vertx-http compo… |
| 2026-11-05 14:16:59 | [CVE-2026-109129](https://nvd.nist.gov/vuln/detail/CVE-2026-109129) |  |  | Authorization Bypass Through User-Controlled Key in the Order Manager component in Apache OFBiz 24.09.07 on all platfor… |
| 2026-11-05 14:17:00 | [CVE-2026-109837](https://nvd.nist.gov/vuln/detail/CVE-2026-109837) |  |  | Authorization Bypass Through User-Controlled Key in Order Returns in Apache OFBiz 24.09 before 24.09.08 on all platform… |
| 2026-11-05 14:17:00 | [CVE-2026-109856](https://nvd.nist.gov/vuln/detail/CVE-2026-109856) |  |  | Direct Request ('Forced Browsing') to Financial Account services in Apache OFBiz 24.09 before 24.09.08 on all platforms… |
| 2026-11-05 14:17:00 | [CVE-2026-109928](https://nvd.nist.gov/vuln/detail/CVE-2026-109928) |  |  | Incorrect Implementation of Authentication Algorithm in the password-reset and login JWT validation in Apache OFBiz 24.… |
| 2026-11-05 14:17:00 | [CVE-2026-114229](https://nvd.nist.gov/vuln/detail/CVE-2026-114229) |  |  | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') in the Catalog image viewer in Apa… |
| 2026-11-05 14:17:00 | [CVE-2026-114233](https://nvd.nist.gov/vuln/detail/CVE-2026-114233) |  |  | Incorrect Privilege Assignment in the Order Manager in Apache OFBiz 24.09 before 24.09.08 on all platforms allows an au… |
| 2026-11-05 14:17:00 | [CVE-2026-114235](https://nvd.nist.gov/vuln/detail/CVE-2026-114235) |  |  | Direct Request ('Forced Browsing') in the Order component in Apache OFBiz 24.09 before 24.09.08 on all platforms allows… |
| 2026-11-05 14:17:00 | [CVE-2026-114271](https://nvd.nist.gov/vuln/detail/CVE-2026-114271) |  |  | Authorization Bypass Through User-Controlled Key in the shopping list services in Apache OFBiz 24.09 before 24.09.08 on… |
| 2026-11-05 14:17:01 | [CVE-2026-114272](https://nvd.nist.gov/vuln/detail/CVE-2026-114272) |  |  | Authorization Bypass Through User-Controlled Key in the content viewing component in Apache OFBiz 24.09 before 24.09.08… |
| 2026-11-05 14:17:01 | [CVE-2026-114277](https://nvd.nist.gov/vuln/detail/CVE-2026-114277) |  |  | Authentication bypass by Assumed-Immutable data vulnerability in Apache OFBiz. Apache OFBiz's optional Janrain Engage S… |
| 2026-11-05 14:17:01 | [CVE-2026-117691](https://nvd.nist.gov/vuln/detail/CVE-2026-117691) | Critical | 9.1 | A flaw was found in the SAML HTTP-Redirect binding implementation of Keycloak. The issue occurs because the server proc… |
| 2026-11-05 14:17:04 | [CVE-2026-123022](https://nvd.nist.gov/vuln/detail/CVE-2026-123022) | Medium | 5.5 | A vulnerability was detected in agentscope-ai AgentScope up to 2.0.11. The impacted element is the function subprocess.… |
| 2026-11-05 14:17:04 | [CVE-2026-123023](https://nvd.nist.gov/vuln/detail/CVE-2026-123023) | Medium | 5.5 | A flaw has been found in agentscope-ai AgentScope up to 2.0.8. This affects the function check_permissions of the file… |
| 2026-11-05 14:17:04 | [CVE-2026-123024](https://nvd.nist.gov/vuln/detail/CVE-2026-123024) | Medium | 5.5 | A vulnerability has been found in agentscope-ai AgentScope up to 2.0.11. This impacts the function get_current_user_id… |
| 2026-11-05 14:17:04 | [CVE-2026-123028](https://nvd.nist.gov/vuln/detail/CVE-2026-123028) | Medium | 5.5 | A vulnerability was identified in itsourcecode Online Book Store 1.0. Affected by this issue is some unknown functional… |
| 2026-11-05 14:17:04 | [CVE-2026-123059](https://nvd.nist.gov/vuln/detail/CVE-2026-123059) | High | 7.5 | In Eclipse BaSyx Helm Charts version 2.2.0 of the `aas-basyx-v2-full` chart, deployments with the bundled Keycloak enab… |
| 2026-11-05 14:17:05 | [CVE-2026-76563](https://nvd.nist.gov/vuln/detail/CVE-2026-76563) | Medium | 6.1 | Improper neutralization of Script-Related HTML tags in a web page (basic XSS) vulnerability in Fileorbis Informatics Se… |
| 2026-11-05 14:17:05 | [CVE-2026-82902](https://nvd.nist.gov/vuln/detail/CVE-2026-82902) |  |  | Server-Side Request Forgery in ViewDataFile in Apache OFBiz 24.09 before 24.09.08 on all platforms allows a remote auth… |
| 2026-11-05 14:17:05 | [CVE-2026-82904](https://nvd.nist.gov/vuln/detail/CVE-2026-82904) |  |  | Uncontrolled Resource Consumption in ServiceMultiEventHandler in Apache OFBiz 24.09 before 24.09.08 on all platforms al… |
| 2026-11-05 14:17:05 | [CVE-2026-82907](https://nvd.nist.gov/vuln/detail/CVE-2026-82907) |  |  | Authentication Bypass by Capture-replay in ExternalLoginKeysManager in Apache OFBiz 24.09 before 24.09.08 on all platfo… |
| 2026-11-05 14:17:05 | [CVE-2026-82910](https://nvd.nist.gov/vuln/detail/CVE-2026-82910) |  |  | Improper Neutralization of Special Elements Used in a Template Engine ('Server-Side Template Injection') in MacroScreen… |
| 2026-11-05 14:17:06 | [CVE-2026-82912](https://nvd.nist.gov/vuln/detail/CVE-2026-82912) |  |  | Improper Neutralization of Special Elements Used in an Expression Language Statement ('Expression Language Injection')… |
| 2026-11-05 14:17:06 | [CVE-2026-82916](https://nvd.nist.gov/vuln/detail/CVE-2026-82916) |  |  | Missing Authorization in XmlDsDump in Apache OFBiz 24.09 before 24.09.08 on all platforms allows a remote authenticated… |
| 2026-11-05 14:17:06 | [CVE-2026-82960](https://nvd.nist.gov/vuln/detail/CVE-2026-82960) |  |  | Improper Control of Generation of Code ('Code Injection') in ModelFormField in the Apache OFBiz cms plugin before 24.09… |
| 2026-11-05 14:17:06 | [CVE-2026-83538](https://nvd.nist.gov/vuln/detail/CVE-2026-83538) |  |  | Missing Authorization in Apache OFBiz 24.09 before 24.09.08 on all platforms allows a remote unauthenticated attacker t… |
| 2026-11-05 14:17:06 | [CVE-2026-83542](https://nvd.nist.gov/vuln/detail/CVE-2026-83542) |  |  | Improper Control of Generation of Code ('Code Injection') in Apache OFBiz 24.09 before 24.09.08 on all platforms allows… |
| 2026-11-05 14:17:06 | [CVE-2026-84183](https://nvd.nist.gov/vuln/detail/CVE-2026-84183) |  |  | Incorrect Authorization in the updateLayout simple-method in applications/content/minilang/layout/LayoutEvents.xml in A… |
| 2026-11-05 14:17:07 | [CVE-2026-84728](https://nvd.nist.gov/vuln/detail/CVE-2026-84728) |  |  | Incorrect Authorization in Apache OFBiz 24.09 before 24.09.08 on all platforms, when documented multitenancy is enabled… |
| 2026-11-05 14:17:07 | [CVE-2026-85627](https://nvd.nist.gov/vuln/detail/CVE-2026-85627) |  |  | Improper Neutralization of Special Elements Used in a Template Engine ('Server-Side Template Injection') in Apache OFBi… |
| 2026-11-05 14:17:07 | [CVE-2026-92887](https://nvd.nist.gov/vuln/detail/CVE-2026-92887) |  |  | Incorrect default value in the REST API framework's .rest.xml definition parser (ModelApiReader) in Apache OFBiz throug… |
| 2026-11-05 14:17:07 | [CVE-2026-97355](https://nvd.nist.gov/vuln/detail/CVE-2026-97355) |  |  | Use of Hard-coded Password vulnerability in the AdminServer component in Apache OFBiz 24.09.07 on all platforms allows… |
| 2026-11-05 14:17:07 | [CVE-2026-97356](https://nvd.nist.gov/vuln/detail/CVE-2026-97356) |  |  | External Control of File Name or Path vulnerability in the ViewFile component of Label Manager in Apache OFBiz 24.09.07… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
