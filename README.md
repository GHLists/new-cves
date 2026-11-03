# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-11-03 22:21 UTC

New CVEs published between 2026-11-03 21:18 UTC and 2026-11-03 22:21 UTC.

[Full CSV](data/new-cves-2026-11-03T22-21-09-837892Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-11-03 22:17:44 | [CVE-2026-112354](https://nvd.nist.gov/vuln/detail/CVE-2026-112354) | Critical | 9.3 | Etrel INCH AC charging station management web interface prior to firmware versions 7.1.2 and 8.0.1 contains a hard-code… |
| 2026-11-03 22:19:17 | [CVE-2026-115541](https://nvd.nist.gov/vuln/detail/CVE-2026-115541) | High | 7.2 | HumHub Community Edition 1.19.0 contains a stored cross-site scripting vulnerability in the friendship confirmation dia… |
| 2026-11-03 22:19:29 | [CVE-2026-118865](https://nvd.nist.gov/vuln/detail/CVE-2026-118865) | High | 7.3 | An authenticated OS command injection vulnerability exists in the Offline Download component (USB storage allocation) o… |
| 2026-11-03 22:19:29 | [CVE-2026-119084](https://nvd.nist.gov/vuln/detail/CVE-2026-119084) | Critical | 9.2 | Unsafe reflection in the connection parameter and credentials profile handling of Amazon Redshift JDBC Driver before 2.… |
| 2026-11-03 22:19:31 | [CVE-2026-120930](https://nvd.nist.gov/vuln/detail/CVE-2026-120930) |  |  | Incorrect authorization in Blink in Google Chrome prior to 156.0.8078.47 allowed a remote attacker to bypass web origin… |
| 2026-11-03 22:19:31 | [CVE-2026-120931](https://nvd.nist.gov/vuln/detail/CVE-2026-120931) | Critical | 9.6 | Out of bounds write in WebGL in Google Chrome on on Android prior to 156.0.8078.47 allowed a remote attacker to execute… |
| 2026-11-03 22:19:46 | [CVE-2026-121522](https://nvd.nist.gov/vuln/detail/CVE-2026-121522) | Medium | 6.7 | In BuildKit versions v0.26.0 through v0.34.1, a specific build definition that resolves metadata for the same Git sourc… |
| 2026-11-03 22:19:46 | [CVE-2026-121524](https://nvd.nist.gov/vuln/detail/CVE-2026-121524) | Medium | 5.5 | A flaw has been found in sumiie24 School-Management-System up to d946d649c7c95e101fc5679ecd91999533bb10d7. Affected by… |
| 2026-11-03 22:19:46 | [CVE-2026-121531](https://nvd.nist.gov/vuln/detail/CVE-2026-121531) | Low | 2.1 | A vulnerability has been found in Umami 3.3.x/3.4.0/3.4.1. This affects an unknown part of the file src/app/api/auth/lo… |
| 2026-11-03 22:19:46 | [CVE-2026-121541](https://nvd.nist.gov/vuln/detail/CVE-2026-121541) | Medium | 5.6 | In Docker Buildx versions v0.19.0 through v0.38.0, an untrusted Bake definition that builds multiple targets together m… |
| 2026-11-03 22:19:46 | [CVE-2026-121542](https://nvd.nist.gov/vuln/detail/CVE-2026-121542) | Low | 1.8 | In Docker Buildx versions v0.19.0 through v0.38.0, an untrusted Bake definition may expose files accessible to the Buil… |
| 2026-11-03 22:19:46 | [CVE-2026-121614](https://nvd.nist.gov/vuln/detail/CVE-2026-121614) | High | 7.1 | Docker Sandboxes versions 0.31.0 before 0.50.0 do not neutralize repository-controlled Git configuration when running c… |
| 2026-11-03 22:19:47 | [CVE-2026-22058](https://nvd.nist.gov/vuln/detail/CVE-2026-22058) | Critical | 9.1 | StorageGRID (formerly StorageGRID Webscale) versions 11.3 and higher allow an attacker with product-specific knowledge… |
| 2026-11-03 22:19:47 | [CVE-2026-22060](https://nvd.nist.gov/vuln/detail/CVE-2026-22060) | Medium | 6.9 | All versions of StorageGRID (formerly StorageGRID Webscale) in default & common configurations allow an unauthenticated… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
