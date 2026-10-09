# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-09 16:19 UTC

New CVEs published between 2026-10-09 15:18 UTC and 2026-10-09 16:19 UTC.

[Full CSV](data/new-cves-2026-10-09T16-19-09-331239Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-10-09 16:17:20 | [CVE-2026-102554](https://nvd.nist.gov/vuln/detail/CVE-2026-102554) | High | 8.2 | Allocation of resources without limits or throttling (CWE-770) during Java object deserialization in Google Guava versi… |
| 2026-10-09 16:17:20 | [CVE-2026-104082](https://nvd.nist.gov/vuln/detail/CVE-2026-104082) | High | 8.6 | SmarterMail before build 9777 contains a remote code execution vulnerability that allows an attacker holding a SysAdmin… |
| 2026-10-09 16:17:20 | [CVE-2026-104083](https://nvd.nist.gov/vuln/detail/CVE-2026-104083) | Medium | 5.3 | SmarterMail before build 9777 contains a stored mutation cross-site scripting vulnerability that allows remote attacker… |
| 2026-10-09 16:17:21 | [CVE-2026-104084](https://nvd.nist.gov/vuln/detail/CVE-2026-104084) | High | 8.7 | SmarterMail before build 9777 contains a privilege escalation vulnerability where JWT access and refresh tokens embed a… |
| 2026-10-09 16:17:24 | [CVE-2026-107783](https://nvd.nist.gov/vuln/detail/CVE-2026-107783) | Medium | 6.7 | Insertion of sensitive information into log file in AWS Tools for PowerShell before 5.0.306 might allow local users to… |
| 2026-10-09 16:17:25 | [CVE-2026-107807](https://nvd.nist.gov/vuln/detail/CVE-2026-107807) | High | 8.8 | Nginx UI is a web user interface for the Nginx web server. From 2.0.0 until 2.5.0, Nginx UI accepts the Node.Secret mas… |
| 2026-10-09 16:17:25 | [CVE-2026-107808](https://nvd.nist.gov/vuln/detail/CVE-2026-107808) | High | 8.1 | Nginx UI is a web user interface for the Nginx web server. From 2.0.0 until 2.5.0, POST /api/login checks EnabledOTP bu… |
| 2026-10-09 16:17:25 | [CVE-2026-107809](https://nvd.nist.gov/vuln/detail/CVE-2026-107809) | High | 8.8 | Nginx UI is a web user interface for the Nginx web server. From 2.0.0 until 2.5.0, AuthRequired accepts a browser-manag… |
| 2026-10-09 16:17:25 | [CVE-2026-107810](https://nvd.nist.gov/vuln/detail/CVE-2026-107810) | High | 8.1 | Nginx UI is a web user interface for the Nginx web server. From 2.0.0 until 2.5.0, internal/backup/restore.go extracts… |
| 2026-10-09 16:17:25 | [CVE-2026-107811](https://nvd.nist.gov/vuln/detail/CVE-2026-107811) | High | 8.8 | Nginx UI is a web user interface for the Nginx web server. From 2.0.0 until 2.5.0, ordinary authenticated users can acc… |
| 2026-10-09 16:17:25 | [CVE-2026-107812](https://nvd.nist.gov/vuln/detail/CVE-2026-107812) | High | 7.5 | Nginx UI is a web user interface for the Nginx web server. From 2.0.0 until 2.5.0, the self-upgrade mechanism validates… |
| 2026-10-09 16:17:26 | [CVE-2026-107813](https://nvd.nist.gov/vuln/detail/CVE-2026-107813) | High | 8.8 | Nginx UI is a web user interface for the Nginx web server. From 2.0.0 until 2.5.0, the api/cluster router exposes node… |
| 2026-10-09 16:17:26 | [CVE-2026-107814](https://nvd.nist.gov/vuln/detail/CVE-2026-107814) | High | 8.4 | MariaDB server is a community developed fork of MySQL server. From 10.6.1 until 10.6.28, 10.11.19, 11.4.13, 11.8.9, 12.… |
| 2026-10-09 16:17:26 | [CVE-2026-108110](https://nvd.nist.gov/vuln/detail/CVE-2026-108110) | High | 7.6 | MOVO through 0.2.3 contains an authorization bypass vulnerability in the chat-api document endpoints that allows authen… |
| 2026-10-09 16:17:26 | [CVE-2026-108111](https://nvd.nist.gov/vuln/detail/CVE-2026-108111) | Medium | 5.3 | ruoyi-ai 3.0.0 through 3.1.0 contains a missing authorization vulnerability in the GET /workflow/search endpoint that e… |
| 2026-10-09 16:17:26 | [CVE-2026-108112](https://nvd.nist.gov/vuln/detail/CVE-2026-108112) | Medium | 5.3 | ruoyi-ai 3.0.0 through 3.1.0 contains a missing authorization vulnerability that allows authenticated users to delete o… |
| 2026-10-09 16:17:26 | [CVE-2026-108113](https://nvd.nist.gov/vuln/detail/CVE-2026-108113) | High | 8.7 | ILIAS before 9.24, 10.12, and 11.5 contains an unrestricted file upload vulnerability in QTI question import image hand… |
| 2026-10-09 16:17:29 | [CVE-2026-75345](https://nvd.nist.gov/vuln/detail/CVE-2026-75345) | High | 7.5 | OpENer v2.3.0 / commit 76b95cf contains an out-of-bounds read in the unconnected explicit messaging path. This allows a… |
| 2026-10-09 16:17:29 | [CVE-2026-75346](https://nvd.nist.gov/vuln/detail/CVE-2026-75346) |  |  | An out-of-bounds read vulnerability exists in EIPStackGroup OpENer v2.3 and master through commit 76b95cf in the server… |
| 2026-10-09 16:17:29 | [CVE-2026-75348](https://nvd.nist.gov/vuln/detail/CVE-2026-75348) | High | 7.5 | An out-of-bounds read vulnerability exists in EIPStackGroup OpENer v2.3 and master up to commit 76b95cf in the EtherNet… |
| 2026-10-09 16:17:29 | [CVE-2026-75349](https://nvd.nist.gov/vuln/detail/CVE-2026-75349) | High | 7.5 | EIPStackGroup OpENer v2.3.0/master up to commit 76b95cf contains an out-of-bounds read vulnerability in Connection Mana… |
| 2026-10-09 16:17:31 | [CVE-2026-90983](https://nvd.nist.gov/vuln/detail/CVE-2026-90983) | High | 8.2 | Use of Client-Side authentication vulnerability in Hayat Health Facilities Inc. (Hayat Hospital) Hayat Mobile allows Au… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
