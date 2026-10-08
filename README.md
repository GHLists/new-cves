# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-08 20:18 UTC

New CVEs published between 2026-10-08 19:18 UTC and 2026-10-08 20:18 UTC.

[Full CSV](data/new-cves-2026-10-08T20-18-40-126418Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-10-08 19:18:41 | [CVE-2026-67693](https://nvd.nist.gov/vuln/detail/CVE-2026-67693) |  |  | An issue in gnutls v.3.8.13 allows an attacker to obtain sensitive information via failing to reject end-entity X.509 c… |
| 2026-10-08 19:20:51 | [CVE-2026-84276](https://nvd.nist.gov/vuln/detail/CVE-2026-84276) | High | 7.5 | IBM Guardium Data Protection 12.2.2 is affected by a denial-of-service vulnerability in the edge-controller. An unauthe… |
| 2026-10-08 19:20:51 | [CVE-2026-84278](https://nvd.nist.gov/vuln/detail/CVE-2026-84278) | High | 7.2 | IBM Guardium Data Protection 12.2 is affected by a command injection vulnerability in the SUID-root ssh_config_wrapper… |
| 2026-10-08 19:20:51 | [CVE-2026-84290](https://nvd.nist.gov/vuln/detail/CVE-2026-84290) | Medium | 5.1 | IBM Guardium Data Protection 12.0, 12.1, 12.2 is affected by an improper validation of user-supplied pointers in the Wf… |
| 2026-10-08 19:20:52 | [CVE-2026-88648](https://nvd.nist.gov/vuln/detail/CVE-2026-88648) |  |  | Incomplete X.509 implementation in GnuTLS v3.8.13 allows attackers controlling a subordinate Certificate Authority to b… |
| 2026-10-08 19:20:52 | [CVE-2026-95209](https://nvd.nist.gov/vuln/detail/CVE-2026-95209) |  |  | An issue in gnutls v3.8.13 causes legitimate CA certificates to be rejected, leading to a Denial of Service (DoS). |
| 2026-10-08 20:17:29 | [CVE-2026-104075](https://nvd.nist.gov/vuln/detail/CVE-2026-104075) | Critical | 9.3 | TVU Networks Receiver/Transceiver devices running firmware before version 7.9 contain an authentication bypass vulnerab… |
| 2026-10-08 20:17:29 | [CVE-2026-104076](https://nvd.nist.gov/vuln/detail/CVE-2026-104076) | Critical | 9.3 | TVU Networks Receiver/Transceiver devices running firmware before version 7.9 contain a missing authentication vulnerab… |
| 2026-10-08 20:17:29 | [CVE-2026-106126](https://nvd.nist.gov/vuln/detail/CVE-2026-106126) | Critical | 9.4 | A command injection vulnerability in the Active Directory Events Listener of Tenable Identity Exposure (SaaS) allows an… |
| 2026-10-08 20:17:30 | [CVE-2026-106432](https://nvd.nist.gov/vuln/detail/CVE-2026-106432) | Low | 2.0 | The BSON encoder in the MongoDB PHP Driver converts a string length to a 32-bit value without validation. When an affec… |
| 2026-10-08 20:17:31 | [CVE-2026-106436](https://nvd.nist.gov/vuln/detail/CVE-2026-106436) | Medium | 6.3 | The BSON encoder in the MongoDB PHP Driver does not check some return values after a document exceeds libbson's size li… |
| 2026-10-08 20:17:33 | [CVE-2026-107389](https://nvd.nist.gov/vuln/detail/CVE-2026-107389) | Medium | 6.2 | music-metadata is a metadata parser for audio and video media files. Prior to 11.16.0, the Matroska and WebM EBML parse… |
| 2026-10-08 20:17:33 | [CVE-2026-107390](https://nvd.nist.gov/vuln/detail/CVE-2026-107390) | Medium | 6.2 | music-metadata is a metadata parser for audio and video media files. Prior to 11.16.0, the MP4 parser accepts an attack… |
| 2026-10-08 20:17:33 | [CVE-2026-107391](https://nvd.nist.gov/vuln/detail/CVE-2026-107391) | Medium | 6.2 | music-metadata is a metadata parser for audio and video media files. In the public development revision introduced afte… |
| 2026-10-08 20:17:33 | [CVE-2026-107392](https://nvd.nist.gov/vuln/detail/CVE-2026-107392) | Medium | 6.2 | music-metadata is a metadata parser for audio and video media files. Prior to 11.15.0, the DSF parser handles an unreco… |
| 2026-10-08 20:17:33 | [CVE-2026-107393](https://nvd.nist.gov/vuln/detail/CVE-2026-107393) | Medium | 6.1 | FreeScout is a self-hosted help desk and shared mailbox. Prior to 1.8.235, when APP_CLOUDFLARE_IS_USED is enabled, Free… |
| 2026-10-08 20:17:34 | [CVE-2026-107394](https://nvd.nist.gov/vuln/detail/CVE-2026-107394) | Medium | 6.8 | Indico is an event management system that uses Flask-Multipass, a multi-backend authentication system for Flask. Prior… |
| 2026-10-08 20:17:34 | [CVE-2026-107395](https://nvd.nist.gov/vuln/detail/CVE-2026-107395) | Medium | 4.3 | Indico is an event management system that uses Flask-Multipass, a multi-backend authentication system for Flask. Prior… |
| 2026-10-08 20:17:34 | [CVE-2026-107396](https://nvd.nist.gov/vuln/detail/CVE-2026-107396) | Medium | 5.4 | Indico is an event management system that uses Flask-Multipass, a multi-backend authentication system for Flask. Prior… |
| 2026-10-08 20:17:34 | [CVE-2026-107608](https://nvd.nist.gov/vuln/detail/CVE-2026-107608) | Medium | 6.8 | Improper link resolution before file access in the asset bundling output handling in AWS aws-cdk-lib before 2.267.0 mig… |
| 2026-10-08 20:17:35 | [CVE-2026-107705](https://nvd.nist.gov/vuln/detail/CVE-2026-107705) | High | 8.3 | Poppler 0.42.0 through 26.10.0 contains a stack-based buffer overflow in Decrypt::revision6Hash() that allows attackers… |
| 2026-10-08 20:17:35 | [CVE-2026-107706](https://nvd.nist.gov/vuln/detail/CVE-2026-107706) | Medium | 5.3 | Dolibarr ERP CRM before 24.0.2 contains an incorrect authorization vulnerability in htdocs/core/ajax/updateextrafield.p… |
| 2026-10-08 20:17:35 | [CVE-2026-107707](https://nvd.nist.gov/vuln/detail/CVE-2026-107707) | High | 8.5 | Intego Antivirus for Windows through 3.0.0.1 contains a link following vulnerability in its optimization module that al… |
| 2026-10-08 20:17:36 | [CVE-2026-82334](https://nvd.nist.gov/vuln/detail/CVE-2026-82334) | High | 8.1 | IBM Guardium Data Protection 12.0, 12.1, 12.2 is vulnerable to a heap-based out-of-bounds read in the TDS7 LOGIN7 proto… |
| 2026-10-08 20:17:36 | [CVE-2026-82335](https://nvd.nist.gov/vuln/detail/CVE-2026-82335) | High | 8.1 | IBM Guardium Data Protection 12.0, 12.1, 12.2 is vulnerable to a heap-based buffer overflow in the MongoDB protocol par… |
| 2026-10-08 20:17:37 | [CVE-2026-82344](https://nvd.nist.gov/vuln/detail/CVE-2026-82344) | High | 8.1 | IBM Guardium Data Protection 12.0, 12.1 is vulnerable to a heap-based buffer overflow in the S-TAP TrafficTap TDS login… |
| 2026-10-08 20:17:37 | [CVE-2026-84244](https://nvd.nist.gov/vuln/detail/CVE-2026-84244) | Critical | 9.3 | IBM Guardium Data Protection 12.2 IBM Security Guardium Data Protection is vulnerable to stored cross-site scripting (X… |
| 2026-10-08 20:17:37 | [CVE-2026-84245](https://nvd.nist.gov/vuln/detail/CVE-2026-84245) | High | 7.8 | IBM Guardium Data Protection 12.2 is vulnerable to a local privilege escalation in the cp_wrapper component. A low-priv… |
| 2026-10-08 20:17:37 | [CVE-2026-84250](https://nvd.nist.gov/vuln/detail/CVE-2026-84250) | High | 8.4 | IBM Guardium Data Protection 12.2 is vulnerable due to weak cryptographic protection and a hard-coded recovery key in t… |
| 2026-10-08 20:17:37 | [CVE-2026-84271](https://nvd.nist.gov/vuln/detail/CVE-2026-84271) | High | 7.8 | IBM Guardium Data Protection 12.2 is vulnerable to a signature verification bypass in the patch installer. An attacker… |
| 2026-10-08 20:17:37 | [CVE-2026-84272](https://nvd.nist.gov/vuln/detail/CVE-2026-84272) | Critical | 9.8 | IBM Guardium Data Protection 12.1 and 12.2.2 are vulnerable to missing authentication in the edge-controller component.… |
| 2026-10-08 20:17:37 | [CVE-2026-84274](https://nvd.nist.gov/vuln/detail/CVE-2026-84274) | Medium | 6.5 | IBM Guardium Data Protection 12.2.2 is affected by a sensitive information exposure vulnerability. During SECRET and AP… |
| 2026-10-08 20:17:38 | [CVE-2026-84275](https://nvd.nist.gov/vuln/detail/CVE-2026-84275) | High | 7.5 | IBM Guardium Data Protection 12.2 is vulnerable to path traversal in the GIM file-upload functionality. An unauthentica… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
