# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-09-30 00:19 UTC

New CVEs published between 2026-09-29 23:18 UTC and 2026-09-30 00:19 UTC.

[Full CSV](data/new-cves-2026-09-30T00-19-55-507818Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-09-30 00:16:33 | [CVE-2026-102793](https://nvd.nist.gov/vuln/detail/CVE-2026-102793) | High | 8.5 | A flaw has been found in Ziroom ZHOME A0101 1.0.1.0. This vulnerability affects the function set_time_zone of the file… |
| 2026-09-30 00:16:34 | [CVE-2026-102794](https://nvd.nist.gov/vuln/detail/CVE-2026-102794) | High | 8.5 | A vulnerability has been found in Ziroom ZHOME A0101 1.0.1.0. This issue affects some unknown processing of the file /a… |
| 2026-09-30 00:16:35 | [CVE-2026-103048](https://nvd.nist.gov/vuln/detail/CVE-2026-103048) |  |  | URL redirection to untrusted site ('open redirect') vulnerability in The Wikimedia Foundation Mediawiki - Collection ex… |
| 2026-09-30 00:16:35 | [CVE-2026-103049](https://nvd.nist.gov/vuln/detail/CVE-2026-103049) |  |  | Improper neutralization of input during web page generation ('cross-site scripting') vulnerability in The Wikimedia Fou… |
| 2026-09-30 00:16:35 | [CVE-2026-103050](https://nvd.nist.gov/vuln/detail/CVE-2026-103050) |  |  | Improper neutralization of input during web page generation ('cross-site scripting') vulnerability in The Wikimedia Fou… |
| 2026-09-30 00:16:35 | [CVE-2026-103051](https://nvd.nist.gov/vuln/detail/CVE-2026-103051) |  |  | Improper neutralization of input during web page generation ('cross-site scripting') vulnerability in The Wikimedia Fou… |
| 2026-09-30 00:16:35 | [CVE-2026-13046](https://nvd.nist.gov/vuln/detail/CVE-2026-13046) | High | 7.5 | A deserialization of untrusted data vulnerability in WatchGuard Fireware OS's SAML single sign-on session handling (sam… |
| 2026-09-30 00:16:35 | [CVE-2026-13224](https://nvd.nist.gov/vuln/detail/CVE-2026-13224) | High | 8.2 | A path traversal vulnerability in the Fireware OS WebUI management agent allows an authenticated administrator to read… |
| 2026-09-30 00:16:35 | [CVE-2026-18105](https://nvd.nist.gov/vuln/detail/CVE-2026-18105) | High | 7.1 | An uncontrolled resource consumption vulnerability in Fireware OS's diagnostic tasks feature allows a low-privileged, a… |
| 2026-09-30 00:16:36 | [CVE-2026-18145](https://nvd.nist.gov/vuln/detail/CVE-2026-18145) | High | 8.6 | A stack-based buffer overflow vulnerability in the spamBlocker (spamd) service of WatchGuard Fireware OS allows an auth… |
| 2026-09-30 00:16:36 | [CVE-2026-81433](https://nvd.nist.gov/vuln/detail/CVE-2026-81433) | High | 8.7 | A stack-based buffer overflow vulnerability in WatchGuard Fireware OS's DHCP fingerprinting daemon (fingerd) allows an… |
| 2026-09-30 00:16:36 | [CVE-2026-86101](https://nvd.nist.gov/vuln/detail/CVE-2026-86101) | High | 7.2 | An improper authorization vulnerability in WatchGuard Fireware OS's SAML login process allows a remote, authenticated S… |
| 2026-09-30 00:16:36 | [CVE-2026-86104](https://nvd.nist.gov/vuln/detail/CVE-2026-86104) | High | 8.7 | An uncontrolled resource consumption vulnerability in the Fireware OS login process (wgagent) allows a remote, unauthen… |
| 2026-09-30 00:16:36 | [CVE-2026-86105](https://nvd.nist.gov/vuln/detail/CVE-2026-86105) | Medium | 6.0 | An improper authorization vulnerability in Fireware OS's Access Portal reverse proxy allows an authenticated, low-privi… |
| 2026-09-30 00:16:36 | [CVE-2026-86128](https://nvd.nist.gov/vuln/detail/CVE-2026-86128) | High | 8.2 | A NULL pointer dereference vulnerability in Fireware OS's NetFlow packet-processing feature allows a remote, unauthenti… |
| 2026-09-30 00:16:36 | [CVE-2026-86131](https://nvd.nist.gov/vuln/detail/CVE-2026-86131) | Critical | 9.2 | A code injection vulnerability in WatchGuard Fireware OS's BOVPN Over TLS client configuration handling allows an attac… |
| 2026-09-30 00:16:36 | [CVE-2026-86132](https://nvd.nist.gov/vuln/detail/CVE-2026-86132) | High | 8.2 | An integer underflow vulnerability in the WatchGuard Fireware OS IKEv2 daemon (iked) allows a remote, unauthenticated a… |
| 2026-09-30 00:16:37 | [CVE-2026-86133](https://nvd.nist.gov/vuln/detail/CVE-2026-86133) | High | 8.2 | An integer underflow vulnerability in the WatchGuard Fireware OS IKE daemon (iked) allows a remote attacker who has com… |
| 2026-09-30 00:16:37 | [CVE-2026-86136](https://nvd.nist.gov/vuln/detail/CVE-2026-86136) | High | 7.1 | A missing authorization vulnerability in the wgagent management daemon's session initialization function allows an auth… |
| 2026-09-30 00:16:37 | [CVE-2026-90441](https://nvd.nist.gov/vuln/detail/CVE-2026-90441) | High | 7.1 | A missing authorization vulnerability in the wgagent management daemon's session initialization function allows an auth… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
