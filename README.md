# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-20 20:22 UTC

New CVEs published between 2026-10-20 19:20 UTC and 2026-10-20 20:22 UTC.

[Full CSV](data/new-cves-2026-10-20T20-22-21-494193Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-10-20 20:17:14 | [CVE-2026-107692](https://nvd.nist.gov/vuln/detail/CVE-2026-107692) |  |  | The War Thunder game client transmits its authentication bearer token (auth_jwt) in the very first data packet after th… |
| 2026-10-20 20:17:16 | [CVE-2026-112380](https://nvd.nist.gov/vuln/detail/CVE-2026-112380) | Critical | 9.0 | Missing authorization in the WhatsApp group channel in Kiro Crew might allow a remote actor who is a member of an opera… |
| 2026-10-20 20:17:17 | [CVE-2026-113715](https://nvd.nist.gov/vuln/detail/CVE-2026-113715) | Low | 2.0 | virtualenv is a tool for creating isolated virtual python environments. Prior to 21.14.9, the stdlib venv creator reads… |
| 2026-10-20 20:17:17 | [CVE-2026-113716](https://nvd.nist.gov/vuln/detail/CVE-2026-113716) | Medium | 4.5 | virtualenv is a tool for creating isolated virtual python environments. Prior to 21.14.9, the builtin creator calls ens… |
| 2026-10-20 20:17:18 | [CVE-2026-113717](https://nvd.nist.gov/vuln/detail/CVE-2026-113717) | Low | 2.3 | virtualenv is a tool for creating isolated virtual python environments. Prior to 21.14.9, PipInvoke.get_pip_install_cmd… |
| 2026-10-20 20:17:18 | [CVE-2026-113718](https://nvd.nist.gov/vuln/detail/CVE-2026-113718) | High | 7.1 | virtualenv is a tool for creating isolated virtual python environments. Prior to 21.14.9, POSIX xonsh activation quote(… |
| 2026-10-20 20:17:18 | [CVE-2026-113719](https://nvd.nist.gov/vuln/detail/CVE-2026-113719) | Medium | 4.5 | virtualenv is a tool for creating isolated virtual python environments. Prior to 21.14.9, PipInstall._uninstall_previou… |
| 2026-10-20 20:17:18 | [CVE-2026-113720](https://nvd.nist.gov/vuln/detail/CVE-2026-113720) | Medium | 4.4 | virtualenv is a tool for creating isolated virtual python environments. Prior to 21.14.9, the app-data copy seeder uses… |
| 2026-10-20 20:17:18 | [CVE-2026-113721](https://nvd.nist.gov/vuln/detail/CVE-2026-113721) | Medium | 4.5 | virtualenv is a tool for creating isolated virtual python environments. Prior to 21.14.9, ViaTemplateActivator._generat… |
| 2026-10-20 20:17:18 | [CVE-2026-113722](https://nvd.nist.gov/vuln/detail/CVE-2026-113722) | High | 7.8 | virtualenv is a tool for creating isolated virtual python environments. Prior to 21.14.9, virtualenv's ScriptMakerCusto… |
| 2026-10-20 20:17:18 | [CVE-2026-113723](https://nvd.nist.gov/vuln/detail/CVE-2026-113723) | High | 7.1 | virtualenv is a tool for creating isolated virtual python environments. Prior to 21.14.9, caller-supplied prompt text c… |
| 2026-10-20 20:17:19 | [CVE-2026-113724](https://nvd.nist.gov/vuln/detail/CVE-2026-113724) | Medium | 4.5 | virtualenv is a tool for creating isolated virtual python environments. Prior to 21.14.9, the safe_delete() deletion er… |
| 2026-10-20 20:17:19 | [CVE-2026-113725](https://nvd.nist.gov/vuln/detail/CVE-2026-113725) | High | 7.8 | virtualenv is a tool for creating isolated virtual python environments. Prior to 21.14.7, the bash activate script esca… |
| 2026-10-20 20:17:19 | [CVE-2026-113866](https://nvd.nist.gov/vuln/detail/CVE-2026-113866) | Medium | 5.9 | When setting up an account, Thunderbird's Exchange AutoDiscover lookup also queried the domain's AutoDiscover service o… |
| 2026-10-20 20:17:19 | [CVE-2026-113867](https://nvd.nist.gov/vuln/detail/CVE-2026-113867) |  |  | Thunderbird did not escape attribute values when serializing outgoing XMPP stanzas. Because values from incoming reques… |
| 2026-10-20 20:17:19 | [CVE-2026-113868](https://nvd.nist.gov/vuln/detail/CVE-2026-113868) | Medium | 5.3 | When authenticating to a POP3 or SMTP server using NTLM, Thunderbird did not check whether the server's challenge was v… |
| 2026-10-20 20:17:19 | [CVE-2026-113869](https://nvd.nist.gov/vuln/detail/CVE-2026-113869) | Medium | 5.4 | When Thunderbird asked for a security device password (for example a smartcard PIN or the Primary Password) while decry… |
| 2026-10-20 20:17:25 | [CVE-2026-86409](https://nvd.nist.gov/vuln/detail/CVE-2026-86409) |  |  | Setting `CURLOPT_AWS_SIGV4` to NULL but does not disable SigV4 authentication, contrary to expectations and documentati… |
| 2026-10-20 20:17:25 | [CVE-2026-86410](https://nvd.nist.gov/vuln/detail/CVE-2026-86410) |  |  | A flaw in the curl command line tool's logic makes it only set SSH host verification options when interacting directly… |
| 2026-10-20 20:17:25 | [CVE-2026-86411](https://nvd.nist.gov/vuln/detail/CVE-2026-86411) |  |  | An `ftp://` transfer configured with `CURLUSESSL_NONE` can reuse a pooled FTP control connection that a previous easy h… |
| 2026-10-20 20:17:25 | [CVE-2026-86412](https://nvd.nist.gov/vuln/detail/CVE-2026-86412) |  |  | A remote HTTP server can set a cookie that curl accepts and writes to a Netscape cookie jar but cannot reload. On the n… |
| 2026-10-20 20:17:25 | [CVE-2026-86413](https://nvd.nist.gov/vuln/detail/CVE-2026-86413) |  |  | When using an *ambient user* in a first transfer doing Negotiate authentication and asked to follow redirects, curl cou… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
