# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-02 22:18 UTC

New CVEs published between 2026-10-02 21:18 UTC and 2026-10-02 22:18 UTC.

[Full CSV](data/new-cves-2026-10-02T22-18-54-111005Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-10-02 22:16:54 | [CVE-2026-104886](https://nvd.nist.gov/vuln/detail/CVE-2026-104886) |  |  | Rejected reason: ** REJECT ** DO NOT USE THIS CANDIDATE NUMBER. ConsultIDs: CVE-2026-78410. Reason: This candidate is a… |
| 2026-10-02 22:16:54 | [CVE-2026-104887](https://nvd.nist.gov/vuln/detail/CVE-2026-104887) |  |  | Rejected reason: ** REJECT ** DO NOT USE THIS CANDIDATE NUMBER. ConsultIDs: CVE-2026-78409. Reason: This candidate is a… |
| 2026-10-02 22:16:54 | [CVE-2026-105043](https://nvd.nist.gov/vuln/detail/CVE-2026-105043) | Low | 3.6 | MathWorks Simulink before R2026b, when showing a crafted .slx file, can have blocks that are never visible in the Simul… |
| 2026-10-02 22:16:54 | [CVE-2026-105046](https://nvd.nist.gov/vuln/detail/CVE-2026-105046) | Medium | 4.3 | Kentico Xperience 13 before 13.0.216 lacks object-level authorization checks for administration API endpoints. |
| 2026-10-02 22:16:55 | [CVE-2026-93474](https://nvd.nist.gov/vuln/detail/CVE-2026-93474) | Medium | 6.9 | Charging station authentication identifiers are publicly accessible via web-based mapping platforms. |
| 2026-10-02 22:16:56 | [CVE-2026-94591](https://nvd.nist.gov/vuln/detail/CVE-2026-94591) | High | 8.6 | Armatura One stores database and message-broker credentials in an install configuration file, encrypting them with AES-… |
| 2026-10-02 22:16:56 | [CVE-2026-94592](https://nvd.nist.gov/vuln/detail/CVE-2026-94592) | High | 8.6 | Armatura One's database initialization routine assigns a fixed, vendor-defined password to the database superuser accou… |
| 2026-10-02 22:16:56 | [CVE-2026-94593](https://nvd.nist.gov/vuln/detail/CVE-2026-94593) | High | 8.5 | Armatura One's backup and restore routine records the full database connection command, including the superuser passwor… |
| 2026-10-02 22:16:56 | [CVE-2026-94594](https://nvd.nist.gov/vuln/detail/CVE-2026-94594) | Medium | 5.1 | Armatura One's message broker logs client connection credentials and the associated password in plain text during norma… |
| 2026-10-02 22:16:56 | [CVE-2026-95102](https://nvd.nist.gov/vuln/detail/CVE-2026-95102) | Critical | 9.3 | WebSocket endpoints lack proper authentication mechanisms, enabling attackers to impersonate charging stations. As a re… |
| 2026-10-02 22:16:56 | [CVE-2026-97212](https://nvd.nist.gov/vuln/detail/CVE-2026-97212) | Medium | 6.9 | The WebSocket backend uses charging station identifiers to uniquely associate sessions but allows multiple endpoints to… |
| 2026-10-02 22:16:56 | [CVE-2026-97363](https://nvd.nist.gov/vuln/detail/CVE-2026-97363) | High | 8.7 | The WebSocket Application Programming Interface lacks restrictions on the number of authentication requests. This absen… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
