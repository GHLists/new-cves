# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-03 14:18 UTC

New CVEs published between 2026-10-03 13:20 UTC and 2026-10-03 14:18 UTC.

[Full CSV](data/new-cves-2026-10-03T14-18-53-130184Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-10-03 14:16:37 | [CVE-2026-105112](https://nvd.nist.gov/vuln/detail/CVE-2026-105112) | Medium | 6.0 | Nezha from 1.8.0 before 2.3.13 contains a lock-order inversion in UpdateGroup and DeleteGroup that allows authenticated… |
| 2026-10-03 14:16:37 | [CVE-2026-105113](https://nvd.nist.gov/vuln/detail/CVE-2026-105113) | High | 7.1 | Nezha Dashboard from 1.8.0 before 2.3.13 contains an improper locking vulnerability where a non-deferred mutex unlock l… |
| 2026-10-03 14:16:37 | [CVE-2026-105114](https://nvd.nist.gov/vuln/detail/CVE-2026-105114) | Medium | 5.3 | OpenAM before 16.1.3 contains a reflected cross-site scripting vulnerability that allows unauthenticated attackers to i… |
| 2026-10-03 14:16:38 | [CVE-2026-105115](https://nvd.nist.gov/vuln/detail/CVE-2026-105115) | High | 8.8 | OpenAM before 16.1.3 contains an unauthenticated arbitrary class instantiation vulnerability in the legacy JAX-RPC SOAP… |
| 2026-10-03 14:16:38 | [CVE-2026-105116](https://nvd.nist.gov/vuln/detail/CVE-2026-105116) | Medium | 5.1 | OpenAM before 16.1.3 contains a latent cross-site scripting defect that places the SAML message, relay state and target… |
| 2026-10-03 14:16:38 | [CVE-2026-105117](https://nvd.nist.gov/vuln/detail/CVE-2026-105117) | Medium | 5.3 | OpenAM before 16.1.3 contains an email content injection vulnerability that allows unauthenticated attackers to control… |
| 2026-10-03 14:16:38 | [CVE-2026-105118](https://nvd.nist.gov/vuln/detail/CVE-2026-105118) | Low | 2.3 | OpenAM before 16.1.3 contains an open redirect vulnerability that allows unauthenticated attackers to redirect users by… |
| 2026-10-03 14:16:38 | [CVE-2026-105119](https://nvd.nist.gov/vuln/detail/CVE-2026-105119) | High | 7.6 | OpenAM before 16.1.3 applies its OAuth2 Provider PKCE enforcement only to authorization requests whose response_type is… |
| 2026-10-03 14:16:38 | [CVE-2026-105120](https://nvd.nist.gov/vuln/detail/CVE-2026-105120) | Medium | 6.9 | OpenAM before 16.1.3 contains an authorization bypass vulnerability in the sessions REST endpoint query operation that… |
| 2026-10-03 14:16:38 | [CVE-2026-105121](https://nvd.nist.gov/vuln/detail/CVE-2026-105121) | Medium | 6.9 | OpenAM before 16.1.3 contains an improper authorization vulnerability that allows delegated administrators to destroy s… |
| 2026-10-03 14:16:39 | [CVE-2026-105122](https://nvd.nist.gov/vuln/detail/CVE-2026-105122) | Medium | 5.3 | OpenAM before 16.1.3 contains a server-side request forgery vulnerability that allows attackers able to register or mod… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
