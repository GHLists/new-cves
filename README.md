# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-11-26 03:18 UTC

New CVEs published between 2026-11-26 02:18 UTC and 2026-11-26 03:18 UTC.

[Full CSV](data/new-cves-2026-11-26T03-18-24-730016Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-11-26 03:16:33 | [CVE-2026-123679](https://nvd.nist.gov/vuln/detail/CVE-2026-123679) | High | 7.0 | An improper access control vulnerability exists in a privileged Unix domain socket of StellarProtect Linux and Stellar… |
| 2026-11-26 03:16:34 | [CVE-2026-123680](https://nvd.nist.gov/vuln/detail/CVE-2026-123680) | High | 8.6 | An authenticated remote code execution vulnerability exists in the firmware update functionality of StellarOne. An atta… |
| 2026-11-26 03:16:34 | [CVE-2026-123681](https://nvd.nist.gov/vuln/detail/CVE-2026-123681) | Low | 2.3 | An HTML injection vulnerability exists in the alert notification functionality of StellarOne due to improper sanitizati… |
| 2026-11-26 03:16:35 | [CVE-2026-123682](https://nvd.nist.gov/vuln/detail/CVE-2026-123682) | High | 8.6 | An authenticated remote code execution vulnerability exists in the update functionality of StellarOne due to insufficie… |
| 2026-11-26 03:16:35 | [CVE-2026-123683](https://nvd.nist.gov/vuln/detail/CVE-2026-123683) | Medium | 6.9 | A SQL injection vulnerability exists in an Accounts Manager service of StellarOne running inside a container due to imp… |
| 2026-11-26 03:16:35 | [CVE-2026-123684](https://nvd.nist.gov/vuln/detail/CVE-2026-123684) | Medium | 6.7 | An improper version validation vulnerability exists in the product update mechanism of StellarProtect Linux and Stellar… |
| 2026-11-26 03:16:35 | [CVE-2026-123685](https://nvd.nist.gov/vuln/detail/CVE-2026-123685) | High | 8.7 | A remote code execution vulnerability exists in the patch apply functionality of StellarProtect Linux and Stellar Agent… |
| 2026-11-26 03:16:35 | [CVE-2026-123686](https://nvd.nist.gov/vuln/detail/CVE-2026-123686) | High | 8.4 | An OS command injection vulnerability exists in the vShell command-line interface of StellarOne due to improper validat… |
| 2026-11-26 03:16:35 | [CVE-2026-123687](https://nvd.nist.gov/vuln/detail/CVE-2026-123687) | High | 8.6 | An arbitrary file write vulnerability exists in the patch upload functionality of StellarOne due to improper validation… |
| 2026-11-26 03:16:38 | [CVE-2026-136991](https://nvd.nist.gov/vuln/detail/CVE-2026-136991) | Low | 2.1 | A weakness has been identified in Spotweb up to 1.5.8. This issue affects the function redirect of the file lib/SpotTem… |
| 2026-11-26 03:16:39 | [CVE-2026-137043](https://nvd.nist.gov/vuln/detail/CVE-2026-137043) | Critical | 9.3 | A security vulnerability has been detected in TOTOLINK N350RT 9.3.5u.6468_B20250827/9.3.5u.6466_B20250825. The affected… |
| 2026-11-26 03:16:39 | [CVE-2026-137046](https://nvd.nist.gov/vuln/detail/CVE-2026-137046) | Medium | 5.5 | A vulnerability was detected in mahmoudai1 school-management-system up to ecec9faaf2fb1a3c5cd096e063f8ef326d09cdfd. The… |
| 2026-11-26 03:16:39 | [CVE-2026-137326](https://nvd.nist.gov/vuln/detail/CVE-2026-137326) | High | 7.3 | ICU4C through 79.1 contains a use-after-free and double free vulnerability in the x11-compound-text converter because c… |
| 2026-11-26 03:16:39 | [CVE-2026-137327](https://nvd.nist.gov/vuln/detail/CVE-2026-137327) | Medium | 4.8 | GNU mtools through 4.0.50 contains a divide-by-zero vulnerability that allows attackers to crash mtools commands by sup… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
