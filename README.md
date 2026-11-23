# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-11-23 11:18 UTC

New CVEs published between 2026-11-23 10:21 UTC and 2026-11-23 11:18 UTC.

[Full CSV](data/new-cves-2026-11-23T11-18-38-801957Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-11-23 11:16:58 | [CVE-2026-118889](https://nvd.nist.gov/vuln/detail/CVE-2026-118889) | Medium | 4.2 | Z80 Ultra product has an improper access control vulnerability in the UI module. Successful exploitation of this vulner… |
| 2026-11-23 11:16:58 | [CVE-2026-123886](https://nvd.nist.gov/vuln/detail/CVE-2026-123886) | High | 8.8 | Spring Data Elasticsearch replaces positional placeholders in string-based @Query methods with the method arguments bef… |
| 2026-11-23 11:16:58 | [CVE-2026-124559](https://nvd.nist.gov/vuln/detail/CVE-2026-124559) | Medium | 6.5 | A flaw was found in QEMU's NBD server. A remote attacker can crash a multi-export NBD server process by exploiting stal… |
| 2026-11-23 11:16:58 | [CVE-2026-125683](https://nvd.nist.gov/vuln/detail/CVE-2026-125683) | Medium | 6.5 | A flaw was found in QEMU's NBD server. A remote attacker can crash qemu-nbd, qemu-storage-daemon, or qemu-system by sen… |
| 2026-11-23 11:16:58 | [CVE-2026-126657](https://nvd.nist.gov/vuln/detail/CVE-2026-126657) | Medium | 6.5 | A flaw was found in QEMU's NBD block driver. A malicious NBD server can send an incomplete structured read reply marked… |
| 2026-11-23 11:16:59 | [CVE-2026-133646](https://nvd.nist.gov/vuln/detail/CVE-2026-133646) | High | 8.7 | Synchronet BBS, in versions 3.20b to 3.21e, contains an out-of-bounds write vulnerability in the answer() function when… |
| 2026-11-23 11:16:59 | [CVE-2026-134886](https://nvd.nist.gov/vuln/detail/CVE-2026-134886) | Medium | 6.9 | A vulnerability has been found in osCommerce up to 4.14.63493. This affects the function actionCached of the file lib/f… |
| 2026-11-23 11:16:59 | [CVE-2026-134887](https://nvd.nist.gov/vuln/detail/CVE-2026-134887) | Medium | 6.9 | A vulnerability was found in osCommerce 4.14.63493. This impacts the function get_address_book_data of the file lib/com… |
| 2026-11-23 11:16:59 | [CVE-2026-134888](https://nvd.nist.gov/vuln/detail/CVE-2026-134888) | Medium | 5.3 | A vulnerability was determined in osCommerce 4.14.63493. Affected is the function CheckoutController::actionRestart of… |
| 2026-11-23 11:17:00 | [CVE-2026-134889](https://nvd.nist.gov/vuln/detail/CVE-2026-134889) | Medium | 5.3 | A vulnerability was identified in osCommerce 4.14.63493. Affected by this vulnerability is the function updateAddress o… |
| 2026-11-23 11:17:00 | [CVE-2026-135055](https://nvd.nist.gov/vuln/detail/CVE-2026-135055) | High | 8.0 | A flaw was found in the GLib DMA-BUF path of WebKitGTK. The UIProcess trusted fds.size() as the DMA-BUF plane count whe… |
| 2026-11-23 11:17:00 | [CVE-2026-135094](https://nvd.nist.gov/vuln/detail/CVE-2026-135094) | Medium | 6.5 | Missing authorization vulnerability in the "GetByProject" endpoint (/Project/{id}) of the VulnController in Cervantes v… |
| 2026-11-23 11:17:00 | [CVE-2026-59340](https://nvd.nist.gov/vuln/detail/CVE-2026-59340) | Medium | 6.5 | PagePdfDocumentReader and ParagraphPdfDocumentReader are vulnerable to a denial of service when processing untrusted PD… |
| 2026-11-23 11:17:00 | [CVE-2026-59442](https://nvd.nist.gov/vuln/detail/CVE-2026-59442) | High | 7.5 | TypesenseFilterExpressionConverter does not correctly translate grouped (parenthesized) filter expressions into the Typ… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
