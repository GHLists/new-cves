# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-11-26 08:19 UTC

New CVEs published between 2026-11-26 07:20 UTC and 2026-11-26 08:19 UTC.

[Full CSV](data/new-cves-2026-11-26T08-19-41-110785Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-11-26 08:17:06 | [CVE-2026-103383](https://nvd.nist.gov/vuln/detail/CVE-2026-103383) |  |  | In Eclipse MWE <= 2.27.0 if you debug mwe workflows a remote attacker can cause arbitrary classes with an zero arg cons… |
| 2026-11-26 08:17:06 | [CVE-2026-133336](https://nvd.nist.gov/vuln/detail/CVE-2026-133336) | Critical | 9.5 | Joomla Extension - chronoengine.com - Unauthenticated arbitrary file upload in ChronoForms extension 8.0.0-8.0.53 - Whe… |
| 2026-11-26 08:17:07 | [CVE-2026-133337](https://nvd.nist.gov/vuln/detail/CVE-2026-133337) | High | 8.2 | Joomla Extension - chronoengine.com - Unauthenticated SQL injection in table sorting in ChronoForms extension 8.0.0-8.0… |
| 2026-11-26 08:17:07 | [CVE-2026-133338](https://nvd.nist.gov/vuln/detail/CVE-2026-133338) | High | 7.6 | Joomla Extension - chronoengine.com - Unauthenticated stored XSS in DB Table cells in ChronoForms extension 8.0.0-8.0.5… |
| 2026-11-26 08:17:07 | [CVE-2026-133525](https://nvd.nist.gov/vuln/detail/CVE-2026-133525) | High | 8.8 | Deserialization of Untrusted Data vulnerability in ThemeFusion Fusion Builder fusion-builder allows Object Injection.Th… |
| 2026-11-26 08:17:07 | [CVE-2026-135772](https://nvd.nist.gov/vuln/detail/CVE-2026-135772) | High | 8.6 | RTL8762C MCU developed by Realtek Semiconductor Corporation has an Improper Protection Against Voltage and Clock Glitch… |
| 2026-11-26 08:17:07 | [CVE-2026-137035](https://nvd.nist.gov/vuln/detail/CVE-2026-137035) | Medium | 6.1 | A flaw was found in bootc. On a sealed composefs boot with a strict composefs digest on the kernel command line, the in… |
| 2026-11-26 08:17:07 | [CVE-2026-137036](https://nvd.nist.gov/vuln/detail/CVE-2026-137036) | Medium | 6.8 | A flaw was found in bootc. On a sealed composefs boot, a failed bootc-root-setup.service does not fail initrd-root-fs.t… |
| 2026-11-26 08:17:07 | [CVE-2026-137315](https://nvd.nist.gov/vuln/detail/CVE-2026-137315) | Low | 2.1 | A vulnerability was detected in SourceCodester Online Food Ordering System 1.0. This issue affects some unknown process… |
| 2026-11-26 08:17:08 | [CVE-2026-137316](https://nvd.nist.gov/vuln/detail/CVE-2026-137316) | Low | 2.1 | A flaw has been found in SourceCodester Online Food Ordering System 1.0. Impacted is an unknown function of the file ad… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
