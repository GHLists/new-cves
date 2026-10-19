# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-19 19:18 UTC

New CVEs published between 2026-10-19 18:19 UTC and 2026-10-19 19:18 UTC.

[Full CSV](data/new-cves-2026-10-19T19-18-59-131493Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-10-19 19:17:03 | [CVE-2025-60482](https://nvd.nist.gov/vuln/detail/CVE-2025-60482) |  |  | A heap use-after-free in the gf_odf_ac4_cfg_clean_list function (/odf/descriptors.c) of GPAC Project/MP4Box 2.5-DEV-rev… |
| 2026-10-19 19:17:19 | [CVE-2026-109434](https://nvd.nist.gov/vuln/detail/CVE-2026-109434) | Medium | 5.1 | Fenrir Sleipnir Browser for Android before 3.9.0 contains a UI spoofing vulnerability that allows remote attackers to i… |
| 2026-10-19 19:17:19 | [CVE-2026-109437](https://nvd.nist.gov/vuln/detail/CVE-2026-109437) | Critical | 9.2 | Cognition before 0.13.0 contains an unauthenticated remote code execution vulnerability due to defaulting its agent san… |
| 2026-10-19 19:17:20 | [CVE-2026-110672](https://nvd.nist.gov/vuln/detail/CVE-2026-110672) |  |  | Cpanel::JSON::XS versions before 4.80 for Perl leak the decoded key of an object rejected for a duplicate key or a miss… |
| 2026-10-19 19:17:20 | [CVE-2026-110673](https://nvd.nist.gov/vuln/detail/CVE-2026-110673) |  |  | Cpanel::JSON::XS versions before 4.80 for Perl allow stack exhaustion via nested tagged values under allow_tags in deco… |
| 2026-10-19 19:17:21 | [CVE-2026-110674](https://nvd.nist.gov/vuln/detail/CVE-2026-110674) |  |  | Cpanel::JSON::XS versions from 4.33 before 4.80 for Perl miss duplicate non-ASCII bare keys, allowing type confusion un… |
| 2026-10-19 19:17:21 | [CVE-2026-110675](https://nvd.nist.gov/vuln/detail/CVE-2026-110675) |  |  | Cpanel::JSON::XS versions from 4.33 before 4.80 for Perl accept malformed UTF-8 in bare hash keys under allow_barekey i… |
| 2026-10-19 19:17:21 | [CVE-2026-110676](https://nvd.nist.gov/vuln/detail/CVE-2026-110676) |  |  | Cpanel::JSON::XS versions before 4.80 for Perl allow memory exhaustion by encoding exponent notation as full decimal di… |
| 2026-10-19 19:17:21 | [CVE-2026-110677](https://nvd.nist.gov/vuln/detail/CVE-2026-110677) |  |  | Cpanel::JSON::XS versions from 4.28 before 4.80 for Perl leak the array collecting duplicate key values under dupkeys_a… |
| 2026-10-19 19:17:21 | [CVE-2026-110678](https://nvd.nist.gov/vuln/detail/CVE-2026-110678) |  |  | Cpanel::JSON::XS versions before 4.80 for Perl allow memory exhaustion by buffering incremental input past max_size in… |
| 2026-10-19 19:17:21 | [CVE-2026-110680](https://nvd.nist.gov/vuln/detail/CVE-2026-110680) |  |  | Cpanel::JSON::XS versions from 4.20 before 4.80 for Perl write out of bounds when a tied or shared hash grows during ca… |
| 2026-10-19 19:17:21 | [CVE-2026-110681](https://nvd.nist.gov/vuln/detail/CVE-2026-110681) |  |  | Cpanel::JSON::XS versions before 4.80 for Perl use the parent interpreter's scalars from a parser object cloned into a… |
| 2026-10-19 19:17:21 | [CVE-2026-110682](https://nvd.nist.gov/vuln/detail/CVE-2026-110682) |  |  | Cpanel::JSON::XS versions from 4.42 before 4.80 for Perl let input chunking change the decoded value of top-level numbe… |
| 2026-10-19 19:17:21 | [CVE-2026-110684](https://nvd.nist.gov/vuln/detail/CVE-2026-110684) |  |  | Cpanel::JSON::XS versions from 3.0202 before 4.80 for Perl leak memory and retain overloaded objects when encoding valu… |
| 2026-10-19 19:17:22 | [CVE-2026-110685](https://nvd.nist.gov/vuln/detail/CVE-2026-110685) |  |  | Cpanel::JSON::XS versions before 4.80 for Perl leak the decoded arguments of a tagged value when its THAW method dies i… |
| 2026-10-19 19:17:22 | [CVE-2026-110686](https://nvd.nist.gov/vuln/detail/CVE-2026-110686) |  |  | Cpanel::JSON::XS versions before 4.80 for Perl use freed filter callbacks when a filter removes itself during decoding… |
| 2026-10-19 19:17:22 | [CVE-2026-110687](https://nvd.nist.gov/vuln/detail/CVE-2026-110687) |  |  | Cpanel::JSON::XS versions from 4.43 before 4.80 for Perl misorder byte-string keys during canonical encoding in utf16_c… |
| 2026-10-19 19:17:22 | [CVE-2026-110688](https://nvd.nist.gov/vuln/detail/CVE-2026-110688) |  |  | Cpanel::JSON::XS versions from 4.51 before 4.80 for Perl allow quadratic CPU use by revalidating the remaining buffer p… |
| 2026-10-19 19:17:26 | [CVE-2026-112249](https://nvd.nist.gov/vuln/detail/CVE-2026-112249) | Medium | 4.8 | A vulnerability was detected in grandnode grandnode2 up to 2.3.0. Affected is the function Html.Raw of the file src/Web… |
| 2026-10-19 19:17:26 | [CVE-2026-112251](https://nvd.nist.gov/vuln/detail/CVE-2026-112251) | Low | 2.1 | A vulnerability was detected in antoinersx clawhost up to 0.0.45. This affects the function handleRequest of the file a… |
| 2026-10-19 19:17:27 | [CVE-2026-112252](https://nvd.nist.gov/vuln/detail/CVE-2026-112252) | Medium | 5.5 | A vulnerability has been found in Wuxi Wubang Security Software Wubang Five-in-One Safety Production Management Informa… |
| 2026-10-19 19:17:27 | [CVE-2026-112259](https://nvd.nist.gov/vuln/detail/CVE-2026-112259) | Medium | 5.5 | A flaw was found in GIMP. Importing a crafted SBZ palette without a color-model attribute can cause a NULL pointer dere… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
