# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-01 21:18 UTC

New CVEs published between 2026-10-01 20:18 UTC and 2026-10-01 21:18 UTC.

[Full CSV](data/new-cves-2026-10-01T21-18-36-925378Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-10-01 21:17:17 | [CVE-2026-102370](https://nvd.nist.gov/vuln/detail/CVE-2026-102370) | Medium | 5.4 | Kasa EC70 v4 and EC71 v4 do not logically disable the production debug interface at the firmware or chip level and do n… |
| 2026-10-01 21:17:18 | [CVE-2026-102514](https://nvd.nist.gov/vuln/detail/CVE-2026-102514) | High | 8.4 | Out-of-bounds Write (CWE-787) in the PEA archive extraction routine (pea.pas, unpea_procedure) of the first-party pea c… |
| 2026-10-01 21:17:18 | [CVE-2026-104020](https://nvd.nist.gov/vuln/detail/CVE-2026-104020) | High | 8.7 | Uncontrolled recursion in the Ion reader in Amazon Ion Python before 0.15.0 might allow a remote unauthenticated actor… |
| 2026-10-01 21:17:18 | [CVE-2026-104181](https://nvd.nist.gov/vuln/detail/CVE-2026-104181) | Medium | 5.4 | Filament is a collection of full-stack components for accelerated Laravel development. From 4.0.0 until 4.13.3 and 5.8.… |
| 2026-10-01 21:17:19 | [CVE-2026-104182](https://nvd.nist.gov/vuln/detail/CVE-2026-104182) | Medium | 6.2 | stream-json is a micro-library of stream components for processing JSON and JSONC with a minimal memory footprint. Prio… |
| 2026-10-01 21:17:19 | [CVE-2026-104183](https://nvd.nist.gov/vuln/detail/CVE-2026-104183) | Medium | 5.1 | stream-json is a micro-library of stream components for processing JSON and JSONC with a minimal memory footprint. Prio… |
| 2026-10-01 21:17:20 | [CVE-2026-27874](https://nvd.nist.gov/vuln/detail/CVE-2026-27874) | Medium | 5.9 | : Use of Hard-coded Credentials vulnerability in Johnson Controls EasyIO FS32 allows : Exploitation of Default or Hard-… |
| 2026-10-01 21:17:21 | [CVE-2026-55393](https://nvd.nist.gov/vuln/detail/CVE-2026-55393) | Critical | 10.0 | Unvalidated pathnames in the web interface in Teledyne FLIR Aware2 versions through 6.9.0.2 (PackBot) and 1.7.9 (FirstL… |
| 2026-10-01 21:17:21 | [CVE-2026-55394](https://nvd.nist.gov/vuln/detail/CVE-2026-55394) | Medium | 5.3 | Unencrypted traffic in the 802.11 network of Teledyne FLIR Aware2 versions through 6.9.0.2 allows adjacent unauthentica… |
| 2026-10-01 21:17:21 | [CVE-2026-55395](https://nvd.nist.gov/vuln/detail/CVE-2026-55395) | Critical | 9.4 | Hardcoded passwords in the access control in Teledyne FLIR Aware2 versions through 6.9.0.2 (PackBot) and 1.7.9 (FirstLo… |
| 2026-10-01 21:17:21 | [CVE-2026-55396](https://nvd.nist.gov/vuln/detail/CVE-2026-55396) | High | 8.5 | Cleartext transmission without a cryptographic integrity check in operator control unit to robot UDP traffic in Teledyn… |
| 2026-10-01 21:17:24 | [CVE-2026-71451](https://nvd.nist.gov/vuln/detail/CVE-2026-71451) | High | 7.2 | - OS Command Injection vulnerability in Johnson Controls EasyIO FS32 allows - Command Injection. This issue affects Eas… |
| 2026-10-01 21:17:26 | [CVE-2026-96780](https://nvd.nist.gov/vuln/detail/CVE-2026-96780) | High | 8.2 | figlet.js is a FIG driver written in JavaScript that aims to implement the FIGfont specification. Prior to 1.11.3, text… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
