# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-11-10 16:18 UTC

New CVEs published between 2026-11-10 15:22 UTC and 2026-11-10 16:18 UTC.

[Full CSV](data/new-cves-2026-11-10T16-18-55-118394Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-11-10 16:17:13 | [CVE-2026-105425](https://nvd.nist.gov/vuln/detail/CVE-2026-105425) | High | 7.2 | OS command injection in Ivanti Sentry before versions 10.7.4, 10.8.3, and 11.0.0 as well as in Ivanti EPMM before versi… |
| 2026-11-10 16:17:13 | [CVE-2026-105426](https://nvd.nist.gov/vuln/detail/CVE-2026-105426) | Medium | 6.7 | Improper input validation in Ivanti EPMM before version 12.10.0.1, 12.9.0.3, and 12.8.0.5 allows a remote authenticated… |
| 2026-11-10 16:17:13 | [CVE-2026-105427](https://nvd.nist.gov/vuln/detail/CVE-2026-105427) | Medium | 4.9 | Improper input validation in Ivanti EPMM before version 12.10.0.1, 12.9.0.3, and 12.8.0.5 allows a remote authenticated… |
| 2026-11-10 16:17:13 | [CVE-2026-105669](https://nvd.nist.gov/vuln/detail/CVE-2026-105669) | Medium | 6.7 | Argument injection in Ivanti Sentry before version 10.8.3 and 10.7.4 allows a remote authenticated attacker with admin… |
| 2026-11-10 16:17:13 | [CVE-2026-105813](https://nvd.nist.gov/vuln/detail/CVE-2026-105813) | Medium | 6.3 | Cleartext storage of sensitive information in Ivanti UWM before version 2026.4 allows a local authenticated attacker to… |
| 2026-11-10 16:17:14 | [CVE-2026-107404](https://nvd.nist.gov/vuln/detail/CVE-2026-107404) | Medium | 4.9 | Argument injection in Ivanti EPMM before version 12.10.0.1, 12.9.0.3, and 12.8.0.5 allows a remote authenticated attack… |
| 2026-11-10 16:17:14 | [CVE-2026-108186](https://nvd.nist.gov/vuln/detail/CVE-2026-108186) | Critical | 9.6 | Improper Input Validation in Zoom Workplace for Windows may allow an unauthenticated user to conduct an escalation of p… |
| 2026-11-10 16:17:14 | [CVE-2026-108187](https://nvd.nist.gov/vuln/detail/CVE-2026-108187) | High | 8.1 | Origin Validation Error in Zoom Workplace for Windows may allow an unauthenticated user to conduct an escalation of pri… |
| 2026-11-10 16:17:14 | [CVE-2026-111239](https://nvd.nist.gov/vuln/detail/CVE-2026-111239) |  |  | The optional SSH administration service grants full access to the administration shell to every user that authenticates… |
| 2026-11-10 16:17:14 | [CVE-2026-111240](https://nvd.nist.gov/vuln/detail/CVE-2026-111240) |  |  | The JDBC based JAAS login module accepts a login without a password for accounts whose stored password is NULL. A remot… |
| 2026-11-10 16:17:14 | [CVE-2026-111241](https://nvd.nist.gov/vuln/detail/CVE-2026-111241) |  |  | When a non-default stateful session bean passivation strategy is configured, passivated bean state is written to predic… |
| 2026-11-10 16:17:14 | [CVE-2026-111242](https://nvd.nist.gov/vuln/detail/CVE-2026-111242) |  |  | When MicroProfile JWT authentication is used for servlets that declare a run-as identity, the security state establishe… |
| 2026-11-10 16:17:15 | [CVE-2026-111243](https://nvd.nist.gov/vuln/detail/CVE-2026-111243) |  |  | A negative MicroProfile JWT clock skew setting is not rejected and disables validation of the token expiration and othe… |
| 2026-11-10 16:17:15 | [CVE-2026-111244](https://nvd.nist.gov/vuln/detail/CVE-2026-111244) |  |  | When MicroProfile JWT role-based access control is used, the access constraints of JAX-RS resources are not always enfo… |
| 2026-11-10 16:17:15 | [CVE-2026-111245](https://nvd.nist.gov/vuln/detail/CVE-2026-111245) |  |  | After a successful WS-Security UsernameToken authentication, the caller identity stays associated with the worker threa… |
| 2026-11-10 16:17:15 | [CVE-2026-111246](https://nvd.nist.gov/vuln/detail/CVE-2026-111246) |  |  | The embedded OpenEJB HTTP server does not isolate HTTP sessions between web applications. A remote attacker can use a s… |
| 2026-11-10 16:17:15 | [CVE-2026-111247](https://nvd.nist.gov/vuln/detail/CVE-2026-111247) |  |  | When resolving security roles of a realm-authenticated caller, the caller's user name is also treated as a role name in… |
| 2026-11-10 16:17:15 | [CVE-2026-111248](https://nvd.nist.gov/vuln/detail/CVE-2026-111248) |  |  | The Jakarta Security identity store backed by the Tomcat user database compares the supplied password with the stored v… |
| 2026-11-10 16:17:15 | [CVE-2026-111249](https://nvd.nist.gov/vuln/detail/CVE-2026-111249) |  |  | The development-time LiveReload support listens on all network interfaces without authentication and accepts websocket… |
| 2026-11-10 16:17:15 | [CVE-2026-111250](https://nvd.nist.gov/vuln/detail/CVE-2026-111250) |  |  | The embedded OpenEJB HTTP server reports every request as authenticated when an application requests authentication pro… |
| 2026-11-10 16:17:16 | [CVE-2026-111251](https://nvd.nist.gov/vuln/detail/CVE-2026-111251) |  |  | The admin service of the standalone OpenEJB server accepts stop requests without any authentication. Any local user or… |
| 2026-11-10 16:17:16 | [CVE-2026-111256](https://nvd.nist.gov/vuln/detail/CVE-2026-111256) |  |  | When JAX-WS or JAX-RS endpoints are published by the embedded OpenEJB HTTP server rather than Tomcat, some configured a… |
| 2026-11-10 16:17:16 | [CVE-2026-111257](https://nvd.nist.gov/vuln/detail/CVE-2026-111257) |  |  | With the default configuration and no users defined in the default user database, TomEE silently adds an administrative… |
| 2026-11-10 16:17:16 | [CVE-2026-111258](https://nvd.nist.gov/vuln/detail/CVE-2026-111258) |  |  | The optional request routing feature forwards requests to their configured destination without applying the security co… |
| 2026-11-10 16:17:16 | [CVE-2026-111259](https://nvd.nist.gov/vuln/detail/CVE-2026-111259) |  |  | The embedded server generates HTTP session identifiers with a non-cryptographic random number generator by default. A r… |
| 2026-11-10 16:17:16 | [CVE-2026-111260](https://nvd.nist.gov/vuln/detail/CVE-2026-111260) |  |  | The Jakarta Security OpenID Connect authentication mechanism generates the state and nonce values with a non-cryptograp… |
| 2026-11-10 16:17:16 | [CVE-2026-111261](https://nvd.nist.gov/vuln/detail/CVE-2026-111261) |  |  | The Jakarta Security LDAP identity store accepts an empty password as valid if the directory server allows unauthentica… |
| 2026-11-10 16:17:16 | [CVE-2026-112191](https://nvd.nist.gov/vuln/detail/CVE-2026-112191) | High | 8.6 | In Eclipse Kura versions 5.4.0 through 5.6.2, the Identity REST APIs (identity/v1, and identity/v2 since 5.5.0, provide… |
| 2026-11-10 16:17:17 | [CVE-2026-11315](https://nvd.nist.gov/vuln/detail/CVE-2026-11315) | Medium | 4.3 | A out-of-bounds read vulnerability exists in the dr_mp3 drmp3_init_internal functionality of dr_libs (version(s): 0.7.3… |
| 2026-11-10 16:17:17 | [CVE-2026-11316](https://nvd.nist.gov/vuln/detail/CVE-2026-11316) | High | 8.8 | A out-of-bounds write vulnerability exists in the dr_wav drwav__read_cue_to_metadata_obj functionality of dr_libs (vers… |
| 2026-11-10 16:17:17 | [CVE-2026-121653](https://nvd.nist.gov/vuln/detail/CVE-2026-121653) | Critical | 9.8 | SQL injection in the Core of Ivanti Endpoint Manager before version 2024 SU8 allows a remote unauthenticated attacker t… |
| 2026-11-10 16:17:17 | [CVE-2026-121683](https://nvd.nist.gov/vuln/detail/CVE-2026-121683) | Critical | 9.4 | Missing authentication in Ivanti Cloud Services Application version 5.0.8 allows a remote unauthenticated attacker to a… |
| 2026-11-10 16:17:18 | [CVE-2026-123179](https://nvd.nist.gov/vuln/detail/CVE-2026-123179) | Medium | 5.5 | An insecure default initialization of resource in the Tomcat shutdown listener of Ivanti Ivanti Sentry before versions… |
| 2026-11-10 16:17:18 | [CVE-2026-123181](https://nvd.nist.gov/vuln/detail/CVE-2026-123181) | Medium | 5.5 | A path traversal vulnerability in Ivanti Sentry before versions 10.7.4 and 10.8.3 allows a remote authenticated attacke… |
| 2026-11-10 16:17:18 | [CVE-2026-124036](https://nvd.nist.gov/vuln/detail/CVE-2026-124036) | High | 7.6 | Missing authorization checks in the visual alert feature of FlockOS, Flock's hosted public safety platform, prior to 20… |
| 2026-11-10 16:17:18 | [CVE-2026-124037](https://nvd.nist.gov/vuln/detail/CVE-2026-124037) | High | 8.2 | An information exposure flaw in the public access-list sign-up feature of the Flock Safety Platform, present from 2026-… |
| 2026-11-10 16:17:18 | [CVE-2026-124038](https://nvd.nist.gov/vuln/detail/CVE-2026-124038) | Low | 1.0 | An uncontrolled XML entity expansion vulnerability in the Flock Installer app for Android before version 2.35.0 allows… |
| 2026-11-10 16:17:20 | [CVE-2026-125747](https://nvd.nist.gov/vuln/detail/CVE-2026-125747) | Medium | 5.3 | ZenTao PMS through 22.7 contains a missing object-level authorization vulnerability in module/build/control.php that al… |
| 2026-11-10 16:17:20 | [CVE-2026-125748](https://nvd.nist.gov/vuln/detail/CVE-2026-125748) | Medium | 5.3 | Parabol before 15.21.2 contains a missing authorization vulnerability in the addReactjiToReactable GraphQL mutation tha… |
| 2026-11-10 16:17:20 | [CVE-2026-125749](https://nvd.nist.gov/vuln/detail/CVE-2026-125749) | Low | 2.3 | TaxHacker through 0.8.5 contains an insecure direct object reference vulnerability in app/(app)/settings/actions.ts tha… |
| 2026-11-10 16:17:21 | [CVE-2026-125750](https://nvd.nist.gov/vuln/detail/CVE-2026-125750) | High | 7.1 | Firekylin through 2.18.1 contains an improper authorization vulnerability that allows editor-role users to read adminis… |
| 2026-11-10 16:17:21 | [CVE-2026-125751](https://nvd.nist.gov/vuln/detail/CVE-2026-125751) | Low | 2.3 | Meteroid before 2.2.0 contains an authorization bypass vulnerability in the ApiTokensService GetApiTokenById gRPC handl… |
| 2026-11-10 16:17:21 | [CVE-2026-125752](https://nvd.nist.gov/vuln/detail/CVE-2026-125752) | Low | 2.3 | Meteroid before 2.2.0 contains a cross-tenant authorization bypass vulnerability in the CouponsService UpdateCouponStat… |
| 2026-11-10 16:17:22 | [CVE-2026-125753](https://nvd.nist.gov/vuln/detail/CVE-2026-125753) | High | 8.2 | ABP Framework 2.9.0 before 10.6.2 and 10.7.0 pre-releases before 10.7.0 contain a path traversal vulnerability in Defau… |
| 2026-11-10 16:17:22 | [CVE-2026-125754](https://nvd.nist.gov/vuln/detail/CVE-2026-125754) | High | 7.1 | Dolibarr 20.0.0 through 23.0.4 and 24.x before 24.0.2 contains an insecure direct object reference vulnerability in api… |
| 2026-11-10 16:17:22 | [CVE-2026-125755](https://nvd.nist.gov/vuln/detail/CVE-2026-125755) | High | 8.3 | Nodemailer 3.0.0 before 10.4.1 contains an address parsing flaw in addressparser that truncates domains at folding whit… |
| 2026-11-10 16:17:22 | [CVE-2026-125756](https://nvd.nist.gov/vuln/detail/CVE-2026-125756) | High | 8.2 | postal-mime before 4.2.1 contains a parser differential vulnerability in its address parser that truncates the domain a… |
| 2026-11-10 16:17:23 | [CVE-2026-125757](https://nvd.nist.gov/vuln/detail/CVE-2026-125757) | Critical | 9.4 | mailcow: dockerized before 2026-11 contains a server-side template injection vulnerability that allows domain administr… |
| 2026-11-10 16:17:23 | [CVE-2026-125758](https://nvd.nist.gov/vuln/detail/CVE-2026-125758) | Critical | 9.1 | Aptabase before commit 61d4c01 contains an authentication bypass vulnerability that allows unauthenticated attackers to… |
| 2026-11-10 16:17:23 | [CVE-2026-125759](https://nvd.nist.gov/vuln/detail/CVE-2026-125759) | High | 7.7 | Nango before 0.71.3 contains an sql injection vulnerability that allows unauthenticated attackers to execute arbitrary… |
| 2026-11-10 16:17:24 | [CVE-2026-18128](https://nvd.nist.gov/vuln/detail/CVE-2026-18128) | Medium | 6.8 | Cleartext transmission of sensitive information in the Agent of Ivanti Endpoint Manager before version 2024 SU8 allows… |
| 2026-11-10 16:17:24 | [CVE-2026-86336](https://nvd.nist.gov/vuln/detail/CVE-2026-86336) |  |  | Apache TomEE running on JDK 21 or later skips EJB method authorization checks, allowing callers to invoke EJB methods w… |
| 2026-11-10 16:17:24 | [CVE-2026-86531](https://nvd.nist.gov/vuln/detail/CVE-2026-86531) |  |  | The embedded OpenEJB HTTP server does not limit the size of incoming request bodies or of multipart requests, and does… |
| 2026-11-10 16:17:24 | [CVE-2026-87758](https://nvd.nist.gov/vuln/detail/CVE-2026-87758) |  |  | The remote EJB client does not verify that the hostname of the server it connects to matches the server's TLS certifica… |
| 2026-11-10 16:17:25 | [CVE-2026-97402](https://nvd.nist.gov/vuln/detail/CVE-2026-97402) | Low | 2.3 | In Eclipse Kura versions 3.1.0 to 5.6.2, the iBeacon and Eddystone advertisement decoders wrongly parse the AD-structur… |
| 2026-11-10 16:17:25 | [CVE-2026-97849](https://nvd.nist.gov/vuln/detail/CVE-2026-97849) |  |  | The embedded Derby network service ignores its configured bind address and listens on all network interfaces. When the… |
| 2026-11-10 16:17:25 | [CVE-2026-97867](https://nvd.nist.gov/vuln/detail/CVE-2026-97867) |  |  | The EJBd remote protocol returns datasource connection details, including database credentials, to remote clients that… |
| 2026-11-10 16:17:26 | [CVE-2026-97870](https://nvd.nist.gov/vuln/detail/CVE-2026-97870) |  |  | When Hessian remoting endpoints are served by the embedded HTTP server, configured authentication and transport securit… |
| 2026-11-10 16:17:26 | [CVE-2026-97872](https://nvd.nist.gov/vuln/detail/CVE-2026-97872) |  |  | When an EJB is exposed over the optional Hessian protocol inside an existing web application, some configured authentic… |
| 2026-11-10 16:17:26 | [CVE-2026-97874](https://nvd.nist.gov/vuln/detail/CVE-2026-97874) |  |  | When Hessian remoting is configured with BASIC authentication, the authentication check is not applied to Hessian endpo… |
| 2026-11-10 16:17:26 | [CVE-2026-97880](https://nvd.nist.gov/vuln/detail/CVE-2026-97880) |  |  | The embedded OpenEJB HTTP server dispatches some requests to REST endpoints configured for HTTP Basic authentication wi… |
| 2026-11-10 16:17:26 | [CVE-2026-97881](https://nvd.nist.gov/vuln/detail/CVE-2026-97881) |  |  | The embedded OpenEJB HTTP server does not restrict static resource paths to the configured resource directories. A remo… |
| 2026-11-10 16:17:27 | [CVE-2026-97888](https://nvd.nist.gov/vuln/detail/CVE-2026-97888) |  |  | The embedded HTTP server does not clear the security identity established during a request before its worker thread han… |
| 2026-11-10 16:17:27 | [CVE-2026-97890](https://nvd.nist.gov/vuln/detail/CVE-2026-97890) |  |  | The embedded HTTP server does not invalidate the previous session identifier when an application changes the session id… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
