# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-10 15:18 UTC

New CVEs published between 2026-10-10 14:19 UTC and 2026-10-10 15:18 UTC.

[Full CSV](data/new-cves-2026-10-10T15-18-41-404807Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-10-10 15:16:56 | [CVE-2026-108114](https://nvd.nist.gov/vuln/detail/CVE-2026-108114) | Medium | 5.3 | Strapi 5.47.0 through 5.57.0 contains an improper authorization vulnerability that allows admin API tokens to retain al… |
| 2026-10-10 15:16:57 | [CVE-2026-108115](https://nvd.nist.gov/vuln/detail/CVE-2026-108115) | Low | 2.3 | Kortix Suna 0.10.7 before 0.13.52 contains a server-side request forgery vulnerability that allows project managers to… |
| 2026-10-10 15:16:57 | [CVE-2026-108545](https://nvd.nist.gov/vuln/detail/CVE-2026-108545) | High | 8.2 | SillyTavern 1.12.13 through 1.19.0 contains a denial of service vulnerability that allows unauthenticated remote attack… |
| 2026-10-10 15:16:57 | [CVE-2026-108546](https://nvd.nist.gov/vuln/detail/CVE-2026-108546) | High | 7.7 | Spotweb through 1.5.8 contains an OS command injection vulnerability in the runcommand NZB handler that allows remote a… |
| 2026-10-10 15:16:57 | [CVE-2026-108547](https://nvd.nist.gov/vuln/detail/CVE-2026-108547) | High | 7.1 | AstronRPA through 1.1.6 contains a missing tenant authorization check in robot-service that allows authenticated users… |
| 2026-10-10 15:16:57 | [CVE-2026-108548](https://nvd.nist.gov/vuln/detail/CVE-2026-108548) | Medium | 6.9 | AstronRPA through 1.1.6 contains an authentication bypass vulnerability in the OpenResty gateway's auth_handler.lua tha… |
| 2026-10-10 15:16:57 | [CVE-2026-108549](https://nvd.nist.gov/vuln/detail/CVE-2026-108549) | Critical | 9.2 | cc-connect through 1.5.0 contains a missing authentication vulnerability in the MAX platform adapter webhook mode in pl… |
| 2026-10-10 15:16:58 | [CVE-2026-108550](https://nvd.nist.gov/vuln/detail/CVE-2026-108550) | High | 8.7 | SkillHub before 0.2.22 contains an incorrect authorization vulnerability in AccountMergeService and AccountMergeControl… |
| 2026-10-10 15:16:58 | [CVE-2026-108551](https://nvd.nist.gov/vuln/detail/CVE-2026-108551) | Critical | 9.3 | openapi-typescript-codegen through 0.31.0 contains a code injection vulnerability that allows attackers controlling an… |
| 2026-10-10 15:16:58 | [CVE-2026-108553](https://nvd.nist.gov/vuln/detail/CVE-2026-108553) | High | 7.7 | OpenRefine through 3.10.1 contains a cross-site request forgery vulnerability in the get-rows command that allows remot… |
| 2026-10-10 15:16:58 | [CVE-2026-108554](https://nvd.nist.gov/vuln/detail/CVE-2026-108554) | Medium | 6.9 | PDFMathTranslate (pdf2zh) through 1.9.11 contains a server-side request forgery vulnerability that allows unauthenticat… |
| 2026-10-10 15:16:58 | [CVE-2026-108555](https://nvd.nist.gov/vuln/detail/CVE-2026-108555) | Low | 2.3 | PairDrop through 1.11.2 contains an IP spoofing vulnerability in Peer._setIP that allows remote attackers to join other… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
