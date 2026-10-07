# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-07 22:18 UTC

New CVEs published between 2026-10-07 21:18 UTC and 2026-10-07 22:18 UTC.

[Full CSV](data/new-cves-2026-10-07T22-18-37-744721Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-10-07 22:17:02 | [CVE-2026-105816](https://nvd.nist.gov/vuln/detail/CVE-2026-105816) | High | 8.0 | Vault and Vault Enterprise did not consistently verify that stored plugin catalog entries reference binaries within the… |
| 2026-10-07 22:17:02 | [CVE-2026-105818](https://nvd.nist.gov/vuln/detail/CVE-2026-105818) | Medium | 5.9 | Vault's PKI secrets engine ACME server did not restrict certificate identities that ACME challenges do not validate whe… |
| 2026-10-07 22:17:02 | [CVE-2026-105820](https://nvd.nist.gov/vuln/detail/CVE-2026-105820) | Medium | 5.4 | Vault's ACL policy cache allowed namespace traversal when policy names contained path traversal constructs. This may al… |
| 2026-10-07 22:17:03 | [CVE-2026-107230](https://nvd.nist.gov/vuln/detail/CVE-2026-107230) | High | 7.4 | The AsyncHttpClient (AHC) library allows Java applications to easily execute HTTP requests and asynchronously process H… |
| 2026-10-07 22:17:03 | [CVE-2026-107231](https://nvd.nist.gov/vuln/detail/CVE-2026-107231) | High | 8.7 | The AsyncHttpClient (AHC) library allows Java applications to easily execute HTTP requests and asynchronously process H… |
| 2026-10-07 22:17:03 | [CVE-2026-107232](https://nvd.nist.gov/vuln/detail/CVE-2026-107232) | High | 7.5 | The AsyncHttpClient (AHC) library allows Java applications to easily execute HTTP requests and asynchronously process H… |
| 2026-10-07 22:17:03 | [CVE-2026-107279](https://nvd.nist.gov/vuln/detail/CVE-2026-107279) | High | 8.8 | The AsyncHttpClient (AHC) library allows Java applications to easily execute HTTP requests and asynchronously process H… |
| 2026-10-07 22:17:03 | [CVE-2026-107280](https://nvd.nist.gov/vuln/detail/CVE-2026-107280) | Medium | 6.9 | The AsyncHttpClient (AHC) library allows Java applications to easily execute HTTP requests and asynchronously process H… |
| 2026-10-07 22:17:03 | [CVE-2026-107281](https://nvd.nist.gov/vuln/detail/CVE-2026-107281) | High | 7.6 | The AsyncHttpClient (AHC) library allows Java applications to easily execute HTTP requests and asynchronously process H… |
| 2026-10-07 22:17:04 | [CVE-2026-107282](https://nvd.nist.gov/vuln/detail/CVE-2026-107282) | Critical | 9.4 | The AsyncHttpClient (AHC) library allows Java applications to easily execute HTTP requests and asynchronously process H… |
| 2026-10-07 22:17:04 | [CVE-2026-107283](https://nvd.nist.gov/vuln/detail/CVE-2026-107283) | Low | 3.7 | The AsyncHttpClient (AHC) library allows Java applications to easily execute HTTP requests and asynchronously process H… |
| 2026-10-07 22:17:04 | [CVE-2026-107284](https://nvd.nist.gov/vuln/detail/CVE-2026-107284) | Low | 3.7 | The AsyncHttpClient (AHC) library allows Java applications to easily execute HTTP requests and asynchronously process H… |
| 2026-10-07 22:17:04 | [CVE-2026-107285](https://nvd.nist.gov/vuln/detail/CVE-2026-107285) | Medium | 5.9 | The AsyncHttpClient (AHC) library allows Java applications to easily execute HTTP requests and asynchronously process H… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
