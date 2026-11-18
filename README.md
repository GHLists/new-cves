# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-11-18 09:19 UTC

New CVEs published between 2026-11-18 08:19 UTC and 2026-11-18 09:19 UTC.

[Full CSV](data/new-cves-2026-11-18T09-19-09-879451Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-11-18 09:17:44 | [CVE-2026-113497](https://nvd.nist.gov/vuln/detail/CVE-2026-113497) | High | 8.7 | A low-privileged remote attacker can change the password of arbitrary users using the REST API, including administrativ… |
| 2026-11-18 09:17:44 | [CVE-2026-128981](https://nvd.nist.gov/vuln/detail/CVE-2026-128981) |  |  | ** UNSUPPORTED WHEN ASSIGNED ** Improper Authentication in Apache SeaTunnel Web 1.0.2 allows a user whose account has b… |
| 2026-11-18 09:17:44 | [CVE-2026-95643](https://nvd.nist.gov/vuln/detail/CVE-2026-95643) | Critical | 9.1 | Zohocorp Manageengine DDI Central build below 6500 are affected by a authenticated PowerShell command injection vulnera… |
| 2026-11-18 09:17:44 | [CVE-2026-95645](https://nvd.nist.gov/vuln/detail/CVE-2026-95645) | Critical | 9.1 | Zohocorp Manageengine DDI Central build below 6500 are affected by a authenticated command injection vulnerability in t… |
| 2026-11-18 09:17:45 | [CVE-2026-99312](https://nvd.nist.gov/vuln/detail/CVE-2026-99312) |  |  | In the Linux kernel, the following vulnerability has been resolved: KVM: x86: Unconditionally reset MMU context when em… |
| 2026-11-18 09:17:45 | [CVE-2026-99313](https://nvd.nist.gov/vuln/detail/CVE-2026-99313) |  |  | In the Linux kernel, the following vulnerability has been resolved: HID: logitech-hidpp: fix race condition when access… |
| 2026-11-18 09:17:45 | [CVE-2026-99314](https://nvd.nist.gov/vuln/detail/CVE-2026-99314) |  |  | In the Linux kernel, the following vulnerability has been resolved: ALSA: us122l: Add missing NULL check in usb_stream_… |
| 2026-11-18 09:17:45 | [CVE-2026-99315](https://nvd.nist.gov/vuln/detail/CVE-2026-99315) |  |  | In the Linux kernel, the following vulnerability has been resolved: ALSA: us122l: Fix NULL dereference at hwdep open an… |
| 2026-11-18 09:17:45 | [CVE-2026-99316](https://nvd.nist.gov/vuln/detail/CVE-2026-99316) |  |  | In the Linux kernel, the following vulnerability has been resolved: ALSA: usx2y: Initialize idle URBs before submitting… |
| 2026-11-18 09:17:45 | [CVE-2026-99317](https://nvd.nist.gov/vuln/detail/CVE-2026-99317) |  |  | In the Linux kernel, the following vulnerability has been resolved: ALSA: hwdep: Serialize DSP load requests The check… |
| 2026-11-18 09:17:45 | [CVE-2026-99318](https://nvd.nist.gov/vuln/detail/CVE-2026-99318) |  |  | In the Linux kernel, the following vulnerability has been resolved: ALSA: bcd2000: Fix use-after-free of MIDI URBs on f… |
| 2026-11-18 09:17:46 | [CVE-2026-99319](https://nvd.nist.gov/vuln/detail/CVE-2026-99319) |  |  | In the Linux kernel, the following vulnerability has been resolved: ALSA: usx2y: Refuse a retried DSP load after a fail… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
