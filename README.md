# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-09-27 13:19 UTC

New CVEs published between 2026-09-27 12:19 UTC and 2026-09-27 13:19 UTC.

[Full CSV](data/new-cves-2026-09-27T13-19-11-070742Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-09-27 13:16:36 | [CVE-2026-100866](https://nvd.nist.gov/vuln/detail/CVE-2026-100866) | Medium | 4.8 | onefetch through 2.28.1 writes repository information field values to the terminal without removing control characters,… |
| 2026-09-27 13:16:37 | [CVE-2026-100867](https://nvd.nist.gov/vuln/detail/CVE-2026-100867) | Medium | 4.8 | spaceship-prompt through 4.22.5 fails to sanitize control characters from project manifest version fields before render… |
| 2026-09-27 13:16:37 | [CVE-2026-100868](https://nvd.nist.gov/vuln/detail/CVE-2026-100868) | Medium | 5.3 | Penpot before 2.18.0 binds the MCP server plugin WebSocket bridge to all network interfaces without authentication in s… |
| 2026-09-27 13:16:38 | [CVE-2026-100869](https://nvd.nist.gov/vuln/detail/CVE-2026-100869) | High | 8.2 | Sylius versions before 2.1.16 and 2.2.9 fail to restrict payment request actions in the Shop API endpoint, allowing cus… |
| 2026-09-27 13:16:38 | [CVE-2026-100870](https://nvd.nist.gov/vuln/detail/CVE-2026-100870) | High | 8.7 | Sylius versions before 1.12.25, 1.13.17, 1.14.20, 2.1.16, and 2.2.9 build administrator password-reset links using the… |
| 2026-09-27 13:16:38 | [CVE-2026-100871](https://nvd.nist.gov/vuln/detail/CVE-2026-100871) | High | 8.7 | Sylius versions before 1.12.25, 1.13.17, 1.14.20, 2.1.16, and 2.2.9 fail to include firewall identification in JWT toke… |
| 2026-09-27 13:16:38 | [CVE-2026-100872](https://nvd.nist.gov/vuln/detail/CVE-2026-100872) | High | 8.7 | Sylius versions before 2.1.16 and 2.2.9 fail to validate payment amounts during cart recalculation, allowing unauthenti… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
