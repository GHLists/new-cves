# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-11-04 09:18 UTC

New CVEs published between 2026-11-04 08:18 UTC and 2026-11-04 09:18 UTC.

[Full CSV](data/new-cves-2026-11-04T09-18-19-566809Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-11-04 09:17:40 | [CVE-2026-114420](https://nvd.nist.gov/vuln/detail/CVE-2026-114420) | Medium | 6.9 | SEPPmail Secure Email Gateway before 15.1.1 does not neutralize LDAP metacharacters in an unauthenticated account-selec… |
| 2026-11-04 09:17:41 | [CVE-2026-114421](https://nvd.nist.gov/vuln/detail/CVE-2026-114421) | High | 8.3 | SEPPmail Secure Email Gateway before 15.1.1 permits password recovery for a created but unregistered GINA account whose… |
| 2026-11-04 09:17:41 | [CVE-2026-114424](https://nvd.nist.gov/vuln/detail/CVE-2026-114424) | Critical | 9.2 | SEPPmail Secure Email Gateway before 15.1.1 can evaluate attacker-influenced replacement text as Perl code in sender or… |
| 2026-11-04 09:17:41 | [CVE-2026-114425](https://nvd.nist.gov/vuln/detail/CVE-2026-114425) | Critical | 9.2 | SEPPmail Secure Email Gateway before 15.1.1 trusts a file path supplied in externally provided Large File Transfer atta… |
| 2026-11-04 09:17:41 | [CVE-2026-114426](https://nvd.nist.gov/vuln/detail/CVE-2026-114426) | High | 8.7 | SEPPmail Secure Email Gateway before 15.1.1 processes and writes v1 file-interface upload data before authenticating th… |
| 2026-11-04 09:17:42 | [CVE-2026-19721](https://nvd.nist.gov/vuln/detail/CVE-2026-19721) | Low | 3.3 | Improper restriction of XML external entity reference vulnerability in TÜBİTAK BİLGEM Software Technologies Research In… |
| 2026-11-04 09:17:42 | [CVE-2026-19731](https://nvd.nist.gov/vuln/detail/CVE-2026-19731) | Low | 3.3 | Improper Limitation of a Pathname to a Restricted Directory ('Path Traversal') vulnerability in TÜBİTAK BİLGEM Software… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
