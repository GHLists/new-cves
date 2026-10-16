# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-16 23:19 UTC

New CVEs published between 2026-10-16 22:18 UTC and 2026-10-16 23:19 UTC.

[Full CSV](data/new-cves-2026-10-16T23-19-37-003051Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-10-16 22:18:58 | [CVE-2026-96626](https://nvd.nist.gov/vuln/detail/CVE-2026-96626) | High | 8.5 | Arcane is an interface for managing Docker containers, images, networks, and volumes. Prior to 2.5.0, UpdateRegistry an… |
| 2026-10-16 22:18:58 | [CVE-2026-96627](https://nvd.nist.gov/vuln/detail/CVE-2026-96627) | High | 8.8 | Arcane is an interface for managing Docker containers, images, networks, and volumes. Prior to 2.6.0, UpdateUser in bac… |
| 2026-10-16 22:18:58 | [CVE-2026-96628](https://nvd.nist.gov/vuln/detail/CVE-2026-96628) | Medium | 4.3 | Arcane is an interface for managing Docker containers, images, networks, and volumes. Prior to 2.11.0, AuthMiddleware.m… |
| 2026-10-16 23:16:58 | [CVE-2026-106549](https://nvd.nist.gov/vuln/detail/CVE-2026-106549) |  |  | Rejected reason: This CVE ID has been rejected or withdrawn by its CVE Numbering Authority. |
| 2026-10-16 23:16:58 | [CVE-2026-107346](https://nvd.nist.gov/vuln/detail/CVE-2026-107346) |  |  | Rejected reason: This CVE ID has been rejected or withdrawn by its CVE Numbering Authority. |
| 2026-10-16 23:17:00 | [CVE-2026-110752](https://nvd.nist.gov/vuln/detail/CVE-2026-110752) |  |  | Text::CSV_XS versions before 1.65 for Perl allow memory exhaustion by allocating one entry per index of an RFC 7111 sel… |
| 2026-10-16 23:17:00 | [CVE-2026-110753](https://nvd.nist.gov/vuln/detail/CVE-2026-110753) |  |  | Text::CSV_XS versions from 1.46 before 1.65 for Perl have a use-after-free of bind_columns variables when skip_empty_ro… |
| 2026-10-16 23:17:00 | [CVE-2026-110754](https://nvd.nist.gov/vuln/detail/CVE-2026-110754) |  |  | Text::CSV_XS versions before 1.65 for Perl leak the parsed fields of a record that fails to parse in getline. getline c… |
| 2026-10-16 23:17:00 | [CVE-2026-110755](https://nvd.nist.gov/vuln/detail/CVE-2026-110755) |  |  | Text::CSV_XS versions before 1.65 for Perl allow quadratic CPU use by copying the unparsed remainder per record of CR-o… |
| 2026-10-16 23:17:00 | [CVE-2026-110756](https://nvd.nist.gov/vuln/detail/CVE-2026-110756) |  |  | Text::CSV_XS versions before 1.65 for Perl drop the end of a record and its line ending when a UTF-8 flagged field prec… |
| 2026-10-16 23:17:00 | [CVE-2026-110757](https://nvd.nist.gov/vuln/detail/CVE-2026-110757) |  |  | Text::CSV_XS versions before 1.65 for Perl allow record splitting by writing strings used as numbers without quotes in… |
| 2026-10-16 23:17:01 | [CVE-2026-110758](https://nvd.nist.gov/vuln/detail/CVE-2026-110758) |  |  | Text::CSV_XS versions before 1.65 for Perl read before the start of an all-blank field under allow_whitespace in strip_… |
| 2026-10-16 23:17:01 | [CVE-2026-110759](https://nvd.nist.gov/vuln/detail/CVE-2026-110759) |  |  | Text::CSV_XS versions before 1.65 for Perl return a 0xFF byte that is not in the input for an empty last field followed… |
| 2026-10-16 23:17:01 | [CVE-2026-111802](https://nvd.nist.gov/vuln/detail/CVE-2026-111802) | Medium | 6.6 | A flaw was found in Nautilus. When a removable drive or disk image is unmounted or ejected, Nautilus prompts the user t… |
| 2026-10-16 23:17:01 | [CVE-2026-17591](https://nvd.nist.gov/vuln/detail/CVE-2026-17591) | Low | 3.6 | A flaw was found in libarchive. An attacker can cause a Denial of Service (DoS) or potential information disclosure due… |
| 2026-10-16 23:17:02 | [CVE-2026-89085](https://nvd.nist.gov/vuln/detail/CVE-2026-89085) | Medium | 6.6 | A flaw was found in parted. A heap-based buffer overflow can occur when processing a specially crafted FAT32 filesystem… |
| 2026-10-16 23:17:02 | [CVE-2026-89088](https://nvd.nist.gov/vuln/detail/CVE-2026-89088) | Medium | 5.5 | A flaw was found in parted. A heap-based buffer overflow exists in libparted's file system resizing logic when handling… |
| 2026-10-16 23:17:02 | [CVE-2026-89096](https://nvd.nist.gov/vuln/detail/CVE-2026-89096) | Medium | 5.9 | A flaw was found in nfs-utils. An unauthenticated remote attacker can trigger a Denial of Service (DoS) by sending repe… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
