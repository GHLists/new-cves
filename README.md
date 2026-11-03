# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-11-03 18:19 UTC

New CVEs published between 2026-11-03 17:20 UTC and 2026-11-03 18:19 UTC.

[Full CSV](data/new-cves-2026-11-03T18-19-37-059851Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-11-03 18:17:54 | [CVE-2026-116845](https://nvd.nist.gov/vuln/detail/CVE-2026-116845) | Medium | 5.3 | NetBox from 2.9.0 before 4.7.4 contains a broken access control vulnerability in BulkComponentCreateView that allows au… |
| 2026-11-03 18:17:57 | [CVE-2026-121263](https://nvd.nist.gov/vuln/detail/CVE-2026-121263) | Low | 2.1 | A vulnerability was determined in phpMyAdmin MoTranslator up to 6.0.1. The impacted element is the function Loader::get… |
| 2026-11-03 18:17:58 | [CVE-2026-121624](https://nvd.nist.gov/vuln/detail/CVE-2026-121624) | High | 7.6 | Nanosystems Supremo for Windows and macOS before 5.0.2.3874 contains an improper certificate validation vulnerability t… |
| 2026-11-03 18:17:58 | [CVE-2026-121625](https://nvd.nist.gov/vuln/detail/CVE-2026-121625) | Medium | 6.3 | GNU Gatekeeper (gnugk) before 5.16 contains an out-of-bounds read vulnerability in ParseRTCP() in ProxyChannel.cxx that… |
| 2026-11-03 18:17:58 | [CVE-2026-121626](https://nvd.nist.gov/vuln/detail/CVE-2026-121626) | Medium | 6.3 | GNU Gatekeeper (gnugk) before 5.16 contains an out-of-bounds read vulnerability in H46024Socket::ReceivedProbePacket()… |
| 2026-11-03 18:17:58 | [CVE-2026-121627](https://nvd.nist.gov/vuln/detail/CVE-2026-121627) | Medium | 5.3 | buku 5.0 through 5.1.1 contains a stored cross-site scripting vulnerability in the bukuserver bookmark list that allows… |
| 2026-11-03 18:17:58 | [CVE-2026-121628](https://nvd.nist.gov/vuln/detail/CVE-2026-121628) | Medium | 6.3 | Bagisto before 2.3.16 and 2.4.x before 2.4.1 contains a race condition vulnerability in manageCartRule() that allows at… |
| 2026-11-03 18:18:02 | [CVE-2026-44265](https://nvd.nist.gov/vuln/detail/CVE-2026-44265) | High | 7.4 | Elo is a purely functional expression language for no-code tools. Prior to 1.0.1, Elo's programmatic AST API accepts ar… |
| 2026-11-03 18:18:02 | [CVE-2026-44266](https://nvd.nist.gov/vuln/detail/CVE-2026-44266) | Critical | 9.8 | Elo is a purely functional expression language for no-code tools. Prior to 1.0.1, the Ruby backend in src/compilers/rub… |
| 2026-11-03 18:18:03 | [CVE-2026-44267](https://nvd.nist.gov/vuln/detail/CVE-2026-44267) | Critical | 9.8 | Elo is a purely functional expression language for no-code tools. Prior to 1.0.1, plain Elo strings supplied to default… |
| 2026-11-03 18:18:03 | [CVE-2026-63418](https://nvd.nist.gov/vuln/detail/CVE-2026-63418) | High | 7.0 | Monitoring Plugins is a suite of plugins for monitoring applications. From 3.0.0-rc1 until 3.0.1, check_icmp stores the… |
| 2026-11-03 18:18:03 | [CVE-2026-63436](https://nvd.nist.gov/vuln/detail/CVE-2026-63436) | Medium | 6.1 | zt-zip is a Java library that provides convenience methods for ZIP archive manipulation. Prior to 1.18.0, the Zips.get(… |
| 2026-11-03 18:18:03 | [CVE-2026-63492](https://nvd.nist.gov/vuln/detail/CVE-2026-63492) |  |  | Rejected reason: This CVE is a duplicate of another CVE. |
| 2026-11-03 18:18:04 | [CVE-2026-63494](https://nvd.nist.gov/vuln/detail/CVE-2026-63494) |  |  | Rejected reason: This CVE is a duplicate of another CVE. |
| 2026-11-03 18:18:04 | [CVE-2026-63499](https://nvd.nist.gov/vuln/detail/CVE-2026-63499) | Medium | 6.9 | zt-zip is a Java library that provides convenience methods for ZIP archive manipulation. Prior to 1.18.1, ZipUtil.unpac… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
