# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-14 23:19 UTC

New CVEs published between 2026-10-14 22:19 UTC and 2026-10-14 23:19 UTC.

[Full CSV](data/new-cves-2026-10-14T23-19-36-486338Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-10-14 23:17:22 | [CVE-2026-106006](https://nvd.nist.gov/vuln/detail/CVE-2026-106006) |  |  | Rejected reason: This CVE ID has been rejected or withdrawn by its CVE Numbering Authority. |
| 2026-10-14 23:17:22 | [CVE-2026-106068](https://nvd.nist.gov/vuln/detail/CVE-2026-106068) |  |  | Rejected reason: This CVE ID has been rejected or withdrawn by its CVE Numbering Authority. |
| 2026-10-14 23:17:22 | [CVE-2026-106485](https://nvd.nist.gov/vuln/detail/CVE-2026-106485) |  |  | Rejected reason: This CVE ID has been rejected or withdrawn by its CVE Numbering Authority. |
| 2026-10-14 23:17:22 | [CVE-2026-107795](https://nvd.nist.gov/vuln/detail/CVE-2026-107795) | High | 7.5 | Omada Controller's MSP and OpenAPI certificate/private-key management APIs do not properly enforce administrative autho… |
| 2026-10-14 23:17:22 | [CVE-2026-110807](https://nvd.nist.gov/vuln/detail/CVE-2026-110807) | Low | 2.1 | A weakness has been identified in sgl-project SGLang up to 0.5.19. Affected by this vulnerability is an unknown functio… |
| 2026-10-14 23:17:22 | [CVE-2026-110829](https://nvd.nist.gov/vuln/detail/CVE-2026-110829) | High | 7.1 | FreeRDP versions from 3.0.0 before 3.32.0 contain a null pointer dereference in the rdpsnd channel when a fragment sets… |
| 2026-10-14 23:17:22 | [CVE-2026-110830](https://nvd.nist.gov/vuln/detail/CVE-2026-110830) | High | 8.2 | FreeRDP before 3.32.0 fails to close prior serial handles in serial_process_irp_create, allowing a malicious RDP server… |
| 2026-10-14 23:17:22 | [CVE-2026-110831](https://nvd.nist.gov/vuln/detail/CVE-2026-110831) | Medium | 5.3 | FreeRDP versions 3.13.0 before 3.32.0 contain a resource retention flaw in drive_process_irp_create, which registers an… |
| 2026-10-14 23:17:22 | [CVE-2026-105627](https://nvd.nist.gov/vuln/detail/CVE-2026-105627) |  |  | Rejected reason: This CVE ID has been rejected or withdrawn by its CVE Numbering Authority. |
| 2026-10-14 23:17:23 | [CVE-2026-110832](https://nvd.nist.gov/vuln/detail/CVE-2026-110832) | High | 7.1 | FreeRDP from 2.0.0 before 3.32.0 contains a memory exhaustion vulnerability in wts_read_drdynvc_data_first that allows… |
| 2026-10-14 23:17:23 | [CVE-2026-110833](https://nvd.nist.gov/vuln/detail/CVE-2026-110833) | High | 8.2 | FreeRDP from 3.0.0-beta1 before 3.32.0 fails to enforce cumulative or absolute size limits when reassembling RDPDR chan… |
| 2026-10-14 23:17:23 | [CVE-2026-110834](https://nvd.nist.gov/vuln/detail/CVE-2026-110834) | High | 7.1 | FreeRDP from 2.0.0 before 3.32.0 contains a null pointer dereference vulnerability that allows malicious RDP servers to… |
| 2026-10-14 23:17:23 | [CVE-2026-110835](https://nvd.nist.gov/vuln/detail/CVE-2026-110835) | Medium | 6.3 | FreeRDP 3.0.0 before 3.32.0 allows HTTP header injection in its proxy because a lone LF in the target portion of a rout… |
| 2026-10-14 23:17:23 | [CVE-2026-110836](https://nvd.nist.gov/vuln/detail/CVE-2026-110836) | High | 7.1 | FreeRDP from 3.0.0 before 3.32.0 contains an infinite loop vulnerability in http_response_recv() that allows malicious… |
| 2026-10-14 23:17:23 | [CVE-2026-110837](https://nvd.nist.gov/vuln/detail/CVE-2026-110837) | Medium | 6.1 | FreeRDP 2.0.0 before 3.32.0, when built with WITH_LAME=ON and WITH_DSP_FFMPEG=OFF, has a heap-based buffer overflow in… |
| 2026-10-14 23:17:24 | [CVE-2026-110838](https://nvd.nist.gov/vuln/detail/CVE-2026-110838) | High | 8.7 | FreeRDP shadow server from 3.0.0 before 3.32.0 dispatches input PDUs during the Confirm Active state before authenticat… |
| 2026-10-14 23:17:24 | [CVE-2026-110839](https://nvd.nist.gov/vuln/detail/CVE-2026-110839) | High | 7.1 | FreeRDP 3.3.0 before 3.32.0, when built with WINPR_UTILS_IMAGE_JPEG=ON, has a heap-based out-of-bounds write in winpr_c… |
| 2026-10-14 23:17:24 | [CVE-2026-110840](https://nvd.nist.gov/vuln/detail/CVE-2026-110840) | High | 7.0 | n8n before 2.41.4 and 2.42.x before 2.42.1 contains an SQL injection vulnerability in version 1 of the Microsoft SQL no… |
| 2026-10-14 23:17:24 | [CVE-2026-110841](https://nvd.nist.gov/vuln/detail/CVE-2026-110841) | Medium | 6.1 | n8n before 2.41.4 and 2.42.0 contains an authorization bypass in the agent chat resume endpoint, which accepts a run id… |
| 2026-10-14 23:17:24 | [CVE-2026-110842](https://nvd.nist.gov/vuln/detail/CVE-2026-110842) | High | 7.7 | n8n before 2.41.4 and 2.42.x before 2.42.1 contains a prototype pollution vulnerability in the MCP workflow-validation… |
| 2026-10-14 23:17:24 | [CVE-2026-110843](https://nvd.nist.gov/vuln/detail/CVE-2026-110843) | High | 8.2 | n8n before 2.41.4 and 2.42.x before 2.42.1 contains an uncontrolled resource consumption vulnerability in the unauthent… |
| 2026-10-14 23:17:24 | [CVE-2026-110844](https://nvd.nist.gov/vuln/detail/CVE-2026-110844) | High | 7.2 | n8n before 1.123.83 contains an authorization bypass vulnerability that allows shared-workflow editors to use credentia… |
| 2026-10-14 23:17:25 | [CVE-2026-110845](https://nvd.nist.gov/vuln/detail/CVE-2026-110845) | High | 7.7 | n8n before 1.123.83, 2.x before 2.41.4, and 2.42.x before 2.42.1 contains a code execution vulnerability in the Git nod… |
| 2026-10-14 23:17:25 | [CVE-2026-110846](https://nvd.nist.gov/vuln/detail/CVE-2026-110846) | High | 7.0 | n8n before 2.41.4 and 2.42.x before 2.42.1 contains a signature bypass in the waiting-webhook endpoint, which selects S… |
| 2026-10-14 23:17:25 | [CVE-2026-110847](https://nvd.nist.gov/vuln/detail/CVE-2026-110847) | High | 7.0 | n8n before 1.123.83, 2.x before 2.41.4, and 2.42.x before 2.42.1 contains a stored cross-site scripting vulnerability i… |
| 2026-10-14 23:17:25 | [CVE-2026-110848](https://nvd.nist.gov/vuln/detail/CVE-2026-110848) | Medium | 6.0 | n8n before 1.123.83, 2.x before 2.41.4, and 2.42.x before 2.42.1 contains a prototype pollution vulnerability in the AI… |
| 2026-10-14 23:17:25 | [CVE-2026-110849](https://nvd.nist.gov/vuln/detail/CVE-2026-110849) | High | 7.2 | n8n before 1.123.83, 2.41.4, and 2.42.1 contains a stored cross-site scripting vulnerability in the file-preview modal,… |
| 2026-10-14 23:17:25 | [CVE-2026-110850](https://nvd.nist.gov/vuln/detail/CVE-2026-110850) | High | 7.2 | n8n before 2.41.4 and 2.42.0 before 2.42.1 does not validate credential ids stored in agent node parameters when an edi… |
| 2026-10-14 23:17:26 | [CVE-2026-110851](https://nvd.nist.gov/vuln/detail/CVE-2026-110851) | Medium | 6.1 | n8n before 2.41.4 and 2.42.x before 2.42.1 contains an authorization bypass in the Agents create endpoint, which accept… |
| 2026-10-14 23:17:26 | [CVE-2026-110852](https://nvd.nist.gov/vuln/detail/CVE-2026-110852) | Medium | 6.3 | n8n before 1.123.83, 2.x before 2.41.4, and 2.42.x before 2.42.1 contains an authentication bypass because dynamic-path… |
| 2026-10-14 23:17:26 | [CVE-2026-110853](https://nvd.nist.gov/vuln/detail/CVE-2026-110853) | High | 7.1 | n8n before 1.123.83 contains an authorization bypass vulnerability that allows authenticated members to spoof workflow… |
| 2026-10-14 23:17:26 | [CVE-2026-110854](https://nvd.nist.gov/vuln/detail/CVE-2026-110854) | High | 8.2 | Parse Server before 8.6.97 and 9.0.0 before 9.10.2-alpha.6 does not handle errors raised while sending verification or… |
| 2026-10-14 23:17:26 | [CVE-2026-110855](https://nvd.nist.gov/vuln/detail/CVE-2026-110855) | High | 7.1 | GitPython before 3.2.0 contains an information disclosure vulnerability that allows malicious repositories to expand en… |
| 2026-10-14 23:17:26 | [CVE-2026-110856](https://nvd.nist.gov/vuln/detail/CVE-2026-110856) | High | 8.7 | GitPython before 3.2.0 contains a regular expression denial of service vulnerability in the _re_actor_epoch pattern use… |
| 2026-10-14 23:17:26 | [CVE-2026-110857](https://nvd.nist.gov/vuln/detail/CVE-2026-110857) | High | 7.7 | GitPython before 3.2.0 contains a remote code execution vulnerability that allows attackers to run commands because Git… |
| 2026-10-14 23:17:27 | [CVE-2026-110858](https://nvd.nist.gov/vuln/detail/CVE-2026-110858) | Critical | 9.2 | GitPython from 3.1.30 before 3.2.0 contains a remote code execution vulnerability in Remote.pull() whose unsafe-option… |
| 2026-10-14 23:17:27 | [CVE-2026-110859](https://nvd.nist.gov/vuln/detail/CVE-2026-110859) | High | 8.7 | GitPython before 3.2.0 contains an argument injection vulnerability in Head.checkout() that allows remote attackers to… |
| 2026-10-14 23:17:27 | [CVE-2026-110860](https://nvd.nist.gov/vuln/detail/CVE-2026-110860) | Medium | 6.9 | GitPython from 3.1.62 before 3.2.0 contains a symlink-following flaw in Submodule.move(), which checks the destination… |
| 2026-10-14 23:17:27 | [CVE-2026-110861](https://nvd.nist.gov/vuln/detail/CVE-2026-110861) | Medium | 6.3 | Better Auth @better-auth/drizzle-adapter and better-auth from 1.6.17 before 1.7.7, and @better-auth/kysely-adapter from… |
| 2026-10-14 23:17:27 | [CVE-2026-110862](https://nvd.nist.gov/vuln/detail/CVE-2026-110862) | Critical | 9.3 | Better Auth from 1.4.0-beta.18 before 1.7.7 contains an authentication bypass vulnerability that allows unauthenticated… |
| 2026-10-14 23:17:27 | [CVE-2026-110863](https://nvd.nist.gov/vuln/detail/CVE-2026-110863) | High | 8.6 | Better Auth @better-auth/sso from 1.7.0-rc.2 before 1.7.3 contains an authentication bypass vulnerability that allows a… |
| 2026-10-14 23:17:27 | [CVE-2026-110864](https://nvd.nist.gov/vuln/detail/CVE-2026-110864) | Critical | 9.1 | Better Auth from 1.5.0-beta.12 before 1.7.7 contains an authentication bypass vulnerability in the OAuth Proxy plugin t… |
| 2026-10-14 23:17:28 | [CVE-2026-110865](https://nvd.nist.gov/vuln/detail/CVE-2026-110865) | High | 7.1 | Renovate before 44.60.1 contains an allowlist bypass vulnerability that allows repository users to evade the allowedHea… |
| 2026-10-14 23:17:28 | [CVE-2026-110866](https://nvd.nist.gov/vuln/detail/CVE-2026-110866) | Medium | 5.3 | Renovate before 44.61.3 contains a protection mechanism bypass vulnerability that allows minimumReleaseAge checks to be… |
| 2026-10-14 23:17:28 | [CVE-2026-110867](https://nvd.nist.gov/vuln/detail/CVE-2026-110867) | Critical | 9.0 | Renovate before 44.60.1 contains an allowlist bypass vulnerability that allows repositories to set restricted environme… |
| 2026-10-14 23:17:28 | [CVE-2026-110868](https://nvd.nist.gov/vuln/detail/CVE-2026-110868) | High | 8.4 | Renovate before 44.79.0 contains a server-side request forgery vulnerability that allows users to make the shared HTTP… |
| 2026-10-14 23:17:28 | [CVE-2026-110869](https://nvd.nist.gov/vuln/detail/CVE-2026-110869) | High | 8.7 | Nodemailer 3.0.0 before 10.0.13 has a regular expression denial of service in SMTPConnection._actionEHLO, whose four AU… |
| 2026-10-14 23:17:28 | [CVE-2026-110870](https://nvd.nist.gov/vuln/detail/CVE-2026-110870) | Medium | 6.9 | Nodemailer from 3.0.0 before 10.0.13 contains an improper input validation vulnerability in its address parser that fai… |
| 2026-10-14 23:17:28 | [CVE-2026-110871](https://nvd.nist.gov/vuln/detail/CVE-2026-110871) | High | 7.1 | Nodemailer from 3.0.0 before 10.0.10 contains a denial of service vulnerability in MessageParser.parseHeaders that allo… |
| 2026-10-14 23:17:29 | [CVE-2026-110872](https://nvd.nist.gov/vuln/detail/CVE-2026-110872) | High | 8.2 | Nodemailer from 3.0.0 before 10.0.10 contains a quadratic complexity denial of service vulnerability in the SMTP client… |
| 2026-10-14 23:17:29 | [CVE-2026-110873](https://nvd.nist.gov/vuln/detail/CVE-2026-110873) | High | 7.1 | Heym from 0.0.55 before 0.0.121 contains a privilege escalation vulnerability that allows shared collaborators to overw… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
