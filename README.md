# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-09-27 17:20 UTC

New CVEs published between 2026-09-27 16:18 UTC and 2026-09-27 17:20 UTC.

[Full CSV](data/new-cves-2026-09-27T17-20-42-329928Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-09-27 17:16:55 | [CVE-2026-101042](https://nvd.nist.gov/vuln/detail/CVE-2026-101042) | High | 7.4 | Parse Server is an open-source backend server. In versions >= 9.0.0 < 9.10.1-alpha.10 and >= 8.0.2 < 8.6.91, the code-b… |
| 2026-09-27 17:16:55 | [CVE-2026-101049](https://nvd.nist.gov/vuln/detail/CVE-2026-101049) | High | 8.3 | Heym before 0.0.53 fails to verify Slack request signatures when trigger nodes lack credential IDs or have empty signin… |
| 2026-09-27 17:16:56 | [CVE-2026-101050](https://nvd.nist.gov/vuln/detail/CVE-2026-101050) | High | 8.3 | Heym before 0.0.53 fails to verify the X-Telegram-Bot-Api-Secret-Token header on Telegram webhook endpoints when creden… |
| 2026-09-27 17:16:56 | [CVE-2026-88771](https://nvd.nist.gov/vuln/detail/CVE-2026-88771) | Critical | 9.5 | Improper input validation vulnerability in Citrix NetScaler ADC and Citrix NetScaler Gateway. This issue affects ADC: b… |
| 2026-09-27 17:16:56 | [CVE-2026-88772](https://nvd.nist.gov/vuln/detail/CVE-2026-88772) | Critical | 9.5 | Vulnerability in Citrix NetScaler ADC and Citrix NetScaler Gateway. This issue affects ADC: before 14.1-73.37, before 1… |
| 2026-09-27 17:16:56 | [CVE-2026-88773](https://nvd.nist.gov/vuln/detail/CVE-2026-88773) | Critical | 9.3 | Inconsistent interpretation of HTTP requests ('HTTP Request/Response smuggling') vulnerability in Citrix NetScaler ADC… |
| 2026-09-27 17:16:56 | [CVE-2026-88774](https://nvd.nist.gov/vuln/detail/CVE-2026-88774) | High | 7.0 | Vulnerability in Citrix NetScaler ADC and Citrix NetScaler Gateway. This issue affects ADC: before 14.1-73.37, before 1… |
| 2026-09-27 17:16:56 | [CVE-2026-88775](https://nvd.nist.gov/vuln/detail/CVE-2026-88775) | High | 8.8 | Memory overflow vulnerability in Citrix NetScaler ADC and Citrix NetScaler Gateway. This issue affects ADC: before 14.1… |
| 2026-09-27 17:16:56 | [CVE-2026-88776](https://nvd.nist.gov/vuln/detail/CVE-2026-88776) | High | 8.8 | Memory overflow vulnerability vulnerability in Citrix NetScaler ADC and Citrix NetScaler Gateway. This issue affects AD… |
| 2026-09-27 17:16:56 | [CVE-2026-88777](https://nvd.nist.gov/vuln/detail/CVE-2026-88777) | High | 8.8 | Memory overflow vulnerability vulnerability in Citrix NetScaler ADC and Citrix NetScaler Gateway. This issue affects AD… |
| 2026-09-27 17:16:57 | [CVE-2026-88778](https://nvd.nist.gov/vuln/detail/CVE-2026-88778) | High | 8.8 | Predictable exact value from previous values vulnerability in Citrix NetScaler ADC and Citrix NetScaler Gateway. This i… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
