# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-02 18:19 UTC

New CVEs published between 2026-10-02 17:18 UTC and 2026-10-02 18:19 UTC.

[Full CSV](data/new-cves-2026-10-02T18-19-07-293706Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-10-02 18:16:59 | [CVE-2026-102626](https://nvd.nist.gov/vuln/detail/CVE-2026-102626) | High | 7.2 | An authenticated LimeSurvey Community Edition 7.4.0 user with the global Surveys: create permission can store a JavaScr… |
| 2026-10-02 18:16:59 | [CVE-2026-102795](https://nvd.nist.gov/vuln/detail/CVE-2026-102795) | High | 7.0 | Improper Access Control vulnerability in Apache Traffic Server. This issue affects Apache Traffic Server: from 9.0.0 th… |
| 2026-10-02 18:17:02 | [CVE-2026-104855](https://nvd.nist.gov/vuln/detail/CVE-2026-104855) | Low | 2.0 | Wasmtime is a runtime for WebAssembly. From 46.0.0 until 46.0.2 and 47.0.3, fuel and epoch preemption checks inside bul… |
| 2026-10-02 18:17:02 | [CVE-2026-104859](https://nvd.nist.gov/vuln/detail/CVE-2026-104859) | High | 7.3 | Nx is a monorepo solution for TypeScript and polyglot codebases. From 21.4.0 until 22.7.8 and from 23.0.0 until 23.1.1,… |
| 2026-10-02 18:17:02 | [CVE-2026-104861](https://nvd.nist.gov/vuln/detail/CVE-2026-104861) | High | 7.5 | probe-image-size gets image dimensions without downloading the entire file. Prior to 7.4.0, lib/parse_sync/svg.js and l… |
| 2026-10-02 18:17:03 | [CVE-2026-59265](https://nvd.nist.gov/vuln/detail/CVE-2026-59265) |  |  | A code execution issue in the Java integration in Apache OpenOffice v4.1.16 and earlier allows a crafted untrusted docu… |
| 2026-10-02 18:17:05 | [CVE-2026-64818](https://nvd.nist.gov/vuln/detail/CVE-2026-64818) |  |  | Rejected reason: This CVE ID has been rejected or withdrawn by its CVE Numbering Authority. |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
