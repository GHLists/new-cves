# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-01 14:18 UTC

New CVEs published between 2026-10-01 13:18 UTC and 2026-10-01 14:18 UTC.

[Full CSV](data/new-cves-2026-10-01T14-18-37-633558Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-10-01 14:17:20 | [CVE-2026-102504](https://nvd.nist.gov/vuln/detail/CVE-2026-102504) |  |  | Imager versions before 1.037 for Perl exit the process reading a raw image with an out-of-range raw_datachannels value… |
| 2026-10-01 14:17:20 | [CVE-2026-102505](https://nvd.nist.gov/vuln/detail/CVE-2026-102505) |  |  | Imager versions before 1.037 for Perl overflow a heap buffer fetching float samples from a paletted image in i_gsampf_f… |
| 2026-10-01 14:17:28 | [CVE-2026-103686](https://nvd.nist.gov/vuln/detail/CVE-2026-103686) | Low | 2.0 | A flaw has been found in rhukster dom-sanitizer up to 1.0.15. Impacted is the function DOMSanitizer::isDangerousUrl of… |
| 2026-10-01 14:17:29 | [CVE-2026-66246](https://nvd.nist.gov/vuln/detail/CVE-2026-66246) | High | 8.8 | iControl is affected by a Broken Access Control vulnerability, which could allow an attacker to exploit missing authent… |
| 2026-10-01 14:17:29 | [CVE-2026-66247](https://nvd.nist.gov/vuln/detail/CVE-2026-66247) | Medium | 4.3 | iControl is affected by an insecure Cross-Origin Resource Sharing (CORS) policy vulnerability, which could allow a mali… |
| 2026-10-01 14:17:30 | [CVE-2026-66248](https://nvd.nist.gov/vuln/detail/CVE-2026-66248) | Low | 3.1 | iControl is affected by an Improper Error Handling vulnerability, which could allow an unauthenticated attacker to trig… |
| 2026-10-01 14:17:30 | [CVE-2026-66249](https://nvd.nist.gov/vuln/detail/CVE-2026-66249) | Low | 3.1 | iControl is affected by a Missing Secure Attribute vulnerability, which could allow an attacker to intercept cookies tr… |
| 2026-10-01 14:17:30 | [CVE-2026-66253](https://nvd.nist.gov/vuln/detail/CVE-2026-66253) | Low | 3.1 | iControl is affected by a Session Timeout vulnerability, which could allow an attacker to exploit an unattended or aban… |
| 2026-10-01 14:17:30 | [CVE-2026-79901](https://nvd.nist.gov/vuln/detail/CVE-2026-79901) | Critical | 9.9 | In deployments using BoKS keytab management, affected versions of boks_keytabmd generate Active Directory service-accou… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
