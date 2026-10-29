# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-29 11:18 UTC

New CVEs published between 2026-10-29 10:18 UTC and 2026-10-29 11:18 UTC.

[Full CSV](data/new-cves-2026-10-29T11-18-54-571687Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-10-29 11:17:24 | [CVE-2026-105031](https://nvd.nist.gov/vuln/detail/CVE-2026-105031) |  |  | When using the OpenSSL TLS implementation, both the pn_ssl_domain_set_trusted_ca_db() & pn_tls_config_set_trusted_certs… |
| 2026-10-29 11:17:24 | [CVE-2026-105042](https://nvd.nist.gov/vuln/detail/CVE-2026-105042) |  |  | A message body that is deeply nested and decoded by pn_message_body() could overflow the stack and cause a crash. This… |
| 2026-10-29 11:17:27 | [CVE-2026-112827](https://nvd.nist.gov/vuln/detail/CVE-2026-112827) | High | 7.1 | Missing Authorization vulnerability in VillaTheme HANDMADE – Dropshipping for Etsy and WooCommerce handmade-dropshippin… |
| 2026-10-29 11:17:28 | [CVE-2026-114193](https://nvd.nist.gov/vuln/detail/CVE-2026-114193) | High | 7.5 | Missing Authorization vulnerability in Eyal Fitoussi GEO my WordPress geo-my-wp allows Exploiting Incorrectly Configure… |
| 2026-10-29 11:17:28 | [CVE-2026-114230](https://nvd.nist.gov/vuln/detail/CVE-2026-114230) |  |  | When dispatching SASL frames to authenticate the peer, Proton will also dispatch AMQP frames if they claim to be SASL f… |
| 2026-10-29 11:17:29 | [CVE-2026-115592](https://nvd.nist.gov/vuln/detail/CVE-2026-115592) | High | 7.1 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in OceanWP OceanWP o… |
| 2026-10-29 11:17:30 | [CVE-2026-115599](https://nvd.nist.gov/vuln/detail/CVE-2026-115599) | High | 7.5 | Missing Authorization vulnerability in ThimPress LearnPress learnpress allows Exploiting Incorrectly Configured Access… |
| 2026-10-29 11:17:30 | [CVE-2026-115611](https://nvd.nist.gov/vuln/detail/CVE-2026-115611) | High | 7.1 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in PluginUs.Net Tabl… |
| 2026-10-29 11:17:30 | [CVE-2026-115942](https://nvd.nist.gov/vuln/detail/CVE-2026-115942) |  |  | A misconfigured wildcard TLS certificate causes a stack read overflow. This issue does not affect any wildcard certific… |
| 2026-10-29 11:17:30 | [CVE-2026-115962](https://nvd.nist.gov/vuln/detail/CVE-2026-115962) | Medium | 4.3 | Authentication Bypass by Spoofing vulnerability in myCred myCred mycred allows Identity Spoofing.This issue affects myC… |
| 2026-10-29 11:17:31 | [CVE-2026-115963](https://nvd.nist.gov/vuln/detail/CVE-2026-115963) | High | 7.1 | Missing Authorization vulnerability in VideoWhisper.com Broadcast Live Video videowhisper-live-streaming-integration al… |
| 2026-10-29 11:17:31 | [CVE-2026-115964](https://nvd.nist.gov/vuln/detail/CVE-2026-115964) | Critical | 9.3 | Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection') vulnerability in StylemixThemes Mo… |
| 2026-10-29 11:17:31 | [CVE-2026-115965](https://nvd.nist.gov/vuln/detail/CVE-2026-115965) | High | 8.5 | Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection') vulnerability in BuddyPress BuddyP… |
| 2026-10-29 11:17:31 | [CVE-2026-115967](https://nvd.nist.gov/vuln/detail/CVE-2026-115967) | High | 8.8 | Weak Authentication vulnerability in Hamid Alinia Login with phone number login-with-phone-number allows Authentication… |
| 2026-10-29 11:17:31 | [CVE-2026-116409](https://nvd.nist.gov/vuln/detail/CVE-2026-116409) | High | 7.1 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in WP Swings Upsell… |
| 2026-10-29 11:17:32 | [CVE-2026-118984](https://nvd.nist.gov/vuln/detail/CVE-2026-118984) | High | 7.0 | OmniRoute 3.8.0 before 3.8.52 contains an unverified password change vulnerability that allows holders of manage- or ad… |
| 2026-10-29 11:17:32 | [CVE-2026-118989](https://nvd.nist.gov/vuln/detail/CVE-2026-118989) | Medium | 5.1 | WebToffee Product Import Export for WooCommerce 2.5.1 before 2.6.8 contains a server-side request forgery vulnerability… |
| 2026-10-29 11:17:32 | [CVE-2026-33923](https://nvd.nist.gov/vuln/detail/CVE-2026-33923) | High | 7.5 | A signature verification vulnerability was discovered in the update installation functionality due to inconsistent vali… |
| 2026-10-29 11:17:33 | [CVE-2026-33924](https://nvd.nist.gov/vuln/detail/CVE-2026-33924) | High | 7.5 | Two OS command injection vulnerabilities were discovered in the update installation functionality due to insufficient v… |
| 2026-10-29 11:17:34 | [CVE-2026-71569](https://nvd.nist.gov/vuln/detail/CVE-2026-71569) | Medium | 4.8 | Server-Side Request Forgery (SSRF) vulnerability in Apache Camel A2A component. This issue affects Apache Camel: from 4… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
