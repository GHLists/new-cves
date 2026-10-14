# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-14 11:21 UTC

New CVEs published between 2026-10-14 10:19 UTC and 2026-10-14 11:21 UTC.

[Full CSV](data/new-cves-2026-10-14T11-21-26-071941Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-10-14 11:16:56 | [CVE-2026-100229](https://nvd.nist.gov/vuln/detail/CVE-2026-100229) | Medium | 6.5 | A flaw was found in GStreamer's H.266 codec parser library (libgstcodecparsers). An out-of-bounds write vulnerability e… |
| 2026-10-14 11:16:56 | [CVE-2026-101301](https://nvd.nist.gov/vuln/detail/CVE-2026-101301) | Medium | 5.3 | The WPCode WordPress plugin before 2.4.0 does not correctly verify that a request is genuinely for the login screen bef… |
| 2026-10-14 11:16:56 | [CVE-2026-101337](https://nvd.nist.gov/vuln/detail/CVE-2026-101337) | High | 8.7 | When base64 data is split up in pieces, of 3 character or less, tokens were incorrectly calculated to produce 0 bytes.… |
| 2026-10-14 11:16:57 | [CVE-2026-101338](https://nvd.nist.gov/vuln/detail/CVE-2026-101338) | High | 8.7 | When a SVCB or HTTPS RR has filled the wire format RDATA up to the brim, another ECH parameter may overwrite the stack,… |
| 2026-10-14 11:16:57 | [CVE-2026-101339](https://nvd.nist.gov/vuln/detail/CVE-2026-101339) | High | 8.7 | A HIP resource record that fills the RDATA near or at is limit, and has another dname RDATA field (a HIP Rendezvous ser… |
| 2026-10-14 11:16:57 | [CVE-2026-101341](https://nvd.nist.gov/vuln/detail/CVE-2026-101341) | High | 8.7 | Tokens of text in RDATA (of for example TXT records) under 32 bytes are not checked to stay within the space reserved f… |
| 2026-10-14 11:16:57 | [CVE-2026-103308](https://nvd.nist.gov/vuln/detail/CVE-2026-103308) | Medium | 6.5 | The Visma Pay for WooCommerce WordPress plugin before 1.2.2 does not verify the authenticity of payment gateway return… |
| 2026-10-14 11:16:57 | [CVE-2026-103358](https://nvd.nist.gov/vuln/detail/CVE-2026-103358) | High | 7.5 | Improper Control of Generation of Code ('Code Injection') vulnerability in VillaTheme Email Template Customizer for Woo… |
| 2026-10-14 11:16:58 | [CVE-2026-103904](https://nvd.nist.gov/vuln/detail/CVE-2026-103904) | High | 8.6 | The public consent endpoint of JTL-Shop accepts arbitrary consent names from unauthenticated visitors without validatin… |
| 2026-10-14 11:16:59 | [CVE-2026-103905](https://nvd.nist.gov/vuln/detail/CVE-2026-103905) | High | 8.7 | The authentication middleware of the JTL-Shop administration backend processes the plugin safe mode toggle on the admin… |
| 2026-10-14 11:16:59 | [CVE-2026-104795](https://nvd.nist.gov/vuln/detail/CVE-2026-104795) | High | 8.8 | The insights-runtime-extractor runs as a privileged DaemonSet (`hostPID: true`) that scans container processes for runt… |
| 2026-10-14 11:17:00 | [CVE-2026-105067](https://nvd.nist.gov/vuln/detail/CVE-2026-105067) | High | 8.5 | Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection') vulnerability in Webnus Modern Eve… |
| 2026-10-14 11:17:02 | [CVE-2026-107431](https://nvd.nist.gov/vuln/detail/CVE-2026-107431) | High | 7.5 | Missing Authorization vulnerability in Crocoblock JetFormBuilder jetformbuilder allows Exploiting Incorrectly Configure… |
| 2026-10-14 11:17:02 | [CVE-2026-107913](https://nvd.nist.gov/vuln/detail/CVE-2026-107913) |  |  | Rejected reason: This CVE ID is a duplicate of CVE-2026-39749 and was never published. Both IDs were assigned to the sa… |
| 2026-10-14 11:17:02 | [CVE-2026-108070](https://nvd.nist.gov/vuln/detail/CVE-2026-108070) | High | 8.7 | A vulnerability involving improper access control in the TSplus Remote Access web server that allows an unauthenticated… |
| 2026-10-14 11:17:03 | [CVE-2026-108071](https://nvd.nist.gov/vuln/detail/CVE-2026-108071) | High | 8.7 | Incorrect authentication vulnerability in the TSplus Remote Access multi-factor authentication (MFA) mechanism. A remot… |
| 2026-10-14 11:17:03 | [CVE-2026-108072](https://nvd.nist.gov/vuln/detail/CVE-2026-108072) | Medium | 5.4 | Vulnerability due to incorrect permissions in TSplus Remote Access shared login scripts. The autostart1.tscr files, loc… |
| 2026-10-14 11:17:04 | [CVE-2026-73795](https://nvd.nist.gov/vuln/detail/CVE-2026-73795) | Medium | 6.4 | A security vulnerability in HPE NonStop TMF Auditread2 can cause Denial of Service. |
| 2026-10-14 11:17:04 | [CVE-2026-73796](https://nvd.nist.gov/vuln/detail/CVE-2026-73796) | Medium | 4.4 | A security vulnerability in HPE NonStop TSQLEXE may cause application crash via a crafted SQL query. |
| 2026-10-14 11:17:05 | [CVE-2026-82844](https://nvd.nist.gov/vuln/detail/CVE-2026-82844) | Medium | 5.3 | The WPForms Lite WordPress plugin before 2.0.2.2 does not verify server-side that a payment was completed before accept… |
| 2026-10-14 11:17:06 | [CVE-2026-88842](https://nvd.nist.gov/vuln/detail/CVE-2026-88842) | Low | 3.3 | A flaw was found in BusyBox dpkg. The write_status_file() function does not reset a field cursor between package stanza… |
| 2026-10-14 11:17:07 | [CVE-2026-88998](https://nvd.nist.gov/vuln/detail/CVE-2026-88998) | Medium | 5.3 | The Tickera WordPress plugin before 3.6.0.4 does not correctly verify the integrity of incoming payment notifications,… |
| 2026-10-14 11:17:09 | [CVE-2026-97315](https://nvd.nist.gov/vuln/detail/CVE-2026-97315) | Medium | 5.4 | The Responsive Blocks WordPress plugin before 2.3.0 does not sanitise or escape some of the values submitted with its F… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
