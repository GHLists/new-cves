# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-11-05 08:18 UTC

New CVEs published between 2026-11-05 07:31 UTC and 2026-11-05 08:18 UTC.

[Full CSV](data/new-cves-2026-11-05T08-18-45-950159Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-11-05 08:17:01 | [CVE-2026-100109](https://nvd.nist.gov/vuln/detail/CVE-2026-100109) | Critical | 9.8 | The Security For WooCommerce WordPress plugin from 1.0.10 to 1.0.16 does not perform capability checks when creating us… |
| 2026-11-05 08:17:03 | [CVE-2026-107776](https://nvd.nist.gov/vuln/detail/CVE-2026-107776) | Low | 2.2 | The Dokan WordPress plugin before 5.3.3 does not reconcile the amount credited to a vendor's reverse-withdrawal ledger… |
| 2026-11-05 08:17:03 | [CVE-2026-109408](https://nvd.nist.gov/vuln/detail/CVE-2026-109408) | High | 7.4 | vault-java-driver, a Java client for HashiCorp Vault, silently disables TLS certificate and hostname verification in th… |
| 2026-11-05 08:17:03 | [CVE-2026-112072](https://nvd.nist.gov/vuln/detail/CVE-2026-112072) | Medium | 6.5 | vault-java-driver, a Java client for HashiCorp Vault, parses Vault's JSON responses with a vendored minimal-json parser… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
