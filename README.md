# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-11-02 01:19 UTC

New CVEs published between 2026-11-02 00:20 UTC and 2026-11-02 01:19 UTC.

[Full CSV](data/new-cves-2026-11-02T01-19-33-416047Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-11-02 01:17:26 | [CVE-2026-120279](https://nvd.nist.gov/vuln/detail/CVE-2026-120279) | Critical | 9.3 | A flaw has been found in WAVLINK WN536AX6-A V260507. The affected element is an unknown function of the file /protocol.… |
| 2026-11-02 01:17:26 | [CVE-2026-120280](https://nvd.nist.gov/vuln/detail/CVE-2026-120280) | Critical | 9.3 | A vulnerability has been found in WAVLINK WN536AX6-A V260507. The impacted element is the function wireguard_cli_group… |
| 2026-11-02 01:17:27 | [CVE-2026-120281](https://nvd.nist.gov/vuln/detail/CVE-2026-120281) | Critical | 9.3 | A vulnerability was found in WAVLINK WN536AX6-A V260507. This affects the function strcpy of the file /protocol.csp of… |
| 2026-11-02 01:17:27 | [CVE-2026-120282](https://nvd.nist.gov/vuln/detail/CVE-2026-120282) | High | 8.6 | A vulnerability was determined in WAVLINK WN536AX6-A V260507. This impacts the function host_black of the file /protoco… |
| 2026-11-02 01:17:27 | [CVE-2026-120283](https://nvd.nist.gov/vuln/detail/CVE-2026-120283) | Critical | 9.3 | A vulnerability was identified in Linksys E8450 1.2.00.360516. Affected is the function strcpy of the file /www/cgi-bin… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
