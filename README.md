# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-11-04 14:18 UTC

New CVEs published between 2026-11-04 13:18 UTC and 2026-11-04 14:18 UTC.

[Full CSV](data/new-cves-2026-11-04T14-18-24-572409Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-11-04 14:17:29 | [CVE-2026-118391](https://nvd.nist.gov/vuln/detail/CVE-2026-118391) | High | 8.9 | Allocation of Resources Without Limits or Throttling vulnerability in elixir-ecto ecto allows an unauthenticated remote… |
| 2026-11-04 14:17:30 | [CVE-2026-119745](https://nvd.nist.gov/vuln/detail/CVE-2026-119745) | Medium | 5.3 | MultiVendorX plugin for WordPress before 5.0.21 contains a missing authorization vulnerability that allows any authenti… |
| 2026-11-04 14:17:39 | [CVE-2026-121993](https://nvd.nist.gov/vuln/detail/CVE-2026-121993) | Medium | 5.3 | wePOS (Point Of Sale for WooCommerce) before 2.0.3 contains a missing authorization vulnerability in the wepos/v1/payme… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
