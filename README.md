# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-11-18 10:22 UTC

New CVEs published between 2026-11-18 09:19 UTC and 2026-11-18 10:22 UTC.

[Full CSV](data/new-cves-2026-11-18T10-22-16-785377Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-11-18 10:16:52 | [CVE-2026-110513](https://nvd.nist.gov/vuln/detail/CVE-2026-110513) |  |  | Insufficient Session Expiration vulnerability in the Apache Iggy server HTTP transport. A self-issued JSON Web Token (J… |
| 2026-11-18 10:16:53 | [CVE-2026-112213](https://nvd.nist.gov/vuln/detail/CVE-2026-112213) | Medium | 6.9 | Out-of-bounds read vulnerability in the pixReadMemJp2kCore() function in Leptonica, located in jp2kio.c. The function r… |
| 2026-11-18 10:16:53 | [CVE-2026-120557](https://nvd.nist.gov/vuln/detail/CVE-2026-120557) | Medium | 6.4 | The WP Delicious – Recipe Plugin for Food Bloggers (formerly Delicious Recipes) plugin for WordPress is vulnerable to S… |
| 2026-11-18 10:16:53 | [CVE-2026-120566](https://nvd.nist.gov/vuln/detail/CVE-2026-120566) | Medium | 6.4 | The WP Delicious – Recipe Plugin for Food Bloggers (formerly Delicious Recipes) plugin for WordPress is vulnerable to S… |
| 2026-11-18 10:16:53 | [CVE-2026-120672](https://nvd.nist.gov/vuln/detail/CVE-2026-120672) | Medium | 4.9 | The Meow Gallery plugin for WordPress is vulnerable to generic SQL Injection via the 'limit' parameter in all versions… |
| 2026-11-18 10:16:53 | [CVE-2026-123343](https://nvd.nist.gov/vuln/detail/CVE-2026-123343) | Medium | 6.5 | The BlockArt Blocks – Gutenberg Blocks, Page Builder Blocks ,WordPress Block Plugin, Sections & Template Library plugin… |
| 2026-11-18 10:16:53 | [CVE-2026-125012](https://nvd.nist.gov/vuln/detail/CVE-2026-125012) | Medium | 6.4 | The Flying Images: Optimize and Lazy Load Images for Faster Page Speed plugin for WordPress is vulnerable to Stored Cro… |
| 2026-11-18 10:16:54 | [CVE-2026-125058](https://nvd.nist.gov/vuln/detail/CVE-2026-125058) | Medium | 6.4 | The Image Source Control Lite – Show Image Credits and Captions plugin for WordPress is vulnerable to Stored Cross-Site… |
| 2026-11-18 10:16:54 | [CVE-2026-126708](https://nvd.nist.gov/vuln/detail/CVE-2026-126708) |  |  | In Eclipse Mosquitto versions 2.0.0 to 2.0.22 and 2.1.0 to 2.1.2, the return value of password hash functions for sha51… |
| 2026-11-18 10:16:54 | [CVE-2026-129509](https://nvd.nist.gov/vuln/detail/CVE-2026-129509) |  |  | In the Apache Airflow Microsoft Azure provider 10.2.0 through 15.3.0, `S3ToAzureBlobStorageOperator` turned off TLS cer… |
| 2026-11-18 10:16:54 | [CVE-2026-129705](https://nvd.nist.gov/vuln/detail/CVE-2026-129705) |  |  | In Eclipse Mosquitto versions 2.1.0 to 2.1.2, a broker with a listener that is configured to use the PROXY protocol v2… |
| 2026-11-18 10:16:54 | [CVE-2026-130491](https://nvd.nist.gov/vuln/detail/CVE-2026-130491) |  |  | In Eclipse versions 1.5-1.6.13, 2.0.0-2.0.22 and 2.1.0-2.1.2, the client library libmosquitto does not reject Will mess… |
| 2026-11-18 10:16:55 | [CVE-2026-19707](https://nvd.nist.gov/vuln/detail/CVE-2026-19707) | Critical | 9.5 | A bug in the Airlock Gateway (8.5.2 and earlier, and 8.6.0) allows attacker-controlled HTML in a backend response to ex… |
| 2026-11-18 10:16:55 | [CVE-2026-1214](https://nvd.nist.gov/vuln/detail/CVE-2026-1214) | Medium | 5.3 | The BuddyPress plugin for WordPress is vulnerable to Sensitive Information Exposure in all versions up to, and includin… |
| 2026-11-18 10:16:55 | [CVE-2026-58320](https://nvd.nist.gov/vuln/detail/CVE-2026-58320) |  |  | Missing Authorization vulnerability in the Apache Iggy server. The system snapshot command (GetSnapshot on the binary t… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
