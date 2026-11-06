# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-11-06 15:18 UTC

New CVEs published between 2026-11-06 14:19 UTC and 2026-11-06 15:18 UTC.

[Full CSV](data/new-cves-2026-11-06T15-18-42-299149Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-11-06 15:17:05 | [CVE-2026-106019](https://nvd.nist.gov/vuln/detail/CVE-2026-106019) | High | 8.8 | Insertion of sensitive information into log file vulnerability in Johnson Controls C-CURE 9000, Victor allows Use of Kn… |
| 2026-11-06 15:17:05 | [CVE-2026-106020](https://nvd.nist.gov/vuln/detail/CVE-2026-106020) | High | 8.6 | Improper neutralization of input used for LLM prompting vulnerability in Johnson Controls EasyIO Neo IO Manager and Too… |
| 2026-11-06 15:17:05 | [CVE-2026-106022](https://nvd.nist.gov/vuln/detail/CVE-2026-106022) | High | 8.6 | Cleartext storage of sensitive information in memory vulnerability in Johnson Controls EasyIO Neo IOManager and Tools I… |
| 2026-11-06 15:17:07 | [CVE-2026-112334](https://nvd.nist.gov/vuln/detail/CVE-2026-112334) | Medium | 6.9 | Wazuh from 1.0.0 before 4.14.9 contains an out-of-bounds write vulnerability in wazuh-execd that allows privileged mana… |
| 2026-11-06 15:17:07 | [CVE-2026-112335](https://nvd.nist.gov/vuln/detail/CVE-2026-112335) | Medium | 6.8 | Wazuh agent from 1.0.0 before 4.14.9 contains a stack-based buffer overflow in the logcollector snort-full log reader t… |
| 2026-11-06 15:17:07 | [CVE-2026-112336](https://nvd.nist.gov/vuln/detail/CVE-2026-112336) | High | 7.1 | Wazuh Manager from 3.0.0 before 4.14.9 contains a memory leak vulnerability in the generic JSON decoder that allows rem… |
| 2026-11-06 15:17:08 | [CVE-2026-112337](https://nvd.nist.gov/vuln/detail/CVE-2026-112337) | Medium | 6.3 | Wazuh from 3.7.0 before 4.14.9 contains a server-side request forgery vulnerability in the Azure wodle get_graph_events… |
| 2026-11-06 15:17:08 | [CVE-2026-112338](https://nvd.nist.gov/vuln/detail/CVE-2026-112338) | High | 8.2 | Wazuh from 4.3.0 before 4.14.9 contains a server-side request forgery vulnerability in the GitHub module (wm_github.c)… |
| 2026-11-06 15:17:08 | [CVE-2026-112339](https://nvd.nist.gov/vuln/detail/CVE-2026-112339) | High | 8.2 | Wazuh from 3.9.0 before 4.14.9 contains a missing TLS hostname verification vulnerability in the fluent-forward module'… |
| 2026-11-06 15:17:08 | [CVE-2026-112340](https://nvd.nist.gov/vuln/detail/CVE-2026-112340) | High | 8.8 | Wazuh dashboard plugins from 4.9.0 before 4.14.9 contain an authorization bypass vulnerability that allows authenticate… |
| 2026-11-06 15:17:08 | [CVE-2026-112341](https://nvd.nist.gov/vuln/detail/CVE-2026-112341) | High | 7.1 | Wazuh versions from 4.0.0 before 4.14.9 contain a sql injection vulnerability in WazuhDBBackend._substitute_params due… |
| 2026-11-06 15:17:08 | [CVE-2026-113618](https://nvd.nist.gov/vuln/detail/CVE-2026-113618) | Medium | 5.3 | The ZSIRep client library (ZSIREP.CLIENT.DLL) is vulnerable to improper server certificate validation. It registers a p… |
| 2026-11-06 15:17:11 | [CVE-2026-118514](https://nvd.nist.gov/vuln/detail/CVE-2026-118514) | Medium | 6.3 | In Symfony http-foundation prior to versions 5.4.56, 6.4.50, 7.4.23, and 8.1.11, Symfony\Component\HttpFoundation\Reque… |
| 2026-11-06 15:17:12 | [CVE-2026-119170](https://nvd.nist.gov/vuln/detail/CVE-2026-119170) | High | 8.2 | There was a regression in how FIPS algorithms were enforced for the hashlib module. Only users that are using OpenSSL i… |
| 2026-11-06 15:17:17 | [CVE-2026-123339](https://nvd.nist.gov/vuln/detail/CVE-2026-123339) | Low | 2.3 | Improper trust of forwarded headers in RouterListener::onKernelFinishRequest() in Symfony HttpKernel versions prior to… |
| 2026-11-06 15:17:17 | [CVE-2026-123485](https://nvd.nist.gov/vuln/detail/CVE-2026-123485) | High | 7.1 | Ground Station from 0.6.0 before 0.8.20 does not restrict the get-orbital-sources Socket.IO handler (also exposed as ge… |
| 2026-11-06 15:17:17 | [CVE-2026-123486](https://nvd.nist.gov/vuln/detail/CVE-2026-123486) | Medium | 6.0 | WWBN AVideo 29.0 through 29.4.0 contains a race condition vulnerability in plugin/PayPalYPT/ipn.php that allows attacke… |
| 2026-11-06 15:17:17 | [CVE-2026-123487](https://nvd.nist.gov/vuln/detail/CVE-2026-123487) | High | 8.7 | Parse Server before 8.6.115 and 9.0.0 before 9.10.7-alpha.1 validates user email address format with a regular expressi… |
| 2026-11-06 15:17:18 | [CVE-2026-123488](https://nvd.nist.gov/vuln/detail/CVE-2026-123488) | Critical | 9.3 | Craft CMS 4.0.0 before 4.18.9 and 5.0.0 before 5.11.2 contains an unauthenticated SQL injection vulnerability in the el… |
| 2026-11-06 15:17:18 | [CVE-2026-123489](https://nvd.nist.gov/vuln/detail/CVE-2026-123489) | High | 7.1 | Craft CMS 4.0.0 before 4.18.9 and 5.0.0 before 5.11.2 contains a blind SQL injection vulnerability because the sandbox-… |
| 2026-11-06 15:17:18 | [CVE-2026-123490](https://nvd.nist.gov/vuln/detail/CVE-2026-123490) | High | 8.7 | Craft CMS from 5.8.17 before 5.11.2 contains a privilege escalation vulnerability because getOwners() applies caller cr… |
| 2026-11-06 15:17:18 | [CVE-2026-123491](https://nvd.nist.gov/vuln/detail/CVE-2026-123491) | High | 8.8 | Craft CMS 4.0.0 before 4.18.9 and 5.0.0 before 5.11.2 contains an SQL injection vulnerability in GraphQL eager-loading:… |
| 2026-11-06 15:17:18 | [CVE-2026-123492](https://nvd.nist.gov/vuln/detail/CVE-2026-123492) | Medium | 6.9 | SiYuan before 3.8.9 contains a nil pointer dereference vulnerability in privateCacheMiddleware that allows authenticate… |
| 2026-11-06 15:17:19 | [CVE-2026-123617](https://nvd.nist.gov/vuln/detail/CVE-2026-123617) | Medium | 6.9 | Openwhyd before 1.65.1 contains a NoSQL injection vulnerability that allows unauthenticated attackers to manipulate use… |
| 2026-11-06 15:17:19 | [CVE-2026-123618](https://nvd.nist.gov/vuln/detail/CVE-2026-123618) | High | 7.6 | ABP Framework before 10.7.1 contains an authentication bypass vulnerability that skips account state and two-factor che… |
| 2026-11-06 15:17:19 | [CVE-2026-123619](https://nvd.nist.gov/vuln/detail/CVE-2026-123619) | Medium | 5.9 | Lektor through 3.3.14 and 3.4.0b15 contains an absolute path traversal vulnerability in the admin API on Windows that a… |
| 2026-11-06 15:17:19 | [CVE-2026-123620](https://nvd.nist.gov/vuln/detail/CVE-2026-123620) | High | 7.7 | Usermin through 2.570 contains an OS command injection vulnerability in the Read Mail module that allows authenticated… |
| 2026-11-06 15:17:19 | [CVE-2026-123621](https://nvd.nist.gov/vuln/detail/CVE-2026-123621) | High | 8.6 | Usermin through 2.570 contains a path traversal vulnerability in mailbox/detachall.cgi that allows remote unauthenticat… |
| 2026-11-06 15:17:19 | [CVE-2026-123622](https://nvd.nist.gov/vuln/detail/CVE-2026-123622) | Medium | 5.1 | Usermin through 2.570 contains a cross-site scripting vulnerability in mailbox/detach.cgi that allows remote attackers… |
| 2026-11-06 15:17:20 | [CVE-2026-123624](https://nvd.nist.gov/vuln/detail/CVE-2026-123624) | Medium | 5.3 | ChatWiki before 2.10.0 contains an insecure direct object reference vulnerability that allows authenticated users to mo… |
| 2026-11-06 15:17:20 | [CVE-2026-123664](https://nvd.nist.gov/vuln/detail/CVE-2026-123664) | Low | 2.1 | A security flaw has been discovered in nasa-gcn gcn.nasa.gov up to b299b562af665878964b981a459f0a9c04b11adf. This issue… |
| 2026-11-06 15:17:20 | [CVE-2026-123665](https://nvd.nist.gov/vuln/detail/CVE-2026-123665) | Low | 2.4 | A weakness has been identified in kubescape up to 4.0.15. Impacted is the function GetWriter of the file core/pkg/resul… |
| 2026-11-06 15:17:20 | [CVE-2026-123782](https://nvd.nist.gov/vuln/detail/CVE-2026-123782) | Medium | 5.3 | ChatWiki before 2.10.0 contains an insecure direct object reference vulnerability in SaveFormField and UpdateFormRequir… |
| 2026-11-06 15:17:21 | [CVE-2026-123783](https://nvd.nist.gov/vuln/detail/CVE-2026-123783) | High | 8.7 | Skyvern through 1.0.56 contains a sandbox bypass vulnerability that allows authenticated users to execute code by recon… |
| 2026-11-06 15:17:21 | [CVE-2026-123784](https://nvd.nist.gov/vuln/detail/CVE-2026-123784) | High | 8.5 | Fluxbox through 1.3.7 contains an OS command injection vulnerability in RootTheme::reconfigTheme() that allows attacker… |
| 2026-11-06 15:17:21 | [CVE-2026-123785](https://nvd.nist.gov/vuln/detail/CVE-2026-123785) | Medium | 6.8 | Fluxbox through 1.3.7 contains an infinite loop vulnerability in Menu::updateMenu() in src/FbTk/Menu.cc that allows att… |
| 2026-11-06 15:17:21 | [CVE-2026-123786](https://nvd.nist.gov/vuln/detail/CVE-2026-123786) | High | 8.4 | Agenta before 0.122.5 contains a server-side request forgery vulnerability that allows workspace members with workflow… |
| 2026-11-06 15:17:22 | [CVE-2026-53980](https://nvd.nist.gov/vuln/detail/CVE-2026-53980) | High | 8.6 | Charmbracelet wish before 2.0.5 contains a path traversal vulnerability in the git middleware (charm.land/wish/v2) that… |
| 2026-11-06 15:17:22 | [CVE-2026-59105](https://nvd.nist.gov/vuln/detail/CVE-2026-59105) | Critical | 9.3 | Jumis (formerly Tildes Jumis) creates and uses a Microsoft SQL Server login named ##Tilde_JumisAdmin## whose password i… |
| 2026-11-06 15:17:22 | [CVE-2026-64894](https://nvd.nist.gov/vuln/detail/CVE-2026-64894) | High | 7.3 | Inclusion of functionality from untrusted control sphere vulnerability in Johnson Controls EasyIO Neo IOManager and Too… |
| 2026-11-06 15:17:26 | [CVE-2026-87045](https://nvd.nist.gov/vuln/detail/CVE-2026-87045) | High | 7.5 | The HTTP/2 server in subsys/net/lib/http/http_server_http2.c clears the connection's stream binding at the start of eve… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
