# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-09-29 15:19 UTC

New CVEs published between 2026-09-29 14:19 UTC and 2026-09-29 15:19 UTC.

[Full CSV](data/new-cves-2026-09-29T15-19-33-811515Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-09-29 15:17:11 | [CVE-2015-20122](https://nvd.nist.gov/vuln/detail/CVE-2015-20122) | High | 8.7 | Seeyon A6 collaborative office automation platform contains an unauthenticated SQL injection vulnerability in the attac… |
| 2026-09-29 15:17:12 | [CVE-2025-33207](https://nvd.nist.gov/vuln/detail/CVE-2025-33207) | Medium | 6.8 | NVIDIA ConnectX and Bluefield contain a vulnerability in a control register, where a user with VF access could cause im… |
| 2026-09-29 15:17:17 | [CVE-2026-102371](https://nvd.nist.gov/vuln/detail/CVE-2026-102371) | Medium | 5.7 | In wsl-pro-service before 0.1.19ubuntu3, the service component which runs as root inside each WSL instance attaches the… |
| 2026-09-29 15:17:17 | [CVE-2026-102491](https://nvd.nist.gov/vuln/detail/CVE-2026-102491) | Medium | 5.5 | A vulnerability was identified in mahonelau kykms up to 8f130c2d85842d5b44caae78cc46d65e505949f7. The impacted element… |
| 2026-09-29 15:17:18 | [CVE-2026-102566](https://nvd.nist.gov/vuln/detail/CVE-2026-102566) | High | 8.5 | CTranslate2 before 4.8.1 contains a heap-based buffer overflow in the binary model loader that fails to validate payloa… |
| 2026-09-29 15:17:18 | [CVE-2026-102567](https://nvd.nist.gov/vuln/detail/CVE-2026-102567) | Medium | 6.9 | CTranslate2 before 4.8.1 contains an out-of-bounds heap read vulnerability in the binary model loader when deserializin… |
| 2026-09-29 15:17:18 | [CVE-2026-102568](https://nvd.nist.gov/vuln/detail/CVE-2026-102568) | Medium | 6.8 | Pardus Parental Control before 0.7.0 contains an incorrect authorization vulnerability in the polkit policy that allows… |
| 2026-09-29 15:17:18 | [CVE-2026-102569](https://nvd.nist.gov/vuln/detail/CVE-2026-102569) | High | 7.0 | ClipBucket v5 through 5.5.3-#197 contains a time-based blind SQL injection vulnerability in the admin video edit functi… |
| 2026-09-29 15:17:18 | [CVE-2026-102570](https://nvd.nist.gov/vuln/detail/CVE-2026-102570) | High | 7.0 | ClipBucket v5 through 5.5.3-#197 contains a time-based blind SQL injection vulnerability in the language update functio… |
| 2026-09-29 15:17:21 | [CVE-2026-22094](https://nvd.nist.gov/vuln/detail/CVE-2026-22094) | Critical | 9.3 | The firmware for the EVbee DC-80 has a weak hardcoded root password, which allows attackers to login as root using the… |
| 2026-09-29 15:17:25 | [CVE-2026-22101](https://nvd.nist.gov/vuln/detail/CVE-2026-22101) | Medium | 5.1 | The access to the service menu is obfuscated, but possible with only physical access. This menu exposes sensitive infor… |
| 2026-09-29 15:17:26 | [CVE-2026-49243](https://nvd.nist.gov/vuln/detail/CVE-2026-49243) | Medium | 5.1 | Webmin is a web-based system administration tool for Unix-like servers. Prior to version 2.650, Webmin users who click… |
| 2026-09-29 15:17:27 | [CVE-2026-63209](https://nvd.nist.gov/vuln/detail/CVE-2026-63209) | High | 7.5 | compress provides various compression algorithms. Prior to version 1.18.7, a signed integer overflow vulnerability in s… |
| 2026-09-29 15:17:27 | [CVE-2026-65102](https://nvd.nist.gov/vuln/detail/CVE-2026-65102) | High | 7.8 | NVIDIA DeepStream contains a vulnerability where an attacker could cause an integer overflow by supplying crafted tenso… |
| 2026-09-29 15:17:27 | [CVE-2026-68911](https://nvd.nist.gov/vuln/detail/CVE-2026-68911) | High | 8.7 | Nicotine+ is a graphical client for the Soulseek peer-to-peer network. Prior to version 3.3.11, a modified remote clien… |
| 2026-09-29 15:17:30 | [CVE-2026-86035](https://nvd.nist.gov/vuln/detail/CVE-2026-86035) | High | 8.5 | Weblate is a web-based continuous localization platform used to manage software translations. Weblate 4.11.1 through 20… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
