# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-09-25 19:19 UTC

New CVEs published between 2026-09-25 18:19 UTC and 2026-09-25 19:19 UTC.

[Full CSV](data/new-cves-2026-09-25T19-19-15-138504Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-09-25 19:16:49 | [CVE-2026-100192](https://nvd.nist.gov/vuln/detail/CVE-2026-100192) | Medium | 6.9 | X-SpringBoot through 6.0 exposes appKey and appSecret credentials in the GET /application/manager/select endpoint witho… |
| 2026-09-25 19:16:50 | [CVE-2026-100303](https://nvd.nist.gov/vuln/detail/CVE-2026-100303) | Medium | 5.3 | TDuck survey form through 6.0 lacks authorization checks on FormThemeController write endpoints for global form themes… |
| 2026-09-25 19:16:50 | [CVE-2026-100304](https://nvd.nist.gov/vuln/detail/CVE-2026-100304) | Medium | 6.0 | TDuck survey form 6.0 contains an information disclosure vulnerability in FormAuthUtils.hasPermission that fails open w… |
| 2026-09-25 19:16:50 | [CVE-2026-100305](https://nvd.nist.gov/vuln/detail/CVE-2026-100305) | Medium | 5.3 | TDuck survey form through 6.0 fails to enforce form fill-in restrictions on the authenticated submission endpoint POST… |
| 2026-09-25 19:16:51 | [CVE-2026-100306](https://nvd.nist.gov/vuln/detail/CVE-2026-100306) | Medium | 6.9 | TDuck survey form through 6.0 fails to validate write passwords on submission endpoints, enforcing the check only on th… |
| 2026-09-25 19:16:53 | [CVE-2026-45801](https://nvd.nist.gov/vuln/detail/CVE-2026-45801) | Medium | 5.3 | GLPI is a free asset and IT management software package. From 0.72 until 10.0.26 and 11.0.8, an authenticated user with… |
| 2026-09-25 19:16:54 | [CVE-2026-47679](https://nvd.nist.gov/vuln/detail/CVE-2026-47679) | High | 8.5 | GLPI is a free asset and IT management software package. From 10.0.0 until 10.0.26 and 11.0.8, any logged-in GLPI user… |
| 2026-09-25 19:16:55 | [CVE-2026-48482](https://nvd.nist.gov/vuln/detail/CVE-2026-48482) | Critical | 9.4 | GLPI is a free asset and IT management software package. From 11.0.0 until 11.0.8, a form administrator can use Form im… |
| 2026-09-25 19:16:58 | [CVE-2026-49469](https://nvd.nist.gov/vuln/detail/CVE-2026-49469) | Medium | 4.6 | GLPI is a free asset and IT management software package. From 0.70 until 10.0.26 and 11.0.8, an authenticated hotliner… |
| 2026-09-25 19:16:58 | [CVE-2026-49470](https://nvd.nist.gov/vuln/detail/CVE-2026-49470) | High | 7.7 | GLPI is a free asset and IT management software package. From 11.0.0 until 11.0.8, the time-based one-time password ver… |
| 2026-09-25 19:17:27 | [CVE-2026-53610](https://nvd.nist.gov/vuln/detail/CVE-2026-53610) | High | 7.5 | GLPI is a free asset and IT management software package. From 11.0.0 until 11.0.8, an attacker can craft a URL for a da… |
| 2026-09-25 19:17:27 | [CVE-2026-53625](https://nvd.nist.gov/vuln/detail/CVE-2026-53625) | High | 7.5 | GLPI is a free asset and IT management software package. From 0.70 until 10.0.26 and 11.0.8, a technician can manipulat… |
| 2026-09-25 19:17:27 | [CVE-2026-53626](https://nvd.nist.gov/vuln/detail/CVE-2026-53626) | High | 7.1 | GLPI is a free asset and IT management software package. From 11.0.5 until 11.0.8, under certain conditions, permission… |
| 2026-09-25 19:17:27 | [CVE-2026-53627](https://nvd.nist.gov/vuln/detail/CVE-2026-53627) | Medium | 6.0 | GLPI is a free asset and IT management software package. From 11.0.0 until 11.0.8, a low-privileged authenticated user… |
| 2026-09-25 19:17:28 | [CVE-2026-53628](https://nvd.nist.gov/vuln/detail/CVE-2026-53628) | Medium | 5.9 | GLPI is a free asset and IT management software package. From 0.84 until 10.0.26 and 11.0.8, an administrator holding t… |
| 2026-09-25 19:17:28 | [CVE-2026-53629](https://nvd.nist.gov/vuln/detail/CVE-2026-53629) | High | 7.1 | GLPI is a free asset and IT management software package. From 9.4.0 until 10.0.26 and 11.0.8, an attacker with the READ… |
| 2026-09-25 19:17:38 | [CVE-2026-55214](https://nvd.nist.gov/vuln/detail/CVE-2026-55214) | High | 8.5 | GLPI is a free asset and IT management software package. From 11.0.6 until 11.0.8, an authenticated technician can stor… |
| 2026-09-25 19:17:38 | [CVE-2026-55217](https://nvd.nist.gov/vuln/detail/CVE-2026-55217) | Medium | 5.3 | GLPI is a free asset and IT management software package. From 0.85 until 10.0.26 and 11.0.8, a low-privileged authentic… |
| 2026-09-25 19:17:53 | [CVE-2026-61855](https://nvd.nist.gov/vuln/detail/CVE-2026-61855) | Medium | 5.3 | Zammad is a web based open source helpdesk/customer support system. In 7.0.3 and 7.1.1, under certain conditions, Zamma… |
| 2026-09-25 19:17:54 | [CVE-2026-63006](https://nvd.nist.gov/vuln/detail/CVE-2026-63006) | Medium | 5.3 | Zammad is a web based open source helpdesk/customer support system. Prior to 7.1.2, attacker-controlled HTML in inbound… |
| 2026-09-25 19:17:54 | [CVE-2026-63204](https://nvd.nist.gov/vuln/detail/CVE-2026-63204) | Low | 2.3 | Zammad is a web based open source helpdesk/customer support system. Prior to 7.1.2, an authenticated user with agent pe… |
| 2026-09-25 19:17:54 | [CVE-2026-63205](https://nvd.nist.gov/vuln/detail/CVE-2026-63205) | Medium | 5.1 | Zammad is a web based open source helpdesk/customer support system. Prior to 7.1.2, when creating or updating an email… |
| 2026-09-25 19:17:54 | [CVE-2026-63206](https://nvd.nist.gov/vuln/detail/CVE-2026-63206) | Medium | 5.3 | Zammad is a web based open source helpdesk/customer support system. Prior to 7.1.2, zammad's HTML sanitizer, which bloc… |
| 2026-09-25 19:17:55 | [CVE-2026-63207](https://nvd.nist.gov/vuln/detail/CVE-2026-63207) | Medium | 6.9 | Zammad is a web based open source helpdesk/customer support system. In 7.0.3 and 7.1.1, an authenticated administrator… |
| 2026-09-25 19:17:55 | [CVE-2026-63208](https://nvd.nist.gov/vuln/detail/CVE-2026-63208) | Medium | 5.1 | Zammad is a web based open source helpdesk/customer support system. Prior to 7.1.2, when a Microsoft Graph request fail… |
| 2026-09-25 19:17:55 | [CVE-2026-63216](https://nvd.nist.gov/vuln/detail/CVE-2026-63216) | Medium | 5.3 | Zammad is a web based open source helpdesk/customer support system. Prior to 7.1.2, unsanitized option labels are rende… |
| 2026-09-25 19:17:57 | [CVE-2026-84458](https://nvd.nist.gov/vuln/detail/CVE-2026-84458) | Critical | 9.1 | Zammad is a web based open source helpdesk/customer support system. Prior to 7.1.2, when the "Automatic account link on… |
| 2026-09-25 19:17:57 | [CVE-2026-84460](https://nvd.nist.gov/vuln/detail/CVE-2026-84460) | Medium | 5.3 | Zammad is a web based open source helpdesk/customer support system. Prior to 7.1.2, any authenticated user can call the… |
| 2026-09-25 19:17:57 | [CVE-2026-84461](https://nvd.nist.gov/vuln/detail/CVE-2026-84461) | Medium | 6.9 | Zammad is a web based open source helpdesk/customer support system. Prior to 7.1.2, the two-factor login step let an at… |
| 2026-09-25 19:17:57 | [CVE-2026-84463](https://nvd.nist.gov/vuln/detail/CVE-2026-84463) | Medium | 6.3 | Zammad is a web based open source helpdesk/customer support system. Prior to 7.1.2, a user with Knowledge Base editing… |
| 2026-09-25 19:17:57 | [CVE-2026-84464](https://nvd.nist.gov/vuln/detail/CVE-2026-84464) | High | 7.1 | Zammad is a web based open source helpdesk/customer support system. Prior to 7.1.2, zammad's External Data Source featu… |
| 2026-09-25 19:17:58 | [CVE-2026-84465](https://nvd.nist.gov/vuln/detail/CVE-2026-84465) | High | 7.1 | Zammad is a web based open source helpdesk/customer support system. Prior to 7.1.2, when Zammad checks the digital sign… |
| 2026-09-25 19:17:59 | [CVE-2026-97060](https://nvd.nist.gov/vuln/detail/CVE-2026-97060) | High | 8.6 | X-SpringBoot through 6.0 lacks object-level authorization in user management endpoints, allowing sub-administrators to… |
| 2026-09-25 19:17:59 | [CVE-2026-97063](https://nvd.nist.gov/vuln/detail/CVE-2026-97063) | Critical | 9.3 | X-SpringBoot through 6.0 returns login verification codes in HTTP responses from unauthenticated endpoints GET /sys/mob… |
| 2026-09-25 19:17:59 | [CVE-2026-97064](https://nvd.nist.gov/vuln/detail/CVE-2026-97064) | Critical | 9.3 | X-SpringBoot through 6.0 ships with a hardcoded static master login verification code 172839 enabled by default in the… |
| 2026-09-25 19:17:59 | [CVE-2026-97895](https://nvd.nist.gov/vuln/detail/CVE-2026-97895) | Low | 2.1 | A vulnerability was determined in krayin laravel-crm up to 2.2.5. This affects an unknown part of the file packages/Web… |
| 2026-09-25 19:17:59 | [CVE-2026-97896](https://nvd.nist.gov/vuln/detail/CVE-2026-97896) | Low | 2.0 | A vulnerability was identified in krayin laravel-crm up to 2.2.5. This vulnerability affects the function Configuration… |
| 2026-09-25 19:18:00 | [CVE-2026-97897](https://nvd.nist.gov/vuln/detail/CVE-2026-97897) | Medium | 5.1 | A security flaw has been discovered in Krayin laravel-crm up to 2.2.5. This issue affects some unknown processing of th… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
