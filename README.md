# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-09 17:18 UTC

New CVEs published between 2026-10-09 16:19 UTC and 2026-10-09 17:18 UTC.

[Full CSV](data/new-cves-2026-10-09T17-18-32-24688Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-10-09 17:16:38 | [CVE-2016-20098](https://nvd.nist.gov/vuln/detail/CVE-2016-20098) | Medium | 5.1 | Moderator Toolbox (reddit-moderator-toolbox) before 4.0.14 contains a stored cross-site scripting vulnerability in the… |
| 2026-10-09 17:16:41 | [CVE-2025-61560](https://nvd.nist.gov/vuln/detail/CVE-2025-61560) |  |  | A race condition vulnerability in the SessionManager of CNCF: Cloud Native Computing Foundation Argo CD v3.0.6 allows a… |
| 2026-10-09 17:16:45 | [CVE-2026-107815](https://nvd.nist.gov/vuln/detail/CVE-2026-107815) | High | 8.5 | MariaDB server is a community developed fork of MySQL server. From 10.6.1 until 10.6.28, 10.11.19, 11.4.13, 11.8.9, 12.… |
| 2026-10-09 17:16:46 | [CVE-2026-108093](https://nvd.nist.gov/vuln/detail/CVE-2026-108093) | Medium | 5.5 | A flaw was found in GIMP. The XCF loader processes image-simulation-intent and image-simulation-bpc parasites without e… |
| 2026-10-09 17:16:46 | [CVE-2026-108119](https://nvd.nist.gov/vuln/detail/CVE-2026-108119) | Medium | 6.3 | A flaw was found in busybox. The tar applet's deferred link-creation handling for symlink and hardlink entries with uns… |
| 2026-10-09 17:16:46 | [CVE-2026-108156](https://nvd.nist.gov/vuln/detail/CVE-2026-108156) | Medium | 6.9 | LobsterAI 2026.5.27 through 2026.9.23 contains an external control of file path vulnerability in the skills:delete IPC… |
| 2026-10-09 17:16:46 | [CVE-2026-108157](https://nvd.nist.gov/vuln/detail/CVE-2026-108157) | Critical | 9.2 | Pingvin Share X from 0.19.0 before 1.22.0 contains an improper authentication vulnerability that allows remote unauthen… |
| 2026-10-09 17:16:46 | [CVE-2026-108158](https://nvd.nist.gov/vuln/detail/CVE-2026-108158) | High | 7.1 | plugNmeet Server through 2.5.2 contains a path traversal vulnerability in the whiteboard conversion endpoint that allow… |
| 2026-10-09 17:16:47 | [CVE-2026-108159](https://nvd.nist.gov/vuln/detail/CVE-2026-108159) | High | 7.7 | AstronRPA through 1.1.6 contains a cross-site scripting vulnerability in the desktop client's smart-component chat that… |
| 2026-10-09 17:16:47 | [CVE-2026-108160](https://nvd.nist.gov/vuln/detail/CVE-2026-108160) | High | 7.7 | AstronRPA through 1.1.6 contains a download of code without integrity check vulnerability that allows network attackers… |
| 2026-10-09 17:16:47 | [CVE-2026-42695](https://nvd.nist.gov/vuln/detail/CVE-2026-42695) | Medium | 6.5 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in FolioVision FV Fl… |
| 2026-10-09 17:16:47 | [CVE-2026-48484](https://nvd.nist.gov/vuln/detail/CVE-2026-48484) | Medium | 6.5 | pyLoad is a free and open-source download manager written in Python. Prior to 0.5.0b3.dev101, the API `rpc` function in… |
| 2026-10-09 17:16:47 | [CVE-2026-55797](https://nvd.nist.gov/vuln/detail/CVE-2026-55797) | High | 8.8 | Argo CD is a declarative, GitOps continuous delivery tool for Kubernetes. From 2.11.0 until 3.3.15, 3.4.10, 3.5.4, and… |
| 2026-10-09 17:16:48 | [CVE-2026-75347](https://nvd.nist.gov/vuln/detail/CVE-2026-75347) | High | 7.5 | EIPStackGroup OpENer v2.3 and master up to commit 76b95cf contain an expired pointer dereference vulnerability in the E… |
| 2026-10-09 17:16:48 | [CVE-2026-75597](https://nvd.nist.gov/vuln/detail/CVE-2026-75597) | Medium | 5.3 | pyLoad is a free and open-source download manager written in Python. Prior to 0.5.0b3.dev101, the `/web/<path:filename>… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
