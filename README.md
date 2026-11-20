# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-11-20 04:20 UTC

New CVEs published between 2026-11-20 03:20 UTC and 2026-11-20 04:20 UTC.

[Full CSV](data/new-cves-2026-11-20T04-20-47-44051Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-11-20 04:17:09 | [CVE-2026-113347](https://nvd.nist.gov/vuln/detail/CVE-2026-113347) | High | 8.6 | Multiple products produced by Ruijie Networks Co., Ltd. contain an OS command injection vulnerability that may lead to… |
| 2026-11-20 04:17:09 | [CVE-2026-133480](https://nvd.nist.gov/vuln/detail/CVE-2026-133480) | Low | 2.1 | A flaw has been found in hrshadhin CloudSchool up to 3.0.1. Affected by this issue is the function PublicController.che… |
| 2026-11-20 04:17:09 | [CVE-2026-133482](https://nvd.nist.gov/vuln/detail/CVE-2026-133482) | Low | 1.9 | A vulnerability has been found in hrshadhin CloudSchool up to 3.0.1. This affects the function EventController@store of… |
| 2026-11-20 04:17:09 | [CVE-2026-133536](https://nvd.nist.gov/vuln/detail/CVE-2026-133536) | Medium | 4.3 | A flaw was found in Keycloak. The OpenID Connect (OIDC) logout endpoint continues to honor post-logout redirect rules f… |
| 2026-11-20 04:17:10 | [CVE-2026-133537](https://nvd.nist.gov/vuln/detail/CVE-2026-133537) | Medium | 6.8 | A flaw was found in Keycloak. When evaluating access permissions, Keycloak Authorization Services improperly matches re… |
| 2026-11-20 04:17:10 | [CVE-2026-133553](https://nvd.nist.gov/vuln/detail/CVE-2026-133553) | High | 7.8 | A flaw was found in crun. When copying files onto a tmpfs mounted with tmpcopyup, crun opens the destination a second t… |
| 2026-11-20 04:17:10 | [CVE-2026-15223](https://nvd.nist.gov/vuln/detail/CVE-2026-15223) | Medium | 5.1 | An improper export control defect in ChatEventDispatchActivity (com.vivo.agent.business.chatmode.activity.ChatEventDisp… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
