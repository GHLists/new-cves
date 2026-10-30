# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-30 09:18 UTC

New CVEs published between 2026-10-30 08:18 UTC and 2026-10-30 09:18 UTC.

[Full CSV](data/new-cves-2026-10-30T09-18-58-850386Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-10-30 09:17:12 | [CVE-2026-109821](https://nvd.nist.gov/vuln/detail/CVE-2026-109821) | Medium | 6.3 | Improper Validation of Specified Quantity in Input vulnerability in the Elixir standard library's URI module allows an… |
| 2026-10-30 09:17:14 | [CVE-2026-115274](https://nvd.nist.gov/vuln/detail/CVE-2026-115274) | Medium | 6.9 | Improper Validation of Specified Quantity in Input vulnerability in the Elixir standard library's JSON module allows an… |
| 2026-10-30 09:17:14 | [CVE-2026-115456](https://nvd.nist.gov/vuln/detail/CVE-2026-115456) | Low | 3.7 | A flaw was found in gcc. An attacker could cause a Denial of Service (DoS) by passing a string that is not null-termina… |
| 2026-10-30 09:17:14 | [CVE-2026-59385](https://nvd.nist.gov/vuln/detail/CVE-2026-59385) | Low | 2.7 | A user with SpaceDeveloper privileges could modify the URL of a space-scoped broker without altering its credentials, e… |
| 2026-10-30 09:17:14 | [CVE-2026-59386](https://nvd.nist.gov/vuln/detail/CVE-2026-59386) | Medium | 6.5 | A SpaceSupporter could improperly modify an application's start command and buildpack—actions requiring SpaceDeveloper… |
| 2026-10-30 09:17:14 | [CVE-2026-59387](https://nvd.nist.gov/vuln/detail/CVE-2026-59387) | High | 8.8 | The Nginx routing configuration for Cloud Controller blocks unauthenticated access to /internal/v4/ and /internal/v5/ e… |
| 2026-10-30 09:17:15 | [CVE-2026-59388](https://nvd.nist.gov/vuln/detail/CVE-2026-59388) | Medium | 6.5 | Cloud Controller (CAPI) leaks sensitive data into audit logs in multiple instances: custom buildpack credentials are ex… |
| 2026-10-30 09:17:15 | [CVE-2026-59396](https://nvd.nist.gov/vuln/detail/CVE-2026-59396) | Medium | 6.9 | A denial-of-service vulnerability exists in UAA's private_key_jwt client-authentication mechanism. When UAA retrieves a… |
| 2026-10-30 09:17:15 | [CVE-2026-64618](https://nvd.nist.gov/vuln/detail/CVE-2026-64618) |  |  | Improper Neutralization of Special Elements used in an SQL Command ("SQL Injection") vulnerability exists in Apache Fin… |
| 2026-10-30 09:17:15 | [CVE-2026-65874](https://nvd.nist.gov/vuln/detail/CVE-2026-65874) |  |  | This issue affects Apache Fineract versions up to and including 1.15.0. The Center read endpoint (GET /api/v1/centers)… |
| 2026-10-30 09:17:15 | [CVE-2026-97209](https://nvd.nist.gov/vuln/detail/CVE-2026-97209) | Medium | 5.4 | Insecure Temporary File vulnerability in Mix deps.partition in Elixir allows a local user to execute code as another us… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
