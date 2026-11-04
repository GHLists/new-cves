# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-11-04 07:18 UTC

New CVEs published between 2026-11-04 06:18 UTC and 2026-11-04 07:18 UTC.

[Full CSV](data/new-cves-2026-11-04T07-18-18-85584Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-11-04 07:17:11 | [CVE-2026-121816](https://nvd.nist.gov/vuln/detail/CVE-2026-121816) | High | 8.7 | Herowatch Mini developed by About Time Technologies has a Missing Authentication vulnerability. Unauthenticated remote… |
| 2026-11-04 07:17:12 | [CVE-2026-121817](https://nvd.nist.gov/vuln/detail/CVE-2026-121817) | High | 8.7 | Herowatch Go Server developed by About Time Technologies has a Insecure Direct Object Reference vulnerability. Authenti… |
| 2026-11-04 07:17:12 | [CVE-2026-121818](https://nvd.nist.gov/vuln/detail/CVE-2026-121818) | High | 8.5 | Herowatch Mini developed by About Time Technologies has a system signing vulnerability. Authenticated local attackers c… |
| 2026-11-04 07:17:12 | [CVE-2026-54851](https://nvd.nist.gov/vuln/detail/CVE-2026-54851) | High | 7.1 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in Awesomemotive Con… |
| 2026-11-04 07:17:12 | [CVE-2026-62000](https://nvd.nist.gov/vuln/detail/CVE-2026-62000) | High | 7.5 | Missing Authorization vulnerability in WC Lovers WCFM Marketplace wc-multivendor-marketplace allows Exploiting Incorrec… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
