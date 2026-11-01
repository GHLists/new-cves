# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-11-01 16:18 UTC

New CVEs published between 2026-11-01 15:18 UTC and 2026-11-01 16:18 UTC.

[Full CSV](data/new-cves-2026-11-01T16-18-54-365464Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-11-01 16:18:13 | [CVE-2026-119480](https://nvd.nist.gov/vuln/detail/CVE-2026-119480) | Medium | 6.5 | Improper Limitation of a Pathname to a Restricted Directory ('Path Traversal') vulnerability in Crocoblock JetFormBuild… |
| 2026-11-01 16:18:14 | [CVE-2026-120233](https://nvd.nist.gov/vuln/detail/CVE-2026-120233) | Medium | 5.5 | A security flaw has been discovered in ag-ui-protocol ag-ui up to 0.0.58. This affects an unknown function of the file… |
| 2026-11-01 16:18:14 | [CVE-2026-120234](https://nvd.nist.gov/vuln/detail/CVE-2026-120234) | Low | 2.1 | A weakness has been identified in ag-ui-protocol ag-ui up to 0.0.58. This impacts the function e.text of the component… |
| 2026-11-01 16:18:14 | [CVE-2026-120235](https://nvd.nist.gov/vuln/detail/CVE-2026-120235) | Low | 2.1 | A security vulnerability has been detected in ag-ui-protocol ag-ui up to 0.0.58. Affected is the function parseSSEStrea… |
| 2026-11-01 16:18:14 | [CVE-2026-120338](https://nvd.nist.gov/vuln/detail/CVE-2026-120338) | Critical | 10.0 | Prefab UI's Generative UI sandbox runs caller-supplied Python inside Pyodide, Python compiled to WebAssembly, in a Deno… |
| 2026-11-01 16:18:15 | [CVE-2026-62048](https://nvd.nist.gov/vuln/detail/CVE-2026-62048) | Critical | 9.3 | Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection') vulnerability in Liquid Web / Stel… |
| 2026-11-01 16:18:15 | [CVE-2026-66570](https://nvd.nist.gov/vuln/detail/CVE-2026-66570) | High | 7.1 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in Nickboss WordPres… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
