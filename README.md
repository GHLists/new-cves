# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-09-26 03:19 UTC

New CVEs published between 2026-09-26 02:20 UTC and 2026-09-26 03:19 UTC.

[Full CSV](data/new-cves-2026-09-26T03-19-59-177953Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-09-26 03:16:57 | [CVE-2026-100525](https://nvd.nist.gov/vuln/detail/CVE-2026-100525) | Medium | 5.3 | The OpenClaw Prometheus diagnostics plugin (@openclaw/diagnostics-prometheus) before version 2026.9.3 does not enforce… |
| 2026-09-26 03:16:57 | [CVE-2026-100526](https://nvd.nist.gov/vuln/detail/CVE-2026-100526) | Medium | 6.0 | OpenClaw's Discord integration (npm package @openclaw/discord) before version 2026.9.3 could lose the sender-scoped med… |
| 2026-09-26 03:16:57 | [CVE-2026-100527](https://nvd.nist.gov/vuln/detail/CVE-2026-100527) | Medium | 6.9 | OpenClaw before 2026.8.2 contains a denial of service vulnerability in the Browser extension relay that allows unauthen… |
| 2026-09-26 03:16:58 | [CVE-2026-100528](https://nvd.nist.gov/vuln/detail/CVE-2026-100528) | Medium | 5.9 | OpenClaw (npm package 'openclaw') before 2026.8.1 could send third-party provider credentials to the wrong endpoint. In… |
| 2026-09-26 03:16:58 | [CVE-2026-100529](https://nvd.nist.gov/vuln/detail/CVE-2026-100529) | High | 7.4 | OpenClaw versions before 2026.8.1 contain an authorization scope widening vulnerability in file-transfer allow-always a… |
| 2026-09-26 03:16:58 | [CVE-2026-100530](https://nvd.nist.gov/vuln/detail/CVE-2026-100530) | High | 8.5 | OpenClaw versions before 2026.8.1 fail to bind working directory context to reusable exec approvals, allowing approved… |
| 2026-09-26 03:16:58 | [CVE-2026-100531](https://nvd.nist.gov/vuln/detail/CVE-2026-100531) | High | 7.1 | The @openclaw/slack npm package before 2026.8.1 contains an authorization flaw in its Slack download-file handler: when… |
| 2026-09-26 03:16:58 | [CVE-2026-100532](https://nvd.nist.gov/vuln/detail/CVE-2026-100532) | High | 7.2 | @openclaw/whatsapp (npm) before 2026.8.1 exposes the WhatsApp login tool through the generic channel-tool path without… |
| 2026-09-26 03:16:58 | [CVE-2026-100533](https://nvd.nist.gov/vuln/detail/CVE-2026-100533) | Medium | 6.0 | OpenClaw versions before 2026.8.1 contain a path traversal vulnerability in the tools.fs.workspaceOnly feature where Un… |
| 2026-09-26 03:16:58 | [CVE-2026-100534](https://nvd.nist.gov/vuln/detail/CVE-2026-100534) | Low | 2.3 | OpenClaw versions before 2026.8.1 contain an authorization bypass vulnerability in webhook TaskFlow cancellation that a… |
| 2026-09-26 03:16:59 | [CVE-2026-100535](https://nvd.nist.gov/vuln/detail/CVE-2026-100535) | High | 7.7 | OpenClaw (npm package 'openclaw') versions >= 2026.4.5 and < 2026.8.1 can lose the originating requester's restrictions… |
| 2026-09-26 03:16:59 | [CVE-2026-100536](https://nvd.nist.gov/vuln/detail/CVE-2026-100536) | High | 7.1 | OpenClaw versions before 2026.8.1 fail to validate all source fields in structured message attachments, allowing attack… |
| 2026-09-26 03:16:59 | [CVE-2026-100537](https://nvd.nist.gov/vuln/detail/CVE-2026-100537) | Low | 2.3 | OpenClaw (npm package 'openclaw') before 2026.8.1 fails to apply the originating requester's effective tool policy duri… |
| 2026-09-26 03:16:59 | [CVE-2026-100538](https://nvd.nist.gov/vuln/detail/CVE-2026-100538) | High | 7.1 | OpenClaw (npm package 'openclaw') before 2026.8.1 does not apply the originating sender's global or per-agent toolsBySe… |
| 2026-09-26 03:16:59 | [CVE-2026-100539](https://nvd.nist.gov/vuln/detail/CVE-2026-100539) | Low | 2.1 | OpenClaw (npm package 'openclaw') before 2026.8.1 fails to revoke memory tool access when an operator hot-disables memo… |
| 2026-09-26 03:16:59 | [CVE-2026-100540](https://nvd.nist.gov/vuln/detail/CVE-2026-100540) | High | 7.6 | OpenClaw Feishu before 2026.8.1 fails to validate whether a configured default account is disabled before selecting it… |
| 2026-09-26 03:16:59 | [CVE-2026-100541](https://nvd.nist.gov/vuln/detail/CVE-2026-100541) | High | 7.7 | OpenClaw's Matrix integration (npm package @openclaw/matrix) versions >= 2026.2.2 and < 2026.8.1 lowercase complete Mat… |
| 2026-09-26 03:17:00 | [CVE-2026-100542](https://nvd.nist.gov/vuln/detail/CVE-2026-100542) | Low | 2.3 | OpenClaw (npm package 'openclaw') versions >= 2026.5.28 and < 2026.8.1 mishandle archive listings in the tar.bz2 skill… |
| 2026-09-26 03:17:00 | [CVE-2026-100543](https://nvd.nist.gov/vuln/detail/CVE-2026-100543) | High | 7.7 | OpenClaw (npm package openclaw) before 2026.8.1 could include deterministic hashes computed over the original, unredact… |
| 2026-09-26 03:17:00 | [CVE-2026-100544](https://nvd.nist.gov/vuln/detail/CVE-2026-100544) | High | 8.7 | openclaw's @openclaw/voice-call package before 2026.8.1 launches the configured agent for classic inbound voice calls w… |
| 2026-09-26 03:17:00 | [CVE-2026-100545](https://nvd.nist.gov/vuln/detail/CVE-2026-100545) | Medium | 6.0 | OpenClaw (npm package `openclaw`) before 2026.8.1 incorrectly enforces sender tool policies during session-memory filen… |
| 2026-09-26 03:17:00 | [CVE-2026-100546](https://nvd.nist.gov/vuln/detail/CVE-2026-100546) | Medium | 6.1 | OpenClaw (npm package `openclaw`) versions >= 2026.7.2 and < 2026.9.2 contain a race condition in the Discord realtime… |
| 2026-09-26 03:17:00 | [CVE-2026-100547](https://nvd.nist.gov/vuln/detail/CVE-2026-100547) | Medium | 6.8 | OpenClaw is a coding agent distributed as the npm package `openclaw`. In affected versions (2026.7.1 through 2026.7.2),… |
| 2026-09-26 03:17:01 | [CVE-2026-100548](https://nvd.nist.gov/vuln/detail/CVE-2026-100548) | Medium | 6.0 | OpenClaw (npm package 'openclaw') versions >= 2026.3.28 and < 2026.8.1 contain a credential exposure issue in memory em… |
| 2026-09-26 03:17:01 | [CVE-2026-100549](https://nvd.nist.gov/vuln/detail/CVE-2026-100549) | Medium | 5.3 | OpenClaw versions before 2026.8.1 contain a path traversal vulnerability in QQBot voice attachment handling where filen… |
| 2026-09-26 03:17:01 | [CVE-2026-100550](https://nvd.nist.gov/vuln/detail/CVE-2026-100550) | Medium | 5.3 | OpenClaw (npm package 'openclaw') before 2026.8.1 contains an access-control bypass in the Microsoft Teams integration.… |
| 2026-09-26 03:17:01 | [CVE-2026-100551](https://nvd.nist.gov/vuln/detail/CVE-2026-100551) | Critical | 9.0 | OpenClaw for iOS versions >= 2026.7.1 and < 2026.8.11 do not enforce saved Gateway TLS pins in the Control UI. While na… |
| 2026-09-26 03:17:01 | [CVE-2026-100552](https://nvd.nist.gov/vuln/detail/CVE-2026-100552) | High | 8.7 | OpenClaw (npm package 'openclaw') before 2026.8.1 does not correctly enforce per-chat tool policies for Codex app-serve… |
| 2026-09-26 03:17:01 | [CVE-2026-100553](https://nvd.nist.gov/vuln/detail/CVE-2026-100553) | Medium | 5.3 | OpenClaw versions >= 2026.6.9 and < 2026.8.1 do not declare the native chatId parameter as a delivery target in the Fei… |
| 2026-09-26 03:17:01 | [CVE-2026-100554](https://nvd.nist.gov/vuln/detail/CVE-2026-100554) | Low | 2.3 | OpenClaw (npm package 'openclaw') versions >= 2026.5.12 and < 2026.8.1 do not immediately invalidate Canvas HTTP author… |
| 2026-09-26 03:17:02 | [CVE-2026-100555](https://nvd.nist.gov/vuln/detail/CVE-2026-100555) | High | 7.1 | OpenClaw is an npm-distributed gateway application. In versions >= 2026.7.1 and < 2026.8.1, Synology Chat attachment de… |
| 2026-09-26 03:17:02 | [CVE-2026-100556](https://nvd.nist.gov/vuln/detail/CVE-2026-100556) | Medium | 5.3 | OpenClaw (npm package openclaw) versions >= 2026.5.2 and < 2026.8.1 contain an incorrect authorization vulnerability in… |
| 2026-09-26 03:17:02 | [CVE-2026-100557](https://nvd.nist.gov/vuln/detail/CVE-2026-100557) | High | 8.7 | OpenClaw versions before 2026.8.1 contain an authorization bypass vulnerability in skill tool dispatch that fails to ca… |
| 2026-09-26 03:17:02 | [CVE-2026-100558](https://nvd.nist.gov/vuln/detail/CVE-2026-100558) | High | 8.7 | OpenClaw versions before 2026.8.1 contain a resource exhaustion vulnerability in the Gateway listener that allows unaut… |
| 2026-09-26 03:17:02 | [CVE-2026-100559](https://nvd.nist.gov/vuln/detail/CVE-2026-100559) | High | 8.6 | OpenClaw versions before 2026.8.1 contain a command parser vulnerability where escaped newlines confuse exec allowlist… |
| 2026-09-26 03:17:02 | [CVE-2026-100560](https://nvd.nist.gov/vuln/detail/CVE-2026-100560) | High | 7.7 | OpenClaw versions before 2026.8.1 contain an authorization bypass vulnerability where Allow Always approvals for exact… |
| 2026-09-26 03:17:02 | [CVE-2026-100561](https://nvd.nist.gov/vuln/detail/CVE-2026-100561) | High | 8.6 | OpenClaw (npm package 'openclaw') versions >= 2026.3.22 and < 2026.8.1 contain an approval-bypass flaw in the exec appr… |
| 2026-09-26 03:17:03 | [CVE-2026-100562](https://nvd.nist.gov/vuln/detail/CVE-2026-100562) | Medium | 5.3 | OpenClaw versions before 2026.8.1 contain an authorization bypass vulnerability in the sessions.create endpoint that al… |
| 2026-09-26 03:17:03 | [CVE-2026-100563](https://nvd.nist.gov/vuln/detail/CVE-2026-100563) | Medium | 5.3 | OpenClaw (npm package `openclaw`) before 2026.8.1 does not neutralize leading characters that spreadsheet applications… |
| 2026-09-26 03:17:03 | [CVE-2026-100564](https://nvd.nist.gov/vuln/detail/CVE-2026-100564) | Medium | 5.3 | OpenClaw versions before 2026.8.1 fail to neutralize spreadsheet formula characters in participant display names within… |
| 2026-09-26 03:17:03 | [CVE-2026-100566](https://nvd.nist.gov/vuln/detail/CVE-2026-100566) | Medium | 6.9 | OpenClaw LINE versions before 2026.8.1 contain an access control vulnerability where group allowlist mode silently inhe… |
| 2026-09-26 03:17:03 | [CVE-2026-100567](https://nvd.nist.gov/vuln/detail/CVE-2026-100567) | High | 8.9 | OpenClaw is an agent gateway distributed as the npm package 'openclaw'. In versions >= 2026.4.5 and < 2026.8.1, the Gat… |
| 2026-09-26 03:17:03 | [CVE-2026-100568](https://nvd.nist.gov/vuln/detail/CVE-2026-100568) | High | 8.7 | OpenClaw versions before 2026.8.1 fail to properly restrict access to operator command cron jobs, allowing model-visibl… |
| 2026-09-26 03:17:04 | [CVE-2026-100569](https://nvd.nist.gov/vuln/detail/CVE-2026-100569) | Medium | 6.8 | OpenClaw is an npm-distributed application. In versions >= 2026.4.25 and < 2026.8.1, the workspace environment-variable… |
| 2026-09-26 03:17:04 | [CVE-2026-100570](https://nvd.nist.gov/vuln/detail/CVE-2026-100570) | High | 8.5 | OpenClaw (npm package 'openclaw') versions >= 2026.3.28 and < 2026.8.1 allow an untrusted workspace .env file to set th… |
| 2026-09-26 03:17:04 | [CVE-2026-100571](https://nvd.nist.gov/vuln/detail/CVE-2026-100571) | Medium | 6.9 | OpenClaw (npm package 'openclaw') versions >= 2026.6.6 and < 2026.8.1 apply the SMS webhook invalid-request rate limit… |
| 2026-09-26 03:17:04 | [CVE-2026-100572](https://nvd.nist.gov/vuln/detail/CVE-2026-100572) | Medium | 6.9 | OpenClaw versions >= 2026.3.25 and < 2026.8.1 apply invalid-token rate limiting for Synology Chat webhooks before authe… |
| 2026-09-26 03:17:04 | [CVE-2026-100573](https://nvd.nist.gov/vuln/detail/CVE-2026-100573) | Medium | 4.8 | OpenClaw versions before 2026.8.1 contain a sandbox policy bypass vulnerability in the MCP loopback component that allo… |
| 2026-09-26 03:17:04 | [CVE-2026-100574](https://nvd.nist.gov/vuln/detail/CVE-2026-100574) | High | 8.2 | OpenClaw (npm package 'openclaw') before 2026.8.1 contains a server-side request forgery vulnerability in its trusted-h… |
| 2026-09-26 03:17:05 | [CVE-2026-100575](https://nvd.nist.gov/vuln/detail/CVE-2026-100575) | High | 8.7 | OpenClaw Slack versions before 2026.8.1 fail to properly enforce sender allowlists in multi-person direct messages. Dis… |
| 2026-09-26 03:17:05 | [CVE-2026-100576](https://nvd.nist.gov/vuln/detail/CVE-2026-100576) | Medium | 5.3 | OpenClaw versions before 2026.8.1 contain a server-side request forgery vulnerability in browser wait predicates that a… |
| 2026-09-26 03:17:05 | [CVE-2026-100577](https://nvd.nist.gov/vuln/detail/CVE-2026-100577) | Medium | 5.3 | OpenClaw versions before 2026.8.1 fail to validate video asset URLs returned by providers, allowing server-side request… |
| 2026-09-26 03:17:05 | [CVE-2026-100578](https://nvd.nist.gov/vuln/detail/CVE-2026-100578) | High | 7.2 | OpenClaw (npm package `openclaw`) before 2026.7.1 fails to restrict owner-only infrastructure tools exposed through the… |
| 2026-09-26 03:17:05 | [CVE-2026-100579](https://nvd.nist.gov/vuln/detail/CVE-2026-100579) | High | 7.2 | OpenClaw (npm package 'openclaw') before 2026.7.1 incorrectly trusts requester provenance in message.action. In identit… |
| 2026-09-26 03:17:05 | [CVE-2026-100580](https://nvd.nist.gov/vuln/detail/CVE-2026-100580) | High | 8.7 | OpenClaw (npm package 'openclaw') before 2026.7.1 improperly handles case sensitivity in the model-facing cron tool: a… |
| 2026-09-26 03:17:05 | [CVE-2026-100581](https://nvd.nist.gov/vuln/detail/CVE-2026-100581) | Medium | 6.8 | OpenClaw for iOS before 2026.8.11 stores Gateway credentials as cleartext JSON in App Group UserDefaults instead of the… |
| 2026-09-26 03:17:06 | [CVE-2026-100582](https://nvd.nist.gov/vuln/detail/CVE-2026-100582) | High | 7.1 | OpenClaw channel plugins (@openclaw/msteams, @openclaw/feishu, @openclaw/matrix, and @openclaw/googlechat) before 2026.… |
| 2026-09-26 03:17:06 | [CVE-2026-100583](https://nvd.nist.gov/vuln/detail/CVE-2026-100583) | Medium | 5.3 | OpenClaw Discord versions before 2026.7.1 contain an authorization bypass vulnerability in guild metadata read actions… |
| 2026-09-26 03:17:06 | [CVE-2026-100584](https://nvd.nist.gov/vuln/detail/CVE-2026-100584) | Medium | 5.4 | OpenClaw is an npm-distributed agent runtime. In versions >= 2026.2.26 and < 2026.7.1, PowerShell command analysis on W… |
| 2026-09-26 03:17:06 | [CVE-2026-100585](https://nvd.nist.gov/vuln/detail/CVE-2026-100585) | High | 8.6 | OpenClaw (npm package `openclaw`) before 2026.7.1 fails to enforce the owner-only authorization requirement for Claude… |
| 2026-09-26 03:17:06 | [CVE-2026-100586](https://nvd.nist.gov/vuln/detail/CVE-2026-100586) | High | 8.7 | OpenClaw Codex before 2026.7.1 fails to properly enforce owner authorization when creating native conversation bindings… |
| 2026-09-26 03:17:06 | [CVE-2026-100587](https://nvd.nist.gov/vuln/detail/CVE-2026-100587) | High | 8.7 | OpenClaw versions before 2026.7.1 fail to properly validate owner authorization in the Codex computer-use installation… |
| 2026-09-26 03:17:06 | [CVE-2026-100588](https://nvd.nist.gov/vuln/detail/CVE-2026-100588) | High | 8.7 | OpenClaw (npm package 'openclaw') before 2026.7.1 does not enforce the administrator scope requirement on browser contr… |
| 2026-09-26 03:17:07 | [CVE-2026-100589](https://nvd.nist.gov/vuln/detail/CVE-2026-100589) | High | 8.7 | OpenClaw versions before 2026.7.1 contain a sandbox bypass vulnerability in the browser tool that allows sandboxed sess… |
| 2026-09-26 03:17:07 | [CVE-2026-100590](https://nvd.nist.gov/vuln/detail/CVE-2026-100590) | Medium | 5.3 | OpenClaw before 2026.7.1 contains an authorization bypass vulnerability in the /voice set command that allows non-owner… |
| 2026-09-26 03:17:07 | [CVE-2026-100591](https://nvd.nist.gov/vuln/detail/CVE-2026-100591) | Medium | 5.3 | OpenClaw is an npm-distributed agent gateway. In versions before 2026.7.1, the global Active Memory toggle mutations co… |
| 2026-09-26 03:17:07 | [CVE-2026-100592](https://nvd.nist.gov/vuln/detail/CVE-2026-100592) | Medium | 5.3 | OpenClaw is an agent gateway distributed via npm. In versions >= 2026.4.10 and < 2026.7.1, persistent memory dreaming m… |
| 2026-09-26 03:17:07 | [CVE-2026-100593](https://nvd.nist.gov/vuln/detail/CVE-2026-100593) | Medium | 5.3 | OpenClaw (npm package `openclaw`) before 2026.7.1 does not enforce the documented owner-only requirement for persistent… |
| 2026-09-26 03:17:07 | [CVE-2026-100594](https://nvd.nist.gov/vuln/detail/CVE-2026-100594) | High | 7.1 | OpenClaw versions before 2026.7.1 contain an authorization bypass vulnerability in the /export-trajectory endpoint that… |
| 2026-09-26 03:17:08 | [CVE-2026-100595](https://nvd.nist.gov/vuln/detail/CVE-2026-100595) | High | 7.1 | OpenClaw versions before 2026.7.1 contain an authorization bypass vulnerability in the diagnostics export command that… |
| 2026-09-26 03:17:08 | [CVE-2026-100596](https://nvd.nist.gov/vuln/detail/CVE-2026-100596) | High | 8.7 | OpenClaw versions before 2026.7.1 fail to properly authorize non-owner users executing MCP configuration changes throug… |
| 2026-09-26 03:17:08 | [CVE-2026-100597](https://nvd.nist.gov/vuln/detail/CVE-2026-100597) | High | 8.8 | OpenClaw (npm package 'openclaw') before 2026.7.1 is vulnerable to a time-of-check time-of-use race condition in OpenSh… |
| 2026-09-26 03:17:08 | [CVE-2026-100598](https://nvd.nist.gov/vuln/detail/CVE-2026-100598) | High | 7.5 | OpenClaw (npm package openclaw) before 2026.7.1 incorrectly binds Signal approval reactions. In affected versions, a re… |
| 2026-09-26 03:17:08 | [CVE-2026-100599](https://nvd.nist.gov/vuln/detail/CVE-2026-100599) | High | 8.7 | OpenClaw versions 2026.5.1 through 2026.7.0 fail to apply the configured exec approval path to Google Meet node command… |
| 2026-09-26 03:17:08 | [CVE-2026-15273](https://nvd.nist.gov/vuln/detail/CVE-2026-15273) | Medium | 6.4 | The Automatic.css plugin for WordPress is vulnerable to Stored Cross-Site Scripting via REQUEST_URI in all version 4.0.… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
