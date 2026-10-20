# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-20 12:19 UTC

New CVEs published between 2026-10-20 11:20 UTC and 2026-10-20 12:19 UTC.

[Full CSV](data/new-cves-2026-10-20T12-19-55-999212Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-10-20 12:17:28 | [CVE-2026-105311](https://nvd.nist.gov/vuln/detail/CVE-2026-105311) | High | 7.7 | The StreamsHub Console operator acts as a confused deputy: a Kubernetes tenant with permission to create a Console cust… |
| 2026-10-20 12:17:28 | [CVE-2026-105312](https://nvd.nist.gov/vuln/detail/CVE-2026-105312) | Critical | 9.9 | A Kubernetes tenant with create permission on Console custom resources can set spec.containers.api.spec.image to an arb… |
| 2026-10-20 12:17:28 | [CVE-2026-105949](https://nvd.nist.gov/vuln/detail/CVE-2026-105949) | High | 8.8 | Cruise Control's Jetty ConstraintSecurityHandler registers security constraints on exact path specs without a catch-all… |
| 2026-10-20 12:17:29 | [CVE-2026-113385](https://nvd.nist.gov/vuln/detail/CVE-2026-113385) | Low | 1.9 | A vulnerability has been found in LeeDrOiD Labs Shortcutter 2 App 9.0.48 on Android. This issue affects the function Cl… |
| 2026-10-20 12:17:29 | [CVE-2026-113388](https://nvd.nist.gov/vuln/detail/CVE-2026-113388) | Low | 1.9 | A security flaw has been discovered in opensource-socialnetwork up to 9.11/10.1. This affects the function input of the… |
| 2026-10-20 12:17:29 | [CVE-2026-113389](https://nvd.nist.gov/vuln/detail/CVE-2026-113389) | High | 8.6 | A vulnerability was detected in DrayTek Vigor2960 1.5.1.6 Revision 8218. Affected by this vulnerability is the function… |
| 2026-10-20 12:17:29 | [CVE-2026-113495](https://nvd.nist.gov/vuln/detail/CVE-2026-113495) | Medium | 5.0 | A flaw was found in cockpit-machines. Red Hat Subscription Management (RHSM) authentication tokens are passed as comman… |
| 2026-10-20 12:17:29 | [CVE-2026-113496](https://nvd.nist.gov/vuln/detail/CVE-2026-113496) | Medium | 5.0 | A flaw was found in cockpit-machines. When saving Virtual Network Computing (VNC) console settings, the configured pass… |
| 2026-10-20 12:17:29 | [CVE-2026-113583](https://nvd.nist.gov/vuln/detail/CVE-2026-113583) | Medium | 5.3 | Cypht webmail 2.0.0 through 2.12.2 contains a DOM-based cross-site scripting vulnerability that allows remote attackers… |
| 2026-10-20 12:17:30 | [CVE-2026-14933](https://nvd.nist.gov/vuln/detail/CVE-2026-14933) | High | 8.6 | Cross-site scripting in the embedded co-browsing feature in Unblu inc. Unblu Spark 7.0 through 7.57.7 and 8.0 through 8… |
| 2026-10-20 12:17:30 | [CVE-2026-18205](https://nvd.nist.gov/vuln/detail/CVE-2026-18205) | Medium | 6.1 | Improper neutralization of input during web page generation ('cross-site scripting') vulnerability in Ticimax Informati… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
