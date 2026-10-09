# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-09 14:18 UTC

New CVEs published between 2026-10-09 13:18 UTC and 2026-10-09 14:18 UTC.

[Full CSV](data/new-cves-2026-10-09T14-18-52-836175Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-10-09 14:17:09 | [CVE-2026-100730](https://nvd.nist.gov/vuln/detail/CVE-2026-100730) | Critical | 9.3 | A service console interface on openPDC and openHistorian deserializes a client-supplied data structure. On systems usin… |
| 2026-10-09 14:17:10 | [CVE-2026-101022](https://nvd.nist.gov/vuln/detail/CVE-2026-101022) | Medium | 5.3 | A Modbus connection feature on openPDC accepts a caller-specified destination address and port with no restriction on w… |
| 2026-10-09 14:17:11 | [CVE-2026-104629](https://nvd.nist.gov/vuln/detail/CVE-2026-104629) | High | 7.7 | A component loading mechanism in openPDC and openHistorian will construct and run any specified type, which may be an i… |
| 2026-10-09 14:17:11 | [CVE-2026-105281](https://nvd.nist.gov/vuln/detail/CVE-2026-105281) | High | 8.7 | The internal data publisher on openPDC accepts network connections without authentication in its default configuration.… |
| 2026-10-09 14:17:18 | [CVE-2026-106581](https://nvd.nist.gov/vuln/detail/CVE-2026-106581) | High | 7.3 | Before 4.92.0, Docker Desktop for Windows did not verify the signature of a package supplied to Docker Desktop Installe… |
| 2026-10-09 14:17:19 | [CVE-2026-107785](https://nvd.nist.gov/vuln/detail/CVE-2026-107785) | Medium | 6.3 | Crux Agent from 1.9.0 before 2.0.3 uses the full SKA bilocation key as the WireGuard preshared key. When a peering sess… |
| 2026-10-09 14:17:19 | [CVE-2026-107803](https://nvd.nist.gov/vuln/detail/CVE-2026-107803) | Medium | 6.5 | ProcessMaker is an open source workflow management software suite. Prior to 2026.14.3, the `GET /api/1.0/tasks` endpoin… |
| 2026-10-09 14:17:20 | [CVE-2026-108063](https://nvd.nist.gov/vuln/detail/CVE-2026-108063) | Medium | 5.5 | A flaw was found in libhangul. When parsing Hanja dictionary files, the library fails to verify that an entry contains… |
| 2026-10-09 14:17:22 | [CVE-2026-62026](https://nvd.nist.gov/vuln/detail/CVE-2026-62026) | High | 7.1 | Cross-Site Request Forgery (CSRF) vulnerability in MIGHTYminnow Dashboard Notes dashboard-notes allows Cross Site Reque… |
| 2026-10-09 14:17:22 | [CVE-2026-79363](https://nvd.nist.gov/vuln/detail/CVE-2026-79363) |  |  | Cloudron 9.1.7 and 9.2 contain a stored cross-site scripting (XSS) vulnerability in the Branding Footer feature. An aut… |
| 2026-10-09 14:17:23 | [CVE-2026-85479](https://nvd.nist.gov/vuln/detail/CVE-2026-85479) | Medium | 6.9 | The STTP-based data publisher on openPDC accepts network connections without authentication in its default configuratio… |
| 2026-10-09 14:17:24 | [CVE-2026-92085](https://nvd.nist.gov/vuln/detail/CVE-2026-92085) | Medium | 5.4 | Improper neutralization of input during web page generation ('cross-site scripting') vulnerability in TMT Machinery Ind… |
| 2026-10-09 14:17:24 | [CVE-2026-94063](https://nvd.nist.gov/vuln/detail/CVE-2026-94063) | High | 7.1 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in ThemeREX Educatio… |
| 2026-10-09 14:17:25 | [CVE-2026-94064](https://nvd.nist.gov/vuln/detail/CVE-2026-94064) | High | 8.8 | Deserialization of Untrusted Data vulnerability in BuddhaThemes Neo \| Barber Shop WordPress Theme neocut allows Object… |
| 2026-10-09 14:17:25 | [CVE-2026-94065](https://nvd.nist.gov/vuln/detail/CVE-2026-94065) | High | 8.8 | Deserialization of Untrusted Data vulnerability in BuddhaThemes ColorFolio colorit allows Object Injection.This issue a… |
| 2026-10-09 14:17:25 | [CVE-2026-94066](https://nvd.nist.gov/vuln/detail/CVE-2026-94066) | High | 7.1 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in SpabRice Pond pon… |
| 2026-10-09 14:17:26 | [CVE-2026-94067](https://nvd.nist.gov/vuln/detail/CVE-2026-94067) | High | 8.1 | Improper Control of Filename for Include/Require Statement in PHP Program ('PHP Remote File Inclusion') vulnerability i… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
