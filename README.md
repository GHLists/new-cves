# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-09-27 09:19 UTC

New CVEs published between 2026-09-27 08:19 UTC and 2026-09-27 09:19 UTC.

[Full CSV](data/new-cves-2026-09-27T09-19-15-48062Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-09-27 09:16:36 | [CVE-2026-94418](https://nvd.nist.gov/vuln/detail/CVE-2026-94418) | Low | 2.3 | Under WOLFSSL_SMALL_CERT_VERIFY, ProcessPeerCertParse() runs the certificate signature check separately from the parse… |
| 2026-09-27 09:16:36 | [CVE-2026-94419](https://nvd.nist.gov/vuln/detail/CVE-2026-94419) | Low | 2.3 | Without NO_SESSION_CACHE_REF, wolfSSL_get_session() does not return a session object but a ClientSession reference of t… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
