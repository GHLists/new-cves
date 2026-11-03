# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-11-03 13:19 UTC

New CVEs published between 2026-11-03 12:19 UTC and 2026-11-03 13:19 UTC.

[Full CSV](data/new-cves-2026-11-03T13-19-40-647956Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-11-03 13:17:17 | [CVE-2026-108046](https://nvd.nist.gov/vuln/detail/CVE-2026-108046) | Medium | 6.9 | Direct Object Reference (IDOR) vulnerability in Alosuite due to insufficient authorization checks when processing objec… |
| 2026-11-03 13:17:17 | [CVE-2026-108047](https://nvd.nist.gov/vuln/detail/CVE-2026-108047) | High | 8.6 | Inadequate authorization vulnerability in Alosuite’s user invitation functionality. The ‘/Requests/userInvitation’ endp… |
| 2026-11-03 13:17:17 | [CVE-2026-108048](https://nvd.nist.gov/vuln/detail/CVE-2026-108048) | Medium | 6.9 | Vulnerability due to a lack of request limits in Alosuite’s password recovery functionality. The ‘/Account/resetPwd’ en… |
| 2026-11-03 13:17:17 | [CVE-2026-108049](https://nvd.nist.gov/vuln/detail/CVE-2026-108049) | Medium | 5.1 | Clickjacking vulnerability in the Alosuite web application. The affected login interface can be embedded in a web page… |
| 2026-11-03 13:17:17 | [CVE-2026-108050](https://nvd.nist.gov/vuln/detail/CVE-2026-108050) | Medium | 5.1 | A stored Cross-Site Scripting (XSS) vulnerability in Alosuite that affects the delivery note functionality. Insufficien… |
| 2026-11-03 13:17:17 | [CVE-2026-108051](https://nvd.nist.gov/vuln/detail/CVE-2026-108051) | Medium | 5.1 | A stored Cross-Site Scripting (XSS) vulnerability in Alosuite that affects the delivery note functionality. Insufficien… |
| 2026-11-03 13:17:18 | [CVE-2026-108052](https://nvd.nist.gov/vuln/detail/CVE-2026-108052) | Medium | 5.1 | A stored Cross-Site Scripting (XSS) vulnerability in Alosuite that affects the delivery note functionality. Insufficien… |
| 2026-11-03 13:17:18 | [CVE-2026-108053](https://nvd.nist.gov/vuln/detail/CVE-2026-108053) | Medium | 5.1 | A stored Cross-Site Scripting (XSS) vulnerability in Alosuite that affects the delivery note functionality. Insufficien… |
| 2026-11-03 13:17:18 | [CVE-2026-108054](https://nvd.nist.gov/vuln/detail/CVE-2026-108054) | Medium | 5.1 | A stored Cross-Site Scripting (XSS) vulnerability in Alosuite that affects the delivery note functionality. Insufficien… |
| 2026-11-03 13:17:18 | [CVE-2026-108055](https://nvd.nist.gov/vuln/detail/CVE-2026-108055) | Medium | 5.1 | A stored Cross-Site Scripting (XSS) vulnerability in Alosuite that affects the delivery note functionality. Insufficien… |
| 2026-11-03 13:17:18 | [CVE-2026-108056](https://nvd.nist.gov/vuln/detail/CVE-2026-108056) | Medium | 5.1 | A stored Cross-Site Scripting (XSS) vulnerability in Alosuite that affects the delivery note functionality. Insufficien… |
| 2026-11-03 13:17:18 | [CVE-2026-108057](https://nvd.nist.gov/vuln/detail/CVE-2026-108057) | Medium | 5.1 | A stored Cross-Site Scripting (XSS) vulnerability in Alosuite that affects the delivery note functionality. Insufficien… |
| 2026-11-03 13:17:18 | [CVE-2026-108058](https://nvd.nist.gov/vuln/detail/CVE-2026-108058) | Medium | 5.1 | A stored Cross-Site Scripting (XSS) vulnerability in Alosuite that affects the delivery note functionality. Insufficien… |
| 2026-11-03 13:17:19 | [CVE-2026-108059](https://nvd.nist.gov/vuln/detail/CVE-2026-108059) | Medium | 5.1 | A stored Cross-Site Scripting (XSS) vulnerability in Alosuite that affects the delivery note functionality. Insufficien… |
| 2026-11-03 13:17:19 | [CVE-2026-108060](https://nvd.nist.gov/vuln/detail/CVE-2026-108060) | Medium | 5.1 | A stored Cross-Site Scripting (XSS) vulnerability in Alosuite that affects the delivery note functionality. Insufficien… |
| 2026-11-03 13:17:21 | [CVE-2026-121458](https://nvd.nist.gov/vuln/detail/CVE-2026-121458) | High | 7.1 | Instatic before 0.0.21 contains a missing authorization vulnerability in its AI/MCP content read tools that allows low-… |
| 2026-11-03 13:17:23 | [CVE-2026-65160](https://nvd.nist.gov/vuln/detail/CVE-2026-65160) | Medium | 5.5 | NVIDIA nvJPEG contains a vulnerability where an attacker could cause a divide-by-zero. A successful exploit of this vul… |
| 2026-11-03 13:17:23 | [CVE-2026-76124](https://nvd.nist.gov/vuln/detail/CVE-2026-76124) | High | 8.8 | The BuddyBoss App plugin for WordPress is vulnerable to Arbitrary File Upload in all versions up to, and including, 3.2… |
| 2026-11-03 13:17:24 | [CVE-2026-99270](https://nvd.nist.gov/vuln/detail/CVE-2026-99270) |  |  | In the Linux kernel, the following vulnerability has been resolved: tcp: Fix potential UAF in reqsk_timer_handler(). Wh… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
