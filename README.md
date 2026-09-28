# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-09-28 20:19 UTC

New CVEs published between 2026-09-28 19:21 UTC and 2026-09-28 20:19 UTC.

[Full CSV](data/new-cves-2026-09-28T20-19-16-421723Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-09-28 20:17:08 | [CVE-2026-101141](https://nvd.nist.gov/vuln/detail/CVE-2026-101141) | Low | 2.0 | A flaw has been found in Eleveo Call Recording Software 9.7.0. Affected is an unknown function of the file /callrec/aud… |
| 2026-09-28 20:17:08 | [CVE-2026-101142](https://nvd.nist.gov/vuln/detail/CVE-2026-101142) | Low | 2.1 | A vulnerability has been found in Eleveo Quality Management 9.7.0. Affected by this vulnerability is an unknown functio… |
| 2026-09-28 20:17:08 | [CVE-2026-101143](https://nvd.nist.gov/vuln/detail/CVE-2026-101143) | Low | 2.1 | A vulnerability was found in Eleveo Quality Management 9.7.0. Affected by this issue is some unknown functionality of t… |
| 2026-09-28 20:17:09 | [CVE-2026-101914](https://nvd.nist.gov/vuln/detail/CVE-2026-101914) | Medium | 6.5 | @grpc/grpc-js implements the core functionality of gRPC purely in JavaScript, without a C++ addon. Prior to 1.13.1 and… |
| 2026-09-28 20:17:09 | [CVE-2026-101915](https://nvd.nist.gov/vuln/detail/CVE-2026-101915) | Low | 3.7 | @grpc/grpc-js implements the core functionality of gRPC purely in JavaScript, without a C++ addon. Prior to 1.13.6 and… |
| 2026-09-28 20:17:09 | [CVE-2026-102004](https://nvd.nist.gov/vuln/detail/CVE-2026-102004) | High | 7.8 | Wind River VxWorks 7 prior to 26.09, specific system call arguments can result in memory corruption within the memory m… |
| 2026-09-28 20:17:11 | [CVE-2026-86950](https://nvd.nist.gov/vuln/detail/CVE-2026-86950) | High | 8.8 | An out-of-bounds write issue was addressed with improved bounds checking. This issue is fixed in iOS 26.7.1 and iPadOS… |
| 2026-09-28 20:17:11 | [CVE-2026-87741](https://nvd.nist.gov/vuln/detail/CVE-2026-87741) | High | 8.8 | The ConvertPlus plugin for WordPress is vulnerable to Deserialization of Untrusted Data in all versions up to, and incl… |
| 2026-09-28 20:17:11 | [CVE-2026-93355](https://nvd.nist.gov/vuln/detail/CVE-2026-93355) | High | 7.6 | LiteLLM contains a weak authentication vulnerability that allows an attacker holding a valid JWT from the configured id… |
| 2026-09-28 20:17:11 | [CVE-2026-96760](https://nvd.nist.gov/vuln/detail/CVE-2026-96760) |  |  | Authlib (v1.7.2 and below) contains a signature verification bypass vulnerability. The JsonWebSignature.deserialize_jso… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
