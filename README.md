# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-27 06:18 UTC

New CVEs published between 2026-10-27 05:19 UTC and 2026-10-27 06:18 UTC.

[Full CSV](data/new-cves-2026-10-27T06-18-39-133827Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-10-27 06:17:23 | [CVE-2026-103312](https://nvd.nist.gov/vuln/detail/CVE-2026-103312) |  |  | The Payment Integration Wompi WordPress plugin through 4.0.1 does not verify the authenticity of incoming payment notif… |
| 2026-10-27 06:17:23 | [CVE-2026-103332](https://nvd.nist.gov/vuln/detail/CVE-2026-103332) |  |  | The Payex Payment Gateway for Woocommerce WordPress plugin through 1.2.10 does not properly verify the authenticity of… |
| 2026-10-27 06:17:23 | [CVE-2026-111820](https://nvd.nist.gov/vuln/detail/CVE-2026-111820) | High | 7.2 | The Analytics Insights – Google Analytics Dashboard for WordPress plugin for WordPress is vulnerable to Stored Cross-Si… |
| 2026-10-27 06:17:24 | [CVE-2026-117468](https://nvd.nist.gov/vuln/detail/CVE-2026-117468) | Medium | 6.5 | Psono Server versions 5.3.5 through 7.2.3 used a permission class that did not enforce token write scope when claiming… |
| 2026-10-27 06:17:24 | [CVE-2026-117469](https://nvd.nist.gov/vuln/detail/CVE-2026-117469) | Medium | 5.4 | Psono Server (CE & EE) versions 1.0.0 through 7.2.3 did not enforce the direction of file-transfer credentials on file-… |
| 2026-10-27 06:17:24 | [CVE-2026-117470](https://nvd.nist.gov/vuln/detail/CVE-2026-117470) | Medium | 6.5 | Psono Server CE & EE versions 3.1.0 through 7.2.3 did not consume a stored WebAuthn challenge after assertion verificat… |
| 2026-10-27 06:17:25 | [CVE-2026-117471](https://nvd.nist.gov/vuln/detail/CVE-2026-117471) | Medium | 5.4 | Psono Server CE && EE versions 0.1.0 through 7.2.3 accepted a user-controlled host when configuring a personal Duo devi… |
| 2026-10-27 06:17:25 | [CVE-2026-117472](https://nvd.nist.gov/vuln/detail/CVE-2026-117472) | Medium | 4.3 | Psono Server CE && EE versions 4.0.33 through 7.2.3 compared the request path for the bulk-secret-read endpoint with a… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
