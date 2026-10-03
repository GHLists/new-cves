# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-03 00:18 UTC

New CVEs published between 2026-10-02 23:19 UTC and 2026-10-03 00:18 UTC.

[Full CSV](data/new-cves-2026-10-03T00-18-40-190572Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-10-03 00:16:35 | [CVE-2026-104433](https://nvd.nist.gov/vuln/detail/CVE-2026-104433) | High | 8.7 | Mooncake transfer engine before 0.3.12 contains an out-of-bounds read vulnerability in the readString function of inclu… |
| 2026-10-03 00:16:35 | [CVE-2026-104474](https://nvd.nist.gov/vuln/detail/CVE-2026-104474) | Medium | 5.4 | OpenLiteSpeed before 1.9.3 contains a local privilege escalation vulnerability in admin/misc/lsup.sh that runs unverifi… |
| 2026-10-03 00:16:35 | [CVE-2026-104475](https://nvd.nist.gov/vuln/detail/CVE-2026-104475) | Medium | 5.1 | IDURAR ERP CRM through 4.1.1 contains a stored cross-site scripting vulnerability that allows authenticated users to in… |
| 2026-10-03 00:16:35 | [CVE-2026-104476](https://nvd.nist.gov/vuln/detail/CVE-2026-104476) | High | 8.2 | Backdrop CMS before 1.35.1 contains an information disclosure vulnerability that allows unauthenticated attackers to re… |
| 2026-10-03 00:16:35 | [CVE-2026-104477](https://nvd.nist.gov/vuln/detail/CVE-2026-104477) | Medium | 5.3 | Showdown through 2.1.0 contains a cross-site scripting vulnerability in the makehtml link and image subparsers, which f… |
| 2026-10-03 00:16:36 | [CVE-2026-104478](https://nvd.nist.gov/vuln/detail/CVE-2026-104478) | High | 7.1 | Formwork before 2.3.13 contains a path traversal vulnerability in BackupController that allows authenticated panel user… |
| 2026-10-03 00:16:36 | [CVE-2026-104479](https://nvd.nist.gov/vuln/detail/CVE-2026-104479) | Medium | 5.1 | Shopclass before 6.2.0 contains a stored cross-site scripting vulnerability that allows self-registered non-admin users… |
| 2026-10-03 00:16:36 | [CVE-2026-105029](https://nvd.nist.gov/vuln/detail/CVE-2026-105029) | Medium | 5.3 | UVdesk support-center-bundle before 1.1.3.3 contains an insecure direct object reference vulnerability in the rateTicke… |
| 2026-10-03 00:16:36 | [CVE-2026-105030](https://nvd.nist.gov/vuln/detail/CVE-2026-105030) | Medium | 6.9 | Kener 4.0.0 before 4.1.6 contains an information disclosure vulnerability that allows unauthenticated attackers to retr… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
