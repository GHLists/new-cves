# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-23 09:18 UTC

New CVEs published between 2026-10-23 08:20 UTC and 2026-10-23 09:18 UTC.

[Full CSV](data/new-cves-2026-10-23T09-18-48-473043Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-10-23 09:17:03 | [CVE-2025-30043](https://nvd.nist.gov/vuln/detail/CVE-2025-30043) | High | 7.1 | CGM CLININET is vulnerable to Missing Authentication for Critical Function in the /DocManagment path. The endpoint is a… |
| 2026-10-23 09:17:04 | [CVE-2025-30045](https://nvd.nist.gov/vuln/detail/CVE-2025-30045) | High | 8.6 | CGM CLININET is vulnerable to Code Injection in the ConvExpr function, which processes Perl expressions into RTF docume… |
| 2026-10-23 09:17:04 | [CVE-2025-30046](https://nvd.nist.gov/vuln/detail/CVE-2025-30046) | Critical | 9.0 | In the CGM CLININET application server, multiple processes responsible for HL7 communication with external systems run… |
| 2026-10-23 09:17:04 | [CVE-2025-30047](https://nvd.nist.gov/vuln/detail/CVE-2025-30047) | Critical | 9.4 | CGM CLININET is vulnerable to Remote Code Execution caused by deserialization of untrusted data. The server exposes an… |
| 2026-10-23 09:17:04 | [CVE-2025-30049](https://nvd.nist.gov/vuln/detail/CVE-2025-30049) | High | 8.2 | The CGM CLININET application stores user passwords as unsalted MD5 hashes. This issue was fixed in versions 2026.MS1 an… |
| 2026-10-23 09:17:04 | [CVE-2025-30050](https://nvd.nist.gov/vuln/detail/CVE-2025-30050) | Critical | 9.4 | CGM CLININET is vulnerable to Code Injection in the RunCGI.pm component, which dynamically imports the module specified… |
| 2026-10-23 09:17:04 | [CVE-2025-30051](https://nvd.nist.gov/vuln/detail/CVE-2025-30051) | Medium | 6.8 | The CGM CLININET application stores the production database login and password, as well as RabbitMQ broker credentials,… |
| 2026-10-23 09:17:05 | [CVE-2025-30052](https://nvd.nist.gov/vuln/detail/CVE-2025-30052) | High | 8.8 | The rsyncd service of the CGM CLININET is vulnerable to Authentication Bypass via IP spoofing. Access is granted based… |
| 2026-10-23 09:17:05 | [CVE-2025-30053](https://nvd.nist.gov/vuln/detail/CVE-2025-30053) | Medium | 6.9 | The CGM CLININET application runs the cgm-updater process listening on an open network port without any authentication.… |
| 2026-10-23 09:17:05 | [CVE-2025-30054](https://nvd.nist.gov/vuln/detail/CVE-2025-30054) | Critical | 9.3 | CGM CLININET is vulnerable to local privilege escalation. The service that processes incoming HL7 messages runs with ro… |
| 2026-10-23 09:17:05 | [CVE-2025-58403](https://nvd.nist.gov/vuln/detail/CVE-2025-58403) | Medium | 5.1 | CGM CLININET is vulnerable to Reflected Cross-Site Scripting (XSS) due to improper neutralization of user-supplied data… |
| 2026-10-23 09:17:05 | [CVE-2026-112359](https://nvd.nist.gov/vuln/detail/CVE-2026-112359) | High | 7.5 | Missing Authorization vulnerability in Amauri.IO WPMobile.App wpappninja allows Exploiting Incorrectly Configured Acces… |
| 2026-10-23 09:17:05 | [CVE-2026-112821](https://nvd.nist.gov/vuln/detail/CVE-2026-112821) | Medium | 6.5 | Missing Authorization vulnerability in Knit Pay Knit Pay knit-pay allows Exploiting Incorrectly Configured Access Contr… |
| 2026-10-23 09:17:05 | [CVE-2026-112825](https://nvd.nist.gov/vuln/detail/CVE-2026-112825) | Medium | 6.5 | Missing Authorization vulnerability in Magepeople inc. Car Rental Manager car-rental-manager allows Exploiting Incorrec… |
| 2026-10-23 09:17:05 | [CVE-2026-112835](https://nvd.nist.gov/vuln/detail/CVE-2026-112835) | High | 7.1 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in e4jvikwp VikRentC… |
| 2026-10-23 09:17:06 | [CVE-2026-112837](https://nvd.nist.gov/vuln/detail/CVE-2026-112837) | High | 8.5 | Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection') vulnerability in Ruben Garcia Gami… |
| 2026-10-23 09:17:06 | [CVE-2026-112838](https://nvd.nist.gov/vuln/detail/CVE-2026-112838) | High | 7.1 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in e4jvikwp VikRentC… |
| 2026-10-23 09:17:06 | [CVE-2026-112860](https://nvd.nist.gov/vuln/detail/CVE-2026-112860) | Critical | 9.3 | Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection') vulnerability in xnau webdesign Pa… |
| 2026-10-23 09:17:06 | [CVE-2026-112862](https://nvd.nist.gov/vuln/detail/CVE-2026-112862) | Critical | 9.8 | Deserialization of Untrusted Data vulnerability in xnau webdesign Participants Database participants-database allows Ob… |
| 2026-10-23 09:17:06 | [CVE-2026-115657](https://nvd.nist.gov/vuln/detail/CVE-2026-115657) | Medium | 4.8 | When used as an executor in either KNIME Server or KNIME Business Hub, KNIME Analytics Platform LTS versions before 5.8… |
| 2026-10-23 09:17:06 | [CVE-2026-16762](https://nvd.nist.gov/vuln/detail/CVE-2026-16762) | High | 8.7 | An attacker able to supply a crafted XML document to an application using QXmlStreamReader can cause disproportionate C… |
| 2026-10-23 09:17:06 | [CVE-2026-25716](https://nvd.nist.gov/vuln/detail/CVE-2026-25716) | High | 7.1 | Missing Authorization vulnerability in Hallo Welt! GmbH BlueSpice (Extension:BlueSpiceUserManager) allows any authentic… |
| 2026-10-23 09:17:06 | [CVE-2026-25784](https://nvd.nist.gov/vuln/detail/CVE-2026-25784) | Critical | 9.3 | Initialization of a Resource with an Insecure Default vulnerability in Hallo Welt! GmbH BlueSpice (container image blue… |
| 2026-10-23 09:17:07 | [CVE-2026-89312](https://nvd.nist.gov/vuln/detail/CVE-2026-89312) | Medium | 6.9 | `AesGcmCryptor.Open` passed a caller-supplied nonce straight to `cipher.AEAD.Open` without checking its length. The Go… |
| 2026-10-23 09:17:07 | [CVE-2026-89313](https://nvd.nist.gov/vuln/detail/CVE-2026-89313) | Medium | 6.3 | `JwksTrustStore.Get` assigned each parsed key to the function's **named return value** while refreshing the JWKS cache.… |
| 2026-10-23 09:17:07 | [CVE-2026-89314](https://nvd.nist.gov/vuln/detail/CVE-2026-89314) | Medium | 6.9 | `jwkFields.CheckConsistency` detected duplicate `key_ops` entries with a pairwise nested loop, making validation cost g… |
| 2026-10-23 09:17:08 | [CVE-2026-89315](https://nvd.nist.gov/vuln/detail/CVE-2026-89315) | Medium | 6.9 | `JwtClaims.MarshalJSON` built a Go struct at runtime with `reflect.StructOf`, synthesising a field named `"A" + claimNa… |
| 2026-10-23 09:17:08 | [CVE-2026-89316](https://nvd.nist.gov/vuln/detail/CVE-2026-89316) | Medium | 6.3 | `LoadPublicKey` resolved an EC key's curve with an unchecked type assertion, `algToOptsMap[alg].(*ECDSAOptions)`. A JWK… |
| 2026-10-23 09:17:08 | [CVE-2026-89317](https://nvd.nist.gov/vuln/detail/CVE-2026-89317) | Medium | 6.3 | gose parsed the JWS `crit` header into `JwsHeader.Crit` and then never read it. RFC 7515 §4.1.11 requires a recipient t… |
| 2026-10-23 09:17:08 | [CVE-2026-89318](https://nvd.nist.gov/vuln/detail/CVE-2026-89318) | Medium | 6.9 | `JweRsaKeyEncryptionDecryptorImpl.Decrypt` passed the JWE's initialization vector to `cipher.AEAD.Open` without checkin… |
| 2026-10-23 09:17:08 | [CVE-2026-89319](https://nvd.nist.gov/vuln/detail/CVE-2026-89319) | Medium | 6.3 | `JweDirectDecryptorBlock.Decrypt` read a 64-bit plaintext length from the `_thales_aad` protected-header field and used… |
| 2026-10-23 09:17:08 | [CVE-2026-89320](https://nvd.nist.gov/vuln/detail/CVE-2026-89320) | High | 8.8 | `HmacShaCryptor.Hash` never hashed its input. For any input it returned `HMAC_K("")` — the MAC of the empty message und… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
