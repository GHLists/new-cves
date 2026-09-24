# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-09-24 13:19 UTC

New CVEs published between 2026-09-24 12:19 UTC and 2026-09-24 13:19 UTC.

[Full CSV](data/new-cves-2026-09-24T13-19-02-076382Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-09-24 13:17:09 | [CVE-2026-19072](https://nvd.nist.gov/vuln/detail/CVE-2026-19072) | Critical | 9.9 | Velociraptor stores the compiled VQL in the hunt object internally to avoid having to recompile the artifacts for each… |
| 2026-09-24 13:17:15 | [CVE-2026-88907](https://nvd.nist.gov/vuln/detail/CVE-2026-88907) | High | 7.4 | Incorrect Authorization vulnerability in TÜBİTAK ULAKBİM UlakPDF allows Authentication Bypass. This issue affects UlakP… |
| 2026-09-24 13:17:16 | [CVE-2026-88916](https://nvd.nist.gov/vuln/detail/CVE-2026-88916) | Medium | 6.8 | Incorrect Authorization vulnerability in TÜBİTAK ULAKBİM UlakPDF allows Privilege Escalation. This issue affects UlakPD… |
| 2026-09-24 13:17:17 | [CVE-2026-94416](https://nvd.nist.gov/vuln/detail/CVE-2026-94416) | Medium | 6.8 | An authorization bypass was found in the Ansible Automation Platform (AAP) gateway. The gateway API allows an authentic… |
| 2026-09-24 13:17:17 | [CVE-2026-96515](https://nvd.nist.gov/vuln/detail/CVE-2026-96515) | High | 8.6 | This vulnerability exists in the Netlink ICT HG323RW router due to insufficient authorization and input validation cont… |
| 2026-09-24 13:17:19 | [CVE-2026-97182](https://nvd.nist.gov/vuln/detail/CVE-2026-97182) | Medium | 5.5 | A security vulnerability has been detected in halo-dev Halo up to 2.25.4/2.26.1. Affected is an unknown function of the… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
