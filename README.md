# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-19 23:18 UTC

New CVEs published between 2026-10-19 22:21 UTC and 2026-10-19 23:18 UTC.

[Full CSV](data/new-cves-2026-10-19T23-18-59-246619Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-10-19 23:17:35 | [CVE-2025-36061](https://nvd.nist.gov/vuln/detail/CVE-2025-36061) | Medium | 6.5 | IBM Storage TS4500 Library 1.1.1.6 through 1.12.0.3 IBM Diamondback Tape Library and IBM Storage TS4500 Library could a… |
| 2026-10-19 23:17:35 | [CVE-2025-36069](https://nvd.nist.gov/vuln/detail/CVE-2025-36069) | Medium | 5.5 | IBM Storage TS4500 Library 1.1.1.6 through 1.12.0.3 does not invalidate session after a logout which could allow an aut… |
| 2026-10-19 23:17:35 | [CVE-2025-36252](https://nvd.nist.gov/vuln/detail/CVE-2025-36252) | Medium | 6.3 | IBM Storage TS4500 Library 1.1.1.6 through 1.12.0.3 IBM TS4500 Tape Library/Diamondback Tape Library does not invalidat… |
| 2026-10-19 23:17:35 | [CVE-2026-112370](https://nvd.nist.gov/vuln/detail/CVE-2026-112370) | High | 8.6 | A vulnerability was found in H3C Magic NX15 100R017. This issue affects the function sub_416874 of the file /usr/bin/us… |
| 2026-10-19 23:17:36 | [CVE-2026-112372](https://nvd.nist.gov/vuln/detail/CVE-2026-112372) | Low | 2.0 | A weakness has been identified in H3C Magic NX15 V100R017. This affects the function importprofile of the file /api/upl… |
| 2026-10-19 23:17:36 | [CVE-2026-112991](https://nvd.nist.gov/vuln/detail/CVE-2026-112991) | Medium | 6.3 | The html_to_markdown expansion module in MISP Modules contains a server-side request forgery (SSRF) vulnerability in it… |
| 2026-10-19 23:17:36 | [CVE-2026-19178](https://nvd.nist.gov/vuln/detail/CVE-2026-19178) | Medium | 6.8 | IBM Storage TS4500 Library 1.1.1.6 through 1.12.0.3 could allow a remote authenticated attacker to gain unauthorized ad… |
| 2026-10-19 23:17:36 | [CVE-2026-19595](https://nvd.nist.gov/vuln/detail/CVE-2026-19595) | Medium | 6.1 | The user-mode syscall verifier z_vrfy_rtio_cqe_get_mempool_buffer() in subsys/rtio/rtio_syscalls.c validated its two ou… |
| 2026-10-19 23:17:36 | [CVE-2026-112371](https://nvd.nist.gov/vuln/detail/CVE-2026-112371) | High | 8.6 | A vulnerability was determined in H3C Magic NX15 NX15V100R017. Impacted is the function write of the file /api/esps of… |
| 2026-10-19 23:17:37 | [CVE-2026-77684](https://nvd.nist.gov/vuln/detail/CVE-2026-77684) | Medium | 5.7 | The Bluetooth Classic Hands-Free Profile HF role in subsys/bluetooth/host/classic/hfp_hf.c does not release the AT comm… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
