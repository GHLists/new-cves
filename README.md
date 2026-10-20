# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-20 13:18 UTC

New CVEs published between 2026-10-20 12:19 UTC and 2026-10-20 13:18 UTC.

[Full CSV](data/new-cves-2026-10-20T13-18-55-493289Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-10-20 13:16:39 | [CVE-2026-105941](https://nvd.nist.gov/vuln/detail/CVE-2026-105941) | High | 8.1 | The Azure Key Vault KMS provider in Kroxylicious accepts an untrusted vaultName from wire-deserialized EDEK bytes witho… |
| 2026-10-20 13:16:40 | [CVE-2026-113390](https://nvd.nist.gov/vuln/detail/CVE-2026-113390) | High | 8.6 | A flaw has been found in DrayTek Vigor2960 1.5.1.6 Revision 8218. Affected by this issue is the function sub_182B0 of t… |
| 2026-10-20 13:16:40 | [CVE-2026-113391](https://nvd.nist.gov/vuln/detail/CVE-2026-113391) | High | 8.6 | A vulnerability has been found in DrayTek Vigor2960 1.5.1.6 Revision 8218. This affects the function uploadlangs of the… |
| 2026-10-20 13:16:40 | [CVE-2026-113392](https://nvd.nist.gov/vuln/detail/CVE-2026-113392) | Low | 2.1 | A vulnerability was found in DrayTek Vigor2960 1.5.1.6 Revision 8218. This vulnerability affects unknown code of the fi… |
| 2026-10-20 13:16:40 | [CVE-2026-113399](https://nvd.nist.gov/vuln/detail/CVE-2026-113399) |  |  | Incorrect boundary conditions in the SVG component. This vulnerability was fixed in Firefox 158.0.1. |
| 2026-10-20 13:16:41 | [CVE-2026-113400](https://nvd.nist.gov/vuln/detail/CVE-2026-113400) |  |  | Uninitialized memory in the Audio/Video: cubeb component. This vulnerability was fixed in Firefox 158.0.1. |
| 2026-10-20 13:16:41 | [CVE-2026-113401](https://nvd.nist.gov/vuln/detail/CVE-2026-113401) |  |  | Denial-of-service in the PDF Viewer component. This vulnerability was fixed in Firefox 158.0.1. |
| 2026-10-20 13:16:41 | [CVE-2026-113470](https://nvd.nist.gov/vuln/detail/CVE-2026-113470) |  |  | Mozilla blocked compromised intermediate eMudhra certificates via OneCRL on the 17th of October which was distributed t… |
| 2026-10-20 13:16:41 | [CVE-2026-113619](https://nvd.nist.gov/vuln/detail/CVE-2026-113619) | High | 7.5 | In Eclipse ioFog Controller versions 3.8.0 through 3.9.1, POST, PUT, and PATCH bodies on routes that enable template su… |
| 2026-10-20 13:16:41 | [CVE-2026-113620](https://nvd.nist.gov/vuln/detail/CVE-2026-113620) | Critical | 9.8 | In Eclipse ioFog Controller versions 3.8.0 through 3.9.1, operator WebSocket upgrades on the exec and log routes do not… |
| 2026-10-20 13:16:43 | [CVE-2026-34484](https://nvd.nist.gov/vuln/detail/CVE-2026-34484) |  |  | Nokia 1830 Global Express GX is vulnerable to a local privilege escalation vulnerability which exists in the administra… |
| 2026-10-20 13:16:43 | [CVE-2026-34485](https://nvd.nist.gov/vuln/detail/CVE-2026-34485) |  |  | Nokia 1830 Global Express (GX) is vulnerable to a CLI ACL Bypass vulnerability where a low-privileged authenticated att… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
