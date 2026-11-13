# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-11-13 06:19 UTC

New CVEs published between 2026-11-13 05:18 UTC and 2026-11-13 06:19 UTC.

[Full CSV](data/new-cves-2026-11-13T06-19-16-273227Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-11-13 06:16:52 | [CVE-2026-116059](https://nvd.nist.gov/vuln/detail/CVE-2026-116059) |  |  | The LetsRecover WordPress plugin through 1.2.0 does not sanitize a user-supplied value that is used as a database colum… |
| 2026-11-13 06:16:52 | [CVE-2026-118063](https://nvd.nist.gov/vuln/detail/CVE-2026-118063) |  |  | The Advance Guest Post WordPress plugin through 1.9 does not properly validate uploaded files, relying on a case-sensit… |
| 2026-11-13 06:16:52 | [CVE-2026-118064](https://nvd.nist.gov/vuln/detail/CVE-2026-118064) |  |  | The Advance Guest Post WordPress plugin through 1.9 does not properly restrict or validate file uploads, authorizing an… |
| 2026-11-13 06:16:52 | [CVE-2026-118065](https://nvd.nist.gov/vuln/detail/CVE-2026-118065) |  |  | The Advance Guest Post WordPress plugin through 1.9 does not perform any authorization or ownership check when deleting… |
| 2026-11-13 06:16:53 | [CVE-2026-120407](https://nvd.nist.gov/vuln/detail/CVE-2026-120407) |  |  | The Contact Form 7 WordPress plugin before 6.2.5 does not restrict which user properties a form field's default value c… |
| 2026-11-13 06:16:53 | [CVE-2026-121853](https://nvd.nist.gov/vuln/detail/CVE-2026-121853) |  |  | The AppPresser WordPress plugin before 5.0.0 does not restrict access to two of its REST API endpoints, allowing unauth… |
| 2026-11-13 06:16:53 | [CVE-2026-123093](https://nvd.nist.gov/vuln/detail/CVE-2026-123093) |  |  | The WP Remote Users Sync WordPress plugin before 2.2.1 does not have authorisation and CSRF checks in one of its AJAX a… |
| 2026-11-13 06:16:53 | [CVE-2026-123097](https://nvd.nist.gov/vuln/detail/CVE-2026-123097) |  |  | The WP Remote Users Sync WordPress plugin before 2.2.1 does not restrict which account fields a synchronised site may s… |
| 2026-11-13 06:16:53 | [CVE-2026-123124](https://nvd.nist.gov/vuln/detail/CVE-2026-123124) |  |  | The WooCommerce Vindi Pagamento WordPress plugin through 0.8.3 does not perform any authorisation check when updating a… |
| 2026-11-13 06:16:53 | [CVE-2026-123670](https://nvd.nist.gov/vuln/detail/CVE-2026-123670) |  |  | The Essential Real Estate WordPress plugin before 5.3.6 does not verify that the recipients it allows for its contact e… |
| 2026-11-13 06:16:53 | [CVE-2026-123711](https://nvd.nist.gov/vuln/detail/CVE-2026-123711) |  |  | The WPCOM Member WordPress plugin before 1.8.3 does not limit or bind attempts to verify WeChat login codes, allowing u… |
| 2026-11-13 06:16:53 | [CVE-2026-124664](https://nvd.nist.gov/vuln/detail/CVE-2026-124664) |  |  | The Mine CloudVod WordPress plugin before 2.6.7 does not check whether the requester is enrolled in a course, or author… |
| 2026-11-13 06:16:53 | [CVE-2026-124763](https://nvd.nist.gov/vuln/detail/CVE-2026-124763) |  |  | The Woocommerce Wishlist WordPress plugin through 1.1.0 does not have authorisation and CSRF checks in one of its unaut… |
| 2026-11-13 06:16:53 | [CVE-2026-124822](https://nvd.nist.gov/vuln/detail/CVE-2026-124822) |  |  | The Easy DragDrop File Uploader WordPress plugin before 1.1.10 does not validate a user-supplied path before deleting i… |
| 2026-11-13 06:16:54 | [CVE-2026-124833](https://nvd.nist.gov/vuln/detail/CVE-2026-124833) |  |  | The Ahime Image Printer WordPress plugin through 1.0.0 does not validate the name, extension or type of uploaded files… |
| 2026-11-13 06:16:54 | [CVE-2026-125711](https://nvd.nist.gov/vuln/detail/CVE-2026-125711) |  |  | The Widgets for Google Reviews WordPress plugin before 14.3, WP Tripadvisor Review Widgets WordPress plugin before 14.3… |
| 2026-11-13 06:16:54 | [CVE-2026-125912](https://nvd.nist.gov/vuln/detail/CVE-2026-125912) |  |  | The WP Ultimate CSV Importer WordPress plugin before 9.2 does not restrict the destination filename and extension, nor… |
| 2026-11-13 06:16:54 | [CVE-2026-126119](https://nvd.nist.gov/vuln/detail/CVE-2026-126119) |  |  | The Streamit WordPress plugin before 1.3.10 does not perform any authorization or nonce verification on one of its unau… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
