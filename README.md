# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-13 23:19 UTC

New CVEs published between 2026-10-13 22:18 UTC and 2026-10-13 23:19 UTC.

[Full CSV](data/new-cves-2026-10-13T23-19-18-517652Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-10-13 22:18:58 | [CVE-2026-84419](https://nvd.nist.gov/vuln/detail/CVE-2026-84419) | Medium | 6.8 | Out-of-bounds write vulnerability in Citrix Workspace app for Windows. This issue affects Workspace app for Windows: be… |
| 2026-10-13 22:18:58 | [CVE-2026-84420](https://nvd.nist.gov/vuln/detail/CVE-2026-84420) | Medium | 5.8 | Out-of-bounds read vulnerability in Citirx Citrix Workspace app for Windows. This issue affects Citrix Workspace app fo… |
| 2026-10-13 22:18:58 | [CVE-2026-84790](https://nvd.nist.gov/vuln/detail/CVE-2026-84790) | High | 7.6 | OpenVPN 2.7_alpha1 through 2.7.7 allows remote authenticated users to impersonate others via a crafted certificate subj… |
| 2026-10-13 22:19:30 | [CVE-2026-94453](https://nvd.nist.gov/vuln/detail/CVE-2026-94453) | High | 7.5 | Libreswan's pluto daemon has a use-after-free vulnerability when a client connecting using IKE over TCP closes the conn… |
| 2026-10-13 22:19:30 | [CVE-2026-95632](https://nvd.nist.gov/vuln/detail/CVE-2026-95632) | High | 7.5 | CAI Content Credentials is affected by an Improper Verification of Cryptographic Signature vulnerability that could res… |
| 2026-10-13 22:19:30 | [CVE-2026-95633](https://nvd.nist.gov/vuln/detail/CVE-2026-95633) | High | 7.5 | CAI Content Credentials is affected by an Improper Verification of Cryptographic Signature vulnerability that could res… |
| 2026-10-13 22:19:30 | [CVE-2026-95634](https://nvd.nist.gov/vuln/detail/CVE-2026-95634) | High | 8.6 | CAI Content Credentials is affected by a Server-Side Request Forgery (SSRF) vulnerability that could result in privileg… |
| 2026-10-13 22:19:45 | [CVE-2026-97381](https://nvd.nist.gov/vuln/detail/CVE-2026-97381) | Critical | 9.9 | Legacy Update is a tool for activating and installing updates on legacy Windows PCs. Legacy Update 1.12.0 through 1.13.… |
| 2026-10-13 23:17:25 | [CVE-2026-104922](https://nvd.nist.gov/vuln/detail/CVE-2026-104922) |  |  | Rejected reason: This CVE ID has been rejected or withdrawn by its CVE Numbering Authority. |
| 2026-10-13 23:17:26 | [CVE-2026-105142](https://nvd.nist.gov/vuln/detail/CVE-2026-105142) |  |  | Rejected reason: This CVE ID has been rejected or withdrawn by its CVE Numbering Authority. |
| 2026-10-13 23:17:26 | [CVE-2026-105390](https://nvd.nist.gov/vuln/detail/CVE-2026-105390) | Medium | 6.9 | Improper synchronization in the OpenVPN ovpn-dco-win for Windows versions 0.6.5 through 1.3.5 and 2.4.0 through 2.8.7 a… |
| 2026-10-13 23:17:26 | [CVE-2026-105151](https://nvd.nist.gov/vuln/detail/CVE-2026-105151) |  |  | Rejected reason: This CVE ID has been rejected or withdrawn by its CVE Numbering Authority. |
| 2026-10-13 23:17:32 | [CVE-2026-15468](https://nvd.nist.gov/vuln/detail/CVE-2026-15468) | Medium | 6.9 | Authorization bypass through User-Controlled key vulnerability in HYPR Passwordless on Windows allows Privilege Escalat… |
| 2026-10-13 23:17:32 | [CVE-2026-53563](https://nvd.nist.gov/vuln/detail/CVE-2026-53563) | Medium | 6.9 | Vulnerability in Citrix UniconOS leading to Persistent Command Execution This issue affects UniconOS: before 2607.2 CR… |
| 2026-10-13 23:17:33 | [CVE-2026-53564](https://nvd.nist.gov/vuln/detail/CVE-2026-53564) | Medium | 5.1 | Vulnerability in Citrix UniconOS leading to Arbitrary file read and write This issue affects UniconOS: before 2607.2 CR… |
| 2026-10-13 23:19:13 | [CVE-2026-88964](https://nvd.nist.gov/vuln/detail/CVE-2026-88964) | High | 7.1 | An integer underflow in OpenVPN version 2.7_alpha3 through 2.7.7 on Windows and Android allows remote authenticated ser… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
