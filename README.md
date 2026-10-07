# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-07 02:18 UTC

New CVEs published between 2026-10-07 01:18 UTC and 2026-10-07 02:18 UTC.

[Full CSV](data/new-cves-2026-10-07T02-18-42-141374Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-10-07 02:16:56 | [CVE-2026-102478](https://nvd.nist.gov/vuln/detail/CVE-2026-102478) | High | 8.7 | In affected versions of Octopus Server, an authenticated user with permission to modify roles could bypass the protecti… |
| 2026-10-07 02:16:57 | [CVE-2026-105324](https://nvd.nist.gov/vuln/detail/CVE-2026-105324) | Critical | 9.2 | An HTTP header injection vulnerability in start-page-loader.cgi of ADM allows an unauthenticated remote attacker to rea… |
| 2026-10-07 02:16:57 | [CVE-2026-106471](https://nvd.nist.gov/vuln/detail/CVE-2026-106471) | High | 8.1 | A flaw was found in Candlepin. The central authorization filter incorrectly grants access when any one of multiple @Ver… |
| 2026-10-07 02:16:57 | [CVE-2026-16528](https://nvd.nist.gov/vuln/detail/CVE-2026-16528) | High | 8.4 | Insertion of Sensitive Information into Log File in certain ASUS router models allows a remote authenticated attacker t… |
| 2026-10-07 02:16:57 | [CVE-2026-19386](https://nvd.nist.gov/vuln/detail/CVE-2026-19386) | Critical | 9.3 | A stack-based buffer overflow in the ASUS router modules allows an authenticated nearby user to execute arbitrary code… |
| 2026-10-07 02:16:58 | [CVE-2026-19396](https://nvd.nist.gov/vuln/detail/CVE-2026-19396) | High | 7.7 | A predictable seed in the pseudo-random number generator (PRNG) in the IFTTT pairing token generation of the ASUS RT-BE… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
