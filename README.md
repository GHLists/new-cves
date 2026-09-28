# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-09-28 11:18 UTC

New CVEs published between 2026-09-28 10:19 UTC and 2026-09-28 11:18 UTC.

[Full CSV](data/new-cves-2026-09-28T11-18-58-898993Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-09-28 11:16:43 | [CVE-2026-101038](https://nvd.nist.gov/vuln/detail/CVE-2026-101038) | High | 8.6 | A vulnerability was determined in FAST FAC1200R 5.0_20201119_1.0.2. Affected by this vulnerability is the function MmtA… |
| 2026-09-28 11:16:43 | [CVE-2026-101039](https://nvd.nist.gov/vuln/detail/CVE-2026-101039) | Critical | 9.3 | A vulnerability was identified in FAST FAC1900R 20190827_2.0.2. Affected by this issue is the function copy_msg_element… |
| 2026-09-28 11:16:43 | [CVE-2026-101040](https://nvd.nist.gov/vuln/detail/CVE-2026-101040) | Medium | 5.7 | A security flaw has been discovered in Ricoh SP 330DN, SP 221, SP C252SF and Aficio SP 3500SF up to 20260813. This affe… |
| 2026-09-28 11:16:43 | [CVE-2026-12267](https://nvd.nist.gov/vuln/detail/CVE-2026-12267) | High | 7.2 | ManageEngine DDI Central versions below 6201 are vulnerable to Command injection in Windows DNS Query Resolution Policy… |
| 2026-09-28 11:16:44 | [CVE-2026-12268](https://nvd.nist.gov/vuln/detail/CVE-2026-12268) | High | 8.8 | ManageEngine DDI Central versions below 6201 are vulnerable to PowerShell command injection in Windows DNS SPF/TXT reco… |
| 2026-09-28 11:16:44 | [CVE-2026-12269](https://nvd.nist.gov/vuln/detail/CVE-2026-12269) | High | 8.8 | Zohocorp ManageEngine DDI Central 6.2.0 build below 6201 had a Keepalived configuration injection vulnerability in the… |
| 2026-09-28 11:16:45 | [CVE-2026-19759](https://nvd.nist.gov/vuln/detail/CVE-2026-19759) | Critical | 9.4 | An Incorrect Authorization vulnerability in the task configuration in Google Cloud Application Integration versions pri… |
| 2026-09-28 11:16:47 | [CVE-2026-81375](https://nvd.nist.gov/vuln/detail/CVE-2026-81375) | High | 8.3 | A Confused Deputy vulnerability in the EmailTask component in Google Cloud Application Integration versions prior to 20… |
| 2026-09-28 11:16:48 | [CVE-2026-81867](https://nvd.nist.gov/vuln/detail/CVE-2026-81867) | Critical | 9.4 | A Deserialization of Untrusted Data vulnerability in the JavaScript Task in Google Cloud Application Integration versio… |
| 2026-09-28 11:16:48 | [CVE-2026-91006](https://nvd.nist.gov/vuln/detail/CVE-2026-91006) |  |  | Apache Karaf's instance-management service (InstanceServiceImpl) builds the command line used to launch a child Karaf J… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
