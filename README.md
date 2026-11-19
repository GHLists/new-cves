# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-11-19 18:20 UTC

New CVEs published between 2026-11-19 17:18 UTC and 2026-11-19 18:20 UTC.

[Full CSV](data/new-cves-2026-11-19T18-20-08-109878Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-11-19 17:18:51 | [CVE-2026-133276](https://nvd.nist.gov/vuln/detail/CVE-2026-133276) | Medium | 6.3 | When extra data is allowed (extra=Extra.allow), providing a __pydantic_initialised__ key when validating a Pydantic V1… |
| 2026-11-19 17:18:51 | [CVE-2026-133303](https://nvd.nist.gov/vuln/detail/CVE-2026-133303) | Critical | 9.0 | A vulnerability in the Audio, Web, and Video Conferencing (AWV) component of Mitel MiCollab through 10.3 (10.3.0.18) co… |
| 2026-11-19 17:18:51 | [CVE-2026-133305](https://nvd.nist.gov/vuln/detail/CVE-2026-133305) | Low | 2.3 | sqlmap before 1.10.11.89 contains a credential exposure vulnerability that allows attackers to capture user-supplied Co… |
| 2026-11-19 17:18:51 | [CVE-2026-133306](https://nvd.nist.gov/vuln/detail/CVE-2026-133306) | High | 8.5 | VideoLAN libaacs 0.7.0 through 0.12.0 contains a stack-based buffer overflow vulnerability in aacs_resolve_path() that… |
| 2026-11-19 17:18:52 | [CVE-2026-133307](https://nvd.nist.gov/vuln/detail/CVE-2026-133307) | High | 8.7 | ClassiCube before 1.4.0 contains a heap-based out-of-bounds write vulnerability in Png_Decode in src/Bitmap.c that allo… |
| 2026-11-19 17:18:52 | [CVE-2026-133308](https://nvd.nist.gov/vuln/detail/CVE-2026-133308) | Medium | 5.3 | ClassiCube before 1.4.0 contains a heap-based out-of-bounds write vulnerability in Png_Reconstruct in src/Bitmap.c that… |
| 2026-11-19 17:18:52 | [CVE-2026-133309](https://nvd.nist.gov/vuln/detail/CVE-2026-133309) | High | 8.5 | @scalar/typebox before 0.1.4 contains a code injection vulnerability in TypeCompiler that allows attackers to execute J… |
| 2026-11-19 17:18:52 | [CVE-2026-133310](https://nvd.nist.gov/vuln/detail/CVE-2026-133310) | Critical | 9.2 | Wing FTP Server before 8.2.8 contains a file mask bypass vulnerability allowing attackers to upload restricted files vi… |
| 2026-11-19 17:18:52 | [CVE-2026-133311](https://nvd.nist.gov/vuln/detail/CVE-2026-133311) | Medium | 5.9 | A vulnerability in the Audio, Web, and Video Conferencing (AWV) component of Mitel MiCollab through 10.3 (10.3.0.18) co… |
| 2026-11-19 17:18:52 | [CVE-2026-133323](https://nvd.nist.gov/vuln/detail/CVE-2026-133323) | Critical | 10.0 | A vulnerability in the Audio, Web, and Video Conferencing (AWV) component of Mitel MiCollab through 10.3 (10.3.0.18) co… |
| 2026-11-19 17:18:53 | [CVE-2026-133324](https://nvd.nist.gov/vuln/detail/CVE-2026-133324) | Medium | 5.3 | A vulnerability in the Audio, Web, and Video Conferencing (AWV) component of Mitel MiCollab through 10.3 (10.3.0.18) co… |
| 2026-11-19 17:18:55 | [CVE-2026-22309](https://nvd.nist.gov/vuln/detail/CVE-2026-22309) | High | 8.6 | The visitor tracking of JTL-Shop automatically registers unknown crawler user agents without filtering the value, and t… |
| 2026-11-19 17:18:55 | [CVE-2026-22310](https://nvd.nist.gov/vuln/detail/CVE-2026-22310) | High | 7.6 | When the setting for saving requests to non-existent pages (404) is enabled, JTL-Shop stores the raw requested URL in i… |
| 2026-11-19 17:18:58 | [CVE-2026-47278](https://nvd.nist.gov/vuln/detail/CVE-2026-47278) | Medium | 6.9 | Frappe is a full-stack web application framework. Prior to 15.108.0 and 16.18.3, the add_comment handler in frappe/temp… |
| 2026-11-19 17:18:58 | [CVE-2026-59988](https://nvd.nist.gov/vuln/detail/CVE-2026-59988) | High | 8.2 | django-docutils provides reStructuredText support for Django. Prior to 0.30.0, public rendering paths including publish… |
| 2026-11-19 17:18:58 | [CVE-2026-69260](https://nvd.nist.gov/vuln/detail/CVE-2026-69260) | High | 7.6 | Git LFS is a Git extension for versioning large files. From 0.5.0 until 3.8.1, Git LFS does not format the SSH URL path… |
| 2026-11-19 17:18:58 | [CVE-2026-69261](https://nvd.nist.gov/vuln/detail/CVE-2026-69261) | High | 7.6 | Git LFS is a Git extension for versioning large files. From 0.5.0 until 3.8.1, Git LFS may forward a Cookie header afte… |
| 2026-11-19 17:18:59 | [CVE-2026-77318](https://nvd.nist.gov/vuln/detail/CVE-2026-77318) | High | 7.3 | Jupyter MCP Server is a Model Context Protocol server for Jupyter. Prior to 1.0.3, standalone streamable-http mode can… |
| 2026-11-19 17:18:59 | [CVE-2026-77336](https://nvd.nist.gov/vuln/detail/CVE-2026-77336) | Medium | 5.3 | Aperi'Solve is an open-source steganalysis web platform. Prior to 3.4.2, an unauthenticated user can submit a PNG to PO… |
| 2026-11-19 17:18:59 | [CVE-2026-77338](https://nvd.nist.gov/vuln/detail/CVE-2026-77338) | Critical | 9.3 | Sprout Track is a self-hosted baby tracking application. Prior to 1.3.5, Sprout Track uses a publicly known hardcoded s… |
| 2026-11-19 17:18:59 | [CVE-2026-77359](https://nvd.nist.gov/vuln/detail/CVE-2026-77359) | Critical | 9.3 | Jupyter MCP Server is a Model Context Protocol server for Jupyter. Prior to 1.0.3, standalone streamable-http mode vali… |
| 2026-11-19 17:18:59 | [CVE-2026-77367](https://nvd.nist.gov/vuln/detail/CVE-2026-77367) | Critical | 9.4 | Daptin is a GraphQL/JSON-API headless CMS. Prior to 0.12.30, the generic GET /api/{entity} list endpoint accepts attack… |
| 2026-11-19 17:18:59 | [CVE-2026-77369](https://nvd.nist.gov/vuln/detail/CVE-2026-77369) | Critical | 9.6 | Daptin is a GraphQL/JSON-API headless CMS. From 0.11.4 until 0.12.30, the generic GET /yjs/:documentName WebSocket rout… |
| 2026-11-19 17:19:00 | [CVE-2026-77376](https://nvd.nist.gov/vuln/detail/CVE-2026-77376) | Medium | 6.1 | Bolt is a fully open source, adaptable platform for building and running modern websites. Prior to 6.1.4, LoginFormAuth… |
| 2026-11-19 17:19:00 | [CVE-2026-77377](https://nvd.nist.gov/vuln/detail/CVE-2026-77377) | Medium | 5.2 | Bolt is a fully open source, adaptable platform for building and running modern websites. Prior to 6.1.4, the authentic… |
| 2026-11-19 17:19:00 | [CVE-2026-77378](https://nvd.nist.gov/vuln/detail/CVE-2026-77378) | Medium | 6.5 | Bolt is a fully open source, adaptable platform for building and running modern websites. Prior to 6.1.4, SQL injection… |
| 2026-11-19 17:19:00 | [CVE-2026-77379](https://nvd.nist.gov/vuln/detail/CVE-2026-77379) | Medium | 5.3 | Bolt is a fully open source, adaptable platform for building and running modern websites. Prior to 6.1.4, the public Re… |
| 2026-11-19 17:19:00 | [CVE-2026-77380](https://nvd.nist.gov/vuln/detail/CVE-2026-77380) | Medium | 5.2 | Bolt is a fully open source, adaptable platform for building and running modern websites. Prior to 6.1.5, the /bolt/asy… |
| 2026-11-19 17:19:00 | [CVE-2026-77382](https://nvd.nist.gov/vuln/detail/CVE-2026-77382) | Medium | 5.9 | falcon-rust is a Rust implementation of the Falcon post-quantum signature scheme. Prior to 0.2.0, the discrete-Gaussian… |
| 2026-11-19 18:18:03 | [CVE-2026-115515](https://nvd.nist.gov/vuln/detail/CVE-2026-115515) | Medium | 5.3 | @fastify/static is the Fastify plugin for serving static files. In versions before 10.1.8, the allowedPath guard receiv… |
| 2026-11-19 18:18:03 | [CVE-2026-117659](https://nvd.nist.gov/vuln/detail/CVE-2026-117659) | High | 8.5 | The InfoScan Electron desktop client improperly handles TLS certificate errors by accepting certificates without valida… |
| 2026-11-19 18:18:03 | [CVE-2026-120157](https://nvd.nist.gov/vuln/detail/CVE-2026-120157) | Medium | 6.9 | The publicly distributed InfoScan Electron installer contains configuration files identifying hostnames associated with… |
| 2026-11-19 18:18:03 | [CVE-2026-120255](https://nvd.nist.gov/vuln/detail/CVE-2026-120255) | Medium | 5.1 | InfoScan uses hard-coded cryptographic keys and initialization-vector values in its database-encryption implementation.… |
| 2026-11-19 18:18:03 | [CVE-2026-120260](https://nvd.nist.gov/vuln/detail/CVE-2026-120260) | Medium | 6.8 | InfoScan does not enforce authentication on an endpoint used to retrieve sales-automation templates. A local attacker c… |
| 2026-11-19 18:18:03 | [CVE-2026-120271](https://nvd.nist.gov/vuln/detail/CVE-2026-120271) | Medium | 6.9 | InfoScan contains an unauthenticated information disclosure vulnerability in its mobile-enumeration and version-reporti… |
| 2026-11-19 18:18:04 | [CVE-2026-120298](https://nvd.nist.gov/vuln/detail/CVE-2026-120298) | Medium | 6.9 | InfoScan fails to properly handle certain malformed or incomplete requests to its login and password-reset endpoints. T… |
| 2026-11-19 18:18:05 | [CVE-2026-128135](https://nvd.nist.gov/vuln/detail/CVE-2026-128135) | High | 7.1 | NLTK (Natural Language Toolkit) is a suite of open source Python modules, data sets, and tutorials supporting research… |
| 2026-11-19 18:18:05 | [CVE-2026-128136](https://nvd.nist.gov/vuln/detail/CVE-2026-128136) | Medium | 6.1 | NLTK (Natural Language Toolkit) is a suite of open source Python modules, data sets, and tutorials supporting research… |
| 2026-11-19 18:18:06 | [CVE-2026-128138](https://nvd.nist.gov/vuln/detail/CVE-2026-128138) | Critical | 9.8 | NLTK (Natural Language Toolkit) is a suite of open source Python modules, data sets, and tutorials supporting research… |
| 2026-11-19 18:18:06 | [CVE-2026-128139](https://nvd.nist.gov/vuln/detail/CVE-2026-128139) | High | 7.5 | NLTK (Natural Language Toolkit) is a suite of open source Python modules, data sets, and tutorials supporting research… |
| 2026-11-19 18:18:06 | [CVE-2026-128140](https://nvd.nist.gov/vuln/detail/CVE-2026-128140) | Medium | 6.5 | NLTK (Natural Language Toolkit) is a suite of open source Python modules, data sets, and tutorials supporting research… |
| 2026-11-19 18:18:06 | [CVE-2026-128978](https://nvd.nist.gov/vuln/detail/CVE-2026-128978) | Medium | 6.0 | Improper certificate validation vulnerability in Estonian Information System Authority (RIA) libdigidocpp, Estonian Inf… |
| 2026-11-19 18:18:06 | [CVE-2026-129221](https://nvd.nist.gov/vuln/detail/CVE-2026-129221) | Medium | 5.4 | NLTK (Natural Language Toolkit) is a suite of open source Python modules, data sets, and tutorials supporting research… |
| 2026-11-19 18:18:07 | [CVE-2026-129222](https://nvd.nist.gov/vuln/detail/CVE-2026-129222) | High | 7.5 | NLTK (Natural Language Toolkit) is a suite of open source Python modules, data sets, and tutorials supporting research… |
| 2026-11-19 18:18:07 | [CVE-2026-129223](https://nvd.nist.gov/vuln/detail/CVE-2026-129223) | High | 7.5 | NLTK (Natural Language Toolkit) is a suite of open source Python modules, data sets, and tutorials supporting research… |
| 2026-11-19 18:18:07 | [CVE-2026-129225](https://nvd.nist.gov/vuln/detail/CVE-2026-129225) | Medium | 5.3 | NLTK (Natural Language Toolkit) is a suite of open source Python modules, data sets, and tutorials supporting research… |
| 2026-11-19 18:18:07 | [CVE-2026-129226](https://nvd.nist.gov/vuln/detail/CVE-2026-129226) | Medium | 5.3 | NLTK (Natural Language Toolkit) is a suite of open source Python modules, data sets, and tutorials supporting research… |
| 2026-11-19 18:18:07 | [CVE-2026-129227](https://nvd.nist.gov/vuln/detail/CVE-2026-129227) | Medium | 5.3 | NLTK (Natural Language Toolkit) is a suite of open source Python modules, data sets, and tutorials supporting research… |
| 2026-11-19 18:18:07 | [CVE-2026-129229](https://nvd.nist.gov/vuln/detail/CVE-2026-129229) | High | 7.5 | NLTK (Natural Language Toolkit) is a suite of open source Python modules, data sets, and tutorials supporting research… |
| 2026-11-19 18:18:08 | [CVE-2026-129230](https://nvd.nist.gov/vuln/detail/CVE-2026-129230) | Medium | 5.5 | NLTK (Natural Language Toolkit) is a suite of open source Python modules, data sets, and tutorials supporting research… |
| 2026-11-19 18:18:08 | [CVE-2026-129231](https://nvd.nist.gov/vuln/detail/CVE-2026-129231) | Medium | 5.3 | NLTK (Natural Language Toolkit) is a suite of open source Python modules, data sets, and tutorials supporting research… |
| 2026-11-19 18:18:08 | [CVE-2026-129233](https://nvd.nist.gov/vuln/detail/CVE-2026-129233) | Medium | 5.3 | NLTK (Natural Language Toolkit) is a suite of open source Python modules, data sets, and tutorials supporting research… |
| 2026-11-19 18:18:08 | [CVE-2026-129399](https://nvd.nist.gov/vuln/detail/CVE-2026-129399) | Medium | 5.1 | Joomla Extension - vi-solutions - Missing core.create check in form creation in Visforms extension 1.0.0-5.6.3, 6.0.0-6… |
| 2026-11-19 18:18:09 | [CVE-2026-129403](https://nvd.nist.gov/vuln/detail/CVE-2026-129403) | Medium | 6.3 | Joomla Extension - vi-solutions - Missing access check in reload task in Visforms extension 1.0.0-5.6.4, 6.0.0-6.2.1 -… |
| 2026-11-19 18:18:09 | [CVE-2026-129405](https://nvd.nist.gov/vuln/detail/CVE-2026-129405) | Medium | 6.3 | Joomla Extension - vi-solutions - Predictable and reusable email verification codes in Visforms extension 1.0.0-5.6.4,… |
| 2026-11-19 18:18:09 | [CVE-2026-129406](https://nvd.nist.gov/vuln/detail/CVE-2026-129406) | Medium | 6.3 | Joomla Extension - vi-solutions - Verification mail rate limit reset in Visforms extension 1.0.0-5.6.4, 6.0.0-6.2.1 - T… |
| 2026-11-19 18:18:09 | [CVE-2026-129407](https://nvd.nist.gov/vuln/detail/CVE-2026-129407) | Medium | 5.1 | Joomla Extension - vi-solutions - Missing authorization and CSRF checks in reset and check-in tasks in Visforms extensi… |
| 2026-11-19 18:18:09 | [CVE-2026-129408](https://nvd.nist.gov/vuln/detail/CVE-2026-129408) | Low | 2.3 | Joomla Extension - vi-solutions - Stored XSS via SQL field labels in Visforms extension 1.0.0-5.6.4, 6.0.0-6.2.1 - Labe… |
| 2026-11-19 18:18:10 | [CVE-2026-129412](https://nvd.nist.gov/vuln/detail/CVE-2026-129412) | High | 8.6 | Joomla Extension - vi-solutions - SQL injection in backend data search and export in Visforms extension 1.0.0-5.6.4, 6.… |
| 2026-11-19 18:18:10 | [CVE-2026-129414](https://nvd.nist.gov/vuln/detail/CVE-2026-129414) | Medium | 5.1 | Joomla Extension - vi-solutions - Improper per-form authorization for field management in Visforms extension 1.0.0-5.6.… |
| 2026-11-19 18:18:10 | [CVE-2026-129415](https://nvd.nist.gov/vuln/detail/CVE-2026-129415) | Medium | 5.1 | Joomla Extension - vi-solutions - Missing core.create check in example data generation and BreezingForms import in Visf… |
| 2026-11-19 18:18:10 | [CVE-2026-130811](https://nvd.nist.gov/vuln/detail/CVE-2026-130811) | Medium | 5.3 | @fastify/static is the Fastify plugin for serving static files. In versions up to and including 10.1.11, when it is con… |
| 2026-11-19 18:18:13 | [CVE-2026-133221](https://nvd.nist.gov/vuln/detail/CVE-2026-133221) | Medium | 5.4 | A flaw was found in Keycloak. An authenticated remote user with a pending required security action, such as configuring… |
| 2026-11-19 18:18:13 | [CVE-2026-22308](https://nvd.nist.gov/vuln/detail/CVE-2026-22308) | High | 8.6 | The preview mode of the OPC (OnPage Composer) page builder of JTL-Shop is activated by a request parameter alone and re… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
