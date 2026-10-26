# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-26 19:21 UTC

New CVEs published between 2026-10-26 18:19 UTC and 2026-10-26 19:21 UTC.

[Full CSV](data/new-cves-2026-10-26T19-21-28-392737Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-10-26 19:16:28 | [CVE-2026-104591](https://nvd.nist.gov/vuln/detail/CVE-2026-104591) |  |  | libosmocore through 1.14.1 contains a buffer overflow in osmo_iuup_compute_payload_crc() in src/gsm/iuup.c. This allows… |
| 2026-10-26 19:16:28 | [CVE-2026-104592](https://nvd.nist.gov/vuln/detail/CVE-2026-104592) |  |  | libosmocore through 1.14.1 contains an out-of-bounds read in the CBSP WRITE-REPLACE decoder in src/gsm/cbsp.c. This all… |
| 2026-10-26 19:16:28 | [CVE-2026-104593](https://nvd.nist.gov/vuln/detail/CVE-2026-104593) |  |  | osmo-msc through 1.15.0 contains a stack-based buffer overflow in decode_mme_name() in src/libmsc/sgs_iface.c. This all… |
| 2026-10-26 19:16:28 | [CVE-2026-104594](https://nvd.nist.gov/vuln/detail/CVE-2026-104594) |  |  | libosmocore through 1.14.1 contains out-of-bounds reads in the IPA CCM identity-tag parsers in src/gsm/ipa.c. This allo… |
| 2026-10-26 19:16:29 | [CVE-2026-110720](https://nvd.nist.gov/vuln/detail/CVE-2026-110720) | Critical | 9.9 | Consul-k8s versions 0.42.0 and later are vulnerable to a cross-namespace authorization bypass in component ACL binding… |
| 2026-10-26 19:16:30 | [CVE-2026-116467](https://nvd.nist.gov/vuln/detail/CVE-2026-116467) | Medium | 6.9 | A security flaw has been discovered in ggml-org llama.cpp up to 0.7.0. Affected by this vulnerability is an unknown fun… |
| 2026-10-26 19:16:30 | [CVE-2026-116471](https://nvd.nist.gov/vuln/detail/CVE-2026-116471) | Low | 2.1 | A security flaw has been discovered in BKWLD Decoy up to 5.11.1. The impacted element is an unknown function of the fil… |
| 2026-10-26 19:16:30 | [CVE-2026-116476](https://nvd.nist.gov/vuln/detail/CVE-2026-116476) | Medium | 5.3 | A weakness has been identified in a2aproject a2a-dotnet up to 1.0.0-preview3. The affected element is the function Task… |
| 2026-10-26 19:16:30 | [CVE-2026-116631](https://nvd.nist.gov/vuln/detail/CVE-2026-116631) | Medium | 5.4 | A malicious web page could open a tel link in a window that was showing a different website, causing the phone-call pro… |
| 2026-10-26 19:16:30 | [CVE-2026-116632](https://nvd.nist.gov/vuln/detail/CVE-2026-116632) | Medium | 5.4 | A malicious web page could insert arbitrary text into the FaceTime call prompt shown by iOS, potentialy allowing it to… |
| 2026-10-26 19:16:31 | [CVE-2026-116638](https://nvd.nist.gov/vuln/detail/CVE-2026-116638) |  |  | The Windows Recovery Environment (WinRE) in Windows 10 and 11 may allow an attacker to bypass firmware security control… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
