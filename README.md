# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-23 19:18 UTC

New CVEs published between 2026-10-23 18:19 UTC and 2026-10-23 19:18 UTC.

[Full CSV](data/new-cves-2026-10-23T19-18-41-135508Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-10-23 19:17:43 | [CVE-2026-112342](https://nvd.nist.gov/vuln/detail/CVE-2026-112342) | High | 7.1 | Tandoor Recipes before 2.7.0 contains an improper cache-key design in cookbook/helper/permission_helper.py that allows… |
| 2026-10-23 19:17:44 | [CVE-2026-115569](https://nvd.nist.gov/vuln/detail/CVE-2026-115569) | Low | 3.3 | Fallow is a codebase intelligence tool for TypeScript and JavaScript. From 2.68.0 until 3.34.0, Fallow follows attacker… |
| 2026-10-23 19:17:44 | [CVE-2026-115570](https://nvd.nist.gov/vuln/detail/CVE-2026-115570) | High | 7.4 | Electron is a framework for writing cross-platform desktop applications using JavaScript, HTML and CSS. Prior to 42.11.… |
| 2026-10-23 19:17:44 | [CVE-2026-115845](https://nvd.nist.gov/vuln/detail/CVE-2026-115845) | Medium | 5.3 | An incomplete list of disallowed inputs in the Python code validator of the run_script tool in AWS MCP Server might all… |
| 2026-10-23 19:17:45 | [CVE-2026-91093](https://nvd.nist.gov/vuln/detail/CVE-2026-91093) | High | 8.5 | A potential security vulnerability has been identified in HP One Agent for certain HP PC products, which might allow fo… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
