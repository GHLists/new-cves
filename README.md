# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-11-10 01:19 UTC

New CVEs published between 2026-11-10 00:18 UTC and 2026-11-10 01:19 UTC.

[Full CSV](data/new-cves-2026-11-10T01-19-10-812498Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-11-10 01:17:10 | [CVE-2026-107240](https://nvd.nist.gov/vuln/detail/CVE-2026-107240) | High | 7.6 | The Node.js web service on VOS (previously Versa FlexVNF) is used for URL-based Zero Touch Provisioning (ZTP) of the VO… |
| 2026-11-10 01:17:12 | [CVE-2026-107241](https://nvd.nist.gov/vuln/detail/CVE-2026-107241) | High | 7.6 | The Node.js web service on VOS (previously Versa FlexVNF) is used for URL-based Zero Touch Provisioning (ZTP) of the VO… |
| 2026-11-10 01:17:12 | [CVE-2026-107242](https://nvd.nist.gov/vuln/detail/CVE-2026-107242) |  |  | The Node.js web service on VOS (previously Versa FlexVNF) is used for URL-based Zero Touch Provisioning (ZTP) of the VO… |
| 2026-11-10 01:17:12 | [CVE-2026-107243](https://nvd.nist.gov/vuln/detail/CVE-2026-107243) | High | 7.6 | The Node.js web service on VOS (previously Versa FlexVNF) is used for URL-based Zero Touch Provisioning (ZTP) of the VO… |
| 2026-11-10 01:17:12 | [CVE-2026-107244](https://nvd.nist.gov/vuln/detail/CVE-2026-107244) | High | 7.6 | The Node.js web service on VOS (previously Versa FlexVNF) is used for URL-based Zero Touch Provisioning (ZTP) of the VO… |
| 2026-11-10 01:17:12 | [CVE-2026-107245](https://nvd.nist.gov/vuln/detail/CVE-2026-107245) |  |  | Versa has confirmed a buffer overflow vulnerability in the IPsec implementation on VOS, aka Versa FlexVNF. Buffer Overf… |
| 2026-11-10 01:17:12 | [CVE-2026-107246](https://nvd.nist.gov/vuln/detail/CVE-2026-107246) | Critical | 9.2 | The Plesk extension "Site Import" before 1.13.2 does not properly validate domain and session identifiers, allowing pat… |
| 2026-11-10 01:17:13 | [CVE-2026-109793](https://nvd.nist.gov/vuln/detail/CVE-2026-109793) | High | 7.5 | SAP NetWeaver Application Server ABAP and SAP Web Dispatcher do not sufficiently validate certain header values process… |
| 2026-11-10 01:17:13 | [CVE-2026-109794](https://nvd.nist.gov/vuln/detail/CVE-2026-109794) | High | 7.5 | SAP NetWeaver Application Server ABAP, ABAP Platform, and SAP Web Dispatcher do not sufficiently handle resource consum… |
| 2026-11-10 01:17:13 | [CVE-2026-109795](https://nvd.nist.gov/vuln/detail/CVE-2026-109795) | Critical | 9.9 | SAP NetWeaver does not perform necessary authorization checks and lacks sufficient input validation in certain remote-e… |
| 2026-11-10 01:17:13 | [CVE-2026-109796](https://nvd.nist.gov/vuln/detail/CVE-2026-109796) | Medium | 4.3 | SAP NetWeaver Application Server ABAP and ABAP Platform does not properly initialize memory in certain internal compone… |
| 2026-11-10 01:17:13 | [CVE-2026-109797](https://nvd.nist.gov/vuln/detail/CVE-2026-109797) | High | 7.1 | In SAP/astonish, an authenticated user could potentially identify and operate on another team�s sandbox containers beca… |
| 2026-11-10 01:17:13 | [CVE-2026-109798](https://nvd.nist.gov/vuln/detail/CVE-2026-109798) | Critical | 9.1 | SAP BusinessObjects Business Intelligence Platform (Web Intelligence) does not properly restrict external entity resolu… |
| 2026-11-10 01:17:13 | [CVE-2026-109799](https://nvd.nist.gov/vuln/detail/CVE-2026-109799) | High | 7.5 | The SAP Cloud SDK for Python contains an improper cryptographic signature verification vulnerability (CWE-347) in IASCo… |
| 2026-11-10 01:17:14 | [CVE-2026-109800](https://nvd.nist.gov/vuln/detail/CVE-2026-109800) | High | 7.7 | SAP Web Dispatcher does not sufficiently validate certain inputs during processing, which could lead to memory corrupti… |
| 2026-11-10 01:17:14 | [CVE-2026-109801](https://nvd.nist.gov/vuln/detail/CVE-2026-109801) | Medium | 6.5 | SAP NetWeaver Application Server Java (NWDI Cockpit)� does not perform sufficient authorization checks for certain func… |
| 2026-11-10 01:17:14 | [CVE-2026-109802](https://nvd.nist.gov/vuln/detail/CVE-2026-109802) | Medium | 6.5 | SAP NetWeaver Application Server for ABAP does not properly validate certain input values. An authenticated user could… |
| 2026-11-10 01:17:14 | [CVE-2026-109803](https://nvd.nist.gov/vuln/detail/CVE-2026-109803) | Critical | 9.9 | SAP NetWeaver Knowledge Management (XML Forms) does not sufficiently restrict the selection of XSL transformations proc… |
| 2026-11-10 01:17:14 | [CVE-2026-109804](https://nvd.nist.gov/vuln/detail/CVE-2026-109804) | High | 7.5 | SAP Message Server does not properly handle certain malformed requests, which could be leveraged by an unauthenticated… |
| 2026-11-10 01:17:14 | [CVE-2026-109805](https://nvd.nist.gov/vuln/detail/CVE-2026-109805) | Medium | 6.4 | Due to a weak HMAC cryptography calculation when receiving an RFC callback in SAP NetWeaver and ABAP Platform (Applicat… |
| 2026-11-10 01:17:14 | [CVE-2026-109806](https://nvd.nist.gov/vuln/detail/CVE-2026-109806) | High | 7.5 | SAP NetWeaver (Internet Graphics Service) does not sufficiently validate certain input values within incoming requests.… |
| 2026-11-10 01:17:15 | [CVE-2026-109807](https://nvd.nist.gov/vuln/detail/CVE-2026-109807) | High | 7.5 | SAP NetWeaver (Internet Graphics Service) does not sufficiently validate certain input values within incoming requests.… |
| 2026-11-10 01:17:15 | [CVE-2026-109808](https://nvd.nist.gov/vuln/detail/CVE-2026-109808) | Low | 3.1 | Due to a missing authorization check in certain remote-enabled functionality, SAP Solution Tools Plug-In allows an auth… |
| 2026-11-10 01:17:15 | [CVE-2026-109809](https://nvd.nist.gov/vuln/detail/CVE-2026-109809) | Medium | 6.5 | SAP NetWeaver Application Server Java (NWDI Cockpit) does not perform sufficient authorization checks for certain funct… |
| 2026-11-10 01:17:15 | [CVE-2026-109810](https://nvd.nist.gov/vuln/detail/CVE-2026-109810) | Medium | 6.1 | SAP NetWeaver Application Server Java (Web Dynpro Java) does not sufficiently validate certain request parameters used… |
| 2026-11-10 01:17:15 | [CVE-2026-109811](https://nvd.nist.gov/vuln/detail/CVE-2026-109811) | Medium | 6.5 | An internal ABAP HTTP component in SAP NetWeaver and ABAP Platform (Application Server ABAP) has SSRF vulnerability due… |
| 2026-11-10 01:17:15 | [CVE-2026-120008](https://nvd.nist.gov/vuln/detail/CVE-2026-120008) | High | 8.2 | SAP NetWeaver (Internet Graphics Service) does not sufficiently validate certain input values within incoming requests.… |
| 2026-11-10 01:17:16 | [CVE-2026-120009](https://nvd.nist.gov/vuln/detail/CVE-2026-120009) | High | 7.2 | SAP ABAP Developer Tools (AMDP Data Preview) does not perform sufficient validation and authorization checks within cer… |
| 2026-11-10 01:17:16 | [CVE-2026-120010](https://nvd.nist.gov/vuln/detail/CVE-2026-120010) | High | 7.5 | SAP NetWeaver Application Server (SAP Message Server) does not properly size memory allocations when handling certain H… |
| 2026-11-10 01:17:16 | [CVE-2026-120014](https://nvd.nist.gov/vuln/detail/CVE-2026-120014) | High | 7.6 | SAP HANA XSA Web Dispatcher does not perform sufficient request validation in certain administrative functionality. In… |
| 2026-11-10 01:17:16 | [CVE-2026-120015](https://nvd.nist.gov/vuln/detail/CVE-2026-120015) | High | 7.5 | SAP Host Agent does not sufficiently validate certain inputs. Under certain condition, an attacker with low privileges… |
| 2026-11-10 01:17:16 | [CVE-2026-120016](https://nvd.nist.gov/vuln/detail/CVE-2026-120016) | Medium | 6.1 | SAP NetWeaver Visual Composer does not perform sufficient input validation and output encoding on certain request data.… |
| 2026-11-10 01:17:16 | [CVE-2026-120017](https://nvd.nist.gov/vuln/detail/CVE-2026-120017) | Critical | 10.0 | SAP NetWeaver AS ABAP and ABAP Platform does not perform sufficient verification of incoming authentication assertions… |
| 2026-11-10 01:17:17 | [CVE-2026-123424](https://nvd.nist.gov/vuln/detail/CVE-2026-123424) |  |  | Rejected reason: This CVE ID has been rejected as a duplicate. |
| 2026-11-10 01:17:17 | [CVE-2026-123426](https://nvd.nist.gov/vuln/detail/CVE-2026-123426) |  |  | Rejected reason: This CVE ID has been rejected as a duplicate. |
| 2026-11-10 01:17:17 | [CVE-2026-123425](https://nvd.nist.gov/vuln/detail/CVE-2026-123425) |  |  | Rejected reason: This CVE ID has been rejected as a duplicate. |
| 2026-11-10 01:17:17 | [CVE-2026-123427](https://nvd.nist.gov/vuln/detail/CVE-2026-123427) |  |  | Rejected reason: This CVE ID has been rejected as a duplicate. |
| 2026-11-10 01:17:17 | [CVE-2026-123429](https://nvd.nist.gov/vuln/detail/CVE-2026-123429) |  |  | Rejected reason: This CVE ID has been rejected as a duplicate. |
| 2026-11-10 01:17:17 | [CVE-2026-123430](https://nvd.nist.gov/vuln/detail/CVE-2026-123430) |  |  | Rejected reason: This CVE ID has been rejected as a duplicate. |
| 2026-11-10 01:17:17 | [CVE-2026-123431](https://nvd.nist.gov/vuln/detail/CVE-2026-123431) |  |  | Rejected reason: This CVE ID has been rejected as a duplicate. |
| 2026-11-10 01:17:17 | [CVE-2026-123432](https://nvd.nist.gov/vuln/detail/CVE-2026-123432) |  |  | Rejected reason: This CVE ID has been rejected as a duplicate. |
| 2026-11-10 01:17:17 | [CVE-2026-123437](https://nvd.nist.gov/vuln/detail/CVE-2026-123437) |  |  | Rejected reason: This CVE ID has been rejected as a duplicate. |
| 2026-11-10 01:17:17 | [CVE-2026-123435](https://nvd.nist.gov/vuln/detail/CVE-2026-123435) |  |  | Rejected reason: This CVE ID has been rejected as a duplicate. |
| 2026-11-10 01:17:17 | [CVE-2026-123438](https://nvd.nist.gov/vuln/detail/CVE-2026-123438) |  |  | Rejected reason: This CVE ID has been rejected as a duplicate. |
| 2026-11-10 01:17:17 | [CVE-2026-123439](https://nvd.nist.gov/vuln/detail/CVE-2026-123439) |  |  | Rejected reason: This CVE ID has been rejected as a duplicate. |
| 2026-11-10 01:17:18 | [CVE-2026-124598](https://nvd.nist.gov/vuln/detail/CVE-2026-124598) | High | 7.5 | An API key is hardcoded and retrievable from the GV-Face package. Since Android applications can be reverse engineered,… |
| 2026-11-10 01:17:18 | [CVE-2026-124599](https://nvd.nist.gov/vuln/detail/CVE-2026-124599) | Medium | 6.2 | The RSA cryptographic key material, including a private key and public key, is embedded within the application package.… |
| 2026-11-10 01:17:18 | [CVE-2026-124600](https://nvd.nist.gov/vuln/detail/CVE-2026-124600) | Critical | 10.0 | GV-Face transmits sensitive user credentials and related authentication data over unencrypted HTTP connections. The HTT… |
| 2026-11-10 01:17:18 | [CVE-2026-124601](https://nvd.nist.gov/vuln/detail/CVE-2026-124601) | Medium | 6.2 | An API key is hardcoded and retrievable from the GV-Access package. Since Android applications can be reverse engineere… |
| 2026-11-10 01:17:18 | [CVE-2026-124602](https://nvd.nist.gov/vuln/detail/CVE-2026-124602) | Medium | 6.2 | The RSA cryptographic key material, including a private key and public key, is embedded within the GV-Access applicatio… |
| 2026-11-10 01:17:18 | [CVE-2026-124603](https://nvd.nist.gov/vuln/detail/CVE-2026-124603) | Medium | 6.2 | An API key is hardcoded and retrievable from the GV-Cloud application package. Since Android applications can be revers… |
| 2026-11-10 01:17:19 | [CVE-2026-124604](https://nvd.nist.gov/vuln/detail/CVE-2026-124604) | Medium | 6.2 | The RSA cryptographic key material, including a private key and public key, is embedded within the GV-Cloud application… |
| 2026-11-10 01:17:19 | [CVE-2026-125079](https://nvd.nist.gov/vuln/detail/CVE-2026-125079) | Medium | 5.5 | A vulnerability was determined in D-Link DCS-6501LH 3.03.02. This impacts the function pf_get_onvif_user_pwd/mydlink_de… |
| 2026-11-10 01:17:19 | [CVE-2026-125082](https://nvd.nist.gov/vuln/detail/CVE-2026-125082) | Low | 2.0 | A security flaw has been discovered in sunkaifei FlyCMS up to e71738e0cfb7ffd48c2ce74242a2dbb43f84f25a. Affected by thi… |
| 2026-11-10 01:17:19 | [CVE-2026-125086](https://nvd.nist.gov/vuln/detail/CVE-2026-125086) | Critical | 9.3 | A vulnerability has been found in D-Link M60 1.12.B01. Impacted is the function system of the file /etc/emDaemon/mosqui… |
| 2026-11-10 01:17:19 | [CVE-2026-125087](https://nvd.nist.gov/vuln/detail/CVE-2026-125087) | Medium | 5.5 | A vulnerability was found in Michael-A-Kuykendall Shimmy up to 2.6.4. The affected element is an unknown function of th… |
| 2026-11-10 01:17:20 | [CVE-2026-76964](https://nvd.nist.gov/vuln/detail/CVE-2026-76964) | Critical | 10.0 | SAP NetWeaver Application Server ABAP does not sufficiently validate certain network input processed by an internal com… |
| 2026-11-10 01:17:20 | [CVE-2026-76965](https://nvd.nist.gov/vuln/detail/CVE-2026-76965) | Critical | 9.9 | SAP NetWeaver Application Server ABAP and ABAP Platform does not perform necessary authorization checks for certain int… |
| 2026-11-10 01:17:20 | [CVE-2026-76966](https://nvd.nist.gov/vuln/detail/CVE-2026-76966) | High | 8.9 | Due to improper RFC protocol validation in the SAP Kernel used by the Application Server ABAP of SAP NetWeaver and ABAP… |
| 2026-11-10 01:17:20 | [CVE-2026-76970](https://nvd.nist.gov/vuln/detail/CVE-2026-76970) | High | 7.5 | Due to a Memory Corruption vulnerability in Application Server ABAP for SAP NetWeaver and ABAP Platform, an unauthentic… |
| 2026-11-10 01:17:20 | [CVE-2026-76973](https://nvd.nist.gov/vuln/detail/CVE-2026-76973) | High | 7.5 | Due to a Memory Corruption vulnerability in Application Server ABAP of SAP NetWeaver and ABAP Platform, an unauthentica… |
| 2026-11-10 01:17:21 | [CVE-2026-89103](https://nvd.nist.gov/vuln/detail/CVE-2026-89103) | Critical | 10.0 | SAP Gateway activates the default Access Control List with high privileges allowing categorization of external attacker… |
| 2026-11-10 01:17:21 | [CVE-2026-89114](https://nvd.nist.gov/vuln/detail/CVE-2026-89114) | High | 7.5 | SAP NetWeaver AS Java EDM Application does not perform an authentication check for certain web service requests. An una… |
| 2026-11-10 01:17:21 | [CVE-2026-89115](https://nvd.nist.gov/vuln/detail/CVE-2026-89115) | Medium | 4.4 | SAP Start Service and SAP Management Console store sensitive credential information in process memory without protectio… |
| 2026-11-10 01:17:22 | [CVE-2026-89119](https://nvd.nist.gov/vuln/detail/CVE-2026-89119) | Critical | 9.6 | SAP Web Dispatcher and SAP NetWeaver Application Server ABAP (Internet Communication Manager) do not perform sufficient… |
| 2026-11-10 01:17:22 | [CVE-2026-89125](https://nvd.nist.gov/vuln/detail/CVE-2026-89125) | Medium | 6.0 | Due to Insecure Storage of Sensitive Information in SAP Web Dispatcher and Internet Communication Manager, an attacker… |
| 2026-11-10 01:17:22 | [CVE-2026-89126](https://nvd.nist.gov/vuln/detail/CVE-2026-89126) | Critical | 10.0 | SAP Web Dispatcher does not sufficiently validate certain network input processed by an internal component. An unauthen… |
| 2026-11-10 01:17:22 | [CVE-2026-89128](https://nvd.nist.gov/vuln/detail/CVE-2026-89128) | Medium | 5.3 | Due to Broken Access Control in SAP NetWeaver AS Java, an unauthenticated attacker could invoke affected SOAP operation… |
| 2026-11-10 01:17:22 | [CVE-2026-89129](https://nvd.nist.gov/vuln/detail/CVE-2026-89129) | Medium | 5.8 | Due to a Server-Side Request Forgery (SSRF) vulnerability in SAP NetWeaver AS Java (Web Services), an unauthenticated a… |
| 2026-11-10 01:17:22 | [CVE-2026-89131](https://nvd.nist.gov/vuln/detail/CVE-2026-89131) | Medium | 4.3 | SAP NetWeaver Enterprise Portal does not sufficiently protect certain server-side actions against cross-site request fo… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
