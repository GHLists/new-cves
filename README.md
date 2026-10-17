# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-17 02:18 UTC

New CVEs published between 2026-10-17 01:19 UTC and 2026-10-17 02:18 UTC.

[Full CSV](data/new-cves-2026-10-17T02-18-45-571822Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-10-17 02:17:18 | [CVE-2026-111823](https://nvd.nist.gov/vuln/detail/CVE-2026-111823) | Critical | 9.8 | Mage OSS through 0.9.80 before 76c4f46 can proceed with session creation upon encountering an unknown OAuth provider. |
| 2026-10-17 02:17:18 | [CVE-2026-111853](https://nvd.nist.gov/vuln/detail/CVE-2026-111853) | High | 8.8 | An issue was discovered on Tektronix 3 Series MDO devices before 1.21.1. An OS command injection vulnerability exists i… |
| 2026-10-17 02:17:18 | [CVE-2026-111854](https://nvd.nist.gov/vuln/detail/CVE-2026-111854) | High | 8.1 | An issue was discovered on Tektronix 3 Series MDO devices before 1.21.1. A path traversal vulnerability in the SCPI FIL… |
| 2026-10-17 02:17:18 | [CVE-2026-111855](https://nvd.nist.gov/vuln/detail/CVE-2026-111855) | High | 7.5 | An issue was discovered on Tektronix 3 Series MDO devices before 1.21.1. A path traversal vulnerability exists in the w… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
