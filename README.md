# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-11-23 09:18 UTC

New CVEs published between 2026-11-23 08:20 UTC and 2026-11-23 09:18 UTC.

[Full CSV](data/new-cves-2026-11-23T09-18-32-360799Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-11-23 09:17:04 | [CVE-2026-115873](https://nvd.nist.gov/vuln/detail/CVE-2026-115873) | High | 8.7 | A remote attacker must authenticate with Read Only (GroupRead) access to at least one Worker Group and reach the Leader… |
| 2026-11-23 09:17:05 | [CVE-2026-115899](https://nvd.nist.gov/vuln/detail/CVE-2026-115899) | Critical | 9.3 | An attacker must control pagination data returned by an upstream API or service queried by an existing REST Collector.… |
| 2026-11-23 09:17:05 | [CVE-2026-115900](https://nvd.nist.gov/vuln/detail/CVE-2026-115900) | High | 8.7 | An attacker must possess a valid Worker distribution credential, reach the Leader distribution listener, and send craft… |
| 2026-11-23 09:17:05 | [CVE-2026-115901](https://nvd.nist.gov/vuln/detail/CVE-2026-115901) | High | 8.5 | Exploitation requires an identity admitted to a configured trusted IdP application, control of claims selected as the O… |
| 2026-11-23 09:17:05 | [CVE-2026-115903](https://nvd.nist.gov/vuln/detail/CVE-2026-115903) | High | 7.1 | An authenticated attacker must reach the Edge file APIs through the Leader or directly on an Edge node. On affected man… |
| 2026-11-23 09:17:05 | [CVE-2026-134882](https://nvd.nist.gov/vuln/detail/CVE-2026-134882) | Critical | 10.0 | A weakness has been identified in TOTOLINK A7100RU 7.4cu.2313_B20191024. This issue affects the function exportOvpn of… |
| 2026-11-23 09:17:08 | [CVE-2026-93584](https://nvd.nist.gov/vuln/detail/CVE-2026-93584) | High | 8.6 | An SQL injection vulnerability in OTRS versions 2024.3.1 through 2026.8.1 allows unauthenticated remote attackers to in… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
