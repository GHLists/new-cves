# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-27 08:19 UTC

New CVEs published between 2026-10-27 07:19 UTC and 2026-10-27 08:19 UTC.

[Full CSV](data/new-cves-2026-10-27T08-19-28-392683Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-10-27 08:16:52 | [CVE-2026-101034](https://nvd.nist.gov/vuln/detail/CVE-2026-101034) | Medium | 6.8 | An attacker who obtained the hardcoded key could decrypt domain/service account passwords, task run-as credentials, and… |
| 2026-10-27 08:16:52 | [CVE-2026-107472](https://nvd.nist.gov/vuln/detail/CVE-2026-107472) | Medium | 4.3 | An out-of-bounds read vulnerability in the QTextCodec TSCII encoding of the Qt 5 Compatibility APIs module (Qt Core in… |
| 2026-10-27 08:16:52 | [CVE-2026-10511](https://nvd.nist.gov/vuln/detail/CVE-2026-10511) | Medium | 6.4 | The Jupiter X Core plugin for WordPress is vulnerable to Stored Cross-Site Scripting via the 'forget_password_link' par… |
| 2026-10-27 08:16:52 | [CVE-2026-111459](https://nvd.nist.gov/vuln/detail/CVE-2026-111459) | High | 7.6 | An improper certificate validation vulnerability exists in Moxa Remote Connect Suite (MRC Client). Under certain condit… |
| 2026-10-27 08:16:53 | [CVE-2026-111460](https://nvd.nist.gov/vuln/detail/CVE-2026-111460) | High | 7.7 | A hard-coded cryptographic key vulnerability exists in the OnCell G3150A-LTE Series. Under certain conditions, an unaut… |
| 2026-10-27 08:16:53 | [CVE-2026-111461](https://nvd.nist.gov/vuln/detail/CVE-2026-111461) | High | 7.5 | An OS command injection vulnerability exists in OnCell G3150A-LTE Series. When the SMS management functionality is enab… |
| 2026-10-27 08:16:53 | [CVE-2026-16521](https://nvd.nist.gov/vuln/detail/CVE-2026-16521) | High | 7.2 | An OS command injection vulnerability exists because of insufficient input filtering. An attacker can inject a command… |
| 2026-10-27 08:16:53 | [CVE-2026-18449](https://nvd.nist.gov/vuln/detail/CVE-2026-18449) | High | 7.5 | The BMC does not correctly enforce integrity and encryption requirements for IPMI commands. An attacker may be able to… |
| 2026-10-27 08:16:53 | [CVE-2026-18450](https://nvd.nist.gov/vuln/detail/CVE-2026-18450) | Critical | 9.8 | The BMC does not correctly enforce integrity and encryption requirements for IPMI commands. An attacker may be able to… |
| 2026-10-27 08:16:53 | [CVE-2026-18451](https://nvd.nist.gov/vuln/detail/CVE-2026-18451) | Low | 3.1 | The HTML5 KVM-over-IP console authenticates with a token returned by the web interface. Weaknesses in token generation… |
| 2026-10-27 08:16:54 | [CVE-2026-65210](https://nvd.nist.gov/vuln/detail/CVE-2026-65210) | Medium | 4.9 | This issue may allow an authenticated IPMI Administrator to read arbitrary files from the BMC filesystem, disclosing ma… |
| 2026-10-27 08:16:54 | [CVE-2026-65219](https://nvd.nist.gov/vuln/detail/CVE-2026-65219) | High | 7.4 | A flaw in the BMC RAKP+ implementation may allow an attacker to send a request followed by a specially crafted RAKP mes… |
| 2026-10-27 08:16:54 | [CVE-2026-65220](https://nvd.nist.gov/vuln/detail/CVE-2026-65220) | High | 8.8 | A logic flaw in the BMC IPMI implementation may allow an attacker to send specially crafted RAKP+ messages and escalate… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
