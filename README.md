# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-09-30 22:19 UTC

New CVEs published between 2026-09-30 21:20 UTC and 2026-09-30 22:19 UTC.

[Full CSV](data/new-cves-2026-09-30T22-19-13-053663Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-09-30 22:16:33 | [CVE-2026-101283](https://nvd.nist.gov/vuln/detail/CVE-2026-101283) | Critical | 9.2 | iperf3 3.20–3.21 (esnet/iperf) has a pre-auth heap buffer overflow in decrypt_rsa_message(): a 256-byte RSA buffer is B… |
| 2026-09-30 22:16:33 | [CVE-2026-103001](https://nvd.nist.gov/vuln/detail/CVE-2026-103001) | Medium | 6.5 | PyJWT is a Python implementation of JSON Web Token standards. From 2.11.0 through 2.13.0, PyJWT's PyJWT._merge_options(… |
| 2026-09-30 22:16:33 | [CVE-2026-47096](https://nvd.nist.gov/vuln/detail/CVE-2026-47096) | Medium | 5.3 | AJA HELO Plus firmware before 2.1.7 contains a stored cross-site scripting vulnerability that allows unauthenticated at… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
