# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-11-27 11:19 UTC

New CVEs published between 2026-11-27 10:20 UTC and 2026-11-27 11:19 UTC.

[Full CSV](data/new-cves-2026-11-27T11-19-08-725167Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-11-27 11:17:04 | [CVE-2025-41680](https://nvd.nist.gov/vuln/detail/CVE-2025-41680) |  |  | Rejected reason: This CVE ID has been rejected or withdrawn by its CVE Numbering Authority. |
| 2026-11-27 11:17:05 | [CVE-2026-127118](https://nvd.nist.gov/vuln/detail/CVE-2026-127118) | High | 7.1 | RCDevs OpenOTP SMS integration connector does not validate the TLS certificate of the remote endpoint, and transmitted… |
| 2026-11-27 11:17:06 | [CVE-2026-137742](https://nvd.nist.gov/vuln/detail/CVE-2026-137742) | Medium | 5.5 | A security flaw has been discovered in Free5GC up to 4.2.3. Affected is the function handleAssociationSetupRequest of t… |
| 2026-11-27 11:17:06 | [CVE-2026-137826](https://nvd.nist.gov/vuln/detail/CVE-2026-137826) | Medium | 6.9 | Lookyloo is a web-based malware analysis and sandboxing platform. The pull-from-remote-instance feature allows a user t… |
| 2026-11-27 11:17:06 | [CVE-2026-137888](https://nvd.nist.gov/vuln/detail/CVE-2026-137888) | Medium | 6.3 | Flowintel contains a Server-Side Request Forgery (SSRF) vulnerability in its HedgeDoc case-notes integration. When a us… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
