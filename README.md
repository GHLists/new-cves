# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-08 07:19 UTC

New CVEs published between 2026-10-08 06:18 UTC and 2026-10-08 07:19 UTC.

[Full CSV](data/new-cves-2026-10-08T07-19-52-487397Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-10-08 07:16:31 | [CVE-2026-85097](https://nvd.nist.gov/vuln/detail/CVE-2026-85097) | Critical | 9.8 | The Bricksforge plugin for WordPress is vulnerable to unauthenticated arbitrary file upload in versions up to, and incl… |
| 2026-10-08 07:16:31 | [CVE-2026-85421](https://nvd.nist.gov/vuln/detail/CVE-2026-85421) | High | 8.7 | A critical security vulnerability has been identified in Brocade ASCG versions before 3.5.0. The HTTPS service fails to… |
| 2026-10-08 07:16:32 | [CVE-2026-85422](https://nvd.nist.gov/vuln/detail/CVE-2026-85422) | High | 8.4 | A vulnerability in Brocade ASCG version before 3.5.0 could allow an attacker to obtain a static cryptographic key hardc… |
| 2026-10-08 07:16:32 | [CVE-2026-85423](https://nvd.nist.gov/vuln/detail/CVE-2026-85423) | High | 8.6 | A vulnerability has been identified in the data collection service of Brocade ASCG versions before 3.5.0. An API endpoi… |
| 2026-10-08 07:16:32 | [CVE-2026-85486](https://nvd.nist.gov/vuln/detail/CVE-2026-85486) | High | 8.6 | Brocade ASCG before 3.5.0 improperly processes user input by evaluating form data prior to validation. When an authenti… |
| 2026-10-08 07:16:32 | [CVE-2026-85487](https://nvd.nist.gov/vuln/detail/CVE-2026-85487) | High | 8.6 | A path traversal vulnerability exists in the HTTP service component of Brocade ASCG versions before 3.5.0. An unauthent… |
| 2026-10-08 07:16:32 | [CVE-2026-85488](https://nvd.nist.gov/vuln/detail/CVE-2026-85488) | High | 7.0 | Brocade ASCG before 3.5.0 has a well-known Brocade default password embedded in a script distributed to every customer.… |
| 2026-10-08 07:16:32 | [CVE-2026-85489](https://nvd.nist.gov/vuln/detail/CVE-2026-85489) | High | 8.7 | An authentication flaw exists in the Brocade ASCG administrative management service component. An unauthenticated netwo… |
| 2026-10-08 07:16:32 | [CVE-2026-85490](https://nvd.nist.gov/vuln/detail/CVE-2026-85490) | High | 7.7 | When Brocade ASCG before 3.5.0 processes support bundle archives ingested from remote compromised endpoints, the applic… |
| 2026-10-08 07:16:33 | [CVE-2026-87425](https://nvd.nist.gov/vuln/detail/CVE-2026-87425) | High | 7.6 | An unauthenticated remote attacker can modify the TLS client trust store in Brocade ASCG versions before 3.5.0. By supp… |
| 2026-10-08 07:16:33 | [CVE-2026-87426](https://nvd.nist.gov/vuln/detail/CVE-2026-87426) | Medium | 5.3 | An unauthenticated network-based attacker can query specific internal management endpoints on Brocade ASCG versions bef… |
| 2026-10-08 07:16:33 | [CVE-2026-87428](https://nvd.nist.gov/vuln/detail/CVE-2026-87428) | High | 8.4 | In Brocade ASCG before 3.5.0, a local unauthorized user on the ASCG VM who can issue a request to the SANnav host netwo… |
| 2026-10-08 07:16:33 | [CVE-2026-87424](https://nvd.nist.gov/vuln/detail/CVE-2026-87424) | High | 8.6 | A vulnerability in the SupportLink API authentication component of Brocade ASCG versions prior to 3.5.0 allows an attac… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
