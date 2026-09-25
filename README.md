# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-09-25 20:18 UTC

New CVEs published between 2026-09-25 19:19 UTC and 2026-09-25 20:18 UTC.

[Full CSV](data/new-cves-2026-09-25T20-18-56-105953Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-09-25 20:17:04 | [CVE-2026-100208](https://nvd.nist.gov/vuln/detail/CVE-2026-100208) | High | 7.5 | Integer overflow or wraparound in Microsoft Office Outlook allows an unauthorized attacker to execute code over a netwo… |
| 2026-09-25 20:17:05 | [CVE-2026-100310](https://nvd.nist.gov/vuln/detail/CVE-2026-100310) | High | 7.3 | GNU libextractor before 1.16 loads plugins from an untrusted search path specified by the LIBEXTRACTOR_PREFIX environme… |
| 2026-09-25 20:17:05 | [CVE-2026-100368](https://nvd.nist.gov/vuln/detail/CVE-2026-100368) | High | 8.4 | CliInvoke is a .NET library for invoking command-line programs, and its `CliInvoke.Specializations` packages provide sp… |
| 2026-09-25 20:17:06 | [CVE-2026-100372](https://nvd.nist.gov/vuln/detail/CVE-2026-100372) | High | 8.6 | ClipBucket v5 before 5.5.3-#197 contains a path traversal vulnerability in the admin template editor that allows authen… |
| 2026-09-25 20:17:06 | [CVE-2026-100373](https://nvd.nist.gov/vuln/detail/CVE-2026-100373) | Medium | 5.1 | OpenMetadata through 2.0.2 contains a server-side request forgery vulnerability in the URLValidator.validateURL functio… |
| 2026-09-25 20:17:07 | [CVE-2026-53990](https://nvd.nist.gov/vuln/detail/CVE-2026-53990) |  |  | Rejected reason: This CVE ID has been rejected or withdrawn by its CVE Numbering Authority. |
| 2026-09-25 20:17:09 | [CVE-2026-57861](https://nvd.nist.gov/vuln/detail/CVE-2026-57861) |  |  | Rejected reason: This CVE ID has been rejected or withdrawn by its CVE Numbering Authority. |
| 2026-09-25 20:17:11 | [CVE-2026-5267](https://nvd.nist.gov/vuln/detail/CVE-2026-5267) |  |  | Ciena Navigator Network Control Suite (NCS) contains an information exposure vulnerability in an event-streaming API th… |
| 2026-09-25 20:17:47 | [CVE-2026-93682](https://nvd.nist.gov/vuln/detail/CVE-2026-93682) | Medium | 5.8 | When the HTTP stream wrapper follows a redirect and the response carries a Location header with an empty value, the red… |
| 2026-09-25 20:17:47 | [CVE-2026-96875](https://nvd.nist.gov/vuln/detail/CVE-2026-96875) | Medium | 6.9 | Improper neutralization of input during web page generation ('cross-site scripting') vulnerability in Mediawiki - Cargo… |
| 2026-09-25 20:17:47 | [CVE-2026-96876](https://nvd.nist.gov/vuln/detail/CVE-2026-96876) | Medium | 6.9 | Improper neutralization of input during web page generation ('cross-site scripting') vulnerability in Mediawiki - Cargo… |
| 2026-09-25 20:17:48 | [CVE-2026-96877](https://nvd.nist.gov/vuln/detail/CVE-2026-96877) | Medium | 6.9 | Improper neutralization of input during web page generation ('cross-site scripting') vulnerability in Mediawiki - Cargo… |
| 2026-09-25 20:17:48 | [CVE-2026-96878](https://nvd.nist.gov/vuln/detail/CVE-2026-96878) | Medium | 6.9 | Improper neutralization of input during web page generation ('cross-site scripting') vulnerability in Mediawiki - Cargo… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
