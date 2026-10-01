# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-01 03:18 UTC

New CVEs published between 2026-10-01 02:19 UTC and 2026-10-01 03:18 UTC.

[Full CSV](data/new-cves-2026-10-01T03-18-43-460929Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-10-01 03:16:58 | [CVE-2026-101887](https://nvd.nist.gov/vuln/detail/CVE-2026-101887) | Low | 2.1 | BlueALSA (bluez-alsa/bluealsad) contains a division-by-zero vulnerability in the LC3plus sink decoder (a2dp-lc3plus.c,… |
| 2026-10-01 03:16:59 | [CVE-2026-103533](https://nvd.nist.gov/vuln/detail/CVE-2026-103533) | Low | 1.2 | A vulnerability was found in David-Crty databasement up to 1.7.1. This impacts the function https:/github.com/David-Crt… |
| 2026-10-01 03:16:59 | [CVE-2026-92537](https://nvd.nist.gov/vuln/detail/CVE-2026-92537) | Medium | 5.3 | The Newsletter – Send awesome emails from WordPress plugin for WordPress is vulnerable to Insufficiently Protected Cred… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
