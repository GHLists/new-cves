# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-30 20:19 UTC

New CVEs published between 2026-10-30 19:18 UTC and 2026-10-30 20:19 UTC.

[Full CSV](data/new-cves-2026-10-30T20-19-16-702941Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-10-30 19:19:10 | [CVE-2026-73186](https://nvd.nist.gov/vuln/detail/CVE-2026-73186) | High | 8.8 | Subscriber PHP Object Injection in Enable Media Replace <= 4.2.2 versions. |
| 2026-10-30 19:19:10 | [CVE-2026-73322](https://nvd.nist.gov/vuln/detail/CVE-2026-73322) |  |  | Incorrect Authorization vulnerability in the single-stage query engine of Apache Pinot. When broker access control is e… |
| 2026-10-30 19:19:12 | [CVE-2026-78527](https://nvd.nist.gov/vuln/detail/CVE-2026-78527) | High | 8.8 | Contributor PHP Object Injection in GS Testimonial Slider <= 3.3.10 versions. |
| 2026-10-30 19:19:13 | [CVE-2026-7003](https://nvd.nist.gov/vuln/detail/CVE-2026-7003) | Medium | 6.9 | WIT SynApps Runtime through 1.4.11 contains a hardcoded credentials vulnerability that allows unauthenticated attackers… |
| 2026-10-30 19:19:13 | [CVE-2026-7004](https://nvd.nist.gov/vuln/detail/CVE-2026-7004) | Medium | 5.1 | WIT SynApps Runtime through 1.4.11 contains a pre-authentication reflected cross-site scripting vulnerability that allo… |
| 2026-10-30 19:19:13 | [CVE-2026-7005](https://nvd.nist.gov/vuln/detail/CVE-2026-7005) | Medium | 5.3 | WIT SynApps Runtime through 1.4.11 contains a browser-mediated cross-origin request forgery vulnerability that allows a… |
| 2026-10-30 19:20:18 | [CVE-2026-90888](https://nvd.nist.gov/vuln/detail/CVE-2026-90888) | Critical | 9.8 | Unauthenticated PHP Object Injection in LeadSnap <= 1.25 versions. |
| 2026-10-30 19:20:19 | [CVE-2026-94175](https://nvd.nist.gov/vuln/detail/CVE-2026-94175) | High | 7.1 | Unauthenticated Cross Site Scripting (XSS) in All In One Login <= 2.4.1 versions. |
| 2026-10-30 20:17:01 | [CVE-2026-115828](https://nvd.nist.gov/vuln/detail/CVE-2026-115828) | Medium | 5.1 | In Secret Server versions earlier than 12.3.1, Secret Server did not always validate the PIN or biometric check when us… |
| 2026-10-30 20:17:02 | [CVE-2026-115829](https://nvd.nist.gov/vuln/detail/CVE-2026-115829) | High | 8.7 | In Secret Server versions earlier than 12.3.1, a user could bypass the initial login step and authenticate by successfu… |
| 2026-10-30 20:17:02 | [CVE-2026-115830](https://nvd.nist.gov/vuln/detail/CVE-2026-115830) | High | 8.7 | In Secret Server versions earlier than 12.3.1, a user under certain conditions could submit an unsigned JWT and receive… |
| 2026-10-30 20:17:02 | [CVE-2026-116238](https://nvd.nist.gov/vuln/detail/CVE-2026-116238) | Critical | 9.2 | In server mode pgAdmin 4 locks an internal account after MAX_LOGIN_ATTEMPTS failed logins (3 by default). The limit cou… |
| 2026-10-30 20:17:03 | [CVE-2026-116239](https://nvd.nist.gov/vuln/detail/CVE-2026-116239) | High | 8.9 | In server mode pgAdmin 4 keeps an account per authentication source, so the same username can exist as, for example, an… |
| 2026-10-30 20:17:03 | [CVE-2026-116240](https://nvd.nist.gov/vuln/detail/CVE-2026-116240) | High | 7.1 | In server mode pgAdmin 4 validates a path into the user's storage directory with check_access_permission(), which build… |
| 2026-10-30 20:17:03 | [CVE-2026-116241](https://nvd.nist.gov/vuln/detail/CVE-2026-116241) | Critical | 9.4 | pgAdmin 4's Import/Export Data tool wraps a user's query export in a psql \copy (...) TO command and checks that the qu… |
| 2026-10-30 20:17:03 | [CVE-2026-116242](https://nvd.nist.gov/vuln/detail/CVE-2026-116242) | High | 7.1 | pgAdmin 4 opens SSH tunnels with the sshtunnel library but gave it neither host_pkey_directories nor ssh_config_file, s… |
| 2026-10-30 20:17:04 | [CVE-2026-116243](https://nvd.nist.gov/vuln/detail/CVE-2026-116243) | High | 7.7 | pgAdmin 4 runs pg_dump, pg_restore, pg_dumpall and psql from the binary path a user sets in their preferences. In serve… |
| 2026-10-30 20:17:04 | [CVE-2026-116244](https://nvd.nist.gov/vuln/detail/CVE-2026-116244) | High | 7.1 | When a pgAdmin 4 connection was not meant to use a Kerberos user's delegated credentials, pgAdmin removed KRB5CCNAME fr… |
| 2026-10-30 20:17:04 | [CVE-2026-116245](https://nvd.nist.gov/vuln/detail/CVE-2026-116245) | High | 7.1 | libpq looks a connection service up in the service file of the operating-system account running pgAdmin 4, and an entry… |
| 2026-10-30 20:17:04 | [CVE-2026-116246](https://nvd.nist.gov/vuln/detail/CVE-2026-116246) | High | 7.0 | To pass a server's password to psql and to the utilities pgAdmin 4 runs as background processes, the server manager wro… |
| 2026-10-30 20:17:04 | [CVE-2026-116247](https://nvd.nist.gov/vuln/detail/CVE-2026-116247) | High | 7.1 | When a server in pgAdmin 4 had no password file, client certificate or client key configured, or the configured one cou… |
| 2026-10-30 20:17:04 | [CVE-2026-116248](https://nvd.nist.gov/vuln/detail/CVE-2026-116248) | Medium | 6.0 | In pgAdmin 4 server mode only administrators are meant to share a server with all users; the server dialog shows the Sh… |
| 2026-10-30 20:17:05 | [CVE-2026-116249](https://nvd.nist.gov/vuln/detail/CVE-2026-116249) | High | 7.2 | In server mode pgAdmin 4 resolves a server's password file, SSL certificate, key, CRL and SSH tunnel identity file rela… |
| 2026-10-30 20:17:05 | [CVE-2026-116250](https://nvd.nist.gov/vuln/detail/CVE-2026-116250) | High | 7.3 | In server mode pgAdmin 4 validates a path a user gives for a file in their storage directory with check_access_permissi… |
| 2026-10-30 20:17:05 | [CVE-2026-116251](https://nvd.nist.gov/vuln/detail/CVE-2026-116251) | Low | 2.3 | pgAdmin 4 did not invalidate a user's existing sessions when their password changed, either through the user's own chan… |
| 2026-10-30 20:17:05 | [CVE-2026-116252](https://nvd.nist.gov/vuln/detail/CVE-2026-116252) | High | 7.1 | pgAdmin 4's materialized view refresh passed the target database's name to psql's --dbname argument unchanged. libpq tr… |
| 2026-10-30 20:17:06 | [CVE-2026-119328](https://nvd.nist.gov/vuln/detail/CVE-2026-119328) | Medium | 6.5 | Immich is a high-performance self-hosted photo and video management solution. Prior to 3.3.0, the unauthenticated machi… |
| 2026-10-30 20:17:06 | [CVE-2026-119329](https://nvd.nist.gov/vuln/detail/CVE-2026-119329) | Medium | 4.3 | Immich is a high-performance self-hosted photo and video management solution. Prior to 3.0.0, GET /api/map/markers used… |
| 2026-10-30 20:17:06 | [CVE-2026-119330](https://nvd.nist.gov/vuln/detail/CVE-2026-119330) | Low | 3.5 | Immich is a high-performance self-hosted photo and video management solution. Prior to 3.2.0, the shared-link creation… |
| 2026-10-30 20:17:07 | [CVE-2026-119331](https://nvd.nist.gov/vuln/detail/CVE-2026-119331) | High | 7.1 | Ladybird is a truly independent web browser. Prior to the c0d68bddf3e3616e5173835f0f4c155ee9700d91 commit, CSSStyleShee… |
| 2026-10-30 20:17:07 | [CVE-2026-119332](https://nvd.nist.gov/vuln/detail/CVE-2026-119332) | High | 8.8 | Ladybird is a truly independent web browser. Prior to 209579c96473c75bd5eba9701fcadb841a045964, FinalizationRegistry::c… |
| 2026-10-30 20:17:07 | [CVE-2026-119333](https://nvd.nist.gov/vuln/detail/CVE-2026-119333) | High | 7.8 | draw.io Desktop is the official Electron build of draw.io. Prior to 31.5.2, the Windows application launched powershell… |
| 2026-10-30 20:17:07 | [CVE-2026-119334](https://nvd.nist.gov/vuln/detail/CVE-2026-119334) | Low | 2.2 | Pi-hole is a DNS sinkhole that protects devices from unwanted content without installing any client-side software. Prio… |
| 2026-10-30 20:17:08 | [CVE-2026-119335](https://nvd.nist.gov/vuln/detail/CVE-2026-119335) | High | 7.8 | Pi-hole is a DNS sinkhole that protects devices from unwanted content without installing any client-side software. Prio… |
| 2026-10-30 20:17:08 | [CVE-2026-119336](https://nvd.nist.gov/vuln/detail/CVE-2026-119336) | High | 7.8 | Pi-hole is a DNS sinkhole that protects devices from unwanted content without installing any client-side software. From… |
| 2026-10-30 20:17:08 | [CVE-2026-119337](https://nvd.nist.gov/vuln/detail/CVE-2026-119337) | High | 7.1 | RAGFlow is an open-source RAG (Retrieval-Augmented Generation) engine. From 0.25.2 until 0.27.3, POST /api/v1/agents/ch… |
| 2026-10-30 20:17:08 | [CVE-2026-119730](https://nvd.nist.gov/vuln/detail/CVE-2026-119730) | Medium | 5.1 | Maxthon Browser for Android before 7.5.8.103 contains an address bar spoofing vulnerability that allows remote attacker… |
| 2026-10-30 20:17:09 | [CVE-2026-55098](https://nvd.nist.gov/vuln/detail/CVE-2026-55098) | Medium | 6.5 | Arc is an open, SQL-native time-series database for telemetry. Prior to the repository-verified 26.06.2 repair, the rem… |
| 2026-10-30 20:17:09 | [CVE-2026-55493](https://nvd.nist.gov/vuln/detail/CVE-2026-55493) | Medium | 6.5 | HotCRP is conference review software. Starting with 2.101, the `cmt:` search term checks whether a comment is visible t… |
| 2026-10-30 20:17:10 | [CVE-2026-55598](https://nvd.nist.gov/vuln/detail/CVE-2026-55598) | Critical | 9.1 | PinePods is a complete, self-hosted podcast management system written in Rust. Prior to 0.9.0, an authenticated user ca… |
| 2026-10-30 20:17:10 | [CVE-2026-61618](https://nvd.nist.gov/vuln/detail/CVE-2026-61618) | Medium | 6.9 | SNARK Verifier is a generic (S)NARK verifier. Prior to 0.2.5, KZG accumulator public-instance limbs are decoded without… |
| 2026-10-30 20:17:10 | [CVE-2026-61620](https://nvd.nist.gov/vuln/detail/CVE-2026-61620) | Critical | 9.8 | HoneySQL turns Clojure data structures into SQL. From 2.0.0 until 2.7.1392, applications that pass user input or other… |
| 2026-10-30 20:17:11 | [CVE-2026-61694](https://nvd.nist.gov/vuln/detail/CVE-2026-61694) | Low | 3.7 | go-xrpl is a Go implementation of the XRP Ledger protocol. In versions through the June 18, 2026 revision identified by… |
| 2026-10-30 20:17:11 | [CVE-2026-61850](https://nvd.nist.gov/vuln/detail/CVE-2026-61850) | Critical | 9.3 | Kargo manages and automates the promotion of software artifacts. From 0.6.0 until 1.8.14, 1.9.9, and 1.10.8, two author… |
| 2026-10-30 20:17:11 | [CVE-2026-62284](https://nvd.nist.gov/vuln/detail/CVE-2026-62284) | High | 8.6 | OSAC operator is a Kubernetes operator. In the affected revision identified as 8220502, the `console-proxy` `RemoteConf… |
| 2026-10-30 20:17:11 | [CVE-2026-62301](https://nvd.nist.gov/vuln/detail/CVE-2026-62301) | High | 7.1 | MyTube is a self-hosted downloader and player for several video websites. Prior to version 1.10.3, backend video access… |
| 2026-10-30 20:17:12 | [CVE-2026-62302](https://nvd.nist.gov/vuln/detail/CVE-2026-62302) | High | 8.7 | MyTube is a self-hosted downloader and player for several video websites. Prior to version 1.10.3, `server.ts` calls `r… |
| 2026-10-30 20:17:12 | [CVE-2026-62333](https://nvd.nist.gov/vuln/detail/CVE-2026-62333) | High | 8.7 | OpenVM is a performant and modular zkVM framework built for customization and extensibility. Before 1.7.0 in the 1.x li… |
| 2026-10-30 20:17:12 | [CVE-2026-62334](https://nvd.nist.gov/vuln/detail/CVE-2026-62334) | High | 8.7 | OpenVM is a performant and modular zkVM framework built for customization and extensibility. Before 1.7.0 in the 1.x li… |
| 2026-10-30 20:17:12 | [CVE-2026-62335](https://nvd.nist.gov/vuln/detail/CVE-2026-62335) | Medium | 6.9 | OpenVM is a performant and modular zkVM framework built for customization and extensibility. Before 1.7.0 in the 1.x li… |
| 2026-10-30 20:17:12 | [CVE-2026-62337](https://nvd.nist.gov/vuln/detail/CVE-2026-62337) | Medium | 6.9 | SNARK Verifier is a generic (S)NARK verifier. Prior to 0.2.5, the Halo 2 aggregation circuit can mishandle proof points… |
| 2026-10-30 20:17:17 | [CVE-2026-78402](https://nvd.nist.gov/vuln/detail/CVE-2026-78402) | High | 7.3 | Stack-based buffer overflow and out-of-bounds write vulnerability in Thales Sentinel Keys Server on Windows allows Over… |
| 2026-10-30 20:17:17 | [CVE-2026-78403](https://nvd.nist.gov/vuln/detail/CVE-2026-78403) | Critical | 9.3 | Stack-based buffer overflow and missing authorization vulnerability in Thales Sentinel Keys Server on Windows allows Ov… |
| 2026-10-30 20:17:29 | [CVE-2026-95673](https://nvd.nist.gov/vuln/detail/CVE-2026-95673) |  |  | Rejected reason: ** REJECT ** DO NOT USE THIS CANDIDATE NUMBER. ConsultIDs: CVE-2026-92243. Reason: This candidate is a… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
