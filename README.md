# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-08 11:19 UTC

New CVEs published between 2026-10-08 10:19 UTC and 2026-10-08 11:19 UTC.

[Full CSV](data/new-cves-2026-10-08T11-19-10-6776Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-10-08 11:16:42 | [CVE-2026-103010](https://nvd.nist.gov/vuln/detail/CVE-2026-103010) | High | 7.8 | Heap-based buffer overflow in the legacy Blowfish decryption routine (BlowFishEncryptor::DecryptFromString) in Progress… |
| 2026-10-08 11:16:42 | [CVE-2026-103011](https://nvd.nist.gov/vuln/detail/CVE-2026-103011) | Medium | 6.5 | Heap-based buffer overflow in the legacy Blowfish encryption routine (BlowFishEncryptor::Encode, called by EncryptToStr… |
| 2026-10-08 11:16:42 | [CVE-2026-103517](https://nvd.nist.gov/vuln/detail/CVE-2026-103517) | Medium | 5.3 | The Airwallex Online Payments Gateway WordPress plugin before 1.36.0 does not verify that an incoming payment notificat… |
| 2026-10-08 11:16:42 | [CVE-2026-103647](https://nvd.nist.gov/vuln/detail/CVE-2026-103647) | High | 8.0 | Cross-site scripting in the webmail of Progressive Robot hMailServer 6.3.2 through 6.3.5 allows a remote attacker who c… |
| 2026-10-08 11:16:43 | [CVE-2026-103649](https://nvd.nist.gov/vuln/detail/CVE-2026-103649) | High | 7.5 | Missing network timeouts in the Linux builds of Progressive Robot hMailServer 6.3.0 through 6.3.5 allow a remote attack… |
| 2026-10-08 11:16:43 | [CVE-2026-104658](https://nvd.nist.gov/vuln/detail/CVE-2026-104658) | High | 7.8 | The Linux live-update apply helper (hmailserver-update) of Progressive Robot hMailServer 6.3.4 and 6.3.5 runs as root o… |
| 2026-10-08 11:16:44 | [CVE-2026-104659](https://nvd.nist.gov/vuln/detail/CVE-2026-104659) | High | 7.5 | Missing Host header validation and missing throttling of failed administrator sign-ins in the REST API listener of Prog… |
| 2026-10-08 11:16:44 | [CVE-2026-104660](https://nvd.nist.gov/vuln/detail/CVE-2026-104660) | High | 7.8 | Missing authorization on COM objects in Progressive Robot hMailServer 6.0.0 through 6.3.5 (Windows only) lets a local i… |
| 2026-10-08 11:16:44 | [CVE-2026-104671](https://nvd.nist.gov/vuln/detail/CVE-2026-104671) | Medium | 5.3 | The TutorStarter WordPress theme before 4.0.4 does not respect the site's user registration setting in one of its AJAX… |
| 2026-10-08 11:16:44 | [CVE-2026-104704](https://nvd.nist.gov/vuln/detail/CVE-2026-104704) | High | 7.4 | Progressive Robot hMailServer 6.0.0 through 6.3.5 does not enforce TLS for outbound SMTP delivery to a mail exchanger w… |
| 2026-10-08 11:16:44 | [CVE-2026-105190](https://nvd.nist.gov/vuln/detail/CVE-2026-105190) | Medium | 5.3 | The Easy Digital Downloads WordPress plugin before 3.7.1 does not consult the site's user registration setting before c… |
| 2026-10-08 11:16:47 | [CVE-2026-93509](https://nvd.nist.gov/vuln/detail/CVE-2026-93509) | Medium | 6.5 | The Wallet System for WooCommerce WordPress plugin before 2.8.0 does not validate that a wallet transfer amount is posi… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
