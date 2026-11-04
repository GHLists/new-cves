# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-11-04 10:21 UTC

New CVEs published between 2026-11-04 09:18 UTC and 2026-11-04 10:21 UTC.

[Full CSV](data/new-cves-2026-11-04T10-21-51-768005Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-11-04 10:17:24 | [CVE-2026-108949](https://nvd.nist.gov/vuln/detail/CVE-2026-108949) |  |  | Denial of Service via OOM vulnerability in Apache ActiveMQ, ActiveMQ Broker. An authenticated OpenWire client that send… |
| 2026-11-04 10:17:24 | [CVE-2026-110021](https://nvd.nist.gov/vuln/detail/CVE-2026-110021) | Medium | 6.9 | PLCnext Engineer checks GSDX manifest reference digests but does not cryptographically verify the XML `SignatureValue`… |
| 2026-11-04 10:17:24 | [CVE-2026-110022](https://nvd.nist.gov/vuln/detail/CVE-2026-110022) | High | 8.6 | The PFI plugin framework deploys executable assemblies (DLLs) from a signed plugin package into the local plugin reposi… |
| 2026-11-04 10:17:24 | [CVE-2026-110935](https://nvd.nist.gov/vuln/detail/CVE-2026-110935) | High | 8.6 | The PFI plugin framework deployment routine does not validate path components when extracting archive entries to the lo… |
| 2026-11-04 10:17:24 | [CVE-2026-111036](https://nvd.nist.gov/vuln/detail/CVE-2026-111036) | High | 8.4 | Server-side request forgery (SSRF) vulnerability in the Coupa Supplier Portal SaaS platform, specifically in the docume… |
| 2026-11-04 10:17:24 | [CVE-2026-111037](https://nvd.nist.gov/vuln/detail/CVE-2026-111037) | Medium | 5.1 | A reflected Cross-Site Scripting (XSS) vulnerability in the Tenders module of the Coupa Supplier Portal SaaS platform.… |
| 2026-11-04 10:17:25 | [CVE-2026-111038](https://nvd.nist.gov/vuln/detail/CVE-2026-111038) | High | 7.3 | CSV formula injection vulnerability in the export functionality of the Coupa Supplier Portal SaaS platform. The vulnera… |
| 2026-11-04 10:17:25 | [CVE-2026-111040](https://nvd.nist.gov/vuln/detail/CVE-2026-111040) | Medium | 5.1 | The platform allows persistent HTML injection into editable fields managed by TinyMCE. An authenticated attacker with l… |
| 2026-11-04 10:17:25 | [CVE-2026-111821](https://nvd.nist.gov/vuln/detail/CVE-2026-111821) |  |  | Improper input validation vulnerability in Apache ActiveMQ, Apache ActiveMQ KahaDB. A user can create a durable subscri… |
| 2026-11-04 10:17:25 | [CVE-2026-111822](https://nvd.nist.gov/vuln/detail/CVE-2026-111822) |  |  | Improper invalidation of cached authorizations vulnerability in Apache ActiveMQ, Apache ActiveMQ Runtime Config. After… |
| 2026-11-04 10:17:25 | [CVE-2026-115498](https://nvd.nist.gov/vuln/detail/CVE-2026-115498) | High | 7.2 | The Slim Jetpack plugin for WordPress is vulnerable to Stored Cross-Site Scripting via the 'g<PAGE_ID>-website (Website… |
| 2026-11-04 10:17:26 | [CVE-2026-120422](https://nvd.nist.gov/vuln/detail/CVE-2026-120422) | High | 8.9 | Sogou Input Method for Windows contains a vulnerability in the configuration retrieval mechanism of its SGTool.exe comp… |
| 2026-11-04 10:17:26 | [CVE-2026-120554](https://nvd.nist.gov/vuln/detail/CVE-2026-120554) | High | 8.8 | The Import and export users and customers plugin for WordPress is vulnerable to Privilege Escalation in all versions up… |
| 2026-11-04 10:17:26 | [CVE-2026-93900](https://nvd.nist.gov/vuln/detail/CVE-2026-93900) | Medium | 6.4 | The Simple CAPTCHA with Cloudflare Turnstile plugin for WordPress is vulnerable to Stored Cross-Site Scripting via the… |
| 2026-11-04 10:17:26 | [CVE-2026-94459](https://nvd.nist.gov/vuln/detail/CVE-2026-94459) | High | 7.2 | IRISPowerscan contain default user accounts with predictable credentials. An unauthenticated attacker with access to an… |
| 2026-11-04 10:17:26 | [CVE-2026-94460](https://nvd.nist.gov/vuln/detail/CVE-2026-94460) | High | 7.2 | IRISPowerscan contain an insecure default configuration where the built-in installation account is assigned elevated pr… |
| 2026-11-04 10:17:27 | [CVE-2026-95649](https://nvd.nist.gov/vuln/detail/CVE-2026-95649) | Medium | 6.1 | IRISPowerscan insufficiently restrict the use of untrusted scripts. An authenticated user with access to script functio… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
