# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-24 14:18 UTC

New CVEs published between 2026-10-24 13:20 UTC and 2026-10-24 14:18 UTC.

[Full CSV](data/new-cves-2026-10-24T14-18-40-994426Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-10-24 14:16:38 | [CVE-2026-114191](https://nvd.nist.gov/vuln/detail/CVE-2026-114191) | High | 7.5 | Missing Authorization vulnerability in Knit Pay UPI QR Code Payment Gateway for WooCommerce upi-qr-code-payment-for-woo… |
| 2026-10-24 14:16:39 | [CVE-2026-114192](https://nvd.nist.gov/vuln/detail/CVE-2026-114192) | Medium | 6.5 | Missing Authorization vulnerability in Magepeople inc. WpEvently mage-eventpress allows Exploiting Incorrectly Configur… |
| 2026-10-24 14:16:39 | [CVE-2026-114629](https://nvd.nist.gov/vuln/detail/CVE-2026-114629) |  |  | Web::Simple versions before 0.035 for Perl allocate a buffer sized by the Content-Length header for urlencoded body par… |
| 2026-10-24 14:16:39 | [CVE-2026-114704](https://nvd.nist.gov/vuln/detail/CVE-2026-114704) | High | 7.2 | Deserialization of Untrusted Data vulnerability in Christoph Vielgrader Relevanssi relevanssi allows Object Injection.T… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
