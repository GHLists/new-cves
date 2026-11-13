# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-11-13 03:18 UTC

New CVEs published between 2026-11-13 02:21 UTC and 2026-11-13 03:18 UTC.

[Full CSV](data/new-cves-2026-11-13T03-18-57-607931Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-11-13 03:17:28 | [CVE-2026-107411](https://nvd.nist.gov/vuln/detail/CVE-2026-107411) | High | 8.7 | Memory overflow in RTSP ALG can lead to unpredictable or erroneous behavior or Denial of Service in Citrix NetScaler |
| 2026-11-13 03:17:28 | [CVE-2026-107412](https://nvd.nist.gov/vuln/detail/CVE-2026-107412) | Critical | 9.5 | Multiple Memory overflow vulnerabilities can lead to unpredictable or erroneous behavior and Denial of Service in Citri… |
| 2026-11-13 03:17:28 | [CVE-2026-107413](https://nvd.nist.gov/vuln/detail/CVE-2026-107413) | High | 8.7 | Memory overflow in SAML authentication can lead to unpredictable or erroneous behavior or Denial of Service in Citrix N… |
| 2026-11-13 03:17:29 | [CVE-2026-107414](https://nvd.nist.gov/vuln/detail/CVE-2026-107414) | High | 8.7 | Memory overflow in WebAuth authentication can lead to unpredictable or erroneous behavior or Denial of Service in Citri… |
| 2026-11-13 03:17:29 | [CVE-2026-127285](https://nvd.nist.gov/vuln/detail/CVE-2026-127285) | Low | 2.1 | A flaw has been found in Cairo-dock Glx-Dock 3.4.0. The affected element is an unknown function of the file bg_forum.ph… |
| 2026-11-13 03:17:30 | [CVE-2026-127286](https://nvd.nist.gov/vuln/detail/CVE-2026-127286) | Medium | 5.5 | A vulnerability was identified in Zackriya-Solutions Meetily up to 0.4.1. Affected is an unknown function of the file b… |
| 2026-11-13 03:17:30 | [CVE-2026-49747](https://nvd.nist.gov/vuln/detail/CVE-2026-49747) |  |  | Software installed and run as a non-privileged user may conduct GPU system calls to trigger an integer overflow and all… |
| 2026-11-13 03:17:30 | [CVE-2026-74911](https://nvd.nist.gov/vuln/detail/CVE-2026-74911) |  |  | Software installed and run as a non-privileged user may conduct improper GPU system calls to the execution of an error… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
