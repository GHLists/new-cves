# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-11-06 18:20 UTC

New CVEs published between 2026-11-06 17:20 UTC and 2026-11-06 18:20 UTC.

[Full CSV](data/new-cves-2026-11-06T18-20-16-792271Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-11-06 17:20:02 | [CVE-2026-85744](https://nvd.nist.gov/vuln/detail/CVE-2026-85744) | Medium | 5.4 | FreeScout is a self-hosted help desk and shared mailbox. Prior to 1.8.227, the conversation_merge action records a fail… |
| 2026-11-06 18:17:36 | [CVE-2026-102356](https://nvd.nist.gov/vuln/detail/CVE-2026-102356) | Medium | 5.0 | Kroki creates diagrams from textual descriptions. From 0.26.0 until 0.31.2, the optional Mermaid companion's mermaid/sr… |
| 2026-11-06 18:17:37 | [CVE-2026-102359](https://nvd.nist.gov/vuln/detail/CVE-2026-102359) | High | 7.5 | Kroki creates diagrams from textual descriptions. Prior to 0.31.2, the TikZ backend's tikz/tikz2svg guard used when KRO… |
| 2026-11-06 18:17:37 | [CVE-2026-102650](https://nvd.nist.gov/vuln/detail/CVE-2026-102650) | High | 7.5 | Nuxt Content is the file-based CMS for Nuxt applications, powered by Markdown and Vue components. From 3.0.0 until 3.15… |
| 2026-11-06 18:17:57 | [CVE-2026-118670](https://nvd.nist.gov/vuln/detail/CVE-2026-118670) | High | 8.8 | OHIF Viewers is a zero-footprint DICOM viewer with shared extension packages. From 3.5.0-beta.0 until 3.12.15, 3.13.7,… |
| 2026-11-06 18:17:58 | [CVE-2026-119758](https://nvd.nist.gov/vuln/detail/CVE-2026-119758) | High | 7.1 | ERPNext OCR app for Frappe/ERPNext through 1.1.1 contains a missing authorization and path traversal vulnerability that… |
| 2026-11-06 18:18:04 | [CVE-2026-123748](https://nvd.nist.gov/vuln/detail/CVE-2026-123748) | Medium | 5.3 | A security flaw has been discovered in chenyme grok2api up to 3.1.6. Affected by this vulnerability is the function pro… |
| 2026-11-06 18:18:05 | [CVE-2026-123824](https://nvd.nist.gov/vuln/detail/CVE-2026-123824) | Low | 2.3 | The Symfony Config component XmlUtils::parse() enables DTD validation before rejecting documents that carry a doctype,… |
| 2026-11-06 18:18:05 | [CVE-2026-123876](https://nvd.nist.gov/vuln/detail/CVE-2026-123876) | Medium | 4.4 | A flaw was found in the default seccomp profile used by Podman via containers-common. Deny rules for AF_VSOCK and NETLI… |
| 2026-11-06 18:18:05 | [CVE-2026-123973](https://nvd.nist.gov/vuln/detail/CVE-2026-123973) | Medium | 5.0 | SharePoint Products CopyMove before 2026-11-06 allows traversal. An authenticated SharePoint user with the necessary pe… |
| 2026-11-06 18:18:05 | [CVE-2026-123976](https://nvd.nist.gov/vuln/detail/CVE-2026-123976) | Medium | 6.8 | EDFbrowser before 2.16 contains an out-of-bounds write vulnerability in check_edf_file() that allows attackers to overf… |
| 2026-11-06 18:18:16 | [CVE-2026-62344](https://nvd.nist.gov/vuln/detail/CVE-2026-62344) | High | 7.5 | Wanderer is a self-hosted trail database for saving and sharing adventures. Prior to 0.19.3, the unauthenticated GET /a… |
| 2026-11-06 18:18:18 | [CVE-2026-75598](https://nvd.nist.gov/vuln/detail/CVE-2026-75598) | Medium | 6.3 | The Gradle Shadow plugin creates fat or uber JARs and supports file transformation and package relocation. Prior to ver… |
| 2026-11-06 18:18:21 | [CVE-2026-85742](https://nvd.nist.gov/vuln/detail/CVE-2026-85742) | High | 7.5 | FreeScout is a self-hosted help desk and shared mailbox. Prior to 1.8.230, a pre-authenticated attacker can place HTML… |
| 2026-11-06 18:18:22 | [CVE-2026-89017](https://nvd.nist.gov/vuln/detail/CVE-2026-89017) | High | 8.7 | Skyline DataMiner BrokerGateway contains an embedded API key vulnerability that allows unauthenticated attackers to ret… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
