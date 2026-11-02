# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-11-02 18:18 UTC

New CVEs published between 2026-11-02 17:18 UTC and 2026-11-02 18:18 UTC.

[Full CSV](data/new-cves-2026-11-02T18-18-56-22954Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-11-02 18:18:33 | [CVE-2024-12139](https://nvd.nist.gov/vuln/detail/CVE-2024-12139) | Medium | 4.3 | The error handling implementation fails to properly sanitize or validate user-supplied input within URL parameters unde… |
| 2026-11-02 18:18:33 | [CVE-2026-106806](https://nvd.nist.gov/vuln/detail/CVE-2026-106806) |  |  | A memory exhaustion issue exists in Open5GS v2.8.0 in the HTTP/2 SBI server. Repeated header names cause previously all… |
| 2026-11-02 18:18:34 | [CVE-2026-106808](https://nvd.nist.gov/vuln/detail/CVE-2026-106808) |  |  | OpenAirInterface Core Network v2.2.1 has a stack-based buffer overflow vulnerability in the OAI CN5G UDM Nudm_UEAU Gene… |
| 2026-11-02 18:18:35 | [CVE-2026-111048](https://nvd.nist.gov/vuln/detail/CVE-2026-111048) | High | 8.4 | FOSSBilling is an open source billing and client-management platform. From 0.1.0 until 0.8.9, the admin/support/note_cr… |
| 2026-11-02 18:18:43 | [CVE-2026-117067](https://nvd.nist.gov/vuln/detail/CVE-2026-117067) |  |  | An out-of-bounds memory access vulnerability in the N2 SCTP interface of OpenAirInterface (OAI) CN5G AMF v2.2.1 allows… |
| 2026-11-02 18:18:43 | [CVE-2026-117068](https://nvd.nist.gov/vuln/detail/CVE-2026-117068) |  |  | An integer underflow vulnerability in the NAS decoder of OpenAirInterface (OAI) CN5G AMF v2.2.1 allows an unauthenticat… |
| 2026-11-02 18:18:44 | [CVE-2026-119085](https://nvd.nist.gov/vuln/detail/CVE-2026-119085) | Critical | 9.4 | Improper neutralization of special elements used in a template engine in the publishing component of Amazon Virtual Eng… |
| 2026-11-02 18:18:50 | [CVE-2026-120416](https://nvd.nist.gov/vuln/detail/CVE-2026-120416) | Medium | 6.9 | A security vulnerability has been detected in AndyFactory newspaper4k up to 0.9.6. This affects the function Article.pa… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
