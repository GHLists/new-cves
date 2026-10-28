# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-28 05:20 UTC

New CVEs published between 2026-10-28 04:18 UTC and 2026-10-28 05:20 UTC.

[Full CSV](data/new-cves-2026-10-28T05-20-03-415305Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-10-28 05:16:59 | [CVE-2026-104383](https://nvd.nist.gov/vuln/detail/CVE-2026-104383) | Critical | 9.4 | Improper Control of Generation of Code in Pigeon MFA service in EagleCloud Aquila versions through 2.6.7.2 on on-premis… |
| 2026-10-28 05:16:59 | [CVE-2026-104384](https://nvd.nist.gov/vuln/detail/CVE-2026-104384) | High | 8.7 | Insufficiently Protected Credentials in tunnel gateway and provisioning interfaces in EagleCloud Aquila versions throug… |
| 2026-10-28 05:16:59 | [CVE-2026-115522](https://nvd.nist.gov/vuln/detail/CVE-2026-115522) | Medium | 5.3 | Exposure of Resource to Wrong Sphere (CWE-668) in FileArtifactService in Google Agent Development Kit (ADK) for Python… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
