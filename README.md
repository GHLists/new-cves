# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-11-18 08:19 UTC

New CVEs published between 2026-11-18 07:19 UTC and 2026-11-18 08:19 UTC.

[Full CSV](data/new-cves-2026-11-18T08-19-21-392974Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-11-18 08:17:18 | [CVE-2025-15716](https://nvd.nist.gov/vuln/detail/CVE-2025-15716) | High | 8.1 | An incorrect implementation of authentication algorithm vulnerability in the SSO API in Synology DiskStation Manager (D… |
| 2026-11-18 08:17:19 | [CVE-2025-2235](https://nvd.nist.gov/vuln/detail/CVE-2025-2235) | High | 8.8 | Improper Verification of Cryptographic Signature vulnerability in OpenText™ Connected MX allows Privilege Escalation. T… |
| 2026-11-18 08:17:19 | [CVE-2026-125820](https://nvd.nist.gov/vuln/detail/CVE-2026-125820) | High | 8.8 | Deserialization of Untrusted Data vulnerability in Rymera Web Co Product Feed PRO for WooCommerce woo-product-feed-pro… |
| 2026-11-18 08:17:19 | [CVE-2026-125829](https://nvd.nist.gov/vuln/detail/CVE-2026-125829) | High | 7.7 | Improper Limitation of a Pathname to a Restricted Directory ('Path Traversal') vulnerability in Rymera Web Co Product F… |
| 2026-11-18 08:17:19 | [CVE-2026-131959](https://nvd.nist.gov/vuln/detail/CVE-2026-131959) | High | 7.8 | GNU Emacs 31.1 contains a code injection vulnerability in its handling of directory-local variables. A crafted .dir-loc… |
| 2026-11-18 08:17:19 | [CVE-2026-1212](https://nvd.nist.gov/vuln/detail/CVE-2026-1212) | Medium | 5.4 | The BuddyPress plugin for WordPress is vulnerable to Insecure Direct Object Reference in all versions up to, and includ… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
