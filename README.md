# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-11-18 02:19 UTC

New CVEs published between 2026-11-18 01:19 UTC and 2026-11-18 02:19 UTC.

[Full CSV](data/new-cves-2026-11-18T02-19-36-091739Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-11-18 02:17:38 | [CVE-2026-105929](https://nvd.nist.gov/vuln/detail/CVE-2026-105929) | High | 8.1 | A path traversal vulnerability (CWE-22) was found in ansible-core's ansible-galaxy role installation. An explicit role… |
| 2026-11-18 02:17:39 | [CVE-2026-106096](https://nvd.nist.gov/vuln/detail/CVE-2026-106096) | Medium | 6.4 | A flaw was found in CRI-O. When the optional Linux LinkLogs feature is enabled, the host pod log directory is bind-moun… |
| 2026-11-18 02:17:39 | [CVE-2026-110307](https://nvd.nist.gov/vuln/detail/CVE-2026-110307) | High | 7.4 | An incorrect authorization vulnerability was identified in GitHub Enterprise Server that allowed an authenticated user… |
| 2026-11-18 02:17:39 | [CVE-2026-112115](https://nvd.nist.gov/vuln/detail/CVE-2026-112115) | High | 8.5 | An untrusted search path in ASUS Armoury Crate allows a local, low-privileged user to achieve privilege escalation by e… |
| 2026-11-18 02:17:39 | [CVE-2026-112117](https://nvd.nist.gov/vuln/detail/CVE-2026-112117) | High | 7.3 | A Improper Limitation of a Pathname to a Restricted Directory ('Path Traversal') in ASUS System Control Interface , all… |
| 2026-11-18 02:17:39 | [CVE-2026-114202](https://nvd.nist.gov/vuln/detail/CVE-2026-114202) | Critical | 10.0 | Use of Hard-coded Cryptographic Key in ASUS Control Center Express allows a remote user to gain administrative privileg… |
| 2026-11-18 02:17:39 | [CVE-2026-114204](https://nvd.nist.gov/vuln/detail/CVE-2026-114204) | Critical | 9.0 | Use of Hard-coded Cryptographic Key in ASUS Control Center Express allows a remote user to bypass authentication by for… |
| 2026-11-18 02:17:39 | [CVE-2026-114205](https://nvd.nist.gov/vuln/detail/CVE-2026-114205) | Critical | 9.4 | Incorrect authorization in ASUS Control Center Express allows a remote authenticated user with a low-privileged role to… |
| 2026-11-18 02:17:40 | [CVE-2026-116637](https://nvd.nist.gov/vuln/detail/CVE-2026-116637) | High | 8.6 | A site administrator could modify files on the appliance host with root privileges and disclose private repository data… |
| 2026-11-18 02:17:40 | [CVE-2026-116643](https://nvd.nist.gov/vuln/detail/CVE-2026-116643) | High | 8.6 | An SSH certificate authentication bypass vulnerability in GitHub Enterprise Server allowed an authenticated organizatio… |
| 2026-11-18 02:17:40 | [CVE-2026-119469](https://nvd.nist.gov/vuln/detail/CVE-2026-119469) | High | 7.0 | Incorrect default permissions in the ASUS DisplayWidget Center allow a local, low-privileged user to achieve arbitrary… |
| 2026-11-18 02:17:40 | [CVE-2026-126574](https://nvd.nist.gov/vuln/detail/CVE-2026-126574) | Critical | 9.4 | Missing authorization vulnerability in ASUS Control Center Datacenter and Control Center Enterprise allows remote authe… |
| 2026-11-18 02:17:41 | [CVE-2026-131647](https://nvd.nist.gov/vuln/detail/CVE-2026-131647) | Medium | 5.3 | A CRLF injection vulnerability was identified in GitHub Enterprise Server that allowed a user with write access to a re… |
| 2026-11-18 02:17:41 | [CVE-2026-131820](https://nvd.nist.gov/vuln/detail/CVE-2026-131820) | High | 7.7 | A server-side request forgery vulnerability in GitHub Enterprise Server allowed an authenticated user with repository w… |
| 2026-11-18 02:17:41 | [CVE-2026-19399](https://nvd.nist.gov/vuln/detail/CVE-2026-19399) | Medium | 6.1 | Improper Authentication and Improper Limitation of a Pathname to a Restricted Directory ('Path Traversal') in ASUS Rout… |
| 2026-11-18 02:17:41 | [CVE-2026-88711](https://nvd.nist.gov/vuln/detail/CVE-2026-88711) | High | 8.7 | Improper neutralization of special elements used in an OS command in certain ASUS Router firmware models allows an remo… |
| 2026-11-18 02:17:41 | [CVE-2026-88760](https://nvd.nist.gov/vuln/detail/CVE-2026-88760) | Medium | 5.3 | Missing Authentication for Critical Function in certain ASUS Router firmware allows unauthenticated nearby users to obt… |
| 2026-11-18 02:17:41 | [CVE-2026-93458](https://nvd.nist.gov/vuln/detail/CVE-2026-93458) | Medium | 6.1 | Insertion of sensitive information into sent data in certain ASUS Router firmware allows a remote attacker to obtain ro… |
| 2026-11-18 02:17:42 | [CVE-2026-93459](https://nvd.nist.gov/vuln/detail/CVE-2026-93459) | High | 8.5 | Use of externally-controlled format string in certain ASUS Router firmware allows a nearby administrator to read or wri… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
