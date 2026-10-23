# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-23 16:18 UTC

New CVEs published between 2026-10-23 15:18 UTC and 2026-10-23 16:18 UTC.

[Full CSV](data/new-cves-2026-10-23T16-18-47-197824Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-10-23 16:16:50 | [CVE-2025-45528](https://nvd.nist.gov/vuln/detail/CVE-2025-45528) |  |  | An issue in Nitro Software, Inc Nitro PDF Pro for macOS v.14.7 allows a local attacker to execute arbitrary code via a… |
| 2026-10-23 16:16:51 | [CVE-2026-50787](https://nvd.nist.gov/vuln/detail/CVE-2026-50787) |  |  | e-SIC Livre (esiclivre) v0.2.2 and earlier contains an uncontrolled resource consumption vulnerability in restrito/inc/… |
| 2026-10-23 16:16:51 | [CVE-2026-52356](https://nvd.nist.gov/vuln/detail/CVE-2026-52356) |  |  | An OS command injection vulnerability in the /htdocs/web/diagnostic.php endpoint of D-Link DAP1160L A1_FW101WWb04 allow… |
| 2026-10-23 16:16:52 | [CVE-2026-57845](https://nvd.nist.gov/vuln/detail/CVE-2026-57845) | High | 8.7 | Hugging Face Datasets through 5.1.0 contains an insecure deserialization vulnerability that allows attackers to execute… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
