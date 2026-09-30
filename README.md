# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-09-30 12:18 UTC

New CVEs published between 2026-09-30 11:18 UTC and 2026-09-30 12:18 UTC.

[Full CSV](data/new-cves-2026-09-30T12-18-39-726393Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-09-30 12:17:12 | [CVE-2026-103012](https://nvd.nist.gov/vuln/detail/CVE-2026-103012) | Low | 2.0 | Claude Code selected an API key stored by Claude Code, for example from an earlier `/login` or written directly to its… |
| 2026-09-30 12:17:12 | [CVE-2026-103114](https://nvd.nist.gov/vuln/detail/CVE-2026-103114) | Low | 2.1 | A vulnerability was identified in OS4ED openSIS-Classic up to 9.3. The impacted element is the function DBQuery_assignm… |
| 2026-09-30 12:17:12 | [CVE-2026-103242](https://nvd.nist.gov/vuln/detail/CVE-2026-103242) | High | 7.1 | A heap-based buffer overflow flaw was found in rpm. RPMTAG_FILESIGNATURES in a crafted, unsigned RPM package's main hea… |
| 2026-09-30 12:17:12 | [CVE-2026-10726](https://nvd.nist.gov/vuln/detail/CVE-2026-10726) | Medium | 6.8 | Cato Windows SDP Client before version 6.12.6 contains an arbitrary file disclosure vulnerability. A low-privileged loc… |
| 2026-09-30 12:17:12 | [CVE-2026-10739](https://nvd.nist.gov/vuln/detail/CVE-2026-10739) | High | 8.5 | Cato Networks SDP Client for Windows before 6.12.6 allows a local user to delete arbitrary files with SYSTEM privileges… |
| 2026-09-30 12:17:13 | [CVE-2026-62146](https://nvd.nist.gov/vuln/detail/CVE-2026-62146) | High | 7.8 | A trust-boundary flaw in CRI-O's sandbox state persistence allows attacker-influenced pod metadata to overwrite CRI-O's… |
| 2026-09-30 12:17:13 | [CVE-2026-85532](https://nvd.nist.gov/vuln/detail/CVE-2026-85532) |  |  | Apache WSS4J accepted attacker-controlled derived-key lengths and offsets without adequate bounds. This could permit cr… |
| 2026-09-30 12:17:14 | [CVE-2026-87830](https://nvd.nist.gov/vuln/detail/CVE-2026-87830) |  |  | In the StAX streaming WS-SecurityPolicy validator, certain relative or unsupported XPath expressions can be converted i… |
| 2026-09-30 12:17:14 | [CVE-2026-88920](https://nvd.nist.gov/vuln/detail/CVE-2026-88920) |  |  | An authentication bypass in the DOM security processor in Apache WSS4J allows unauthenticated remote attackers to forge… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
