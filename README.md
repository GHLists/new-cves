# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-11-05 13:21 UTC

New CVEs published between 2026-11-05 12:19 UTC and 2026-11-05 13:21 UTC.

[Full CSV](data/new-cves-2026-11-05T13-21-34-165284Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-11-05 13:17:06 | [CVE-2026-103863](https://nvd.nist.gov/vuln/detail/CVE-2026-103863) |  |  | Improper neutralization of input during web page generation ('cross-site scripting') vulnerability in Apache Sling Engi… |
| 2026-11-05 13:17:07 | [CVE-2026-103864](https://nvd.nist.gov/vuln/detail/CVE-2026-103864) |  |  | Improper output neutralization for logs in Apache Sling Engine. This issue affects Apache Sling Engine: before 3.0.4. U… |
| 2026-11-05 13:17:07 | [CVE-2026-103866](https://nvd.nist.gov/vuln/detail/CVE-2026-103866) |  |  | Inconsistent interpretation of HTTP requests ('HTTP Request/Response smuggling') vulnerability in Apache Sling Engine.… |
| 2026-11-05 13:17:07 | [CVE-2026-123020](https://nvd.nist.gov/vuln/detail/CVE-2026-123020) | Low | 2.1 | A security vulnerability has been detected in eosphoros-ai DB-GPT up to 0.8.1. The affected element is the function Fil… |
| 2026-11-05 13:17:07 | [CVE-2026-123047](https://nvd.nist.gov/vuln/detail/CVE-2026-123047) | High | 7.5 | In Eclipse BaSyx Helm Charts versions 3.0.0-rc.1 to 3.12.1 of the `basyx` chart, deployments with the bundled Keycloak… |
| 2026-11-05 13:17:07 | [CVE-2026-123119](https://nvd.nist.gov/vuln/detail/CVE-2026-123119) | Low | 2.3 | The Symfony HttpClient component NoPrivateNetworkHttpClient does not pin the checked IP address of cached hosts, allowi… |
| 2026-11-05 13:17:08 | [CVE-2026-95652](https://nvd.nist.gov/vuln/detail/CVE-2026-95652) | Medium | 6.6 | Execution with unnecessary privileges vulnerability in TÜBİTAK BİLGEM Software Technologies Research Institute pardus-u… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
