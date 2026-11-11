# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-11-11 17:19 UTC

New CVEs published between 2026-11-11 16:20 UTC and 2026-11-11 17:19 UTC.

[Full CSV](data/new-cves-2026-11-11T17-19-29-21626Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-11-11 17:17:14 | [CVE-2026-110697](https://nvd.nist.gov/vuln/detail/CVE-2026-110697) | Critical | 9.9 | A flaw was found in Quay where the robot account listing function constructs a SQL LIKE pattern from user-controlled na… |
| 2026-11-11 17:17:16 | [CVE-2026-116633](https://nvd.nist.gov/vuln/detail/CVE-2026-116633) | Medium | 6.9 | A potential vulnerability was reported in some Lenovo Tablets that could allow a third-party application to perform an… |
| 2026-11-11 17:17:16 | [CVE-2026-119233](https://nvd.nist.gov/vuln/detail/CVE-2026-119233) |  |  | proxygen's HTTP/3 codec buffered an incomplete non-DATA frame, such as a control-stream frame, a frame of an unknown or… |
| 2026-11-11 17:17:16 | [CVE-2026-119234](https://nvd.nist.gov/vuln/detail/CVE-2026-119234) |  |  | mvfst did not adequately merge or compact out-of-order STREAM frame data, and a small received fragment could keep a mu… |
| 2026-11-11 17:17:16 | [CVE-2026-119235](https://nvd.nist.gov/vuln/detail/CVE-2026-119235) |  |  | proxygen's QPACK decoder enforced its size limit on a string literal in an encoder-stream instruction only after the en… |
| 2026-11-11 17:17:16 | [CVE-2026-119236](https://nvd.nist.gov/vuln/detail/CVE-2026-119236) |  |  | An mvfst QUIC server retained CRYPTO frame data received at an encryption level (Initial or Handshake) that the TLS han… |
| 2026-11-11 17:17:16 | [CVE-2026-119237](https://nvd.nist.gov/vuln/detail/CVE-2026-119237) |  |  | In proxygen's HTTP/3 session, when a HEADERS block referenced QPACK dynamic table entries that had not yet been receive… |
| 2026-11-11 17:17:17 | [CVE-2026-119238](https://nvd.nist.gov/vuln/detail/CVE-2026-119238) | Medium | 4.8 | A potential improper permissions vulnerability was reported in Lenovo XiangBangbang that could allow a local applicatio… |
| 2026-11-11 17:17:17 | [CVE-2026-119723](https://nvd.nist.gov/vuln/detail/CVE-2026-119723) |  |  | When parsing request variables such as query-string and form parameters, HHVM did not check that appending a nested arr… |
| 2026-11-11 17:17:17 | [CVE-2026-121737](https://nvd.nist.gov/vuln/detail/CVE-2026-121737) |  |  | When a remote, unauthenticated HTTP/1.1 client pipelined the start of a second request and then stopped reading, proxyg… |
| 2026-11-11 17:17:17 | [CVE-2026-122043](https://nvd.nist.gov/vuln/detail/CVE-2026-122043) | Medium | 6.0 | repmgr 4.0.0 through 5.5.0 is affected by an OS command injection vulnerability (CWE-78) in event notifications. When e… |
| 2026-11-11 17:17:17 | [CVE-2026-124687](https://nvd.nist.gov/vuln/detail/CVE-2026-124687) | High | 7.1 | In Progress® Kendo® UI for jQuery versions from 2022.2.621 prior to 2026.4.1111 the DropDownButton and SplitButton allo… |
| 2026-11-11 17:17:17 | [CVE-2026-124688](https://nvd.nist.gov/vuln/detail/CVE-2026-124688) | High | 7.1 | In Progress® Kendo® UI for jQuery prior to 2026.4.1111 the TabStrip, PanelBar, and Menu widgets support mapping a dataS… |
| 2026-11-11 17:17:17 | [CVE-2026-124689](https://nvd.nist.gov/vuln/detail/CVE-2026-124689) | High | 7.1 | In Progress Kendo UI for jQuery versions 2026.3.1014 up to, but not including, 2026.4.1110, ActionSheet does not encode… |
| 2026-11-11 17:17:18 | [CVE-2026-124690](https://nvd.nist.gov/vuln/detail/CVE-2026-124690) | High | 7.1 | In Progress Kendo UI for jQuery, sanitizeSvgContent() parses custom icon markup into a live DOM before filtering it. An… |
| 2026-11-11 17:17:18 | [CVE-2026-124692](https://nvd.nist.gov/vuln/detail/CVE-2026-124692) | High | 7.1 | In Progress Kendo UI for jQuery versions 2026.3.1015 up to, but not including, 2026.4.1110, the Grid and TreeList colum… |
| 2026-11-11 17:17:18 | [CVE-2026-124693](https://nvd.nist.gov/vuln/detail/CVE-2026-124693) | High | 7.1 | In Progress Kendo UI for jQuery versions 2026.3.1015 up to, but not including, 2026.4.1110, PivotGrid and PivotConfigur… |
| 2026-11-11 17:17:18 | [CVE-2026-124694](https://nvd.nist.gov/vuln/detail/CVE-2026-124694) | High | 7.1 | In Progress Kendo UI for jQuery versions 2026.3.1015 up to, but not including, 2026.4.1110, PropertyGrid does not encod… |
| 2026-11-11 17:17:18 | [CVE-2026-126720](https://nvd.nist.gov/vuln/detail/CVE-2026-126720) |  |  | Rooxis RXR-12 Wi-Fi router contains an unauthenticated remote code execution vulnerability in /usr/bin/cloud_manage, wh… |
| 2026-11-11 17:17:18 | [CVE-2026-126722](https://nvd.nist.gov/vuln/detail/CVE-2026-126722) |  |  | Rooxis RXR-12 Wi-Fi router contains an undocumented telnet backdoor daemon (/usr/bin/telnetd_startup) that, upon receip… |
| 2026-11-11 17:17:18 | [CVE-2026-126723](https://nvd.nist.gov/vuln/detail/CVE-2026-126723) |  |  | Rooxis RXR-12 Wi-Fi router contains an authenticated command injection vulnerability in the LuCI white_list RPC handler… |
| 2026-11-11 17:17:19 | [CVE-2026-126724](https://nvd.nist.gov/vuln/detail/CVE-2026-126724) |  |  | Rooxis RXR-12 Wi-Fi router contains an undocumented UID-0 backdoor account (dg) with a firmware-wide default password (… |
| 2026-11-11 17:17:19 | [CVE-2026-77873](https://nvd.nist.gov/vuln/detail/CVE-2026-77873) | High | 7.0 | An improper permissions vulnerability was reported in Lenovo System Update that could allow a local authenticated user… |
| 2026-11-11 17:17:20 | [CVE-2026-77882](https://nvd.nist.gov/vuln/detail/CVE-2026-77882) | High | 8.5 | A deserialization of untrusted data vulnerability was discovered in Lenovo System Update that could allow a local authe… |
| 2026-11-11 17:17:23 | [CVE-2026-89061](https://nvd.nist.gov/vuln/detail/CVE-2026-89061) | High | 8.5 | During an internal security assessment, a potential vulnerability was discovered in Lenovo PC Manager, distributed excl… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
