# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-11-03 02:18 UTC

New CVEs published between 2026-11-03 01:18 UTC and 2026-11-03 02:18 UTC.

[Full CSV](data/new-cves-2026-11-03T02-18-22-793306Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-11-03 02:16:52 | [CVE-2026-107441](https://nvd.nist.gov/vuln/detail/CVE-2026-107441) | High | 8.8 | An out-of-bounds write vulnerability in the CGI program of Zyxel GS1900-24E firmware versions through 2.90(AAHK.2)C0 co… |
| 2026-11-03 02:16:53 | [CVE-2026-120831](https://nvd.nist.gov/vuln/detail/CVE-2026-120831) | Medium | 6.5 | A flaw was found in libslirp in if_output(). When moving a session from the fast queue to the batch queue, the code unl… |
| 2026-11-03 02:16:53 | [CVE-2026-76955](https://nvd.nist.gov/vuln/detail/CVE-2026-76955) | High | 8.8 | A buffer overflow vulnerability in the zdp_wtp binary in Zyxel NWA110AX firmware versions through 7.12(ABTG.0)C0 could… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
