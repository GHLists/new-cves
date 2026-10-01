# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-01 20:18 UTC

New CVEs published between 2026-10-01 19:18 UTC and 2026-10-01 20:18 UTC.

[Full CSV](data/new-cves-2026-10-01T20-18-53-04341Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-10-01 20:17:20 | [CVE-2026-100251](https://nvd.nist.gov/vuln/detail/CVE-2026-100251) | Medium | 6.9 | Wormhole.app as deployed before 2026-08-22 misconfigures the coturn TURN server and does not properly restrict TCP rela… |
| 2026-10-01 20:17:21 | [CVE-2026-102628](https://nvd.nist.gov/vuln/detail/CVE-2026-102628) | Critical | 9.2 | The Cadmos LTI application hosted at cadmos.eummena.io had Laravel debug mode enabled (APP_DEBUG=true, APP_ENV=local) i… |
| 2026-10-01 20:17:21 | [CVE-2026-102666](https://nvd.nist.gov/vuln/detail/CVE-2026-102666) | Medium | 6.9 | The Joyland AI app contains hard-coded credentials for the GeTui push notification service, allowing an attacker to acc… |
| 2026-10-01 20:17:21 | [CVE-2026-102667](https://nvd.nist.gov/vuln/detail/CVE-2026-102667) | Critical | 9.0 | Joyland AI app allows an attacker with shared network access to inject JavaScript into content loaded in WebView. Witho… |
| 2026-10-01 20:17:21 | [CVE-2026-102668](https://nvd.nist.gov/vuln/detail/CVE-2026-102668) | Medium | 6.9 | The Joyland AI app accepts any TLS certificates from any server without validation. |
| 2026-10-01 20:17:22 | [CVE-2026-102669](https://nvd.nist.gov/vuln/detail/CVE-2026-102669) | Medium | 6.9 | Joyland AI app does not verify hostnames, allowing a malicious host to connect or intercept chat messages. |
| 2026-10-01 20:17:22 | [CVE-2026-102670](https://nvd.nist.gov/vuln/detail/CVE-2026-102670) | Medium | 5.3 | Joyland AI app explicitly permits cleartext HTTP traffic on Android 9+ where the default is to block it. |
| 2026-10-01 20:17:22 | [CVE-2026-102671](https://nvd.nist.gov/vuln/detail/CVE-2026-102671) | Medium | 6.9 | The Joyland AI app accepts invalid SSL certificates in the invisible advertisement WebView by default. |
| 2026-10-01 20:17:23 | [CVE-2026-103484](https://nvd.nist.gov/vuln/detail/CVE-2026-103484) | High | 8.8 | IVFFlat index build in pgvector before 0.8.7 allows a database user to write data out-of-bounds, which can lead to arbi… |
| 2026-10-01 20:17:24 | [CVE-2026-104286](https://nvd.nist.gov/vuln/detail/CVE-2026-104286) | Critical | 9.8 | An improper limitation of a pathname to a restricted directory ('path traversal') vulnerability in Fortinet FortiMail 8… |
| 2026-10-01 20:17:24 | [CVE-2026-14983](https://nvd.nist.gov/vuln/detail/CVE-2026-14983) | High | 7.1 | Missing authentication in the web interface in Teledyne FLIR Aware2 versions through 6.9.0.2 allows remote unauthentica… |
| 2026-10-01 20:17:24 | [CVE-2026-14984](https://nvd.nist.gov/vuln/detail/CVE-2026-14984) | Critical | 9.4 | Cleartext transmission in the primary control endpoints of Teledyne FLIR Aware2 versions through 6.9.0.2 allows remote… |
| 2026-10-01 20:17:25 | [CVE-2026-53953](https://nvd.nist.gov/vuln/detail/CVE-2026-53953) | Critical | 9.1 | GetSimple CMS is a content management system (CMS), and GetSimple CMS CE is the community edition of that CMS. In versi… |
| 2026-10-01 20:17:25 | [CVE-2026-53964](https://nvd.nist.gov/vuln/detail/CVE-2026-53964) | High | 7.2 | Document Merge Service is a document template merge service providing an API to manage templates and merge them with gi… |
| 2026-10-01 20:17:25 | [CVE-2026-54049](https://nvd.nist.gov/vuln/detail/CVE-2026-54049) | High | 8.7 | Sakai is a Collaboration and Learning Environment (CLE). From versions 23.0 to before 23.5, and versions 25.0 to before… |
| 2026-10-01 20:17:25 | [CVE-2026-55251](https://nvd.nist.gov/vuln/detail/CVE-2026-55251) | Medium | 6.5 | NetBox Device Type Library is a collection of community-sourced device type definitions for import into NetBox. Prior t… |
| 2026-10-01 20:17:26 | [CVE-2026-55252](https://nvd.nist.gov/vuln/detail/CVE-2026-55252) | Medium | 5.1 | OpenRun is an open-source, self-hosted GitOps platform for deploying web apps and internal tools to Docker or Kubernete… |
| 2026-10-01 20:17:26 | [CVE-2026-56660](https://nvd.nist.gov/vuln/detail/CVE-2026-56660) | Critical | 9.1 | GetSimple CMS is a content management system (CMS), and GetSimple CMS CE is the community edition of that CMS. Prior to… |
| 2026-10-01 20:17:26 | [CVE-2026-56661](https://nvd.nist.gov/vuln/detail/CVE-2026-56661) | High | 7.5 | GetSimple CMS is a content management system (CMS), and GetSimple CMS CE is the community edition of that CMS. Prior to… |
| 2026-10-01 20:17:26 | [CVE-2026-56662](https://nvd.nist.gov/vuln/detail/CVE-2026-56662) | Critical | 9.6 | GetSimple CMS is a content management system (CMS), and GetSimple CMS CE is the community edition of that CMS. Prior to… |
| 2026-10-01 20:17:29 | [CVE-2026-70650](https://nvd.nist.gov/vuln/detail/CVE-2026-70650) | High | 8.8 | GetSimple CMS is a content management system (CMS), and GetSimple CMS CE is the community edition of that CMS. In versi… |
| 2026-10-01 20:17:29 | [CVE-2026-71426](https://nvd.nist.gov/vuln/detail/CVE-2026-71426) | High | 7.1 | GetSimple CMS is a content management system (CMS), and GetSimple CMS CE is the community edition of that CMS. In versi… |
| 2026-10-01 20:17:29 | [CVE-2026-71542](https://nvd.nist.gov/vuln/detail/CVE-2026-71542) | High | 8.7 | GetSimple CMS is a content management system (CMS), and GetSimple CMS CE is the community edition of that CMS. In versi… |
| 2026-10-01 20:17:32 | [CVE-2026-82357](https://nvd.nist.gov/vuln/detail/CVE-2026-82357) | High | 7.1 | RT-Labs AB C-Open CANopen contains a NULL pointer dereference if the LSS protocol is used to configure the device. An o… |
| 2026-10-01 20:17:32 | [CVE-2026-82358](https://nvd.nist.gov/vuln/detail/CVE-2026-82358) | High | 7.1 | RT-Labs AB C-Open CANopen contains a write protection bypass in the SDO (Service Data Object) server implementation 'sr… |
| 2026-10-01 20:17:32 | [CVE-2026-93832](https://nvd.nist.gov/vuln/detail/CVE-2026-93832) | Medium | 4.8 | A component of one of the Motorola system applications was exported without permission, allowing for the revocation of… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
