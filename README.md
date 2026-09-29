# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-09-29 04:18 UTC

New CVEs published between 2026-09-29 03:18 UTC and 2026-09-29 04:18 UTC.

[Full CSV](data/new-cves-2026-09-29T04-18-55-229329Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-09-29 04:17:52 | [CVE-2026-102245](https://nvd.nist.gov/vuln/detail/CVE-2026-102245) | Medium | 5.5 | A weakness has been identified in MODSetter SurfSense up to 2.0.3. The affected element is an unknown function of the f… |
| 2026-09-29 04:17:54 | [CVE-2026-102247](https://nvd.nist.gov/vuln/detail/CVE-2026-102247) | High | 7.1 | A vulnerability was detected in FastAdmin 1.6.1.20250430/1.6.5.20260602. This affects an unknown function of the file a… |
| 2026-09-29 04:17:54 | [CVE-2026-102248](https://nvd.nist.gov/vuln/detail/CVE-2026-102248) | Medium | 5.5 | A vulnerability was identified in Rebuild up to 4.4.7/4.5.0-beta5. This affects an unknown part of the file /user/login… |
| 2026-09-29 04:17:54 | [CVE-2026-102249](https://nvd.nist.gov/vuln/detail/CVE-2026-102249) | Medium | 5.5 | A security flaw has been discovered in REBUILD up to 4.4.11. This vulnerability affects unknown code of the file /commo… |
| 2026-09-29 04:17:55 | [CVE-2026-102414](https://nvd.nist.gov/vuln/detail/CVE-2026-102414) | Medium | 6.3 | pbkdf2 through 3.1.6 re-hashes passwords longer than the digest's block size on every iteration in its JavaScript fallb… |
| 2026-09-29 04:17:55 | [CVE-2026-102422](https://nvd.nist.gov/vuln/detail/CVE-2026-102422) | Critical | 9.2 | shell-quote's `quote()` function emits a `{ comment }` token as `#` followed by its text, which comments out the rest o… |
| 2026-09-29 04:18:02 | [CVE-2026-97024](https://nvd.nist.gov/vuln/detail/CVE-2026-97024) | High | 7.1 | A path traversal vulnerability in Flatpak's handling of the files/etc directory during app deployment allows a maliciou… |
| 2026-09-29 04:18:02 | [CVE-2026-97029](https://nvd.nist.gov/vuln/detail/CVE-2026-97029) | Medium | 5.7 | Flatpak's process ID namespace separation does not prevent a sandboxed app's kill(0, signal) or killpg(0, signal) calls… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
