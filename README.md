# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-08 04:18 UTC

New CVEs published between 2026-10-08 03:20 UTC and 2026-10-08 04:18 UTC.

[Full CSV](data/new-cves-2026-10-08T04-18-38-351302Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-10-08 04:17:14 | [CVE-2026-107444](https://nvd.nist.gov/vuln/detail/CVE-2026-107444) | Medium | 4.3 | A flaw was found in Katello where the Docker Tags repositories API does not properly enforce organization scoping when… |
| 2026-10-08 04:17:19 | [CVE-2026-107445](https://nvd.nist.gov/vuln/detail/CVE-2026-107445) | Medium | 5.4 | A flaw was found in Katello where the Flatpak Remote Repositories API does not properly enforce authorization when acce… |
| 2026-10-08 04:17:19 | [CVE-2026-107446](https://nvd.nist.gov/vuln/detail/CVE-2026-107446) | Medium | 6.8 | containerd overlaybd through 1.0.18 has a do_load_index (LSMT index loading) integer overflow (and resultant out-of-bou… |
| 2026-10-08 04:17:19 | [CVE-2026-107448](https://nvd.nist.gov/vuln/detail/CVE-2026-107448) | Low | 3.4 | Magic: The Gathering Arena (Windows/Steam client; 2026.59.30.12801.127931.6 and certain later 2026.60.x builds) passes… |
| 2026-10-08 04:17:52 | [CVE-2026-87660](https://nvd.nist.gov/vuln/detail/CVE-2026-87660) | High | 7.0 | An improper file permission and missing authorization vulnerability exists in the diagnostic kernel module subsystem of… |
| 2026-10-08 04:17:52 | [CVE-2026-87666](https://nvd.nist.gov/vuln/detail/CVE-2026-87666) | High | 8.6 | An OS command injection vulnerability exists in the time and zone management subsystem of Brocade Fabric OS versions be… |
| 2026-10-08 04:17:52 | [CVE-2026-87667](https://nvd.nist.gov/vuln/detail/CVE-2026-87667) | High | 8.4 | An argument injection vulnerability exists in the configuration management command-line utility of Brocade Fabric OS ve… |
| 2026-10-08 04:17:53 | [CVE-2026-87673](https://nvd.nist.gov/vuln/detail/CVE-2026-87673) | High | 7.0 | An OS command injection vulnerability exists in maintenance command-line diagnostic utilities on Brocade Fabric OS vers… |
| 2026-10-08 04:17:53 | [CVE-2026-87674](https://nvd.nist.gov/vuln/detail/CVE-2026-87674) | High | 8.5 | A local privilege escalation vulnerability exists in the system logging daemon of Brocade Fabric OS versions before 9.2… |
| 2026-10-08 04:17:55 | [CVE-2026-87675](https://nvd.nist.gov/vuln/detail/CVE-2026-87675) | High | 7.3 | An OS command injection vulnerability exists in the configuration management subsystem of Brocade Fabric OS versions be… |
| 2026-10-08 04:17:56 | [CVE-2026-87685](https://nvd.nist.gov/vuln/detail/CVE-2026-87685) | High | 8.4 | An arbitrary file manipulation vulnerability exists in the WebTools management interface of Brocade Fabric OS versions… |
| 2026-10-08 04:17:56 | [CVE-2026-87687](https://nvd.nist.gov/vuln/detail/CVE-2026-87687) | High | 8.5 | An authorization and input validation vulnerability exists in Brocade Fabric OS versions before 9.2.2d and 10.0.0 throu… |
| 2026-10-08 04:17:56 | [CVE-2026-87688](https://nvd.nist.gov/vuln/detail/CVE-2026-87688) | High | 8.5 | An input validation vulnerability exists in the security certificate management component of the Brocade Fabric OS admi… |
| 2026-10-08 04:18:00 | [CVE-2026-94575](https://nvd.nist.gov/vuln/detail/CVE-2026-94575) | Medium | 6.9 | A logic vulnerability in Brocade Fabric OS versions before 10.0.1 web management framework allows an authenticated, low… |
| 2026-10-08 04:18:00 | [CVE-2026-94580](https://nvd.nist.gov/vuln/detail/CVE-2026-94580) | Medium | 5.7 | An arbitrary file and directory deletion vulnerability exists in the REST API management interface handling USB storage… |
| 2026-10-08 04:18:00 | [CVE-2026-94584](https://nvd.nist.gov/vuln/detail/CVE-2026-94584) | Low | 2.1 | A race condition and thread-safety vulnerability exists in the web management daemon of Brocade Fabric OS versions befo… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
