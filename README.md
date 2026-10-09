# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-09 22:18 UTC

New CVEs published between 2026-10-09 21:19 UTC and 2026-10-09 22:18 UTC.

[Full CSV](data/new-cves-2026-10-09T22-18-35-974204Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-10-09 22:16:59 | [CVE-2026-108267](https://nvd.nist.gov/vuln/detail/CVE-2026-108267) | Critical | 9.1 | Privasys Go is a maintained fork of the Go programming language that adds RA-TLS support to crypto/tls. Prior to privas… |
| 2026-10-09 22:16:59 | [CVE-2026-108268](https://nvd.nist.gov/vuln/detail/CVE-2026-108268) | Critical | 9.1 | Enclave OS Virtual runs container workloads inside confidential virtual machines with end-to-end attestation. Prior to… |
| 2026-10-09 22:16:59 | [CVE-2026-108269](https://nvd.nist.gov/vuln/detail/CVE-2026-108269) | Critical | 9.1 | Remote Attestation TLS Clients provides multi-language utilities for verifying attested TLS connections. Prior to 0.5.0… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
