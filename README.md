# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-29 13:20 UTC

New CVEs published between 2026-10-29 12:19 UTC and 2026-10-29 13:20 UTC.

[Full CSV](data/new-cves-2026-10-29T13-20-45-475778Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-10-29 13:17:04 | [CVE-2026-113688](https://nvd.nist.gov/vuln/detail/CVE-2026-113688) | Medium | 5.3 | Server-side request forgery in the SmartIT URL-based attachment feature of BMC IT Service Management Suite versions 25.… |
| 2026-10-29 13:17:04 | [CVE-2026-113689](https://nvd.nist.gov/vuln/detail/CVE-2026-113689) | Medium | 5.1 | Stored cross-site scripting in the SmartIT work-notes feature of BMC IT Service Management Suite versions 25.3.01, 25.4… |
| 2026-10-29 13:17:04 | [CVE-2026-113690](https://nvd.nist.gov/vuln/detail/CVE-2026-113690) | Medium | 4.8 | Stored cross-site scripting in the SmartIT attachment feature of BMC IT Service Management Suite versions 25.3.01, 25.4… |
| 2026-10-29 13:17:08 | [CVE-2026-118087](https://nvd.nist.gov/vuln/detail/CVE-2026-118087) | Medium | 6.5 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in Gemini Labs Site… |
| 2026-10-29 13:17:08 | [CVE-2026-118093](https://nvd.nist.gov/vuln/detail/CVE-2026-118093) | Medium | 5.3 | Missing Authorization vulnerability in WPFunnels Team Product Feed Manager best-woocommerce-feed allows Exploiting Inco… |
| 2026-10-29 13:17:08 | [CVE-2026-118094](https://nvd.nist.gov/vuln/detail/CVE-2026-118094) | Medium | 6.5 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in Igor Funa Ad Inse… |
| 2026-10-29 13:17:10 | [CVE-2026-22386](https://nvd.nist.gov/vuln/detail/CVE-2026-22386) | Medium | 4.3 | Missing Authorization vulnerability in Ahmad WP Job Portal wp-job-portal allows Exploiting Incorrectly Configured Acces… |
| 2026-10-29 13:17:10 | [CVE-2026-24533](https://nvd.nist.gov/vuln/detail/CVE-2026-24533) | Medium | 6.5 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in CozyThemes Cozy B… |
| 2026-10-29 13:17:11 | [CVE-2026-39735](https://nvd.nist.gov/vuln/detail/CVE-2026-39735) | Medium | 6.5 | Missing Authorization vulnerability in Crocoblock JetEngine jet-engine allows Exploiting Incorrectly Configured Access… |
| 2026-10-29 13:17:11 | [CVE-2026-39741](https://nvd.nist.gov/vuln/detail/CVE-2026-39741) | Medium | 5.3 | Missing Authorization vulnerability in RelyWP Simple Cloudflare Turnstile simple-cloudflare-turnstile allows Exploiting… |
| 2026-10-29 13:17:11 | [CVE-2026-42703](https://nvd.nist.gov/vuln/detail/CVE-2026-42703) | Medium | 6.5 | Missing Authorization vulnerability in Kaliforms Kali Forms kali-forms allows Exploiting Incorrectly Configured Access… |
| 2026-10-29 13:17:12 | [CVE-2026-48196](https://nvd.nist.gov/vuln/detail/CVE-2026-48196) | Medium | 6.5 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in Kaliforms Kali Fo… |
| 2026-10-29 13:17:12 | [CVE-2026-49142](https://nvd.nist.gov/vuln/detail/CVE-2026-49142) | High | 8.7 | OpenEMR before 8.5.0 contains an authenticated SQL injection vulnerability in the Syndromic Surveillance module that al… |
| 2026-10-29 13:17:13 | [CVE-2026-52709](https://nvd.nist.gov/vuln/detail/CVE-2026-52709) | Medium | 6.5 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in bPlugins Video Ga… |
| 2026-10-29 13:17:13 | [CVE-2026-56056](https://nvd.nist.gov/vuln/detail/CVE-2026-56056) | Medium | 6.5 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in Mamunur Rashid Th… |
| 2026-10-29 13:17:15 | [CVE-2026-93006](https://nvd.nist.gov/vuln/detail/CVE-2026-93006) | Medium | 6.8 | A flaw was found in dnsmasq. The TFTP server can serve the wrong file contents because a recently used transfer cache i… |
| 2026-10-29 13:17:15 | [CVE-2026-93007](https://nvd.nist.gov/vuln/detail/CVE-2026-93007) | Medium | 5.3 | A flaw was found in dnsmasq. The TCP DNS service uses a small fixed pool of child processes and does not set a receive… |
| 2026-10-29 13:17:16 | [CVE-2026-93008](https://nvd.nist.gov/vuln/detail/CVE-2026-93008) | Medium | 6.8 | A flaw was found in dnsmasq. When following a CNAME in a DNS response, the resolver can cache records for the CNAME tar… |
| 2026-10-29 13:17:16 | [CVE-2026-93011](https://nvd.nist.gov/vuln/detail/CVE-2026-93011) | Medium | 5.3 | A flaw was found in dnsmasq. After a reduction of internal domain-name buffer sizes, the DNSSEC validator can write a f… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
