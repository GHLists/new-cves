# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-06 01:19 UTC

New CVEs published between 2026-10-06 00:18 UTC and 2026-10-06 01:19 UTC.

[Full CSV](data/new-cves-2026-10-06T01-19-11-39582Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-10-06 01:16:33 | [CVE-2026-104031](https://nvd.nist.gov/vuln/detail/CVE-2026-104031) | Medium | 5.5 | A flaw was found in SSSD. In configurations where the autofs responder service is enabled, memory allocated during succ… |
| 2026-10-06 01:16:33 | [CVE-2026-104032](https://nvd.nist.gov/vuln/detail/CVE-2026-104032) | Medium | 5.5 | A flaw was found in SSSD. An unprivileged local user can repeatedly request master automount map updates through the au… |
| 2026-10-06 01:16:34 | [CVE-2026-104033](https://nvd.nist.gov/vuln/detail/CVE-2026-104033) | Medium | 5.4 | A flaw was found in SSSD. When configured to enforce account expiration using LDAP (Lightweight Directory Access Protoc… |
| 2026-10-06 01:16:34 | [CVE-2026-104034](https://nvd.nist.gov/vuln/detail/CVE-2026-104034) | Medium | 4.7 | A flaw was found in SSSD. A use-after-free vulnerability exists in the Kerberos Credential Manager (KCM) responder duri… |
| 2026-10-06 01:16:34 | [CVE-2026-104035](https://nvd.nist.gov/vuln/detail/CVE-2026-104035) | Medium | 5.5 | A flaw was found in SSSD. An issue in the Kerberos Credential Manager (KCM) responder allows a local user to cause a De… |
| 2026-10-06 01:16:34 | [CVE-2026-104036](https://nvd.nist.gov/vuln/detail/CVE-2026-104036) | Medium | 5.8 | A flaw was found in SSSD's NFS idmap plugin. When retrieving cached user or group names, the plugin detects if an entry… |
| 2026-10-06 01:16:34 | [CVE-2026-104037](https://nvd.nist.gov/vuln/detail/CVE-2026-104037) | Medium | 5.5 | A flaw was found in SSSD. A local attacker can exploit this issue by sending a specially crafted request with an invali… |
| 2026-10-06 01:16:34 | [CVE-2026-104038](https://nvd.nist.gov/vuln/detail/CVE-2026-104038) | Medium | 5.9 | A flaw was found in sssd. A remote attacker can cause a denial of service (DoS) by submitting a certificate that lacks… |
| 2026-10-06 01:16:35 | [CVE-2026-105472](https://nvd.nist.gov/vuln/detail/CVE-2026-105472) | Low | 2.1 | A weakness has been identified in girishsaraf Online-Appointment-Booking-System up to f427b4757128ca253d33d0cc4e87bbb9c… |
| 2026-10-06 01:16:36 | [CVE-2026-92821](https://nvd.nist.gov/vuln/detail/CVE-2026-92821) | Medium | 6.8 | A flaw was found in SSSD. When configured to evaluate password expiration warnings before restrictive access rules in L… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
