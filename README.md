# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-11-04 01:18 UTC

New CVEs published between 2026-11-04 00:18 UTC and 2026-11-04 01:18 UTC.

[Full CSV](data/new-cves-2026-11-04T01-18-18-808474Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-11-04 01:17:23 | [CVE-2026-121598](https://nvd.nist.gov/vuln/detail/CVE-2026-121598) | High | 8.6 | A security vulnerability has been detected in TOTOLINK A950RG 4.1.2cu.5268_B20221104. This impacts the function strcpy… |
| 2026-11-04 01:17:23 | [CVE-2026-121599](https://nvd.nist.gov/vuln/detail/CVE-2026-121599) | High | 8.6 | A vulnerability was detected in TOTOLINK A950RG 4.1.2cu.5268_B20221104. Affected is the function setWiFiMultipleConfig/… |
| 2026-11-04 01:17:23 | [CVE-2026-121600](https://nvd.nist.gov/vuln/detail/CVE-2026-121600) | High | 8.6 | A flaw has been found in TOTOLINK A950RG 4.1.2cu.5268_B20221104. Affected by this vulnerability is the function setMacF… |
| 2026-11-04 01:17:23 | [CVE-2026-121606](https://nvd.nist.gov/vuln/detail/CVE-2026-121606) | Critical | 9.3 | A vulnerability has been found in Qihoo 360 D621-2, D603-2, D600-2, D619, D606-6 and D706 up to 6.4.9. Affected by this… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
