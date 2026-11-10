# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-11-10 13:21 UTC

New CVEs published between 2026-11-10 12:20 UTC and 2026-11-10 13:21 UTC.

[Full CSV](data/new-cves-2026-11-10T13-21-42-497404Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-11-10 13:18:18 | [CVE-2026-100962](https://nvd.nist.gov/vuln/detail/CVE-2026-100962) | Medium | 5.3 | NVIDIA NeMo Export-Deploy for all platforms contains a vulnerability in multimodal deployment where an attacker could c… |
| 2026-11-10 13:18:22 | [CVE-2026-121267](https://nvd.nist.gov/vuln/detail/CVE-2026-121267) | High | 7.8 | Incorrect default permissions vulnerability in TÜBİTAK BİLGEM Software Technologies Research Institute eta-remote allow… |
| 2026-11-10 13:18:22 | [CVE-2026-124747](https://nvd.nist.gov/vuln/detail/CVE-2026-124747) | High | 7.5 | A flaw was found in BusyBox. When resuming a download over File Transfer Protocol (FTP), the wget utility fails to veri… |
| 2026-11-10 13:18:22 | [CVE-2026-125744](https://nvd.nist.gov/vuln/detail/CVE-2026-125744) | Low | 1.2 | Our API endpoint for changing ticket layouts did not properly check permissions of the requesting user or API token. An… |
| 2026-11-10 13:18:23 | [CVE-2026-125745](https://nvd.nist.gov/vuln/detail/CVE-2026-125745) | Low | 2.3 | Custom Post Types and Custom Fields creator (WCK) before 2.4.1 contains a missing authorization vulnerability that allo… |
| 2026-11-10 13:18:23 | [CVE-2026-125871](https://nvd.nist.gov/vuln/detail/CVE-2026-125871) | Medium | 6.3 | The sourcecache expansion module in MISP Modules (misp-modules) contains a Server-Side Request Forgery (SSRF) vulnerabi… |
| 2026-11-10 13:18:29 | [CVE-2026-16478](https://nvd.nist.gov/vuln/detail/CVE-2026-16478) | High | 7.0 | Permissive list of allowed inputs vulnerability in TÜBİTAK BİLGEM Software Technologies Research Institute pardus-nvidi… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
