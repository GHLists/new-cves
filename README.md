# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-20 03:19 UTC

New CVEs published between 2026-10-20 02:18 UTC and 2026-10-20 03:19 UTC.

[Full CSV](data/new-cves-2026-10-20T03-19-02-010121Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-10-20 03:17:15 | [CVE-2026-12489](https://nvd.nist.gov/vuln/detail/CVE-2026-12489) | Medium | 6.5 | An incorrect authorization vulnerability in the Data Access Layer (DAL) of Zyxel EX3501-T0 firmware versions through 5.… |
| 2026-10-20 03:17:16 | [CVE-2026-86467](https://nvd.nist.gov/vuln/detail/CVE-2026-86467) |  |  | Apache Airflow Amazon provider: the AWS auth manager's SAML login flow does not bind the authentication response to the… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
