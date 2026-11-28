# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-11-28 02:20 UTC

New CVEs published between 2026-11-28 01:20 UTC and 2026-11-28 02:20 UTC.

[Full CSV](data/new-cves-2026-11-28T02-20-34-742702Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-11-28 02:17:33 | [CVE-2026-138117](https://nvd.nist.gov/vuln/detail/CVE-2026-138117) | High | 8.5 | HyperSpy from 1.2.0 before 2.6.0 contains a code execution vulnerability that allows attackers to run Python code by em… |
| 2026-11-28 02:17:33 | [CVE-2026-138118](https://nvd.nist.gov/vuln/detail/CVE-2026-138118) | High | 8.5 | HyperSpy from 1.4.0 before 2.6.0 contains an insecure deserialization vulnerability that allows attackers to execute ar… |
| 2026-11-28 02:17:33 | [CVE-2026-138119](https://nvd.nist.gov/vuln/detail/CVE-2026-138119) | High | 8.7 | Kestra before 1.3.36 contains a reflected cross-site scripting vulnerability that allows unauthenticated attackers to e… |
| 2026-11-28 02:17:33 | [CVE-2026-138120](https://nvd.nist.gov/vuln/detail/CVE-2026-138120) | Medium | 6.9 | Kestra 1.3.24 before 2.0.0 contains a timing side-channel vulnerability in BasicAuthService.isAuthenticated() that allo… |
| 2026-11-28 02:17:33 | [CVE-2026-138121](https://nvd.nist.gov/vuln/detail/CVE-2026-138121) | High | 7.5 | Kestra 1.3.24 before 1.3.41 contains an insufficient credential expiration vulnerability that allows holders of a revok… |
| 2026-11-28 02:17:34 | [CVE-2026-138122](https://nvd.nist.gov/vuln/detail/CVE-2026-138122) | Low | 2.3 | ClassroomIO through 1.0.0 contains an insecure direct object reference vulnerability that allows authenticated course m… |
| 2026-11-28 02:17:34 | [CVE-2026-138148](https://nvd.nist.gov/vuln/detail/CVE-2026-138148) | Medium | 6.9 | picomatch through 4.0.7 contains a glob filter bypass vulnerability because globstar (**) patterns are compiled without… |
| 2026-11-28 02:17:34 | [CVE-2026-138149](https://nvd.nist.gov/vuln/detail/CVE-2026-138149) | Medium | 5.3 | FeatBit before 6.1.3 contains an authorization bypass vulnerability that allows authenticated members of one organizati… |
| 2026-11-28 02:17:34 | [CVE-2026-138150](https://nvd.nist.gov/vuln/detail/CVE-2026-138150) | Medium | 6.8 | SimGear through 2024.1.7 contains an infinite loop vulnerability in sgSimpleBuffer::resize() where an unsigned 32-bit w… |
| 2026-11-28 02:17:34 | [CVE-2026-138151](https://nvd.nist.gov/vuln/detail/CVE-2026-138151) | High | 8.2 | bgpq4 before 1.17 contains an integer overflow vulnerability in expander.c that allows malicious IRR servers to corrupt… |
| 2026-11-28 02:17:34 | [CVE-2026-138152](https://nvd.nist.gov/vuln/detail/CVE-2026-138152) | Medium | 5.3 | Otter – Page Builder Blocks & Extensions for Gutenberg before 3.2.12 contains a server-side request forgery vulnerabili… |
| 2026-11-28 02:17:35 | [CVE-2026-138153](https://nvd.nist.gov/vuln/detail/CVE-2026-138153) | Medium | 5.3 | Otter – Page Builder Blocks & Extensions for Gutenberg before 3.2.12 contains an incorrect authorization vulnerability… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
