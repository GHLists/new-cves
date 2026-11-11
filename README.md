# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-11-11 11:18 UTC

New CVEs published between 2026-11-11 10:20 UTC and 2026-11-11 11:18 UTC.

[Full CSV](data/new-cves-2026-11-11T11-18-53-588754Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-11-11 11:17:11 | [CVE-2026-111792](https://nvd.nist.gov/vuln/detail/CVE-2026-111792) |  |  | Uncontrolled Recursion vulnerability in Apache XML Graphics Batik. This issue affects Apache XML Graphics Batik: throug… |
| 2026-11-11 11:17:13 | [CVE-2026-118965](https://nvd.nist.gov/vuln/detail/CVE-2026-118965) | Critical | 9.4 | Path traversal in the discovered host label synchronization in Checkmk <2.5.0p19, <2.4.0p40 and 2.3.0 (EOL) allows an a… |
| 2026-11-11 11:17:13 | [CVE-2026-120495](https://nvd.nist.gov/vuln/detail/CVE-2026-120495) | Critical | 9.4 | Path traversal in the Synthetic Monitoring "Robotmk" test service of Checkmk <2.5.0p19, <2.4.0p40, and 2.3.0 (EOL) allo… |
| 2026-11-11 11:17:14 | [CVE-2026-121374](https://nvd.nist.gov/vuln/detail/CVE-2026-121374) | Critical | 9.4 | Argument injection in the Kubernetes special agent in Checkmk <2.5.0p19, <2.4.0p40, and 2.3.0 (EOL) allows a user with… |
| 2026-11-11 11:17:16 | [CVE-2026-123478](https://nvd.nist.gov/vuln/detail/CVE-2026-123478) | High | 7.1 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in Meow Apps AI Engi… |
| 2026-11-11 11:17:16 | [CVE-2026-124253](https://nvd.nist.gov/vuln/detail/CVE-2026-124253) | High | 7.1 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in codepeople Calcul… |
| 2026-11-11 11:17:16 | [CVE-2026-124739](https://nvd.nist.gov/vuln/detail/CVE-2026-124739) | High | 7.5 | A flaw was found in BusyBox. When the httpd web server processes subdirectory configuration files, an overly long index… |
| 2026-11-11 11:17:17 | [CVE-2026-124741](https://nvd.nist.gov/vuln/detail/CVE-2026-124741) | High | 7.6 | A flaw was found in BusyBox. The udhcpc6 DHCPv6 client does not properly validate the size of network options sent by a… |
| 2026-11-11 11:17:21 | [CVE-2026-78287](https://nvd.nist.gov/vuln/detail/CVE-2026-78287) | Critical | 10.0 | Improper Control of Generation of Code ('Code Injection') vulnerability in Staggs STAGGS staggs allows Remote Code Incl… |
| 2026-11-11 11:17:22 | [CVE-2026-90993](https://nvd.nist.gov/vuln/detail/CVE-2026-90993) |  |  | XXE vulnerability in Apache XML Graphics Batik. This issue affects Apache XML Graphics Batik: through 1.19. Users are r… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
