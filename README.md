# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-11-12 21:18 UTC

New CVEs published between 2026-11-12 20:20 UTC and 2026-11-12 21:18 UTC.

[Full CSV](data/new-cves-2026-11-12T21-18-47-724057Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-11-12 21:17:17 | [CVE-2026-106018](https://nvd.nist.gov/vuln/detail/CVE-2026-106018) | High | 8.7 | Authentication bypass using an alternate path or channel vulnerability in Johnson Controls EasyIO FW allows Authenticat… |
| 2026-11-12 21:17:21 | [CVE-2026-126205](https://nvd.nist.gov/vuln/detail/CVE-2026-126205) | Medium | 5.3 | Loofah is a general library for manipulating and transforming HTML/XML documents and fragments, built on top of Nokogir… |
| 2026-11-12 21:17:21 | [CVE-2026-126206](https://nvd.nist.gov/vuln/detail/CVE-2026-126206) | Medium | 5.3 | Loofah is a general library for manipulating and transforming HTML/XML documents and fragments, built on top of Nokogir… |
| 2026-11-12 21:17:21 | [CVE-2026-126207](https://nvd.nist.gov/vuln/detail/CVE-2026-126207) | Medium | 4.7 | Loofah is a general library for manipulating and transforming HTML/XML documents and fragments, built on top of Nokogir… |
| 2026-11-12 21:17:22 | [CVE-2026-126208](https://nvd.nist.gov/vuln/detail/CVE-2026-126208) | Medium | 4.7 | Loofah is a general library for manipulating and transforming HTML/XML documents and fragments, built on top of Nokogir… |
| 2026-11-12 21:17:22 | [CVE-2026-126209](https://nvd.nist.gov/vuln/detail/CVE-2026-126209) | Medium | 5.3 | Loofah is a general library for manipulating and transforming HTML/XML documents and fragments, built on top of Nokogir… |
| 2026-11-12 21:17:22 | [CVE-2026-126793](https://nvd.nist.gov/vuln/detail/CVE-2026-126793) | High | 8.6 | An untrusted search path issue in Aurora PostgreSQL dialect detection in the AWS Advanced Go Wrapper from release 2026-… |
| 2026-11-12 21:17:22 | [CVE-2026-127206](https://nvd.nist.gov/vuln/detail/CVE-2026-127206) | Medium | 6.9 | Image CAPTCHA for Contact Form 7 and WPForms through 3.3.29 contains a CAPTCHA bypass vulnerability that allows unauthe… |
| 2026-11-12 21:17:22 | [CVE-2026-127207](https://nvd.nist.gov/vuln/detail/CVE-2026-127207) | Medium | 5.3 | Sendcloud for WooCommerce through 1.0.41 contains a missing authorization vulnerability that allows authenticated low-p… |
| 2026-11-12 21:17:22 | [CVE-2026-127208](https://nvd.nist.gov/vuln/detail/CVE-2026-127208) | High | 8.6 | datamodel-code-generator before 0.84.0 contains a code injection vulnerability that allows attackers to achieve arbitra… |
| 2026-11-12 21:17:33 | [CVE-2026-86322](https://nvd.nist.gov/vuln/detail/CVE-2026-86322) | High | 8.8 | A flaw was found in Foreman’s Api::V2::PersonalAccessTokensController, where Foreman::Controller::UserAware#find_user r… |
| 2026-11-12 21:17:33 | [CVE-2026-86323](https://nvd.nist.gov/vuln/detail/CVE-2026-86323) | Medium | 4.3 | A flaw was found in Foreman’s Api::V2::MailNotificationsController, where authorization checks on user-specific mail-no… |
| 2026-11-12 21:17:33 | [CVE-2026-86324](https://nvd.nist.gov/vuln/detail/CVE-2026-86324) | Medium | 4.3 | A flaw was found in Foreman’s Api::V2::SshKeysController, where the target user is resolved through Foreman::Controller… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
