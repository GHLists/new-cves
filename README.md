# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-14 06:19 UTC

New CVEs published between 2026-10-14 05:19 UTC and 2026-10-14 06:19 UTC.

[Full CSV](data/new-cves-2026-10-14T06-19-05-387075Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-10-14 06:17:05 | [CVE-2026-107153](https://nvd.nist.gov/vuln/detail/CVE-2026-107153) | High | 7.0 | Multiple smartphones provided by Rakuten Mobile, Inc. utilize AOSP test keys for their Android Verified Boot (AVB) func… |
| 2026-10-14 06:17:05 | [CVE-2026-110457](https://nvd.nist.gov/vuln/detail/CVE-2026-110457) | Low | 3.7 | A malicious actor with access to the network and under certain conditions could exploit a Path Traversal vulnerability… |
| 2026-10-14 06:17:06 | [CVE-2026-110458](https://nvd.nist.gov/vuln/detail/CVE-2026-110458) | Low | 3.7 | A malicious actor with access to the network and under certain conditions could exploit a Path Traversal vulnerability… |
| 2026-10-14 06:17:06 | [CVE-2026-110459](https://nvd.nist.gov/vuln/detail/CVE-2026-110459) | High | 8.6 | A malicious actor with access to the network could exploit an Improper Access Control vulnerability found in UniFi Prot… |
| 2026-10-14 06:17:06 | [CVE-2026-50216](https://nvd.nist.gov/vuln/detail/CVE-2026-50216) | Medium | 5.3 | An integer underflow exists in the DNS proxy component of the macOS NetworkExtension system extension shipped with Akam… |
| 2026-10-14 06:17:06 | [CVE-2026-50217](https://nvd.nist.gov/vuln/detail/CVE-2026-50217) | Medium | 4.7 | A use-after-free vulnerability in the Windows WFP callout driver of Akamai Guardicore Platform Agent (GPA) allows a loc… |
| 2026-10-14 06:17:06 | [CVE-2026-50218](https://nvd.nist.gov/vuln/detail/CVE-2026-50218) | High | 8.5 | Akamai GPA (Guardicore Platform Agent) client on all platforms before 7.4 improperly validates JWT tokens used for seed… |
| 2026-10-14 06:17:07 | [CVE-2026-94370](https://nvd.nist.gov/vuln/detail/CVE-2026-94370) | Medium | 6.5 | A defect in the Qt for MCUs core string handling causes heap memory corruption. When an application passes text into Qt… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
