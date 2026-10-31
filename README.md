# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-31 18:18 UTC

New CVEs published between 2026-10-31 17:20 UTC and 2026-10-31 18:18 UTC.

[Full CSV](data/new-cves-2026-10-31T18-18-12-20461Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-10-31 18:17:07 | [CVE-2026-120199](https://nvd.nist.gov/vuln/detail/CVE-2026-120199) | Medium | 5.3 | LearnHouse before 1.1.1 contains a missing authorization vulnerability in the assignment API that allows authenticated… |
| 2026-10-31 18:17:07 | [CVE-2026-120200](https://nvd.nist.gov/vuln/detail/CVE-2026-120200) | Medium | 5.3 | Nexterm through 1.2.2-BETA contains a missing authorization vulnerability that allows authenticated users to hibernate,… |
| 2026-10-31 18:17:07 | [CVE-2026-120201](https://nvd.nist.gov/vuln/detail/CVE-2026-120201) | Critical | 9.3 | Jpom 2.10.0 through 2.11.12 contains an authentication bypass vulnerability that allows unauthenticated attackers to ga… |
| 2026-10-31 18:17:08 | [CVE-2026-120202](https://nvd.nist.gov/vuln/detail/CVE-2026-120202) | High | 7.1 | Highflame ramparts 0.8.1 through 0.8.10 contains a security scan bypass vulnerability that allows attackers to hide mal… |
| 2026-10-31 18:17:08 | [CVE-2026-120203](https://nvd.nist.gov/vuln/detail/CVE-2026-120203) | High | 8.7 | ShowDoc 2.8.14 before 3.9.6 contains a code injection vulnerability in its Mock feature that allows authenticated users… |
| 2026-10-31 18:17:08 | [CVE-2026-120204](https://nvd.nist.gov/vuln/detail/CVE-2026-120204) | Medium | 6.3 | DeepInfer through 0.1.0 contains a path traversal vulnerability in the unauthenticated /profile endpoint that allows re… |
| 2026-10-31 18:17:08 | [CVE-2026-120205](https://nvd.nist.gov/vuln/detail/CVE-2026-120205) | High | 7.4 | Thelia before 3.1.0 contains a stored cross-site scripting vulnerability in ForSomeCustomers::getSummary() that allows… |
| 2026-10-31 18:17:08 | [CVE-2026-120206](https://nvd.nist.gov/vuln/detail/CVE-2026-120206) | Medium | 5.9 | Thelia before 3.2.0 contains a cross-site request forgery vulnerability in the back office that allows attackers to for… |
| 2026-10-31 18:17:08 | [CVE-2026-120207](https://nvd.nist.gov/vuln/detail/CVE-2026-120207) | High | 7.0 | Thelia Page Module before 2.0.4 contains a cross-site request forgery vulnerability that allows remote attackers to del… |
| 2026-10-31 18:17:09 | [CVE-2026-120208](https://nvd.nist.gov/vuln/detail/CVE-2026-120208) | High | 7.7 | libheif 1.18.0 before 1.23.3 contains a heap-based buffer overflow vulnerability in unc_decoder_mixed_interleave::proce… |
| 2026-10-31 18:17:09 | [CVE-2026-120209](https://nvd.nist.gov/vuln/detail/CVE-2026-120209) | Critical | 9.3 | AJ-Report through 1.7.1 signs share tokens with a hard-coded JWT secret, allowing attackers to forge valid Share-Tokens… |
| 2026-10-31 18:17:09 | [CVE-2026-120210](https://nvd.nist.gov/vuln/detail/CVE-2026-120210) | Medium | 5.3 | FFmpeg 5.0 through 9.0.2 contains a path traversal vulnerability in the IMF demuxer that allows attackers to open files… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
