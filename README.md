# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-11-12 07:21 UTC

New CVEs published between 2026-11-12 06:20 UTC and 2026-11-12 07:21 UTC.

[Full CSV](data/new-cves-2026-11-12T07-21-24-07057Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-11-12 07:16:45 | [CVE-2026-113408](https://nvd.nist.gov/vuln/detail/CVE-2026-113408) | Low | 3.3 | Path traversal in Git allows writing to arbitrary file via cloning and committing to bad repository |
| 2026-11-12 07:16:46 | [CVE-2026-12507](https://nvd.nist.gov/vuln/detail/CVE-2026-12507) | Critical | 9.1 | Zohocorp ManageEngine AssetExplorer versions below 7860, ServiceDesk Plus versions below 15290, ServiceDesk Plus MSP ve… |
| 2026-11-12 07:16:47 | [CVE-2026-12591](https://nvd.nist.gov/vuln/detail/CVE-2026-12591) | Critical | 9.9 | Zohocorp ManageEngine M365 Manager Plus versions below 4818 is affected by an authenticated technician may exploit insu… |
| 2026-11-12 07:16:47 | [CVE-2026-87772](https://nvd.nist.gov/vuln/detail/CVE-2026-87772) | High | 7.8 | Incorrect Authorization vulnerability in TÜBİTAK BİLGEM Software Technologies Research Institute Pardus About allows Pr… |
| 2026-11-12 07:16:47 | [CVE-2026-8331](https://nvd.nist.gov/vuln/detail/CVE-2026-8331) | High | 8.8 | An unrestricted upload of files with dangerous type vulnerability in the Microchip TimePictra platform allows functiona… |
| 2026-11-12 07:16:48 | [CVE-2026-8332](https://nvd.nist.gov/vuln/detail/CVE-2026-8332) | High | 8.8 | A hard-coded root password in Microchip TimePictra platform installation files could allow an attacker with access to t… |
| 2026-11-12 07:16:49 | [CVE-2026-8333](https://nvd.nist.gov/vuln/detail/CVE-2026-8333) | Critical | 9.4 | A stored cross-site scripting vulnerability in Microchip the TimePictra platform could allow an authenticated, low-priv… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
