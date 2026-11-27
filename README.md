# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-11-27 08:21 UTC

New CVEs published between 2026-11-27 07:21 UTC and 2026-11-27 08:21 UTC.

[Full CSV](data/new-cves-2026-11-27T08-21-07-636025Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-11-27 08:16:38 | [CVE-2025-41671](https://nvd.nist.gov/vuln/detail/CVE-2025-41671) |  |  | Rejected reason: This CVE ID has been rejected or withdrawn by its CVE Numbering Authority. |
| 2026-11-27 08:16:38 | [CVE-2025-25272](https://nvd.nist.gov/vuln/detail/CVE-2025-25272) |  |  | Rejected reason: This CVE ID has been rejected or withdrawn by its CVE Numbering Authority. |
| 2026-11-27 08:16:38 | [CVE-2026-110928](https://nvd.nist.gov/vuln/detail/CVE-2026-110928) |  |  | Rejected reason: CVE-2026-110928 has been marked as a duplicate of CVE-2026-106586. |
| 2026-11-27 08:16:38 | [CVE-2026-115834](https://nvd.nist.gov/vuln/detail/CVE-2026-115834) | Low | 3.1 | A flaw was found in sequoia-openpgp. The Display and Debug implementations for UserID and NotationData passed attacker-… |
| 2026-11-27 08:16:39 | [CVE-2026-80243](https://nvd.nist.gov/vuln/detail/CVE-2026-80243) | Medium | 6.3 | Dell Secure Connect Gateway - Virtual Edition, versions prior to 5.36.00.16, contains a Buffer Copy without Checking Si… |
| 2026-11-27 08:16:39 | [CVE-2026-95622](https://nvd.nist.gov/vuln/detail/CVE-2026-95622) | Medium | 6.5 | A flaw was found in ModemManager. When parsing a Cell Broadcast Message, some 3GPP data-coding-scheme values (8-bit and… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
