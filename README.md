# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-13 01:18 UTC

New CVEs published between 2026-10-13 00:18 UTC and 2026-10-13 01:18 UTC.

[Full CSV](data/new-cves-2026-10-13T01-18-53-595517Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-10-13 01:16:42 | [CVE-2026-108942](https://nvd.nist.gov/vuln/detail/CVE-2026-108942) | Medium | 5.1 | A security flaw has been discovered in philz1337x clarity-upscaler up to cfbdb842c6c839c8e97741722b8cf9a4b7662d98. This… |
| 2026-10-13 01:16:42 | [CVE-2026-108943](https://nvd.nist.gov/vuln/detail/CVE-2026-108943) | Low | 1.9 | A weakness has been identified in ModelTC LightX2V up to 0.5.0. Affected is the function AutoTokenizer.from_pretrained… |
| 2026-10-13 01:16:42 | [CVE-2026-108944](https://nvd.nist.gov/vuln/detail/CVE-2026-108944) | Low | 2.4 | A security vulnerability has been detected in repository RAE up to a4d18c4db766419cbe7cb8c02cd9f7ceb0ec9041. Affected b… |
| 2026-10-13 01:16:42 | [CVE-2026-108945](https://nvd.nist.gov/vuln/detail/CVE-2026-108945) | Medium | 4.8 | A vulnerability was detected in iMoonLab yolov13 up to 73289949533efac82bb5f72ec19b746618656bd2. Affected by this issue… |
| 2026-10-13 01:16:46 | [CVE-2026-58242](https://nvd.nist.gov/vuln/detail/CVE-2026-58242) | Low | 3.5 | SAP Cloud Connector contains an improper authorization check, which could be exploited by a low-privileged attacker thr… |
| 2026-10-13 01:16:46 | [CVE-2026-58249](https://nvd.nist.gov/vuln/detail/CVE-2026-58249) | High | 7.5 | SAP NetWeaver and SAP Web Dispatcher do not properly validate certain fields in specially crafted requests handled by a… |
| 2026-10-13 01:16:46 | [CVE-2026-76972](https://nvd.nist.gov/vuln/detail/CVE-2026-76972) | Medium | 6.5 | Due to a Cross-Site Scripting (XSS) vulnerability in SAP Manufacturing Integration and Intelligence, an attacker could… |
| 2026-10-13 01:16:46 | [CVE-2026-76975](https://nvd.nist.gov/vuln/detail/CVE-2026-76975) | Medium | 6.1 | Due to a DOM-Based Cross-Site Scripting (XSS) vulnerability, an unauthenticated attacker could generate a malicious lin… |
| 2026-10-13 01:16:46 | [CVE-2026-76976](https://nvd.nist.gov/vuln/detail/CVE-2026-76976) | Medium | 5.4 | Applications based on SAP GUI for HTML in SAP NetWeaver Application Server ABAP do not sufficiently sanitize user-suppl… |
| 2026-10-13 01:16:47 | [CVE-2026-87689](https://nvd.nist.gov/vuln/detail/CVE-2026-87689) | Critical | 9.8 | The Metasploit Framework Web Service REST API (msf-ws) exposes the credential store through Msf::WebServices::Credentia… |
| 2026-10-13 01:16:47 | [CVE-2026-89105](https://nvd.nist.gov/vuln/detail/CVE-2026-89105) | Medium | 4.2 | The HybridTokenAuthenticator component of the SAP/cloud-security-services-integration-library accepts tokens from unint… |
| 2026-10-13 01:16:47 | [CVE-2026-89106](https://nvd.nist.gov/vuln/detail/CVE-2026-89106) | Medium | 4.4 | SAP UI5 does not perform sufficient input validation under certain configurations. An attacker with low privileges coul… |
| 2026-10-13 01:16:47 | [CVE-2026-89107](https://nvd.nist.gov/vuln/detail/CVE-2026-89107) | Critical | 9.9 | SAP S/4HANA (Manage Substitution/Validation Rules) does not sufficiently validate input processed by rule definition fu… |
| 2026-10-13 01:16:47 | [CVE-2026-89108](https://nvd.nist.gov/vuln/detail/CVE-2026-89108) | Critical | 9.1 | SAP Manufacturing Integration and Intelligence does not sufficiently enforce authorization boundaries within certain ad… |
| 2026-10-13 01:16:47 | [CVE-2026-89110](https://nvd.nist.gov/vuln/detail/CVE-2026-89110) | Critical | 9.9 | SAP NetWeaver Visual Composer does not perform sufficient authorization checks in certain portal functionality. An atta… |
| 2026-10-13 01:16:47 | [CVE-2026-89111](https://nvd.nist.gov/vuln/detail/CVE-2026-89111) | Critical | 10.0 | The SAP Cloud SDK for Python contains an OAuth2 SSRF vulnerability affecting multi-tenant BTP applications. An attacker… |
| 2026-10-13 01:16:48 | [CVE-2026-89112](https://nvd.nist.gov/vuln/detail/CVE-2026-89112) | Medium | 6.5 | The admin API endpoint used to retrieve CLA signature records does not consistently enforce the required authorization… |
| 2026-10-13 01:16:48 | [CVE-2026-89113](https://nvd.nist.gov/vuln/detail/CVE-2026-89113) | High | 8.8 | SAP Commerce Cloud does not sufficiently validate certain user-supplied input before it is incorporated into a database… |
| 2026-10-13 01:16:48 | [CVE-2026-89116](https://nvd.nist.gov/vuln/detail/CVE-2026-89116) | Medium | 5.9 | The affected code used child_process.execSync with a shell string for generator installation and uninstallation. This a… |
| 2026-10-13 01:16:48 | [CVE-2026-89117](https://nvd.nist.gov/vuln/detail/CVE-2026-89117) | Medium | 6.1 | SAP NetWeaver Enterprise Portal allows an unauthenticated attacker to inject malicious scripts into a URL parameter. Th… |
| 2026-10-13 01:16:48 | [CVE-2026-89118](https://nvd.nist.gov/vuln/detail/CVE-2026-89118) | Medium | 5.3 | SAP NetWeaver Enterprise Portal allows an unauthenticated attacker to access restricted resources and retrieve non-crit… |
| 2026-10-13 01:16:48 | [CVE-2026-89120](https://nvd.nist.gov/vuln/detail/CVE-2026-89120) | High | 7.1 | A regression caused by an API change in SAP ABAP Platform reintroduces a previously fixed authorization weakness. The s… |
| 2026-10-13 01:16:48 | [CVE-2026-89121](https://nvd.nist.gov/vuln/detail/CVE-2026-89121) | Medium | 4.7 | SAP S/4HANA does not perform sufficient instance-level authorization checks for certain modification operations on asso… |
| 2026-10-13 01:16:49 | [CVE-2026-89122](https://nvd.nist.gov/vuln/detail/CVE-2026-89122) | Medium | 6.1 | SAP NetWeaver Enterprise Portal does not sufficiently validate input to a certain portal component. An unauthenticated… |
| 2026-10-13 01:16:49 | [CVE-2026-89124](https://nvd.nist.gov/vuln/detail/CVE-2026-89124) | Medium | 4.3 | Display Product Catalog Based on Customs Declaration application does not perform sufficient authorization checks withi… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
