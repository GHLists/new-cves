# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-11-02 17:18 UTC

New CVEs published between 2026-11-02 16:19 UTC and 2026-11-02 17:18 UTC.

[Full CSV](data/new-cves-2026-11-02T17-18-09-032966Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-11-02 17:17:32 | [CVE-2026-105769](https://nvd.nist.gov/vuln/detail/CVE-2026-105769) | Critical | 9.3 | kaniko before 1.25.20 can send a Microsoft Entra ID (Azure AD) access token for Azure Resource Manager to an attacker-c… |
| 2026-11-02 17:17:33 | [CVE-2026-106803](https://nvd.nist.gov/vuln/detail/CVE-2026-106803) |  |  | A stack-based buffer overflow exists in Kamailio v6.1.3 and v6.1.4 in the ims_registrar_pcscf module. When processing a… |
| 2026-11-02 17:17:33 | [CVE-2026-106804](https://nvd.nist.gov/vuln/detail/CVE-2026-106804) |  |  | A stack-based buffer overflow exists in Kamailio v6.1.3 and v6.1.4 in the ims_qos_npn module. The w_rx_aar_register() f… |
| 2026-11-02 17:17:33 | [CVE-2026-106805](https://nvd.nist.gov/vuln/detail/CVE-2026-106805) |  |  | A resource exhaustion issue exists in Free5GC v4.2.3 during PFCP Session Establishment failure handling. When the SMF d… |
| 2026-11-02 17:17:33 | [CVE-2026-106807](https://nvd.nist.gov/vuln/detail/CVE-2026-106807) |  |  | A denial-of-service vulnerability exists in open5GS v2.8.0 in the PFCP transaction handling path. When the PFCP transac… |
| 2026-11-02 17:17:39 | [CVE-2026-119301](https://nvd.nist.gov/vuln/detail/CVE-2026-119301) | Medium | 5.0 | Improper neutralization of quoting syntax in SQL identifier construction in the Apache Iceberg write component in AWS S… |
| 2026-11-02 17:17:40 | [CVE-2026-120596](https://nvd.nist.gov/vuln/detail/CVE-2026-120596) |  |  | A remotely exploitable denial-of-service vulnerability exists in the TCP options parser of the Nut/Net TCP/IP stack inc… |
| 2026-11-02 17:17:44 | [CVE-2026-65059](https://nvd.nist.gov/vuln/detail/CVE-2026-65059) |  |  | Furl versions through 3.15 for Perl allow memory exhaustion via unbounded decompression of HTTP responses. Furl inflate… |
| 2026-11-02 17:17:45 | [CVE-2026-88810](https://nvd.nist.gov/vuln/detail/CVE-2026-88810) | High | 7.2 | A privilege escalation issue was discovered in Rancher Manager's role-based access control. The inheritedNamespacedRule… |
| 2026-11-02 17:17:45 | [CVE-2026-88811](https://nvd.nist.gov/vuln/detail/CVE-2026-88811) | Critical | 9.1 | Missing filtering in the SUSE Rancher Manager meta proxy could cause passed in rancher credentials to be leaked to clou… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
