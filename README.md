# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-11-21 00:20 UTC

New CVEs published between 2026-11-20 23:18 UTC and 2026-11-21 00:20 UTC.

[Full CSV](data/new-cves-2026-11-21T00-20-53-36734Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-11-21 00:17:43 | [CVE-2026-112465](https://nvd.nist.gov/vuln/detail/CVE-2026-112465) |  |  | An out-of-bounds read was addressed with improved bounds checking. This issue is fixed in iOS 27.2 and iPadOS 27.2, mac… |
| 2026-11-21 00:17:44 | [CVE-2026-112603](https://nvd.nist.gov/vuln/detail/CVE-2026-112603) |  |  | A logic issue was addressed with improved checks. This issue is fixed in Xcode 27.2. An app may be able to gain root pr… |
| 2026-11-21 00:17:44 | [CVE-2026-112662](https://nvd.nist.gov/vuln/detail/CVE-2026-112662) |  |  | A race condition was addressed with additional validation. This issue is fixed in iOS 27.2 and iPadOS 27.2. An app may… |
| 2026-11-21 00:17:44 | [CVE-2026-113953](https://nvd.nist.gov/vuln/detail/CVE-2026-113953) |  |  | An integer overflow was addressed with improved input validation. This issue is fixed in iOS 27.2 and iPadOS 27.2, macO… |
| 2026-11-21 00:17:44 | [CVE-2026-113954](https://nvd.nist.gov/vuln/detail/CVE-2026-113954) |  |  | A use-after-free issue was addressed with improved memory management. This issue is fixed in iOS 27.2 and iPadOS 27.2.… |
| 2026-11-21 00:17:44 | [CVE-2026-113955](https://nvd.nist.gov/vuln/detail/CVE-2026-113955) |  |  | A cross-origin issue was addressed with improved tracking of security origins. This issue is fixed in iOS 26.7.2 and iP… |
| 2026-11-21 00:17:44 | [CVE-2026-114021](https://nvd.nist.gov/vuln/detail/CVE-2026-114021) |  |  | An out-of-bounds write issue was addressed with improved bounds checking. This issue is fixed in macOS Golden Gate 27.2… |
| 2026-11-21 00:17:45 | [CVE-2026-114022](https://nvd.nist.gov/vuln/detail/CVE-2026-114022) |  |  | An out-of-bounds write issue was addressed with improved bounds checking. This issue is fixed in macOS Sequoia 15.8.2,… |
| 2026-11-21 00:17:45 | [CVE-2026-114023](https://nvd.nist.gov/vuln/detail/CVE-2026-114023) |  |  | A path handling issue was addressed with improved validation. This issue is fixed in macOS Golden Gate 27.2, macOS Sequ… |
| 2026-11-21 00:17:45 | [CVE-2026-114024](https://nvd.nist.gov/vuln/detail/CVE-2026-114024) |  |  | This issue was addressed with improved checks. This issue is fixed in iOS 27.2 and iPadOS 27.2, macOS Golden Gate 27.2,… |
| 2026-11-21 00:17:45 | [CVE-2026-114025](https://nvd.nist.gov/vuln/detail/CVE-2026-114025) |  |  | An out-of-bounds write was addressed with improved input validation. This issue is fixed in iOS 26.7.2 and iPadOS 26.7.… |
| 2026-11-21 00:17:45 | [CVE-2026-114026](https://nvd.nist.gov/vuln/detail/CVE-2026-114026) |  |  | An out-of-bounds read was addressed with improved bounds checking. This issue is fixed in iOS 27.2 and iPadOS 27.2, mac… |
| 2026-11-21 00:17:45 | [CVE-2026-132475](https://nvd.nist.gov/vuln/detail/CVE-2026-132475) |  |  | An out-of-bounds write issue was addressed with improved bounds checking. This issue is fixed in macOS Golden Gate 27.2… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
