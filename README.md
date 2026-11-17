# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-11-17 17:20 UTC

New CVEs published between 2026-11-17 16:21 UTC and 2026-11-17 17:20 UTC.

[Full CSV](data/new-cves-2026-11-17T17-20-36-541798Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-11-17 17:17:43 | [CVE-2026-100967](https://nvd.nist.gov/vuln/detail/CVE-2026-100967) | High | 7.8 | NVIDIA Megatron-LM contains a vulnerability where an attacker could cause deserialization of untrusted data. A successf… |
| 2026-11-17 17:17:43 | [CVE-2026-100968](https://nvd.nist.gov/vuln/detail/CVE-2026-100968) | High | 7.8 | NVIDIA Megatron-LM contains a vulnerability in dataset loading where an attacker could cause deserialization of untrust… |
| 2026-11-17 17:17:53 | [CVE-2026-119725](https://nvd.nist.gov/vuln/detail/CVE-2026-119725) | High | 8.2 | Improper Limitation of a Pathname to a Restricted Directory ('Path Traversal') vulnerability in PocketBook / Obreey Pro… |
| 2026-11-17 17:17:53 | [CVE-2026-119726](https://nvd.nist.gov/vuln/detail/CVE-2026-119726) | High | 8.3 | Improper Limitation of a Pathname to a Restricted Directory ('Path Traversal') vulnerability in PocketBook / Obreey Pro… |
| 2026-11-17 17:17:53 | [CVE-2026-120287](https://nvd.nist.gov/vuln/detail/CVE-2026-120287) | Medium | 6.9 | Allocation of Resources Without Limits or Throttling vulnerability in Plug.Parsers.MULTIPART in elixir-plug plug allows… |
| 2026-11-17 17:17:58 | [CVE-2026-126547](https://nvd.nist.gov/vuln/detail/CVE-2026-126547) | High | 7.8 | Missing Authorization vulnerability in Broadcom AutoSys Workload Automation (Workload Control Center (WCC) modules) on… |
| 2026-11-17 17:17:58 | [CVE-2026-126548](https://nvd.nist.gov/vuln/detail/CVE-2026-126548) | High | 7.1 | Server-Side Request Forgery (SSRF) vulnerability in Broadcom AutoSys Workload Automation (Workload Control Center (WCC)… |
| 2026-11-17 17:17:58 | [CVE-2026-126549](https://nvd.nist.gov/vuln/detail/CVE-2026-126549) | Medium | 5.1 | Insertion of Sensitive Information into Log File vulnerability in Broadcom AutoSys Workload Automation (Workload Contro… |
| 2026-11-17 17:17:59 | [CVE-2026-126550](https://nvd.nist.gov/vuln/detail/CVE-2026-126550) | High | 8.6 | Insertion of Sensitive Information into Log File, Insufficiently Protected Credentials vulnerability in Broadcom AutoSy… |
| 2026-11-17 17:17:59 | [CVE-2026-126551](https://nvd.nist.gov/vuln/detail/CVE-2026-126551) | Critical | 9.3 | Use of Hard-coded Cryptographic Key vulnerability in Broadcom AutoSys Workload Automation (Workload Control Center (WCC… |
| 2026-11-17 17:17:59 | [CVE-2026-126552](https://nvd.nist.gov/vuln/detail/CVE-2026-126552) | Critical | 9.3 | Missing Authentication for Critical Function, OS Command Injection vulnerability in Broadcom AutoSys Workload Automatio… |
| 2026-11-17 17:17:59 | [CVE-2026-126553](https://nvd.nist.gov/vuln/detail/CVE-2026-126553) | Critical | 9.3 | Deserialization of Untrusted Data vulnerability in Broadcom AutoSys Workload Automation (Workload Control Center (WCC)… |
| 2026-11-17 17:17:59 | [CVE-2026-126555](https://nvd.nist.gov/vuln/detail/CVE-2026-126555) | Medium | 5.3 | Missing Authorization, Hidden Functionality vulnerability in Broadcom AutoSys Workload Automation (Workload Control Cen… |
| 2026-11-17 17:17:59 | [CVE-2026-126556](https://nvd.nist.gov/vuln/detail/CVE-2026-126556) | Medium | 5.1 | Invocation of Process Using Visible Sensitive Information, Insufficiently Protected Credentials vulnerability in Broadc… |
| 2026-11-17 17:17:59 | [CVE-2026-126557](https://nvd.nist.gov/vuln/detail/CVE-2026-126557) | Medium | 4.8 | Out-of-bounds Write vulnerability in Broadcom AutoSys Workload Automation (AutoSys engine (AE) native clients modules)… |
| 2026-11-17 17:18:00 | [CVE-2026-126558](https://nvd.nist.gov/vuln/detail/CVE-2026-126558) | High | 8.7 | OS Command Injection, Incomplete List of Disallowed Inputs vulnerability in Broadcom AutoSys Workload Automation (Workl… |
| 2026-11-17 17:18:02 | [CVE-2026-129246](https://nvd.nist.gov/vuln/detail/CVE-2026-129246) | High | 7.8 | Due to a Debian-specific patch, the directory used to share data between the LightDM and the users logging in was writa… |
| 2026-11-17 17:18:05 | [CVE-2026-130801](https://nvd.nist.gov/vuln/detail/CVE-2026-130801) |  |  | The device's command parser does not require asymmetric cryptographic signatures to validate incoming APDU packets. Thi… |
| 2026-11-17 17:18:05 | [CVE-2026-130802](https://nvd.nist.gov/vuln/detail/CVE-2026-130802) |  |  | The NFC authentication handshake relies on a fixed, static challenge instead of a unique, random value for every sessio… |
| 2026-11-17 17:18:05 | [CVE-2026-130803](https://nvd.nist.gov/vuln/detail/CVE-2026-130803) |  |  | The firmware and flash memory store critical cryptographic secrets, such as global AES keys and network master keys, in… |
| 2026-11-17 17:18:05 | [CVE-2026-130804](https://nvd.nist.gov/vuln/detail/CVE-2026-130804) |  |  | The microcontroller lacks enabled debug lock bits, leaving the physical Single-Wire (SWS) debugging interface completel… |
| 2026-11-17 17:18:08 | [CVE-2026-65132](https://nvd.nist.gov/vuln/detail/CVE-2026-65132) | High | 7.8 | NVIDIA Megatron-LM contains a vulnerability in checkpoint loading where an attacker could cause deserialization of untr… |
| 2026-11-17 17:18:09 | [CVE-2026-67455](https://nvd.nist.gov/vuln/detail/CVE-2026-67455) | High | 8.8 | NVIDIA Model Optimizer for Linux and Windows contains a vulnerability where an attacker could cause a deserialization o… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
