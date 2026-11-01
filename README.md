# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-11-01 13:18 UTC

New CVEs published between 2026-11-01 12:19 UTC and 2026-11-01 13:18 UTC.

[Full CSV](data/new-cves-2026-11-01T13-18-37-777081Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-11-01 13:18:00 | [CVE-2026-120227](https://nvd.nist.gov/vuln/detail/CVE-2026-120227) | High | 8.6 | A vulnerability was detected in WAVLINK WN701AE M01AE_V260105. This affects the function del_staticrule of the file sta… |
| 2026-11-01 13:18:01 | [CVE-2026-120306](https://nvd.nist.gov/vuln/detail/CVE-2026-120306) | Critical | 9.9 | Beta9 turns each shell command in a tenant image definition into a Dockerfile RUN line and executes it with Buildah on… |
| 2026-11-01 13:18:01 | [CVE-2026-120307](https://nvd.nist.gov/vuln/detail/CVE-2026-120307) | Critical | 9.9 | The Beta9 worker serves the sandbox file API from outside the container. getHostPathFromContainerPath turns the tenant'… |
| 2026-11-01 13:18:01 | [CVE-2026-120308](https://nvd.nist.gov/vuln/detail/CVE-2026-120308) | Critical | 9.9 | A Beta9 tenant can attach a volume when deploying a function, endpoint, or task queue. The gateway builds the host path… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
