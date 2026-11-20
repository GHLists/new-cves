# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-11-20 23:18 UTC

New CVEs published between 2026-11-20 22:21 UTC and 2026-11-20 23:18 UTC.

[Full CSV](data/new-cves-2026-11-20T23-18-45-656242Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-11-20 23:16:57 | [CVE-2026-107942](https://nvd.nist.gov/vuln/detail/CVE-2026-107942) | Low | 3.1 | Improper Content Security Policy (CSP) nonce implementation in HCL BigFix MCM allows a remote attacker to reduce the ef… |
| 2026-11-20 23:16:57 | [CVE-2026-124213](https://nvd.nist.gov/vuln/detail/CVE-2026-124213) |  |  | Rejected reason: ** REJECT ** DO NOT USE THIS CANDIDATE NUMBER. ConsultIDs: CVE-2026-125822. Reason: This candidate is… |
| 2026-11-20 23:16:57 | [CVE-2026-134163](https://nvd.nist.gov/vuln/detail/CVE-2026-134163) | Medium | 6.9 | probe-image-size 7.4.0 contains a regular expression denial of service vulnerability in lib/common/svg_header.js that a… |
| 2026-11-20 23:16:58 | [CVE-2026-134164](https://nvd.nist.gov/vuln/detail/CVE-2026-134164) | High | 8.7 | probe-image-size before 7.5.0 contains an algorithmic-complexity denial of service vulnerability in lib/exif_utils.js t… |
| 2026-11-20 23:16:58 | [CVE-2026-134165](https://nvd.nist.gov/vuln/detail/CVE-2026-134165) | Medium | 6.9 | probe-image-size before 7.5.0 contains an unbounded memory allocation vulnerability in lib/parse_stream/avif.js that al… |
| 2026-11-20 23:16:58 | [CVE-2026-134166](https://nvd.nist.gov/vuln/detail/CVE-2026-134166) | Medium | 6.9 | probe-image-size before 7.5.0 contains an unbounded memory buffering vulnerability in parseExif in lib/parse_stream/web… |
| 2026-11-20 23:16:58 | [CVE-2026-134167](https://nvd.nist.gov/vuln/detail/CVE-2026-134167) | High | 8.7 | devpi-web before 5.2.0 contains an unauthenticated path traversal vulnerability in the +doc documentation route because… |
| 2026-11-20 23:16:58 | [CVE-2026-134168](https://nvd.nist.gov/vuln/detail/CVE-2026-134168) | Medium | 5.3 | devpi-server before 6.21.0 contains a path traversal vulnerability that allows authenticated users to write files outsi… |
| 2026-11-20 23:16:58 | [CVE-2026-134169](https://nvd.nist.gov/vuln/detail/CVE-2026-134169) | High | 8.7 | Qwik City before 1.20.3 (@builder.io/qwik-city) and @qwik.dev/router before 2.0.0-rc.4 contain an improperly controlled… |
| 2026-11-20 23:16:59 | [CVE-2026-134170](https://nvd.nist.gov/vuln/detail/CVE-2026-134170) | High | 8.2 | Cesanta Mongoose 7.22 before 7.24 with the built-in TLS stack contains an out-of-bounds read in mg_timegm() that allows… |
| 2026-11-20 23:16:59 | [CVE-2026-134171](https://nvd.nist.gov/vuln/detail/CVE-2026-134171) | Medium | 6.9 | Cesanta Mongoose 7.21 before 7.24 contains an out-of-bounds read vulnerability in rx_ip6() checksum validation that all… |
| 2026-11-20 23:16:59 | [CVE-2026-134172](https://nvd.nist.gov/vuln/detail/CVE-2026-134172) | High | 8.5 | audio-separator before 0.47.2 contains an insecure deserialization vulnerability that allows attackers to execute code… |
| 2026-11-20 23:16:59 | [CVE-2026-16132](https://nvd.nist.gov/vuln/detail/CVE-2026-16132) | Medium | 5.1 | A stored cross-site scripting (XSS) vulnerability exists in the Icon API: Menu submodule of the Drupal 7 Icon API modul… |
| 2026-11-20 23:16:59 | [CVE-2026-19030](https://nvd.nist.gov/vuln/detail/CVE-2026-19030) | Medium | 6.9 | Observable Discrepancy vulnerability in Drupal CAPTCHA for Drupal 7 allows unauthenticated attackers to test login cred… |
| 2026-11-20 23:16:59 | [CVE-2026-79790](https://nvd.nist.gov/vuln/detail/CVE-2026-79790) |  |  | Rejected reason: This CVE ID has been rejected or withdrawn by its CVE Numbering Authority. |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
