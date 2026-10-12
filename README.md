# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-12 15:18 UTC

New CVEs published between 2026-10-12 14:18 UTC and 2026-10-12 15:18 UTC.

[Full CSV](data/new-cves-2026-10-12T15-18-39-658093Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-10-12 15:17:05 | [CVE-2026-103521](https://nvd.nist.gov/vuln/detail/CVE-2026-103521) | High | 7.2 | In Thelia v2.6.0, the document upload endpoint properly blocks the upload of executable file types, but the document up… |
| 2026-10-12 15:17:05 | [CVE-2026-103522](https://nvd.nist.gov/vuln/detail/CVE-2026-103522) | High | 7.2 | In Thelia v2.6.0, the store banner upload feature performs insufficient filetype validation that relies exclusively on… |
| 2026-10-12 15:17:05 | [CVE-2026-103523](https://nvd.nist.gov/vuln/detail/CVE-2026-103523) |  |  | Thelia v2.6.0 contains an open redirect vulnerability in its address creation workflow. After a user accesses a crafted… |
| 2026-10-12 15:17:05 | [CVE-2026-103524](https://nvd.nist.gov/vuln/detail/CVE-2026-103524) |  |  | Thelia v2.6.0 is vulnerable to multiple stored XSS vulnerabilities within the administrative interface. User-supplied i… |
| 2026-10-12 15:17:06 | [CVE-2026-103526](https://nvd.nist.gov/vuln/detail/CVE-2026-103526) | Low | 3.7 | In Thelia v2.6.0, both the administrative login and forgotten password endpoints return different responses for invalid… |
| 2026-10-12 15:17:06 | [CVE-2026-103527](https://nvd.nist.gov/vuln/detail/CVE-2026-103527) |  |  | Thelia v2.6.0's Smarty templates (address.html and address-update.html) fail to properly escape double quotes in the “n… |
| 2026-10-12 15:17:06 | [CVE-2026-103528](https://nvd.nist.gov/vuln/detail/CVE-2026-103528) |  |  | Thelia 2.6.0 uses Smarty for email templates without properly restricting access to dangerous PHP functions. An authent… |
| 2026-10-12 15:17:06 | [CVE-2026-103529](https://nvd.nist.gov/vuln/detail/CVE-2026-103529) |  |  | Thelia v2.6.0 permits authenticated administrators to upload and install modules via the ZIP upload function without va… |
| 2026-10-12 15:17:06 | [CVE-2026-103535](https://nvd.nist.gov/vuln/detail/CVE-2026-103535) |  |  | Thelia v2.6.1 contains path traversal and PHP code injection vulnerabilities in its translation editor that can be chai… |
| 2026-10-12 15:17:06 | [CVE-2026-103537](https://nvd.nist.gov/vuln/detail/CVE-2026-103537) |  |  | Thelia 2.6.1 contains an absolute path traversal vulnerability in its Smarty template handling that enables SSTI and re… |
| 2026-10-12 15:17:07 | [CVE-2026-108094](https://nvd.nist.gov/vuln/detail/CVE-2026-108094) | High | 7.8 | A use-after-free flaw was found in mutter in the Wayland color-management ICC image-description path. A local attacker… |
| 2026-10-12 15:17:07 | [CVE-2026-108895](https://nvd.nist.gov/vuln/detail/CVE-2026-108895) | High | 8.6 | A weakness has been identified in Linksys E1700 1.0.0.4.003. The affected element is the function setDMZ of the file /g… |
| 2026-10-12 15:17:07 | [CVE-2026-108896](https://nvd.nist.gov/vuln/detail/CVE-2026-108896) | High | 8.6 | A vulnerability was found in Linksys E1700 1.0.0.4.003. This affects the function setLinksysIpv6 of the file /goform/se… |
| 2026-10-12 15:17:07 | [CVE-2026-108897](https://nvd.nist.gov/vuln/detail/CVE-2026-108897) | Medium | 5.5 | A security vulnerability has been detected in Smart Media4U Technology SHAREit App 6.27.38_ww on Android. The impacted… |
| 2026-10-12 15:17:07 | [CVE-2026-108898](https://nvd.nist.gov/vuln/detail/CVE-2026-108898) | Low | 2.0 | A vulnerability was detected in Netis WF2409E 3.3.42541. This affects an unknown function of the component Wireless Set… |
| 2026-10-12 15:17:07 | [CVE-2026-109390](https://nvd.nist.gov/vuln/detail/CVE-2026-109390) | Critical | 9.8 | AnyDesk before 8.0.3 allows unauthenticated remote attackers to execute arbitrary code via a heap-based buffer overflow… |
| 2026-10-12 15:17:09 | [CVE-2026-92877](https://nvd.nist.gov/vuln/detail/CVE-2026-92877) | High | 8.3 | The JAXB factory methods historically relied solely on `FEATURE_SECURE_PROCESSING` to prevent XML External Entity (XXE)… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
