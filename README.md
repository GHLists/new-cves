# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-22 20:18 UTC

New CVEs published between 2026-10-22 19:19 UTC and 2026-10-22 20:18 UTC.

[Full CSV](data/new-cves-2026-10-22T20-18-35-751204Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-10-22 20:17:05 | [CVE-2026-112330](https://nvd.nist.gov/vuln/detail/CVE-2026-112330) | High | 8.7 | Motor.NET before 0.19.0 contains a denial of service vulnerability that allows a remote attacker who can publish to a c… |
| 2026-10-22 20:17:05 | [CVE-2026-112331](https://nvd.nist.gov/vuln/detail/CVE-2026-112331) | High | 8.7 | Motor.NET before 0.19.0 contains a denial-of-service vulnerability that allows a remote attacker who can produce record… |
| 2026-10-22 20:17:05 | [CVE-2026-112332](https://nvd.nist.gov/vuln/detail/CVE-2026-112332) | High | 8.7 | Motor.NET before 0.19.0 contains an uncaught exception vulnerability in JsonNetDeserializer.Deserialize that allows a r… |
| 2026-10-22 20:17:06 | [CVE-2026-115398](https://nvd.nist.gov/vuln/detail/CVE-2026-115398) | Medium | 6.8 | Ghidra before 12.2 contains a resource allocation without limits vulnerability in FileSystemIndexHelper used by TarFile… |
| 2026-10-22 20:17:06 | [CVE-2026-115503](https://nvd.nist.gov/vuln/detail/CVE-2026-115503) | Medium | 6.8 | Ghidra before 12.2 contains an improper handling of highly compressed data vulnerability in ExtensionUtils.unzipToInsta… |
| 2026-10-22 20:17:06 | [CVE-2026-115504](https://nvd.nist.gov/vuln/detail/CVE-2026-115504) | High | 8.5 | CFITSIO through 4.7.0 contains an out-of-bounds write vulnerability in ffgcls2() in getcols.c that trusts attacker-cont… |
| 2026-10-22 20:17:06 | [CVE-2026-115505](https://nvd.nist.gov/vuln/detail/CVE-2026-115505) | High | 7.2 | libsmb2 before 6.3 contains integer overflow vulnerabilities in the DCE/RPC NDR decoder in lib/dcerpc.c that allow heap… |
| 2026-10-22 20:17:06 | [CVE-2026-115506](https://nvd.nist.gov/vuln/detail/CVE-2026-115506) | High | 8.7 | libexpat through 2.9.0 contains a denial of service vulnerability because billion laughs protection in accountingDiffTo… |
| 2026-10-22 20:17:06 | [CVE-2026-115507](https://nvd.nist.gov/vuln/detail/CVE-2026-115507) | Medium | 5.1 | Vikunja 2.2.0 before 2.7.1 contains an HTML injection vulnerability in CreateConversationalHeader in pkg/notifications/… |
| 2026-10-22 20:17:06 | [CVE-2026-115508](https://nvd.nist.gov/vuln/detail/CVE-2026-115508) | High | 7.1 | Crawl4AI 0.7.0 before 0.9.5 contains an inefficient regular expression complexity vulnerability in the Docker API serve… |
| 2026-10-22 20:17:07 | [CVE-2026-115509](https://nvd.nist.gov/vuln/detail/CVE-2026-115509) | Low | 2.3 | Jitsu console before 2.14.0-beta.41 contains an incorrect authorization vulnerability in sources/state.ts handlers that… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
