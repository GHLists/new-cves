# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-01 16:19 UTC

New CVEs published between 2026-10-01 15:20 UTC and 2026-10-01 16:19 UTC.

[Full CSV](data/new-cves-2026-10-01T16-19-50-351772Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-10-01 16:17:32 | [CVE-2026-101322](https://nvd.nist.gov/vuln/detail/CVE-2026-101322) | High | 8.3 | In Eclipse BaSyx AAS Web UI versions v2-241220 through releases before v2-260924, the shared request handler attached t… |
| 2026-10-01 16:17:36 | [CVE-2026-103505](https://nvd.nist.gov/vuln/detail/CVE-2026-103505) | Medium | 6.9 | Improper neutralization of argument delimiters in the volume handling component in AWS EFS CSI Driver (aws-efs-csi-driv… |
| 2026-10-01 16:17:40 | [CVE-2026-103690](https://nvd.nist.gov/vuln/detail/CVE-2026-103690) | Low | 2.1 | A flaw has been found in itsourcecode Leave Management System 1.0. This vulnerability affects unknown code of the file… |
| 2026-10-01 16:17:40 | [CVE-2026-12627](https://nvd.nist.gov/vuln/detail/CVE-2026-12627) | Critical | 9.8 | Fortra's Core Privileged Access Manager (BoKS) contains a stack-based buffer overflow vulnerability in boks_autoregiste… |
| 2026-10-01 16:17:41 | [CVE-2026-17053](https://nvd.nist.gov/vuln/detail/CVE-2026-17053) | Medium | 4.4 | The SMBus driver API exposed smbus_smbalert_remove_cb() and smbus_host_notify_remove_cb() as Zephyr syscalls. Their ver… |
| 2026-10-01 16:17:41 | [CVE-2026-18734](https://nvd.nist.gov/vuln/detail/CVE-2026-18734) |  |  | Rejected reason: ** REJECT ** DO NOT USE THIS CANDIDATE NUMBER. Reason: This candidate was issued in error. Notes: All… |
| 2026-10-01 16:17:43 | [CVE-2026-42356](https://nvd.nist.gov/vuln/detail/CVE-2026-42356) |  |  | Deployment of wrong handler vulnerability in Apache HTTP Server allows the target of some internal redirects from CGI p… |
| 2026-10-01 16:17:43 | [CVE-2026-42528](https://nvd.nist.gov/vuln/detail/CVE-2026-42528) |  |  | A memory calculation bug in mod_dav in Apache httpd 2.4.67 and earlier allows an attacker with permission to create Web… |
| 2026-10-01 16:17:44 | [CVE-2026-46729](https://nvd.nist.gov/vuln/detail/CVE-2026-46729) |  |  | NULL Pointer Dereference vulnerability in Apache HTTP Servers mod_heartmonitor over unicast listener. This issue affect… |
| 2026-10-01 16:17:44 | [CVE-2026-47360](https://nvd.nist.gov/vuln/detail/CVE-2026-47360) |  |  | Exposure of Sensitive Information to an Unauthorized Actor vulnerability in Apache HTTP Server's mod_session_cookie mod… |
| 2026-10-01 16:17:59 | [CVE-2026-79896](https://nvd.nist.gov/vuln/detail/CVE-2026-79896) | High | 7.5 | Fortra BoKS Manager contains an out-of-bounds read vulnerability in the custom TLS ClientHello parser used by boks_port… |
| 2026-10-01 16:18:08 | [CVE-2026-94620](https://nvd.nist.gov/vuln/detail/CVE-2026-94620) | Critical | 9.4 | Classroom 50 is a free and open-source tool for managing and grading programming assignments via GitHub. Prior to versi… |
| 2026-10-01 16:18:09 | [CVE-2026-9864](https://nvd.nist.gov/vuln/detail/CVE-2026-9864) | Medium | 4.8 | Fortra BoKS Server Agent contains a predictable password generation vulnerability in the adjoin utility. Machine-accoun… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
