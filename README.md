# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-20 08:18 UTC

New CVEs published between 2026-10-20 07:19 UTC and 2026-10-20 08:18 UTC.

[Full CSV](data/new-cves-2026-10-20T08-18-58-59112Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-10-20 08:16:40 | [CVE-2024-2323](https://nvd.nist.gov/vuln/detail/CVE-2024-2323) | Medium | 4.8 | The RemoteUserStoreManagerService does not sufficiently validate password change attempts when the password history val… |
| 2026-10-20 08:16:42 | [CVE-2026-111090](https://nvd.nist.gov/vuln/detail/CVE-2026-111090) | High | 7.8 | A logic error exists in the signature verification routine resulting in acceptance of unauthenticated update and licens… |
| 2026-10-20 08:16:42 | [CVE-2026-112177](https://nvd.nist.gov/vuln/detail/CVE-2026-112177) | High | 7.3 | A flaw was found in Ghostscript as shipped with Red Hat Enterprise Linux 8. The correction for CVE-2019-14869 was omitt… |
| 2026-10-20 08:16:42 | [CVE-2026-113405](https://nvd.nist.gov/vuln/detail/CVE-2026-113405) | High | 8.7 | BA-Workflow developed by YS-infoware has a SQL Injection vulnerability. Authenticated remote attackers can inject arbit… |
| 2026-10-20 08:16:43 | [CVE-2026-113407](https://nvd.nist.gov/vuln/detail/CVE-2026-113407) | High | 8.7 | BA-Workflow developed by YS-infoware has a SQL Injection vulnerability. Authenticated remote attackers can inject arbit… |
| 2026-10-20 08:16:43 | [CVE-2026-113406](https://nvd.nist.gov/vuln/detail/CVE-2026-113406) | High | 8.7 | BA-Workflow developed by YS-infoware has a SQL Injection vulnerability. Authenticated remote attackers can inject arbit… |
| 2026-10-20 08:16:44 | [CVE-2026-43834](https://nvd.nist.gov/vuln/detail/CVE-2026-43834) | High | 7.5 | A stack-based buffer overflow vulnerability in the logs settings functionality could allow an authenticated attacker to… |
| 2026-10-20 08:16:44 | [CVE-2026-43835](https://nvd.nist.gov/vuln/detail/CVE-2026-43835) | High | 8.6 | A vulnerability in the firmware upgrade functionality could allow an authenticated attacker to upload a forged firmware… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
