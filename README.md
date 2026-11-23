# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-11-23 23:20 UTC

New CVEs published between 2026-11-23 22:18 UTC and 2026-11-23 23:20 UTC.

[Full CSV](data/new-cves-2026-11-23T23-20-48-53822Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-11-23 22:19:04 | [CVE-2026-113824](https://nvd.nist.gov/vuln/detail/CVE-2026-113824) | Critical | 9.1 | Authorization bypass through user-controlled key in Microsoft Clarity allows an unauthorized attacker to elevate privil… |
| 2026-11-23 22:19:11 | [CVE-2026-115296](https://nvd.nist.gov/vuln/detail/CVE-2026-115296) | Medium | 6.5 | Missing authorization in Kibana Security AI Assistant conversation deletion can allow an authenticated assistant user t… |
| 2026-11-23 22:19:30 | [CVE-2026-118285](https://nvd.nist.gov/vuln/detail/CVE-2026-118285) | Critical | 9.6 | Server-side request forgery in Azure Machine Learning allows an authorized attacker to elevate privileges over a networ… |
| 2026-11-23 22:19:30 | [CVE-2026-118286](https://nvd.nist.gov/vuln/detail/CVE-2026-118286) | Critical | 9.1 | Improper access control in Azure Site Recovery allows an unauthorized attacker to elevate privileges over a network. |
| 2026-11-23 22:19:55 | [CVE-2026-120777](https://nvd.nist.gov/vuln/detail/CVE-2026-120777) | High | 7.1 | Incorrect authorization in Azure Managed Service Identity allows an authorized attacker to elevate privileges over a ne… |
| 2026-11-23 22:19:56 | [CVE-2026-120787](https://nvd.nist.gov/vuln/detail/CVE-2026-120787) | High | 7.5 | Improper certificate validation in Microsoft Office PowerPoint allows an unauthorized attacker to execute code over a n… |
| 2026-11-23 22:20:10 | [CVE-2026-129837](https://nvd.nist.gov/vuln/detail/CVE-2026-129837) | High | 7.5 | A flaw was found in rsyslog. A remote, unauthenticated attacker can cause a Denial of Service (DoS) by sending a specia… |
| 2026-11-23 22:20:10 | [CVE-2026-130165](https://nvd.nist.gov/vuln/detail/CVE-2026-130165) | High | 8.2 | React is a JavaScript library for building user interfaces. In versions prior to 19.0.9, 19.1.10, 19.2.9 and 19.3.1, re… |
| 2026-11-23 22:20:12 | [CVE-2026-132615](https://nvd.nist.gov/vuln/detail/CVE-2026-132615) |  |  | The ggml-rpc server suffers from an uninitialized heap memory disclosure vulnerability where the alloc_buffer function… |
| 2026-11-23 22:20:12 | [CVE-2026-133981](https://nvd.nist.gov/vuln/detail/CVE-2026-133981) | Medium | 6.5 | An issue was discovered in Elasticsearch where specially crafted compressed payloads can cause an infinite loop. A low-… |
| 2026-11-23 22:20:12 | [CVE-2026-134069](https://nvd.nist.gov/vuln/detail/CVE-2026-134069) | High | 8.2 | Use of a default cryptographic key in the instance registration component in Amazon SSM Agent before 3.3.5226.0 on AWS-… |
| 2026-11-23 22:20:16 | [CVE-2026-50691](https://nvd.nist.gov/vuln/detail/CVE-2026-50691) | Critical | 9.9 | Improper authorization in M365 Copilot allows an authorized attacker to elevate privileges over a network. |
| 2026-11-23 22:20:39 | [CVE-2026-62841](https://nvd.nist.gov/vuln/detail/CVE-2026-62841) | Critical | 10.0 | Improper authentication in Azure Event Grid allows an unauthorized attacker to elevate privileges over a network. |
| 2026-11-23 22:20:52 | [CVE-2026-65817](https://nvd.nist.gov/vuln/detail/CVE-2026-65817) | High | 8.3 | Improper neutralization of special elements used in an os command ('os command injection') in Azure Managed Instance fo… |
| 2026-11-23 22:21:30 | [CVE-2026-69437](https://nvd.nist.gov/vuln/detail/CVE-2026-69437) | High | 8.6 | Missing authorization in Azure AI Foundry allows an unauthorized attacker to disclose information over a network. |
| 2026-11-23 22:22:11 | [CVE-2026-69899](https://nvd.nist.gov/vuln/detail/CVE-2026-69899) | Critical | 9.1 | Authentication bypass by spoofing in Azure DevTest Labs allows an unauthorized attacker to perform spoofing over a netw… |
| 2026-11-23 22:22:36 | [CVE-2026-70193](https://nvd.nist.gov/vuln/detail/CVE-2026-70193) | Critical | 9.9 | Improper limitation of a pathname to a restricted directory ('path traversal') in Microsoft Office SharePoint allows an… |
| 2026-11-23 22:22:50 | [CVE-2026-70305](https://nvd.nist.gov/vuln/detail/CVE-2026-70305) | Critical | 9.6 | Improper neutralization of input during web page generation ('cross-site scripting') in Azure Portal allows an unauthor… |
| 2026-11-23 22:23:40 | [CVE-2026-81962](https://nvd.nist.gov/vuln/detail/CVE-2026-81962) | High | 8.6 | Incorrect authorization in Azure Machine Learning allows an unauthorized attacker to disclose information over a networ… |
| 2026-11-23 22:23:40 | [CVE-2026-82979](https://nvd.nist.gov/vuln/detail/CVE-2026-82979) | High | 7.1 | SQL injection in WHMCS could allow an authenticated client with View & Manage Contacts permission to retrieve other cli… |
| 2026-11-23 22:23:40 | [CVE-2026-82981](https://nvd.nist.gov/vuln/detail/CVE-2026-82981) | High | 8.7 | SQL injection in WHMCS could allow an unauthenticated user to retrieve clients' personal and support information, as we… |
| 2026-11-23 22:24:54 | [CVE-2026-93700](https://nvd.nist.gov/vuln/detail/CVE-2026-93700) | Critical | 9.0 | An authenticated WHMCS client could potentially leverage this flaw to read sensitive configuration files on the WHMCS h… |
| 2026-11-23 23:17:01 | [CVE-2026-101862](https://nvd.nist.gov/vuln/detail/CVE-2026-101862) | High | 8.7 | EUSurvey through 1.6, prior to commit 0669a36, contains a path traversal vulnerability in the survey import function th… |
| 2026-11-23 23:17:01 | [CVE-2026-101863](https://nvd.nist.gov/vuln/detail/CVE-2026-101863) | High | 8.7 | EUSurvey 1.5.5 through 1.6, prior to commit d5295d5, contains a missing authorization vulnerability in the POST /forms/… |
| 2026-11-23 23:17:01 | [CVE-2026-101864](https://nvd.nist.gov/vuln/detail/CVE-2026-101864) | Critical | 9.2 | EUSurvey through 1.6, prior to commit a4161a9, contains a weak password recovery mechanism that allows attackers who ob… |
| 2026-11-23 23:17:01 | [CVE-2026-101866](https://nvd.nist.gov/vuln/detail/CVE-2026-101866) | High | 8.8 | EUSurvey through 1.6, prior to commit 118facd, contains an authorization bypass vulnerability in the public POST /runne… |
| 2026-11-23 23:17:01 | [CVE-2026-101867](https://nvd.nist.gov/vuln/detail/CVE-2026-101867) | High | 8.6 | EUSurvey through 1.6, prior to commit edb5021, contains an incorrect authorization vulnerability in the GET /settings/s… |
| 2026-11-23 23:17:01 | [CVE-2026-101868](https://nvd.nist.gov/vuln/detail/CVE-2026-101868) | High | 8.7 | EUSurvey through 1.6, prior to commit 4bf95a3, contains an authorization bypass vulnerability in the GET /preparepublis… |
| 2026-11-23 23:17:01 | [CVE-2026-101869](https://nvd.nist.gov/vuln/detail/CVE-2026-101869) | High | 8.7 | EUSurvey 1.4.4.6738 through 1.6, prior to commit de1145c, contains an SQL injection vulnerability in the public results… |
| 2026-11-23 23:17:02 | [CVE-2026-101870](https://nvd.nist.gov/vuln/detail/CVE-2026-101870) | High | 8.7 | EUSurvey through 1.6, prior to commit de1145c, contains an authorization bypass vulnerability in the public POST /editc… |
| 2026-11-23 23:17:02 | [CVE-2026-101871](https://nvd.nist.gov/vuln/detail/CVE-2026-101871) | High | 8.7 | EUSurvey 1.5.2 through 1.6, prior to commit ffd5da7, contains a missing authorization vulnerability in the public POST… |
| 2026-11-23 23:17:02 | [CVE-2026-101872](https://nvd.nist.gov/vuln/detail/CVE-2026-101872) | High | 7.1 | EUSurvey through 1.6, prior to commit 4bf95a3, contains a blind SQL injection vulnerability in the GET /dashboard/surve… |
| 2026-11-23 23:17:02 | [CVE-2026-101873](https://nvd.nist.gov/vuln/detail/CVE-2026-101873) | Medium | 5.3 | EUSurvey 1.5.2 through 1.6, prior to commit bb7432c, contains a stored cross-site scripting vulnerability in Delphi sur… |
| 2026-11-23 23:17:02 | [CVE-2026-101874](https://nvd.nist.gov/vuln/detail/CVE-2026-101874) | Medium | 5.3 | EUSurvey through 1.6, prior to commit 6db6147, contains an insecure direct object reference vulnerability in the GET /e… |
| 2026-11-23 23:17:02 | [CVE-2026-101876](https://nvd.nist.gov/vuln/detail/CVE-2026-101876) | Medium | 5.3 | EUSurvey through 1.6, prior to commit 03cc974, contains a blind server-side request forgery vulnerability in PDF export… |
| 2026-11-23 23:17:02 | [CVE-2026-101877](https://nvd.nist.gov/vuln/detail/CVE-2026-101877) | Medium | 5.3 | EUSurvey through 1.6, prior to commit 4ff1ba0, contains a missing authorization vulnerability in the GET /pdf/survey/{s… |
| 2026-11-23 23:17:03 | [CVE-2026-122090](https://nvd.nist.gov/vuln/detail/CVE-2026-122090) | High | 8.4 | Pelican 4.12.0 contains an OS command injection vulnerability in pelican-import. An attacker-controlled wp:post_name fr… |
| 2026-11-23 23:17:03 | [CVE-2026-130166](https://nvd.nist.gov/vuln/detail/CVE-2026-130166) | High | 7.7 | n8n is an open source workflow automation platform. Prior to 1.123.90 and 2.14.0, the invitation acceptance endpoint ac… |
| 2026-11-23 23:17:04 | [CVE-2026-130167](https://nvd.nist.gov/vuln/detail/CVE-2026-130167) | High | 7.5 | n8n is an open source workflow automation platform. Prior to 2.47.6, 2.48.3, and 3.2.2, the password reset link and rol… |
| 2026-11-23 23:17:04 | [CVE-2026-130169](https://nvd.nist.gov/vuln/detail/CVE-2026-130169) | Critical | 10.0 | AutoGPT is a workflow automation platform for creating, deploying, and managing continuous artificial intelligence agen… |
| 2026-11-23 23:17:04 | [CVE-2026-132257](https://nvd.nist.gov/vuln/detail/CVE-2026-132257) | High | 8.2 | AutoGPT is a workflow automation platform for creating, deploying, and managing continuous artificial intelligence agen… |
| 2026-11-23 23:17:04 | [CVE-2026-133455](https://nvd.nist.gov/vuln/detail/CVE-2026-133455) | Medium | 6.5 | AutoGPT is a workflow automation platform for creating, deploying, and managing continuous artificial intelligence agen… |
| 2026-11-23 23:17:04 | [CVE-2026-133930](https://nvd.nist.gov/vuln/detail/CVE-2026-133930) | Medium | 5.3 | A pooled-buffer lifetime error in Elasticsearch ES\|QL Arrow response formatting can disclose data from other users' con… |
| 2026-11-23 23:17:04 | [CVE-2026-134020](https://nvd.nist.gov/vuln/detail/CVE-2026-134020) | Medium | 6.5 | OpenEMR is a free and open source electronic health records and medical practice management application. Prior to 8.5.0… |
| 2026-11-23 23:17:04 | [CVE-2026-134021](https://nvd.nist.gov/vuln/detail/CVE-2026-134021) | High | 7.5 | TastyIgniter is an open-source online ordering, table reservation, and restaurant management system. Prior to 4.3.1, th… |
| 2026-11-23 23:17:05 | [CVE-2026-134022](https://nvd.nist.gov/vuln/detail/CVE-2026-134022) | Low | 3.7 | TastyIgniter is an open-source online ordering, table reservation, and restaurant management system. Prior to 4.2.0, th… |
| 2026-11-23 23:17:05 | [CVE-2026-134023](https://nvd.nist.gov/vuln/detail/CVE-2026-134023) | High | 7.4 | TastyIgniter is an open-source online ordering, table reservation, and restaurant management system. Prior to 4.2.0, ch… |
| 2026-11-23 23:17:05 | [CVE-2026-134024](https://nvd.nist.gov/vuln/detail/CVE-2026-134024) | Medium | 6.8 | TastyIgniter is an open-source online ordering, table reservation, and restaurant management system. Prior to 4.4.4, ad… |
| 2026-11-23 23:17:05 | [CVE-2026-135415](https://nvd.nist.gov/vuln/detail/CVE-2026-135415) | Low | 2.1 | A flaw has been found in MiniMax up to 0.7.2. Affected is the function authorizedLocalScript of the file bash-checker.t… |
| 2026-11-23 23:17:05 | [CVE-2026-135416](https://nvd.nist.gov/vuln/detail/CVE-2026-135416) | Medium | 5.5 | A vulnerability has been found in D-Link DIR-600L 2.17b02. Affected by this vulnerability is the function hedwigcgi_mai… |
| 2026-11-23 23:17:05 | [CVE-2026-135418](https://nvd.nist.gov/vuln/detail/CVE-2026-135418) | Low | 2.1 | A vulnerability was found in jprocms up to 1.7.7. Affected by this issue is the function DbBackupFileServiceImpl.downlo… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
