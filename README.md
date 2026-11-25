# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-11-25 01:18 UTC

New CVEs published between 2026-11-25 00:18 UTC and 2026-11-25 01:18 UTC.

[Full CSV](data/new-cves-2026-11-25T01-18-52-171969Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-11-25 01:16:48 | [CVE-2026-122093](https://nvd.nist.gov/vuln/detail/CVE-2026-122093) |  |  | Strong::Random versions through 0.96 for Perl allow every later rand output to be predicted from three earlier ones. Th… |
| 2026-11-25 01:16:48 | [CVE-2026-132255](https://nvd.nist.gov/vuln/detail/CVE-2026-132255) | Medium | 6.5 | AutoGPT is a workflow automation platform for creating, deploying, and managing continuous artificial intelligence agen… |
| 2026-11-25 01:16:48 | [CVE-2026-132256](https://nvd.nist.gov/vuln/detail/CVE-2026-132256) | Medium | 6.5 | AutoGPT is a workflow automation platform for creating, deploying, and managing continuous artificial intelligence agen… |
| 2026-11-25 01:16:48 | [CVE-2026-132260](https://nvd.nist.gov/vuln/detail/CVE-2026-132260) | Medium | 6.5 | AutoGPT is a workflow automation platform for creating, deploying, and managing continuous artificial intelligence agen… |
| 2026-11-25 01:16:48 | [CVE-2026-132271](https://nvd.nist.gov/vuln/detail/CVE-2026-132271) | Medium | 6.5 | AutoGPT is a workflow automation platform for creating, deploying, and managing continuous artificial intelligence agen… |
| 2026-11-25 01:16:48 | [CVE-2026-133461](https://nvd.nist.gov/vuln/detail/CVE-2026-133461) | Medium | 5.1 | AutoGPT is a workflow automation platform for creating, deploying, and managing continuous artificial intelligence agen… |
| 2026-11-25 01:16:49 | [CVE-2026-134875](https://nvd.nist.gov/vuln/detail/CVE-2026-134875) | Medium | 4.9 | An unencrypted RSA private key for a default HTTPS certificate is included in GeoVision GV-EBD4700 firmware V1.11 (A02-… |
| 2026-11-25 01:16:49 | [CVE-2026-136146](https://nvd.nist.gov/vuln/detail/CVE-2026-136146) | Low | 1.9 | A security flaw has been discovered in vanna-ai vanna 2.0.0/2.0.1/2.0.2. Affected by this vulnerability is the function… |
| 2026-11-25 01:16:49 | [CVE-2026-136147](https://nvd.nist.gov/vuln/detail/CVE-2026-136147) | Low | 2.1 | A weakness has been identified in DWS Antik Browser 1.17.0. Affected by this issue is some unknown functionality of the… |
| 2026-11-25 01:16:49 | [CVE-2026-136444](https://nvd.nist.gov/vuln/detail/CVE-2026-136444) | Low | 2.1 | A vulnerability was detected in JaguarJack catch-admin up to 5.4.1. The affected element is the function Store/Update o… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
