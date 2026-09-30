# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-09-30 10:18 UTC

New CVEs published between 2026-09-30 09:21 UTC and 2026-09-30 10:18 UTC.

[Full CSV](data/new-cves-2026-09-30T10-18-40-793784Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-09-30 10:17:16 | [CVE-2026-103235](https://nvd.nist.gov/vuln/detail/CVE-2026-103235) | High | 8.7 | MISP contains a mass assignment vulnerability in the event delegation feature. When a user with delegation permission s… |
| 2026-09-30 10:17:16 | [CVE-2026-103237](https://nvd.nist.gov/vuln/detail/CVE-2026-103237) | High | 8.3 | MISP contains an improper input validation vulnerability in its ORM save path. When a user submits data through various… |
| 2026-09-30 10:17:16 | [CVE-2026-10764](https://nvd.nist.gov/vuln/detail/CVE-2026-10764) | High | 8.7 | Information disclosure in BVMS 4.5 up to 12.3 including allows man-in-the-middle attackers to gain unauthorized access… |
| 2026-09-30 10:17:17 | [CVE-2026-77185](https://nvd.nist.gov/vuln/detail/CVE-2026-77185) | Critical | 9.1 | Authentication bypass in sshd-core in Apache MINA SSHD versions 2.0.0 to 2.19.0 and 3.0.0-M1 to 3.0.0-M5 for a certain… |
| 2026-09-30 10:17:17 | [CVE-2026-79625](https://nvd.nist.gov/vuln/detail/CVE-2026-79625) | High | 7.2 | Affected products do not properly synchronize access to their monitoring functionality. When multiple clients send conc… |
| 2026-09-30 10:17:17 | [CVE-2026-93994](https://nvd.nist.gov/vuln/detail/CVE-2026-93994) | High | 8.1 | Apache MINA SSHD is a Java library for client-side and server-side SSH. SSH servers can be configured to require multi-… |
| 2026-09-30 10:17:17 | [CVE-2026-93995](https://nvd.nist.gov/vuln/detail/CVE-2026-93995) | Medium | 6.5 | Improper input validation in sshd-git in Apache MINA SSHD, versions up to 2.19.0 and 3.0.0-M1 to 3.0.0-M5. Apache MINA… |
| 2026-09-30 10:17:17 | [CVE-2026-93996](https://nvd.nist.gov/vuln/detail/CVE-2026-93996) | Medium | 6.5 | Uncontrolled resource consumption in component ssd-scp in Apache MINA SSHD versions up to 2.19.0 or 3.0.0-M1 to 3.0.0-M… |
| 2026-09-30 10:17:17 | [CVE-2026-94002](https://nvd.nist.gov/vuln/detail/CVE-2026-94002) | High | 7.5 | Possible memory exhaustion in SFTP clients (DefaultSftpClient) in component sshd-sftp in Apache MINA SSHD versions 0.9.… |
| 2026-09-30 10:17:18 | [CVE-2026-94029](https://nvd.nist.gov/vuln/detail/CVE-2026-94029) | Medium | 6.5 | Server-side memory exhaustion in Apache MINA SSHD 1.0.0 to 2.19.0 and 3.0.0-M1 to 3.0.0-M5, component sshd-sftp, in the… |
| 2026-09-30 10:17:18 | [CVE-2026-94052](https://nvd.nist.gov/vuln/detail/CVE-2026-94052) | Critical | 9.1 | A missing check in LdapPasswordAuthenticator in component sshd-ldap in Apache MINA SSHD versions 1.2.0 to 2.19.0 or 3.0… |
| 2026-09-30 10:17:18 | [CVE-2026-94053](https://nvd.nist.gov/vuln/detail/CVE-2026-94053) | Critical | 9.1 | Authentication bypass via LDAP injection in component sshd-ldap in Apache MINA SSHD versions 1.2.0 to 2.19.0 and 3.0.0-… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
