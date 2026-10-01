# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-01 17:18 UTC

New CVEs published between 2026-10-01 16:19 UTC and 2026-10-01 17:18 UTC.

[Full CSV](data/new-cves-2026-10-01T17-18-45-786937Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-10-01 17:17:16 | [CVE-2025-31980](https://nvd.nist.gov/vuln/detail/CVE-2025-31980) | Medium | 4.3 | HCL BigFix Service Management is affected by an Improper Input Validation vulnerability, which could allow an attacker… |
| 2026-10-01 17:17:17 | [CVE-2026-101888](https://nvd.nist.gov/vuln/detail/CVE-2026-101888) | High | 8.6 | The Prime Mover plugin for WordPress before 2.2.1 contains a Zip Slip path traversal vulnerability that allows authenti… |
| 2026-10-01 17:17:17 | [CVE-2026-101889](https://nvd.nist.gov/vuln/detail/CVE-2026-101889) | High | 7.0 | The Prime Mover plugin for WordPress before 2.2.1 contains a path traversal vulnerability that allows authenticated adm… |
| 2026-10-01 17:17:17 | [CVE-2026-101890](https://nvd.nist.gov/vuln/detail/CVE-2026-101890) | Medium | 5.1 | The Prime Mover plugin for WordPress before 2.2.1 contains a stored cross-site scripting vulnerability that allows atta… |
| 2026-10-01 17:17:19 | [CVE-2026-103921](https://nvd.nist.gov/vuln/detail/CVE-2026-103921) | High | 7.4 | GraphQL Tools provides utilities for building, stitching, and mocking GraphQL schemas. Prior to 1.1.35, the executor-le… |
| 2026-10-01 17:17:19 | [CVE-2026-12405](https://nvd.nist.gov/vuln/detail/CVE-2026-12405) | High | 8.8 | A flaw was found in rubygem-foreman_remote_execution. A command injection vulnerability exists in the Red Hat Satellite… |
| 2026-10-01 17:17:19 | [CVE-2026-12423](https://nvd.nist.gov/vuln/detail/CVE-2026-12423) | High | 7.5 | A flaw was found in Foreman. The Red Hat Satellite /unattended/provision API endpoint is vulnerable to an authenticatio… |
| 2026-10-01 17:17:20 | [CVE-2026-12540](https://nvd.nist.gov/vuln/detail/CVE-2026-12540) | High | 8.2 | A flaw was found in Foreman. A command injection vulnerability exists in the foreman-rake errors:fetch_log task. The re… |
| 2026-10-01 17:17:20 | [CVE-2026-12541](https://nvd.nist.gov/vuln/detail/CVE-2026-12541) | High | 8.2 | A flaw was found in Foreman. OS command injection vulnerabilities exist in the foreman-rake db:dump and db:import_dump… |
| 2026-10-01 17:17:20 | [CVE-2026-12544](https://nvd.nist.gov/vuln/detail/CVE-2026-12544) | High | 7.7 | A flaw was found in Foreman. The foreman-rake initialization logic in /usr/share/foreman/config/settings.rb contains a… |
| 2026-10-01 17:17:21 | [CVE-2026-13043](https://nvd.nist.gov/vuln/detail/CVE-2026-13043) | Critical | 9.3 | A missing authentication vulnerability in the Kernel Memory Access Driver (PSKMAD) used by WatchGuard endpoint security… |
| 2026-10-01 17:17:21 | [CVE-2026-14316](https://nvd.nist.gov/vuln/detail/CVE-2026-14316) | High | 8.1 | The revoked-key error path builds a human-readable failure reason using sprintf() into a heap buffer. The allocated buf… |
| 2026-10-01 17:17:23 | [CVE-2026-21833](https://nvd.nist.gov/vuln/detail/CVE-2026-21833) | Low | 3.7 | HCL AION is affected by a vulnerability in which the Content-Security-Policy (CSP) HTTP response header is not configur… |
| 2026-10-01 17:17:25 | [CVE-2026-48005](https://nvd.nist.gov/vuln/detail/CVE-2026-48005) |  |  | Missing authentication checks in mod_auth_digest in Apache Software Foundation Apache HTTP Server before 2.4.69 on all… |
| 2026-10-01 17:17:26 | [CVE-2026-56153](https://nvd.nist.gov/vuln/detail/CVE-2026-56153) |  |  | Out-of-bounds Write vulnerability in Apache HTTP Server's mod_charset_lite. This issue affects Apache HTTP Server: from… |
| 2026-10-01 17:17:26 | [CVE-2026-56154](https://nvd.nist.gov/vuln/detail/CVE-2026-56154) |  |  | Use After Free vulnerability in Apache HTTP Server's mod_rewrite when using lookahead (%{LA-U:HTTP:...}) This issue aff… |
| 2026-10-01 17:17:26 | [CVE-2026-56449](https://nvd.nist.gov/vuln/detail/CVE-2026-56449) |  |  | Out-of-bounds Write vulnerability in Apache HTTP Server's mod_proxy_html with crafted HTTP response bodies. This issue… |
| 2026-10-01 17:17:27 | [CVE-2026-57941](https://nvd.nist.gov/vuln/detail/CVE-2026-57941) |  |  | Use After Free vulnerability in Apache HTTP Server's mod_http2 via shared session->bbtmp re-entrancy This issue affects… |
| 2026-10-01 17:17:29 | [CVE-2026-58415](https://nvd.nist.gov/vuln/detail/CVE-2026-58415) |  |  | Internal state files accessible to external parties in mod_dav_fs in Apache Software Foundation Apache HTTP Server befo… |
| 2026-10-01 17:17:29 | [CVE-2026-59685](https://nvd.nist.gov/vuln/detail/CVE-2026-59685) |  |  | Out-of-bounds Write vulnerability in Apache HTTP Server on Windows while processing paths with 8.3 names that may grow… |
| 2026-10-01 17:17:29 | [CVE-2026-59797](https://nvd.nist.gov/vuln/detail/CVE-2026-59797) |  |  | Improper Privilege Management vulnerability in Apache HTTP Server's mod_ssl via SSLRequire and file-related expressions… |
| 2026-10-01 17:17:29 | [CVE-2026-63045](https://nvd.nist.gov/vuln/detail/CVE-2026-63045) |  |  | Improper validation of FTP PASV reply address in mod_proxy_ftp in Apache Software Foundation Apache HTTP Server through… |
| 2026-10-01 17:17:29 | [CVE-2026-63292](https://nvd.nist.gov/vuln/detail/CVE-2026-63292) |  |  | Stack-based buffer overflow in mod_vhost_alias in Apache Software Foundation Apache HTTP Server through 2.4.68 on all p… |
| 2026-10-01 17:17:29 | [CVE-2026-63686](https://nvd.nist.gov/vuln/detail/CVE-2026-63686) |  |  | A NULL pointer dereference in mod_xml2enc in Apache Software Foundation Apache HTTP Server before 2.4.69 on all platfor… |
| 2026-10-01 17:17:30 | [CVE-2026-63718](https://nvd.nist.gov/vuln/detail/CVE-2026-63718) |  |  | Inconsistent Interpretation of HTTP Requests ('HTTP Request/Response Smuggling') response smuggling vulnerability in Ap… |
| 2026-10-01 17:17:30 | [CVE-2026-67171](https://nvd.nist.gov/vuln/detail/CVE-2026-67171) | Medium | 5.3 | HCL BigFix Service Management is affected by an Information Disclosure vulnerability because an exposed API endpoint ex… |
| 2026-10-01 17:17:30 | [CVE-2026-67172](https://nvd.nist.gov/vuln/detail/CVE-2026-67172) | Low | 3.7 | HCL BigFix Service Management is affected by an Information Disclosure vulnerability the application returns sensitive… |
| 2026-10-01 17:17:30 | [CVE-2026-73636](https://nvd.nist.gov/vuln/detail/CVE-2026-73636) |  |  | Authentication bypass by capture-replay in mod_auth_digest in Apache Software Foundation Apache HTTP Server 2.4.x on al… |
| 2026-10-01 17:17:31 | [CVE-2026-73975](https://nvd.nist.gov/vuln/detail/CVE-2026-73975) | High | 8.4 | djehuty is a research data repository system developed by 4TU.ResearchData. Prior to version 26.3.2, an authenticated d… |
| 2026-10-01 17:17:31 | [CVE-2026-77387](https://nvd.nist.gov/vuln/detail/CVE-2026-77387) | Medium | 4.0 | geopy is a geocoding library for Python. Prior to 2.5.0, geopy.Point and Point.from_string() can spend excessive CPU ti… |
| 2026-10-01 17:17:31 | [CVE-2026-79768](https://nvd.nist.gov/vuln/detail/CVE-2026-79768) |  |  | Path equivalence: '/./' (single dot directory) vulnerability in Apache HTTP Server's mod_userdir module when configured… |
| 2026-10-01 17:17:31 | [CVE-2026-73637](https://nvd.nist.gov/vuln/detail/CVE-2026-73637) |  |  | Use after free in mod_auth_digest in Apache Software Foundation Apache HTTP Server before 2.4.69 on all platforms allow… |
| 2026-10-01 17:17:33 | [CVE-2026-93546](https://nvd.nist.gov/vuln/detail/CVE-2026-93546) |  |  | Integer overflow in mod_dav_fs in Apache HTTP Server through 2.4.68 allows an authenticated WebDAV client with write ac… |
| 2026-10-01 17:17:34 | [CVE-2026-96658](https://nvd.nist.gov/vuln/detail/CVE-2026-96658) | Critical | 9.9 | A flaw was found in Foreman. An authenticated attacker with low-level permissions can achieve remote code execution (RC… |
| 2026-10-01 17:17:35 | [CVE-2026-96659](https://nvd.nist.gov/vuln/detail/CVE-2026-96659) | Critical | 9.1 | A flaw was found in Foreman. This vulnerability allows an authenticated user with low-level Viewer permissions to cause… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
