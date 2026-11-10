# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-11-10 09:20 UTC

New CVEs published between 2026-11-10 08:18 UTC and 2026-11-10 09:20 UTC.

[Full CSV](data/new-cves-2026-11-10T09-20-50-200777Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-11-10 09:17:21 | [CVE-2026-106007](https://nvd.nist.gov/vuln/detail/CVE-2026-106007) | Medium | 5.3 | The FraudLabs Pro SMS Verification WordPress plugin through 1.12.1 does not enforce its SMS-retry limit on the server s… |
| 2026-11-10 09:17:21 | [CVE-2026-106025](https://nvd.nist.gov/vuln/detail/CVE-2026-106025) | Medium | 5.3 | The Cargo Shipping Location for WooCommerce WordPress plugin before 6.0 does not properly restrict access to a REST API… |
| 2026-11-10 09:17:22 | [CVE-2026-120012](https://nvd.nist.gov/vuln/detail/CVE-2026-120012) | High | 7.5 | SAP Cloud SDK for AI (Node.js) could inadvertently include sensitive authentication credentials in error messages gener… |
| 2026-11-10 09:17:22 | [CVE-2026-120013](https://nvd.nist.gov/vuln/detail/CVE-2026-120013) | High | 7.5 | The agent_memory module accepts a caller-supplied tenant parameter in create_client(tenant=...). Prior to version 0.50.… |
| 2026-11-10 09:17:22 | [CVE-2026-60035](https://nvd.nist.gov/vuln/detail/CVE-2026-60035) | High | 8.6 | A high privileged remote attacker can perform a code injection in the backends network auth function leading to code ex… |
| 2026-11-10 09:17:22 | [CVE-2026-60036](https://nvd.nist.gov/vuln/detail/CVE-2026-60036) | High | 8.6 | A high privileged remote attacker can perform a code injection in the backends patch activate function leading to code… |
| 2026-11-10 09:17:23 | [CVE-2026-60037](https://nvd.nist.gov/vuln/detail/CVE-2026-60037) | High | 8.6 | A high privileged remote attacker can perform an OpenSSL code injection in the frontends device importer function leadi… |
| 2026-11-10 09:17:23 | [CVE-2026-60038](https://nvd.nist.gov/vuln/detail/CVE-2026-60038) | High | 8.6 | A high privileged remote attacker can perform an OpenSSL code injection in the backends ImportPKCS12 function leading t… |
| 2026-11-10 09:17:23 | [CVE-2026-60039](https://nvd.nist.gov/vuln/detail/CVE-2026-60039) | High | 8.6 | A high privileged remote attacker can perform a code injection in the backends backup restore function leading to code… |
| 2026-11-10 09:17:23 | [CVE-2026-60040](https://nvd.nist.gov/vuln/detail/CVE-2026-60040) | High | 8.7 | An unauthenticated remote attacker can perform a DoS in the backends backup creation function. This can result in a tot… |
| 2026-11-10 09:17:23 | [CVE-2026-60041](https://nvd.nist.gov/vuln/detail/CVE-2026-60041) | Medium | 5.3 | An unauthenticated remote attacker can perform a CSRF attack on a logged in backend user allowing for execution of mult… |
| 2026-11-10 09:17:23 | [CVE-2026-60042](https://nvd.nist.gov/vuln/detail/CVE-2026-60042) | Medium | 6.9 | An unauthenticated remote attacker can perform an authentication bypass on the com_check function, potentially triggeri… |
| 2026-11-10 09:17:24 | [CVE-2026-60043](https://nvd.nist.gov/vuln/detail/CVE-2026-60043) | Medium | 6.4 | An unauthenticated remote attacker can perform a XSS attack on a logged in backend user allowing for execution of multi… |
| 2026-11-10 09:17:24 | [CVE-2026-60044](https://nvd.nist.gov/vuln/detail/CVE-2026-60044) | High | 8.7 | The backups created by the application use a weak static password allowing an unauthenticated remote attacker to access… |
| 2026-11-10 09:17:24 | [CVE-2026-60045](https://nvd.nist.gov/vuln/detail/CVE-2026-60045) | Medium | 6.9 | A high privileged remote attacker can upload arbitrary files to a guessable location. This can result in a loss of avai… |
| 2026-11-10 09:17:24 | [CVE-2026-60046](https://nvd.nist.gov/vuln/detail/CVE-2026-60046) | High | 8.7 | An unauthenticated remote attacker can perform password resets for any user with known username and email without rate… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
